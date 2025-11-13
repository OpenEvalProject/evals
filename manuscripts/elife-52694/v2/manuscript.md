# Opioids depress breathing through two small brainstem sites

## Authors

- Iris Bachmutsky<sup>1</sup>
- Xin Paul Wei<sup>1</sup>
- Eszter Kish<sup>1</sup>
- Kevin Yackle<sup>1</sup> ([ORCID: 0000-0003-1870-2759](https://orcid.org/0000-0003-1870-2759)) †

### Affiliations

1. Department of Physiology, University of California-San Francisco San Francisco United States
2. Neuroscience Graduate Program, University of California-San Francisco San Francisco United States
3. Biomedical Sciences Graduate Program, University of California-San Francisco San Francisco United States

† Corresponding author

## Abstract

The rates of opioid overdose in the United States quadrupled between 1999 and 2017, reaching a staggering 130 deaths per day. This health epidemic demands innovative solutions that require uncovering the key brain areas and cell types mediating the cause of overdose— opioid-induced respiratory depression. Here, we identify two primary changes to murine breathing after administering opioids. These changes implicate the brainstem’s breathing circuitry which we confirm by locally eliminating the µ-Opioid receptor. We find the critical brain site is the preBötzinger Complex, where the breathing rhythm originates, and use genetic tools to reveal that just 70–140 neurons in this region are responsible for its sensitivity to opioids. Future characterization of these neurons may lead to novel therapies that prevent respiratory depression while sparing analgesia.

## Introduction

Nearly 400,000 people in the United States died from a drug overdose involving a prescription or illicit opioid between 1999 and 2017 (Scholl et al., 2018). This epidemic is not unique to the United States and with the increasing distribution of highly potent synthetic opioids like fentanyl, it has become a global public health emergency (Rudd et al., 2016). Death from opioid overdose results from slow and shallow breathing, also known as opioid induced respiratory depression (OIRD, Pattinson, 2008). Like humans, breathing in mice is severely depressed by opioids and this response is eliminated when the µ-Opioid receptor (Oprm1) is globally deleted (Dahan et al., 2001). Oprm1 is broadly expressed, in both the central and peripheral nervous systems, including sites that could modulate breathing such as: the cerebral cortex, brainstem respiratory control centers, primary motor neurons, solitary nucleus, and oxygen sensing afferents (Mansour et al., 1994; Kirby and McQueen, 1986). Therefore, either one or multiple sites could be mediating the depressive effects of opioids on breathing.

Indeed, multiple brain regions have been shown to independently slow breathing after local injection of opioid agonists (Kirby and McQueen, 1986; Montandon et al., 2011; Mustapic et al., 2010; Prkic et al., 2012). Although informative, doubts remain for which of these sites are necessary and sufficient to induce OIRD from systemic opioids for three reasons. First, injection of opioid agonists or antagonists into candidate areas modulates µ-opioid receptors on the cell body (post-synaptic) as well as receptors on incoming terminals (pre-synaptic). Second, these studies necessitate anesthetized and reduced animal preparations, which alter brain activity in many of the candidate Oprm1 expressing sites. And third, there is not a standard and quantitative definition for how breathing changes in OIRD, and this makes comparing studies that use different breathing metrics measured in different experimental paradigms challenging.

To address these limitations, we conducted a detailed quantitative analysis of OIRD in awake animals and identify two key changes to the breath that drive the depressive effects of opioids. These two metrics thereafter define OIRD in our study and can serve as a rubric for others. We then locally eliminate the µ-opioid receptor in awake mice, disambiguating pre and post-synaptic effects, and use these metrics to define two key brain sites that mediate OIRD. Recently, a similar approach demonstrated some role for these sites in OIRD (Varga et al., 2020). Among these two sites in our study, we find that one is dominant and driven by just 140 critical neurons in vitro and, importantly, these neurons are not required for opioid-induced analgesia, suggesting a neutral target for developing safer opioids or rescue strategies for opioid overdose.

## Results

Up to now, OIRD has generally been described as a slowing and shallowing of breath (Pattinson, 2008). We therefore felt it was important to more precisely, quantitatively describe the changes in breathing in hopes of elucidating potential mechanisms of respiratory depression. We began by asking whether specific parameters of the breath are affected by opioids. We monitored breathing in awake, behaving mice by whole body plethysmography after intraperitoneal injection (IP) of saline for control and then 20 mg/kg morphine at least 24 hr later (Figure 1A). Compared to saline, breathing after morphine administration (in normoxia) became much slower and inspiratory airflow decreased, each by 60% (Figure 1B,C). This culminated in ~50% decrease in overall minute ventilation (MV = approximated tidal volume x respiratory rate, Figure 1C), demonstrating that 20 mg/kg morphine is, indeed, a suitable dose to model OIRD.

![Figure 1.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig1-v2.jpg)

**Figure 1.:** (A) Representative examples of the breathing airflow (mL/sec.) in normoxia (21% O2) measured by whole body plethysmography. 15 min before recordings, animals are intraperitoneally (IP) injected with either saline (black) or 20 mg/kg morphine (red). Morphine recordings are captured 1–7 days after saline. (B) Scatterplot of instantaneous breathing rate (Hz) versus airflow (mL/sec.) for each breath (dot) taken during the 40 min recordings. Morphine causes breathing to become slow and less forceful. (C) Ratio of average breathing parameters after IP injection of morphine-to-saline. Respiratory rate, peak inspiratory airflow, and minute ventilation (MV = approximated tidal volume*rate) for n = 29 animals in normoxia. Red diamond, single animal average. Black diamond, average of all animals. Error bar, standard error of mean (SEM). (D–E) Representative example of breathing airflow and instantaneous scatter plot (rate vs. airflow) from a 10 min whole body plethysmography recording of breathing in hypercapnia (21% O2, 5% CO2) to minimize changes in breathing due to differences in behavior after morphine injection. (F) Ratio of respiratory rate (p-value=1×10−19, Cohen’s d = 5.96), peak inspiratory airflow (p-value=1×10−22, Cohen’s d = 6.18), and minute ventilation (p-value=1×10−20, Cohen’s d = 5.31) after IP injection of morphine-to-saline for n = 29 animals in hypercapnia. (G) Representative single breath airflow trace for breaths in hypercapnia after saline (black) or morphine (red) IP injection. Hypercapnic saline breaths can be divided into two phases whose durations (msec.) can be measured: inspiration (Ti) and expiration (Te). Hypercapnic morphine breaths have a third phase after expiration where airflow is nearly 0 mL/sec., which we call a pause. (H) Bar graph of the average length ± standard deviation of Ti and Te for a single representative animal. (I) Probability density function plot of the pause length in breathing during hypercapnia after saline (black) or morphine (red) IP injection on a numerical (left) and logarithmic scale (right). Note, morphine selectively increases Ti and pause length. (J) Percent of the average breath period spent in inspiration, expiration, or pause for hypercapnic breaths after saline or morphine injection. (K) Scatterplot of inspiratory time (msec.) vs. peak inspiratory airflow (mL/sec.) for 10 min of hypercapnic breaths after saline (black) or morphine (red) IP injection. As inspiratory time increases, peak inspiratory flow decreases. (L) Scatterplot of tidal volume (µL.) vs. peak inspiratory airflow (mL/sec.) for 10 min of hypercapnic breaths after saline (black) or morphine (red) IP injection. Even though peak inspiratory airflow decreases after morphine, tidal volume is preserved due to prolonged Ti. (M) Ratio of tidal volume after IP injection of morphine-to-saline for n = 29 animals in hypercapnia (p-value=3×10−6, Cohen’s d = 1.13). (N) Schematic of the two key morphine induced changes to the breath: decreased inspiratory airflow and pause. Decreased inspiratory airflow prolongs Ti since negative feedback from the lung reflecting breath volume is slower. We interpret the pause as a delay in initiation of the subsequent inspiration.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Example breaths binned by pause length (from left to right: 0–50, 50–100, 100–200, and 200-300msec.) from a control animal breathing in hypercapnia after intraperitoneal injection of 20 mg/kg morphine. All breaths are aligned at the onset of the pause (vertical dashed black lines). Note that for longer pauses, the airflow is nearly 0 (dashed blue line) for tens to hundreds of milliseconds and then ends in an increased expiratory airflow, likely active expiration induced by hypercapnia.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Scatterplots of 100 individual breaths (dots) from n = 15 animals and the line of best fit (dashed line) where the expiratory length (msec.) of breaths is calculated with or without a pause. The different colors represent various airflow thresholds (mL/sec.) where the pause is initiated (black: no threshold, gray: 0 mL/sec., red: 0.5 mL/sec., green: 1 mL/sec., blue: 1.5 mL/sec.). Under hypercapnia conditions after intraperitoneal saline injection (left), at a pause threshold of 0.5 mL/sec. less than 2% of all breaths had a pause defined greater than 5msec. However, after 20 mg/kg morphine in hypercapnia, 40% of breaths had a pause greater than 5msec. At a threshold of 0.5 mL/sec., since most breaths (>98%) under baseline conditions do not have any pause, this threshold was conservatively chosen for our analysis.

Breath morphology in normoxia after IP saline versus morphine cannot be directly compared since activity of the mouse is different (exploring vs. sedated, Supplementary file 1), which significantly influences the types of breaths taken. This prevented a precise characterization of breath parameters that dictate OIRD. To overcome this, we measured breathing in hypercapnic air (21% O2, 5% CO2) which normalizes behavior and thus breathing (Figure 1D, Supplementary file 1). As in normoxia, morphine depressed respiratory rate (by 50%, Figure 1E,F), peak inspiratory airflow (by 60%, Figure 1E,F), and minute ventilation (by 60%, Figure 1F). Hypercapnic breaths after saline exhibited two phases, inspiration and expiration, each lasting about 50 msec. (Figure 1G,H). After morphine, only the inspiratory phase (measured as inspiratory time, Ti) became substantially longer (Figure 1G,H). Additionally, hypercapnic breaths showed a new, third phase after the initial expiration (measured as expiratory time, Te, Figure 1G,H) that was characterized by prolonged little to no airflow (<0.5 mL/sec.) preceding hypercapnia induced active expiration (Pisanski and Pagliardini, 2019). We define this new phase as a pause (low airflow + active expiration, Figure 1G, Figure 1—figure supplement 1). Such pauses lasted up to several hundred milliseconds (Figure 1I), accounting for about one-third of the average breath length (Figure 1J). Thus, the 50% decrease in respiratory rate after morphine administration is primarily due to prolonging of Ti and pause phases, and the increased prevalence of time spent in pause significantly contributes to the decrease in minute ventilation.

Typically the length of inspiratory time is determined by a stretch-evoked feedback signal from the lung which terminates inspiration (West, 2005). This reflex is represented by the correlation observed between Ti and peak inspiratory airflow (Figure 1K). Breaths in morphine still maintain this correlation despite having a longer Ti and decreased inspiratory airflow (Figure 1K). As a result, morphine breaths have a similar approximated tidal volume (TV) compared to saline control (Figure 1L,M). In other words, as opioids decrease inspiratory airflow, Ti displays a compensatory increase to preserve TV (Figures 1N and Hill et al., 2018). In summary, opioids cause only two primary changes to the breath, namely, 1) decreased inspiratory airflow and 2) addition of a pause phase that delays initiation of subsequent breaths (Figure 1N). These two parameters can both be controlled by the breathing central pattern generator, the preBötzinger Complex (preBötC), in the brainstem and suggest that this may be a key locus affected during OIRD (Smith et al., 1991; Feldman et al., 2013; Cui et al., 2016).

Indeed, the preBötC has been proposed to play a key role in OIRD since localized injection of opioids results in respiratory depression and localized naloxone reverses decreased breathing after administration of systemic opioids (Montandon et al., 2011; Montandon and Horner, 2014). However, such experiments fail to distinguish between the action of opioids on presynaptic terminals (Mudge et al., 1979) of distant neurons projecting into the preBötC versus direct action on preBötC neurons themselves (Figure 2A; Montandon et al., 2011; Dobbins and Feldman, 1994; Gray et al., 1999) To overcome this, we genetically eliminated the µ-Opioid receptor (Oprm1) from preBötC cells exclusively, sparing projecting inputs, by stereotaxic injection of adeno-associated virus constitutively expressing Cre (AAV-Cre-GFP) into the preBötC of Oprm1 flox/flox (Oprm1f/f) adult mice (Figure 2B). Injection site specificity was confirmed by the restricted expression of Cre-GFP (Figure 2—figure supplement 1), and subsequent Oprm1 deletion, was inferred. To establish a baseline, we first measured breathing after administration of saline and morphine in normoxia and hypercapnia in intact animals, as described above. At least one month after bilateral injection of virus into the preBötC, we then re-analyzed breathing (Figure 2C). With this protocol, each animal’s unique breathing and OIRD response serves as its own internal control, which is necessary due to the variability in OIRD severity between mice (Figure 1F). Deletion of Oprm1 in the preBötC did not affect breathing observed after saline injection (Figure 2D,E), suggesting that in this context, opioids do not exert an endogenous effect. In contrast, breathing was markedly less depressed by morphine administration (Figure 2D,E) compared to the intact control state: breaths were twice as fast (3 to 6 Hz, Figure 2F,H), the peak inspiratory flow was larger (Figure 2F,I), and pauses were nearly eliminated (Figure 2G,J). Notably, histological analysis confirmed that AAV-Cre-GFP expression was localized to the preBötC (Figure 2—figure supplement 1), and AAV-GFP or tdTomato injected control mice without removal of Oprm1 showed no change in OIRD compared to the pre-injected control state (Figure 2H–J), demonstrating that animals do not develop tolerance to opioids within our experimental timeline. Importantly, rescue of OIRD similarly occurred in normoxia (Figure 2—figure supplement 2) and was also specific to breathing since opioids induced analgesia in tail-flick assay after deletion of Oprm1 in the preBötC (Figure 2—figure supplement 3).

![Figure 2.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig2-v2.jpg)

**Figure 2.:** (A) Schematic of a sagittal section through the adult mouse brain. The µ-Opioid receptor (Oprm1) is expressed by a subset of preBötC neurons and is also expressed on presynaptic terminals of some neurons projecting to the preBötC. This confounds the effects observed after localized preBötC injection of opioid or naloxone to investigate its role in OIRD. (B) To overcome this, we eliminate Oprm1 only from the preBötC, and not the presynaptic inputs, to define the role of preBötC neurons in OIRD. (C) Experimental time-course. Breathing is measured 15 min after IP injection of saline or 20 mg/kg morphine in both normoxia and hypercapnia. Then Oprm1f/f animals are injected with a constitutive-Cre AAV into the preBötC bilaterally. After several weeks breathing is assayed again as above. In this way, each animal’s breathing before viral injection can serve as its own control breathing. Response to pain is also measured with a tail-flick assay before and after viral injection to ensure that analgesic response is unaffected. (D–E) Representative examples of the breathing airflow (mL/sec.) in hypercapnia after saline (black) or morphine (red) before (D) and after (E) Cre-virus injection. (F) Scatter plot of instantaneous respiratory frequency vs. airflow (ml/sec), as well as probability density function plots of both parameters for a representative animal during hypercapnia after saline (black) or morphine (red, blue) IP injection, before (red) and after (blue) Cre-injection. (G) Probability density function plot of pause length (msec.) for a representative animal during hypercapnia after IP morphine before (red) and after (blue) Cre-injection, log scale. Prevalence of long duration pauses is greatly reduced. (H–J) Ratio of average breathing parameters after IP injection of morphine-to-saline. Respiratory rate (H) p-value=0.003, Cohen’s d = 3.0), peak inspiratory airflow (I) p-value=0.0005, Cohen’s d = 3.01), and pause length (J) p-value=0.04, Cohen’s d = 2.0) for 6 Oprm1f/f animals with Cre-virus injected into the preBötC or 7 control animals with reporter-virus injected into the preBötC. All sham p-values were not significant (>0.09) and Cohen’s D < 0.6. For each experiment ‘intact’ values are before viral injection, with ‘deleted’ and ‘sham’ values representing post viral injection conditions in experimental and control animals, respectively. Diamond and square, single animal average. Mixed repeated two-way ANOVA comparing Cre vs. Sham injected was statistically significant for respiratory rate (F(1,11)=5.5, p-value=0.04) and pause (F(1,11)=6.2, p-value=0.03), but not for peak inspiratory airflow (F(1,11)=2.1, p-value=0.17) Black diamond, average of all animals. Error bar, standard error of mean (SEM). * indicates p-value<0.05. ns indicates p-value>0.05.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) GFP protein (green) and Somatostatin neuropeptide (red) expression in a 25 µM coronal section of the brainstem from an adult Oprm1f/f mouse injected bilaterally with AAV-Cre-GFP into the preBötC. Somatostatin expression demarcates the preBötC (dashed white circles, 43). This validates the specific targeting of AAV-Cre, and thus Oprm1 deletion, to the preBötC. (B) Schematic of three serial coronal sections of the mouse brain from most anterior (left) to posterior (right) that cover the preBötC injection sites visualized by AAV-Cre-GFP expression (example in A). The extend of GFP expression for each injection site is highlighted by the green annotations in B) and the representative example in A) (green dashed line). Note that overlap of all injection sites colocalizes with the preBötC (black solid line).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** The same animals in Figure 2 were also assayed for OIRD under normoxic instead of hypercapnic conditions. Briefly, breathing is measured 15 min after IP injection of 20 mg/kg morphine in normoxia, animals are injected with a constitutive-Cre AAV into the preBötC bilaterally, and after several weeks re-assayed as above. (A–B) A representative probability density function of respiratory rate (A) and peak inspiratory airflow (ml/sec, (B) of all breaths taken during the 40 min assay while in normoxia after intraperitoneal injection of 20 mg/kg morphine before (red) and after (blue) AAV-Cre injection. The increased respiratory rate and peak inspiratory airflow after bilateral preBötC AAV-Cre injection indicates that the rescue of OIRD observed in hypercapnia also occurs in normoxia.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** The tail flick response time was measured 15 min after IP saline (gray) or 20 mg/kg morphine (red) injection. Each animal was assayed twice before (Pre-) and twice after (Pst-) bilateral AAV-Cre-GFP injection into either the preBötC or PBN/KF of adult Oprm1f/f mice. Dot, time for single assay of one animal. Note, Oprm1 in the preBötC and PBN/KF is not required for morphine’s ability to blunt the tail flick response.

Although key features of OIRD (inspiratory airflow and pause) were attenuated by preBötC AAV-Cre injection, rescue was incomplete. This could be explained by incomplete Oprm1 deletion within the preBötC, or participation of another brain site in OIRD. Injection of opioids into the parabrachial (PBN)/Kolliker-Fuse (KF) nucleus can also slow breathing, making it a candidate second site (Mustapic et al., 2010; Prkic et al., 2012). In fact, the PBN/KF has been proposed to be the key site mediating OIRD (Eguchi et al., 1987; Lalley et al., 2014). We therefore took a similar approach to test the role of the PBN/KF in OIRD (Figure 3A). AAV-Cre injection into the PBN/KF (Figure 3—figure supplement 1) produced a slight increase in the morphine-evoked respiratory rate (Figure 3—figure supplement 2, Figure 3D,E) and inspiratory airflow (Figure 3—figure supplement 2, Figure 3F,G), but had a more moderate effect than injection into the preBötC.

![Figure 3.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig3-v2.jpg)

**Figure 3.:** (A) Schematic of a sagittal section through the adult mouse brain showing Cre-viral injection into the preBötC and PBN/KF to measure their individual and combined contribution to OIRD. (B) Like Figure 2, breathing was assayed before and after each time Cre-virus was injected into Oprm1f/f mice. In cohort 1, Cre-virus was first injected into the preBötC and then the PBN/KF and in cohort 2, Cre-virus was injected into the PBN/KF and then preBötC. (C) Representative examples of the breathing airflow (mL/sec.) in hypercapnia for an animal in cohort 1 after saline (black) or morphine (red) before either viral injection and after both preBötC and PBN/KF Cre-virus injections. (D–E) Probability density function plot of the instantaneous respiratory frequency for a representative animal from cohorts 1 and 2 (D) and ratio of average rate (E) after IP injection of morphine-to-saline for 6 animals in cohort 1 and 4 animals in cohort 2 before (pre) and after each Cre-virus injection into the preBötC (blue) or PBN/KF (green). Among the 2 cohorts, n = 6 PBN/KF injections were bilateral and n = 4 mostly unilateral. Cohort 1: preBötC vs. double p-value=0.07, Cohen’s d = 0.70. Cohort 2: PBN/KF vs. double p-value=0.1, Cohen’s d = 0.76. (F–G) Probability density function plot of the peak inspiratory airflow for a representative animal from cohorts 1 and 2 (F) and ratio of average peak inspiratory airflow (G) after IP injection of morphine-to-saline before (pre) and after each Cre-virus injection into the preBötC (blue) or PBN/KF (green). preBötC Cre-injection has a larger magnitude rescue and after preBötC and PBN/KF injections animals barely have any OIRD phenotype. Cohort 1: preBötC vs. double p-value=0.85, Cohen’s d = 0.10. Cohort 2: PBN/KF vs. double p-value=0.03, Cohen’s d = 1.32. (H–I) Representative plethysmography traces in normoxia from a control Oprm1f/f mouse (N) or a double Cre-injected Oprm1f/f mouse (preBötC and PBN/KF, (O) after IP injection of 150 mg/kg fentanyl. * indicates p-value<0.05. ns indicates p-value>0.05.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Schematic of a coronal section through the brainstem at the position of the PBN/KF. The PBN/KF is in the dorsal brainstem near the cerebellar peduncle. Half the brain is represented here. (B) GFP protein (green) expression in a 25 µM coronal section of the brainstem from an adult Oprm1f/f mouse injected bilaterally with AAV-Cre-GFP into the PBN/KF. This anatomical localization of GFP validates the specific targeting of AAV-Cre, and thus Oprm1 deletion, to the PBN/KF. (C) Schematic of two serial coronal sections of the mouse brain from most anterior (left) to posterior (right) that cover the PBN/KF injection sites visualized by AAV-Cre-GFP expression (example in B). The extend of GFP expression for each injection site is highlighted by the green annotations in C), and the representative example in B) (green dashed line). Note that overlap of all injection sites contains the KF (black solid line).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Schematic of a sagittal section through the adult mouse brain. Oprm1 is expressed by neurons within the pontine Parabrachial/Kolliker Fuse (PBN/KF) which has modulatory input into the preBötC (Chamberlin and Saper, 1994; Alheid et al., 2004) and is a proposed region for respiratory depression during OIRD (Smith et al., 1991; Feldman et al., 2013). As in Figure 2, breathing was assayed before and after Cre-virus injection into the PBN/KF of Oprm1f/f mice. (B) Representative examples of the breathing airflow (mL/sec.) in hypercapnia after saline (black) or morphine (red) before and after Cre-virus injection. (C–D) Probability density function plot of the instantaneous respiratory frequency for a representative animal (C) and ratio of average rate (D) p-value=0.4, Cohen’s d = 0.62) after IP injection of morphine-to-saline for 3 animals before (pre) and after (post) Cre-virus injection into the PBN/KF. (E–F) Probability density function plot of the peak inspiratory airflow for a representative animal (E) and ratio of average peak inspiratory airflow (F) p-value=0.02, Cohen’s d = 1.68) after IP injection of morphine-to-saline for 3 animals before (pre) and after (post) Cre-virus injection into the PBN/KF. * indicates p-value<0.05. ns indicates p-value>0.05.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** The same animals in Figure 3 were also assayed for OIRD under normoxic instead of hypercapnic conditions. Breathing is measured 15 min after IP injection of 20 mg/kg morphine in normoxia before, several weeks after animals are injected with a constitutive-Cre AAV into the preBötC or PBN/KF bilaterally, and then after the complementary brain site is injected. (A–B) A representative probability density function of respiratory rate (A) and peak inspiratory airflow (ml/sec, (B) of all breaths taken during the 40 min assay while in normoxia after intraperitoneal injection of 20 mg/kg morphine before (red), after AAV-Cre injection into the preBötC (blue), and after AAV-Cre injection into the PBN/KF (yellow). Note the slight increase in respiratory rate and peak inspiratory airflow after bilateral PBN/KF AAV-Cre injection is consistent with data collected in hypercapnia and indicates that the preBötC is the dominant site.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** (A) Schematic of a coronal section through the brainstem at the position of the PBN/KF. The PBN/KF is in the dorsal brainstem near the cerebellar peduncle. Half the brain is represented here. (B) GFP protein (green) expression in a 25 µM coronal section of the brainstem from an adult Oprm1f/f mouse injected bilaterally with AAV-Cre-GFP into the PBN/KF. In this instance, GFP expression is robustly seen on right side and few cells are labeled on the left. This localization of GFP suggests targeting of AAV-Cre, and thus Oprm1 deletion, is only in to one PBN/KF.

To determine if the preBötC and PBN/KF can completely account for OIRD (Figure 3A), we genetically deleted Oprm1 from the preBötC and then from the PBN/KF (Cohort 1) or vice versa (Cohort 2, Figure 3B). In either cohort, double deletion breathing after morphine administration looked nearly identical to that of saline control animals (Figure 3C), with breathing rate and inspiratory airflow depressed by only ~20% compared to saline (Figure 3D–G). Moreover, changes in breathing after viral injection at the second site appeared additive (Figure 3D–G) and equivalent to individual preBötC (Figure 2) or PBN/KF (Figure 3—figure supplement 2, Figure 3D–G) effects for each cognate cohort. The double deletion OIRD rescue was similar in normoxia (Figure 3—figure supplement 3). To our surprise, rescues also occurred in animals which happened to have mostly unilateral PBN/KF AAV-cre transduction (Figure 3—figure supplement 4), therefore these animals were still included in our double deletion analysis (Figure 3E,G). Breathing in double-deleted animals was even resilient to super-saturating doses of opioid that severely slow breathing in control animals (150 mg/kg fentanyl, Figure 3H,I). Taken together, our data are consistent with a model in which both the preBötC and PBN/KF contribute to opioid respiratory depression, with the former being predominant, and together account for OIRD.

Given the relative importance of the preBötC to OIRD, we sought to identify which Oprm1 expressing cells within this region depress breathing. Single cell transcriptome profiling of the ventral lateral brainstem of P0 mice (Figure 4A) showed that Oprm1 (mRNA) is expressed almost exclusively by neurons (Figure 4—figure supplement 1) and is remarkably restricted to just 8% of presumed preBötC neurons (Figure 4B). This alone is interesting, as it suggests that modulation of only a small subset of neurons with the preBötC is enough to significantly impact its ability to generate a rhythm. We also determined that within the preBötC, Oprm1 (mRNA) was expressed by glycinergic (Slc6a5 expressing), gabaergic (Gad2/Slc32a1 expressing), and glutamatergic (Slc17a6 expressing) neural types alike (Figure 4C) and therefore Oprm1 (mRNA) expression is not exclusive to any known rhythmogenic preBötC subpopulation.

![Figure 4.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig4-v2.jpg)

**Figure 4.:** (A) Schematic of single-cell mRNA sequencing paradigm. Postnatal day 0 (P0) medullary brainstem slices containing the preBötC bilaterally (circled in red) were dissected and isolated for sequencing. (B), Single cell transcriptome profiling of cells isolated from P0 preBötC. Of 1817 cells isolated, only 267 were presumed preBötC neurons of which only 21 expressed Oprm1 mRNA. (C), Heatmap of scaled transcript abundance for Oprm1 and markers of glutamatergic, gabaergic, and glycinergic preBötC neurons. Oprm1 expressing cells are both excitatory and inhibitory. (D), Schematic of extracellular recordings of the preBötC rhythm in P0-4 medullary brainstem slices. The preBötC has input to the hypoglossal motor neurons which form the CN12 rootlet, relaying an inspiratory motor command to the tongue in intact animals. Due to its input from the preBötC, extracellular recording from this rootlet display autonomous rhythmic activity corresponding to in vitro respiration (Mansour et al., 1994). (E), Representative recording of bursting activity after application of 50 nM DAMGO and 100 nM Naloxone. Top: in control (Oprm1f/f) slices bath application of 50 nM DAMGO quickly slowed and decreased the amplitude from baseline bursting. After rhythm cessation, bath application of Naloxone restored the rhythm. Bottom: in Slc17a6-cre;Oprm1f/f mice 50 nM DAMGO did not stop, or even slow rhythmic activity. (F), Percent of slices from each genotype with rhythm cessation after 50 nM DAMGO application. Control (n = 11), Gad2-Cre;Oprm1f/f (n = 6), Slc32a1-Cre;Oprm1f/f (n = 2), Slc6a5-Cre;Oprm1f/f (n = 4), and Slc17a6-Cre;Oprm1f/f (n = 3). (G), Schematic showing three subpopulations of glutamatergic lineages delineated by transcription factors Dbx1 and Foxp2. Foxp2 neurons represents a smaller, and overlapping, population of Dbx1 neurons. (H,) Identification of molecular subtypes of Oprm1 preBötC excitatory neurons. Sagittal section of the preBötC from a P0 Oprm1-mCherry;Dbx1-Cre;Rosa-LSL-YFP mouse immunostained for mCherry (OPRM1 fused to mCherry, red), YFP (Green) and FOXP2 (Blue). About ~50% of Oprm1 preBötC neurons are glutamatergic/Dbx1 derived (arrowhead) and of those,~35% express FOXP2 (asterisk). Scale bar, 50 µM. (I,) Quantification of the number of preBötC for each molecular subtype identified in H. J), Dose response curve for the bursting rate and amplitude after bath application of 0, 50, 100, and 500 nM DAMGO applied to Slc17a6-Cre;Oprm1f/f (gray, n = 3), Dbx1-Cre;Oprm1f/f (green, n = 3), Foxp2-Cre;Oprm1f/f (blue, n = 4) and control (black, n = 11) P0-4 preBötC slices. Rate and amplitude for each slice are normalized to baseline. (K), Schematic summary showing that the key node for opioids to suppress breathing is the preBötC and within this site, elimination of Oprm1 from just a small subset of those neurons,~70–140 excitatory neurons, prevents opioid respiratory suppression.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** 1817 single cells were isolated from the ventrolateral medulla of the P0 mouse. The transcriptome was sequenced with 10X genomics technology and cells were clustered by principle components analysis into 13 groups. three groups (2, 8, and 11, red numbers) expressed neural markers like Stmn2 (mRNA) shown here. Group two was a mixture of excitatory and inhibitory neurons and is the presumed preBötC cluster due to expression of Sst, Tacr1, and Cdh9 (mRNA, not shown). Group eight is a BötC cluster based on expression of Gad1 and Neurod6 (mRNA, not shown). Group 11 is a lateral reticular nucleus cluster based on expression of Zic1 and Barhl1 (mRNA, not shown). All other groups were oligodendrocytes, oligodendrocyte precursor cells, astrocytes, microglia and endothelial cells. The only group with enriched Oprm1 (mRNA) expression is the preBötC group 2. Within this group only 21/267 neurons express Oprm1 (mRNA). The single cell in group 1, 3, 6 (which are non-neural) that express Oprm1 (mRNA) are presumed contaminants.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Representative recording of bursting activity at baseline, after application of 50 nM DAMGO (red line), and 100 nM Naloxone (blue line). Top: Slc32a1-Cre;Oprm1f/f targeting GABAergic neurons (n = 2). Middle: Gad2-Cre;Oprm1f/f targeting GABAergic neurons (n = 6). Bottom: Slc6a5-Cre;Oprm1f/f targeting Glycinergic neurons (n = 4).

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/52694/elife-52694-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Nearly perfect colocalization of FOXP2 protein (red) and YFP (green) in a 25 µM sagittal section of the preBötC from a P0 Foxp2-Cre;Rosa-LSL-YFP mouse. This validates the use of Foxp2-Cre to remove Oprm1 from Foxp2-derived neurons. Scale bar, 100 µM.

Slices containing the preBötC autonomously generate respiratory-like rhythmic activity in vitro which is depressed in both rate and amplitude by bath administration of opioid agonists (Gray et al., 1999; Lorier et al., 2010), similar to opioid effects we observed on breathing in vivo. To determine which neural class mediates the depression of preBötC activity, we measured rhythmic bursting activity in vitro (Figure 4D) after selectively genetically deleting Oprm1 from each neural class. We achieved this deletion by crossing Oprm1f/f mice with each of the following: Slc17a6-Cre, Slc32a1-Cre, Gad2-Cre, or Slc6a5-Cre transgenic animals. preBötC slices from control mice (Oprm1f/f, Oprm1f/+, or Oprm1+/+) burst every 5–10 s and this activity was eliminated in 100% of slices by bath application of the selective µ-Opioid receptor agonist [D-Ala2, NMe-Phe4, Gly-ol5]-enkephalin (DAMGO, 50 nM), and subsequently rescued by opioid antagonist naloxone (Figure 4E,F). Strikingly, the bursting rhythm of Slc17a6-Cre;Oprm1f/f slices was not slowed by DAMGO, whereas the rhythm in Gad2-, Slc32a1-, and Slc6a5-Cre; Oprm1f/f slices was entirely eliminated, akin to wild type controls (Figure 4E,F, Figure 4—figure supplement 2). This demonstrates that glutamatergic excitatory neurons, representing ~50% of all preBötC Oprm1-expressing neurons and therefore 4% of preBötC neurons, mediate OIRD in vitro.

Next, we dissected the glutamatergic Oprm1 preBötC neurons by two developmental transcription factors, Dbx1 or Foxp2 (Gray et al., 2010; Bouvier et al., 2010; Gray, 2013), to determine if a subset can rescue rhythm depression (Figure 4G). Triple-labeling of Dbx1-YFP, OPRM1 fused to mCherry (OPRM1-mCherry), and FOXP2 protein quantified within a single preBötC revealed three molecular subtypes of P0 Oprm1 glutamatergic neurons: 92 ± 9 Dbx1, 50 ± 2 Dbx1/FOXP2, and 20 ± 4 FOXP2 (Figure 4H,I). We selectively eliminated the µ-Opioid receptor in these two lineages (Dbx1-Cre;Oprm1f/f or Foxp2-Cre;Oprm1f/f) and measured preBötC slice activity at increasing concentrations of DAMGO, exceeding the dose necessary to silence the control rhythm (500 nM vs. 50 nM). Elimination of Oprm1 from both genotypes was sufficient to rescue the frequency and amplitude of preBötC bursting in DAMGO, and the Dbx1 rescue was comparable to elimination of Oprm1 from all glutamatergic neurons, while the Foxp2 rescue was substantial, but partial (~50–60%, Figure 4J). This shows that opioids silence a small cohort (~140) of glutamatergic neurons to depress preBötC activity, and that a molecularly defined subpopulation, about half, can be targeted to rescue these effects.

## Discussion

Here we show that two small brainstem sites are sufficient to rescue opioid induced respiratory depression in vivo. Between them, the preBötC is the critical site and we molecularly define ~140 Oprm1 glutamatergic neurons within that are responsible for this effect in vitro. Future study of these neurons will provide the first example of endogenous opioid modulation of breathing. Furthermore, characterization of these neurons and their molecular response to opioids may extend existing strategies (Manzke et al., 2003) or reveal a novel strategy for separating respiratory depression from analgesia and therefore enable the development of novel opioids or related compounds that relieve pain without risk of overdose.

### A rubric for studying opioid and other respiratory depressants

We find that although multiple breathing parameters are impacted by opioids, decreased inspiratory airflow and delayed breath initiation, which we term pause, represent the primary changes that result in OIRD. Pauses occur during expiration and account for tens to hundreds of milliseconds of low airflow per breath. In hypercapnia, these pause periods terminate with an active expiration. The force, timing of inspiration, and expression of active expiration are ultimately determined by the inspiratory rhythm generator, the preBötC, and focused our initial studies to this site (Smith et al., 1991; Feldman et al., 2013; Cui et al., 2016; Huckstepp et al., 2016). Additionally, correlates of these two changes manifest as decreased burst size and frequency in the activity of the preBötC slice in vitro. These two key changes in the breath can guide future OIRD studies and efforts to characterize and test novel opioid drugs. Additionally, this workflow can be applied to the analysis of other respiratory depressants.

### Just two small brainstem sites mediate OIRD

Our experimental design allowed us to determine that both the preBötC and PBN/KF have independent and additive rescue of OIRD. Of these two, the preBötC has the larger magnitude rescue of our two core breathing parameters. The combined deletion of µ-Opioid receptor from both sites essentially eliminates OIRD, even to extremely high doses of the potent opioid fentanyl. This suggests that targeting just these two sites is sufficient to rescue opioid respiratory depression. We interpret the small remaining effect of opioids we observe to be due to incomplete transduction of these brain areas but cannot rule out other minor contributing sites. It is also possible, given the challenge of restricting viral transduction, that some of the demonstrated effects are already due to spillover deletion of µ-Opioid receptor in neighboring brain areas, such as the bulbospinal rostral ventral respiratory group. Our studies were limited to two opioids (morphine and fentanyl) at a specific dose and it will be important in future work to determine if these two brain sites are also critical for OIRD caused by these opioids at different doses or other opioids altogether.

### Depression of preBötC rhythm by silencing a small glutamatergic subpopulation

The two hallmark changes during OIRD, decreased inspiratory airflow and delayed initiation, perfectly match the opioid induced depression of amplitude and frequency in the preBötC slice. We show that ~140 Oprm1 glutamatergic preBötC neurons mediate this effect. And surprisingly, half this number, just ~70 glutamatergic neurons are sufficient to rescue opioid depression of the preBötC rhythm (50 Dbx1/FOXP2 and 20 FOXP2 in Foxp2-Cre;Oprm1f/f, Figure 4—figure supplement 3). Further, given the importance of Dbx1 neurons in respiratory rhythm generation (Gray et al., 2010; Bouvier et al., 2010), rescuing Oprm1 in just ~50/140 Dbx1 neurons (the Foxp2+ subset) may be sufficient to prevent preBötC depression, the smallest number of neurons we propose. This small number is remarkably consistent with the number of Dbx1 neurons that must be lesioned to arrest preBötC activity (Wang et al., 2014). Given the similarity of these effects, we hypothesize that opioids are primarily acting by silencing presynaptic release, effectively removing these neurons from the network. Alternatively, it is proposed that just a small subset of preBötC excitatory neurons may generate the inspiratory rhythm (Phillips et al., 2019) and perhaps these key Oprm1 neurons are enriched within this subgroup. In this instance, since hyperpolarization of preBötC rhythmogenic neurons slows and silences breathing (Koizumi et al., 2016), opioids may act postsynaptically as proposed by others (Montandon et al., 2011; Johnson et al., 1996). Regardless, it is profound that such a small number can abruptly halt the respiratory rhythm in a network of more than 1000 neurons and suggests that either these neurons act as a key population for rhythmogenesis, or that recurrent excitatory networks are exquisitely sensitive to the number of participating cells. Important future work will need to use the Dbx1/Oprm1 and Foxp2/Oprm1 molecular codes to selectively eliminate Oprm1 from these neurons to test if truly so few neurons profoundly control or modulate breathing in vivo.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th></th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Oprm1f/f</td>
      <td>The Jackson Laboratory</td>
      <td>030074</td>
      <td>RRID:IMSR_JAX:030074</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Oprm1-mCherry</td>
      <td>The Jackson Laboratory</td>
      <td>029013</td>
      <td>RRID:IMSR_JAX:29013</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Slc17a6-Cre</td>
      <td>The Jackson Laboratory</td>
      <td>016963</td>
      <td>RRID:IMSR_JAX:016963</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Gad2-Cre</td>
      <td>The Jackson Laboratory</td>
      <td>0101802</td>
      <td>RRID:IMSR_JAX:0101802</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Slc32a1-Cre</td>
      <td>The Jackson Laboratory</td>
      <td>028862</td>
      <td>RRID:IMSR_JAX:028862</td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Slc6a5-Cre</td>
      <td>PMID:25643296</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Dbx1-Cre</td>
      <td>PMID:16041369</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Foxp2-Cre</td>
      <td>PMID:27210758</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Mus musculus)</td>
      <td>Rosa-LSL-YFP</td>
      <td>The Jackson Laboratory</td>
      <td>006148</td>
      <td>RRID:IMSR_JAX:006148</td>
    </tr>
    <tr>
      <td>Adenovirus</td>
      <td>AAV5-CMV-Cre-GFP</td>
      <td>UNC Vector Core</td>
      <td></td>
      <td>AAV5</td>
    </tr>
    <tr>
      <td>Adenovirus</td>
      <td>AAV5-CAG-GFP</td>
      <td>UNC Vector Core</td>
      <td></td>
      <td>AAV5</td>
    </tr>
    <tr>
      <td>Adenovirus</td>
      <td>AAV5-CAG-tdtomato</td>
      <td>UNC Vector Core</td>
      <td></td>
      <td>AAV5</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rabbit anti-SST</td>
      <td>Peninsula</td>
      <td>T-4103</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rabbit anti-FOXP2</td>
      <td>Abcam</td>
      <td>ab16046</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>chicken anti-GFP</td>
      <td>Abcam</td>
      <td>ab13970</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>rat anti-mCherry</td>
      <td>Lifetech</td>
      <td>M11217</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>goat anti-rat 555</td>
      <td>Lifetech</td>
      <td>A21434</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>goat anti-chicken 488</td>
      <td>Lifetech</td>
      <td>A11039</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>goat anti-rabbit 633</td>
      <td>Lifetech</td>
      <td>35562</td>
      <td>1:200</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Morphine sulfate</td>
      <td>Henry Schein</td>
      <td>057202</td>
      <td>20 mg/kg</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>Fentanyl citrate</td>
      <td>Sigma</td>
      <td>F3886</td>
      <td>150 mg/kg</td>
    </tr>
    <tr>
      <td>Peptide</td>
      <td>DAMGO</td>
      <td>Abcam</td>
      <td>ab120674</td>
      <td>20–500 nM</td>
    </tr>
  </tbody>
</table>

### Animals

Oprm1f/f (Weibel et al., 2013), Oprm1-mCherry (Erbs et al., 2015), Slc17a6-Cre (Vong et al., 2011), Gad2-Cre (Taniguchi et al., 2011), Slc32a1-Cre (Vong et al., 2011), Slc6a5-Cre (Sherman et al., 2015), Dbx1-Cre (Bielle et al., 2005), Foxp2-Cre (Rousso et al., 2016), Rosa-LSL-YFP (Madisen et al., 2010) have been described. Littermates of transgene-containing mice were used as wild type controls. C57Bl/6 mice were used for single cell mRNA sequencing. Mice were housed in a 12 hr light/dark cycle with unrestricted food and water. Oprm1f/f mice were assigned into experimental and control groups at weaning and given anonymized identities for experimentation and data collection. All animal experiments were performed in accordance with national and institutional guidelines with standard precautions to minimize animal stress and the number of animals used in each experiment.

### Recombinant viruses

All viral procedures followed the Biosafety Guidelines approved by the University of California, San Francisco (UCSF) Institutional Animal Care and Use Program (IACUC) and Institutional Biosafety Committee (IBC). The following viruses were used: AAV5-CMV-Cre-GFP (4.7 × 1019 particles/mL, The Vector Core at the University of North Carolina at Chapel Hill), AAV5-CAG-GFP (1.0 × 1013 particles/mL, The Vector Core at the University of North Carolina at Chapel Hill) or AAV5-CAG-tdtomato (4.3 × 1012 particles/mL, The Vector Core at the University of North Carolina at Chapel Hill).

### Immunostaining

Postnatal day 0–4 brains were dissected in cold PBS, and adult brains were perfused with cold PBS and then 4% paraformaldehyde by intracardiac perfusion. The isolated brains from neonates and adults were then fixed in 4% paraformaldehyde overnight at 4°C and dehydrated in 30% sucrose the next 24 hr at 4°C. Brains were embedded and frozen in OCT once equilibrated in 30% sucrose. Cryosections (18–25 μM) were washed twice for 5 min in 0.1% Tween-20 in PBS, once for 10 min in 0.3% Triton-X100 in PBS, and then twice for 5 min in 0.1% Tween-20 in PBS. Following wash, sections were blocked for 20 min with either 10% goat serum in 0.3% Trition-X100 PBS. Sections were then incubated overnight at 4°C in the appropriate block solution containing primary antibody. Primary antibodies used were: rabbit anti-SST (Peninsula T-4103, 1:500), rabbit anti-FOXP2 (Abcam ab16046, 1:500), chicken anti-GFP (Abcam ab13970, 1:500), rat anti-mCherry (Lifetech. M11217, 1:500). After primary incubation, sections were washed three times for 10 min in 0.1% Tween-20 in PBS, then incubated for 1 hr at room temperature or overnight at 4°C in block containing secondary antibody. Secondary antibodies were: goat anti-rat 555 (Lifetech A21434, 1:200), goat anti-chicken 488 (Lifetech A11039, 1:200), goat anti-rabbit 633 (Lifetech 35562, 1:200). After secondary incubation, sections were washed in 0.1% Tween-20 in PBS and mounted in Mowiol with DAPI mounting media to prevent photobleaching.

### Plethysmography, respiratory and behavioral analysis

Adult (8–20 weeks) Oprm1f/f mice were first administered either IP 100–200 µL of saline or morphine (20 mg/kg, Henry Schein 057202) and placed in an isolated recovery cage for 15 min to allow full onset of action of the drug. Individual mice were then monitored in a 450 mL whole animal plethysmography chamber at room temperature (22°C) in 21% O2 balanced with N2 (normoxia) or 21% O2, 5% CO2 balanced with N2 (hypercapnia). For fentanyl (150 mg/kg, Sigma F3886) onset of action was so fast (<10 s) that animals were placed directly in the plethysmography chamber after administration of drug. Each session (combination of drug and oxygen condition) was separated by at least 24 hr to allow full recovery. Breathing was monitored by plethysmography, and other activity in the chamber monitored by video recording, for 40 min periods in normoxia and 10 min periods in hypercapnia. In cases where mice were subject to single or double site AAV injection to delete Oprm1 or sham controls, breathing was recorded first before viral injection and then again after deletion (or sham) more than 4 weeks later. Breathing traces were collected using EMKA iOX2 software and exported to Matlab for analysis. Each breath was automatically segmented based on airflow crossing zero as well as quality control metrics. Respiratory parameters (e.g. peak inspiratory flow, instantaneous frequency, pause length, tidal volume, etc) for each breath, as well as averages across states, were then calculated. Instantaneous frequency was defined as the inverse of breath duration. Pause length was defined as the expiratory period after airflow dropped below 0.5 mL/sec. The pause period is initially a prolonged airflow around or just above 0 mL/sec. and terminates with an increase in expiratory airflow, likely the active expiration induced by hypercapnia (11, Figure 1—figure supplement 1). The 0.5 mL/sec. threshold was chosen since it identifies low airflow pauses that are just above 0 mL/sec. which rarely occur in control hypercapnic breaths (Figure 1—figure supplement 2). Although pauses in length 50-100msec. could be considered false positives because they do not have a considerable low airflow period (see Figure 1—figure supplement 1 and , panel 2), they occur at a low rate in saline (1.53%) and we see an increased distribution of pauses in morphine that last hundreds of milliseconds (Figure 1I, see Figure 1—figure supplement 1 and , panel 3 and 4). Other respiratory parameters were defined by when airflow crosses the value of 0, with positive to negative being inspiration onset and negative to positive being expiration onset. Note, reported airflow in mL/sec. and tidal volume in mL are approximates of the true volumes. Whole body plethysmography imperfectly measures these parameters without corrections for humidity and temperature. However, since humidity and temperature are largely stable between recordings, because they are conducted in a temperature and humidity stable mouse facility, the estimated airflow (mL/sec.) and tidal volume (mL) can be compared in saline vs. morphine or pre and post-Cre virus injection studies. Additionally, in some instances respiratory parameters are appropriately normalized to animal weight in order to accurately compare between animals. However, this normalization is not appropriate for our study since lung volume in mice does not change in adulthood (Mitzner et al., 2001), and all respiratory measurements are compared statistically as the ratio of saline to morphine injections within the same animal. The analysis was performed with custom Matlab code available on Github with a sample dataset (Bachmutsky, 2020, https://github.com/YackleLab/Opioids-depress-breathing-through-two-small-brainstem-sites; copy archived at https://github.com/elifesciences-publications/Opioids-depress-breathing-through-two-small-brainstem-sites).

Due to limitations in breeding, a power calculation was not explicitly performed before our studies. Studies were conducted on all mice generated; six cohorts of animals. After respiration was measured, mice were sacrificed and injection sites were validated before inclusion of the data for further statistical analysis. We first conducted a Shapiro-Wilk normality on the average values (averaged across breaths) of the pre- and post-morphine respiratory parameters (e.g., peak inspiratory flow, instantaneous frequency) from n = 29 animals. We then used either paired Student’s t-test (if normal) or Wilcox Rank Sum test (if not normal) to evaluate statistical significance in comparing the distribution of these values. In comparisons of Oprm1-deleted vs. Sham conditions a mixed-repeated measure two-way ANOVA was performed to determine if these two groups were significantly different. Post-hoc Student’s t or Wilcox Rank Sum tests were then used to evaluate statistical significance between normalized (morphine/saline, or morphine-saline) respiratory parameters for intact vs. Oprm1 deleted or intact vs. Sham conditions. Normality in this case was determined by Shapiro-Wilk test on the distribution of normalized respiratory parameters from n = 29 animals. All the above statistics were performed using the publicly available Excel package ‘Real Statistics Functions’ and SPSS.

### Tail flick assays

Mice were injected with saline (control trials) or 20 mg/kg morphine. 15 min later mice were put into a restraining wire mesh with the tail exposed. One-third of the tail was dipped into a 48–50°C water bath and time was measured for the tail to flick. Immediately after the flick, the tail was removed from the bath. If the tail did not flick within 10 s, then the tail was removed. The procedure was video recorded so time to response could be quantified post-hoc. Each mouse was recorded for two saline and two morphine trials.

### Stereotaxic injection

Bilateral stereotaxic injections were performed in mice anesthetized by isoflurane. Coordinates used for the preBötC were: −6.75 mm posterior, −5.05 mm ventral from surface, ±1.3 mm lateral from bregma. Coordinates used for the PBN/KF were: −5.05 mm posterior, −3.7 ventral from surface, ±1.7 lateral from bregma. Injection sites specificity was confirmed by the restricted expression of Cre-GFP, GFP, or tdTomato centered in the anatomically defined Parabrachial/Kolliker-Fuse (Levitt et al., 2015) and preBötC (Smith et al., 1991; Feldman et al., 2013) areas. In the case of preBötC injections, anatomical location of injection site was also confirmed by localization with Somatostatin antibody staining (Tan et al., 2008). µ-Opioid receptor deletion was not explicitly demonstrated by immunohistochemistry. After injection of the virus, mice recovered for at least 3–4 weeks before breathing metrics were recorded again. In a subset of animals, mice were then subject to a second site deletion of the complementary brain area, ie. preBötC and then from the PBN/KF (Cohort 1) or vice versa (Cohort 2). These mice were then allowed to recover for another period of at least 3–4 weeks, after which a third set of breathing metrics were recorded. A subset of PBN/KF injected mice had only unilateral expression of Cre and their use is acknowledged in the text.

### Slice electrophysiology

Rhythmic 550 to 650 μm-thick transverse medullary slices which contain the preBötC and cranial nerve XII (XIIn) from neonatal Oprm1f/f, Oprm1f/f;Slc17a6-Cre+/-, Oprm1f/f;Gad2-Cre+/-, Oprm1f/f;Slc6a5-Cre+/-, Oprm1f/f;Slc32a1-Cre+/-, Oprm1f/f;Dbx1-Cre+/-, Oprm1f/f;Foxp2-Cre+/- (P0-5) were prepared as described (Ruangkittisakul et al., 2014). Briefly, slices were cut in ACSF containing (in mM): 124 NaCl, 3 KCl, 1.5 CaCl2, 1 MgSO4, 25 NaHCO3, 0.5 NaH2PO4, and 30 D-glucose, equilibrated with 95% O2 and 5% CO2 (4°C, pH = 7.4). The rostral portion of the slice was taken once the compact nucleus ambiguus was visualized. The dorsal side of each slice containing the closing of the 4th ventricle. For recordings, slices were incubated with ACSF from above and the extracellular K+ was raised to 9 mM and temperature to 27°C. Slices equilibrated for 20 min before experiments were started. The preBötC neural activity was recorded from either XIIn rootlet or as population activity directly from the XII motor nucleus using suction electrodes. Activity was recorded with a MultiClamp700A or B using pClamp9 at 10000 Hz and low/high pass filtered at 3/400 Hz. After equilibration, 20 min. of baseline activity was collected and then increasing concentrations of DAMGO (ab120674) were bath applied (20 nM, 50 nM, 100 nM, 500 nM). Activity was recorded for 20 min. after each DAMGO application. After the rhythm was eliminated or 500 nM DAMGO was reached, 100 nM Naloxone (Sigma Aldrich N7758) was bath applied to demonstrate slice viability. Rhythmic activity was normalized to the first control recording for dose response curves.

### Single cell mRNA sequencing and analysis

650 µm-thick medullary slices containing the preBötC were prepared from 10 P0 mice C57Bl/6 mice as described above. The preBötC and surrounding tissue was punched out of each slice with a P200 pipette tip and incubated in bubbled ACSF containing 1 mg/ml pronase for 30 min at 37°C with intermittent movement. Digested tissue was centrifuged at 800 rpm for 1 min, and the supernatant was discarded and replaced with 1% FBS in bubbled ACSF. The cell suspension was triturated serially with fire-polished pipettes with ~600 µm,~300 µm and ~150 µm diameter. The cells were filtered using a 40 µm cell strainer (Falcon 352340). DAPI was added to a final concentration of 1 µg/mL. The cell suspension was FACS sorted on a BD FACS AriaII for living (DAPI negative) single cells. The cells were centrifuged at 300 g for 5 min and resuspended in 30 µL 0.04% BSA in PBS. The library was prepared using the 10x Genomics Chromium Single Cell 3' Library and Gel Bead Kit v2 (1206267) and according to manufacturer’s instructions by the Gladstone genomics core. The final libraries were sequenced on HiSeq 4000.

For analysis, sequencing reads were processed using the 10x Genomics Cell Ranger v.2.01 pipeline. A total of 1860 cells were sequenced. Further analysis was performed using Seurat v2.3. Cells with less than 200 genes were removed from the dataset. Data was LogNormalized and scaled at 1e4. Highly variable genes were identified and used for principal component analysis. 25 principal components were used for unsupervised clustering using the FindCluster function. 12 clusters were identified at a resolution of 1.0, displayed in Figure 4—figure supplement 1. FindAllMarkers and violin plots of known cell type markers were used to identify each cluster.
