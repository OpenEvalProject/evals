# Switch-like and persistent memory formation in individual Drosophila larvae

## Authors

- Amanda Lesar<sup>1</sup> ([ORCID: 0000-0001-6611-5941](https://orcid.org/0000-0001-6611-5941))
- Javan Tahir<sup>1</sup>
- Jason Wolk<sup>1</sup>
- Marc Gershow<sup>1</sup> ([ORCID: 0000-0001-7528-6101](https://orcid.org/0000-0001-7528-6101)) †

### Affiliations

1. Department of Physics, New York University New York United States
2. Center for Neural Science, New York University New York United States
3. NYU Neuroscience Institute, New York University Langone Medical Center New York United States

† Corresponding author

## Abstract

Associative learning allows animals to use past experience to predict future events. The circuits underlying memory formation support immediate and sustained changes in function, often in response to a single example. Larval Drosophila is a genetic model for memory formation that can be accessed at molecular, synaptic, cellular, and circuit levels, often simultaneously, but existing behavioral assays for larval learning and memory do not address individual animals, and it has been difficult to form long-lasting memories, especially those requiring synaptic reorganization. We demonstrate a new assay for learning and memory capable of tracking the changing preferences of individual larvae. We use this assay to explore how activation of a pair of reward neurons changes the response to the innately aversive gas carbon dioxide (CO2). We confirm that when coupled to CO2 presentation in appropriate temporal sequence, optogenetic reward reduces avoidance of CO2. We find that learning is switch-like: all-or-none and quantized in two states. Memories can be extinguished by repeated unrewarded exposure to CO2 but are stabilized against extinction by repeated training or overnight consolidation. Finally, we demonstrate long-lasting protein synthesis dependent and independent memory formation.

## Introduction

Associative learning allows animals to use past experience to predict important future events, such as the appearance of food or predators, or changes in their environmental conditions (Pavlov, 1927; Kandel et al., 2014). The Drosophila larva is a favorable model system for the study of learning and memory formation (Gerber et al., 2013; Widmann et al., 2018; Quinn and Dudai, 1976; Scherer et al., 2003; Apostolopoulou et al., 2013; Neuser et al., 2005; Saumweber et al., 2018), with approximately 10,000 neurons in its representative insect brain. Widely available experimental tools allow manipulation of gene expression and introduction of foreign transgenes in labeled neurons throughout the Drosophila brain, including in the learning and memory centers (Saumweber et al., 2018; Eichler et al., 2017; Li et al., 2014; Duffy, 2002), whose synaptic connectivities can be reconstructed via electron microscopy (Eichler et al., 2017; Eschbach et al., 2020a; Eschbach et al., 2020b).

Larvae carry out complex behaviors including sensory-guided navigation (Luo et al., 2010; Klein et al., 2015; Fishilevich et al., 2005; Asahina et al., 2009; Gomez-Marin and Louis, 2014; Gershow et al., 2012; Gomez-Marin et al., 2011; Sawin et al., 1994; Kane et al., 2013; Busto et al., 1999; Humberg et al., 2018), which can be modified by learning (Gerber et al., 2013; Scherer et al., 2003; Neuser et al., 2005; Widmann et al., 2018). Larval Drosophila has long been a model for the study of memory formation, with a well-established paradigm developed to study associative memory formation through classical conditioning (Gerber et al., 2013; Widmann et al., 2018; Schleyer et al., 2018; Scherer et al., 2003; Neuser et al., 2005; Gerber and Stocker, 2007; Apostolopoulou et al., 2013; Saumweber et al., 2018; Weiglein et al., 2019). In this paradigm, larvae are trained and tested in groups, and learning is quantified by the difference in the olfactory preferences of differently trained groups of larvae. These assays quantify the effects of learning on a population level, but it is impossible to identify whether or to what extent an individual larva has learned.

New methods allow direct measurement of neural activity in behaving larvae (Karagyozov et al., 2018; He et al., 2019; Vaadia et al., 2019) and reconstruction of the connections between the neurons in a larva’s brain (Eichler et al., 2017; Eschbach et al., 2020a; Eschbach et al., 2020b; Takemura et al., 2017; Berck et al., 2016), potentially allowing us to explore how learning changes the structure and function of this model nervous system. Using these tools requires us to identify larvae that have definitively learned. Recently, a device has been developed for assaying individual adult flies’ innate (Honegger et al., 2020) and learned (Smith et al., 2021) olfactory preferences, but no comparable assay exists for the larval stage.

Further, to explore structural changes associated with learning, we need to form protein-synthesis dependent long-term memories (Yin et al., 1995; Yin et al., 1994; Perazzona et al., 2004). Larvae trained to associate odor with electric shock form memories that persist for at least 8 hr (Khurana et al., 2009). Odor-salt memories have been shown to partially persist for at least 5 hr (Widmann et al., 2016; Eschment et al., 2020) and can be protein-synthesis dependent (Eschment et al., 2020), depending on the initial feeding state of the larva. Overnight memory retention, whether or not requiring protein-synthesis, has not been demonstrated in the larva, nor has long-lasting retention of appetitive memories.

In this work, we demonstrate a new apparatus for in situ training and measurement of olfactory preferences for individual larvae. We use this assay to quantify appetitive memories formed by presentation of carbon dioxide (CO2) combined with optogenetic activation of reward neurons. Using this device, we find that larvae are sensitive to both the timing and context of the reward presentation, that learning is quantized and all-or-none, and that repeated presentation of CO2 without reinforcer can erase a newly formed memory. We induce memories that persist overnight, and control whether these memories require protein synthesis through alteration of the training protocol.

## Results

### A Y-maze assay to characterize olfactory preferences of individual Drosophila larvae

Establishing the degree to which an individual larva seeks out or avoids an odorant requires repeated measurements of that larva’s response to the odor. We developed a Y-maze assay (Buchanan et al., 2015; Werkhoven et al., 2019) to repeatedly test an individual’s olfactory preference. The Y-mazes (Figure 1A) are constructed from agarose with channels slightly larger than the larvae, allowing free crawling only in a straight line (Heckscher et al., 2012; Sun and Heckscher, 2016). An individual larva travels down one channel and approaches the intersection with the other two branches of the maze. Here, the larva is presented with odorized air (or in this work, air containing CO2) in one branch and pure air in the other. The larva then chooses and enters one of the two branches. This choice may be immediate or the result of a longer process in which the larva samples both channels and even reverses (Figure 1—video 2, Figure 1—video 3). When the larva reaches the end of its chosen channel, a circular chamber redirects it to return along the same channel to the intersection to make another choice. Custom computer vision software detects the motion of the larva while computer controlled valves manipulate the direction of airflow so that the larva is always presented with a fresh set of choices each time it approaches the intersection (Figure 1A, Figure 1—video 1).

![Figure 1.](https://cdn.elifesciences.org/articles/70317/elife-70317-fig1-v1.jpg)

**Figure 1.:** (A) Image sequence of a larva making two consecutive decisions in the Y-maze assay. White arrows indicate direction of air flow; red arrow shows direction of larva’s head. (B) Probability of choosing channel containing CO2 without any training. (C) Schematic representation of experiments in (D,E,F). All larvae were tested in the Y-maze for 1 hr to determine initial preference and again following manipulation to determine a final preference. The manipulations were: Paired Training - reward in concert with CO2 presentation, 15 s intervals, 20 repetitions; Offset After - reward presentation 7.5 s after CO2 onset, 15 s intervals, 20 repetitions; Reverse-Paired Training - reward opposite CO2 presentation, 15 s intervals, 20 repetitions; Offset Before - reward presentation 7.5 s before CO2 onset, 15 s intervals, 20 repetitions; DAN Activation Without CO2 - CO2 is never presented, while reward is presented at 15 s intervals, 20 repetitions; no training - no manipulation between two testing periods; Forward Paired (extended spacing) - 15 s reward follows 15 s CO2 presentation, followed by 60 s of air, 20 repetitions; Backwards Paired (extended spacing) - 15 s reward prior to 15 s CO2 presentation, followed by 60 s of air, 20 repetitions; Reward Between CO2 (extended spacing) - 15 s reward presentation between two 15 s CO2 presentations, followed by 45 s of air, 20 repetitions. (D) Probability of choosing CO2 containing channel before and after manipulation. All animals were fed ATR supplemented food, except those marked ATR-. (E) Probability of choosing CO2 containing channel before and after training as a function of reward timing, in training protocols with extended air spacings. All animals were DANi1>CsChrimson and fed ATR. (F) Probability of choosing CO2 containing channel before and after 20 cycles of paired training, as a function of CO2 concentration, used both during training and testing. All animals were DANi1>CsChrimson and fed ATR. * p<0.05, ** p<0.01, *** p<0.001.

We first sought to determine the suitability of this assay for measuring innate behavior. Drosophila larvae avoid carbon dioxide (CO2) at all concentrations (Faucher et al., 2006; Jones et al., 2007; Kwon et al., 2007; Gershow et al., 2012). We presented larvae with a choice between humidified air and humidified air containing CO2 each time they approached the central junction. At the 18% concentration used throughout this work, larvae with functional CO2 receptors chose the CO2-containing channel about 25% of the time. The probability of choosing the CO2 containing channel increased as CO2 concentration in that channel decreased (Figure 1F). Gr63a1 (Jones et al., 2007) larvae lacking a functional CO2 receptor were indifferent to the presence of CO2 in the channel (Figure 1B), as were animals in which the CO2 receptor neurons were silenced (Gr21a>Kir.21), indicating that larvae responded to the presence of CO2 and not some other property of the CO2 containing air stream. Silencing the Mushroom Body (OK107>Kir2.1) did not impair innate CO2 avoidance.

### Pairing CO2 presentation with optogenetic activation of a single pair of reward neurons eliminates CO2 avoidance

Activation of the DAN-i1 pair of mushroom body input neurons has been shown to act as a reward for associative learning (Saumweber et al., 2018; Thum and Gerber, 2019; Schleyer et al., 2020; Weiglein et al., 2019; Eschbach et al., 2020b). In these experiments, the conditioned odor was innately attractive, but CO2 is innately aversive. We wondered whether pairing DAN-i1 activation with CO2 would lessen or even reverse the larva’s innate avoidance of CO2.

To train larvae in the same Y-maze used to measure preference, we manipulated the valves so that the entire chamber was either filled with humidified air or with humidified air mixed with additional CO2, independent of the position of the larva, which was not tracked during training. At the same time, we activated DAN-i1 neurons expressing CsChrimson using red LEDs built in to the apparatus. For some larvae, we activated DAN-i1 when CO2 was present (paired, Figure 1D). For others, we activated the reward neurons when only air was present (reverse-paired, Figure 1D). Each training cycle consisted of one 15 s CO2 presentation and one 15 s air presentation, with DAN-i1 activated for the entirety of the CO2 (paired) or air (reverse-paired) presentation phase. The training protocols schematized in Figure 1D were repeated for 20 successive cycles. Thus, for instance, in the reverse-paired scheme CO2 offset at t=15s coincided with reward onset, and the reward offset at t=30s coincided with CO2 onset at t=0 of the subsequent cycle.

For each larva, we first measured naive preference and then preference following training. We found that in the paired group, larvae became indifferent to CO2 presentation following 20 training cycles (Figure 1D, DANi1>CsChrimson, Paired). We did not observe any change in preference in the reverse-paired group (DANi1>CsChrimson, Reverse-Paired). Nor did we observe a preference change following paired training for genetically identical animals not fed all-trans-retinal (ATR), a necessary co-factor for CsChrimson function (DANi1>CsChrimson, Paired ATR-). Animals fed ATR but not exposed to red light failed to show a preference shift (DANi1>CsChrimson, No Training). Larvae of the parent strains fed ATR and given paired training showed no preference shift (Effector Control, Driver Control). To control for possible effects of DAN-i1 activation, we activated DAN-i1 in 15 s intervals without presenting CO2 at all during the training (DANi1>CsChrimson, DAN w/o CO2); these larvae showed no shift in preference.

Taken together these results show that the change in CO2 preference requires activation of the DAN-i1 neurons and is not due to habituation (Twick et al., 2014; Das et al., 2011; Larkin et al., 2010), red light presentation, or other aspects of the training protocol. In particular, the paired and reverse-paired group experienced identical CO2 presentations and DAN-i1 activations with the only difference the relative timing between CO2 presentation and DAN-i1 activation.

Activation of DAN-i1 coincident with CO2 presentation decreased larvae’s subsequent avoidance of CO2. Formally, this admits two possibilities: the larva’s preference for CO2 increased because CO2 was presented at the same time as the reward or because CO2 predicted the reward. To test whether learning was contingent on coincidence or prediction, we carried out an additional set of experiments. As before, we first tested innate preference, then presented 20 alternating cycles of 15 s of CO2 followed by 15 s of air. However, this time during the conditioning phase, we either activated DAN-i1 7.5 s after CO2 onset, in which case CO2 predicted DAN-i1 activation, or 7.5 s before CO2 onset, in which case CO2 predicted withdrawal of DAN-i1 activation.

In both cases, DAN-i1 was activated in the presence of CO2 for 7.5 s and in the presence of air alone for 7.5 s. If learning depended only on the coincidence between reward and CO2 presentations, both should be equally effective at generating a change in preference. In fact, we only found an increase in CO2 preference following training in which the CO2 predicted the reward (Figure 1D).

Next, we asked whether reward prediction alone was sufficient to establish a memory, or if coincidence between CO2 and DAN-i1 activation was also required. We altered the training protocol to present 15 s of CO2 followed by 60 s of air. Some larvae were rewarded by activation of DAN-i1 in the 15 s immediately following CO2 presentation (Forward Paired), while others were rewarded in the 15 s immediately prior to CO2 presentation (Backwards Paired). For a third group of larvae, CO2 was presented both before and after reward presentation (reward between CO2 presentations). At no time was DAN-i1 activated in the presence of CO2, but in the first group CO2 predicted DAN-i1 activation while in the others it did not. We found an increased CO2 preference for animals in this first group only (Figure 1E), indicating that reward prediction is both necessary and sufficient for learning in this assay.

In other associative conditioning experiments using DAN-i1 activation as a reward, decreased attraction to the odor was observed in the reverse-paired groups (Saumweber et al., 2018; Thum and Gerber, 2019; Schleyer et al., 2020). In our experiments, we did not see any evidence of increased aversion in the reverse-paired groups.

Untrained larvae avoided CO2. After 20 cycles of paired, offset-after, or forward-paired training, larvae no longer avoided CO2, but they also did not seek it out. We wondered whether it might be possible to train larvae to develop an attraction to the innately aversive CO2. In other contexts, reward via activation of 3 DANs (DAN-i1, DAN-h1, DAN-j1 - whether DAN-h1 is present in second instar larvae, used in this study, is presently unreported) labeled by the 58E02-Gal4 line has been reported to produce strong learning scores (Saumweber et al., 2018; Rohwedder et al., 2016; Lyutova et al., 2019; Schleyer et al., 2020). We repeated the training protocol, substituting 58E02 activation for DAN-i1 activation alone, but did not see an increased preference following training compared to DAN-i1 activation alone (Figure 1D, 58E02>CsChrimson).

Next, we asked how varying the CO2 concentration might affect animals’ performance in the assay. We presented lower concentrations of CO2 both during the training and testing phases, and found that decreasing the CO2 concentration decreased innate avoidance of CO2. In all cases, following training, larvae lost avoidance to CO2 but none showed statistically significant attraction (Figure 1F).

### Learning is quantized and all-or-none

We investigated how change in preference for CO2 following associative conditioning with DAN-i1 activation depended on the amount of training. As in the previous experiments, we first measured the innate preference, then trained each larva using repeated cycles alternating pure and CO2 containing air, while activating DAN-i1 in concert with CO2 presentation. In these experiments, however, we varied the number of training cycles an individual larva experienced. We found that as a group, larvae that had experienced more training chose the CO2 containing channel more often (Figure 2A).

![Figure 2.](https://cdn.elifesciences.org/articles/70317/elife-70317-fig2-v1.jpg)

**Figure 2.:** (A) Probability of choosing CO2 containing channel before and after training, as a function of amount of training. *** p<0.001. (B) Histograms of individual larva preferences after training, grouped by number of training cycles. (C) Histogram of individual larva preference after training for all larvae. (D) Population average probability of choosing CO2 following training vs. dose. (E) Fraction of larvae untrained vs. number of training cycles. Teal: fit parameters and error ranges from quantized model, purple lines, prediction and error ranges from memoryless model. Note logarithmic y-axis on insert. (C–E) Orange: graded model prediction - post-training preference is represented by a single Gaussian distribution whose mean and variance depend on amount of training; Teal: quantized model prediction - post-training preference is represented by two fixed Gaussian distributions and the fraction of larvae in each population depends on the amount of training; Purple: all-or-none model prediction - post-training preference is represented by two fixed Gaussian distributions and the effect of a single training cycle is to train a fixed fraction of the remaining untrained larvae.

Our data showed that increasing the amount of training increased overall preference for CO2 up to a saturation point. But what was the mechanism for this change? Did each cycle of training increase each larva’s preference for CO2 by some small amount, with the effect accumulating over repeated training (graded learning)? Or did some larvae experience a dramatic preference change – from naive to fully trained – with each cycle of training, with the number of fully trained larvae increasing with training repetitions (quantized learning)?

Either quantized or graded learning can explain the shift of mean preference of a population (Gallistel et al., 2004); to differentiate between the modes of learning, we examined repeated decisions made by individual animals, measurements that were impossible in previous larval assays. For each larva, we quantified the change in CO2 preference before and after training. Figure 2B shows a histogram of larva preference (the fraction of times an individual larva chose the CO2 containing channel) after training, grouped by the number of cycles of training a larva received.

Larvae that received no training (0 cycles) formed a single population that chose CO2 27% of the time. Larvae that were trained to saturation (20 training cycles) also formed a single group centered around 52% probability of choosing CO2. Both the graded and quantized learning models make the same predictions for these endpoints, but their predictions vary starkly for the intermediate cases. A graded learning model predicts that all larvae that received the same amount of training would form a single group whose mean preference for CO2 would increase with increasing training. A quantized learning model predicts that larvae that have received the same amount of training will form two discrete groups (‘trained’ and ‘untrained’) with fixed centers whose means do not depend on the amount of training. With increased training an increasing fraction of larvae would be found in the trained group.

We fit the distributions of preference following conditioning to graded and quantized learning models. In the graded model, the preference was represented by a single Gaussian distribution whose mean and variance were a function of amount of training (orange, Figure 2). In the quantized model, the preference was represented by two Gaussian distributions; the fraction of larvae in each population was a function of the amount of training (teal, Figure 2).

We found that the data were better described by the quantized learning model (Table 4): larvae form two discrete groups, with the fraction in the trained group increasing with each cycle of additional training. The centers of the two groups do not vary with the amount of training, a point made most clear by considering the preference after training of all larvae taken together regardless of the amount of training received (Figure 2C), which shows two well defined and separated groups. From these data, we concluded that the effect of our associative conditioning on an individual larva is to either cause a discrete switch in preference or to leave the initial preference intact.

Next we asked what effect, if any, associative conditioning had on larvae that retained their innate preferences following training. Whether humans form associative memories gradually through repeated training or learn in an all-or-none manner has been the subject of debate in the Psychology literature (Roediger and Arnold, 2012); recent electrophysiological measurements in humans supports the all-or-none hypothesis (Ison et al., 2015). If learning is all-or-nothing, then if a larva has received training but has not yet expressed a behavioral switch, it is the same as if the larva has received no training at all. In this case, with every training cycle, regardless of past experience, every untrained larva will have the same probability of learning: $ρ$, and the effect of training can be described by a particularly simple equation

$$
n_{u}⁢(i+1)=n_{u}⁢(i)-ρ⁢n_{u}⁢(i)
$$

where $n_{u}⁢(i)$ are the number untrained larvae following $i$ cycles of training. Note that $ρ$ can depend on the training protocol or other external variables, but it does not depend on the past training experiences of the larvae, and can be considered a fixed constant for a given experimental condition. The solution to this equation is an exponentially decaying population of untrained larvae. For a given initial population $n_{u}⁢(0)$ of untrained larvae,

$$
n_{u}⁢(i)=(1-ρ)^{i}⁢n_{u}⁢(0)
$$

Any so-called memoryless process like this produces an exponential decay of the initial population (Apostol, 1969). Meanwhile, processes with memory can produce other distributions. For example, if the training were cumulative, we would expect a threshold effect: as the number of cycles of training increased from 0, most larvae would initially remain untrained until a critical number of cycles (nc) were reached and there would be a sudden shift to a mostly trained population. While a process with memory can also produce exponential decay (e.g. if each larva required a fixed nc cycles of training to learn, and nc was itself exponentially distributed), all memoryless processes must produce an exponential decay, and exponential decay is therefore an indicator of a memoryless (all-or-none) process.

Our fit to the quantized learning model produces an estimate of the fraction of larvae that remain untrained following training. We plotted the fraction of untrained larvae vs. number of training cycles and saw that the fraction of larvae in the untrained group exponentially decreased with increasing training (Figure 2E, note logarithmic y-axis on insert). We then fit the population distributions to an all-or-none quantized learning model in which the effect of a single training cycle was to train a fixed fraction of the remaining untrained larvae (purple, Figure 2). This model fit the data better than the graded learning model and almost as well as the original quantized learning model (in which the fraction of untrained larvae was fit separately to each group) despite having fewer parameters than either model. According to standard selection rules (BIC and AIC), the all-or-none quantized model best describes the data (Table 4).

### Repeated exposure without reward following training leads to memory extinction

Reversal learning, in which the reward contingency is reversed, and extinction, in which the conditioned stimulus is presented without reward, experiments explore cognitive flexibility. Previous experiments with both adult Drosophila (Tully et al., 1990; Ren et al., 2012; Wu et al., 2017; Vogt et al., 2015) and larval (Mancini et al., 2019) Drosophila demonstrated a reversal learning paradigm. Extinction has been demonstrated in adult flies (Felsenberg et al., 2017; Felsenberg et al., 2018; Schwaerzel et al., 2002) but not in larvae.

To test for extinction, we again first measured an individual larva’s CO2 preference and then carried out associative conditioning for a given number (2-10) of training cycles. Next instead of immediately testing the larva’s new preference for CO2, we exposed the larva to an extinction phase – 18 cycles of alternating CO2 and air without any optogenetic reward. Following the extinction period, we tested larvae as usual to measure their changed preference for CO2. As a control against the effects of increased CO2 exposure, we also performed habituation experiments, which were the same as the extinction experiments, except the 18 unrewarded cycles were presented prior to the rewarded training cycles. The extinction and habituation protocols are schematized in Figure 3A.

![Figure 3.](https://cdn.elifesciences.org/articles/70317/elife-70317-fig3-v1.jpg)

**Figure 3.:** Training + Extinction: larvae were exposed to 18 cycles of alternating CO2 and air following training. Habituation + Training: larvae were exposed to 18 cycles of alternating CO2 and air prior to training. (B) Probability of choosing CO2 containing channel (top) and fraction of larvae in trained group according to double Gaussian model fit (bottom) before and after training scheme. (C) Histograms of individual larva preference after training, for all larva and for larva trained with 2–4 training cycles. * p<0.05, ** p<0.01, *** p<0.001.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/70317/elife-70317-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Testing and training protocol for B,C. Larvae were trained with three cycles of paired training, followed by 18 extinction cycles of alternating CO2 and air with no reward presented. After extinction, larvae were presented with three additional paired training cycles before testing. (B) Probability of choosing CO2 containing channel before and after training scheme. (C) Fraction of larvae in trained group according to double Gaussian model fit before and after training scheme. All larvae were DAN-i1>CsChrimson and raised on ATR+ food. *** p<0.001.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/70317/elife-70317-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (A) Larvae population average response in the first ten minutes following training (0–10 min), compared to the latter fifty minutes of testing (10–60 min), for larvae that had been given 2, 5, or 20 cycles of paired training. (B) Larvae population average response for the first five choices made by the larvae following training, compared to the remaining choices, for larvae that had been given 2, 5, or 20 cycles of paired training and made at least 10 decisions following training. (C,D,E) Larvae population average response over 15-min segments following training, for larvae trained with (C) 2 cycles, (D) 5 cycles, or (E) 20 cycles of training. All larvae were DAN-i1>CsChrimson and raised on ATR+ food.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/70317/elife-70317-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** (A) Testing and training protocols for experiments in B. All larvae are tested in the Y-maze for one hour to determine initial preference. Larvae were then trained with 10 cycles of paired training, followed by a 15-min test period. The 10 cycle train/15 min test was repeated four times. (B) Probability of choosing CO2-containing channel before training, and during each of the four test periods. All larvae were DAN-i1>CsChrimson and raised on ATR+ food. *** p <0.001.

When we compared the ‘habituated’ groups of larvae to larvae trained for the same number of cycles without habituation or extinction, we found that unrewarded CO2 presentation prior to training had no effect on the eventual preference change (Figure 3B). This was unsurprising, as the initial testing period already offered a number of unrewarded CO2 presentations. In contrast, unrewarded CO2 presentations following training reversed the effect of training; for small (2 or 3 cycles) amounts of training, the reversal was almost complete (Figure 3B).

We previously observed that associative conditioning produced a discrete and quantized change in CO2 preference. Here, we found that extinction following training greatly reversed the effects of conditioning. We wondered whether larvae that had been subject to both training and extinction reverted to their original CO2 preference or to an intermediate state. In the former case, we would expect to see a bimodal distribution of preference change following training and extinction, while in the latter we would see a third group of larvae. This group would be most evident in experiments where two to four cycles of training were followed by extinction, as these had the largest deficit in the fraction of trained larvae compared to habituated larvae that received the same amount of training. We examined the preferences of all larvae following two to four cycles of training, grouped by whether they were normally trained, habituated, or subject to extinction (Figure 3C). In all cases, we observed two groups with the same central means and no evidence of a third intermediate group. We concluded that larvae subject to training then extinction reverted to their ‘untrained’ state.

We wondered whether larvae would still learn if they received additional training directly following extinction. As before, we measured the innate preference, presented three paired training cycles followed by the extinction phase. At this point, based on our previous results, larvae would have returned to their initial innate avoidance of CO2. We then immediately presented three more paired training cycles before behavioral testing (Figure 3—figure supplement 1A). We found that following this training-extinction-training protocol, both the population preference for CO2 (Figure 3—figure supplement 1B) and the fraction of larvae trained (Figure 3—figure supplement 1C) were comparable to larvae that had been trained three times without extinction cycles.

Given the relatively short duration of training and the ability of unrewarded CO2 presentations to extinguish prior training, we wondered whether larvae might change their CO2 preferences over the course of the hour-long post-training behavioral readout. In particular, might the apparent threshold of 50% attraction be an artifact due to a short period of attraction to CO2 followed by a longer period of indifference or modest avoidance?

To test for a short period of increased attraction immediately following training, we reanalyzed the results of experiments with 2, 5, and 20 cycles of paired training. In each case, we compared the initial 10 min of the post-training choice assay to the final 50 min (Figure 3—figure supplement 2A) and found no significant difference between the initial and final periods for any of these training conditions. We then compared the mean preference over the first five choices (representing five unrewarded CO2 presentations) made by each larva to the mean preference in the remainder of the experiment and again found no significant difference (Figure 3—figure supplement 2B). Breaking the behavioral readout into equal 15 min periods also reveals no strong temporal signal (Figure 3—figure supplement 2C–E).

Finally, we developed a new protocol to minimize the possible effects of extinction over the course of the behavioral readout, using the fact that training following extinction can re-establish a lost memory (Figure 3—figure supplement 1). We trained each larva with 10 paired cycles (5 min of training), then tested their preference for 15 min, then presented another 10 paired training cycles followed by another 15 min of testing, for a total of 4 training and testing blocks (Figure 3—figure supplement 3). The results were comparable to when we presented a single training block followed by an hour-long test period. Thus, we concluded that the apparent limit of 50% population preference to CO2 following training was not due to the long time-scale of the behavioral readout.

### Larvae can retain memory overnight; the type of memory formed depends on the training protocol

Studies in adult (Tully et al., 1990; Yin et al., 1995; Margulies et al., 2005) and larval (Honjo and Furukubo-Tokunaga, 2005; Honjo and Furukubo-Tokunaga, 2009; Widmann et al., 2016; Khurana et al., 2009; Eschment et al., 2020; Aceves-Piña and Quinn, 1979) Drosophila have identified distinct memory phases: short-term memory (STM), middle-term memory (MTM), long-term memory (LTM), and anesthesia-resistant memory (ARM). LTM and ARM are consolidated forms of memory controlled by partially separate molecular and anatomical pathways (Isabel et al., 2004; Jacob and Waddell, 2020; Wu et al., 2012). ARM is resistant to anesthetic agents (Quinn et al., 1974); LTM requires cAMP response element-binding protein (CREB)-dependent transcription and de-novo protein synthesis, while ARM does not (Yin et al., 1995; Perazzona et al., 2004). Adults have been shown to retain memories for up to a week (Yin et al., 1995). Larvae trained to associate odor with electric shock form memories that persist for at least 8 hr (Khurana et al., 2009). Odor-salt memories have been shown to persist for at least 5 hr (Widmann et al., 2016; Eschment et al., 2020) and can be either ARM or LTM, depending on the initial feeding state of the larva.

We sought to determine whether we could create consolidated memories that would persist overnight, and if so, whether these memories represented ARM or LTM. As in previously described experiments, we first tested each larva’s individual preference in the Y-maze assay, trained it to associate CO2 presentation with DAN-i1 activation, and then measured its individual preference again following training. After this second round of testing, we removed the larva from the apparatus and placed it on food (without ATR) overnight. The next day, we placed the larva back in the Y-maze and again tested its preference for CO2, without any additional training.

We found that following 20 cycles of training, larvae became indifferent to CO2 and this indifference persisted to the next day. Similarly, we found that most larvae switched preference following five cycles of training and retained that preference overnight. Larvae that received no training or 20 cycles of unpaired training had no change in CO2 preference immediately following training or the next day (Figure 4B).

![Figure 4.](https://cdn.elifesciences.org/articles/70317/elife-70317-fig4-v1.jpg)

**Figure 4.:** (A) Testing and training protocols. Except where indicated, larvae were tested, trained immediately after testing, tested again, then placed on food overnight and tested the following day. For extinction experiments, larvae were trained three times, and then exposed to 18 cycles of alternating CO2 and air either immediately following training or prior to testing the next day. (B,C,D) Probability of choosing CO2 containing channel (top) and fraction of larvae in trained group according to double Gaussian model fit (bottom) prior to training, immediately following training, and the next day. When the center bar is missing, larvae were not tested immediately following training but instead removed immediately to food. M Nx = massed training, N repetitions, S 10x = spaced training 10 total pairings, RP = reverse paired (see Figure 1C), No Train = no training. Larvae in (B,C) were DANi1>CsChrimson. Larvae in (D) were DANi1>hs-dCREB2-b;CsChrimson. Larvae were raised on food containing ATR, except for ATR+/CXM-, ATR+/CXM+ larvae who were fed ATR supplemented yeast paste (without/with cycloheximide) for 4 hr prior to initial testing. For reverse-paired (RP) and no training schemes, see Figure 1B. * p<0.05, ** p<0.01, *** p<0.001.

We had previously shown two cycles of training caused roughly half the larva to change preference immediately after training. We decided to use this partition to verify a correlation between immediate and long-term memories; we expected that larvae initially in the ‘trained’ group would also form a ‘trained’ group the following day. However, while we found that two cycles of training were sufficient to cause some larvae to become indifferent to CO2 immediately following training, when we tested these larvae the next day, we found that all had reverted to their initial avoidance of CO2.

There were two possible explanations for this reversion. Perhaps, two cycles of training were sufficient to form a short term memory, but more training was required to induce a long-term memory. Or perhaps the testing period, in which larvae were exposed repeatedly to CO2 without reward, reversed the two-cycle training. To control for the latter, we modified the experimental protocol. We tested each larva’s innate preference, presented two training cycles, and then immediately removed the larva to food overnight, without any further testing. When we tested these larvae the next day, we found that they showed decreased avoidance of CO2. This indicated that two cycles of training were sufficient to form a memory lasting overnight, but that immediate exposure to unrewarded CO2 following this short training interval likely reversed the effects of training, an effect we observed in Figure 3. When larvae were trained for 20 cycles, omitting the testing had no effect on these larvae’s preferences the following day.

To confirm that extinction could explain the failure to form a persistent memory, we exposed larvae to three cycles of paired training, then 18 cycles of extinction (as in Figure 3) and then removed them to food overnight before testing their preferences the next day. As expected, these larvae avoided CO2 as much the next day as they did prior to training (Figure 4B, Ext Post-Train).

We wondered whether memories that had consolidated overnight would be more resistant to extinction. We repeated the previous experiment with a single modification. As before, we tested the larva’s initial preference and trained it with three cycles of rewarded CO2 presentation. This time, we immediately removed the larva to food following training. The next day, we returned the larva to the Y-maze and presented the extinction phase of 18 unrewarded CO2 presentations prior to testing for CO2 preference. We found that in this case, larvae still expressed an increased preference for CO2 despite the extinction phase (Figure 4B, Ext Pre-Test). The only difference between the two experiments was whether we attempted extinction immediately after training or the next day. Thus, we concluded that overnight consolidation made memories more resistant to extinction.

ARM can be distinguished from LTM because the latter requires de novo protein synthesis and can be disrupted by ingestion of the translation-inhibitor cycloheximide (CXM). To incorporate CXM feeding, we modified our protocols. Instead of raising larvae on ATR supplemented food, we raised them on standard food and then fed them with ATR supplemented yeast paste for 4 hr prior to the experiment (ATR+/CXM-). For some larvae (ATR+/CXM+), we also added CXM to the yeast paste. In this way, we could be sure that if ATR+/CXM+ larvae ingested enough ATR to allow for CsChrimson activation of DAN-i1, they must have also ingested CXM as well. To further verify CXM ingestion, we placed ATR+/CXM+ and ATR+/CXM- larvae on clean food and allowed them to continue development. 95% of ATR+/CXM- larvae pupated, while only 45% of ATR+/CXM+ larvae pupated.

Following the 4 hr feeding period, ATR+/CXM+ and ATR+/CXM- larvae were treated identically. As in the previously described experiments, we first tested each larva’s individual preference in the Y-maze assay, trained the larva 20 times to associate CO2 presentation with DAN-i1 activation, and then measured its individual preference again following training. After this second round of testing, we removed the larva from the apparatus and placed it on food (without ATR or CXM) overnight. The next day we placed the larva back in the Y-maze and again tested its preference for CO2, without any additional training.

We found that performances tested immediately and 16 hr after training were both unaffected by CXM treatment. Following 20 cycles of training, larvae from both groups (ATR+/CXM+; ATR+/CXM-) became indifferent to CO2 and this indifference persisted to the next day (Figure 4C). This suggests that the memory formation was independent of de novo protein synthesis.

In adult Drosophila, whether ARM or LTM is formed depends on the training protocol (Tully et al., 1990; Tully et al., 1994; Yin et al., 1995; Yu et al., 2006; Bouzaiane et al., 2015). ‘Massed’ training, in which all conditioning occurs in rapid sequence without rest intervals, results in ARM, while ‘spaced’ training, in which the conditioning occurs in blocks separated by intervals of time, produces LTM. Our training protocol more closely resembles massed training, so it seemed sensible that it would produce ARM. To see if we could instead develop LTM, we established a spaced training protocol. Larvae received two paired cycles of training, followed by a 15-min interval of air-presentation only; this sequence was repeated five times. To keep the total length of the experiment within a (covid-related) limited daily time window, we did not test the larvae immediately after training but only the next day.

Prior to spaced training, both ATR+/CXM- and ATR+/CXM+ larvae avoided CO2 to the same degree. We found that 1 day following spaced training, ATR+/CXM+ larvae continued to avoid CO2, while ATR+/CXM- larvae did not. This indicated that spaced training formed a memory whose retention was disrupted by CXM. To verify that spacing the trials was essential to forming a protein-synthesis dependent memory, we duplicated the experiments exactly, except we presented 10 cycles of training en masse, rather than spacing them. In this case, both ATR+/CXM- and ATR+/CXM- larvae expressed learned indifference to CO21 day following training (Figure 4C).

As an alternate to CXM feeding, LTM (but not ARM) formation can also be disrupted through use of hs-dCREB2-b, a heat-shock inducible dominant-negative repressor of transcription mediated by dCREB2-a. (Perazzona et al., 2004; Yin et al., 1995). Specifically, in adult flies expressing hs-dCREB2-b, memory retention is disrupted in a heat-shock-dependent manner following spaced, but not massed training (Yin et al., 1995). We therefore repeated our long-term memory experiments in larvae that in addition to expressing Chrimson in DAN-i1 neurons also carried the hs-dCREB2-b transgene. Massed and spaced training were carried out as previously described, using larvae raised on ATR supplemented food, except that some larvae (HS) received a 30 min heat-shock (at 37 C), followed by a 30 min recovery period (at 25 C) immediately prior to the beginning of the experiment (i.e. prior to the initial testing of naive preference). Preference for CO2 was tested prior to training, immediately following training, and the next day, following an overnight rest on food without ATR.

We found that, congruent with our CXM experiments, the day after spaced training, heat-shocked larvae (Figure 4D,S 10x, HS) avoided CO2 to the same extent they did prior to training, while larvae that were not heat-shocked (Figure 4D,S 10X, No HS) retained learned indifference; larvae that received massed training (Figure 4D,M 10x, HS and No HS) retained their learned indifference overnight, regardless of heat-shock. These results are consistent with similar experiments in adult flies (Yin et al., 1994; Yu et al., 2006).

Immediately following spaced training (80 min after the initiation of the spaced training protocol), heat-shocked larvae continued to avoid CO2, showing that memory formation was impaired on a relatively short timescale. This is consistent with previous work in the larva, where dCREB2-b expression induced memory deficits beginning 30 min following a single 30 min training cycle (Honjo and Furukubo-Tokunaga, 2005), and immediately following 125 min of spaced training (Widmann et al., 2016). In those experiments, neither training protocol was shown to induce a persistent long-term memory.

## Discussion

In this work, we demonstrated a new apparatus for training individual larvae and assessing their olfactory preferences. Compared to the existing paradigm, our assay allows for measuring individual animals’ changes in preference due to training, allows for greater control of the temporal relation between the conditioned and unconditioned stimuli, and does not require any handling of the animals between training and testing.

In our assay, larvae learned in a switch-like (all-or-none two-state quantized) manner. The learning process was better described as a sudden transition between states than as a graded change in preference, and each cycle of training (presentation of CO2 coupled with reward) either caused a state transition or did not. Pigeons, rats, and rabbits have all been shown to experience sudden performance increases in learning tasks, suggesting quantized learning may be a generalized phenomenon (Gallistel et al., 2004). We found no evidence of a cumulative effect of prior training in the probability that a given cycle of training would induce a state transition in larvae that had not already transitioned. We did, however, find evidence that repeated cycles of training stabilized memories against later extinction effected by presentation of CO2 without reward. These measurements were enabled by our assay’s ability to track individual preferences over the course of the entire experiment.

We directly tested the ability of unrewarded CO2 presentations to extinguish a just-formed memory by presenting CO2 without air immediately following training (Figure 3). We also indirectly measured the effects of extinction due to unrewarded CO2 presentation during the hour-long behavioral test (Figure 3—figure supplement 2). Following two cycles of training, immediate presentation of 18 unrewarded CO2 cycles abolished the formed memory (Figure 3B), but without this direct extinction protocol, we saw no evidence of extinction over the course of the hour-long behavioral test (Figure 3—figure supplement 2A–C). It is perhaps unsurprising that rapid and consistent unrewarded presentations immediately following training are more effective at extinguishing a memory than the later and more varied unrewarded presentations during the behavioral test. But following two cycles of training, the behavioral test does prevent expression of the formed memory the next day (Figure 4B). This could show that the unrewarded presentations during behavioral testing are too late and/or sporadic to prevent immediate memory expression but do prevent the transition to more long-lived ARM. Further study will be required to confirm this. Our apparatus can precisely control the timing and nature of both rewarded and unrewarded presentations to probe different phases of memory formation and consolidation.

We found that larvae trained in our assay retained memories overnight: 16–20 hr. When training was presented all at once, these memories were not disrupted by ingestion of the protein-synthesis inhibitor cycloheximide or induction of the transcrption repressor dCREB2-b, while when training was spaced over time, cycloheximide feeding and dCREB2-b induction both prevented long duration memory formation. Thus, we identified spaced training as producing long-term memory (LTM) and the massed training as producing anesthesia-resistant memory (ARM). These results are the first demonstrations that larvae can retain memories overnight; they are entirely congruent with observations in adult flies.

We explored how the order of CO2 and reward presentations affected learning. We found that for larvae to learn, CO2 onset must occur coincident with or before reward onset, but that it was neither necessary nor sufficient for CO2 and reward to be presented together at the same time. While we assume that the same neural mechanism underlies learning in the ‘paired’, 'offset after' (Figure 1D) and ‘forward-paired’ (Figure 1E) paradigms, it is at least formally possible that the mechanism might be different in these contexts. Most of the work in this paper used the ‘paired’ protocol; it would be interesting to test in the future whether the 'forward-paired' protocol produces memories that differ in their resistance to extinction or in their long-term persistence.

Our results using the ‘reverse paired’ (Figure 1D) and 'backwards paired’ (Figure 1E) protocols differed from previous reports. In other assays, presenting the reward (including via activation of DAN-i1) prior to presenting the conditioned odor results in decreased attraction/increased avoidance (Schleyer et al., 2020; Saumweber et al., 2018) of that odor. We found that such ‘reverse-pairings’ neither increased nor decreased a larva’s avoidance of CO2. There are a number of differences, most significantly our new behavioral assay and our use of the innately aversive CO2 as the conditioned stimulus that might account for the discrepancy.

While this work does not directly speak to the neural mechanism behind the change in preference, it is congruent with the evolving model of learning in Drosophila. In this model, different Mushroom Body Output Neurons (MBONs) promote approach or avoidance (Aso et al., 2014; Eschbach and Zlatic, 2020; Perisse et al., 2013; Owald et al., 2015; Owald and Waddell, 2015; Hige et al., 2015) and synapse onto a convergence neuron that integrates their activities (Eschbach and Zlatic, 2020). Prior to learning, aversive and appetitive MBONs are thought to receive similar drives from Kenyon Cells (KCs) that respond to specific olfactory signals. That is, in response to a stimulus, the activities of MBONs representing these opposite valences are initially balanced, and behavior is governed by an innate preference to that odor, controlled by neuronal circuits external to the MB (Aso et al., 2014; Eschbach and Zlatic, 2020). Aversive and appetitive learning depress the odor drive to appetitive and aversive MBONs, respectively: learning that a stimulus is appetitive weakens the connection between KCs encoding that stimulus and the avoidance MBONs, promoting approach, while aversive conditioning weakens the connection between KCs and approach MBONs, promoting avoidance (Aso et al., 2014; Owald and Waddell, 2015; Eschbach and Zlatic, 2020).

According to this model, presentation of CO2 coincident with or prior to the activation of DAN-i1 reduces the ability of CO2 to excite one or more aversive MBONs, likely including MBON-i1, which encodes avoidance (Eschbach and Zlatic, 2020) and is postsynaptic to DAN-i1 (Eichler et al., 2017). This results in an appetitive drive from the MB that cancels out the innate avoidance pathway. Why in our experiments the learned appetitive drive appears to exactly cancel but not overcome the innate aversion should be the subject of further study; it may be a simple coincidence or artifact of the experimental protocol, or it may reflect more profound circuit principles.

Understanding memory formation at the circuit and synaptic levels simultaneously is a heroic task, even aided by the larva’s numerically simple nervous system and the tools (including EM-reconstruction) available in the larva. The work here represents progress toward this goal. We demonstrate long-term protein synthesis dependent memory, implying that memories are encoded in synaptic change. Our assay allows us to precisely identify those individuals who have formed long-term memories. Animals are found in only two behavioral states: innate avoidance or learned indifference; this likely reflects two discrete states of the underlying neural circuit.

Our associative conditioning paradigm pairing CO2 presentation with DAN-i1 activation has experimental advantages for circuit-cracking. The conditioned stimulus is sensed by a single pair of genetically identified sensory neurons; the unconditioned stimulus is provided by activation of a single pair of genetically identified reward neurons whose connectivity has been fully reconstructed (Schleyer et al., 2020). How the larva navigates in response to CO2 presentation has been described in detail (Faucher et al., 2006; Gershow et al., 2012; Gepner et al., 2015; Gepner et al., 2018), as has how neurons downstream of DAN-i1 and the KCs contribute to navigational decision making (Eichler et al., 2017; Saumweber et al., 2018; Thum and Gerber, 2019; Schleyer et al., 2020). This is a particularly favorable starting point to understand how synaptic plasticity due to associative conditioning leads to changes in circuit function that effect changed behavioral outcomes.

### Conclusion

We introduced a Y-maze assay capable of measuring the olfactory preferences of individual larval Drosophila and of in situ associative conditioning. We found that when larvae learn to associate CO2 with reward neuron activation, the result is a switch from innate avoidance to learned indifference, with no intervening states. We demonstrated a protocol to form stable protein-synthesis dependent long term memories. This provides a strong starting point for ‘cracking’ a complete olfactory learning circuit.

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
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w[1118]; P{y[+t7.7]w[+mC]=20XUAS-IVS-CsChrimson.mVenus}attP2 (w;;UAS-CsChrimson)</td>
      <td>Bloomington Stock Center</td>
      <td>RRID:BDSC_55136</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>SS00864 split-Gal4 (DAN-i1-Gal4)</td>
      <td>Saumweber et al., 2018</td>
      <td></td>
      <td>Gift of Marta Zlatic, Janelia Research Campus</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w[*]; Gr63a[1]</td>
      <td>Bloomington Stock Center</td>
      <td>RRID:BDSC_9941</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w[1118]; P{y[+t7.7] w[+mC]=GMR58E02-GAL4}attP2 (GMR58E02-Gal4)</td>
      <td>Bloomington Stock Center</td>
      <td>RRID:BDSC_41347</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w;hs-dCREB2-b 17–2</td>
      <td>Yin et al., 1995</td>
      <td>FlyBase_ FBti0038019</td>
      <td>Gift of Jerry Chi-Ping Yin, University of Wisconsin, Madison</td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w[*]; P{w[+mW.hs]=GawB}ey[OK107]/In(4)ci[D], ci[D] pan[ciD] sv[spa-pol] (OK107-Gal4)</td>
      <td>Bloomington Stock Center</td>
      <td>RRID:BDSC_854</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w[*]; P{w[+mC]=UAS-Hsap\KCNJ2.EGFP}7 (UAS-kir2.1)</td>
      <td>Bloomington Stock Center</td>
      <td>RRID:BDSC_6595</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (D. melanogaster)</td>
      <td>w[*]; P{w[+mC]=Gr21a-GAL4.C}133t52.1 (Gr21a-Gal4)</td>
      <td>Bloomington Stock Center</td>
      <td>RRID:BDSC_23890</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>livetracker</td>
      <td>github.com/GershowLab/TrainingChamber (copy archived at URL swh:1:rev:e2a7ccc4e8d845e6cac59d3b2f344cca826c4727, Lesar, 2021)</td>
      <td>This work</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Crosses and genotypes

#### Larva collection

Flies of the appropriate genotypes (Table 1) were placed in 60 mm embryo-collection cages (59–100, Genessee Scientific) and allowed to lay eggs for 6 hr at 25C on enriched food media (Nutri-Fly German Food, Genesee Scientific). For all experiments except otherwise specified, the food was supplemented with 0.1 mM all-trans-retinal (ATR, Sigma Aldrich R2500). Cages were kept in the dark during egg laying. When eggs were not being collected for experiments, flies were kept on plain food at 18C.

Petri dishes containing eggs and larvae were kept at 25C in the dark for 48–60 hr. Second instar larvae were separated from food using 30% sucrose solution and washed in water. Larvae were selected for size. Preparations for experiments were carried out in a dark room.

**Table 1.**
 Crosses used to generate larvae for experiments throughout this work.For strain information, see key resource table.


<table>
  <thead>
    <tr>
      <th>Figure</th>
      <th>Designation</th>
      <th>Female parent</th>
      <th>Male parent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Gr63a1</td>
      <td colspan="2">w;Gr63a1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>OK107&gt;Kir2.1</td>
      <td>UAS-Kir2.1-GFP</td>
      <td>OK107-Gal4</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Gr21a&gt;Kir2.1</td>
      <td>UAS-Kir2.1-GFP</td>
      <td>Gr21a-Gal4</td>
    </tr>
    <tr>
      <td>1-4</td>
      <td>DANi1&gt;CsChrimson</td>
      <td>w;;UAS-CsChrimson</td>
      <td>SS00864</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Driver ctrl</td>
      <td colspan="2">SS00864</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Effector ctrl</td>
      <td colspan="2">w;;UAS-CsChrimson</td>
    </tr>
    <tr>
      <td>1</td>
      <td>58E02&gt;CsChrimson</td>
      <td>w;;UAS-CsChrimson</td>
      <td>58E02-Gal4</td>
    </tr>
    <tr>
      <td>4</td>
      <td>hs-dcreb2-b;DANi1&gt;CsChrimson</td>
      <td>w;hs-dcreb2-b;UAS-CsChrimson</td>
      <td>SS00864</td>
    </tr>
  </tbody>
</table>

### Y-maze

We used SLA three-dimensional printing to create microfluidic masters for casting (Karagyozov et al., 2018; Chan et al., 2015). Masters were designed in Autodesk Inventor and printed on an Ember three-dimensonal printer (Autodesk) using black prototyping resin (Colorado Photopolymer Solutions). After printing, masters were washed in isopropyl alcohol, air-dried, and baked at 65C for 45 min to remove volatile additives and non-crosslinked resin. 4% agarose (Apex Quick Dissolve LE Agarose, Cat #20-102QD, Genesee Scientific) was poured over the masters and allowed to solidify; then mazes were removed from the mold. Agarose Y-mazes were stored in tap water before use.

The mazes are 1 mm in depth. Each channel is 1.818 mm in length and 0.4 mm in width, and ends in a circular chamber (radius = 1 mm) which redirects larva back to the intersection. An inlet channel (depth = 0.1 mm, length = 1.524 mm, width = 0.1 mm) to the circular chamber connects to tubing for our network of air, CO2, and vacuum sources.

### Behavioral experiments

Individual larvae were selected for size and placed into a Y-maze using a paintbrush. The Y-maze was placed into a PDMS (Sylgard 184, 10:1 base:curing agent) base, where tubing was secured. The Y-maze and base were encased in a dark custom-built box. Larvae were monitored under 850 nm infrared illumination (Everlight Electronics Co Ltd, HIR11-21C/L11/TR8) using a Raspberry Pi NoIR camera (Adafruit, 3100), connected to a Raspberry Pi microcomputer (Raspberry Pi 3 Model B+, Adafruit, 3775). Experiments were recorded using the same camera, operating at 20 fps. Eight copies of the assay were built, to assay the behaviors of multiple larvae in parallel.

Pressure for air, CO2, and vacuum were controlled at the sources (for vacuum regulation: 41585K43, McMaster-Carr; for pressure regulation: 43275K16, McMaster-Carr). CO2 and air were humidified through a bubble humidifier. Vacuum, air, and CO2 tubing to individual assays were separated through a block manifold after pressure control and humidification (BHH2-12, Clippard).

The CO2 concentration was controlled by a resistive network of tubing connected to the air and CO2 sources. This inexpensive alternative to a mass-flow controller produced a stable ratio of CO2 to air that was consistent from day to day and independent of the overall flow rate. The direction of flow was controlled by solenoid pinch valves (NPV2-1C-03–12, Clippard), actuated by a custom circuit we designed.

Custom computer vision software detected the location of the larva in real time. Based on the larva’s location, computer controlled valves manipulated the direction of airflow so that the larva was always presented with a fresh set of choices each time it approached the intersection. The software randomly decided which channel would contain air and which contained air mixed with CO2.

In each maze, one channel was selected to be the outlet for flow and the other two were inlets. An individual larva began in the outlet channel and approached the intersection of the Y-maze, then chose to enter either an inlet branch containing air with CO2 or an inlet branch containing air only. When the larva’s full body entered the chosen channel, software recorded the larva’s choice of channel. When the larva reached the end of that channel and entered the circular chamber, valves switched to turn off CO2 and to switch vacuum to the channel containing larva, making that channel the outlet. The CO2 remained off (the larva experienced only pure air) until the larva exited the circular chamber. When the larva exited the circular chamber and proceeded towards the intersection, CO2 was introduced to one randomly selected inlet channel.

Software recorded the location of the larva at every frame (approx 20 Hz); the direction of airflow in the maze (which channel(s) had air; which channel had CO2 mixed with air, if any; and which channel had vacuum); and all decisions the larva made. We recorded when larvae entered or left a channel, and whether that channel presented CO2. Larvae could take three actions as they approached the intersection: choose the channel containing air with CO2 (scored as APPROACH); choose the channel containing pure air (scored as AVOID); or move backwards into their original channel before they reach the intersection. If a larva backed up and reentered the circular chamber it departed from before reaching the intersection, the software reset and presented the larva with a fresh set of choices when it next left the circle. We did not score backing up as a choice of either CO2 or air.

Following an hour of testing, larvae were trained in the same Y-maze assay used to measure preference. During the training period, unless described otherwise, each 30 s training cycles alternated 15 s of CO2 presentation, where both inlet channels contained a humidified mix of CO2 and air; followed by 15 s of air presentation, where both inlet channels had humidified air alone. This cycle was repeated some number of times (specified for each experiment in the figures). Red LEDs (Sun LD, XZM2ACR55W-3) integrated into the setup were used to activate CsChrimson synchronously with CO2 presentation (paired) or air presentation (reverse-paired).

The volume of the flow chamber was 11.68 mm3 and the volume of the tubing downstream of the valves is approximately 214 mm3. The flow rate exceeded 560 mm3/s, and the state of the chamber was taken to be the same as the state of valves.

Following training, larvae were tested for one hour in an identical scheme to that previously described for the naive measurement.

After larvae were placed into the Y-maze, larva were left in the maze in the dark for a minimum of 5 min. If a larva was not moving through the maze after 5 min, the larva was replaced before the experiment began. If larvae stopped moving through the maze during the first hour of testing, larvae were removed from the maze before training and results were discarded. This happened infrequently (approximately 5% of experiments).

### Protocol for timing dependence experiments

For experiments in Figure 1D, reward presentation was offset from CO2 onset. 30 s training cycles alternated 15 s of CO2 presentation, where both channels contained a mix of CO2 and air; followed by 15 s of air presentation, where neither channel had CO2. Red LEDs are used to activate CsChrimson for 15 s. For some larvae, reward onset occurred 7.5 s after CO2 presentation; for others, reward onset occurred 7.5 s before CO2 presentation. For all experiments of this type, larvae were presented with 20 cycles of training.

For experiments in Figure 1E, 75-second training cycles alternated 15 s of CO2 presentation, where both inlet channels contained a mix of CO2 and air with 60 s of air presentation. For some larvae, reward presentation occurred immediately following CO2 termination for 15 s. For others, reward presentation occurred 15 s prior to CO2 onset, and reward presentation was terminated upon CO2 presentation. For a third group of larvae, we rewarded larvae for 15 s between two CO2 presentations. In this case, 15 s of CO2 presentation was followed by 15 s of reward presentation in the absence of CO2, followed by another 15 s of CO2 presentation. After the second presentation, there was a 30 s air gap before the cycle repeated. For all experiments of these types, larvae were presented with 20 cycles of training.

### Habituation and extinction protocols

For experiments in Figure 3, we used either an extinction or habituation protocol during training. For both types, larvae were tested for 1 hr to determine their innate CO2 preference in the method described above.

For extinction experiments, larvae were trained in the same Y-maze used to measure preference. 30 s training cycles alternate 15 s of CO2 presentation, where both channels contain a mix of CO2 and air; followed by 15 s of air presentation, where neither channel had CO2. Red LEDs were used to activate CsChrimson synchronously with CO2 presentation. This training cycle was repeated some number of times (specified for each experiment above). Immediately after training, we presented the larva with 18 cycles of repeated CO2/air exposure (15 s of CO2 followed by 15 s of air; repeat) with no reward pairing. After these extinction cycles, larva preference for CO2 was tested for one hour.

Habituation experiments were done exactly as for extinction experiments, except that the 18 unrewarded cycles of repeated CO2/air exposure were presented immediately prior to the training cycles.

For experiments in Figure 4B, we tested each larva’s initial preference for one hour, then presented three rewarded paired training cycles. For some larvae (‘Extinction Post-Train’), we then immediately presented 18 extinction cycles, removed the larvae to food overnight as described above, and then tested their preferences for one hour the next day. For another set of larvae (’Extinction Pre-Test’), we removed the larvae to food immediately following training. The next day, after the larvae were cleaned and inserted into the Y-maze, they were exposed to 18 extinction cycles immediately prior to testing their CO2 preferences for 1 hr.

### Overnight memory formation

For the memory retention experiments of Figure 4, testing and training followed identical procedures as above to establish larva preference. After the second round of testing testing, the larvae were removed from the Y-maze assay with a paintbrush and transferred to an individual 4% agar plate (30 mm, FB0875711YZ Fisher Scientific), with yeast paste added. Larvae were kept in the dark at 18 C for approximately 20 hr. Prior to experiments the next day, larva were removed from the agar plate and washed in water before being placed in a new Y-maze. Larvae were then tested for CO2 preference for one hour as previously described. In all experiments in which larvae were removed from the apparatus and later retested, they were placed in the same apparatus but with a new agar Y-maze. Out of 443 larvae placed on agar plates to be tested the following day, 439 larvae were recovered and retested. The four lost larvae were excluded from analysis.

### Cycloheximide feeding protocol

For specified experiments in section Figure 4, larva were raised on ATR- food plates at 25C for 48 hr. Second instar larvae were separated from food using 30% sucrose solution and washed in water. Four hours prior to experiments, larvae were transferred to an agar dish with yeast paste for feeding. Yeast paste was made with either a solution of 35 mM cycloheximide (CXM, Sigma Aldrich C7698) and 0.1 mM all-trans-retinal (ATR, Sigma Aldrich R2500) in 5% sucrose (ATR+/CXM+); or 0.1 mM ATR in 5% sucrose (ATR+/CXM-). To verify CXM ingestion, we placed ATR+/CXM+ and ATR+/CXM- larvae not selected for experiments back on clean food and allowed them to continue development. 95% of ATR+/CXM- larvae pupated, while only 45% of ATR+/CXM+ larvae pupated. Before the experiment, larvae were transferred to an empty petri dish and washed with tap water before being placed into a maze. Except where noted, the same experimental protocol was followed as for non-CXM overnight memory.

### Protocol for cycloheximide experiments

For the CXM experiments in section Figure 4, larvae were trained with either a massed or spaced training protocol. The 20x massed training protocol was as previously described for other experiments in Figure 4.

In the 10x spaced training protocol, larvae were first tested for 1 hr to determine their initial CO2 preference. They then received two cycles of paired DAN-i1 activation with CO2 presentation (15 s of CO2 presentation paired with reward, followed by 15 s of air presentation), followed by 15 min of air presentation. This was then repeated five times (10 activations total). In these experiments, we did not test the larvae immediately following training but instead removed them to food and tested their preferences the next day only.

The 10x massed training protocol was identical to the 10x spaced training protocol, except training consisted of 10 sequential cycles of paired DAN-i1 activation with CO2 presentation (15 s of CO2 presentation paired with reward, followed by 15 s of air presentation, repeated 10 times). As in the spaced training experiments, larvae were removed to food immediately following training, and their preferences were tested the next day only.

### hs-dCREB2-b heat-shock protocol

Petri dishes with larvae were placed in an oven at 37°C for 30 min. The petri dish was placed in a water bath in the oven and covered to preserve humidity and to ensure ATR+ larvae were kept in the dark. The larvae were then removed to 25°C for a 30 min recovery period before experiments. Experiments began immediately after the recovery period. Larvae were kept in the dark at all times during this protocol.

Larvae were tested for CO2 preference prior to training, immediately following training, and the next day, after being kept overnight on food without ATR. Some larvae in the spaced training groups were not active immediately following training. In the heat-shocked group, 11 out of 24 larvae made less than five decisions during the immediate test; in the not-heat-shocked group, 6 out of 22 larvae made less than five decisions during the immediate test. For this scheme, larvae were in the Y-maze for longer than previous experiments, as the spaced training protocol is 80 min (compared to approximately 10 min or less for the standard massed training). All larvae were retested the following day, even if the larva did not make many decisions when tested immediately following training. After the overnight rest period, all non-heat-shocked and 20/24 heat-shocked larvae were active in the final test period. Inactive larvae were included in the analysis and in the bootstrapping of error bars, but contributed little to the population measure because of the few decisions made.

### Development of initial protocols

There are a number of parameters that can be adjusted in our assay, including the identity and concentration of gas used as a CS, the concentration and timing of ATR feeding, the period, duty cycle, and number of CS and US presentations, and duration of behavioral readouts before and after training. We began with our normal protocol for optogenetic activation (Gepner et al., 2015; Gepner et al., 2018): eggs were laid on ATR supplemented food, and larvae were raised in the dark. We somewhat arbitrarily chose a 30 s, 50% duty cycle applied for 20 cycles as our standard for paired training presentation; we began with DANi1>CsChrimson based on previous work (Saumweber et al., 2018; Thum and Gerber, 2019; Schleyer et al., 2020; Weiglein et al., 2019; Eschbach et al., 2020b), and the fact that CsChrimson can be activated via red light without provoking a strong visual response. We then adjusted the CO2 concentration to maximize the contrast between CO2 preference before and after training. From this basic platform, we changed as little as possible while manipulating the parameter of interest, for example we maintained the 30 s 50% duty cycle paired training while changing the number of cycles, or we maintained 20 cycles while varying the temporal sequence of CS and US presentation, or we used exactly the same 30 s, 50% duty cycle, 20 cycle paired protocol while changing the driver to RF58E02.

### Data analysis

The probability of choosing the CO2 containing channel was scored for individual larvae and for populations as

$$
ProbchooseCO_{2}=\frac{#APPROACH}{#APPROACH+#AVOID}
$$

The population average was determined by dividing the total number of times any larva in the population chose the CO2 containing channel by the total number of times any larva chose either channel. In other words, larvae that made more decisions contributed more heavily to the average.

The number of larva and total number of approach and avoid decisions made by larvae for each type of experiment is shown in Table 2. Error bars for 'probability choose CO2’ data displays and all significance tests in the figures were generated by bootstrapping.

**Table 2.**
 Data for experiments in Figure 1, Figure 2, Figure 3, and Figure 4.# Larva: number of individual larvae tested for experiment type; # Approach Pre-Train: total number of times all larvae chose the channel containing air with CO2 prior to training; # Avoid Pre-Train: total number of times all larvae chose the channel containing pure air prior to training; # Approach Post-Train: total number of times all larvae chose the channel containing air with CO2 after the indicated training scheme; # Avoid Post-Train: total number of times all larvae chose the channel containing pure air after the indicated training scheme; # Approach Next Day: total number of times all larvae chose the channel containing air with CO2 during testing approximately 20 hr after training; # Avoid Next: total number of times all larvae chose the channel containing pure air during testing approximately 20 hr after training. All tests were 1 hr (for each larva).


<table>
  <thead>
    <tr>
      <th>Experiment</th>
      <th>Genotype</th>
      <th># Larva</th>
      <th># Approach Pre-Train</th>
      <th># Avoid Pre-Train</th>
      <th># Approach Post-Train</th>
      <th># Avoid Post-Train</th>
      <th># Approach Next Day</th>
      <th># Avoid Next Day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Figure 1B</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gr63a1</td>
      <td>Gr63a1</td>
      <td>44</td>
      <td>831</td>
      <td>745</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>DANi1&gt; CsChrimson, ATR+</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>159</td>
      <td>1714</td>
      <td>4978</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>DANi1&gt; CsChrimson, ATR-</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>16</td>
      <td>256</td>
      <td>614</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 1D</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Paired</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>64</td>
      <td>561</td>
      <td>1760</td>
      <td>936</td>
      <td>868</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Offset After</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>20</td>
      <td>288</td>
      <td>757</td>
      <td>316</td>
      <td>305</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Reverse Paired</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>29</td>
      <td>315</td>
      <td>1022</td>
      <td>154</td>
      <td>530</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Offset Before</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>19</td>
      <td>218</td>
      <td>512</td>
      <td>136</td>
      <td>315</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Paired, ATR-</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>16</td>
      <td>256</td>
      <td>614</td>
      <td>127</td>
      <td>307</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>No Training</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>50</td>
      <td>578</td>
      <td>1599</td>
      <td>479</td>
      <td>1295</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>DAN w/o CO2</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>16</td>
      <td>260</td>
      <td>597</td>
      <td>161</td>
      <td>354</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Driver ctrl</td>
      <td>SS00864</td>
      <td>17</td>
      <td>110</td>
      <td>289</td>
      <td>158</td>
      <td>358</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Effector ctrl</td>
      <td>UAS-CsChrimson</td>
      <td>18</td>
      <td>214</td>
      <td>516</td>
      <td>114</td>
      <td>294</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>58E02&gt; CsChrimson</td>
      <td>58E02&gt; CsChrimson</td>
      <td>21</td>
      <td>380</td>
      <td>912</td>
      <td>493</td>
      <td>501</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 1E</td>
      <td>DANi1&gt; CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Forward Paired</td>
      <td></td>
      <td>22</td>
      <td>181</td>
      <td>496</td>
      <td>350</td>
      <td>337</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Backwards Paired</td>
      <td></td>
      <td>18</td>
      <td>181</td>
      <td>438</td>
      <td>124</td>
      <td>320</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Btw CO2</td>
      <td></td>
      <td>23</td>
      <td>272</td>
      <td>652</td>
      <td>165</td>
      <td>283</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 1F</td>
      <td>DANi1&gt; CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>6.5%</td>
      <td></td>
      <td>19</td>
      <td>361</td>
      <td>568</td>
      <td>319</td>
      <td>290</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>8%</td>
      <td></td>
      <td>27</td>
      <td>256</td>
      <td>567</td>
      <td>295</td>
      <td>255</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>15%</td>
      <td></td>
      <td>19</td>
      <td>170</td>
      <td>368</td>
      <td>249</td>
      <td>233</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>18%</td>
      <td></td>
      <td>64</td>
      <td>561</td>
      <td>1760</td>
      <td>936</td>
      <td>868</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 2A</td>
      <td>DANi1&gt; CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>0 Cycles</td>
      <td></td>
      <td>50</td>
      <td>578</td>
      <td>1599</td>
      <td>479</td>
      <td>1295</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>1 Cycles</td>
      <td></td>
      <td>35</td>
      <td>218</td>
      <td>606</td>
      <td>317</td>
      <td>495</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>2 Cycles</td>
      <td></td>
      <td>87</td>
      <td>840</td>
      <td>2552</td>
      <td>1081</td>
      <td>1292</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>3 Cycles</td>
      <td></td>
      <td>31</td>
      <td>310</td>
      <td>930</td>
      <td>686</td>
      <td>686</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>4 Cycles</td>
      <td></td>
      <td>32</td>
      <td>245</td>
      <td>712</td>
      <td>493</td>
      <td>511</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>5 Cycles</td>
      <td></td>
      <td>63</td>
      <td>863</td>
      <td>2491</td>
      <td>975</td>
      <td>993</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>10 Cycles</td>
      <td></td>
      <td>14</td>
      <td>100</td>
      <td>287</td>
      <td>154</td>
      <td>144</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>20 Cycles</td>
      <td></td>
      <td>64</td>
      <td>561</td>
      <td>1760</td>
      <td>936</td>
      <td>868</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 3B</td>
      <td>DANi1&gt; CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2 Cycles, Training</td>
      <td></td>
      <td>87</td>
      <td>840</td>
      <td>2552</td>
      <td>1081</td>
      <td>1292</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>2 Cycles, Habituation + Training</td>
      <td></td>
      <td>30</td>
      <td>385</td>
      <td>1127</td>
      <td>422</td>
      <td>554</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>2 Cycles, Training + Extinction</td>
      <td></td>
      <td>30</td>
      <td>336</td>
      <td>946</td>
      <td>375</td>
      <td>793</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>3 Cycles, Training</td>
      <td></td>
      <td>30</td>
      <td>308</td>
      <td>924</td>
      <td>675</td>
      <td>679</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>3 Cycles, Habituation + Training</td>
      <td></td>
      <td>18</td>
      <td>222</td>
      <td>591</td>
      <td>260</td>
      <td>294</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>3 Cycles, Training + Extinction</td>
      <td></td>
      <td>26</td>
      <td>279</td>
      <td>695</td>
      <td>195</td>
      <td>416</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>4 Cycles, Training</td>
      <td></td>
      <td>30</td>
      <td>225</td>
      <td>659</td>
      <td>490</td>
      <td>502</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>4 Cycles, Habituation + Training</td>
      <td></td>
      <td>18</td>
      <td>239</td>
      <td>701</td>
      <td>372</td>
      <td>352</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>4 Cycles, Training + Extinction</td>
      <td></td>
      <td>27</td>
      <td>384</td>
      <td>1074</td>
      <td>394</td>
      <td>475</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>5 Cycles, Training</td>
      <td></td>
      <td>63</td>
      <td>863</td>
      <td>2491</td>
      <td>975</td>
      <td>993</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>6 Cycles, Habituation + Training</td>
      <td></td>
      <td>19</td>
      <td>266</td>
      <td>758</td>
      <td>367</td>
      <td>324</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>6 Cycles, Training + Extinction</td>
      <td></td>
      <td>18</td>
      <td>253</td>
      <td>687</td>
      <td>309</td>
      <td>317</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>10 Cycles, Training</td>
      <td></td>
      <td>14</td>
      <td>100</td>
      <td>287</td>
      <td>154</td>
      <td>144</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>10 Cycles, Habituation + Training</td>
      <td></td>
      <td>30</td>
      <td>406</td>
      <td>1193</td>
      <td>607</td>
      <td>503</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>10 Cycles, Training + Extinction</td>
      <td></td>
      <td>30</td>
      <td>426</td>
      <td>1180</td>
      <td>401</td>
      <td>386</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 4B</td>
      <td>DANi1&gt; CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>20x</td>
      <td></td>
      <td>28</td>
      <td>380</td>
      <td>1172</td>
      <td>509</td>
      <td>499</td>
      <td>459</td>
      <td>409</td>
    </tr>
    <tr>
      <td>20x (Only Test Next Day)</td>
      <td></td>
      <td>14</td>
      <td>224</td>
      <td>768</td>
      <td>-</td>
      <td>-</td>
      <td>296</td>
      <td>250</td>
    </tr>
    <tr>
      <td>5x</td>
      <td></td>
      <td>29</td>
      <td>472</td>
      <td>1427</td>
      <td>488</td>
      <td>480</td>
      <td>404</td>
      <td>461</td>
    </tr>
    <tr>
      <td>2x</td>
      <td></td>
      <td>42</td>
      <td>514</td>
      <td>1537</td>
      <td>594</td>
      <td>693</td>
      <td>201</td>
      <td>548</td>
    </tr>
    <tr>
      <td>2x (Only Test Next Day)</td>
      <td></td>
      <td>22</td>
      <td>209</td>
      <td>696</td>
      <td>-</td>
      <td>-</td>
      <td>213</td>
      <td>283</td>
    </tr>
    <tr>
      <td>No Train</td>
      <td></td>
      <td>20</td>
      <td>316</td>
      <td>889</td>
      <td>187</td>
      <td>544</td>
      <td>104</td>
      <td>337</td>
    </tr>
    <tr>
      <td>RP 20x</td>
      <td></td>
      <td>21</td>
      <td>282</td>
      <td>905</td>
      <td>121</td>
      <td>430</td>
      <td>109</td>
      <td>361</td>
    </tr>
    <tr>
      <td>Ext Post-Train</td>
      <td></td>
      <td>23</td>
      <td>181</td>
      <td>477</td>
      <td>-</td>
      <td>-</td>
      <td>158</td>
      <td>365</td>
    </tr>
    <tr>
      <td>Ext Pre-Test</td>
      <td></td>
      <td>31</td>
      <td>417</td>
      <td>1002</td>
      <td>-</td>
      <td>-</td>
      <td>385</td>
      <td>429</td>
    </tr>
    <tr>
      <td>Figure 4C</td>
      <td>DANi1&gt; CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>M 20x (CXM+/ATR+)</td>
      <td></td>
      <td>20</td>
      <td>110</td>
      <td>282</td>
      <td>252</td>
      <td>237</td>
      <td>237</td>
      <td>272</td>
    </tr>
    <tr>
      <td>M 20x (CXM-/ATR+)</td>
      <td></td>
      <td>17</td>
      <td>159</td>
      <td>419</td>
      <td>271</td>
      <td>236</td>
      <td>228</td>
      <td>235</td>
    </tr>
    <tr>
      <td>S 20x (CXM+/ATR+)</td>
      <td></td>
      <td>23</td>
      <td>191</td>
      <td>486</td>
      <td>-</td>
      <td>-</td>
      <td>150</td>
      <td>316</td>
    </tr>
    <tr>
      <td>S 20x (CXM-/ATR+)</td>
      <td></td>
      <td>20</td>
      <td>197</td>
      <td>511</td>
      <td>-</td>
      <td>-</td>
      <td>254</td>
      <td>264</td>
    </tr>
    <tr>
      <td>M 10x (CXM+/ATR+)</td>
      <td></td>
      <td>23</td>
      <td>136</td>
      <td>345</td>
      <td>-</td>
      <td>-</td>
      <td>331</td>
      <td>344</td>
    </tr>
    <tr>
      <td>M 10x (CXM-/ATR+)</td>
      <td></td>
      <td>20</td>
      <td>175</td>
      <td>454</td>
      <td>-</td>
      <td>-</td>
      <td>419</td>
      <td>375</td>
    </tr>
    <tr>
      <td>Figure 4D</td>
      <td>DANi1&gt; hs-dCREB2-b;CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>M 10x HS</td>
      <td></td>
      <td>21</td>
      <td>175</td>
      <td>434</td>
      <td>392</td>
      <td>370</td>
      <td>253</td>
      <td>246</td>
    </tr>
    <tr>
      <td>M 10x No HS</td>
      <td></td>
      <td>22</td>
      <td>248</td>
      <td>656</td>
      <td>367</td>
      <td>353</td>
      <td>451</td>
      <td>490</td>
    </tr>
    <tr>
      <td>S 10x HS</td>
      <td></td>
      <td>24</td>
      <td>172</td>
      <td>420</td>
      <td>68</td>
      <td>156</td>
      <td>153</td>
      <td>339</td>
    </tr>
    <tr>
      <td>S 10x No HS</td>
      <td></td>
      <td>22</td>
      <td>294</td>
      <td>736</td>
      <td>212</td>
      <td>184</td>
      <td>335</td>
      <td>352</td>
    </tr>
  </tbody>
</table>

For each experimental set, we performed the bootstrapping as follows. If there were X larvae from that experiment, we selected X larvae with replacement from that set. Then, from each larvae selected, we selected with replacement from the decisions that larvae had made. For example, if the larvae had made Y ‘approach’ and Z ‘avoid’ decisions, we selected (Y+Z) decisions with replacement from that set to represent the larvae. We then calculated the population average from this generated set of animals. We generated 10,0000 numerical replicates using this bootstrapping method. Error bars were the standard deviation of these replicates. Note that in each replicate, the same animals were included in each (e.g. trained and untrained) group.

A p-value $p<x$ indicates that at least $x$ fraction of these replicates ended with the same ranking result (e.g. $p<0.01$ between trained and untrained would indicate that in at least 9900 out of 10,000 replicates, the trained group had a larger CO2 preference than the untrained group or vice versa). These p-values are included in the ‘Hierarchical Bootstrap’ column of Table 3.

**Table 3.**
 p-Values for experiments in Figure 1, Figure 2, Figure 3, and Figure 4.P-values for experiments were calculated: Bootstrap - p-values calculated as explained in Materials and methods; Fisher - p-values calculated using Fisher’s exact test; U-test - p-values calculated using two-sided Mann–Whitney U test. Unless otherwise noted, p-values are calculated between pre-train and post-train data. A shaded row indicates not all tests reach the same significance level (out of ns, p <0.05, p <0.01, p <0.001).


<table>
  <thead>
    <tr>
      <th>Experiment</th>
      <th>Genotype</th>
      <th>Hierarchical Bootstrap</th>
      <th>Bootstrap Animal Only</th>
      <th>Fisher</th>
      <th>U-test</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Figure 1B</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gr63a1/DANi1&gt; CsChrimson, ATR+</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>Gr63a1/DANi1&gt; CsChrimson, ATR-</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>Figure 1D</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Paired</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>Offset After</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>Reverse Paired</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>0.3429</td>
      <td>0.2689</td>
      <td>0.6166</td>
      <td>0.9379</td>
    </tr>
    <tr>
      <td>Offset Before</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>0.4479</td>
      <td>0.4373</td>
      <td>0.9479</td>
      <td>0.9770</td>
    </tr>
    <tr>
      <td>Paired, ATR-</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>0.4762</td>
      <td>0.4315</td>
      <td>1.000</td>
      <td>0.2658</td>
    </tr>
    <tr>
      <td>No Training</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>0.4066</td>
      <td>0.3664</td>
      <td>0.7726</td>
      <td>0.9835</td>
    </tr>
    <tr>
      <td>DAN w/o CO2</td>
      <td>DANi1&gt; CsChrimson</td>
      <td>0.3935</td>
      <td>0.3102</td>
      <td>0.7173</td>
      <td>0.4852</td>
    </tr>
    <tr>
      <td>Driver ctrl</td>
      <td>SS00864</td>
      <td>0.3106</td>
      <td>0.0313</td>
      <td>0.3411</td>
      <td>0.3977</td>
    </tr>
    <tr>
      <td>Effector ctrl</td>
      <td>UAS-CsChrimson</td>
      <td>0.3383</td>
      <td>0.2361</td>
      <td>0.6336</td>
      <td>0.8366</td>
    </tr>
    <tr>
      <td>58E02&gt; CsChrimson</td>
      <td>58E02&gt; CsChrimson</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>Figure 1C</td>
      <td>DANi1&gt; CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Forward Paired</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>Backwards Paired</td>
      <td></td>
      <td>0,3368</td>
      <td>0.163</td>
      <td>0.6801</td>
      <td>0.1939</td>
    </tr>
    <tr>
      <td>Btw CO2</td>
      <td></td>
      <td>0.0107</td>
      <td>0.0001</td>
      <td>0.006543</td>
      <td>0.0003257</td>
    </tr>
    <tr>
      <td>Figure 1D</td>
      <td>DANi1&gt; CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>6.5%</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>8%</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>15%</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>18%</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>Figure 2A</td>
      <td>DANi1&gt; CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>0 Cycles</td>
      <td></td>
      <td>0.4132</td>
      <td>0.3647</td>
      <td>0.7726</td>
      <td>0.9835</td>
    </tr>
    <tr>
      <td>1 Cycles</td>
      <td></td>
      <td>0.0003</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>0.0591</td>
    </tr>
    <tr>
      <td>2 Cycles</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>3 Cycles</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>4 Cycles</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>5 Cycles</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>10 Cycles</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>20 Cycles</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>Figure 3B</td>
      <td>DANi1&gt; CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2 Cycles, Training</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>2 Cycles, Habituation + Training</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>2 Cycles, Training + Extinction</td>
      <td></td>
      <td>0.0117</td>
      <td>0.0020</td>
      <td>0.001339</td>
      <td>0.04743</td>
    </tr>
    <tr>
      <td>3 Cycles, Training</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>3 Cycles, Habituation + Training</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>0.0007459</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>3 Cycles, Training + Extinction</td>
      <td></td>
      <td>0.1133</td>
      <td>0.0176</td>
      <td>0.1763</td>
      <td>0.03069</td>
    </tr>
    <tr>
      <td>4 Cycles, Training</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>4 Cycles, Habituation + Training</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>4 Cycles, Training + Extinction</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>5 Cycles, Training</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>6 Cycles, Habituation + Training</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>6 Cycles, Training + Extinction</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>10 Cycles, Training</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>10 Cycles, Habituation + Training</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>10 Cycles, Training + Extinction</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>Figure 4B</td>
      <td>DANi1&gt; CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>20x Pre-Test/Post-Test</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>20x Pre-Test/Next Day</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>20x (Only Test Next Day) Pre-Test/Next Day</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>5x Pre-Test/Post-Test</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>5x Pre-Test/Next Day</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>2x Pre-Test/Post-Test</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>2x Pre-Test/Next Day</td>
      <td></td>
      <td>0.2086</td>
      <td>0.0501</td>
      <td>0.3524</td>
      <td>0.07216</td>
    </tr>
    <tr>
      <td>2x (Only Test Next Day) Pre-Test/Next Day</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>No Train Pre-Test/Post-Test</td>
      <td></td>
      <td>0.4035</td>
      <td>0.3319</td>
      <td>0.7893</td>
      <td>0.2003</td>
    </tr>
    <tr>
      <td>No Train Pre-Test/Next Day</td>
      <td></td>
      <td>0.1583</td>
      <td>0.0530</td>
      <td>0.3071</td>
      <td>0.8884</td>
    </tr>
    <tr>
      <td>RP 20x Pre-Test/Post-Test</td>
      <td></td>
      <td>0.2677</td>
      <td>0.1507</td>
      <td>0.4276</td>
      <td>0.7396</td>
    </tr>
    <tr>
      <td>RP 20x Pre-Test/Next Day</td>
      <td></td>
      <td>0.4205</td>
      <td>0.3481</td>
      <td>0.8474</td>
      <td>0.3765</td>
    </tr>
    <tr>
      <td>Ext Post-Train Pre-Test/Next Day</td>
      <td></td>
      <td>0.1801</td>
      <td>0.0146</td>
      <td>0.3315</td>
      <td>0.01336</td>
    </tr>
    <tr>
      <td>Ext Pre-Test Pre-Test/Next Day</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>Figure 4C</td>
      <td>DANi1&gt; CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>M 20x (CXM+/ATR+) Pre-Test/Post-Test</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>M 20x (CXM+/ATR+) Pre-Test/Next Day</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>M 20x (CXM-/ATR+) Pre-Test/Post-Test</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>M 20x (CXM-/ATR+) Pre-Test/Next Day</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>S 10x (CXM+/ATR+) Pre-Test/Next Day</td>
      <td></td>
      <td>0.1099</td>
      <td>0.014</td>
      <td>0.1671</td>
      <td>0.02985</td>
    </tr>
    <tr>
      <td>S 10x (CXM-/ATR+) Pre-Test/Next Day</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>M 10x (CXM+/ATR+) Pre-Test/Next Day</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>M 10x (CXM-/ATR+) Pre-Test/Next Day</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>Figure 4D</td>
      <td>DANi1&gt; hs-dCREB2-b;CsChrimson</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>M 10x, HS Pre-Test/Post-Test</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>M 10x, HS Pre-Test/Next Day</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>M 10x, No HS Pre-Test/Post-Test</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>M 10x, No HS Pre-Test/Next Day</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>S 10x, HS Pre-Test/Post-Test</td>
      <td></td>
      <td>0.3804</td>
      <td>0.2830</td>
      <td>0.7310</td>
      <td>0.2750</td>
    </tr>
    <tr>
      <td>S 10x, HS Pre-Test/Next Day</td>
      <td></td>
      <td>0.2645</td>
      <td>0.08860</td>
      <td>0.4650</td>
      <td>0.3802</td>
    </tr>
    <tr>
      <td>S 10x, No HS Pre-Test/Post-Test</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
    <tr>
      <td>S 10x, No HS Pre-Test/Next Day</td>
      <td></td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
      <td>&lt;10−4</td>
    </tr>
  </tbody>
</table>

We also performed a non-hierarchical bootstrap, in which animals were resampled but their decisions were not, preserving any correlations between decisions. In this case, we generated 10,000 numerical replicates by selecting with replacement from that set of larvae; the actual sequence of decisions made by the resampled larvae was then used without further resampling. A p-value $p<x$ indicates that at least $x$ fraction of these replicates ended with the same ranking result. These p-values are included in the ‘Bootstrap Animal Only’ column of Table 3. In Table 3, we also show p-values for the Fisher’s exact test, which treats every decision as independent, and the Mann-Whitney u-test, which treats every larva in each group as a discrete measurement and does not account for differing numbers of decisions made by larvae.

To fit the data in Figure 2 to various models, we used a maximum-likelihood approach. First we grouped the larvae according to the number of cycles (nc) of training they received. In each group, for each larva we quantified the number of decisions made following training. The number of decisions made by the $j^{t⁢h}$ larva that received nc cycles of training was $n⁢(n_{c},j)$ and the fraction of times the larva chose the CO2 containing channel was $p⁢(n_{c},j)$. Then we sought a set of parameters $\theta$ that maximized

$$
\sumn_{c}\sumjlog⁡P⁢(p⁢(n_{c},j)|n⁢(n_{c},j),\theta)
$$

where $P$ was the model specific-probability function. For instance, for the quantized learning (two-Gaussian shifting fraction) model:

$$
P(p(n_{c},j)|n(n_{c},j),\theta)=f_{u}(n_{c})𝒩(p(n_{c},j),\mu_{u},\sigma~\sqrt{\frac{\mu_{u}∗(1−\mu_{u})}{n(n_{c},j)}})+(1−f_{u}(n_{c}))𝒩(p(n_{c},j),\mu_{t},\sigma~\sqrt{\frac{\mu_{t}∗(1−\mu_{t})}{n(n_{c},j)}})
$$

where $𝒩⁢(x,\mu,\sigma)=\frac{1}{\sqrt{2⁢\pi⁢\sigma^{2}}}⁢exp-\frac{(x-\mu)^{2}}{2⁢\sigma^{2}}$ and the parameters $\theta$ are

$$
\theta={\mu_{u},\mu_{t},\sigma~,f_{u}⁢(0),f_{u}⁢(1),f_{u}⁢(2),f_{u}⁢(3),f_{u}⁢(4),f_{u}⁢(5),f_{u}⁢(10),f_{u}⁢(20)}
$$

The parameter $\sigma~$ represents an adjustment to the expected variance due to counting statistics. If all larva chose randomly and independently from the two channels with a fixed probability $p¯$ of choosing CO2, then we would expect that the number of times the CO2 containing channel would be binomially distributed. For ease of computation, we approximated the binomial distribution as a normal distribution. In this case, the probability density of observing $p⁢(n_{c},j)$ given $n⁢(n_{c},j)$ would be normally distributed with mean $p¯$ and variance

$$
\sigma^{2}=\frac{(p¯)⁢(1-p¯)}{n⁢(n_{c},j)}
$$

In fact, we found that after choosing a CO2 containing channel, both naive and trained larvae are less likely to choose the CO2 containing channel the next time they approach the intersection. Because the choices are not independent, the variance of the mean of a series of choices is not given by Equation 7. Instead, we modeled the variance as

$$
\sigma^{2}=\sigma~^{2}⁢\frac{(p¯)⁢(1-p¯)}{n⁢(n_{c},j)}
$$

where $\sigma~$ was a global fit parameter in the shifting and exponential fraction models and in the shifting mean model a function of the amount training. This formulation preserves the properties that the variance should increase as the mean probability of choosing CO2 approaches 50% and should be larger when fewer decisions are averaged together. However, if we instead just assume a single global σ, the results of our analysis (that the exponential fraction model is preferred) are unchanged.

In the graded learning (single Gaussian with shifting mean and variance) model, µ and σ were allowed to change as a function of training. The probability of an individual observation was

$$
P⁢(p⁢(n_{c},j)|n⁢(n_{c},j),\theta)=𝒩⁢(p⁢(n_{c},j),\mu⁢(n_{c}),\frac{\sigma⁢(n_{c})}{\sqrt{n⁢(n_{c},j)}})
$$

and the parameters were

$$
\theta={\mu⁢(0),\sigma⁢(0),\mu⁢(1),\sigma⁢(1),\mu⁢(2),\sigma⁢(2),\mu⁢(3),\sigma⁢(3),\mu⁢(4),\sigma⁢(4),\mu⁢(5),\sigma⁢(5),\mu⁢(10),\sigma⁢(10),\mu⁢(20),\sigma⁢(20)}
$$

The exponential fraction model is identical to the quantized learning model, except that the fraction of untrained larvae is an exponentially decreasing function of the number of training cycles:

$$
f_{u}⁢(n_{c})=\lambda^{n_{c}}
$$

and the parameters were

$$
\theta={\mu_{u},\mu_{t},\sigma~,\lambda}
$$

These models were then fit to the data by maximizing the log-likelihood of the observed data set using the MATLAB function fmincon. The predictions of these fits are shown in Figure 2. These results are summarized in Table 4, along with the Aikake and Bayes Information Criterion, AIC and BIC, which are used to compare models with different numbers of parameters. According to both AIC and BIC, the exponential fraction model is strongly favored.

**Table 4.**
 Model fits to data in Figure 2.Shifting Mean and $\sigma~$, shifting fraction, and exponential fraction models are presented in Figure 2. Model name: name of the model. Formula: expression for the probability of the data given the model and its parameters. # params: number of free parameters in the model. $Δ⁢log⁡(P)$ logarithm of the probability of the data given best fit to this model minus logarithm of the probability of the data given the best fit model overall. A higher (less negative) value means the model better fits the data without regard to the number of parameters. $Δ⁢A⁢I⁢C$, $Δ⁢B⁢I⁢C$ - Aikake and Bayes Information Criterion minus the lowest values over the models tested. Lower numbers indicate model is favored. According to both criterion, the exponential fraction model is strongly favored over the shifting fraction model, and the shifting fraction model is strongly favored over all models except the exponential fractional model.


<table>
  <thead>
    <tr>
      <th>Model name</th>
      <th>Formula</th>
      <th># params</th>
      <th>Δ⁢log⁡(P)</th>
      <th>Δ⁢AIC</th>
      <th>Δ⁢BIC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Shifting Mean (fixed σ~)</td>
      <td>P∝∏nc∈(0,1,2,3,4,5,10,20)∏j𝒩⁢(p⁢(nc,j),μ⁢(nc),σ~⁢μ⁢(nc)*(1-μ⁢(nc))n⁢(nc,j))</td>
      <td>9</td>
      <td>−42.7</td>
      <td>84.86</td>
      <td>104.45</td>
    </tr>
    <tr>
      <td>Shifting Mean and σ (Graded learning)</td>
      <td>P∝∏nc∈(0,1,2,3,4,5,10,20)∏j𝒩⁢(p⁢(nc,j),μ⁢(nc),σ⁢(nc)n⁢(nc,j))</td>
      <td>16</td>
      <td>−12.9</td>
      <td>39.3</td>
      <td>86.3</td>
    </tr>
    <tr>
      <td>Shifting Fraction (Quantized learning)</td>
      <td>P∝∏nc∈(0,1,2,3,4,5,10,20)∏jfu⁢(nc)⁢𝒩⁢(p⁢(nc,j),μu,σ~⁢μu*(1-μu)n⁢(nc,j))+ …(1-fu⁢(nc))⁢𝒩⁢(p⁢(nc,j),μt,σ~⁢μt*(1-μt)n⁢(nc,j))</td>
      <td>11</td>
      <td>−3.93</td>
      <td>11.3</td>
      <td>38.7</td>
    </tr>
    <tr>
      <td>Shifting Fraction (3 clusters)</td>
      <td>P∝∏nc∈(0,1,2,3,4,5,10,20)∏jf1⁢(nc)⁢𝒩⁢(p⁢(nc,j),μ1,σ~⁢μ1*(1-μ1)n⁢(nc,j))+ …f2(nc)𝒩(p(nc,j),μ2,σ~μ2∗(1−μ2)n(nc,j))+ …(1-f1⁢(nc)-f2⁢(nc))⁢𝒩⁢(p⁢(nc,j),μ3,σ~⁢μ3*(1-μ3)n⁢(nc,j))</td>
      <td>20</td>
      <td>0</td>
      <td>21.4</td>
      <td>84.1</td>
    </tr>
    <tr>
      <td>Exponential Fraction (All-or-none)</td>
      <td>P∝∏nc∈(0,1,2,3,4,5,10,20)∏jλnc⁢𝒩⁢(p⁢(nc,j),μu,σ~⁢μu*(1-μu)n⁢(nc,j))+ …(1-λnc)⁢𝒩⁢(p⁢(nc,j),μt,σ~⁢μt*(1-μt)n⁢(nc,j))</td>
      <td>4</td>
      <td>−5.3</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

Throughout the paper 'Fraction of larvae trained’ represents the best fit to the two Gaussian shifting fraction model. The error bars represent the uncertainty in the model fit. Specifically, they represent the range of $f$ over which

$$
log⁡P⁢(data|\theta_{0},f)\geqlog⁡P⁢(data|\theta_{0},f_{0})-\frac{1}{2}
$$

where $f$ is the fraction of trained larvae, f0, is the best fit fraction of trained larvae, and $\theta_{0}$ represents the best fit of the remainder of the parameters, which are not adjusted.
