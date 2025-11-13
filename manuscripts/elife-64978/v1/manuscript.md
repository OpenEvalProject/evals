# Strategically managing learning during perceptual decision making

## Authors

- Javier Masís<sup>1</sup> ([ORCID: 0000-0002-9643-8677](https://orcid.org/0000-0002-9643-8677)) †
- Travis Chapman<sup>2</sup>
- Juliana Y Rhee<sup>1</sup>
- David D Cox<sup>1</sup>
- Andrew M Saxe<sup>3</sup> ([ORCID: 0000-0002-9831-8812](https://orcid.org/0000-0002-9831-8812)) †

### Affiliations

1. Department of Molecular and Cellular Biology, Harvard University Cambridge United States ([ROR:03vek6s52](https://ror.org/03vek6s52))
2. Center for Brain Science, Harvard University Cambridge United States ([ROR:03vek6s52](https://ror.org/03vek6s52))
3. Department of Experimental Psychology, University of Oxford Oxford United Kingdom ([ROR:052gg0110](https://ror.org/052gg0110))

† Corresponding author

## Abstract

Making optimal decisions in the face of noise requires balancing short-term speed and accuracy. But a theory of optimality should account for the fact that short-term speed can influence long-term accuracy through learning. Here, we demonstrate that long-term learning is an important dynamical dimension of the speed-accuracy trade-off. We study learning trajectories in rats and formally characterize these dynamics in a theory expressed as both a recurrent neural network and an analytical extension of the drift-diffusion model that learns over time. The model reveals that choosing suboptimal response times to learn faster sacrifices immediate reward, but can lead to greater total reward. We empirically verify predictions of the theory, including a relationship between stimulus exposure and learning speed, and a modulation of reaction time by future learning prospects. We find that rats’ strategies approximately maximize total reward over the full learning epoch, suggesting cognitive control over the learning process.

## Introduction

Optimal behavior in decision making is frequently defined as maximization of reward over time (Gold and Shadlen, 2002), and this requires balancing the speed and accuracy of one’s choices (Bogacz et al., 2006). For example, imagine you are given a multiple-choice quiz on an esoteric topic with which you are familiar, such as behavioral neuroscience or cognitive psychology, and rewarded for every correct answer. In balancing speed and accuracy, you should spend some time on each question to ensure you get it right. Now imagine that you are given a different quiz on an esoteric topic with which you are not familiar, such as low Reynolds number hydrodynamics or underwater basket weaving. In balancing speed and accuracy, you should now guess on as many questions as you can as quickly as you can in order to maximize reward. The ideal balance of speed and accuracy differs considerably in the cases of high and low competence. However, there is an important additional dynamical aspect to consider: competence can change as a function of experience through learning. For instance, taking the hydrodynamics quiz enough times, you might start to get the hang of it, by going slow enough that you can remember questions and their associated answers, rather than guessing as quickly as you can. Given these almost opposing normative strategies for high and low competence, how does one effectively move from low competence to high competence? In other words, how does an agent strategically manage decision making in light of learning?

In this study, we formalize this problem in the context of a two-choice perceptual decision making task in rodents and simulated agents. Perceptual decisions, in particular two-choice decisions, allow us to leverage one of the most prolific decision making models, the drift-diffusion model (DDM) (Ratcliff, 1978) (and the considerable analytical dissections of it Bogacz et al., 2006), and one of the most prolific paradigms captured by it, the speed-accuracy trade-off (SAT), as a measurement of optimal behavior (i.e. maximization of reward per unit time) (Woodworth, 1899, Henmon, 1911, Garrett, 1922, Pew, 1969, Pachella, 1974, Wickelgren, 1977, Ruthruff, 1996, Ratcliff and Rouder, 1998, Gold and Shadlen, 2002, Bogacz et al., 2006; Bogacz et al., 2010; Heitz and Schall, 2012; Heitz, 2014, Rahnev and Denison, 2018).

Studies of the SAT have focused on how the brain may solve it (Gold and Shadlen, 2002, Roitman and Shadlen, 2002), what the optimal solution is (Bogacz et al., 2006), and whether agents can indeed manage it (Simen et al., 2006, Balci et al., 2011a; Simen et al., 2009; Bogacz et al., 2010, Drugowitsch et al., 2014, Drugowitsch et al., 2015; Manohar et al., 2015). Though most work in this area has taken place in humans and non-human primates, several studies have established the presence of a SAT in rodents (Uchida and Mainen, 2003, Abraham et al., 2004; Rinberg et al., 2006; Reinagel, 2013a; Reinagel, 2013b; Kurylo et al., 2020). The broad conclusion of much of this literature is that after extensive training, many subjects come close to optimal performance (Simen et al., 2009Bogacz et al., 2010; Balci et al., 2011b; Zacksenhouse et al., 2010, Balci et al., 2011b, Starns and Ratcliff, 2010, Holmes and Cohen, 2014, Drugowitsch et al., 2014, Drugowitsch et al., 2015). When faced with deviations from optimality, several hypotheses have been proposed, including error avoidance, poor internal estimates of time, and a minimization of the cognitive cost associated with an optimal strategy (Maddox and Bohil, 1998, Bogacz et al., 2006, Zacksenhouse et al., 2010).

Past studies have shown how agents behave after reaching steady-state performance (Simen et al., 2009, Starns and Ratcliff, 2010, Bogacz et al., 2010Zacksenhouse et al., 2010, Balci et al., 2011b, Balci et al., 2011a; Starns and Ratcliff, 2010, Drugowitsch et al., 2014, Drugowitsch et al., 2015), but relatively less attention has been paid to how agents learn to approach near-optimal behavior (but see Law and Gold, 2009, Balci et al., 2011b, Drugowitsch et al., 2019). While maximizing instantaneous reward rate is a sensible goal when the task is fully mastered, it is less clear that this objective is appropriate during learning.

Here, we set out to understand how agents manage the SAT during learning by studying the learning trajectory of rats and simulated agents in a free-response two-alternative forced-choice visual object recognition task (Zoccolan et al., 2009). Rats near-optimally maximized instantaneous reward rate ($i⁢R⁢R$) at the end of learning but chose response times that were too slow to be $i⁢R⁢R$-optimal early in learning. To understand the rats’ learning trajectory, we examined learning trajectories in a recurrent neural network (RNN) trained on the same task. We derive a reduction of this RNN to a learning drift-diffusion model (LDDM) with time-varying parameters that describes the network’s average learning dynamics. Mathematical analysis of this model reveals a dilemma: at the beginning of learning when error rates are high, $i⁢R⁢R$ is maximized by fast responses (Bogacz et al., 2006). However, fast responses mean minimal stimulus exposure, little opportunity for perceptual processing, and consequently slow learning. Because of this learning speed/$i⁢R⁢R$ (LS/$i⁢R⁢R$) trade-off, slow responses early in learning can yield greater total reward over engagement with the task, suggesting a normative basis for the rats’ behavior. We then experimentally tested and confirmed several model predictions by evaluating whether response time and learning speed are causally related, and whether rats choose their response times so as to take advantage of learning opportunities. Our results suggest that rats exhibit cognitive control of the learning process, adapting their behavior to approximately accrue maximal total reward across the entire learning trajectory, and indicate that a policy that prioritizes learning in perceptual tasks may be advantageous from a total reward perspective.

## Results

### Trained rats solve the SAT

We trained $n=26$ rats on a visual object recognition two-alternative forced-choice task (see Methods) (Zoccolan et al., 2009). The rats began a trial by licking the central of three capacitive lick ports, at which time a static visual object that varied in size and rotation from one of two categories appeared on a screen. After evaluating the stimulus, the rats licked the right or left lick port. When correct, they received a water reward, and when incorrect, a timeout period (Figure 1a, Figure 1—figure supplement 1). Because this was a free-response task, rats were also able to initiate a trial and not make a response, but these ignored trials made up a small fraction of all trials and were not considered during our analysis (Figure 1—figure supplement 2).

![Figure 1.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig1-v1.jpg)

**Figure 1.:** (a) Rat initiates trial by licking center port, one of two visual stimuli appears on the screen, rat chooses correct left/right response port for that stimulus and receives a water reward. (b) Speed-accuracy space: a decision making agent’s $E⁢R$ and mean normalized $D⁢T$ (a normalization of $D⁢T$ based on the average timing between one trial and the next, see Methods). Assuming a simple drift-diffusion process, agents that maximize $i⁢R⁢R$ (see Methods) must lie on an optimal performance curve (OPC, black trace) (Bogacz et al., 2006). Points on the OPC relate error rate to mean normalized decision time, where the normalization takes account of task timing parameters (e.g. average response-to-stimulus interval). For a given SNR, an agent’s performance must lie on a performance frontier swept out by the set of possible threshold-to-drift ratios and their corresponding error rates and mean normalized decision times. The intersection point between the performance frontier and the OPC is the error rate and mean normalized decision time combination that maximizes $i⁢R⁢R$ for that SNR. Any other point along the performance frontier, whether above or below the OPC, will achieve a suboptimal. $i⁢R⁢R$ Overall, $i⁢R⁢R$ increases toward the bottom left with maximal instantaneous reward rate at error rate = 0.0 and mean normalized decision time = 0.0. (c) Mean performance across 10 sessions for trained rats ($n=26$) at asymptotic performance plotted in speed-accuracy space. Each cross is a different rat. Color indicates fraction of maximum instantaneous reward rate ($i⁢R⁢R$) as determined by each rat’s performance frontier. Errors are bootstrapped SEMs. (d) Violin plots depicting fraction of maximum, $i⁢R⁢R$ a quantification of distance to the OPC, for same rats and same sessions as c. Fraction of maximum $i⁢R⁢R$ is a comparison of an agent’s current $i⁢R⁢R$ with its optimal $i⁢R⁢R$ given its inferred SNR. Approximately 15 of 26 (∼60%) of rats attain greater than 99% fraction maximum $iRRs$ for their individual inferred SNRs. * denotes p < 0.05 one-tailed Wilcoxon signed-rank test for mean >0.99.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Error trial: rat chooses incorrect left/right response port and incurs a timeout period.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (a) Schematic of an ignore trial: rat does not choose a left/right response port and receives no feedback. (b) Fraction of trials ignored (ignored trials/(correct + incorrect + ignored trials)) during learning for animals encountering the task for the first time (stimulus pair 1). (c) Fraction of trials ignored for animals learning stimulus pair 2 after training on stimulus pair 1.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (a) The accuracy and reaction time data from 26 trained rats was fit to a simple drift-diffusion model using the hierarchical Bayesian estimation of the drift-diffusion model (HDDM) package (Wiecki et al., 2013). (b) Estimated posterior distributions of parameter values across all animals.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** Estimating $T_{0}$.(a) Linear and quadratic extrapolations to accuracy as a function of reaction time. The T0 estimate is when each extrapolation intersects chance accuracy (0.5). (b) Mean accuracy for trials with reaction times 350–375 ms for $n=26$ rats. (c) Minimum motor time estimated by looking at first peak of time between licks to/from center port for $n=11$ rats. (d) Cartoon of stimulus onset latency across visual areas from Vermaercke et al., 2014 to estimate minimum visual processing time. (e) Diagram of T0 estimates, with an upper limit (minimum reaction time) and lower limit (minimum motor time + minimum visual processing time). (f) Mean learning trajectory for $n=26$ rats with various t0 estimates. (g) Subjects ($n=26$) in speed-accuracy space with various T0 estimates.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig1-figsupp5-v1.jpg)

**Figure 1—figure supplement 5.:** (a) Histogram of voluntary ITIs (time in addition to mandatory experimentally determined $D_{e⁢r⁢r}$ and $D_{c⁢o⁢r⁢r}$) for $n=26$ rats across 10 sessions for previous correct (blue) and previous error (red) ITIs. Voluntary ITIs are spaced every 500 ms because of violations to the ‘cannot lick’ period. Inset: proportion of voluntary ITIs below 500, 1000, and 2000 ms boundaries. (b) Median voluntary ITIs up too 500, 1000, and 2000 ms boundaries. (c) Overlay of voluntary ITIs spaced 500 ms apart after previous correct trials. (d) Overlay of voluntary ITIs spaced 500 ms apart after previous error trials.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig1-figsupp6-v1.jpg)

**Figure 1—figure supplement 6.:** Mandatory post-error ($D~_{e⁢r⁢r}$) and post-correct ($D~_{c⁢o⁢r⁢r}$) response-to-stimulus interval times.(a) Diagram of intertrial interval (ITI) after previous error trial. All times (punishment stimulus, enforced intertrial interval, cannot lick reward ports, and pre-stimulus time) were verified based on timestamps on experimental file logs. After the punishment stimulus and enforced intertrial interval, there is a 300 ms period where rats cannot lick the reward ports. If violated, 500 ms are added to the intertrial interval followed by another 300 ms ‘cannot lick’ period. In addition to this restriction, rats may take as much voluntary time between trials as they wish. Any violation of the ‘cannot lick’ period is counted as voluntary time, and only the minimum mandatory time of 3136 ms is counted for $D~_{e⁢r⁢r}$. (b) Diagram of ITI after previous correct trial. All times (dispense water reward, collect water reward, enforced intertrial interval, cannot lick reward ports, pre-stimulus time) were verified based on timestamps on experimental file logs. The same ‘cannot lick’ period is present as in a. All times (dispense water reward, collect water reward, enforced intertrial interval, cannot lick reward ports, pre-stimulus time) were verified based on timestamps on experimental file logs. Any violation of the ‘cannot lick’ period is counted as voluntary time, and only the minimum mandatory time of 6370 ms is counted for $D~_{c⁢o⁢r⁢r}$.

![Figure 1—figure supplement 7.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig1-figsupp7-v1.jpg)

**Figure 1—figure supplement 7.:** Reward rate sensitivity to $T_{0}$ and voluntary intertrial interval (ITI).(a) Fraction of maximum instantaneous reward rate across $n=26$ rats over 10 sessions at asymptotic performance over possible voluntary ITI values of 0–1000 ms and over the minimum and maximum estimated T0 values. (b) Fraction of maximum instantaneous reward rate across $n=26$ rats over 10 sessions at asymptotic performance over possible T0 values from 160 to 350 ms (min to max estimated T0 values) and over the median voluntary ITIs with 500, 1000, and 2000 ms boundaries. (c) Fraction of maximum instantaneous reward rate across $n=26$ rats as a function of normalized training time during learning period and possible voluntary ITIs from 0 to 2000 ms calculated with the T0 minimum of 160 ms. The gray curves represent a weighted average over previous correct/error median voluntary ITIs over normalized training time. Contours with different fractions of maximum instantaneous reward rate in pink. (d) Same as in c but calculated with T0 maximum of 350 ms.

We examined the relationship between error rate ($ER$) and reaction time ($R⁢T$) during asymptotic performance using the DDM (Figure 1—figure supplement 3). In the DDM, perceptual information is integrated through time until the level of evidence for one alternative reaches a threshold. The SAT is controlled by the subject’s choice of threshold, and is solved when a subject’s performance lies on an optimal performance curve (OPC; Figure 1b; Bogacz et al., 2006). The OPC defines the mean normalized decision time ($DT$) and $E⁢R$ combination for which an agent will collect maximal $i⁢R⁢R$ (see Methods). At any given time, an agent will have some perceptual sensitivity (signal-to-noise ratio [SNR]) which reflects how much information about the stimulus arrives per unit time. Given this SNR, an agent’s position in speed-accuracy space (the space relating $E⁢R$ and $D⁢T$) is constrained to lie on a performance frontier traced out by different thresholds (Figure 1b). Using a low threshold yields fast but error-prone responses, while using a high threshold yields slow but accurate responses. An agent only maximizes $i⁢R⁢R$ when it chooses the $E⁢R$ and $D⁢T$ combination on its performance frontier that intersects the OPC. After learning the task to criterion, over half the subjects collected over 99% of their total possible reward, based on inferred SNRs assuming a DDM (Figure 1c and d).

Calculating mean normalized $D⁢T$ for comparison with the OPC requires knowing two quantities, $D⁢T$ and the average non-decision time per error trial $D_{e⁢r⁢r}$. The average non-decision time $D_{e⁢r⁢r}=T_{0}+D~_{e⁢r⁢r}$ contains the motor and initial perceptual processing components of $R⁢T$, denoted T0; and the post-response timeout on error trials $D~_{e⁢r⁢r}$. Mean normalized $D⁢T$ is then the ratio $D⁢T/D_{e⁢r⁢r}$. In order to determine each subject’s $D⁢T$, we estimated T0 through a variety of methods, opting for a biological estimate (measured lickport latency response times and published visual processing latencies; Figure 1—figure supplement 4). To ensure that our results did not depend on our choice of T0, we ran a sensitivity analysis on a wide range of possible values of T0 (Figure 1—figure supplement 4f). We then had to determine $D~_{e⁢r⁢r}$, which can contain mandatory and voluntary intertrial intervals. We found that the rats generally kept voluntary intertrial intervals to a minimum, and we interpreted longer intervals as effectively ‘exiting’ the DDM framework (Figure 1—figure supplement 5). As such, we defined $D~_{err}$ to only contain mandatory intertrial intervals (see Methods, Figure 1—figure supplement 6). To ensure that our results did not depend on either choice, we ran a sensitivity analysis on the combined effects of T0 and a $D~_{err}$ containing voluntary intertrial intervals on RR (Figure 1—figure supplement 7). A full discussion of how these parameters were determined is included in the Methods.

Across a population, a uniform stimulus difficulty will reveal different SNRs because the internal perceptual processing ability in every subject will be different. Thus, although we did not explicitly vary stimulus difficulty (Simen et al., 2009, Bogacz et al., 2010; Zacksenhouse et al., 2010Balci et al., 2011b), as a population, animals clustered along the OPC across a range of $ERs$ (Figure 1d), supporting the assertion that well-trained rats achieve a near maximal $i⁢R⁢R$ in this perceptual task. We note that subjects did not span the entire range of possible $ERs$, and that the differences in optimal $DTs$ dictated by the OPC for the $ERs$ we did observe are not large. It remains unclear whether our subjects would be optimal over a wider range of task parameters. Notwithstanding, previous work with a similar task found that rats did increase $DTs$ in response to increased penalty times, indicating a sensitivity to these parameters (Reinagel, 2013a). Thus, for our perceptual task and its parameters, trained rats approximately solve the SAT.

### Rats do not maximize instantaneous reward rate during learning

Knowing that rats harvested reward near-optimally after learning, we next asked whether rats harvested instantaneous reward near-optimally during learning as well. If rats optimized $i⁢R⁢R$ throughout learning, their trajectories in speed-accuracy space should always track the OPC.

During learning, a representative individual ($n=1$) started with long $RTs$ that decreased as accuracy increased across training time (Figure 2a). Transforming this trajectory to speed-accuracy space revealed that throughout learning the individual did not follow the OPC (Figure 2b). Early in learning, the individual started with a much higher $D⁢T$ than optimal, but as learning progressed it approached the OPC. The maximum $i⁢R⁢R$ opportunity cost is the fraction of maximum possible $i⁢R⁢R$ relinquished for a choice of threshold (and average $D⁢T$) (see Methods). We found that this individual gave up over 20% of possible $i⁢R⁢R$ at the beginning of learning but harvested reward near-optimally at asymptotic performance (Figure 2c). These trends held when the learning trajectories of $n=26$ individuals were averaged (Figure 2d–f). To ensure that our particular training regime (which involved changes in stimulus size and rotation) was not responsible for these trends, we trained a separate cohort ($n=8$) with a simplified regime that did not involve any changes to the stimuli and we did not observe any meaningful differences (Figure 2—figure supplement 1, see Methods). These results show that rats do not greedily maximize $i⁢R⁢R$ throughout learning and lead to the question: if rats maximize $i⁢R⁢R$ at the end of learning, what principle governs their strategy at the beginning of learning?

![Figure 2.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig2-v1.jpg)

**Figure 2.:** (a) Reaction time (blue) and error rate (pink) for an example subject (rat AL14) across 23 sessions. (b) Learning trajectory of individual subject (rat AL14) in speed-accuracy space. Color map indicates training time. Optimal performance curve (OPC) in blue. (c) Maximum $i⁢R⁢R$ opportunity cost (see Methods) for individual subject (rat AL14). (d) Mean reaction time (blue) and error rate (pink) for $n=26$ rats during learning. Sessions across subjects were transformed into normalized sessions, averaged and binned to show learning across 10 bins. Normalized training time allows averaging across subjects with different learning rates (see Methods). (e) Learning trajectory of $n=26$ rats in speed-accuracy space. Color map and OPC as in a. (f) Maximum $i⁢R⁢R$ opportunity cost of rats in b throughout learning. Errors reflect within-subject session SEMs for a and b and across-subject session SEMs for d, e, and f.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (a) ‘Canonical only’: rats trained to asymptotic performance with only front-view image of each of the two stimuli. ‘Size and rotation’: rats first shown front-view image of stimuli. After reaching criterion ($a⁢c⁢c⁢u⁢r⁢a⁢c⁢y=0.7$), size staircased. Following criterion, rotation staircased. Upon criterion, stimuli randomly drawn across size and rotation. (b) Learning trajectory in speed-accuracy space over normalized training time for rats trained with the ‘size and rotation’ (left panel) and the ‘canonical only’ training regimes (right panel). (c) Average location in speed-accuracy space for 10 sessions after asymptotic performance for individual rats in both training regimes, as in b. (d) Mean accuracy over learning (left panel) and for 5 sessions after asymptotic performance (right panel) for rats trained with the ‘size and rotation’ ($n=26$) and the ‘canonical only’ (n=8) training regimes. (e) Mean reaction time. (f) Mean fraction max $i⁢R⁢R$. (g) Mean total trials per session. (h) Mean voluntary intertrial interval up to 500 ms after error trials. (i) Mean fraction ignored trials. All errors are SEM. Significance in right panels of d–i determined by Wilcoxon rank-sum test with p<0.05.

### Learning DDM

To theoretically understand the effect of different learning strategies, we developed a simple linear RNN formalism for our task. This framework enables investigation of how long-term perceptual learning across many trials is influenced by the choice of decision time on individual trials (Figure 3). We first describe this neural network formalism, before showing how it can be analytically reduced to a classic DDM with time-dependent parameters that evolve over the course of learning.

![Figure 3.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig3-v1.jpg)

**Figure 3.:** (a) Roll out in time of recurrent neural network (RNN) for one trial. (b) The decision variable for the recurrent neural network (dark gray), and other trajectories of the equivalent DDM for different diffusion noise samples (light gray). (c, d, e) Changes in $E⁢R$, $D⁢T$, and $i⁢R⁢R$ over a long period of task engagement in the RNN (light gray, pixel simulation individual traces; black, pixel simulation mean; pink, Gaussian simulation mean) compared to the theoretical predictions from the learning DDM (blue). (f) Visualization of traces in c and d in speed-accuracy space along with the optimal performance curve (OPC) in green. The threshold policy was set to be $i⁢R⁢R$-sensitive for c–f.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (a) The recurrent linear neural network can be analytically reduced. In the reduction, the decision variable draws an observation from one of two randomly chosen Gaussian ‘stimuli’. The observations are scaled by a perceptual weight. After the addition of some irreducible noise, the value of the decision variable at previous time step is added to the current time step. A trial ends once the decision variable hits a predetermined threshold. The dynamics of the perceptual weight capture the mean effect of gradient descent learning in the recurrent linear neural network. (b) Weight w of neural network across task engagement time for multiple simulations of the network (gray), the mean of the simulations (black), and the analytical reduction of the network (blue). (c) Same as in b but for the threshold z. (d) Same as in b but for the error rate. (e) Same as in b but for the decision time. (f) Same as in b but for the instantaneous reward rate (correct trials per second). (g) Learning trajectory in speed-accuracy space for simulations, simulation mean, and analytical reduction (theory). Optimal performance curve (OPC) is shown in red.

#### Linear RNN

Our model takes the form of a simple RNN, depicted unrolled through time in Figure 3a. The network receives noisy sensory input over time during a trial, amplifies this evidence through weighted synaptic connections, and integrates the result until a threshold is reached. After making a decision and receiving feedback, the synaptic connections are updated a small amount according to an error-corrective gradient descent learning rule. Therefore, there are two key timescales in the model: first, the fast activity dynamics during a single trial, which produces a single decision with a certain reaction time; and second, the slow weight dynamics due to learning across many trials. In the following, we denote time within trial as the variable $t$, and the trial number as $t⁢r⁢i⁢a⁢l$. We now describe the dynamics on each timescale in greater detail.

Within a trial, $N$ dimensional inputs $s(t)\inR^{N}$ arrive at discrete times $t=1dt,2dt,⋯$, where $dt$ is a small time step parameter. In our experimental task, $s(t)$ might represent the activity of LGN neurons in response to a given visual stimulus. Because of eye motion and noise in the transduction from light intensity to visual activity, the response of individual neurons will only probabilistically relate to the correct answer at any given instant. In our simulations, we take $s⁢(t)$ to be the pixel values of the exact images presented to the animals, but transformed at each time point by small rotations (±20°) and translations (±25% of the image width and height), as depicted in Figure 3a. This input variability over time makes temporal integration valuable even in this visual classification task. To perform this integration, each input $s⁢(t)$ is filtered through perceptual weights $w(trial)\inR^{N}$ and added to a read-out node (decision variable) $y^(t)$ along with i.i.d. integrator noise $η(t)∼N(0,c_{o}^{2}dt)$. This integrator noise models internal neural noise. The evolution of the decision variable is given by the simple linear recurrence

$$
y^(t+dt)=y^(t)+w(trial)⋅s(t)+η(t),
$$

until the decision variable hits a threshold $\pmz⁢(t⁢r⁢i⁢a⁢l)$ that is constant on each trial. Here, the RNN already performs an integration through time (a choice motivated by prior experiments in rodents Brunton et al., 2013), and improvements in performance come from adjusting the input-to-integrator weights $w⁢(t⁢r⁢i⁢a⁢l)$ to better extract task-relevant sensory information.

Across trials, the perceptual weights $w⁢(t⁢r⁢i⁢a⁢l)$ are updated to improve performance. In principle this could be accomplished with many possible learning mechanisms such as reinforcement learning (Law and Gold, 2009) or Bayesian inference (Drugowitsch et al., 2019). Here, we investigate gradient-based optimization of an objective function, as commonly used in deep learning approaches (Richards et al., 2019, Saxe et al., 2021). In particular, we consider using gradient descent on the hinge loss, corresponding to standard practice in deep learning. The hinge loss is

$$
Loss(trial)=max(0,1−y(trial)y^(trial))
$$

where $y⁢(t⁢r⁢i⁢a⁢l)=\pm1$ is the correct output sign for the trial. Then the weights are updated by gradient descent on this loss,

$$
w(trial+1)=w(trial)−\lambda\frac{∂Loss(trial)}{∂w},
$$

where $\lambda$ is a small learning rate. The hinge loss is a proxy for accuracy, and so this weight update implements a learning scheme based on error feedback. In essence, perceptual weights are updated after error trials to improve the likelihood of answering correctly in the future.

To summarize the key parameters of the RNN, the model requires specifying the input distribution $s⁢(t)$, the initial perceptual weights $w⁢(0)$, the integrator noise variance $c_{o}^{2}$, the gradient descent learning rate $\lambda$, and the decision threshold $z⁢(t⁢r⁢i⁢a⁢l)$ used on each trial. With these parameters specified, the model can be simulated to make predictions for how behavior will evolve over training, as shown in Figure 3c–f, gray and black traces.

#### Reduction to LDDM

While the behavior of the RNN model obtained in simulations can be compared to data, deep network models remain challenging to understand (Saxe et al., 2021). We therefore sought to mathematically analyze this setting to derive a simple theory of the average learning dynamics that highlights key trade-offs.

We start by noting that the input to the decision variable $y^$ at each time step is a weighted sum of many random variables, which by the law of large numbers will be approximately Gaussian. We therefore develop a reduction of this model based on an effective Gaussian scalar input distribution. At each time step the input pathway receives a Gaussian input $x(t)∼N(Aydt,c_{i}^{2}dt)$, where $A$ parametrizes the signal related to $y$, and the input noise variance $c_{i}^{2}$ parametrizes irreducible noise in input channels that cannot be rejected. This input is multiplied by a scalar weight $u$, added to output noise $η$ of variance $c_{o}^{2}$ and sent into the integrating node $y^$,

$$
y^(t+dt)=y^(t)+u(trial)x(t)+η(t),
$$

where we emphasize that $u$ and $x⁢(t)$ are now both scalar. We may then perform gradient descent on the hinge loss, yielding the update $u⁢(t⁢r⁢i⁢a⁢l+1)=u⁢(t⁢r⁢i⁢a⁢l)-\lambda⁢\frac{\partial⁡L⁢o⁢s⁢s⁢(t⁢r⁢i⁢a⁢l)}{\partial⁡u}$. As expected from the law of large numbers, for the right choice of input signal and parameters $A$ and ci, simulations of this effective Gaussian model closely match the full simulation from pixels, as shown in Figure 3c–f, pink trace.

Next, to relate these dynamics to the well-studied DDM framework, we examine behavior when the time step is small ($d⁢t→0$) to obtain a continuous time formulation. In the continuum limit, these discrete within-trial dynamics of the network yield decision variables with identical distributions to a drift-diffusion process with an effective SNR $A¯$ and normalized threshold $z¯$

$$
A¯=\frac{A^{2}u^{2}}{u^{2}c_{i}^{2}+c_{o}^{2}},
$$



$$
z¯=\frac{z}{Au},
$$

yielding the mean error rate ($E⁢R$) and decision time ($D⁢T$)

$$
ER=\frac{1}{1+e^{2z¯A¯}},
$$



$$
D⁢T=z¯⁢tanh⁡(z¯⁢A¯).
$$

Finally, we assume that the learning rate is small ($\lambda≪1$), such that weights change little on any given trial and the gradient dynamics are driven by the mean update,

$$
u(trial+dt)=u(trial)−\lambda⟨\frac{∂Loss(trial)}{∂u}⟩
$$

where $⟨⋅⟩$ denotes the average with respect to the distribution of outputs obtained with perceptual weights $u⁢(t⁢r⁢i⁢a⁢l)$ and threshold $z⁢(t⁢r⁢i⁢a⁢l)$. These average dynamics depend in a complex way on the current performance of the network. We compute these average dynamics analytically (see Methods), yielding the continuous time change in effective SNR in the DDM that is equivalent to gradient descent learning in the underlying neural network model. In particular, gradient descent in the RNN is equivalent to the following SNR dynamics in the DDM:

$$
\tau~\frac{d}{dt}A¯(t)=2\sqrt{\frac{A¯(t)(A¯^{∗})}{c}}(1−\frac{A¯(t)}{A¯^{∗}})^{5/2}\frac{ER(t)}{DT(t)+D_{tot}(t)}[DT(t)−\frac{log⁡(1/ER(t)−1)}{A¯^{∗}(1−\frac{A¯(t)}{A¯^{∗}})^{2}}].
$$

Here, time $t$ measures seconds of task engagement (i.e. it measures time passing within a trial as well as intertrial time and any penalty delays after error trials), and $D_{t⁢o⁢t}⁢(t)=(1-E⁢R⁢(t))⁢D_{c⁢o⁢r⁢r}+(E⁢R⁢(t))⁢D_{e⁢r⁢r}$ is the average non-decision task engagement time per trial (where $D_{c⁢o⁢r⁢r}$ and $D_{e⁢r⁢r}$ are the average non-decision task engagement times after correct and error trials). The SNR dynamics depend on five parameters: the time constant $\tau~$ related to the learning rate, the initial SNR $A¯⁢(0)$, the asymptotic achievable SNR after learning $A¯^{*}$, the integration-noise to input-noise variance ratio $c≡c_{o}^{2}/c_{i}^{2}$, and the choice of threshold $z⁢(t)$ over training. We note that the dependence of the dynamics on the choice of threshold $z⁢(t)$ is implicit in $E⁢R⁢(t),D⁢T⁢(t)$, and $D_{t⁢o⁢t}⁢(t)$ in Equation 10. The dynamics of this LDDM closely tracks simulated trajectories of the full network from pixels (Figure 3c–f blue trace, Figure 3—figure supplement 1; see Methods).

Remarkably, this reduction shows that the high-dimensional dynamics of the RNN receiving stochastic pixel input and performing gradient descent on the weights (Figure 3, gray trace) can be described by a DDM with a single deterministic scalar variable – the effective SNR – that changes over time (Figure 3, blue trace). Notably, without the mapping to the original RNN, it is not possible to understand what effect error-corrective gradient descent learning would have at the level of the DDM, or how the learning process is influenced by choice of decision times. In particular, the change in SNR that arises from gradient descent on the underlying RNN weights (Equation 10) is not equivalent to that arising from gradient descent on the SNR parameter in the DDM directly because gradient descent is not parametrization invariant.

#### Learning speed trades off with instantaneous reward rate

The LDDM reveals that learning dynamics depend on the choice of threshold $z⁢(t)$ on each trial over learning, because threshold impacts both error rate and decision time, which appear in the SNR dynamics of Equation 10. We next sought to qualitatively understand this relationship. A key prediction of the LDDM is a tension between learning speed and $i⁢R⁢R$, the LS/$i⁢R⁢R$ trade-off. This tension is clearest early in learning when $ERs$ are near 50%. Then the rate of change in SNR is

$$
\frac{d}{dt}A¯∝\frac{DT}{DT+D_{tot}},
$$

where the proportionality constant does not depend on $D⁢T$ (see derivation, Methods). Hence learning speed increases with increasing $D⁢T$. By contrast, when accuracy is 50% the $i⁢R⁢R$ decreases with increasing $D⁢T$,

$$
iRR(t)≈\frac{1/2}{DT+D_{tot}}.
$$

When encountering a new task, therefore, agents face a dilemma: they can either harvest a large $i⁢R⁢R$ or they can learn quickly.

#### Learning dynamics depend on threshold policies

Just as the standard DDM instantiates different decision making strategies as different choices of threshold (for instance aimed at maximizing $i⁢R⁢R$, accuracy, or robustness) (Holmes and Cohen, 2014; Zacksenhouse et al., 2010), the LDDM instantiates different learning strategies through the choice of threshold trajectory over learning. Threshold affects $D⁢T$ and $E⁢R$, and through these, the learning dynamics in Equation 10. To consider a range of strategies, we developed four potential threshold policies.

Constant threshold. This policy implements a fixed constant threshold $z^{c}⁢(t)=z_{0}$. It serves as a control for behavior that would arise without the ability to modulate decision threshold. Constant thresholds across difficulties have been found to be used as part of near-optimal and presumably cognitively cheaper strategies in humans (Balci et al., 2011b). This policy introduces the parameter z0.

iRR-greedy. This policy sets the threshold to the value that maximizes instantaneous reward on each trial, $z^{g}⁢(t)=z^{*}⁢(A¯)$, such that behavior always lies on the OPC. This instantiates a ‘myopic’ strategy that does not consider how threshold can impact long-term learning. This policy is similar to a previously proposed neural network model of rapid threshold adjustment based on reward rate (Simen et al., 2006). The policy introduces no parameters.

iRR-sensitive. This policy implements a threshold $z^{s}⁢(t)$ that decays with time constant $\gamma$ from an initial value $z^{s}⁢(0)=z_{0}$ toward the $i⁢R⁢R$-optimal threshold,

$$
\gamma\frac{d}{dt}z^{s}(t)=z^{∗}(A¯(t))−z^{s}(t).
$$

Notably, as the SNR changes due to learning, the target threshold also changes through time. Asymptotically, this policy converges to greedy $i⁢R⁢R$-optimal behavior; however, by starting with a high initial threshold, it can undergo a transient period where responses are slower or faster than $i⁢R⁢R$-optimal, potentially influencing learning. It instantiates a heuristic strategy in which behavior differs from $i⁢R⁢R$-optimal behavior early in learning. This policy introduces two parameters, z0 and $\gamma$.

Global optimal. This policy selects the threshold $z^{o}⁢(t)$ that maximizes total cumulative reward at some known predetermined end to the task $T_{t⁢o⁢t}$,

$$
z^{o}(t)=argmaxz(t)⁡\int_{0}^{T_{tot}}RR(t)dt.
$$

We approximately compute this threshold function using automatic differentiation (see Methods). This policy serves as a normative oracle to which behavior may be compared. We note that this optimal policy considers the full time course of learning and is aware of all task parameters such as the duration of total task engagement $T_{t⁢o⁢t}$, asymptotically achievable SNR $A^{*}$, etc. In practice these parameters cannot be known before experiencing the task, and so this policy is not an implementable strategy but a normative reference point. The policy introduces no parameters.

In designing this model, we kept components as simple as possible to highlight key qualitative trade-offs between learning speed and decision strategy. Because of its simplicity, like the standard DDM, it is not meant to quantitatively describe all aspects of behavior. We instead use it to investigate qualitative features of decision making strategy, and expect that these features would be preserved in other related models of perceptual decision making (Usher and McClelland, 2001Mazurek et al., 2003, Gold and Shadlen, 2007, Heekeren et al., 2004Heekeren et al., 2008Ma et al., 2006Brown and Heathcote, 2008, Ratcliff and McKoon, 2008, Beck et al., 2008, Roitman and Shadlen, 2002; Purcell et al., 2010Bejjanki et al., 2011; Drugowitsch et al., 2012; Fard et al., 2017).

### Model reveals that prioritizing learning can maximize total reward

In order to qualitatively understand how these models behave through time, we visualized their learning dynamics. To approximately place the LDDM task parameters in a similar space to the rats, we performed maximum likelihood fitting using automatic differentiation through the discretized reduction dynamics (see Methods). The four policies we considered clustered into two groups, distinguished by their behavior early in learning. A ‘greedy’ group, which contained just the $i⁢R⁢R$-greedy policy, remained always on the OPC (Figure 4a), and had fast initial response times (Figure 4b), a long initial period at high error (Figure 4c), and high initial $i⁢R⁢R$ (Figure 4d). By contrast, a ‘non-greedy’ group, which contained the $i⁢R⁢R$-sensitive, constant threshold, and global optimal policies, started far above the OPC (Figure 4a), and had slow initial response times (Figure 4b), rapid improvements in ER (Figure 4c), and low $i⁢R⁢R$ (Figure 4d). Notably, while members of the non-greedy group started off with lower $i⁢R⁢R$, they rapidly surpassed the slow learning group (Figure 4d) and ultimately accrued more total reward (Figure 4e). Overall, these results show that threshold strategy strongly impacts learning dynamics due to the learning speed/$i⁢R⁢R$ trade-off (Figure 4f), and that prioritizing learning speed can achieve higher cumulative reward than prioritizing instantaneous reward rate.

![Figure 4.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig4-v1.jpg)

**Figure 4.:** (a) Model learning trajectories in speed-accuracy space plotted against the optimal performance curve (OPC) (black). (b) Decision time through learning for the four different threshold policies in a. (c) Error rate throughout learning for the four different threshold policies in a. (d) Instantaneous reward rate as a function of task engagement time for the full learning trajectory and a zoom-in on the beginning of learning (inset). (e) Cumulative reward as a function of task engagement time for the full learning trajectory and a zoom-in on the beginning of learning (inset). Threshold policies: $i⁢R⁢R$-greedy (green), constant threshold (blue), $i⁢R⁢R$-sensitive (orange), and global optimal (red). (f) In the speed-accuracy trade-off (left), $E⁢R$ (blue) decreases with increasing initial mean $RT$ (green) at high error rates (∼0.5) also decreases with increasing initial mean $R⁢T$. Thus, at high $ERs$, an agent solves the speed-accuracy trade-off by choosing fast $RTs$ that result in higher $ERs$ and maximize $i⁢R⁢R$. In the learning speed/ $i⁢R⁢R$ trade-off (right), initial learning speed ($d⁢S⁢N⁢R/d⁢t$, pink) increases with increasing initial mean $R⁢T$, whereas $i⁢R⁢R$ (green) follows the opposite trend. Thus, an agent must trade $i⁢R⁢R$ in order to access higher learning speeds. Plots generated using linear drift-diffusion model (LDDM).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (a) Deviance information criterion (DIC) for different hierarchical DDM (HDDM) fits to learning during stimulus pair 1 (lower value indicates a better fit). The models were fit to the first 1000 and last 1000 trials for every animal using the HDDM framework (Wiecki et al., 2013). Different parameters were allowed to vary with learning phase while the rest were fixed across learning phase. We fit three simple DDMs, one model that only allowed drift rate variability to vary with learning, three DDMs that included a fixed drift rate variability across learning phase (‘include drift variability’), and three DDMs where drift rate variability varied with learning in addition to different combinations of drift rate and threshold. The best models were those that allowed both drift rate and threshold to vary with learning. Including drift rate variability and allowing it to also vary with learning phase did not improve the model fits. Parameters for these model fits are included in the subsequent figures. (b) Same as a but for stimulus pair 2. The models were fit to the last 500 trials of baseline sessions with stimulus pair 1, and the first 500 trials and last 500 trials of stimulus pair 2, with each 500 trial batch serving as a learning phase. As with stimulus pair 1, the best models were those that allowed both drift rate and threshold to vary with learning, and drift rate variability did not appear to allow a better model fit.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (a) The learning data from stimulus pair 1 (a, b, c) and 2 (d, e, f) were fit with a simple DDM using the hierarchical DDM (HDDM) framework (Wiecki et al., 2013) as described in Figure 4—figure supplement 1. The HDDM reports posterior probability estimates for its parameters. The posterior for mean parameters across subjects is on the left of every panel, and the mean of the posterior for every individual fit is on the right of every panel. (a) While holding threshold constant, drift increased with learning. (b) While holding drift rate constant, threshold decreased with learning. (c) When allowing both drift rate and threshold to vary with learning, drift rate increased and threshold decreased with learning. (d) For stimulus pair 2, while holding threshold constant, drift increased with learning, matching its value during baseline sessions. (e) While holding drift rate constant, threshold decreased with learning, matching its value during baseline sessions. (f) When allowing both drift rate and threshold to vary with learning, drift rate increased and threshold decreased with learning, matching their values during baseline sessions. p-Values for mean estimates were calculated by taking the difference of the posteriors and counting the proportion of differences that was, depending on directionality 0. p-Values for individual estimates were calculated by taking a Wilcoxon rank-sum test across pairs.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** (a) The learning data from stimulus pair 1 (a, b, c) and 2 (d, e, f) were fit with a simple DDM + fixed drift rate variability using the hierarchical DDM (HDDM) framework (Wiecki et al., 2013) as described in Figure 4—figure supplement 1. (a) While holding threshold constant, drift increased with learning. (b) While holding drift rate constant, threshold decreased with learning. (c) When allowing both drift rate and threshold to vary with learning, drift rate increased and threshold decreased with learning. Drift rate variability estimates were close to 0. (d) For stimulus pair 2, while holding threshold constant, drift increased with learning, matching its value during baseline sessions. (e) While holding drift rate constant, threshold decreased with learning, matching its value during baseline sessions. (f) When allowing both drift rate and threshold to vary with learning, drift rate increased and threshold decreased with learning, matching their values during baseline sessions. p-Values were calculated as in Figure 4—figure supplement 2.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig4-figsupp4-v1.jpg)

**Figure 4—figure supplement 4.:** (a) The learning data from stimulus pair 1 (a, b, c) and 2 (d, e, f) were fit with a simple DDM + variable drift rate variability using the hierarchical DDM (HDDM) framework (Wiecki et al., 2013) as described in Figure 4—figure supplement 1. (a) While holding threshold constant, drift and drift rate variability increased with learning. (b) While holding drift rate constant, threshold and drift rate variability decreased with learning. (c) When allowing both drift rate and threshold to vary with learning, drift rate and drift rate variability increased and threshold decreased with learning. (d) For stimulus pair 2, while holding threshold constant, drift increased with learning, matching its value during baseline sessions, while drift rate variability trended toward decreasing with stimulus pair 2. (e) While holding drift rate constant, threshold decreased with learning, matching its value during baseline sessions, and drift rate variability decreased. (f) When allowing both drift rate and threshold to vary with learning, drift rate increased and threshold decreased with learning, matching their values during baseline sessions. Drift rate variability trended toward decreasing with stimulus pair 2. p-Values were calculated as in Figure 4—figure supplement 2.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig4-figsupp5-v1.jpg)

**Figure 4—figure supplement 5.:** (a) Fraction of instantaneous reward rate with respect to the $i⁢R⁢R$-greedy policy for all model threshold policies during learning. The instantaneous reward rates of all policies were normalized by the $i⁢R⁢R$-greedy policy’s instantaneous reward rate through task engagement time. (b) Same as a but for the full trajectory of the simulation. (c) Fraction of instantaneous reward rate with respect to the global optimal policy for all model threshold policies during learning. The instantaneous reward rates of all policies were normalized by the greedy policy’s instantaneous reward rate through task engagement time. (d) Same as c but for the full trajectory of the simulation.

We further analyzed the differences between the three strategies in the non-greedy group. The global optimal policy selects extremely slow initial $DTs$ to maximize the initial speed of learning. By contrast, the $i⁢R⁢R$-sensitive and constant threshold policies start with moderately slow responses. Nevertheless, we found that these simple strategies accrued 99% of the total reward of the global optimal strategy (Figure 4—figure supplement 5). Hence these more moderate policies, which do not require oracle knowledge of future task parameters, derive most of the benefit in terms of total reward and may reflect a reasonable approach when the duration of task engagement is unknown.

Considering the rats’ trajectories in light of these strategies, their slow responses early in learning stand in stark contrast to the fast responses of the $i⁢R⁢R$-greedy policy (Figure 2b, Figure 4a). Equally, their responses were faster than the extremely slow initial $DTs$ of the global optimal model. Both the $i⁢R⁢R$-sensitive and constant threshold models qualitatively matched the rats’ learning trajectory. However, the best DDM parameter fits of the rats’ behavior allowed their thresholds to decrease throughout learning, failing to support the constant threshold model (Figure 4—figure supplements 1–4). Subsequent experiments (Figure 6) provide further evidence against a simple constant threshold strategy. Consistent with substantial improvements in perceptual sensitivity through learning, DDM fits to the rats also showed an increase in drift rate throughout learning (Figure 4—figure supplements 1–4). Similar increases in drift rate have been observed as a universal feature of learning throughout numerous studies fitting learning data with the DDM (Ratcliff et al., 2006; Dutilh et al., 2009Petrov et al., 2011Balci et al., 2011b, Liu and Watanabe, 2012, Zhang and Rowe, 2014). These qualitative comparisons suggest that rats adopt a ‘non-greedy’ strategy that trades initial rewards to prioritize learning in order to harvest a higher $i⁢R⁢R$ sooner and accrue more total reward over the course of learning.

### Learning speed scales with reaction time

To test the central prediction of the LDDM that learning (change in SNR) scales with mean $D⁢T$, we designed an $R⁢T$ restriction experiment and studied the effects of the restriction on learning in the rats. Previously trained rats ($n=12$) were randomly divided into two groups in which they would have to learn a new stimulus pair while responding above or below their individual mean $RTs$ (‘slow’ and ‘fast’) for the previously trained stimulus pair (Figure 5a). Before introducing the new stimuli, we carried out practice sessions with the new timing restrictions to reduce potential effects related to a lack of familiarity with the new regime. After the restriction, $RTs$ were significantly different between the two groups (Figure 5b). In the model, we simulated an $R⁢T$ restriction by setting two different $DTs$ (Figure 5c).

![Figure 5.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig5-v1.jpg)

**Figure 5.:** (a) Schematic of experiment and hypothesized results. Previously trained animals were randomly divided into two groups: could only respond above (blue, $n=7$) or below (black, $n=5$) their individual mean reaction times for the previously trained stimulus and the new stimulus. Subjects responding above their individual mean reaction times were predicted to learn faster, reach a higher instantaneous reward rate sooner and accumulate more total reward. (b) Mean and individual reaction times before and after the reaction time restriction in rats. The mean reaction time for subjects randomly chosen to respond above their individual mean reaction times (blue, $n=7$) was not significantly different to those randomly chosen to respond below their individual means (black, $n=5$) before the restriction (Wilcoxon rank-sum test p > 0.05), but were significant after the restriction (Wilcoxon rank-sum test p < 0.05). Errors represent 95% confidence intervals. (c) In the model a long (blue) and a short (black) target decision time were set through a control feedback loop on the threshold, $\frac{d}{dt}z(t)=\gamma(DT_{targ}−DT(t))$ with parameter $\gamma=0.01$. (d) Mean accuracy ±95% confidence interval across sessions for rats required to respond above (blue, $n=7$) or below (black, $n=5$) their individual mean reaction times for a previously trained stimulus. Both groups had initial accuracy below chance because rats assume a response mapping based on an internal assessment of similarity of new stimuli to previously trained stimuli. To counteract this tendency and ensure learning, we chose the response mapping for new stimuli that contradicted the rats’ mapping assumption, having the effect of below-chance accuracy at first. * denotes p < 0.05 in two-sample independent $t$-test. Inset: accuracy change (slope of linear fit to accuracy across sessions to both groups, units: fraction per session). * denotes p < 0.05 in a Wilcoxon rank-sum test. (e) Mean inferred signal-to-noise ratio (SNR), (f) mean, $i⁢R⁢R$ and (g) mean cumulative reward across task engagement time for new stimulus pair for animals in each group. (h) Accuracy, (i) SNR, (j) $i⁢R⁢R$, and (k) cumulative reward across task engagement time for long (blue) and short (black) target decision times in the linear drift-diffusion model (LDDM).

We found no difference in initial mean session accuracy between the two groups, followed by significantly higher accuracy in the slow group in subsequent sessions (Figure 5d). The slope of accuracy across sessions was significantly higher in the slow group (Figure 5d, inset). Importantly, the fast group had a positive slope and an accuracy above chance by the last session of the experiment, indicating this group learned (Figure 5d).

Because of the SAT in the DDM, however, accuracy could be higher in the slow group even with no difference in perceptual sensitivity (SNR) or learning speed simply because on average they view the stimulus for longer during a trial, reflecting a higher threshold. To see if underlying perceptual sensitivity increased faster in the slow group, we computed the rats’ inferred SNR throughout learning (see Methods, Equation 24), which takes account of the relationship between $R⁢T$ and $E⁢R$. The SNR of the slow group increased faster (Figure 5e), consistent with a learning speed that scales with $D⁢T$.

We found that the slow group had a lower initial $i⁢R⁢R$, but that this $i⁢R⁢R$ exceeded that of the fast group halfway through the experiment (Figure 5f). Similarly, the slow group trended toward a higher cumulative reward by the end of the experiment (Figure 5g). The LDDM qualitatively replicates all of our behavioral findings (Figure 5h–k). These results demonstrate the potential total reward benefit of faster learning, which in this case was a product of enforced slower $RTs$.

Our experiments and simulations demonstrate that longer $RTs$ lead to faster learning and higher reward for our task setting both in vivo and in silico. Moreover, they are consistent with the hypothesis that rats choose high initial $RTs$ in order to prioritize learning and achieve higher $iRRs$ and cumulative rewards during the task.

### Rats choose reaction time based on learning prospects

The previous experiments suggest that rats trade initial rewards for faster learning. Nonetheless, it is unclear how much control rats exert over their $RTs$. A control-free heuristic approach, such as adopting a fixed high threshold (our constant threshold policy), might incidentally appear near optimal for our particular task parameters, but might not be responsive to changed task conditions. If an agent is controlling the reward investment it makes in the service of learning, then it should only make that investment if it is possible to learn.

To test whether the rats’ $R⁢T$ modulations were sensitive to learnability, we conducted a new experiment in which we divided rats into a group that encountered new learnable visible stimuli ($n=16$, sessions = 13), and another that encountered unlearnable transparent or near-transparent stimuli ($n=8$, sessions = 11) (Figure 6a). From the perspective of the LDDM, both groups start with approximately zero SNR, however only the group with the visible stimuli can improve that SNR. Because the rats do not know the learnability of new stimuli, we initialize the LDDM with a high threshold to model the belief that any new stimuli may be learnable. If the rats choose their $RTs$ based on how much it is possible to learn, then: (1) rats encountering new stimuli that they can learn will increase their $RTs$ to learn quickly and increase future $i⁢R⁢R$. (2) Rats encountering new stimuli that they cannot learn might first increase their $RTs$ to learn that there is nothing to learn, but (3) will subsequently decrease $RTs$ to maximize $i⁢R⁢R$.

![Figure 6.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig6-v1.jpg)

**Figure 6.:** (a) Schematic of experiment: rats trained on stimulus pair 1 were presented with new visible stimulus pair 2 or transparent (alpha = 0, 0.1) stimuli. If rats change their reaction times based on stimulus learnability, they should increase their reaction times for the new visible stimuli to increase learning and future $i⁢R⁢R$ and decrease their reaction time to increase $i⁢R⁢R$ for the transparent stimuli. (b) Learning across normalized sessions in speed-accuracy space for new visible stimuli ($n=16$, crosses) and transparent stimuli ($n=8$, squares). Color map indicates time relative to start and end of the experiment. (c) $i⁢R⁢R$-sensitive threshold model runs with ‘visible’ (crosses) and ‘transparent’ (squares) stimuli (modeled as containing some signal, and no signal) plotted in speed-accuracy space. The crosses are illustrative and do not reflect any uncertainty. Color map indicates time relative to start and end of simulation. (d) Mean change in reaction time across sessions for visible stimuli or transparent stimuli compared to previously known stimuli. Positive change means an increase relative to previous average. Inset: first and second half of first session for transparent stimuli. * denotes $p<0.05$ in permutation test. (e) Correlation between initial individual mean change in reaction time (quantity in d) and change in signal-to-noise ratio (SNR) (learning speed: slope of linear fit to SNR per session) for first three sessions with new visible stimuli. R2 and $p$ from linear regression in d. Error bars reflect standard error of the mean in b and d. (f) Decision time across time engagement time for visible and transparent stimuli runs in model simulation. (g) Instantaneous change in SNR ($\frac{d}{d⁢t}⁢A¯$) as a function of initial reaction time (decision time + non-decision time T0) in model simulation.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (a) During transparent stimuli, the reaction time ($R⁢T$) minimum was relaxed to 0 ms to fully measure a possible shift in $R⁢T$ behavior. To be able to ascertain whether transparent stimuli led to a significant change in $R⁢T$, the $R⁢T$ histogram of transparent stimuli (early [first two sessions]: purple, late [last two sessions]: yellow) sessions was compared to control sessions with visible stimuli (gray) with no $R⁢T$ minimum. Medians indicated with dashed lines. Kolmogorv-Smirnov two-sample tests over distributions found significant differences ($p<10^{−4}$). (b) Vincentized $RTs$ for transparent and control visible stimuli sessions with no minimum reaction time showed the early transparent sessions were slower than the control sessions, and the late sessions were faster across quantiles.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** (a) Vincentized reaction time distributions for $n=26$ subjects learning stimulus pair 1 (first 3 sessions, purple; last 10 asymptotic sessions, yellow). (b) Vincentized reaction time distributions for $n=16$ subjects learning stimulus pair 2 (first 2 sessions, purple; last 2 sessions, yellow). (b) Vincentized reaction time distributions for $n=8$ subjects learning transparent stimuli (first 2 sessions, purple; last 2 sessions, yellow).

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig6-figsupp3-v1.jpg)

**Figure 6—figure supplement 3.:** (a) The learning data from transparent stimuli were fit with a simple DDM + variable drift rate variability using the hierarchical DDM (HDDM) framework (Wiecki et al., 2013). Three learning phases were included: the last 500 trials with control visible stimuli, and the first 500 and the last trials with transparent stimuli. (a) We allowed drift rate, threshold, drift rate variability, and T0 to vary with learning phase. Drift rate decreased with transparent stimuli, remaining constant throughout. Threshold monotonically decreased with transparent stimuli. Drift rate variability appeared to decrease and stay constant with transparent stimuli, albeit at a value near 0. T0 appeared to decrease with transparent stimuli. p-Values were calculated as in Figure 4—figure supplement 2.

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig6-figsupp4-v1.jpg)

**Figure 6—figure supplement 4.:** In order to measure the extent of stimulus-independent strategies for transparent stimuli, we fit baseline sessions with visible stimuli and sessions with the transparent stimuli with PsyTrack, a flexible generalized linear model (GLM) package for measuring the weights of different inferred psychophysical variables (Roy et al., 2021). We fit our data with a model that included bias, win-stay/lose-switch (previous trial outcome), perseverance (previous trial choice), and the actual stimulus as potential explanatory variables for left/right choice behavior. (a) Measurement of bias across $n=8$ animals. Generally, bias and bias variability increased with transparent stimuli compared to visible stimuli. Although not uniform, animals tended to become more biased to the side that they were already biased during visible stimuli. (b) During visible stimuli, the stimulus had strong non-zero weights, indicating it influenced choice behavior. Stimulus has positive weights for some animals and negative for others because stimuli mappings were counterbalanced across animals. Win-stay/lose-switch and perseverance weights varied across animals during visible stimuli. Generally, these variables increased weights and variability during transparent stimuli, while the stimulus collapsed to a weight of 0 (as expected, given it was transparent). The weight of the bias variable was omitted for visual clarity as the actual bias was reported in a.

![Figure 6—figure supplement 5.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig6-figsupp5-v1.jpg)

**Figure 6—figure supplement 5.:** (a) Individual (gray) and mean (black) post-error slowing across first 15 sessions for $n=26$ animals. Post-error slowing was calculated by taking the difference between $RTs$ on trials with previous correct trials and previous error trials. A positive difference indicates post-error slowing. (b) Individual mean (gray) and population mean (black) post-error slowing for first 2 sessions of learning and last 2 sessions of learning for $n=26$ animals. A Wilcoxon signed-rank test found no significant difference in post-error slowing between the first 2 and last 2 sessions for every animal (p = 0.585). (c) Same as in a for $n=16$ rats, with the addition of 4 baseline sessions with stimulus pair 1 plus the 13 sessions while subjects were learning stimulus pair 2. (d) Same as in b but comparing the last 2 baseline sessions with stimulus pair 1 and the first 2 sessions learning stimulus pair 2. A Wilcoxon signed-rank test found no significant difference in post-error slowing when the animals started learning stimulus pair 2 (p = 0.255).

We found that the rats with the visible stimuli qualitatively replicated the same trajectory in speed-accuracy space that we found when rats were trained for the first time (Figure 2b, Figure 6b). Indeed, the best DDM fits were those that allowed both threshold and drift rate to vary with learning, as was the case with the first stimuli the rats encountered, and in line with the LDDM (Figure 4—figure supplements 1–4). Because these previously trained rats had already mastered the task mechanics, this result rules out non-stimulus-related learning effects as the sole explanation for long $RTs$ at the beginning of learning and supports our hypothesis that the slowdown in $R⁢T$ was attributable to the rats trying to learn the new stimuli efficiently. We calculated the mean change in $R⁢T$ (mean ΔRT) of new stimuli versus known stimuli. The visible stimuli group had a significant slowdown in $R⁢T$ lasting many sessions that returned to baseline by the end of the experiment (Figure 6d, black trace).

Rats with the transparent stimuli also approached the OPC by decreasing their $RTs$ across sessions to better maximize $i⁢R⁢R$ (Figure 6b). After a brief initial increase in $R⁢T$ in the first half of the first session (Figure 6d, inset), $RTs$ rapidly decreased (Figure 6d, gray trace). Notably, $RTs$ fell below the baseline $RTs$, indicating a strategy of responding quickly, which approaches $i⁢R⁢R$-optimal behavior for this zero SNR task. Additionally, we considered the rats’ entire $R⁢T$ distributions to investigate the effect of learnability beyond $R⁢T$ means. We found that while the $R⁢T$ distributions changed similarly from the beginning to end of learning for the learnable stimuli (stimulus pair 1 and 2), they differed for the unlearnable (transparent) stimuli, indicating an effect of learnability on the entire $R⁢T$ distributions (Figure 6—figure supplement 2). Hence, rodents are capable of modulating their strategy depending on their learning prospects.

Although there is no informative signal in this task with transparent stimuli, the rats could still be using stimulus-independent signals, such as choice history or feedback, to drive heuristic strategies. Indeed, DDM fits indicated a non-zero drift rate even in the absence of informative stimuli (Figure 6—figure supplement 3). To investigate whether the rats implemented stimulus-independent heuristic strategies in addition to random choice, we measured left/right bias and quantified the weights of bias, perseverance (choose the same port as the previous trial), and win-stay/lose-switch (choose the port that was correct on the previous trial) (Roy et al., 2021). In general, bias seemed to increase with transparent stimuli in the direction that each individual was already biased during visible stimuli. Perseverance and win-stay/lose-switch also seemed to increase and fluctuate more during transparent stimuli, suggesting a greater reliance on these heuristics now that the stimulus was uninformative (Figure 6—figure supplement 4). Engaging these heuristics may be a way that the rats expedited their choices in order to maximize $i⁢R⁢R$ while still ‘monitoring’ the task for any potentially informative changes or patterns. Despite the fact that the animals’ still engaged these non-optimal heuristics, the lack of learnability in the transparent stimuli still led to a change in strategy that was distinct from that with learnable stimuli.

Importantly, this learnability experiment argues against other simple strategies accounting for the changes in $RTs$. If rats respond more slowly after error trials, a phenomenon known as post-error slowing (PES), they might exhibit slower $RTs$ early in learning when errors are frequent (Notebaert et al., 2009). Indeed, we found a slight mean post-error slowing effect of about 50 ms that was on average constant throughout learning, though it was highly variable across individuals (Figure 6—figure supplement 5). However, rats viewing transparent stimuli had $ERs$ constrained to 50%, yet their $RTs$ systematically decreased (Figure 6b), such that post-error slowing alone cannot account for their strategy. Similarly, choosing $RTs$ as a simple function of time since encountering a task would not explain the difference in $R⁢T$ trajectories between visible and transparent stimuli (Figure 6d).

A simulation of this experiment with the $i⁢R⁢R$-sensitive threshold LDDM qualitatively replicated the rats’ behavior (Figure 6c, f and g). Rodent behavior is thus consistent with a threshold policy that starts with a relatively long $D⁢T$ upon encountering a new task, and then decays toward the $i⁢R⁢R$-optimal $D⁢T$. All other threshold strategies we considered fail to account for the totality of the results. The $i⁢R⁢R$-greedy strategy – as before – stays pinned to the OPC and speeds up upon encountering the novel stimuli rather than slowing down. The constant threshold strategy fails to predict the speed-up in $D⁢T$ for the transparent stimuli if we assume constant diffusion noise. This is because when the perceptual signal is small, mean $D⁢T$ can be shown to be the squared ratio of threshold to diffusion noise (see Methods). It is thus also possible to explain the speed-up with a constant threshold and increasing diffusion noise. With either interpretation, however, it is clear that a policy where the ratio of threshold to diffusion noise is constant is not compatible with the results. Finally, the global optimal strategy (which has oracle knowledge of the prospects for learning in each task) behaves like the $i⁢R⁢R$-greedy policy from the start on the transparent stimuli as there is nothing to learn.

Our $R⁢T$ restriction experiment showed that higher initial $RTs$ led to faster learning, a higher $i⁢R⁢R$ and more cumulative reward. Consistent with these findings, there was a correlation between initial mean ΔRT and initial ΔSNR across subjects viewing the visible stimuli, indicating the more an animal slowed down, the faster it learned (Figure 6e). We further tested these results in the voluntary setting by tracking $i⁢R⁢R$ and cumulative reward for the rats in the learnable stimuli setting with the largest (blue, $n=4$) and smallest (black, $n=4$) ‘self-imposed’ change in $R⁢T$ (Figure 7a). The rats with the largest change started with a lower but ended with a higher mean iRR, and collected more cumulative reward (Figure 7b and c). Thus, in the voluntary setting there is a clear relationship between $R⁢T$, learning speed, and its total reward benefits.

![Figure 7.](https://cdn.elifesciences.org/articles/64978/elife-64978-fig7-v1.jpg)

**Figure 7.:** (a) Schematic showing segregation of top 25% of subjects ($n=4$) with the largest initial ΔRTs for the new visible stimuli and the bottom 25% of subjects ($n=4$) with the smallest initial ΔRTs. Initial ΔRTs were calculated as an average of the first two sessions for all subjects. (b) Mean $i⁢R⁢R$ for subjects with largest and smallest mean changes in reaction time across task engagement time. (c) Mean cumulative reward over task engagement time for subjects as in b.

## Discussion

### Summary and limitations

Our theoretical and empirical results identify a trade-off between the need to learn rapidly and the need to accrue immediate reward in a perceptual decision making task. We find that rats adapt their decision strategy to improve learning speed and approximately maximize total reward, effectively navigating this trade-off over the total period of task engagement. In our experiments, rats responded slowly upon encountering novel stimuli, but only when there was a visual stimulus to learn from. This result indicates that they chose to respond more slowly in order to learn quickly, and only made the investment when learning was possible. This behavior requires foregoing both a cognitively easier strategy – fast random choice – and relinquishing a higher immediately available reward for several sessions spanning multiple days. By imposing different response times in groups of animals, we empirically verified our theoretical prediction that slow responses lead to faster learning and greater total reward in our task. These findings collectively show that rats exhibit cognitive control of the learning process, that is, the ability to engage in goal-directed behavior that would otherwise conflict with default or more immediately rewarding responses (Dixon et al., 2012, Shenhav et al., 2013; Shenhav et al., 2017, Cohen et al., 1990; Cohen and Egner, 2017).

Our high-throughput behavioral study with a controlled training protocol permits examination of the entire trajectory of learning, revealing hallmarks of non-greedy decision making. Nonetheless, it is accompanied by several experimental limitations. Our estimation of SNR improvements during learning relies on the DDM. Importantly, while this approach has been widely used in prior work (Brunton et al., 2013; Ratcliff et al., 2006; Balci et al., 2011b; Drugowitsch et al., 2019; Petrov et al., 2011 ), our conclusions are predicated on this model’s approximate validity for our task. Future work could address this issue by using a paradigm in which learners with different response deadlines are tested at the same fixed response deadline, equalizing the impact of stimulus exposure at test. This model-free paradigm is not trivial in rodents, because response deadlines cannot be rapidly instructed. Our study also focuses on one visual perceptual task. Further work should verify our findings with other perceptual tasks across difficulties, modalities, and organisms.

To understand possible learning trajectories, we introduced a theoretical framework based on an RNN, and from this derived an LDDM. The LDDM extends the canonical drift-diffusion framework to incorporate long-term perceptual learning, and formalizes a trade-off between learning speed and instantaneous reward. However, it remains approximate and limited in several ways. The LDDM builds off the simplest form of a DDM, while various extensions and related models have been proposed to better fit behavioral data, including urgency signals (Ditterich, 2006; Cisek et al., 2009; Deneve, 2012; Hanks et al., 2011; Drugowitsch et al., 2012), history-dependent effects (Busse et al., 2011; Scott et al., 2015; Akrami et al., 2018; Odoemene et al., 2018; Pinto et al., 2018; Lak et al., 2018; Mendonça et al., 2018), imperfect sensory integration (Brunton et al., 2013), confidence (Kepecs et al., 2008; Lak et al., 2014; Drugowitsch et al., 2019), and multi-alternative choices (Krajbich and Rangel, 2011, Tajima et al., 2019). Prior work in the DDM framework has investigated learning dynamics with a Bayesian update and constant thresholds across trials (Drugowitsch et al., 2019). Our framework uses simpler error-corrective learning rules, and focuses on how the decision threshold policy over many trials influences long-term learning dynamics and total reward. Future work could combine these approaches to understand how Bayesian updating on each trial would change long-term learning dynamics, and potentially, the optimality of different threshold strategies.

More broadly, it remains unclear whether the drift-diffusion framework in fact underlies perceptual decision making, with a variety of other proposals providing differing accounts (Gold and Shadlen, 2007, Zoltowski et al., 2019; Stine et al., 2020). We speculate that the qualitative learning speed/instantaneous reward rate trade-off that we formally derive in the LDDM would also arise in other models of within-trial decision making dynamics. In addition, on a long timescale over many trials, the LDDM improves performance through error-corrective learning. Future work could investigate learning dynamics under other proposed learning algorithms such as feedback alignment (Lillicrap et al., 2016), node perturbation (Williams, 1992), or reinforcement learning (Law and Gold, 2009). Additionally, the LDDM does not currently include a meta-learning component with which the agent can dynamically gauge the learnability of the task explicitly in order to set its decision threshold. Instead, the LDDM assumes a ‘learnability prior’ implemented as a high initial threshold condition for every new task. This limitation could be solved with a Bayesian observer that predicts learnability based on experience and controls the threshold accordingly. One potential avenue in this direction would be the implementation of the learned value of control theory, which provides a mechanism through which an agent can compare stimulus features to those it has encountered in the past in order to determine control allocation (Lieder et al., 2018). Moreover, the link between the LDDM and cognitive control is implicit: we interpret the choice of threshold in the DDM as a control process (a higher threshold than is optimal reflects control because it requires foregoing present reward in the service of future reward). Future modeling work should make the choice of control explicit, taking into account the inherent cost of control (Shenhav et al., 2013), and then using that choice to determine the decision threshold. Doing so would allow control to not only reflect the choice of threshold, as we have done, but also as a gain term on the drift rate (Leng et al., 2021), which may more completely capture control’s role in two-choice decisions.

### Explore/exploit trade-off

Conceptually, the learning speed/instantaneous reward rate trade-off is related to the explore/exploit trade-off common in reinforcement learning, but differs in level of analysis. As traditionally framed in reinforcement learning, an agent has the option of maximizing reward based on its current information (exploitation), or of reaching a potentially larger future reward by expanding its current information (exploration). When framed this way, learning is an act of exploration. However, as framed in our study, learning is a systematic, directed strategy (or ‘action’), that is, exploitation, employed in order to maximize total future reward. The reconciliation between these seemingly contradictory accounts occurs at the meta-level: when an agent is aware that learning is the optimal strategy to maximize total future discounted reward, it is exploiting a strategy that trades learning speed for instantaneous reward rate. However, when that agent is not yet aware whether it can learn, then it must explore this question (i.e. meta-learn) before deciding whether it should exploit an explicit learning strategy (‘exploitation of exploration’) that will also come at the cost of instantaneous reward. Although explained sequentially, these two mechanisms can occur in parallel (i.e. an agent constantly probing its learning prospects). One intriguing finding is that state-of-the-art deep reinforcement learning agents, which succeed in navigating the traditional explore/exploit dilemma on complicated tasks like Atari games (Mnih et al., 2016), nevertheless fail to learn perceptual decisions like those considered here (Leibo et al., 2018). This may be because exploration and exploitation can mean different things depending on the level of analysis, and efficiently learning a perceptual task may require the ‘exploitation of exploration’. Our findings may thus offer routes for improving these artificial systems.

### Cognitive control

In order to navigate the learning speed/instantaneous reward rate trade-off, our findings suggest that rats deploy cognitive control of the learning process. Two main features of cognitive control govern its use: it is limited (Shenhav et al., 2017), and it is costly (Krebs et al., 2010; Padmala and Pessoa, 2011, Kool et al., 2010, Dixon et al., 2012; Westbrook et al., 2013; Kool and Botvinick, 2018; Westbrook et al., 2019). If control is costly, then its application needs to be justified by the benefits of its application. The expected value of control (EVC) theory posits that control is allocated in proportion to the EVC (Shenhav et al., 2013). Previous work demonstrated that rats are capable of the economic reasoning required for optimal control allocation (Niyogi et al., 2014a; Niyogi et al., 2014b; Sweis et al., 2018). We demonstrated that rats incur a substantial initial instantaneous reward rate opportunity cost to learn the task more quickly, foregoing a cognitively less demanding fast random strategy that would yield higher initial rewards. Rather than optimizing instantaneous reward rate, which has been the focus of prior theories (Gold and Shadlen, 2002, Balci et al., 2011b; Bogacz et al., 2006), our analysis suggests that rats approximately optimize total reward over task engagement. Relinquishing initial reward to learn faster, a cognitively costly strategy, is justified by a larger total reward over task engagement. This pattern of behavior matches theoretical predictions of the value of learning based on a recent expansion of the EVC theory (Masís et al., 2021).

Assessing the expected value of learning in a new task requires knowing how much can be learned, how quickly one can learn, and for how long the task will be performed (Masís et al., 2021). None of these quantities is directly observable upon first encountering a new task, leading to the question of how rodents know to slow down in one task but not another. Importantly, rats only traded reward for information when learning was possible, a result in line with data demonstrating that humans are more likely to trade reward for information during long experimental time horizons, when learning is more likely (Wilson et al., 2014). Monkeys also reduce their reliance on expected value during decision making in order to explore strategically when it is deemed beneficial (Jahn et al., 2022). Moreover, previous work has highlighted the explicit opportunity cost of longer deliberation times (Drugowitsch et al., 2012), a trade-off that will differ during learning and at asymptotic performance, as we demonstrate here. One possibility is that rats estimate learnability and task duration through meta-learning processes that learn to estimate the value of learning through experience with many tasks (Finn et al., 2017; Wang et al., 2018; Metcalfe, 2009). The amount of control allocated to learning the current task could be proportional to its estimated value, determined based on similarity to previous learning situations and their reward outcomes and control costs (Lieder et al., 2018). Some of this bias for new information, termed curiosity, could be partly endogenous, serving as a useful heuristic for organisms outside of the lab, where rewards are sparse and action spaces are broad (Gottlieb and Oudeyer, 2018). Previous observations of suboptimal decision times in humans analogous to those we observed in rats might reflect incomplete learning, or subjects who think they still have more to learn (Balci et al., 2011b; Bogacz et al., 2010; Cohen et al., 1990). Future work could test further predictions emerging from a control-based theory of learning. An agent should assess both the predicted duration of task engagement and the predicted difficulty of learning in order to determine the optimal decision making strategy early in learning, and this can be tested by, for instance, manipulating the time horizon and difficulty of the task. From a control-based perspective, the expected reward from a task is also relevant to control allocation. Indeed, recent work in humans shows that externally motivating learners with the prospect of a test at the end of a task led to a much higher allocation of time on the harder-to-learn items compared to the case when learners were not warned of a test (Ten et al., 2020).

The trend of a decrease in response time and an increase in accuracy through practice – which we observed in our rats – has been widely observed for decades in the skill acquisition literature, and is known as the Law of Practice (Thorndike, 1913, Newell and Rosenbloom, 1981, Logan, 1992, Heathcote et al., 2000). Accounts of the Law of Practice have posited a cognitive control-mediated transition from shared/controlled to separate/automatic representations of skills with practice (Posner and Snyder, 1975, Shiffrin and Schneider, 1977, Cohen et al., 1990). On this view, control mechanisms are a limited, slow resource that impose unwanted processing delays. Our results suggest an alternative non-mutually exclusive reward-based account for why we may so ubiquitously observe the Law of Practice. Slow responses early in learning may be the goal of cognitive control, as they allow for faster learning, and faster learning leads to higher total reward. When faced with the ever-changing tasks furnished by naturalistic environments, it is the speed of learning which may exert the strongest impact on total reward.

### Bounded optimality

More broadly, the optimization of behavior, not in a vacuum, but in the context of one’s constraints – intrinsic and environmentally determined – underlies several general theories of cognition, including theories that explain the allocation of cognitive control (Shenhav et al., 2013; Lieder et al., 2018), the selection of decision heuristics (Gigerenzer, 2008), and the rationale of seemingly irrational economic choices (Kahneman and Tversky, 1979, Juechems et al., 2021). These theories are instances of bounded optimality – a prominent theoretical framework of biological and artificial cognition stating that an agent is optimal when it maximizes reward per unit time within the limitations of its computational architecture (Russell and Subramanian, 1994, Lewis et al., 2014; Gershman et al., 2015; Griffiths et al., 2015; Bhui et al., 2021; Summerfield and Parpart, 2021).

Instances of this framework typically assume that cognitive constraints remain fixed and, more so, that agents do not take alterations of these constraints into account when choosing what to do. There exists, however, a novel theoretical avenue within this framework. An agent can optimize its behavior not only through maximization of reward within constraints, but also through the minimization of those constraints themselves. If an agent can change itself to minimize its constraints by, for example, improving its perceptual representations through learning, the future reward prospects of doing so should be considered in its current choices, even if it is at the expense of current reward. Intelligent agents, like humans, can and do change themselves through learning in order to improve future reward prospects. Our study formalizes this phenomenon in the context of two-choice perceptual decisions, but much work remains to be done in other contexts, modalities, and organisms.

## Methods

### Behavioral training

#### Subjects

All care and experimental manipulation of animals were reviewed and approved by the Harvard Institutional Animal Care and Use Committee (IACUC), protocol 27–22. We trained animals on a high-throughput visual object recognition task that has been previously described (Zoccolan et al., 2009). A total of 44 female Long-Evans rats were used for this study, with 38 included in analyses. Twenty-eight rats (AK1–12 and AL1–16) initiated training on stimulus pair 1, and 26 completed it (AK8 and AL12 failed to learn). Another 8 animals (AM1–8) were trained on stimulus pair 1 but were not included in the initial analysis focusing on asymptotic performance and learning (Figure 1d and e; Figure 2) because they were trained after the analyses had been completed. Subjects AM5–8, although trained, did not participate in other behavioral experiments so do not appear in this study. Sixteen animals (AL1–8, AL13–16, and AM1–8) participated in learning stimulus pair 2 (‘new visible stimuli’; canonical-only training regime) while 10 animals (AK1–3, 5–7, 9–12) initially participated in viewing transparent (alpha = 0; AK1, 3, 6, 7, 11) or near-transparent stimuli (alpha = 0.1; AK2, 5, 9, 10, 12), with the subjects sorted randomly into each group. The transparent and near-transparent groups were aggregated but two animals from the near-transparent group were excluded for performing above chance (AK5 and AK12) as this experiment focused on the effects of stimuli that could not be learned. The same 16 animals used for stimulus pair 2 were used for learning stimulus pair 3 under two different reaction time restrictions in which the subjects were sorted randomly. One rat (AL1) was excluded from the outset for not having learned stimulus pair 2. Two additional rats (AL4 and AL7) were excluded for not completing enough trials during practice sessions with the new reaction time restrictions. A final rat (AM1) was excluded because she failed to learn the task. The 12 remaining rats were grouped into seven subjects required to respond above (AL3, AL8, AL13, AL15, AL16, AM3, AM4) and five subjects required to respond below their individual average reaction times (AL2, AL5, AL6, AL14, AM2). Finally, eight rats (AN1–8) were trained on a simplified training regime (‘canonical only’) used as a control for the typical ‘size and rotation’ training object recognition regime (described below). Table 1 summarizes individual subject participation across behavioral experiments.

**Table 1.**
 Individual animal participation across behavioral experiments.


<table>
  <thead>
    <tr>
      <th>Animal</th>
      <th>Sex</th>
      <th>Stimulus pair 1</th>
      <th>Stimulus pair 2</th>
      <th>Transparent stimuli</th>
      <th>Stimulus pair 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AK1</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Alpha = 0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AK2</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Alpha = 0.1</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AK3</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Alpha = 0.0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AK4</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AK5</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Alpha = 0.1 (excluded)‡</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AK6</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Alpha = 0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AK7</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Alpha = 0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AK8</td>
      <td>F</td>
      <td>Size and rotation (excluded)*</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AK9</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Alpha = 0.1</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AK10</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Alpha = 0.1</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AK11</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Alpha = 0.0</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AK12</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Alpha = 0.1 (excluded)‡</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AL1</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Canonical only</td>
      <td>(Excluded)§</td>
      <td></td>
    </tr>
    <tr>
      <td>AL2</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Canonical only</td>
      <td>Below</td>
      <td></td>
    </tr>
    <tr>
      <td>AL3</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Canonical only</td>
      <td>Above</td>
      <td></td>
    </tr>
    <tr>
      <td>AL4</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Canonical only</td>
      <td>Below (excluded) ¶</td>
      <td></td>
    </tr>
    <tr>
      <td>AL5</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Canonical only</td>
      <td>Below</td>
      <td></td>
    </tr>
    <tr>
      <td>AL6</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Canonical only</td>
      <td colspan="2">Below</td>
    </tr>
    <tr>
      <td>AL7</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Canonical only</td>
      <td colspan="2">Below (excluded)¶</td>
    </tr>
    <tr>
      <td>AL8</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Canonical only</td>
      <td colspan="2">Above</td>
    </tr>
    <tr>
      <td>AL9</td>
      <td>F</td>
      <td colspan="4">Size and rotation</td>
    </tr>
    <tr>
      <td>AL10</td>
      <td>F</td>
      <td colspan="4">Size and rotation</td>
    </tr>
    <tr>
      <td>AL11</td>
      <td>F</td>
      <td colspan="4">Size and rotation</td>
    </tr>
    <tr>
      <td>AL12</td>
      <td>F</td>
      <td colspan="4">Size and rotation (excluded)*</td>
    </tr>
    <tr>
      <td>AL13</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Canonical only</td>
      <td colspan="2">Above</td>
    </tr>
    <tr>
      <td>AL14</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Canonical only</td>
      <td colspan="2">Below</td>
    </tr>
    <tr>
      <td>AL15</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Canonical only</td>
      <td colspan="2">Above</td>
    </tr>
    <tr>
      <td>AL16</td>
      <td>F</td>
      <td>Size and rotation</td>
      <td>Canonical only</td>
      <td colspan="2">Above</td>
    </tr>
    <tr>
      <td>AM1</td>
      <td>F</td>
      <td>Size and rotation†</td>
      <td>Canonical only</td>
      <td colspan="2">Below (excluded)**</td>
    </tr>
    <tr>
      <td>AM2</td>
      <td>F</td>
      <td>Size and rotation†</td>
      <td>Canonical only</td>
      <td colspan="2">Below</td>
    </tr>
    <tr>
      <td>AM3</td>
      <td>F</td>
      <td>Size and rotation†</td>
      <td>Canonical only</td>
      <td colspan="2">Above</td>
    </tr>
    <tr>
      <td>AM4</td>
      <td>F</td>
      <td>Size and rotation†</td>
      <td>Canonical only</td>
      <td colspan="2">Above</td>
    </tr>
    <tr>
      <td>AM5</td>
      <td>F</td>
      <td colspan="4">Size and rotation†</td>
    </tr>
    <tr>
      <td>AM6</td>
      <td>F</td>
      <td colspan="4">Size and rotation†</td>
    </tr>
    <tr>
      <td>AM7</td>
      <td>F</td>
      <td colspan="4">Size and rotation†</td>
    </tr>
    <tr>
      <td>AM8</td>
      <td>F</td>
      <td colspan="4">Size and rotation†</td>
    </tr>
    <tr>
      <td>AN1</td>
      <td>F</td>
      <td colspan="4">Canonical only</td>
    </tr>
    <tr>
      <td>AN2</td>
      <td>F</td>
      <td>Canonical ony</td>
      <td colspan="3"></td>
    </tr>
    <tr>
      <td>AN3</td>
      <td>F</td>
      <td>Canonical only</td>
      <td colspan="3"></td>
    </tr>
    <tr>
      <td>AN4</td>
      <td>F</td>
      <td>Canonical only</td>
      <td colspan="3"></td>
    </tr>
    <tr>
      <td>AN5</td>
      <td>F</td>
      <td>Canonical only</td>
      <td colspan="3"></td>
    </tr>
    <tr>
      <td>AN6</td>
      <td>F</td>
      <td>Canonical only</td>
      <td colspan="3"></td>
    </tr>
    <tr>
      <td>AN7</td>
      <td>F</td>
      <td>Canonical only</td>
      <td colspan="3"></td>
    </tr>
    <tr>
      <td>AN8</td>
      <td>F</td>
      <td>Canonical only</td>
      <td colspan="3"></td>
    </tr>
  </tbody>
</table>

_*Failed to learn task.†Not included in initial learning experiment.‡Above chance for near-transparent stimuli.§Failed to learn previous stimuli.¶Not enough practice trials with reaction time restrictions.**Failed to learn stimuli with reaction time restrictions._

#### Behavioral training boxes

Rats were trained in high-throughput behavioral training rigs, each made up of four vertically stacked behavioral training boxes. In order to enter the behavioral training boxes, the animals were first individually transferred from their home cages to temporary plastic housing cages that would slip into the behavioral training boxes and snap into place. Each plastic cage had a porthole in front where the animals could stick out their head. In front of the animal in the behavior boxes were three easily accessible stainless steel lickports electrically coupled to capacitive sensors, and a computer monitor (Dell P190S, Round Rock, TX, USA; Samsung 943-BT, Seoul, South Korea) at approximately 40° visual angle from the rats’ location. The three sensors were arranged in a straight horizontal line approximately a centimeter apart and at mouth-height for the rats. The two side ports (L/R) were connected to syringe pumps (New Era Pump Systems, Inc NE-500, Farmingdale, NY, USA) that would automatically dispense water upon a correct trial. The center port was connected to a syringe that was used to manually dispense water during the initial phases of training (see below). Each behavior box was equipped with a computer (Apple Macmini 6,1 running OsX 10.9.5 [13F34] or Macmini 7.1 running OSX El Capitan 10.11.13, Cupertino, CA, USA) running MWorks, an open source software for running real-time behavioral experiments (MWorks 0.5.dev [d7c9069] or 0.6 [c186e7], The MWorks Project https://mworks.github.io/). The capacitive sensors (Phidget Touch Sensor P/N 1129_1, Calgary, Alberta, Canada) were controlled by a microcontroller (Phidget Interface Kit 8/8/8P/N 1018_2) that was connected via USB to the computer. The syringe pumps were connected to the computer via an RS232 adapter (Startech RS-232/422/485 Serial over IP Ethernet Device Server, Lockbourne, OH, USA). To allow the experimenter visual access to the rats’ behavior, each box was, in addition, illuminated with red LEDs, not visible to the rats.

#### Habituation

Long-Evans rats (Charles River Laboratories, Wilmington, MA, USA) of about 250 g were allowed to acclimate to the laboratory environment upon arrival for about a week. After acclimation, they were habituated to humans for 1 or 2 days. The habituation procedure involved petting and transfer of the rats from their cage to the experimenter’s lap until the animals were comfortable with the handling. Once habituated to handling, the rats were introduced to the training environment. To allow the animals to get used to the training plastic cages, the feedback sounds generated by the behavior rigs, and to become comfortable in the behavior training room, they were transferred to the temporary plastic cages used in our high-throughput behavioral training rigs and kept in the training room for the duration of a training session undergone by a set of trained animals. This procedure was repeated after water deprivation, and during the training session undergone by the trained animals, the new animals were taught to poke their head out of a porthole available in each plastic cage to receive a water reward from a handheld syringe connected to a lickport identical to the ones in the behavior training boxes in the training rigs. Once the animals reliably stuck their head out of the porthole (1 or 2 days) and accessed water from the syringe, they were moved into the behavior boxes.

#### Early shaping

On their first day in the behavior boxes, rats were individually tutored as follows: Water reward was manually dispensed from the center lickport which is normally used to initiate a trial. When the animal licked the center lickport, a trial began. After a 500 ms tone period, one of two visual objects (stimulus pair 1) appeared on the screen (large front view, degree of visual angle 40°) chosen pseudo-randomly (three randomly consecutive presentations of one stimulus resulted in a subsequent presentation of the other stimulus). This appearance was followed by a 350 ms minimum reaction time that was instituted to promote visual processing of the stimuli. If the animal licked one of the side (L/R) lickports during this time, then the trial was aborted, there would be a minimum intertrial time (1300 ms), and the process would begin again.

At the time of stimulus presentation, a free water reward was dispensed from the correct side (L/R) lickport. If the animals licked the correct side lickport within the allotted amount of time (3500 ms) then an additional reward was automatically dispensed from that port. This portion of training was meant to begin teaching the animals the task mechanics, that is to first lick the center port, and then one of the two side ports.

After the rats were sufficiently engaged with the lickports and began self-initiating trials by licking the center lickport (usually 1 to several days, determined by experimenter) no more water was dispensed manually through the center lickport, but the free water rewards from the side lickports were still given. Once the rats were self-initiating enough trials without manual rewards from the center lickport (>200 per session), the free reward condition was stopped, and only correct responses were rewarded.

#### Training

Data collection for this study began once the rats had demonstrated proficiency of the task mechanics (as described above). The training curriculum followed was similar to that by Zoccolan et al., 2009. Rats performed the task for about 2 hr daily. Initially, the rats were only presented with large front views (40° visual angle, 0° of rotation) of the two stimuli (stimulus pair 1). Once the rats reached a performance level of ≥70% with these views, the stimuli decreased in size to 15° visual angle in a staircased fashion with steps of 2.5° visual angle. Once the rats reached 15° visual angle, rotations of the stimuli to the left or right were staircased in steps of 5° at a constant size of 30° visual angle. Once the rats reached ±60° of rotation, they were considered to have completed training and were presented with random transformations of the stimuli at different sizes (15°–40° visual angle, step = 15°; 0° of rotation) or different rotations (-60° to +60° of rotation, step = 15°; 30° visual angle). After this point, 10 additional training sessions were collected to allow the animals’ performance to stabilize with this expanded stimulus set.

During training, there was a bias correction that tracked the animals’ tendency to be biased to one side. If biased, stimuli mapped to the unbiased side were presented for a maximum of three consecutive trials. For example, if the bias correction detected an animal was biased to the right, the left-mapped stimulus would appear three trials at a time in a non-random fashion and the animals’ performance would drop from 50% to 25%, reducing the advantageousness of a biased strategy dramatically. If the animals continued to exhibit bias after one or two sessions of bias correction, then the limit was pushed to five consecutive trials. Once the bias disappeared, stimulus presentation resumed in a pseudo-random fashion.

The left/right mapping of the stimuli to lickports was counterbalanced across animals, ruling out any effects related left/right stimulus-independent biases, or left/right-independent stimulus bias across animals.

#### Training regime comparison

Although object recognition is supposed to be a fairly automatic process (Cox, 2014), it is possible that the 14 possible presentations of each stimulus of stimulus pair 1 (6 sizes at constant rotation, and 8 rotations at constant size) varied in difficulty. To rule out any possible difficulty effects during training and at asymptotic performance, We trained $n=8$ different rats to asymptotic performance on the task but only on large, front views of the visual objects (Figure 2—figure supplement 1a). We compared the learning and asymptotic performance of the ‘size and rotation’ cohort and the ‘canonical only’ cohort across a wide range of behavioral measures. During learning, animals in both regimes followed similar learning trajectories in speed-accuracy space (Figure 2—figure supplement 1b), and clustered around the OPC at asymptotic performance (Figure 2—figure supplement 1c). Comparisons of accuracy, reaction time, and fraction maximum instantaneous reward rate trajectories during learning and at averages asymptotic performance revealed no detectable differences (Figure 2—figure supplement 1d—f). Total trials per session, and voluntary intertrial intervals after error trials did show slightly varied trajectories during learning, though there were no differences in their means after learning (Figure 2—figure supplement 1g, h). The difference in total trials per session could be unrelated to the difference in training regimes. The difference in voluntary intertrial intervals, however, could be related to the introduction of different sizes and rotations: a sudden spike in this metric is seen about halfway through normalized sessions and decays over time. If this is the case, it is a curious result that rats choose to display their purported ‘surprise’ in between trials, and not during trials, as we found no difference in the reaction time trajectories. Both training regimes had overlapping fraction trials ignored metrics during learning, with a sharp decrease after the start, and a small significant difference in their number at asymptotic performance (Figure 2—figure supplement 1i). We point out the fact that we do not consider voluntary intertrial intervals nor ignored trials in our analysis, so the differences between the regimes do not affect our conclusions. Overall, these results suggest that there is not a measurable or relevant difficulty effect based on our training regime with a variety of stimulus presentations.

#### Stimulus learnability experiment

Transparent stimuli. In order to assess how animals behaved in a scenario with non-existent learning potential, a subset of already well-trained animals were presented with transparent ($n=5$, alpha = 0) or near-transparent ($n=5$, alpha = 0.1) versions of the familiar stimulus pair 1 for a duration of 11 sessions. Before these sessions, 4 sessions with stimulus pair 1 at full opacity (alpha = 1) were conducted to ensure animals could perform the task adequately before the manipulation. We predicted that the near-transparent condition would segregate animals into two groups, those that could perform the task and those that could not, based on each individual’s perceptual ability. The animals in the near-transparent condition that remained around chance performance ($n=3$, rat AK2, AK9, and AK10) were grouped with the animals from the transparent condition, while those that performed well above chance ($n=2$, rat AK5 and AK12) were excluded.

Reaction times were predicted to decrease during the course of the experiment, so to measure the change most effectively, the minimum reaction time requirement of 350 ms was removed. However, removing the requirement could lead to reduced reaction times regardless of the presented stimuli. To be able to measure whether the transparent stimuli led to a significant difference in reaction times compared to visible stimuli, we ran sessions with visible stimuli with no reaction time requirement for the same animals and compared these reaction times with those from the transparent condition. We found that the aggregate reaction time distributions were significantly different (Figure 6—figure supplement 1a). A comparison of vincentized reaction times revealed that there was a significant difference in the fastest reaction time decile (Figure 6—figure supplement 1b), confirming that reaction times decreased significantly during presentation of transparent stimuli.

New visible stimuli. In order to assess how animals behaved in a scenario with high learning potential, a subset ($n=16$) of already well-trained animals on stimulus pair 1 were presented with a never before seen stimulus pair (stimulus pair 2) for a duration of 13 sessions. Before these sessions, 5 sessions with the familiar stimulus pair 1 were recorded immediately preceding the stimulus pair 2 sessions in order to compare performance and reaction time after the manipulation for every animal. Previous pilot experiments showed that the animals immediately assigned a left/right mapping to the new stimuli based on presumed similarity to previously trained stimulus pair, so in order to enforce learning, the left/right mapping contrary to that predicted by the animals in the pilot tests was chosen. Because of this, animals typically began with an accuracy below 50%, as they first had to undergo reversal learning for their initial mapping assumptions. Because the goal of this experiment was to measure effects during learning and not demonstrate invariant object recognition, the new stimuli were presented in large front views only (visual angle = 40°, rotation = 0°).

### Behavioral data analysis

#### Software

Behavioral psychophysical data was recorded using the open-source MWorks 0.5.1 and 0.6 software (https://mworks.github.io/downloads/). The data were analyzed using Python 2.7 with the pymworks extension. We employed the hierarchical estimation of the DDM in python (HDDM) package for DDM fits (Wiecki et al., 2013). To measure stimulus-independent psychophysical strategies such as bias and perseverance, we employed PsyTrack, a generalized linear model package for fitting dynamic psychophysical models to behavioral data (Roy et al., 2021) in conjunction with Python 3.8.

#### DDM fit

In order to verify that our behavioral data could be modeled as a drift-diffusion process, the data were fit with an HDDM (Wiecki et al., 2013), permitting subsequent analysis (such as comparison to the OPC) based on the assumption of a drift-diffusion process. To verify that a DDM was appropriate for our data, we fit a simple DDM to 10 asymptotic sessions after learning stimulus pair 1 for $n=26$ subjects (Figure 1—figure supplement 3). In order to assess parameter changes across learning, we fit DDMs to the stimulus pair 1 experiment and the stimulus pair 2 experiment where the learning epochs were treated as conditions in each experiment. This allowed us to hold some parameters constant while conditioning others on learning. We fit both simple DDMs and DDMs with drift rate variability to the two experiments, allowing drift rate, threshold, and drift rate variability to vary with learning epoch. In particular, we fit three broad types of models: (1) simple DDMs (Figure 4—figure supplement 2), (2) DDMs + fixed drift rate variability (Figure 4—figure supplement 3), and (3) DDMs + drift rate variability that varied freely with learning epoch (Figure 4—figure supplement 4). For each of the types of models we held drift constant, threshold constant, or allowed both to vary with learning. The best fits, as determined by the deviance information criterion (DIC), came from models where we allowed both drift and threshold to vary with learning; the addition of drift rate variability did not appear to improve model fits (Figure 4—figure supplement 1). For both learning experiments, drift rates increased and thresholds decreased by the end of learning, in agreement with previous findings (Ditterich, 2006; Ratcliff et al., 2006; Dutilh et al., 2009; Balci et al., 2011b; Liu and Watanabe, 2012; Zhang and Rowe, 2014). In addition, for the transparent stimuli experiment we fit a DDM that allowed drift rate, threshold, drift rate variability, and T0 to vary with learning phase in order to observe the changes in drift rate and threshold (Figure 6—figure supplement 3).

#### PsyTrack fit

In order to estimate stimulus-independent psychophysical strategies in the transparent stimulus experiment (Figure 6—figure supplement 4), we used PsyTrack to fit a generalized linear model to our behavioral data (Roy et al., 2021). The model assigns weights to user-determined input variables to explain the output variable. The output variable consists of a vector for left/right choices on every trial for an individual subject, where left = 0 and right = 1 (or 1 and 2). PsyTrack automatically calculates weights on bias, with a positive weight indicating a rightward bias, and a negative weight indicating a leftward bias. We fit the model by providing it with three explanatory input variables: stimulus, perseverance, and win-stay/lose-switch. For the input variables, the left/right coding differed from that for the output variable as per the model documentation (left = -1, right = +1). The stimulus variable indicated the stimulus that appeared on that trial (stimulus A = -1, stimulus B = +1). However, the left/right mapping of these stimuli was counterbalanced across subjects, so depending on the mapping, subjects could have a strong positive or negative weight, both indicating the stimuli explained choices. The perseverance variable indicated the left/right location of the subject’s choice on the previous trial. The win-stay/lose-switch variable indicated the location of the correct choice on the previous trial. For both perseverance and win-stay/lose-switch, positive weights indicate the predicted presence of perseverance and win-stay/lose-switch rather than left/right information.

#### Behavioral metrics

Error rate ($E⁢R$) was calculated by dividing the number of error trials by the number of total trials (error + correct) within a given window of trials in a full behavioral training session. Accuracy was calculated as $1-E⁢R$.

$$
ER=\frac{errortrials}{totaltrials}
$$



$$
accuracy=1−ER
$$

Reaction time ($R⁢T$) for one trial was measured by subtracting the time of the first lick on a response lickport from the stimulus onset time on the computer monitor. Mean $R⁢T$ was calculated by averaging reaction times across trials within a given window of trials or the trials in a full behavioral training session.

$$
RT=\frac{1}{n}\sumtrial i=1trial nRT_{i}
$$

Vincentized reaction time is one method to report aggregate reaction time data meant to preserve individual distribution shape and be less sensitive to outliers in the group distribution (Ratcliff, 1979, Blokland, 1998), although some scientists have argued parametric fitting (with an ex-Gaussian distribution, for example) and parameter averaging across subjects outperforms Vincentizing as sample size increases (Rouder and Speckman, 2004; Whelan, 2008). Each subject’s reaction time distribution is divided into quantiles (e.g. deciles; similar to percentile, but between 0 and 1), and then the quantiles across subjects are averaged.

Decision time ($D⁢T$) for one trial was measured by subtracting the non-decision time $T_{0}$ (see Estimating $T_{0}$) from $R⁢T$. Mean $D⁢T$ was calculated by subtracting $T_{0}$ from the mean $R⁢T$ across trials within a given window of trials or the trials in a full behavioral training session.

$$
DT=RT−T_{0}
$$

Post-error and correct non-decision task engagement times ($D_{e⁢r⁢r}$, $D_{c⁢o⁢r⁢r}$) are defined (for notational simplicity) as the sum of non-decision time T0 and the experimentally determined response-to-stimulus times after error $D~_{e⁢r⁢r}$ and correct trials $D~_{c⁢o⁢r⁢r}$. Please see Determining $D~_{e⁢r⁢r}$ and $D~_{c⁢o⁢r⁢r}$ for how we determined these experimental variables.

$$
D_{err}=D~_{err}+T_{0}
$$



$$
D_{corr}=D~_{corr}+T_{0}
$$

Mean normalized decision time ($D⁢T/D_{e⁢r⁢r}$) was measured by dividing mean $D⁢T$ by $D_{e⁢r⁢r}$, the sum of the non-decision time T0 and $D~_{e⁢r⁢r}$, the mean non-decision task engagement time in an error trial (see $D_{e⁢r⁢r}$, $D_{c⁢o⁢r⁢r}$).

Mean difference in mean reaction time ($Δ⁢R⁢T$) was calculated by subtracting the mean reaction time of a number of baseline sessions from the mean reaction time of an experimental session. A positive difference indicates an increase over baseline mean reaction time. The mean of the two immediately preceding sessions with stimulus pair 1 were subtracted from the mean reaction time of every session with stimulus pair 2 or transparent stimuli for every animal individually (Figure 6d and e). These differences were then averaged to get a mean difference in mean reaction time $Δ⁢R⁢T$.

Mean instantaneous reward rate ($i⁢R⁢R$) (regularly referred to as just reward rate, $R⁢R$) is defined as mean accuracy per mean time per trial (Gold and Shadlen, 2002):

$$
iRR=\frac{meanaccuracy}{meantimepertrial}.
$$

We define the average non-decision task engagement time per trial,

$$
D_{tot}=(1−ER)D_{corr}+ER⋅D_{err}.
$$

The mean instantaneous reward rate is then (see Equation A26 in Bogacz et al., 2006)

$$
iRR=\frac{1−ER}{DT+D_{tot}}
$$

N.B. Because our study hinges on the important difference between present, future and cumulative rewards and tracks changes in $E⁢R$ and $D⁢T$ over learning, we write what is traditionally referred to as reward rate $R⁢R$ as instantaneous reward rate $i⁢R⁢R$ to emphasize these differences. Because $E⁢R$ and $D⁢T$ can change throughout learning, reward rate as traditionally defined only captures an ‘instant’ in a learning trajectory.

Mean total correct trials is a model-free measure of the reward attained by the animals within a given window of trials. Every correct response yields an identical water reward, hence, reward can be counted by counting correct responses across trials. For one subject a∈ [1, 2, 3,…, k], total correct trials at trial n are the sum of correct trials up to trial n:

$$
c_{n}^{a}=\sumtrial i=1trial no_{i}^{a}
$$

where $o_{i}^{a}$ is an element in a vector $o^{a}$ containing the outcomes of those trials $o^{a}=[o_{1}^{a},o_{2}^{a},o_{3}^{a},…,o_{n}^{a}]$. For correct and error responses  $o_{n}^{a}$ = 1 and 0 respectively (e.g.$o_{n}^{a}$ = [0, 0, 1, 1, 0, …, 1]).

Mean total correct trials up to trial n is calculated by taking the average of total correct trials across all animals k up to trial n.

$$
⟨c_{n}⟩=\frac{1}{k}\sumtrial i=1trial nc_{i}^{1}+c_{i}^{2}+c_{i}^{3}+...+c_{i}^{k}
$$

Mean cumulative reward is a measure of the reward attained by the animals within a given window of trials. To calculate this quantity, a moving average of $R⁢T$ and accuracy for a given window size are first calculated for every animal individually. To avoid averaging artifacts, only values a full window length from the beginning are considered. Given these moving averages, $i⁢R⁢R$ is then calculated for every animal and subsequently averaged across animals to get a moving average of mean reward rate. To calculate the mean cumulative reward, a numerical integral over a particular task time, such as task engagement time (see Measuring task time), is then calculated using the composite trapezoidal rule.

SNR is a measure of an agent’s perceptual ability in a discrimination task. Given an animal’s particular $E⁢R$ and $D⁢T$, we use an equation to infer its SNR $A¯$ deduced from standard DDM equations to infer its SNR (Equation 56 in Bogacz et al., 2006):

$$
A¯_{infer}=\frac{1−2ER}{2DT}log⁡\frac{1−ER}{ER}
$$

The SNR equation defines a U-shaped curve that increases as $ERs$ move away from 0.5. For cases early in learning where $ERs$ were below 0.5 because of potential initial biases, we assumed the inferred SNR was negative (meaning the animals had to unlearn the biases in order to learn, and thus had a monotonically increasing SNR during learning).

SNR performance frontier is a measure of an agent’s possible error rate and reaction time combinations based on their current perceptual ability. Because of the SAT, not all combinations of $E⁢R$ and $D⁢T$ are possible. Instead, performance is bounded by an agent’s SNR $A¯$ at any point in time, and their particular ($E⁢R$, $D⁢T$) combination will depend on their choice of threshold.

Given a fixed $D_{e⁢r⁢r}$ (as in the case of our experiment), this bound exists in the form of a performance frontier – the combination of all resultant $ERs$ and mean normalized $DTs$ possible given a fixed SNR $A¯$ and all possible thresholds $z¯$.

We can use $A¯_{infer}$ (Equation 24) to calculate its performance frontier for a range of thresholds $z¯\in$ [0, $∞$) with standard equations from the DDM:

$$
ER_{A¯_{infer}}=\frac{1}{1+e^{2z¯A¯_{infer}}}
$$



$$
DT_{A¯_{infer}}=z¯tanh⁡(z¯A¯_{infer})
$$

For every performance frontier there will be one unique ($E⁢R_{A¯_{infer}}$, $D⁢T_{A¯_{infer}}$) combination for which reward rate will be greatest, and it will lie on the OPC.

Fraction maximum instantaneous reward rate is a measure of distance to the OPC, that is, optimal performance. Given an animal’s $E⁢R$ and $D⁢T$, we inferred their SNR and calculated their performance frontier as described above. We then divided the animal’s reward rate by the maximum reward rate on their performance frontier, corresponding to the point on the OPC they could have attained given their inferred SNR $A¯_{infer}$:

$$
fraction max iRR=\frac{iRR_{ER, DT}}{maxiRR_{A¯_{infer}}}
$$

Maximum instantaneous reward rate opportunity cost, like fraction maximum instantaneous reward rate, is also measure of distance to the OPC, that is, optimal performance, but it emphasizes the reward rate fraction given up by the subject given its current $E⁢R$ and $D⁢T$ combination along its SNR performance frontier. It is simply:

$$
max iRR opportunity cost=1−fraction max iRR
$$

Mean post-error slowing is a metric to account for the potential policy of learning by slowing down after error trials. In order to quantify the amount of post-error slowing in a particular subject, the subject’s reaction times in a session are segregated into correct trials following an error, and correct trials following a correct choice, and separately averaged. The difference between these indicates the degree of post-error slowing present in that subject during that session.

$$
post-error slowing (PES)=⟨RT_{post-error correct trials}⟩−⟨RT_{post-correct correct trials}⟩
$$

The mean post-error slowing for one session is thus the mean of this quantity across all subjects k.

$$
⟨PES⟩=\frac{PES^{1}+PES^{2}+PES^{3}+...+PES^{k}}{k}
$$

Left/right bias measures the extent to which a subject is biased to the left or right lickport regardless of the stimulus presented. For every individual, left or right choices for every trial are coded as a binary vector (left = 0, right = 1). The correct response side is also coded as a binary vector. Bias is calculated by taking the difference of these vectors. A Gaussian filter is then applied to smooth the bias vector over time, with negative numbers reflecting a left bias and positive numbers reflecting a right bias.

#### Computing error

Within-subject session errors (e.g. Figure 1d) for accuracy and reaction times were calculated by bootstrapping trial outcomes and reaction times for each session. We calculated a bootstrapped standard error of the mean by taking the standard deviation of the distribution of means from the bootstrapped samples. A 95% confidence interval can be calculated from the distribution of means as well.

Across-subject session errors (e.g. Figure 6d) were computed by calculating the standard error of the mean of individual animal session means.

Across-subject sliding window errors (e.g. Figure 6b; Figure 7b) were calculated by averaging trials over a sliding window (e.g. 200 trials) for each animal first, then taking the standard error of the mean of each step across animals. Alternatively, the average could be taken across a quantile (e.g. first decile, second decile, etc.), and then the standard error of the mean of each quantile across animals was computed.

#### Measuring task time

Trials are the smallest unit of behavioral measure in the task and are defined by one stimulus presentation accompanied by one outcome (correct, error) and one reaction time.

Sessions are composed of as many trials as an animal chooses to complete within a set window of wall clock time, typically around 2 hr once daily. An error rate (fraction of error trials over total trials for the session) and a mean reaction time can be calculated for a session.

Normalized sessions are a group of sessions (e.g. 1, 2, 3, …, 10) where a particular session’s normalized index corresponds to its index divided by the total number of sessions in the group (e.g. 0.1, 0.2, 0.3, …, 1.0). Because animals may take different numbers of sessions to learn to criterion, a normalized index for sessions allows better comparison of psychophysical measurements throughout learning.

Stimulus viewing time measures the time that the animals are viewing the stimulus, defined as the sum of all reaction times up to trial n as:

$$
stimulus viewing time=\sumtrial i=1trial nRT_{i}
$$



$$
task engagement time=\sumtrial i=1trial nRT_{i}+n_{corr}D~_{corr}+n_{err}D~_{err}
$$

The sum of reaction times up to trial n plus the sum of  $D~_{e⁢r⁢r}$ = 3136 ms and  $D~_{c⁢o⁢r⁢r}$ = 6370 ms, the mandatory post-error and post-correct response-to-stimulus intervals, proportional to the number of error and correct trials (n=ncorr + nnerr).

#### Statistical analyses

Figure 1d: We wished to test whether the mean fraction maximum reward rate of our subjects over the 10 sessions after having completed training were significantly different from optimal performance. A Shapiro-Wilk test failed to reject (p<0.05) a null hypothesis for normality for 18/26 subjects, with the following p-values (from left to right): (0.8162, 0.1580, 0.3746, 0.6985, 0.0025, 0.0467, 0.0040, 0.6522, 0.0109, 0.1625, 1.8178e-05, 0.0901, 0.7606, 0.0295, 0.0009, 0.2483, 0.5627, 0.0050, 0.4464, 0.6839, 0.5953, 0.0140, 0.1820, 0.1747, 0.6385, 0.2304). Thus, we conducted a one-sided Wilcoxon signed-rank test on our sample against 0.99, testing for the evidence that each subject’s mean fraction max reward rate was greater than 99% of the maximum (p<0.05), and obtained the following p-values (from left to right): (0.0025, 0.0025, 0.0025, 0.1013, 0.2223, 0.0063, 0.0047, 0.0025, 0.0025, 0.0025, 0.0025, 0.0571, 0.6768, 0.0047, 0.7125, 0.0372, 0.8794, 0.4797, 0.7125, 0.8987, 0.0372, 0.0109, 0.9975, 0.9766, 0.9917, 0.9975).

Figure 5b: We wished to test the difference in mean $R⁢T$ between two randomly chosen groups of animals before and after an $R⁢T$ restriction to assess the effectiveness of the restriction. A Shapiro-Wilk test did not support an assumption of normality for the ‘below’ group in either condition resulting in the following (W statistic, p-value) for the pre-$R⁢T$ restriction ‘above’ and ‘below’ groups and post-RT restriction ‘above’ and ‘below’ groups: (0.9073, 0.3777), (0.6806, 0.0059), (0.8976, 0.3168), (0.6583, 0.0033). Hence, we conducted a Wilcoxon rank-sum test for the pre- and post-$R⁢T$ restriction groups and found the pre-$R⁢T$ restriction group was not significant (p=0.570) while the post-$R⁢T$ restriction group was (p=0.007), indicating the two groups were not significantly different before the RT restriction, but became significantly different after the restriction.

Figure 5d: We wished to test the difference in accuracy between the ‘above’ and ‘below’ groups for every session of stimulus pair 3. A Shapiro-Wilk test failed to reject the assumption of normality (p<0.05) for any session from either condition (except session 4, ‘above’, which could be expected given there were 16 tests), with the following (W statistic, p-value) for [session: ‘above’, ‘below’] by session: [1: (0.9340, 0.6240),(0.8959, 0.3068)], [2: (0.9381, 0.6522), (0.8460, 0.1130)], [3: (0.9631, 0.8291), (0.9058, 0.3676)], [4: (0.7608, 0.0374), (0.9728, 0.9177)], [5: (0.8921, 0.3680), (0.9779, 0.9486)], [6: (0.7813, 0.0565), (0.9702, 0.9002)], [7: (0.8942, 0.3786), (0.9711, 0.9062)], [8: (0.7848, 0.0605), (0.9611, 0.8280)].

A Levene test failed to reject the assumption of equal variances for every pair of sessions except the first (statistic, p-value): (6.3263, 0.0306), (2.2780, 0.1621), (1.2221, 0.2948), (0.8570, 0.3764), (2.7979, 0.1253), (0.7364, 0.4109), (0.0871, 0.7739), (0.0088, 0.9269).

Hence, we performed a two-sample independent t-test for every session with the following p-values: (0.4014, 0.04064, 0.0057, 0.0038, 0.0011, 0.0038, 0.0006, 6.3658e-05).

We also wished to test the difference between the slopes of linear fits to the accuracy curves for both conditions. A Shapiro-Wilk test failed to reject the assumption of normality (p<0.05) for either condition, with the following (W statistic, p-value) for ‘above’ and ‘below’: (0.8964, 0.3095), (0.8794, 0.3065). A Levene test failed to reject the assumption of equal variances (p<0.05) for each condition (statistic, p-value): (0.2141, 0.6535). Hence, we performed a two-sample independent t-test and found a significant difference (p=0.0027).

Figure 6d: We wished to test whether the animals had significantly changed their session mean $RTs$ with respect to their individual previous baseline $RTs$ (paired samples). To do this, we conducted a permutation test for every session with the new visible stimuli (stimulus pair 2) or the transparent stimuli. For 1000 repetitions, we randomly assigned labels to the experimental or baseline $RTs$ and then averaged the paired differences. The p-value for a particular session was the fraction of instances where the average permutation difference was more extreme than the actual experimental difference. For sessions with stimulus pair 2, the p-values from the permutation test were: (0.0034, 0.0069, 0.0165, 0.0071, 0.0291, 0.0347, 0.06, 0.0946, 0.3948, 0.244, 0.244, 0.4497, 0.3437). For sessions with transparent stimuli (plus rats AK2, AK9, and AK10 from the near-transparent stimuli), the p-values from the permutation were (0.0859375, 0.44921875, 0.15625, 0.03125, 0.02734375, 0.015625, 0.26953125, 0.02734375, 0.03125, 0.01953125, 0.0546875). To investigate whether the animals’ significantly slowed down their mean $RTs$ compared to baseline during the first session of transparent stimuli, we divided $RTs$ in the first session in half and ran a permutation test on each half with the following p-values: (0.0390625, 0.2890625).

Figure 6e: In order to test the correlation between the initial change in $R⁢T$ and the initial change in SNR for stimulus pair 2, we ran a standard linear regression on the average per subject for each of these variables for the first three sessions of stimulus pair 2 with  $R^{2}$ = 0.38 and p-value = 0.01.

Figure 2—figure supplement 1d—i: Statistical significance of differences in means between the two training regimes for a variety of psychophysical measures was determined by a Wilcoxon rank-sum test with p<0.05. The p-values were: (d) accuracy: 0.21, (e) reaction time: 0.81, (f) fraction max $i⁢R⁢R$: 0.22, (g) total trial number: 0.46, (h): voluntary intertrial interval after error: 0.75, (i) fraction trials ignored: 0.03.

Figure 4—figure supplement 2: Statistical significance for mean parameters was calculated by taking the difference between the posterior distributions and using the proportion of the difference distribution that overlapped with 0 as the p-value. For individuals’ parameters, p-values were determined via a Wilcoxon signed-rank test. The p-values were: (a) drift mean:<1e-4, drift individuals:<1e-4; (b) threshold mean: 0.0012, threshold individuals: 0.0008; (c) drift mean: <1e-4, drift individuals: <1e-4, threshold mean: 0.0298, threshold individuals: 0.0585; (d) drift mean: (baseline versus start learn: <1e-4, baseline versus after learn: 0.0378, start versus after learn: <1e-4), drift individuals: (baseline versus start learn: 0.0004, baseline versus after learn: 0.0703, start versus after learn: 0.0004); (e) threshold mean: (baseline versus start learn: 0.1100, baseline versus after learn: 0.3546, start versus after learn: 0.1904), threshold individuals: (baseline versus start learn: 0.0045, baseline versus after learn: 0.4380, start versus after learn: 0.1627); (f) drift mean: (baseline versus start learn: <1e-4, baseline versus after learn: 0.0616, start versus after learn: <1e-4), drift individuals: (baseline versus start learn: 0.0004, baseline versus after learn: 0.1089, start versus after learn: 0.0004), threshold mean: (baseline versus start learn: 0.2546, baseline versus after learn: 0.4614, start versus after learn: 0.2816), threshold individuals: (baseline versus start learn: 0.0200, baseline versus after learn: 0.7174, start versus after learn: 0.1089).

Figure 4—figure supplement 3: Statistical significance was determined as for Figure 4—figure supplement 2. The p-values were: (a) drift mean: <1e-4, drift individuals: <1e-4; (b) threshold mean: 0.0036, threshold individuals: 0.0013; (c) drift mean: <1e-4, drift individuals: <1e-4, threshold mean: 0.0314, threshold individuals: 0.0585; (d) drift mean: (baseline versus start learn: <1e-4, baseline versus after learn: 0.0428, start versus after learn: <1e-4), drift individuals: (baseline versus start learn: 0.0004, baseline versus after learn: 0.0703, start versus after learn: 0.0004); (e) threshold mean: (baseline versus start learn: 0.0866, baseline versus after learn: 0.4192, start versus after learn: 0.1252), threshold individuals: (baseline versus start learn: 0.0038, baseline versus after learn: 0.5349, start versus after learn: 0.1089); (f) drift mean: (baseline versus start learn: <1e-4, baseline versus after learn: 0.0618, start versus after learn: <1e-4), drift individuals: (baseline versus start learn: 0.0004, baseline versus after learn: 0.0980, start versus after learn: 0.0004), threshold mean: (baseline versus start learn: 0.2436, baseline versus after learn: 0.4596, start versus after learn: 0.2860), threshold individuals: (baseline versus start learn: 0.0200, baseline versus after learn: 0.7174, start versus after learn: 0.1089).

Figure 4—figure supplement 4: Statistical significance was determined as for Figure 4—figure supplement 2. The p-values were: (a) drift mean: <1e-4, drift individuals: <1e-4, drift variability: <1e-4; (b) threshold mean: 0.0036, threshold individuals:< 1e-4, drift variability: <1e-4; (c) drift mean: <1e-4, drift individuals: <1e-4, threshold mean: 0.0696, threshold individuals: 0.1587, drift variability: <1e-4; (d) drift mean: (baseline versus start learn: <1e-4, baseline versus after learn: 0.0422, start versus after learn: <1e-4), drift individuals: (baseline versus start learn: 0.0004, baseline versus after learn: 0.0557, start versus after learn: 0.0004), drift variability: (baseline versus start learn: 0.7940, baseline versus after learn: 0.8104, start versus after learn: 0.4564); (e) threshold mean: (baseline versus start learn: <1e-4, baseline versus after learn: 0.4188, start versus after learn: 0.0002), threshold individuals: (baseline versus start learn: 0.0004, baseline versus after learn: 0.5014, start versus after learn: 0.0004), drift variability: (baseline versus start learn: <1e-4, baseline versus after learn: 0.4442, start versus after learn: <1e-4); (f) drift mean: (baseline versus start learn:<1e-4, baseline versus after learn: 0.0596, start versus after learn: <1e-4), drift individuals: (baseline versus start learn: 0.0004, baseline versus after learn: 0.0980, start versus after learn: 0.0004), threshold mean: (baseline versus start learn: 0.2474, baseline versus after learn: 0.4702, start versus after learn: 0.2652), threshold individuals: (baseline versus start learn: 0.0200, baseline versus after learn: 0.7174, start versus after learn: 0.1089), drift variability: (baseline versus start learn: 0.2392, baseline versus after learn: 0.5294, start versus after learn: 0.2132).

Figure 6—figure supplement 1a, b: We tested for a difference in the aggregate reaction time distributions of a transparent stimuli condition in the first two and last two sessions ($n=8$ subjects), and a no minimum reaction time condition with known stimuli ($n=8$ subjects) via a two-sample Kolmogorov-Smirnov test and found a p-value of <1e-4 for both comparisons.

Figure 6—figure supplement 3: Statistical significance was determined as for Figure 4—figure supplement 2. The p-values were: (a) drift mean: (visible versus start transparent: 0.0002, visible versus end transparent: <1e-4, start versus end transparent: 0.3180), drift individuals: (visible versus start transparent: 0.0117, visible versus end transparent: 0.0117, start versus end transparent: 0.5754), threshold mean: (visible versus start transparent: 0.1362, visible versus end transparent: 0.0094, start versus end transparent: 0.0658), threshold individuals: (visible versus start transparent: 0.0499, visible versus end transparent: 0.0173, start versus end transparent: 0.0173), drift variability: (visible versus start transparent: 0.1494, visible versus end transparent: 0.1614, start versus end transparent: 0.5032), T0 mean: (visible versus start transparent: 0.0068, visible versus end transparent: 0.0194, start versus end transparent: 0.6106), T0 individuals: (visible versus start transparent: 0.0117, visible versus end transparent: 0.0117, start versus end transparent: 0.0929).

Figure 6—figure supplement 5b, d: We tested for a difference in mean post-error slowing between the first two sessions and last two sessions of training for each animal for stimulus pair 1 (b) or the last two sessions of stimulus pair 1 and the first two sessions of stimulus pair 2 (d) via a Wilcoxon-signed rank test. The p-values were (b) 0.585 and (d) 0.255.

#### Evaluation of optimality

Under the assumptions of a simple drift-diffusion process, the OPC defines a set of optimal threshold-to-drift ratios with corresponding decision times and error rates for which an agent maximizes instantaneous reward rate (Bogacz et al., 2006). Decision times are scaled by the particular task timing as mean normalized decision time: $D⁢T/D_{e⁢r⁢r}$. The OPC is parameter free and can thus be used to compare performance across tasks, conditions, and individuals. An optimal agent will lie on different points on the OPC depending on differences in task timing ($D_{e⁢r⁢r}$) and stimulus difficulty (SNR). Assuming constant task timing, the SNR will determine different positions along the OPC for an optimal agent. For $DT>0$ and $0<ER<0.5$, the OPC is defined as:

$$
\frac{DT}{D_{err}}=[\frac{1}{ERlog⁡\frac{1−ER}{ER}}−\frac{1}{1−2ER}]^{−1}
$$

and exists in speed-accuracy space, defined by $D⁢T/D_{e⁢r⁢r}$ and ER. Given an estimate of $D_{e⁢r⁢r}$, the $E⁢R$ and $D⁢T$ for any given animal can be compared to the optimal values defined by the OPC in speed-accuracy space.

Moreover, because $E⁢R$ should decrease with learning, learning trajectories for different subjects and models can also be compared to the OPC and to each other in speed-accuracy space.

Mean normalized decision time depends only on $D_{e⁢r⁢r}$.

For completeness, we include a derivation showing that the appropriate normalized decision time for the OPC depends only on $D_{e⁢r⁢r}$, not $D_{c⁢o⁢r⁢r}$. According to Gold and Shadlen, 2002, average reward rate is defined as:

$$
RR=\frac{average accuracy}{average time per trial}
$$

We can write the average reward rate as (see A26 from Bogacz et al., 2006),

$$
RR=\frac{1−ER}{DT+D_{corr}+ER(D_{err}−D_{corr})}.
$$

Optimal behavior is defined as maximizing reward rate with respect to the thresholds in the DDM. We thus rewrite $E⁢R$ and $D⁢T$ in terms of average threshold and average SNR,

$$
RR=\frac{1−\frac{1}{1+e^{2z¯A¯}}}{z¯tanh⁡(z¯A¯)+D_{corr}+\frac{1}{1+e^{2z¯A¯}}(D_{err}−D_{corr})}
$$



$$
=\frac{1}{z¯+D_{corr}+(D_{err}−z¯)e^{−2z¯A¯}}.
$$

Next to find the extremum, we take the derivative of $R⁢R$ with respect to the threshold and set it to zero,

$$
\frac{∂RR}{∂z¯}=−\frac{1+(−1−2A¯(D_{err}−z¯))e^{−2z¯A¯}}{(z¯+D_{corr}+(D_{err}−z¯)e^{−2z¯A¯})^{2}}
$$



$$
0=1−[1+2A¯(D_{err}−z¯)]e^{−2z¯A¯}
$$



$$
=\frac{1−2ER}{ER}−\frac{D_{err}}{DT}(1−2ER)log⁡\frac{1−ER}{ER}−log⁡\frac{1−ER}{ER}
$$

where in the final step we have rewritten $z¯$ and $A¯$ in terms of $E⁢R$ and $D⁢T$.

Rearranging to place $D⁢T$ on the left-hand side reveals an OPC where decision time is normalized by the post-error non-decision time $D_{e⁢r⁢r}$:

$$
\frac{DT}{D_{err}}=[\frac{1}{ERlog⁡\frac{1−ER}{ER}}−\frac{1}{1−2ER}]^{−1}
$$

Notably, the post-correct non-decision time $D_{c⁢o⁢r⁢r}$ is not part of the normalization. Intuitively, this is because post-correct delays are an unavoidable part of accruing reward and therefore do not influence the optimal policy.

#### Estimating T0

T0 is defined as the non-decision time component of a reaction time, comprising motor and perceptual processing time (Holmes and Cohen, 2014). It can be estimated by fitting a DDM to the psychophysical data. Because of the experimentally imposed minimum reaction time meant to ensure visual processing of the stimuli, however, our reaction time distributions were truncated at 350 ms, meaning a DDM fit estimate of T0 is likely to be an overestimate. To address this issue, we set out to determine possible boundaries for T0 and estimated it in a few ways, all of which did indeed fall between those boundaries (Figure 1—figure supplement 4e).

We found that after training, in the interval between 350 and 375 ms, nearly all of our animals had accuracy measurements above chance (Figure 1—figure supplement 4b), meaning that the minimum reaction time of 350 ms served as an upper bound to possible T0 values.

To determine a lower bound, we obtained measurements for the two components comprising T0: motor and initial perceptual processing times. To measure the minimum motor time required to complete a trial, we analyzed licking times across the different lickports. The latency from the last lick in the central port to the first lick in one of the two side ports peaked at around 80 ms (Figure 1—figure supplement 4c). In addition, the latency from one lick to the next lick at the same port at any of the lickports was also around 80 ms (data not shown). Because the latencies in lick times between lickports (requires movement of the head) and within the same lockport (does not require movement of the head) were about equal we concluded that the minimum motor time was determined by the limit on lick frequency, and not on a movement of the head redirecting the animal from the central port to one of the side ports. To measure the initial perceptual processing times, we looked to published latencies of visual stimuli traveling to higher visual areas in the rat. Published latencies reaching area TO (predicted to be after V1, LM, and LI in the putative ventral stream in the rat) were around 80 ms (Figure 1—figure supplement 4d; Vermaercke et al., 2014). Based on these measurements, we estimated a T0 lower bound of approximately 160 ms.

One worry is that our lower bound could potentially be too low, as it is only estimated indirectly. Recent work on the SAT in a low-level visual discrimination tasks in rats found that accuracy was highest at a reaction time of 218 ms (Kurylo et al., 2020). However, accuracy was still above chance for reaction times binned between 130 and 180 ms. In this task, reaction time was measured when an infrared beam was broken, which means we can assume there was no motor processing time. This leaves decision time, and initial perceptual processing time (part of T0) within the 130–180 ms duration. The complexity of solving a high-level visual task like ours and a low-level one will result in substantial differences in decision time, but should not in principle affect non-decision time. Considering a latency estimate of 80 ms based on physiological evidence (Vermaercke et al., 2014) can account for the initial perceptual processing component of T0 and gives an estimate T0=80 ms for this study.

Because a reaction time around T0 should not allow for any decision time, accuracy should be around 50%. To estimate T0 based on this observation, we extrapolated the time at which accuracy would drop to 50% after plotting accuracy as a function of reaction time (Figure 1—figure supplement 4a) and found values of 165 and 225 ms for linear and quadratic extrapolations respectively. Finally, we fit our behavioral data with an HDDM (Wiecki et al., 2013) and found a T0 estimate of 295 ±4 ms (despite there being no data below 350 ms). To address this issue, we fit a DDM to a small number of behavioral sessions we conducted with animals trained on the minimum reaction time of 350 ms but where that constraint was eliminated and found a T0 estimate of 265 ± 120 (SD) ms. We stress that because the animals were trained with a minimum reaction time, they likely would have required extensive training without that constraint to fully make use of the time below the minimum reaction time, thus this estimate is likely to also be an overestimate. We do note however that the estimate is lower than the estimate with an enforced minimum reaction time and has a much higher standard deviation (spanning our lower and upper bound estimates).

Despite the range of possible T0 values, we find that our qualitative findings (in terms of learning trajectory and near-optimality after learning) do not change (Figure 1—figure supplement 4f, g), and proceed with a T0=160 ms for the main text.

### Determining D~e⁢r⁢r and D~c⁢o⁢r⁢r

The experimental protocol imposes a mandatory post-error and post-correct response-to-stimulus time ($D~_{e⁢r⁢r}$ and $D~_{c⁢o⁢r⁢r}$, respectively). However, these times may not be accurate because of delays in the software communicating with different components such as the syringe pumps, and other delays such as screen refresh rates. We thus determined the actual mandatory post-error and post-correct response-to-stimulus times by measuring them based on timestamps on experimental file logs and found that $D~_{e⁢r⁢r}=3136$ ms, and $D~_{c⁢o⁢r⁢r}=6370$ ms (Figure 1—figure supplement 6).

#### Voluntary intertrial interval

We assume that the animals optimize reward rate based on task engagement time, that is, the sum of reaction times and all mandatory task delays, but not including any extra voluntary intertrial intervals. Therefore, our measures of non-decision task engagement time $D_{e⁢r⁢r}$ and $D_{c⁢o⁢r⁢r}$ do not include voluntary intertrial intervals. In essence this amounts to the assumption that animals exit the task between trials, potentially pursuing other goals, and do not count this voluntary interval when measuring their within-task reward rate.

We conducted a detailed analysis of the voluntary intertrial intervals after both correct and error trials (Figure 1—figure supplement 5). To prevent a new trial from initiating while the animals were licking one of the side lickports, the task included a 300 ms interval at the end of a trial where an extra 500 ms were added if the animal licked one of the side lickports (Figure 1—figure supplement 6). There was no stimulus (visual or auditory) to indicate the presence of this task feature so the animals were not expected to learn it. It was clear that the animals did not learn this task feature as most voluntary intertrial intervals are clustered in 500 ms intervals and decay after each boundary (Figure 1—figure supplement 5a). Aligning the voluntary intertrial distributions every 500 ms reveals substantial overlap (Figure 1—figure supplement 5c, d), indicating similar urgency in every 500 ms interval, with an added amount of variance the farther the interval from zero. Moreover, measuring the median voluntary intertrial interval from 0 to 500, 0–1000, and 0–2000 ms showed very similar values (47, 67, 108 ms after error trials, Figure 1—figure supplement 5b). The median was higher after correct trials (55, 134, 512 ms, Figure 1—figure supplement 5b) because the animals were collecting reward from the side lickports and much more likely to trigger the extra 500 ms penalty times.

#### Reward rate sensitivity to T0 and voluntary intertrial interval

To ensure that our results did not depend on our chosen estimate for T0 and our choice to ignore voluntary intertrial intervals when computing metrics like $D_{t⁢o⁢t}$ and reward rate, we computed fraction maximum instantaneous reward rate as a function of T0 and voluntary intertrial interval. We conducted this analysis across $n=26$ rats at asymptotic performance (Figure 1—figure supplement 7a, b), and during the learning period (Figure 1—figure supplement 7c, d). During asymptotic performance, sweeping T0 from our estimated minimum to our maximum possible values generated negligible changes in reward rate across a much larger range of possible voluntary intertrial intervals than we observed (Figure 1—figure supplement 7a). Reward rate was more sensitive to voluntary intertrial intervals, but did not drop below 90% of the possible maximum when considering a median voluntary intertrial interval up to 2000 ms (the median when allowing up to a 2000 ms window after a trial, after which agents are considered to have ‘exited the task’) (Figure 1—figure supplement 7b). During learning, we found similar results, with possible voluntary intertrial interval values have a larger effect on reward rate than T0, however even with the most extreme combination of a maximum T0=350 ms, and the median voluntary intertrial interval up to 2000 ms (Figure 1—figure supplement 7d, light gray trace), fraction maximum reward rate was at most 10–15% away from the least extreme combination of T0=160 ms and voluntary intertrial interval = 0 (Figure 1—figure supplement 7c, horizontal line along the bottom of the heat map) for most of the learning period. These results confirm that our qualitative findings do not depend on our estimated values of T0 and choice to ignore voluntary intertrial intervals.

#### Ignore trials

Because of the free-response nature of the task, animals were permitted to ignore trials after having initiated them (Figure 1—figure supplement 2). Although the fraction of ignored trials did seem to be higher at the beginning of learning for the first set of stimuli the animals learned (stimulus pair 1; Figure 1—figure supplement 2a), this effect did not repeat for the second set (stimulus pair 2, Figure 1—figure supplement 2b). This suggests that the cause for ignoring the trials during learning was not stimulus-based but rather related to learning the task for the first time. Overall, the mean fraction of ignored trials remained consistently low across stimulus sets and ignore trials were excluded from our analyses.

#### Post-error slowing

In order to verify whether the increase in reaction time we saw at the beginning of learning relative to the end of learning was not solely attributable to a post-error slowing policy, we quantified the amount of post-error slowing during learning for both stimulus pair 1 and stimulus pair 2. For stimulus pair 1, we found that there was a consistent but slight amount of average post-error slowing (Figure 6—figure supplement 5a). This amount was not significantly different at the start and end of learning (Figure 6—figure supplement 5b).

We re-did this analysis for stimulus pair 2 and found similar results: animals had a consistent, modest amount of post-error slowing but it did not change across sessions during learning (Figure 6—figure supplement 5c). We tested for a significant difference in post-error slowing between the last two sessions of stimulus pair 1 and the first two sessions of the completely new stimulus pair 2 and found none (Figure 6—figure supplement 5d) even though there was a large immediate change in error rate. In fact, there was a trend toward a decrease in post-error slowing (and toward post-correct slowing) in the first few sessions of stimulus pair 2. This is consistent with the hypothesis that post-error slowing is an instance of a more general policy of orienting toward infrequent events (Notebaert et al., 2009). As correct trials became more infrequent than error trials when stimulus pair 2 was presented, we observed a trend toward post-correct slowing, as predicted by this interpretation.

Our subjects exhibit a modest, consistent amount of post-error slowing, which could at least partially explain the reaction time differences we see throughout learning. An experiment with transparent stimuli where error rate was constant but reaction times dropped, however, strongly contradicts the account that the rats implement a simple strategy like post-error slowing to modulate their reaction times during learning.

### RNN model and LDDM reduction

We consider a recurrent network receiving noisy visual inputs over time. In particular, we imagine that an input layer projects through weighted connections to a single recurrently connected read-out node, and that the weights must be tuned to extract relevant signals in the input. The read-out node activity is compared to a modifiable threshold which governs when a decision terminates. This network model can then be trained via error-corrective gradient descent learning or some other procedure. In the following we derive the average dynamics of learning.

To reduce this network to a DDM with time-dependent SNR, we first note that due to the law of large numbers, activity increments of the read-out node will be Gaussian provided that the distribution of input stimuli has bounded moments. We can thus model the input-to-readout pathway at each time step as a Gaussian input $x⁢(t)$ flowing through a scalar weight $u$, with noise of variance $c_{o}^{2}$ added before the signal is sent into an integrating network. Taking the continuum limit, this yields a drift-diffusion process with effective drift rate $A~=A⁢u$ and noise variance $c~^{2}=u^{2}⁢c_{i}^{2}+c_{o}^{2}$. Here, $A$ parameterizes the perceptual signal, $c_{i}^{2}$ is the input noise variance (noise in input channels that cannot be rejected), and $c_{o}^{2}$ is the output noise variance (internal noise in output circuitry). The resulting decision variable $y^$ at time $T$ is Gaussian distributed as $N⁢(A⁢u⁢T⁢y,u^{2}⁢c_{i}^{2}⁢T+c_{o}^{2}⁢T)$, where $y$ is the correct binary choice. A decision is made when $y^$ hits a threshold of $\pmz$.

#### Within-trial drift-diffusion dynamics

On every trial, therefore, the subject’s behavior is described by a drift-diffusion process, for which the average reward rate as a function of signal to noise and threshold parameters is known (Bogacz et al., 2006). The accuracy and decision time of this scheme is determined by two quantities. First, the SNR

$$
A¯=(\frac{A~}{c~})^{2}=\frac{A^{2}u^{2}}{u^{2}c_{i}^{2}+c_{o}^{2}},
$$

and second, the threshold-to-drift ratio $z¯=z/A~=\frac{z}{A⁢u⁢(t)}$.

We can rewrite the SNR as

$$
A¯(t)=\frac{A^{2}u(t)^{2}}{c_{i}^{2}u(t)^{2}+c_{o}^{2}}=\frac{A^{2}}{c_{i}^{2}+c_{o}^{2}/u(t)^{2}}.
$$

From this it is clear that, when learning has managed to amplify the input signals such that $u⁢(t)→∞$, the asymptotic SNR is simply $A¯^{*}=A^{2}/c_{i}^{2}$. Further, rearranging to

$$
A¯(t)=\frac{A¯^{∗}}{1+(c_{o}^{2}/c_{i}^{2})/u(t)^{2}}
$$

shows that there are in fact just two parameters: the asymptotic achievable SNR $A¯^{*}$ and the output-to-input noise variance ratio $c≡c_{o}^{2}/c_{i}^{2}$,

$$
A¯(t)=\frac{A¯^{∗}}{1+c/u(t)^{2}}.
$$

The mean error rate ($E⁢R$), mean decision time ($D⁢T$), and mean reward rate ($R⁢R$) are therefore

$$
ER=\frac{1}{1+e^{2z¯A¯}}
$$



$$
DT=z¯tanh⁡(z¯A¯)
$$



$$
RR=\frac{1−ER}{DT+D_{tot}}
$$

where we have suppressed the dependence of $A¯$ and $z¯$ on time for clarity. Here, $D_{t⁢o⁢t}=T_{0}+E⁢R⋅D_{e⁢r⁢r}+(1-E⁢R)⋅D_{c⁢o⁢r⁢r}$ is the average non-decision task engagement time.

The term $z¯⁢A¯$ is a measure of the total evidence accrued on average, and is equal to

$$
z¯A¯=\frac{z}{Au(t)}\frac{A¯^{∗}}{1+c/u(t)^{2}}
$$



$$
=\frac{zA¯^{∗}/A}{u(t)+c/u(t)}.
$$

Here, for a fixed threshold $z$, the denominator shows the trade-off for increasing perceptual sensitivity: small $u⁢(t)$ causes errors due to output noise, while large $u⁢(t)$ causes errors due to overly fast integration for the specified threshold level.

#### Across-trial error-corrective learning dynamics

To model learning, we consider that animals adjust perceptual sensitivities $u$ over time in service of minimizing an objective function. In this section we derive the average learning dynamics when the objective is to minimize the error rate. The LDDM can be conceptualized as an ‘outer-loop’ that modifies the SNR of a standard DDM ‘inner-loop’ described in the preceding subsection. If perceptual learning is slow, there is a strong separation of timescales between these two loops. On the timescale of a single trial, the agent’s SNR is approximately constant and evidence accumulation follows a standard DDM, whereas on the timescale of many trials, the specific outcome on any one trial has only a small effect on the network weights $w$, such that the learning-induced changes are driven by the mean $E⁢R$ and $D⁢T$.

To derive the mean effect of error-corrective learning updates, we suppose that on each trial the network uses gradient descent on the hinge loss to update its parameters, corresponding to standard practice for supervised neural networks. The hinge loss is

$$
L(u,y)=max(0,1−y^y),
$$

yielding the gradient descent update.

$$
u[r+1]←u[r]−\lambda\frac{∂L(u[r],y)}{∂u}
$$

where $\lambda$ is the learning rate and $r$ is the trial number.

When the learning rate is small ($\lambda≪1$), each trial changes the weights minimally and the overall update is approximately given by the average continuous time dynamics

$$
\frac{du}{dr}=−⟨\lambda\frac{∂L(u,y)}{∂u}⟩
$$



$$
=−\lambda⟨⟨\frac{∂L(u,y)}{∂u}|error⟩+⟨\frac{∂L(u,y)}{∂u}|correct⟩⟩
$$



$$
=−\lambdaER⟨\frac{∂L(u,y)}{∂u}|error⟩
$$



$$
=\lambdaER⟨y\frac{∂y^}{∂u}|error⟩
$$

where $⟨⋅⟩$ denotes an average over the correct answer $y$, the inputs and the output noise. The first step follows from iterated expectation. The second step follows from the fact that the probability of an error is simply the error rate $E⁢R$, and for correct trials, the derivative of the hinge loss is zero. Next,

$$
\frac{∂y^}{∂u}=\frac{∂}{∂u}(\sumi=0Tux_{i}+η_{i})
$$



$$
=\sumi=0Tx_{i}
$$

where $T$ is the time step at which $y^$ crosses the decision threshold $\pmz$. Returning to Equation (56),

$$
\lambdaER⟨y\frac{∂y^}{∂u}|error⟩=\lambdaER⟨y\sumi=1Tx_{i}|error⟩.
$$

Hence, the magnitude of the update depends on the typical total sensory evidence given that an error is made. To calculate this, let $x¯_{t}=\sum_{i=0}^{t}x_{i}$ be the total sensory evidence up to time $t$, and $η¯_{t}=\sum_{i=0}^{t}$ be the total decision noise up to $t$. These are independent and normally distributed as

$$
x¯_{t}∼N(yAtdt,c_{i}^{2}tdt)
$$



$$
η¯_{t}∼N(0,c_{o}^{2}tdt).
$$

Therefore, we have

$$
⟨y\sumi=1Tx_{i}|error⟩=⟨yx¯_{T}|error⟩
$$



$$
=⟨yx¯_{T}|ux¯_{T}+η¯_{T}=−yz⟩
$$



$$
=⟨yx¯_{T}|ux¯_{T}/y+η¯_{T}/y=−z⟩.
$$

These variables are jointly Gaussian. Letting $v_{1}=y⁢x¯_{T}$ and $v_{2}=u⁢x¯_{T}/y+η¯_{T}/y$, the means $\mu_{1},\mu_{2}$, variances $\sigma_{1}^{2},\sigma_{2}^{2}$, and covariance $Cov⁢(v_{1},v_{2})$ of $v_{1},v_{2}$ given the hitting time $T$ are

$$
\mu_{1}=ATdt
$$



$$
\mu_{2}=uATdt
$$



$$
\sigma_{1}^{2}=c_{i}^{2}Tdt
$$



$$
\sigma_{2}^{2}=u^{2}c_{i}^{2}Tdt+c_{o}^{2}Tdt
$$



$$
Cov(yx¯_{T},ux¯_{T}/y+η¯_{T}/y)=⟨yx¯_{T}(ux¯_{T}/y+η¯_{T}/y)⟩−⟨yx¯_{T}⟩⟨ux¯_{T}/y+η¯_{T}/y⟩
$$



$$
=u⟨x¯_{T}^{2}⟩−u⟨x¯_{T}⟩^{2}
$$



$$
=uc_{i}^{2}Tdt.
$$

The conditional expectation is therefore

$$
⟨⟨v_{1}|v_{2}=−z,T⟩⟩_{T|error}=⟨\mu_{1}+\frac{Cov(v_{1},v_{2})}{\sigma_{2}^{2}}(−z−\mu_{2})⟩_{T|error}
$$



$$
=⟨ATdt+\frac{uc_{i}^{2}}{u^{2}c_{i}^{2}+c_{o}^{2}}(−z−uATdt)⟩_{T|error}
$$



$$
=A(DT)−\frac{uc_{i}^{2}}{u^{2}c_{i}^{2}+c_{o}^{2}}(z+uA(DT))
$$

where we have used the fact that $⟨Tdt⟩_{T|error}=DT$, because in the DDM the mean decision time is the same for correct and error trials. Inserting Equation (74) into Equation (59) yields

$$
\frac{d}{dr}u=\lambdaER(A(DT)+\frac{1}{1+\frac{c_{o}^{2}}{u^{2}ci^{2}}}(−z/u−A(DT)))
$$



$$
=\lambdaER(A(DT)−\frac{1}{1+c/u^{2}}(z/u+A(DT))).
$$

Finally, we switch the units of the time variable from trials to seconds using the relation $d⁢t=(D⁢T+D_{t⁢o⁢t})⁢d⁢r$, yielding the dynamics

$$
\tau\frac{d}{dt}u=\frac{ER}{DT+D_{tot}}(A(DT)−\frac{1}{1+c/u^{2}}[\frac{z}{u}+A(DT)]).
$$

The above equation describes the dynamics of $u$ under gradient descent learning. We note that here, the dependence of the dynamics on threshold trajectory is contained implicitly in the $D⁢T$, $E⁢R$, and $D_{t⁢o⁢t}$ terms.

To obtain equivalent dynamics for the SNR $A¯$, we have

$$
\tau\frac{d}{dt}A¯=2\frac{A^{2}c_{o}^{2}u}{(c_{i}^{2}+c_{o}^{2}/u(t)^{2})^{2}}u(t)^{−3}\frac{d}{dt}u
$$



$$
=2\frac{c}{A¯^{∗}}A¯^{2}u^{−3}\frac{d}{dt}u.
$$

Rearranging the definition of $A¯$ yields

$$
u^{2}=\frac{cA¯}{A¯^{∗}−A¯}.
$$

Inserting (Equation 80) into (Equation 79) and simplifying, we have

$$
\tau\frac{d}{dt}A¯=2\sqrt{\frac{A¯(A¯^{∗})}{c}}(1−\frac{A¯}{A¯^{∗}})^{3/2}\frac{d}{dt}u
$$



$$
=2\sqrt{\frac{A¯(A¯^{∗})}{c}}(1−\frac{A¯}{A¯^{∗}})^{3/2}\frac{ER}{DT+D_{tot}}(A(DT)−\frac{1}{1+c/u^{2}}[\frac{z}{u}+A(DT)])
$$



$$
=2A\sqrt{\frac{A¯(A¯^{∗})}{c}}(1−\frac{A¯}{A¯^{∗}})^{5/2}\frac{ER}{DT+D_{tot}}[DT−\frac{log⁡(1/ER−1)}{A¯^{∗}(1−\frac{A¯}{A¯^{∗}})^{2}}].
$$

Here, in the second step we have used the fact that $A¯=\frac{1−2ER}{2⟨DT⟩}log⁡\frac{1−ER}{ER}$ and Equation (80). Finally, absorbing the drift rate $A$ into the time constant $\tau=\frac{1}{A⁢\lambda}$, we have the dynamics

$$
\tau~\frac{d}{dt}A¯=2\sqrt{\frac{A¯(A¯^{∗})}{c}}(1−\frac{A¯}{A¯^{∗}})^{5/2}\frac{ER}{DT+D_{tot}}[DT−\frac{log⁡(1/ER−1)}{A¯^{∗}(1−\frac{A¯}{A¯^{∗}})^{2}}].
$$

This equation reveals that the LDDM has four scalar parameters: the asymptotic SNR $A¯^{*}$, the output-to-input-noise variance ratio $c$, the initial SNR at time zero $A¯⁢(0)$, and the combined drift rate/learning rate time constant $\tau~$. In addition, it requires the choice of threshold trajectory $z⁢(t)$.

To reveal the basic learning speed/instantaneous reward rate trade-off in this model, we investigate the limit where $A¯$ is small but finite (low signal-to-noise) and the threshold is small, such that the error rate is near $E⁢R=1/2$. Then the final term in Equation (84) goes to zero, giving

$$
\tau~\frac{d}{dt}A¯≈\sqrt{\frac{A¯(A¯^{∗})}{c}}(1−\frac{A¯}{A¯^{∗}})^{5/2}\frac{DT}{DT+D_{tot}}
$$



$$
∝\frac{DT}{DT+D_{tot}},
$$

such that learning speed is increasing in $D⁢T$. By contrast the instantaneous reward rate when $E⁢R=1/2$ is

$$
RR≈\frac{1/2}{DT+D_{tot}},
$$

which is a decreasing function of $D⁢T$.

We note that when the perceptual signal is small, $D⁢T$ is determined by the ratio of threshold to diffusion noise. Starting with Equation 47, we rewrite it in terms of threshold, perceptual signal, and noise:

$$
DT=\frac{z}{A~}tanh⁡(\frac{z}{A~}\frac{A~^{2}}{c~^{2}})
$$

If we explore the limit in which perceptual signal is small, and following L’Hôpital’s rule:

$$
limA~→0DT=limA~→0\frac{\frac{d}{dA~}ztanh⁡(\frac{z}{c~^{2}}A~)}{\frac{d}{dA~}A~}=limA~→0\frac{zsech^{2}(\frac{z}{c~^{2}}A~)}{1}
$$

Leaving:

$$
limA~→0DT=(\frac{z}{c~})^{2}
$$

Thus, a change in $D⁢T$ when perceptual signal is low could be caused by either a changing threshold with fixed diffusion noise, a constant threshold with varying diffusion noise, or a combination thereof, without the immediate ability to tell these apart. In these cases, however, we note that the ratio of threshold to diffusion noise cannot stay constant if $D⁢T$ changes.

#### Threshold policies

We evaluate several simple threshold policies.

$$
\gamma\frac{d}{dt}z^{s}(t)=z^{∗}(A¯(t))−z^{s}(t).
$$

where $\gamma$ controls the rate of convergence.

Finally, the global optimal policy optimizes the entire function $z¯⁢(t)$ to maximize total cumulative reward during exposure to the task. To compute the optimal threshold trajectory, we discretize the reduction dynamics in Equation 77 and perform gradient ascent on $z¯⁢(t)$ using automatic differentiation in the PyTorch python package. While this procedure is not guaranteed to find the global optimum (due to potential nonconvexity of the optimization problem), in practice we found highly reliable results from a range of initial conditions and believe that the identified threshold trajectory is near the global optimum.

#### Parameter fitting

The LDDM has several parameters governing its performance, including the asymptotic optimal SNR, the output/input noise variance ratio, the learning rate, and parameters controlling threshold policies where applicable. To fit these, we discretized the reduction dynamics and performed gradient ascent on the log likelihood of the observed data under the LDDM, again using automatic differentiation in the PyTorch python package. Because our model is highly simplified, our goal was only to place the parameters in a reasonable regime rather than obtain quantitative fits. We note that our fitting procedure could become stuck in local minima, and that a range of other parameter settings might also be consistent with the data. The best fitting parameters we obtained and used in all model results were $A=0.9542,c_{i}=0.3216,c_{o}=30,u_{0}=0.0001$. We used a discretization time step of $d⁢t=160$. For the constant threshold and $i⁢R⁢R$-sensitive policies, the best fitting initial threshold was $z⁢(0)=30$. For the $i⁢R⁢R$-sensitive policy, the best fitting decay rate was $\gamma=0.00011891$.
