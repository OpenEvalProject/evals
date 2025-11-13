# Statistical learning shapes pain perception and prediction independently of external cues

## Authors

- Jakub Onysk<sup>1</sup> ([ORCID: 0000-0003-0876-5465](https://orcid.org/0000-0003-0876-5465)) †
- Nicholas Gregory<sup>1</sup>
- Mia Whitefield<sup>1</sup>
- Maeghal Jain<sup>1</sup>
- Georgia Turner<sup>1</sup>
- Ben Seymour<sup>4</sup> ([ORCID: 0000-0003-1724-5832](https://orcid.org/0000-0003-1724-5832))
- Flavia Mancini<sup>1</sup> ([ORCID: 0000-0001-8441-9236](https://orcid.org/0000-0001-8441-9236)) †

### Affiliations

1. Computational and Biological Learning Unit, Department of Engineering, University of Cambridge Cambridge United Kingdom ([ROR:013meh722](https://ror.org/013meh722))
2. Applied Computational Psychiatry Lab, Max Planck Centre for Computational Psychiatry and Ageing Research, Queen Square Institute of Neurology and Mental Health Neuroscience Department, Division of Psychiatry, University College London London United Kingdom ([ROR:02jx3x895](https://ror.org/02jx3x895))
3. MRC Cognition and Brain Sciences Unit, University of Cambridge Cambridge United Kingdom ([ROR:013meh722](https://ror.org/013meh722))
4. Wellcome Centre for Integrative Neuroimaging, John Radcliﬀe Hospital, Headington Oxford United Kingdom ([ROR:0080acb59](https://ror.org/0080acb59))
5. Center for Information and Neural Networks (CiNet) Osaka Japan

† Corresponding author

## Abstract

The placebo and nocebo effects highlight the importance of expectations in modulating pain perception, but in everyday life we don’t need an external source of information to form expectations about pain. The brain can learn to predict pain in a more fundamental way, simply by experiencing ﬂuctuating, non-random streams of noxious inputs, and extracting their temporal regularities. This process is called statistical learning. Here, we address a key open question: does statistical learning modulate pain perception? We asked 27 participants to both rate and predict pain intensity levels in sequences of ﬂuctuating heat pain. Using a computational approach, we show that probabilistic expectations and confidence were used to weigh pain perception and prediction. As such, this study goes beyond well-established conditioning paradigms associating non-pain cues with pain outcomes, and shows that statistical learning itself shapes pain experience. This finding opens a new path of research into the brain mechanisms of pain regulation, with relevance to chronic pain where it may be dysfunctional.

## Introduction

Clinical pain typically varies over time; in most pain states, the brain receives a stream of volatile and noisy noxious signals, which are also auto-correlated in time. The temporal structure of these signals is important, because the human brain has evolved the exceptional ability to extract regularities from streams of auto-correlated sensory signals, a process called statistical learning (Dehaene et al., 2015; Schapiro and Turk-Browne, 2015; Fiser and Lengyel, 2019; Meyniel et al., 2016; Kourtzi and Welchman, 2019; Sherman et al., 2020; Turk-Browne et al., 2009). In the context of pain, statistical learning can allow the brain to predict future pain, which is crucial for orienting behaviour and maximising well-being (Mancini et al., 2022; Mulders et al., 2023). Statistical learning might also be fundamental to the ability of the nervous system to endogenously regulate pain. Indeed, statistical learning generates predictions about forthcoming pain. We already know that pain expectations can modulate pain levels by gating the reciprocal transmission of neural signals between the brain and spinal cord, as shown by previous work on placebo and nocebo effects (Tracey, 2010; Tinnermann et al., 2017; Eippert et al., 2009; Geuter and Büchel, 2013; Fields, 2018).

By using temporal sequences of noxious inputs, we have previously shown that the pain system supports the statistical learning of the basic rate of getting pain by engaging both somatosensory and supramodal cortical regions (Mancini et al., 2022). Specifically, both sensorimotor cortical regions and the ventral striatum encode probabilistic predictions about pain intensity, which are updated as a function of learning by engaging parietal and prefrontal regions. According to a Bayesian inference framework, both the predictive inference and its conﬁdence should, in principle, modulate the neural response to noxious inputs and affect perception, as a function of learning. In support of this conjecture, there is evidence that the confidence of probabilistic pain predictions modulates the cortical response to pain (Mulders et al., 2023). The relationship is inverse: the lower the confidence, the higher is the early cortical response to noxious inputs (and vice versa), as measured by EEG. This is expected based on Bayesian inference theory: when confidence is low, the brain relies less on his prior beliefs and more on sensory evidence to respond to the input. Bayesian inference theory also predicts that prior expectations and their confidence scale perception (Knill and Richards, 1996). Thus, we hypothesise that the predictions generated by learning the statistics of noxious inputs in dynamically evolving sequences of stimuli modulate the perception of forthcoming inputs.

Previously, it was found that pain perception is strongly inﬂuenced by probabilistic expectations as defined by a cue that predicts high or low pain (Jepma et al., 2018). In contrast to such cue paradigm, the primary aim of our experiment was to determine whether the expectations participants hold about the sequence itself inform their perceptual beliefs about the intensity of the stimuli. To that end, we recruited 27 healthy participants to complete a psycho-physical experiment where we delivered four different, 80-trial-long sequences of evolving thermal stimuli, with four levels of temporal regularity. On each trial, a 2 s thermal stimulus was applied, following which participants were asked to either rate their perception of the intensity (Figure 1A) or to predict the intensity of the next stimulus in the sequence (Figure 1B). Participants also reported their response confidence.

![Figure 1.](https://cdn.elifesciences.org/articles/90634/elife-90634-fig1-v1.jpg)

**Figure 1.:** On each trial, each participant received a thermal stimulus lasting 2s from a sequence of intensities. This was followed by a perception (A) or a prediction (B) input screen, where the y-axis indicates the level of perceived/predicted intensity (0–100) centred around participant’s pain threshold, and the x-axis indicates the level of confidence in one’s perception (0–1). The inter-stimulus interval (ISI; black screen) lasted 2.5s (trial example in C). (D) Example intensity sequences are plotted in green, participant’s perception and prediction responses are in red and black, respectively. (E) Participant’s confidence rating for perception (red) and prediction (black) trials.

We contrasted four models of statistical learning, which varied according to the inference strategy used (i.e. optimal Bayesian inference or a heuristic) and the role of expectations on perception. All models used confidence ratings to weigh the inference. We anticipate that probabilistic learning weighted by confidence and expectations modulates pain perception. This provides behavioural evidence for a link between learning and endogenous pain regulation. One reason why this is important is that it might help understand individual differences in the ability to endogenously regulate pain. This is particularly relevant for chronic pain, given that endogenous pain regulation can be dysfunctional in several chronic pain conditions (Bushnell et al., 2013; Bruehl et al., 1999; Yarnitsky, 2015; King et al., 2009; Bannister and Dickenson, 2017), even before chronic pain develops (Tracey, 2016). Although there is ample evidence for changes in the functional anatomy and connectivity of endogenous pain modulatory systems in chronic pain, their computational mechanisms are poorly understood.

## Results

### Model-naive performance

Prior to modelling, we first checked whether participant’s performance in the task was affected by the level of temporal regularity, i.e., the sequence condition. We varied the level of volatility and stochasticity across blocks (i.e. conditions), whilst we fixed their overall level within each block; the level of volatility was defined by the number of trials until the mean intensity level changes. The stochasticity is the additional noise that is added on each trial to the underlying mean, often referred to as the observation noise. The changes were often subtle and participants were not informed when they happened. We set two levels (low/high) of each type of uncertainty, achieving a 2×2 factorial design, with the order of conditions randomised across participants. A set of four example sequences of thermal intensities delivered to one of the participants can be found in Figure 1C, alongside their ratings of perception and predictions. Additionally, example confidence ratings for each type of response are plotted in Figure 1D. Appendix 1—figures 2 and 3 show the plots of each participant’s responses superimposed onto the sequences of noxious inputs.

As a measure of performance, we calculated the root mean square error (RMSE) of participants responses (ratings and predictions) compared to the normative noxious input for each condition as in Figure 2 (see also Materials and methods). The lower the RMSE, the more accurate participants’ responses are. Performance in diﬀerent conditions was analysed with a repeated measures ANOVA, whose results are reported in full in Appendix 1—table 1. Although volatility did not affect rating accuracy ($F(1,26)=0.96,p=0.336,η_{p}^{2}=0.036$), we found a two-way interaction between the level of stochasticity of the sequence (low, high) and the type of rating provided (perceived intensity vs. prediction) ($F(1,26)=29.842,p<0.001,η_{p}^{2}=0.534$). We followed up this interaction in post hoc comparisons, as reported in Appendix 1—table 2. The performance score differences between all the pairs of stochasticity and response type interactions were significant, apart from the perception ratings in the stochastic environment as compared with perception and prediction performance in the low stochastic setting. Intuitively, the RMSE score analysis revealed an overall trend of participants performing worse on the prediction task, in particular when the level of stochasticity is high.

![Figure 2.](https://cdn.elifesciences.org/articles/90634/elife-90634-fig2-v1.jpg)

**Figure 2.:** Violin plots of participant root mean square error (RMSE) for each condition for A: rating and B: prediction responses as compared with the input. Lower and upper hinges correspond to the first and third quartiles of partipants’ errors (the upper/lower whisker extends from the hinge to the largest/smallest value no further than 1.5 * ”Interquartile range” from the hinge); the line in the box corresponds to the median. Each condition has N=27 particpants.

### Modelling strategy

Our models were selected a priori, following the modelling strategy from Jepma et al., 2018, and hence considered the same set of core models for clear extension of the analysis to our non-cue paradigm. The key question for us was whether expectations were used to weigh the behavioural estimates during sequence learning. Therefore, we compared Bayesian and non-Bayesian models of sequential learning that weighted their ratings based on prior expectations versus two corresponding models that assumed perfect perception (i.e. not weighted by prior beliefs). As a baseline, we included a random response model (please see Materials and methods for a formal treatment of the computational models).

According to an optimal Bayesian inference strategy, on each trial, participants update their beliefs about the feature of interest (thermal stimuli) based on probabilistic inference, maintaining a full posterior distribution over its values (Jepma et al., 2018; Särkkä, 2013). Operating within a Bayesian paradigm, participants are assumed to track and, following new information, update both the mean of the sequence of interest and the uncertainty around it (Hoskin et al., 2019). In most cases, such inference makes an assumption about environmental dynamics. For example, a common assumption is that the underlying mean (a hidden/latent state) evolves linearly according to a Gaussian random walk, with the rate of this evolution defined by the the variance of this Gaussian walk (volatility). The observed value is then drawn from another Gaussian with that mean, which has some observation noise (stochasticity). In this case, the observer can infer the latent states through the process of Bayesian filtering (Särkkä, 2013), using the Kalman filter (KF) algorithm (Kalman, 1960; Figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/90634/elife-90634-fig3-v1.jpg)

**Figure 3.:** Computational models used in the main analysis to capture participants’ pain perception ($P^_{t}$) and prediction ($E^_{t+1}$) ratings. Both types of ratings are affected by confidence rating ($C_{t})$) on each trial. (A) In the reinforcement learning model, participant’s pain perception ($P_{t}$) is taken to be weighted sum of the current noxious input ($N_{t}$) and their current pain expectation ($E_{t}$). Following the noxious input, participant updates their pain expectation ($E_{t+1}$). (B) In the Kalman filter model, a generative model of the environment is assumed (yellow background) - where the mean pain level ($x_{t}$) evolves according to a Gaussian random walk (volatility $v^{2}$). The true pain level on each trial ($\pi_{t}$) is then drawn from a Gaussian (stochasticity $s^{2}$). Lastly, the noxious input, $N_{t}$, is assumed an imperfect indicator of the true pain level (subjective noise $ϵ^{2}$). Inference and prediction steps are depicted in a blue box. Participant’s perceived pain is a weighted sum of expectation about the pain level ($m_{t}$) and current noxious input ($N_{t}$). Following each observation, $N_{t}$, participant updates their expectation about the pain level ($m_{t+1}$).

Sequence learning can also be captured by a heuristic to the Bayesian inference, i.e., a simple reinforcement learning (RL) rule. Here, participants maintain and update a point estimate of the expected value of the sequence in an adaptive manner, within a non-stationary environment. RL explicitly involves correcting the tracked mean of the sequence proportionally to a trial-by-trial prediction error - a difference between the expected and actual value of the sequence (Sutton and Barto, 2018; Figure 3A). Importantly, RL agents do not assume any specific dynamics of the environment and hence are considered model-free.

Both models perform a form of error correction about the underlying sequence. The rate at which this occurs is captured by the learning rate $\alpha\in[0,1]$ element. The higher the learning rate, the faster participants update their beliefs about the sequence after each observation. For the RL model, the learning rate α is a free parameter that is constant across the trials. On the other hand, the learning rate in the KF model $\alpha_{t}$ (known as the Kalman gain) is calculated on every trial. It depends on participants’ trial-wise belief uncertainty as well as their overall estimation of the inherent noise in the environment (stochasticity, $s$). The belief uncertainty is updated after each observation and depends on participants’ sense of volatility ($v$) and stochasticity ($s$) in the environment.

Crucially, we also used participants’ trial-by-trial confidence ratings to measure to what extent conﬁdence plays a role in learning. This is captured by the confidence scaling factor $C$, which defines the extent to which confidence aﬀects response (un-)certainty. Intuitively, the higher the confidence scaling factor $C$, the less important role confidence plays in participant’s response. With relatively low values of $C$, when the confidence is low, participants’ responses are more noisy, i.e., less certain. We demonstrate this in Figure 4 by plotting hypothetical responses (A–F) and the effect on the noise scaling (G–L) as a function of $C$ and confidence ratings.

![Figure 4.](https://cdn.elifesciences.org/articles/90634/elife-90634-fig4-v1.jpg)

**Figure 4.:** (A–F) For a range of values of the confidence scaling factor $C$, we simulated a set of typical responses a participant would make for various levels of confidence ratings. The belief about the mean of the sequence is set at 50, while the response noise at 10. The confidence scaling factor $C$ effectively scales the response noise, adding or reducing response uncertainty. (G–L) The effect of different levels of parameter $C$ on noise scaling. As $C$ increases the effect of confidence is diminished.

To evaluate the effect of expectation on perceived intensity (on top of statistical learning modulating perception), we expanded the standard RL and KF models by adding a perceptual weighting element, $\gamma\in[0,1]$ (similarly to Jepma et al., 2018). Essentially, $\gamma$ governs how much each participant relies on the normative input on each trial, and how much their expectation of the input inﬂuences their reported perception - i.e., they take a weighted average of the two. The higher the $\gamma$, the bigger the impact of the expectation on perception. Again, in the case of the RL model (eRL - expectation weighted RL), $\gamma$ is a free parameter that is constant across trials, while in the KF model (eKF - expectation weighted KF), $\gamma_{t}$ is calculated on every trial and depends on: (1) the participants’ trial-wise belief uncertainty, (2) their overall estimation of the inherent noise in the environment (stochasticity, $s$), and (3) the participant’s subjective uncertainty about the level of intensity, $ϵ$.

Thus, in total we tested five models: RL and KF (perception not weighted by expectations), eRL and eKF (perception weighted by expectations), and a baseline random model. We then proceeded to fit these five computational models to participants’ responses. For parameter estimation, we used hierarchical Bayesian methods, where we obtained group- and individual-level estimates for each model parameter (see Materials and methods).

### Modelling results

We fit each model for each condition sequence. Example trial-by-trial model prediction plots from one participant can be found in Appendix 1—figure 4. To establish which of the models fitted the data best, we ran model comparison analysis based on the difference in expected log point-wise predictive density (ELPD) between models. The models are ranked according to the ELPD (with the largest providing the best fit). The ratio between the ELPD difference and the standard error around it provides a significance test proxy through the sigma effect. We considered at least a 2 sigma effect as indication of a significant diﬀerence. In each condition, the expectation weighted models (eKF and eRL) provided better fit than models without this element (KF and RL; approximately 2–4 sigma difference, as reported in Figure 5A–D) and Appendix 1—table 5. This suggests that regardless of the levels of volatility and stochasticity, participants still weigh perception of the stimuli with their expectation. In particular, we found that the expectation weighted KF model offered a better fit than the eRL, although in conditions of high stochasticity this diﬀerence was short of significance against the eRL model. This suggests that in learning about temporal regularities in the sequences of thermal stimuli, participants’ expectations modulate the perception of the stimulus. Moreover, this process was best captured by a model that updates the observer’s belief about the mean and the uncertainty of the sequence in a Bayesian manner.

![Figure 5.](https://cdn.elifesciences.org/articles/90634/elife-90634-fig5-v1.jpg)

**Figure 5.:** The dots indicate the expected log point-wise predictive density (ELPD) difference between the winning model (eKF - expectation weighted Kalman filter) and every other model. The line indicates the standard error (SE) of the difference. The non-winning models’ ELPD differences are annotated with the ratio between the ELPD difference and SE indicating the sigma effect, a significance heuristic.

We also found that as the confidence in the response decreases, the response uncertainty is scaled linearly with a negative slope ranging between 0.112 and 0.276 across conditions (Figure 6), confirming the intuition that less confidence leads to bigger uncertainty.

![Figure 6.](https://cdn.elifesciences.org/articles/90634/elife-90634-fig6-v1.jpg)

**Figure 6.:** (A–D) Each coloured line corresponds to one participant, with the black line indicating the mean across all participants. The mean slope for each condition is annotated.

As an additional check, for each participant, condition and response type (perception and prediction), we plotted participants’ ratings against model predicted ratings and calculated a grand mean correlation in Appendix 1—figure 5.

Next, we checked whether the parameters of the the winning eKF model differed across diﬀerent sequence conditions. Given that volatility was fixed within condition, we treated it as a single-context scenario from the point of view of modelling (Heald et al., 2023), and we did not interpret its effect on the learning rate (Piray and Daw, 2021). There were no differences for the group-level parameters; i.e., we did not detect significant diﬀerences between conditions in a hypothetical healthy participant group as generalised from our population of participants (Appendix 1—figure 12).

However, we found some differences at the individual level of parameters (i.e. within our specific population of recruited participants), which we detected by performing repeated measures ANOVAs (see Appendix 1—figure 13 for visualisation). The stochasticity parameter $s$ was affected by the interaction between the levels of stochasticity and volatility ($F(1,26)=35.108,p<0.001,η_{p}^{2}=0.575$), and was higher in highly stochastic and volatile conditions as compared to conditions where either volatility $(t=7.735,p_{bonf}<0.001)$, stochasticity $(t=9.396,p_{bonf}<0.001)$, or both were low $(t=8.826,p_{bonf}<0.001)$. This suggests that, while participants’ performance was generally worse in highly stochastic environments, participants seem to have attributed this to only one source - stochasticity ($s$), regardless of the source of higher uncertainty in the sequence (stochasticity or volatility).

The response noise $ξ$ was modulated by the level of volatility ($F(1,26)=5.079,p=0.033,η_{p}^{2}=0.163$), where it was smaller in highly volatile conditions. Moreover, we detected a significant interaction between volatility and stochasticity on the confidence scaling factor $C$ ($F(1,26)=81.258,p<0.001,η_{p}^{2}=0.758$), where the values $C$ were overall lower when either volatility $(t=−11.570,p_{bonf}<0.001)$, stochasticity $(t=−6.165,p_{bonf}<0.001)$, or both $(t=−4.575,p_{bonf}<0.001)$ were high as compared to the conditions where both levels of noise were low. This indicates there may have been some trade-off between $ξ$ and $C$, as lower values of $C$ introduce additional uncertainty when participant’s confidence is low.

Lastly, we found the initial uncertainty belief $w_{0}$ was affected by the interaction between volatility and stochasticity ($F(1,26)=5275.367,p<0.001,η_{p}^{2}=0.995$) without a consistent pattern. All the other effects were not significant.

In summary, we formalised the process behind pain perception and prediction in noxious time-series within the framework of sequential learning, where the best description of participants’ statistical learning was captured through Bayesian filtering, in particular using a confidence weighted KF model. Most importantly, we discovered that, in addition to weighing their responses with confidence, participants used their expectations about stimulus intensity levels to form a judgement as to what they perceived. This mechanism was present across various levels of uncertainty that defined the sequences (volatility and stochasticity).

## Discussion

Statistical learning allows the brain to extract regularities from streams of sensory inputs and is central to perception and cognitive function. Despite its fundamental role, it has often been overlooked in the field of pain research. Yet, chronic pain appears to ﬂuctuate over time. For instance Mayr et al., 2022; Baliki et al., 2012; Foss et al., 2006, reported that chronic back pain ratings vary periodically, over several seconds-minutes and in absence of movements. This temporal aspect of pain is important because periodic temporal structures are easy to learn for the brain (Dehaene et al., 2015; Mancini et al., 2022). If the temporal evolution of pain is learned, it can be used by the brain to regulate its responses to forthcoming pain, effectively shaping how much pain it experiences. Indeed, we show that healthy participants extract temporal regularities from sequences of noxious stimuli and use this probabilistic knowledge to form confidence weighted judgements and predictions about the level of pain intensity they experience in the sequence. We formalised our results within a Bayesian inference framework, where the belief about the level of pain intensity is updated on each trial according to the amount of uncertainty participants ascribe to the stimuli and the environment. Importantly, their perception and prediction of pain were inﬂuenced by the expected level of intensity that participants held about the sequence before responding. When varying different levels of inherent uncertainty in the sequences of stimuli (stochasticity and volatility), the expectation and confidence weighted models fitted the data better than models weighted for confidence but not for expectations (Figure 5A–D). The expectation weighted Bayesian (eKF) model offered a better fit than the expectation weighted, model-free RL model, although in conditions of high stochasticity this difference was short of significance. Overall, this suggests that participants’ expectations play a significant role in the perception of sequences of noxious stimuli.

### Statistical inference and learning in pain sequences

The first main contribution of our work is towards the understanding of the phenomenon of statistical learning in the context of pain. Statistical learning is an important function that the brain employs across the lifespan, with relevance to perception, cognition, and learning (Sherman et al., 2020). The large majority of past research on statistical learning focused on visual and auditory perception (Dehaene et al., 2015; Fiser and Lengyel, 2019; Meyniel et al., 2016; Meyniel and Dehaene, 2017), with the nociceptive system receiving relatively little attention (Tabor et al., 2017). Recently, we showed that the human brain can learn to predict a sequence of two pain levels (low and high) in a manner consistent with optimal Bayesian inference, by engaging sensorimotor regions, parietal, premotor regions, and dorsal striatum (Mancini et al., 2022). We also found that the confidence of these probabilistic inferences modulates the cortical response to pain, as expected by hierarchical Bayesian inference theory (Mulders et al., 2023). Here, we tested sequences with a much larger range of stimulus intensities to elucidate the effect of statistical learning and expectations on pain perception. As predicted by hierarchical Bayesian inference theory, we find that the pain intensity judgements are scaled by both expectations and confidence.

Hence, our work highlights the inferential nature of the nociceptive system (Jepma et al., 2018; Tabor et al., 2017; Fardo et al., 2017; Seymour and Mancini, 2020; Büchel et al., 2014), where in addition to the sheer input received by the nociceptors, there is a wealth of a priori knowledge and beliefs the agent holds about themselves and the environment that need to be integrated to form a judgement about pain (Yoshida et al., 2013; Anchisi and Zanon, 2015; Wiech, 2016; Tabor and Burr, 2019). This has an immediate signiﬁcance for the real world, where weights need to be assigned to prior beliefs and/or stimuli to successfully protect the organism from further damage, but only to an extent to which it is beneficial.

Secondly, our results regarding the effect of expectation on pain perception relate to a much larger literature on this topic. The prime example would be placebo analgesia (i.e. the expectation of pain relief decreasing pain perception) and nocebo hyperalgesia (i.e. the expectation of high level of pain increasing its perception; Tracey, 2010; Büchel et al., 2014; Colloca et al., 2008; Blasini et al., 2017). Recent work attempted to capture such expectancy effects within the Bayesian inference framework. For example, Hoskin et al., 2019, showed that in addition to expectation inﬂuencing perceived pain in general, higher level of uncertainty around that expectation attenuated its effect on perception. Similarly, Hird et al., 2019, demonstrated that when the discrepancy between the expectation and outcome (prediction error) is unusually large, the role of expectation is significantly reduced and so the placebo and nocebo effects are not that strong. An unusually large prediction error could be thought of as contributing to increased uncertainty about the stimuli, which mirrors the results from Hoskin et al., 2019 Bayesian framework. Nevertheless, the types of stimuli used in the above studies (i.e. noxious stimuli cued by non-noxious stimuli) differed from the more ecologically valid sequences of pain that are reported by chronic pain patients (Mayr et al., 2022), as we indicated above. Furthermore, Jepma et al., 2018, used a conditioning paradigm and also found that expectations inﬂuence both perception and learning, in a self-reinforcing loop. Our work has followed a similar modelling strategy to Jepma et al., 2018, but it goes beyond simple conditioning schedules or sequences of two-level discrete painful stimuli, showing expectancy effects even when the intensities are allowed to vary across a wider range of values and according to more complex statistical temporal structures. Additionally, given the reported role of confidence in the perception of pain (Mulders et al., 2023; Brown et al., 2008), we draw a more complete picture by including participants’ confidence ratings in our modelling analysis.

Future studies would need to determine whether statistical learning and its effect on pain is altered in chronic pain conditions. This is important because statistical learning could, in principle, inﬂuence how a pain state evolves. Once a pain state is initiated, how an individual learns and anticipates the ﬂuctuating pain signals may contribute to determine how well it can be regulated by the nervous system, thus affecting the severity and recurrence of pain ﬂares. This, in turn, would affect whether aversive associations with the instigating stimulus are extinguished or reinforced (Seymour and Mancini, 2020). In chronic pain, dysfunctional learning may promote the amplification and maintenance of pain signals, contributing to the reinforcement of aversive associations with incident stimuli, as well as the persistence of pain (Seymour, 2019; Baliki and Apkarian, 2015; Vlaeyen et al., 2016).

Our paper comes with open tools, which can be adapted in future studies on statistical learning in chronic pain. The key advantage of taking an hypothesis-driven, computational-neuroscience approach to quantify learning is that it allows to go beyond symptoms-mapping, identifying the quantifiable computational principles that mediate the link between symptoms and neural function.

In summary, we show that statistical expectations and confidence scale the judgement of pain in sequences of noxious stimuli as predicted by hierarchical Bayesian inference theory, opening a new avenue of research on the role of learning in pain.

## Materials and methods

### Participants

Thirty-three (18 female) healthy adult participants were recruited for the experiment. The mean age of participants was 22.4±2.7 years of age (range: 18–35). Participants had no chronic condition and no infectious illnesses, as well as no skin conditions (e.g. eczema) at the site of stimulus delivery. Moreover, we only recruited participants that had not taken any anti-anxiety, anti-depressive medication, nor any illicit substances, alcohol and pain medication (including NSAIDs such as ibuprofen and paracetamol) in the 24 hr prior to the experiment. All participants gave informed written consent to take part in the study, which was approved by the local ethics committee (Department of Engineering, University of Cambridge Ethics Committee).

### Protocol

The experimental room’s temperature was maintained between 20°C and 23°C. Upon entry, an infrared thermometer was used to ensure participants’ temperature was above 36°C at the forehead and forearm of the non-dominant hand, to account for the known effects of temperature on pain perception (Strigo et al., 2000). A series of slideshows were presented, which explained the premise of the experiment and demonstrated what the participant would be asked to carry out. Throughout this presentation, questions were asked to ensure participants understood the task. Participants were given multiple opportunities to ask questions throughout the presentation.

We used the Medoc Advanced Thermosensory Stimulator 2 (TSA2) (Medoc Advanced Medical Systems, 2022) to deliver thermal stimuli using the CHEPS thermode. The CHEPS thermode allowed for rapid cooling (40°C/s) and heating (70°C/s) so transitions between the baseline and stimuli temperatures were minimal. The TSA2 was controlled externally, via Matlab (Mathworks).

We then established the pain threshold, using the method of limits (Lue and Shih, 2017), in order to centre the range of temperature intensities used in the experiment. Each participant was provided with stimuli of increasing temperature, starting from 40°C going up in 0.5°C increments, using an inter-stimulus interval (ISI) of 2.5 s and a 2 s duration. The participant was asked to indicate when the stimuli went from warm to painful - this temperature was noted and the stimuli ended. The procedure was repeated three times, and the average was used as an estimate of the pain threshold.

During the experiment, four sequences of thermal stimuli were delivered. Due to the phenomenon of offset analgesia, where decreases in tonic pain result in a proportionally larger decrease in perceived pain (Hermans et al., 2016), we chose phasic stimuli, with a duration of 2 s and an ISI 2.5 s. In order to account for individual differences, the temperatures which the levels refer to are based upon the participants’ threshold. The median intensity level was defined as threshold, giving a max temperature of 3°C above threshold, which was found to be acceptable by participants. Before the start of the experiment each participant was provided with the highest temperature stimuli that could be presented, given their measured threshold, to ensure they were comfortable with this. Two participants found the stimulus too painful - the temperature range was lowered by 1°C and this was found to be acceptable.

After every trial of each sequence, the participant was asked for either their perception of the previous stimulus or their prediction for the next stimulus through a 2D VAS (Figure 1B), presented using PsychToolBox-3 (Kleiner, 2007). The y-axis encodes the intensity of the stimulus either perceived or predicted, ranging from 0 (no heat detected/predicted) to 100 (worst pain imaginable perceived/predicted); on this scale, 50 represents the pain threshold. This was done as a given sequence was centred around the threshold. The x-axis encodes confidence in either perception or prediction, ranging from 0 - completely uncertain (‘unsure’) - to 1 - complete confidence in the rating (‘sure’). Differing background colours were chosen to ensure participants were aware of what was being asked, and throughout the experiment participants were reminded to take care in answering the right question. The mouse movement was limited to be inside of the coloured box, which defined the area of participants’ input. At the beginning of each input screen, the mouse location was uniformly randomised within the input box.

The sequence of response types was randomised so as to retain 40 prediction and 40 perception ratings for each of the four sequence conditions. For an 80-trial-long sequence, this gave 80 participant responses. Each sequence condition was separated by a 5 min break, during which the thermode’s probe was slightly moved around the area of skin on the forearm to reduce sensitisation (i.e. a gradual increase in perceived intensity with repetitive noxious stimuli) (Hollins et al., 2011). In the middle of each sequence, there was a 3 min break. During the ISI, the temperature returned to a baseline of 38°C. One participant was unable to complete the sequence as their threshold was too low, and data from four participants was lost due to Medoc software issues (the remote control failed and the data of two out of four sessions were not saved). We excluded one participant’s whose ratings/predictions were inversely proportional to the noxious input. Thus, we analysed data from 27 participants.

### Generative process of the painful sequences

We manipulated two sources of uncertainty in the sequence: the stochasticity ($s$) of the observation and the volatility ($v$) of the underlying sequence (Piray and Daw, 2021). Sequences were defined by two levels (high or low) of stochasticity and volatility, resulting in four different sequences conditions - creating a 2×2 factorial design. Each sequence was defined as a series of chunks, where the intensity for trial $t$, $i_{t}$, was sampled from $N(I,\sigma^{2})$, where $\sigma^{2}$ indicates the level of stochasticity ($\sigma^{2}=1.75$ for high level of stochasticity, $\sigma^{2}=0.25$ for low level of stochasticity). The mean of the chunk, $I$, was drawn from $U(3.5,10.5)$. To ensure a noticeable difference in chunk intensity to the participant, concurrent chunk means were constrained to be at least two intensity levels different. Volatility was implemented by defining the length, or number of trials, of a chunk ($l$) drawn from $U(L−a,L+a)$, where $L$ is the mean o the chunk length ($L=15$ for high volatility level, $L=25$ for low volatility level). A jitter, $a$, was added around the mean to ensure the transition from one chunk to the next was not consistent or predictable. For both high and low volatility conditions, we set $a=3$. Sampled values were then discretised, where any intensities outside the valid intensity range $[1,13]$ were discarded and re-sampled resulting in an 80-trial-long sequence for each condition. The mean of each sequence was centred around intensity level 7, i.e., the participants threshold. So defined, six sets of four sequences were sampled. Each participant received one set, with a randomised sequence order. See an example sequence (after subject-specific linear transformation) and one participant’s responses (including confidence ratings) in Figure 1C and D.

### Data pre-processing

Since the intensity values of the noxious input were discretised between 1 and 13, while the participant’s responses (perception and prediction) were given on a 0–100 scale, we applied a linear transformation of the input to map its values onto a common 0–100 range. For each participant, for a set of inputs at perception trials from the concatenated sequence (separate sequence conditions in the order as presented), we fit a linear least squares regression using Python’s scipy.stats.linregress function. On rare occasions, when the transformed input was negative, we refit the line using Python’s non-linear least squares function scipy.optimize.curve_fit, constraining the intercept above 0 (Virtanen et al., 2020). We then extracted each participant’s optimised slope and intercept and applied the transformation to both the concatenated and condition-specific sequence of inputs. So transformed, the sequences were then used in all the analyses. Plots of each participant transformation can be found in Appendix 1—figure 1. We superimposed participant’s responses onto the noxious input condition sequences in Appendix 1—figure 2.

To capture participant’s model-naive performance in the task, both for the concatenated and condition-specific sequence, we calculated RMSE of each participant’s perception (Equation 1) and prediction (Equation 2) responses as compared to the input. The lower the RMSE, the higher the response accuracy.

$$
RMSE_{P}=\sqrt{\frac{\sumt=1T_{P}(Y_{t}−P^_{t})}{T_{P}}}
$$



$$
RMSE_{E}=\sqrt{\frac{\sumt=1T_{E}(y_{t+1}−E^_{t+1})}{T_{E}}}
$$

where $T_{P}$ is the number of perception trials, $P^_{t}$ is participant’s perception response to the stimulus $y_{t}$ at trial $t$, $T_{E}$ is the number of prediction trials, and $E^_{t+1}$ is participant’s prediction of the next stimulus intensity $y_{t+1}$ at trial $t+1$.

### Models

#### Reinforcement learning

##### RL

In RL models, learning is driven by discrepancies between the estimate of the expected value and observed values. Before any learning begins, at trial $t=1$, participants have an initial expectation, $E_{1}=E_{0}$, which is a free parameter that we estimate.

On each trial, participants receive a thermal input $N_{t}$. We then calculate the prediction error $\delta_{t}$, defined as the difference between the expectation $E_{t}$ and the input $N_{t}$ (Equation 3).

$$
\delta_{t}=N_{t}−E_{t}
$$

Participant is then assumed to update their expectation of the stimulus on the next trial as in Equation 4:

$$
E_{t+1}=E_{t}+\alpha\delta_{t}
$$

where $\alpha$ is the learning rate (free parameter), which governs how fast participants assimilate new information to update their belief.

On trials when participants rate their perceived intensity, we assume no effects on their perception other than conﬁdence rating $c_{t}$ and response noise, so participants’ perception response $P^_{t}$ is drawn from a Gaussian distribution, with the mean $P_{t}=N_{t}$ and a confidence-scaled response noise $ξ$ (free parameter), as in Equation 5:

$$
P^_{t}∼N(P_{t},ξ^{2}exp{C^{−1}(1−c_{t})}^{2})
$$

where $C$ is the confidence scaling factor (free parameter), which deﬁnes the extent to which conﬁdence affects response uncertainty. Please see Figure 4 for an intuition behind confidence scaling.

On trials when participants are asked to predict the intensity of the next thermal stimulus, we use the updated expectation $E_{t+1}$ to model participants’ prediction response $E^_{t+1}$. This is similarly affected by confidence rating and response noise and is deﬁned as in Equation 6.

$$
E^_{t+1}∼N(E_{t+1},ξ^{2}exp{C^{−1}(1−c_{t})}^{2})
$$

To recap, the RL model has four free parameters: the learning rate $\alpha$, response noise $ξ$, the initial expectation $E_{0}$, and the confidence scaling factor $C$.

##### eRL

Additionally, where we investigate the effects of expectation on the perception of pain (Jepma et al., 2018), we included an element that allows us to express the perception as a weighted sum of the input and expectation (Equation 7):

$$
P_{t}=(1−\gamma)N_{t}+\gammaE_{t}
$$

where $\gamma\in[0,1]$ (free parameter) captures how much participants rely on the normative thermal input vs. their expectation. When $\gamma=0$, the expectation plays no role and the model simplifies to that of the standard RL above. In total, the eRL model has five free parameters, with the other equations the same as in the RL model, with the exception of the prediction error, which now relies on the expectation weighted pain perception $P_{t}$ (Equation 8).

$$
\delta_{t}=P_{t}−E_{t}
$$

### Kalman filter

#### KF

To capture sequential learning in a Bayesian manner, we used the KF model (Jepma et al., 2018; Särkkä, 2013; Kalman, 1960). KF assumes a generative model of the environment where the latent state on trial t, $x_{t}$ (the mean of the sequences in the experiment), evolves according to a Gaussian random walk with a fixed drift rate, $v$ (volatility), as in Equation 9.

$$
x_{t}∼N(x_{t−1},v^{2})
$$

The observation on trial t, $N_{t}$, is then drawn from a Gaussian (Equation 10) with a fixed variance, which represents the observation uncertainty $s$ (stochasticity).

$$
N_{t}∼N(x_{t},s^{2})
$$

As such the KF assumes stable dynamics since the generative process has fixed volatility and stochasticity.

For ease of explanation, we refer to the thermal input at each trial as $N_{t}$, we also use the $N_{1:t}$ notation, which refers to a sequence of observations up to and including trial $t$. The model allows to obtain posterior beliefs about the latent state $x_{t}$ given the observations. This is done by tracking an internal estimate of the mean $m_{t}$ and the uncertainty, $w_{t}$, of the latent state $x_{t}$.

First, following standard KF results, on each trial, the participant is assumed to hold a prior belief (indicated with (–) superscript) about the latent state, $x_{t}$ (Equation 11).

$$
x_{t}|N_{1:t−1}∼N(m_{t}^{(−)},w_{t}^{2(−)})
$$

On the first trial, before any observations, we set $m_{1}^{(−)}=E^{0},w_{1}^{(−)}=w_{0}$ (free parameters). In light of the new observation, $N_{t}$ on trial $t$, the tracked mean and uncertainty of the latent state are reweighed based on the new evidence $N_{t}$ and its associated observation uncertainty $s$ as in Equation 12.

$$
x_{t}|N_{1:t}∼N(\frac{s^{2}m_{t}^{(−)}+w_{t}^{2(−)}N_{t}}{s^{2}+w_{t}^{2(−)}},\frac{s^{2}w_{t}^{2(−)}}{s^{2}+w_{t}^{2(−)}})
$$

We can then define the learning rate $\alpha_{t}$ (Equation 13),

$$
\alpha_{t}=\frac{w_{t}^{2(−)}}{s^{2}+w_{t}^{2(−)}}
$$

to get the update rule for the new posterior beliefs (indicated with (+) superscript) about the mean (Equation 14) and uncertainty (Equation 15) of $x_{t}$.

$$
m_{t}^{(+)}=m_{t}^{(−)}(1−\alpha_{t})+N_{t}\alpha_{t}
$$



$$
w_{t}^{2(+)}=w_{t}^{2(−)}(1−\alpha_{t})
$$

Following this new belief, and the assumption about the environmental dynamics (volatility), the participant forms a new prior belief about the latent state $x_{t+1}$ for the next trial $t+1$ as in Equation 16.

$$
x_{t+1}|N_{1:t}∼N(m_{t+1}^{(−)},w_{t+1}^{2(−)})
$$

where

$$
m_{t+1}^{(−)}=m_{t}^{(+)}
$$



$$
w_{t+1}^{2(−)}=w_{t}^{2(+)}+v^{2}
$$

We can simplify the notation to make it comparable to the RL models. We let $m_{t+1}=m_{t}^{(+)}=m_{t+1}^{(−)}$, and $w_{t+1}^{2}=w_{t+1}^{2(−)}=w_{t}^{2(+)}+v^{2}$. Following a new observation at trial $t$, we calculate the prediction error (Equation 19) and learning rate (Equation 20).

$$
\delta_{t}=y_{t}−m_{t}
$$



$$
\alpha_{t}=\frac{w_{t}^{2}}{w_{t}^{2}+s^{2}}
$$

We then update the belief about the mean (Equation 21) and uncertainty (Equation 22) of the latent state for the next trial.

$$
m_{t+1}=m_{t}(1−\alpha_{t})+N_{t}\alpha_{t}=m_{t}+\alpha_{t}(N_{t}−m_{t})
$$



$$
w_{t+1}^{2}=w_{t}^{2}(1−\alpha_{t})+v^{2}
$$

Now, mapping this onto the experiment, the mean of the latent state is participants’ expectation $E_{t}=m_{t}$, and so we have participant perception rating modelled as in Equation 23.

$$
P^_{t}∼N(P_{t},ξ^{2}exp{C^{−1}(1−c_{t})}^{2})
$$

and the prediction rating for the next trial as in Equation 24.

$$
E^_{t+1}∼N(E_{t+1},ξ^{2}exp{C^{−1}(1−c_{t})}^{2})
$$

In total the model has six free parameters: $s$ (environmental stochasticity), $v$ (environmental volatility), $ξ$ (response noise), $E_{0}$ (initial belief about the mean), $w_{0}$ (initial belief about the uncertainty), and $C$ (confidence scaling factor).

#### eKF

We can introduce the effect of expectation on the pain perception, by assuming that participants treat the thermal input as an imperfect indicator of the true level of pain (Jepma et al., 2018). In this case, the input, $N_{t}$, is modelled as in Equation 25:

$$
N_{t}∼N(\pi_{t},ϵ^{2})
$$

which forms an expression for the likelihood of the observation and adds an additional level to the inference, slightly modifying the KF assumptions such that:

$$
\pi_{t}∼N(x_{t},s^{2})
$$

However, we can apply the standard KF results and Bayes’ rule to arrive at simple update rules for the participants’ belief about the mean and uncertainty of the latent state $x_{t}$t. From this, we get a prior on the $\pi_{t}$ defined in Equation 27:

$$
\pi_{t}|N_{1:t−1}∼N(m_{t}^{(−)},w_{t}^{2(−)}+s^{2})
$$

which, following a new input $N_{t}$, gives us the posterior belief about $\pi_{t}$ as in Equation 28.

$$
\pi_{t}|N_{1:t}∼N(\frac{ϵ^{2}m_{t}^{(−)}+(s^{2}+w_{t}^{2(−)})N_{t}}{ϵ^{2}+s^{2}+w_{t}^{2(−)}},\frac{ϵ^{2}(s^{2}+w_{t}^{2(−)})}{ϵ^{2}+s^{2}+w_{t}^{2(−)}})
$$

Now, if we define $\gamma_{t}$ as in Equation 29:

$$
\gamma_{t}=\frac{ϵ^{2}}{ϵ^{2}+s^{2}+w_{t}^{2(−)}}
$$

We have that the posterior belief about the mean level of pain $\pi_{t}$ is calculated as:

$$
P_{t}^{(+)}=\gamma_{t}m_{t}^{(−)}+(1−\gamma_{t})N_{t}
$$

which is a weighted sum of the input $N_{t}$ and participant expectation about the latent state $x_{t}$, governed by the perceptual weight $\gamma_{t}$, analogously to the eRL model. Finally, the posterior belief about $x_{t}$ is obtained in Equation 31.

$$
x_{t}|N_{1:t}∼N(\frac{(ϵ^{2}+s^{2})m_{t}^{(−)}+w_{t}^{2(−)}N_{t}}{ϵ^{2}+s^{2}+w_{t}^{2(−)}},\frac{(ϵ^{2}+s^{2})w_{t}^{2(−)}}{ϵ^{2}+s^{2}+w_{t}^{2(−)}})
$$

Now, setting the learning rate as in Equation 32:

$$
\alpha_{t}=\frac{w_{t}^{2}}{ϵ^{2}+w_{t}^{2}+s^{2}}
$$

we get:

$$
m_{t}^{(+)}=m_{t}^{(−)}(1−\alpha_{t})+N_{t}\alpha_{t}
$$



$$
w_{t}^{2(+)}=w_{t}^{2(−)}(1−\alpha_{t})
$$

Next, following the same notation simplification as before, we get the update rules for the prior belief about the mean (Equation 35) and uncertainty (Equation 36) of the latent state $x_{t+1}$ for the next trial.

$$
m_{t+1}=m_{t}(1−\alpha_{t})+N_{t}\alpha_{t}=m_{t}+\alpha_{t}(N_{t}−m_{t})
$$



$$
w_{t+1}^{2}=w_{t}^{2}(1−\alpha_{t})+v^{2}
$$

as well as the expression for subjective perception, $P_{t}$, at trial $t$ (Equation 37).

$$
P_{t}=\gamma_{t}m_{t}+(1−\gamma_{t})N_{t}
$$

The perception and prediction responses are modelled analogously as the KF model. In total, the model has seven free parameters: $ϵ$ (subjective noise), $s$ (environmental stochasticity), $v$ (environmental volatility), $ξ$ (response noise), $E_{0}$ (initial belief about the mean), $w_{0}$ (initial belief about the uncertainty), and C (confidence scaling factor).

### Random model

As a baseline, we also included a model that performs a random guess. The perceptual/prediction ratings were modelled as in Equation 38.

$$
P^_{t}∼N(R,ξ^{2}exp{C^{−1}(1−c_{t})}^{2})
$$

The model has three free parameters: $R$, $ξ$, and $C$, where $R$ is a constant value that participants respond with.

### Model fitting

Model parameters were estimated using hierarchical Bayesian methods, performed with RStan package (v. 2.21.0) (Stan Development Team, 2019) in R (v. 4.0.2) based on Markov Chain Monte Carlo techniques (No-U-Turn Hamiltonian Monte Carlo). For the individual-level parameters we used non-centred parametrisation (Papaspiliopoulos et al., 2007). For the group-level parameters we used $N(0,1)$ priors for the mean, and the gamma-mixture representation of the Student’s-t(3,0,1) for the scale (Stan Development, 2022). Parameters in the (0, 1) range were constrained using Phi_approx - a logistic approximation to the cumulative Normal distribution (Bowling et al., 2009).

For each condition and each of the four chains, we ran 6000 samples (after discarding 6000 warm-up ones). For each condition, we examined R-hat values for each individual- (including the $N(0,1)$ error term from the non-centred parametrisation) and group-level parameters from each model to verify whether the Markov chains have converged. At the group-level and individual-level, all R-hat values had a value <1.1, indicating convergence. In the random response model, 0.01–0.16% iterations saturated the maximum tree depth of 11.

#### Model comparison

For model comparison, we used R package loo, which provides eﬃcient approximate leave-one-out (LOO) cross-validation. The package allows to estimate the difference in models’ expected predictive accuracy through the difference in ELPD (Vehtari et al., 2017). By looking at the ratio between the ELPD difference and the SE of the difference, we get the sigma effect - a heuristic for significance of such model differences. There’s no agreed-upon threshold of SEs that determines significance, but the higher the sigma difference, the more robust is the eﬀect. The closeness of fit can also be captured with LOO information criterion (LOOIC), where the lower LOOIC values indicate better fit.

#### Parameter comparison

For the comparison of group-level parameters between conditions, we extracted 95% high-density intervals of the permuted and merged (across chains) posterior samples of each group-level parameter (Kruschke, 2023). To assess significant differences between conditions, we calculated a difference between such defined intervals. In the Bayesian scenario, a significant difference is indicated by the interval not containing the value 0 (Aylward et al., 2019; Ahn et al., 2017).

#### Parameter and model recovery

To asses the reliability of our modelling analysis (Wilson and Collins, 2019), for each model we performed parameter recovery analysis, where we simulated participants’ responses using newly drawn individual-level parameters from the group-level distributions.

We repurposed existing sequences of noxious inputs in the [1, 13] range (pre-transformation). When then applied a linear transformation to the input sequences using sampled slope and intercept coeﬃcients from a Gaussian distribution of these coeﬃcients that we estimated based on our dataset using R’s fitdistrplus package. Furthermore, we simulated the confidence ratings based on lag-1 auto-correlation across a moving window of the transformed input sequence.

We then fit the same model to the simulated data and calculated Pearson correlation coeﬃcients $r$ between the generated and estimated individual-level parameters. The higher the coeﬃcient $r$, the more reliable the estimates are, which can be categorised as: poor (if r<0.5); fair (if 0.5<r<0.75); good (0.75<r<0.9); excellent (if r>0.9) (White et al., 2018). Results are reported in Appendix 1—table 3 and Appendix 1—figures 6–11.

We also performed model recovery analysis (Wilson and Collins, 2019), where we first simulated responses using each model and then fit each model-specific dataset with each model. We then counted the number of times a model fit the simulated data best (according to the LOOIC rule), effectively creating an M×M confusion matrix, where M is the number of models. In the case where we have a diagonal matrix of ones, the models are perfectly recoverable and hence as reliable as possible. Results are reported in Appendix 1—table 4.

In Appendix 1—Tables 6–9 we report bulk and tail effective sample size (ESS) for each condition, for each model and parameter.
