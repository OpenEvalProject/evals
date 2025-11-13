# Inferring eye position from populations of lateral intraparietal neurons

## Authors

- Arnulf BA Graf<sup>1</sup> †
- Richard A Andersen<sup>1</sup>

### Affiliations

1. Division of Biology and Biological Engineering California Institute of Technology Pasadena United States

† Corresponding author

## Abstract

Understanding how the brain computes eye position is essential to unraveling high-level visual functions such as eye movement planning, coordinate transformations and stability of spatial awareness. The lateral intraparietal area (LIP) is essential for this process. However, despite decades of research, its contribution to the eye position signal remains controversial. LIP neurons have recently been reported to inaccurately represent eye position during a saccadic eye movement, and to be too slow to support a role in high-level visual functions. We addressed this issue by predicting eye position and saccade direction from the responses of populations of LIP neurons. We found that both signals were accurately predicted before, during and after a saccade. Also, the dynamics of these signals support their contribution to visual functions. These findings provide a principled understanding of the coding of information in populations of neurons within an important node of the cortical network for visual-motor behaviors.

## Materials and methods

### Delayed memory saccade task on a grid

The animals performed delayed memory saccades on a Cartesian grid whose nodes were spaced by 8 deg. The animals maintained fixation for 1000 ms at one randomly chosen location on the 3 × 3 grid. Next a target was flashed for 300 ms in one location randomly chosen from the eight neighboring locations, and the animals were required to maintain fixation during this epoch. The animals had to remember the target location for 1300 ms ± 200 ms (drawn from a uniform distribution). Upon extinction of the fixation, they made a saccade to the remembered target location in complete darkness, thus acquiring a postsaccade fixation on a 5 × 5 grid. They maintained fixation there for 500 ms (fixation I) in the absence of visual input. A fixation light was subsequently turned on at the target location for another 500 ms, possibly triggering a small corrective saccade. Upon completion of this second fixation (fixation II), the stimulus was removed and the animals were rewarded by a drop of water. We only considered correct trials. The animals completed ∼11 random blocks, for a total of ∼11 × ((3 × 3) × 8) = 792 saccades. The eye position was tracked by an infrared camera, and the signal was sampled at 2 kHz (EyeLink, SR Research, Ontario, Canada). All behavioral variables were instructed and monitored in real-time (LabView, National Instruments, Austin, TX, USA).

The delayed memory task allowed us to examine separately neuronal signals mediating sensory inputs (vision), planning, and motor commands. Furthermore, we were able to study how pre- and postsaccade eye positions and saccade directions are represented because we extended the delayed memory task to cover a grid. One novelty of this task is that eye position and saccade directions were sampled exhaustively on a Cartesian grid, thus yielding a complete set of independent oculomotor variables. In contrast to previous single neurons studies where behaviors were tailored to best drive a given neuron (e.g., preferred and anti-preferred saccade direction), another novelty of the task resides in the fact that we used a fixed and finite set of oculomotor behaviors to drive neuronal populations as a whole.

### Neuronal population recordings

Two adult male rhesus monkeys (Macaca mulatta, monkey S 14.3 kg and monkey P 13.7 kg) were used in the experiments. All procedures were in accordance with the guidelines of the Caltech Institutional Animal Care and Use Committee and the National Institute of Health Guide for the Care and Use of Laboratory Animals. Each animal was implanted with a headpost and custom-made recording chamber under aseptic conditions using isoflurane anesthesia. Both animals received postoperative analgesics during postsurgical recovery. We used MRI scans as guides for the location of LIP.

We recorded populations of LIP neurons using a 5-channel microdrive with movable quartz-platinum/tungsten microelectrodes (Thomas Recording, Giessen, Germany). The neuronal data were filtered between 100 Hz and 8 kHz (preamplifier, Plexon, Dallas, TX, USA), and then sampled at 40 kHz (Multichannel Acquisition Processor, Plexon). Single units were sorted online using a dual-window discriminator based on the shape of the waveform. At the beginning of each recording session, we verified that each electrode tip was located in LIP by obtaining a vigorous sensory, planning and motor activity during a center-out delayed memory saccade task. Each animal was recorded in a different hemisphere. Hence, when combining the neuronal populations recorded in both animals, we were able to overcome the component of the sampling bias associated with the fact that LIP has contralateral response fields for visual stimuli and movement direction (Quian Quiroga et al., 2006). To empirically quantify the component of the sampling inherent to the homogeneity of neurons in the sample, we acquired a different population of simultaneously recorded neurons for each session.

We gathered empirical samples of simultaneously recorded neurons for three reasons. First, this allowed us to assess the sampling bias underlying the computation of the NPC. Second, the neurons recorded simultaneously were subject to exactly the same experimental conditions, thus eliminating session-to-session variability from the computation of the NPC. Third, simultaneously recorded neurons gave a more natural sample of the NPC because these neurons were involved—although to different degrees—in exactly the same behaviors within a session and across sessions. This is in stark contrast to most single neuron studies where the task was optimized to best drive the studied neuron.

### Computing the accuracy of the neuronal population code

To address population coding in LIP, we studied the accuracy with which pre- and postsaccade eye positions and the saccade direction could be predicted from the population response. This neuronal population code (NPC) is a single summary metric that encompasses the response properties of multiple neurons across a range of oculomotor behaviors, unlike most classical measures of single-cell electrophysiology where each neuron and behavior are studied separately. The NPC describes the accuracy of cortical computations relevant to a given task within an area, and the information available in principle to a downstream neuron that gets synaptic inputs from this population.

We used Bayesian inference to model the NPC by predicting the accuracy with which a behavior can be inferred from the population response taken to be the spike count of each neuron over a given temporal window (Foldiak, 1993; Seung and Sompolinsky, 1993; Salinas and Abbott, 1994; Sanger, 1996; Oram et al., 1998; Dayan and Abbott, 2001; Jaynes, 2003; Pouget et al., 2003; Sanger, 2003; Averbeck and Lee, 2004; Brown et al., 2004; Ma et al., 2006; Graf et al., 2011). The prior p(b) on the behavior b, i.e. the probability of a given behavior, was computed from the number of occurrences of that behavior. It represents the behavioral history, and is entirely defined by the task (the task has no error trials). The likelihood function p(r|b) is the probability to obtain a population response (spike count) r given a behavior b, evaluated across behaviors. It is a description of the encoding process that addresses how a behavior is represented at the level of neuronal populations. We computed the likelihood by assuming that the N neurons were independent, yielding:

$$
p(r|b)=\prodi=1Np(r_{i}|b)
$$

Next, we used a parametric approximation for the likelihood function of each neuron. The simplest approximation is to assume that the spike counts of a neuron for a given behavior follow a Poisson distribution:

$$
p(r|b)=\frac{\mu(b)^{r}}{r!}exp(−\mu(b))
$$

where $\mu(b)$ is the mean response across all trials corresponding to the behavior b. This model requires the empirical determination of one parameter: the mean response (tuning curve). This model has been widely used, and was also extended to take correlations between neurons into account (Sanger, 1996; Oram et al., 1998; Ma et al., 2006; Graf et al., 2011). Alternatively, a more complicated approximation is to assume that the spike count distribution can be approximated by a truncated Gaussian over positive integers:

$$
p(r|b)=\frac{G(r,\mu,\sigma,b)}{\int0∞G(r,\mu,\sigma,b)dr}
$$

where: $G(r,\mu,\sigma,b)=\frac{1}{\sqrt{2\pi\sigma(b)^{2}}}exp(−\frac{(r−\mu(b))^{2}}{2\sigma(b)^{2}})$

This model requires the empirical determination of two parameters: the mean $\mu(b)$ and the variance $\sigma(b)^{2}$ of the response across all trials corresponding to the behavior b. Both approximations gave decoding accuracies (see below) that were strongly correlated (r2 = 0.95, p=0).

The posterior function $p(b|r)$ is the hallmark of decoding: it is the probability to obtain a behavior given a neuronal population response. By Bayes' theorem, it is proportional to the product of the likelihood function and the prior:

$$
p(b|r)=\frac{p(r|b)p(b)}{p(r)}
$$

where $p(r)$ is the partition function. In order to ensure good generalization (and thus avoid overfitting), we evaluated the posterior function using a leave-one-out cross-validation scheme (Duda et al., 2001). In other words, the trials that were used to evaluate the posterior were different from the trials used to compute the parameters of the model.

The posterior function is a probability distribution that informs us how likely a behavior can be associated with a given neuronal population response. We considered the maximum of the posterior distribution as the estimate corresponding to a population activity (MAP estimate). We determined the prediction accuracy of each behavior by computing the proportion of veridical MAP estimates evaluated across all trials, i.e., the fraction of trials where true and estimated behaviors coincided (exact estimates). Finally, the accuracy of the NPC was the average of the prediction accuracy of each behavior. The mean and standard error of the NPC were determined using 1000 bootstraps across all trials.

Our task allowed us to study three oculomotor behaviors: the 3 × 3 = 9 presaccade eye positions, the eight saccade directions and the 5 × 5 = 25 postsaccade (future) eye positions. These behaviors were entangled in a single population response. In each trial, the animal executed one out of a total of 9 × 8 = 72 oculomotor behaviors. Each population response thus predicted one saccade direction and one presaccade eye position. Because presaccade eye position and saccade direction were independent, their respective NPCs were computed separately, for example the NPC for the saccade direction was determined using the fraction of correct saccade direction estimates across all trials. The postsaccade eye position was the vector sum of the presaccade eye position and the saccade direction. Multiple presaccade eye positions and saccade directions could yield the same postsaccade eye position. The postsaccade eye position was thus dependent on the presaccade eye position and the saccade direction. We explicitly modeled this dependency in the Bayesian framework by translating the vector sum of the behaviors into a marginalization of the posterior distributions: the posterior of the postsaccade eye position was the sum across the posteriors of all presaccade eye positions and saccade directions that yielded the same postsaccade eye position. In other words, the vector sum of the behaviors translated into a sum of their respective posteriors.

### Time course of the accuracy of the NPC

To determine the time course of the NPC, we first aligned the spike times for each trial to either the target onset or the saccade onset. The saccade onset (reaction time) was determined offline based on the saccade velocity using a method adapted from (Engbert and Kliegl, 2003). For each neuron, we subsequently computed the spike counts over causal boxcar windows (rectangular windows looking only in the past) of length 250 ms sliding in 10 ms steps. We chose a length of 250 ms because this interval is short enough compared to the length of the epochs in the task, but long enough to have sufficient spike counts for decoding. For each time step, we then computed the prediction accuracy (mean ± SEM from bootstrap estimates), yielding the time course of the NPC. The inference was thus done on intervals of identical length (250 ms) across the entire task.

To compute the decoding accuracy for a given task epoch (which may vary in length), we computed the root mean square of the NPC time course between the events defining the task epoch (mean ± SEM across bootstrap estimates). In other words, we computed the area under the time course normalized by the length of the epoch. This allowed us to compare the NPC across task epochs of different lengths in an unbiased fashion because the NPC computed directly from the spike counts collected over epochs of different lengths is dependent on the length of the epoch.

We examined the possible sources of the NPC updating by computing the onsets and peaks of the time course of the NPC across the entire task. First, we smoothed the NPC time courses using a truncated Gaussians over a 250 ms window. We then compared for each time step the derivatives of the NPC time course before and after. We finally determined the onsets by maximizing the difference of the derivatives after and before the onset, and the peaks by maximizing the difference of the derivatives before and after the peak.

### Recursive neuronal elimination

To quantitatively rank the contributions of each neuron to the NPC, we developed a technique derived from machine learning (Duda et al., 2001; Guyon et al., 2002): Recursive Neuronal Elimination (RNE). RNE finds the subset of most important neurons by iteratively removing neurons that least affect the accuracy of the NPC. We first pooled all recording sessions that had at least nine trials per oculomotor behavior, for a total of 325 independently recorded neurons. We then found the neuron(s) that when removed from the population maximized the decoding accuracy across the remaining neurons. We iteratively applied this procedure to the remaining neurons, thus creating a list of neurons ranked from least to most important. The decoding accuracy was averaged across the three behaviors because the same neuronal subset was used to predict each one of them. Also, we determined the decoding accuracies using the root mean square across the task epochs that best mediate each behavior: the memory, fixation and fixation II epochs for the saccade direction, pre- and postsaccade eye position respectively.

RNE yields populations of neurons that are devoid of non-task related neurons and redundant neurons (e.g., neurons with similar tuning). It is thus ideally suited to study the dependency of prediction accuracy and population size in a principled manner that avoids using neuronal subsets defined by random pooling (Bremmer et al., 1998). As such RNE can be used to assess the sparseness of the NPC. Also, RNE is a quantitative method to address sampling bias in large neuronal populations. Finally, once an ‘optimized’ subset is defined, the accuracy of the NPC for this subset can be used to correct the accuracy of the NPC for each empirical population by scaling its average decoding accuracy to mach the one of the ‘optimized’ subset.
