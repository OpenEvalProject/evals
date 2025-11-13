# Cortical state transitions and stimulus response evolve along stiff and sloppy parameter dimensions, respectively

## Authors

- Adrian Ponce-Alvarez<sup>1</sup> ([ORCID: 0000-0003-1446-7392](https://orcid.org/0000-0003-1446-7392)) †
- Gabriela Mochol<sup>1</sup>
- Ainhoa Hermoso-Mendizabal<sup>2</sup>
- Jaime de la Rocha<sup>2</sup> ([ORCID: 0000-0002-3314-9384](https://orcid.org/0000-0002-3314-9384))
- Gustavo Deco<sup>1</sup>

### Affiliations

1. Center for Brain and Cognition, Computational Neuroscience Group, Department of Information and Communication Technologies, Universitat Pompeu Fabra Barcelona Spain
2. Institut d’Investigacions Biomèdiques August Pi i Sunyer (IDIBAPS) Barcelona Spain
3. Institució Catalana de la Recerca i Estudis Avançats (ICREA) Barcelona Spain
4. Department of Neuropsychology, Max Planck Institute for Human Cognitive and Brain Sciences Leipzig Germany
5. School of Psychological Sciences, Monash University Melbourne Australia

† Corresponding author

## Abstract

Previous research showed that spontaneous neuronal activity presents sloppiness: the collective behavior is strongly determined by a small number of parameter combinations, defined as ‘stiff’ dimensions, while it is insensitive to many others (‘sloppy’ dimensions). Here, we analyzed neural population activity from the auditory cortex of anesthetized rats while the brain spontaneously transited through different synchronized and desynchronized states and intermittently received sensory inputs. We showed that cortical state transitions were determined by changes in stiff parameters associated with the activity of a core of neurons with low responses to stimuli and high centrality within the observed network. In contrast, stimulus-evoked responses evolved along sloppy dimensions associated with the activity of neurons with low centrality and displaying large ongoing and stimulus-evoked fluctuations without affecting the integrity of the network. Our results shed light on the interplay among stability, flexibility, and responsiveness of neuronal collective dynamics during intrinsic and induced activity.

## Introduction

How biological systems achieve a tradeoff between stability and flexibility is a central question in biology. A candidate explanation for the coexistence of these two features is sloppiness (Machta et al., 2013; Transtrum et al., 2015). In general, sloppiness is a property of complex models exhibiting large parameter uncertainty when fit to data, meaning that different combinations of parameters lead to a similar system behavior, while changes in some few critical parameters, called stiff parameters, significantly modifies it. In this way, biological systems can be either robust to large fluctuations of input/environmental signals which effects are embedded in a high-dimensional subspace of insensitive parameters, or, on the contrary, by tuning some few parameters, configured to be highly sensitive and selective to relevant signals.

Recently, it has been shown that the spontaneous activity of neural circuits presents sloppiness both in vitro and in vivo (Panas et al., 2015), suggesting that collective activity is stabilized by a subset of highly active and stable neurons, while the activity and co-activity of the remaining neurons present larger spontaneous fluctuations without strongly affecting the collective statistics. However, this view is challenged by extensive research showing that the spontaneous cortical activity transits through different synchronized and desynchronized cortical states (Marguet and Harris, 2011; Harris and Thiele, 2011; Luczak et al., 2013; Pachitariu et al., 2015) that represent statistically different collective behaviors (Hahn et al., 2017) with different information processing capabilities (Pachitariu et al., 2015; Engel et al., 2016; Beaman et al., 2017). Moreover, how sensory inputs affect sloppiness is unknown and it is a relevant question to understand how sensory stimuli change the network state in a way that responsiveness and stability are ensured. In the present study, we examined how changes in neural network parameters correlate with spontaneous transitions among cortical states and stimulus-evoked responses.

To answer these questions, we recorded the neuronal spiking activity in the primary auditory cortex (A1) of six anesthetized rats. We analyzed the joint activity of groups of neurons while the cortex spontaneously transited through different synchronized and desynchronized cortical states and intermittently received external acoustic stimuli. We used a statistical model to describe the joint spiking activity with a small number of parameters. We found that the estimated parameters of neuronal ensemble activity presented sloppiness and that sensory inputs and cortical state transitions evolved in different pathways in parameter space. Specifically, we found that cortical state transitions evolve along stiff dimensions, whereas sensory-evoked activity evolves along sloppy dimensions. Finally, we showed that stiff parameters are related to the activity and co-activity of neurons with high centrality within the functional network of the recorded neurons.

## Results

We recorded spontaneous and stimulus-evoked population activity from the primary auditory cortex (A1) of urethane-anesthetized rats (n = 6) using multisite silicon microelectrodes (see Materials and methods). The data was composed of activity from $N_{pop}$ well-isolated single units ($N_{pop}=$ 44-147 neurons) and some spike-trains from multi-unit activity (3-103 spike-trains). Unless otherwise specified, the analyses present here focused on single-unit activity only. We analyzed the data during spontaneous activity and in response to acoustic 'clicks' (5-ms square pulses; inter-stimulus interval, 2.5 or 3.5 s). To track the evolution of the neuronal activity, we divided each recording session into $N_{E}$ adjacent epochs of 100 s, each one containing 12–29 stimulus presentations. Within each 100-s epoch the data was separated into spontaneous activity, that is the activity during 1.5-s intervals preceding each stimulus (i.e., 18–43.5 s of spontaneous activity in total for each epoch), and stimulus-evoked activity, that is the activity right after the stimulus onset (Figure 1A–B).

![Figure 1.](https://cdn.elifesciences.org/articles/53268/elife-53268-fig1-v2.jpg)

**Figure 1.:** (A) Each recording session was divided into $N_{E}$ adjacent epochs of 100 s. (B) Each epoch contained a series of stimulus presentations. Stimuli consisted on acoustic clicks. For each 100-s epoch we collected the spontaneous activity, that is the activity during 1.5-s intervals preceding each stimulus (red intervals), to build concatenated binary data. (C) Binary data was obtained by discretizing time in bins of dt = 10 ms. Within each time bin, the ensemble activity of $N$ neurons was described by a binary vector, $\sigma→=\sigma_{1},\sigma_{2},…,\sigma_{N}$, where $\sigma_{i}=+1$ if the i-th neuron generated a spike (black) and $\sigma_{i}=-1$ otherwise (white). (D) Maximum entropy models were used to describe the binary patterns of subsets of 10 neurons, during each 100-s epoch. The model parameters $Ω={h,J}$ represents the intrinsic tendency of neuron i towards activation ($\sigma_{i}=+1$) or silence ($\sigma_{i}=-1$), noted $h_{i}$, and the effective interaction between neurons i and j, noted $J_{ij}$.

### Description of spontaneous activity patterns using maximum entropy models

We first examined the temporal evolution of the spontaneous activity across the $N_{E}$ epochs. Because we were interested in the evolution of the statistics of ensemble activity, we described the collective activity of groups of $N$ single-units using a maximum entropy model (MEM) (Schneidman et al., 2006; Shlens et al., 2009; Tkačik et al., 2015) in each epoch (see Materials and methods and Figure 1C–D). These models allowed us to describe the patterned activity with a small number of parameters. To fit the model, time was discretized in bins of dt = 10 ms. Within each time bin, the ensemble activity of $N$ neurons was described by a binary vector, $\sigma→=\sigma_{1},\sigma_{2},…,\sigma_{N}$, where $\sigma_{i}=+1$ if the i-th neuron fired a spike in that time bin and $\sigma_{i}=-1$ otherwise. The collective activity was determined by the probability distribution $P\sigma→$ over all $2^{N}$ possible binary patterns. The MEM fits $P_{data}\sigma→$ by finding a distribution $P_{MEM}\sigma→$ that maximizes its entropy under the constraint that the activation rates ($⟨\sigma_{i}⟩$) and the pairwise correlations ($<\sigma_{i}\sigma_{j}>$) found in the data are preserved in the model. It is known that the maximum entropy distribution that is consistent with these constraints is the Boltzmann distribution, $P\sigma→∝e^{-E\sigma→}$, where $E\sigma→$ is the energy of the pattern $\sigma→$, given by: $E\sigma→=-\sumi=1Nh_{i}\sigma_{i}+\frac{1}{2}\sumj=1NJ_{ij}\sigma_{i}\sigma_{j}$ (Schneidman et al., 2006; Tkačik et al., 2015). The model parameter $h_{i}$ represents the intrinsic tendency of neuron i towards activation ($\sigma_{i}=+1$) or silence ($\sigma_{i}=-1$) and the parameter $J_{ij}$ represents the effective interaction between neurons i and j. Once we learned the parameters $Ω={h,J}$ using a gradient descent algorithm (see Materials and methods), the expected probability of any pattern is known. For each recording session and for each of the $N_{E}$ epochs, we fitted the model using the spontaneous binarized activity from an ensemble of $N$ = 10 randomly selected single neurons from the entire population of $N_{pop}$ single neurons. We chose $N$ = 10 because 100-s epochs provided around 5000 observed spontaneous patterns, which is a reasonable amount to get an estimate of the distribution of the 210 = 1024 possible patterns. To accurately estimate models of larger $N$, the epochs ought to be much larger preventing possibility to investigate the temporal evolution of the model along the experiment. We finally repeated the process of randomly choosing $N$ = 10 single units $Q$ times for each experiment (for datasets 3 and 5: $Q=10$ ensembles, otherwise: $Q=20$). In summary, for each recording session, we built $Q\timesN_{E}$ models, each composed of 10 units. Before studying the evolution of the model parameters $Ω(t)$ across epochs ($t=$ 0, 1, 2..), we first evaluated how well the MEM fitted the data.

For each epoch, we used the Jensen-Shannon divergence ($D_{JS}$, see Materials and methods) to measure the similarity between the probability distribution of the empirical and model binary patterns (Figure 2A–C). We compared this similarity to the distribution of binary patterns predicted from independent-MEMs, for which only the activation rates were preserved (i.e., only $h$ was optimized). We found that the empirical distribution was well approximated by MEMs and that, for all recording sessions, the goodness-of-fit (i.e., $1/D_{JS}$) was orders of magnitude higher for MEMs than for independent-MEMs (Figure 2C), leading to excellent model performances (i.e., Kullback-Leibler ratio equal to 0.95 ± 0.03 on average, see Materials and methods).

![Figure 2.](https://cdn.elifesciences.org/articles/53268/elife-53268-fig2-v2.jpg)

**Figure 2.:** (A) Comparison between the probability distribution of empirical binary patterns and the probability distribution predicted by MEMs (black dots) and independent models (gray dots), for all epochs and all neuronal ensembles. Every point represents a binary pattern that has appeared in the data at least once. Red line represents the identity line. (B) Jensen-Shannon divergence (DJS) between spiking data and MEMs, and between spiking data and independent models, across time, averaged across neuronal ensembles. Error bars are smaller than the widths of the traces. Data in (A) and (B) correspond to one example rat (#1). (C) Goodness-of-fit (1/DJS) for MEMs and for independent models, averaged over all models (i.e., all ensembles and all epochs), for each rat. Error bars indicate SEM.

### Temporal evolution of activity observables, model parameters, and their sensitivity

We next analyzed the temporal evolution of the different spiking data statistics and the model parameters. We first measured the temporal variation of the activity observables (i.e., firing rates and pairwise correlations) by calculating the average Pearson correlation (or similarity $\gamma$; see Materials and methods) between the values in epoch $t$ and those in epoch $t+Δt$ (Figure 3A). This similarity rapidly decayed with $\Deltat$, indicating that the observables substantially changed over time. We next examined how much these variations influenced the evolution of the collective activity characterized by the distribution of binary patterns. For this, we evaluated how well the data in a given epoch $t$ could be explained by the MEM constructed using the data at time $t+Δt$. Specifically, we calculated $D_{JS}Δt$, given by the average Jensen-Shannon divergence between the distribution of data binary patterns in epoch $t$, that is $P_{data, t}$, and the distribution of binary patterns predicted by the MEM constructed using the data in epoch $t+Δt$, that is $P_{MEM,t+Δt}$ (see Materials and methods). We found that $D_{JS}Δt$ increased as a function of $\Deltat$, indicating that the collective activity changed during the recording session, so that the model parameters $Ω(t)$ at epoch $t$ did not predict the collective activity at epoch $t+Δt$ (Figure 3B). Indeed, the model parameters substantially changed over time, with a rapidly decaying similarity (Figure 3C, orange and purple traces).

![Figure 3.](https://cdn.elifesciences.org/articles/53268/elife-53268-fig3-v2.jpg)

**Figure 3.:** (A) Similarity (i.e., Pearson correlation coefficient) of mean firing rates (red) and pairwise correlations (purple) as a function of elapsed time Δt. (B) Jensen-Shannon divergence (DJS) between the distribution of empirical spiking patterns in epoch t and the distribution of binary patterns of the pairwise MEM in epoch t + Δt, averaged over all t. (C) Left: Similarity of Fisher information matrix (FIM) elements, biases ($h_{i}$), and couplings ($J_{ij}$) as a function of elapsed time Δt. Right: FIMs at time t = 0 h and t = 1 h. Data in (A), (B), and (C) correspond to one example rat (#1); traces show averages over neuronal ensembles and shaded areas correspond to SEM. (D) Similarity of FIM elements, rates, biases, correlations, and couplings after 1/2 hour (i.e., Δt = 30 min), averaged across all neuronal ensembles, for each rat. Error bars indicate SEM.

As shown in Panas et al. (2015), changes in model parameters can differently contribute to collective activity, since the model can be sensitive to changes in some few combinations of parameters. Following this, we next evaluated the sensitivity of model parameters by calculating the Fisher information matrix (FIM, see Materials and methods) for each neuronal ensemble and each epoch. The FIM measures how much the model log-likelihood $P_{MEM}(\sigma→|Ω)$ changes with respect to changes in the parameters $Ω$. We first notice that the FIM had the highest stability across time, compared to the data firing rates and correlations and the model parameters (Figure 3C, blue trace). Indeed, the similarity after 1/2 hour was $\gamma=$ 0.882 ± 0.002 for the FIM, $\gamma=$ 0.732 ± 0.003 for the firing rates, $\gamma=$ 0.551 ± 0.004 for the biases, $\gamma=$ 0.364 ± 0.004 for the correlations, $\gamma=$ 0.234 ± 0.003 for the couplings (F4,495 = 305.73, p<0.001, one-way ANOVA followed by Tukey's post hoc analysis) (Figure 3D). Altogether these results show that the sensitivity of the model parameters remained relatively stable despite substantial changes in firing rates, correlations, collective activity and the model parameters themselves.

### Spontaneous neuronal activity presents sloppiness

Having shown that the sensitivity of model parameters was relatively stable during the recording sessions, we next studied the structure of the FIMs. First, we noted that most elements of the FIM had near-zero values (Figure 4A) indicating that most of the parameters had a small effect on the model log-likelihood. In contrast, a small fraction of elements had values strongly different from zero as revealed by the heavy tail of the distribution of FIM values (Figure 4A). To identify the parameter combinations that had the strongest effect on model behavior, we decomposed the FIM into eigenvectors and classified them according to their eigenvalue (Figure 4B). We observed that, except for some few eigenvalues, most of the FIM eigenvalues were small, corresponding to combinations of parameters that had little effect on model behavior. These unimportant parameter combinations defined the sloppy dimensions of the model. The few eigenvectors with large eigenvalues defined the stiff parameter dimensions along which the model behavior was strongly affected.

![Figure 4.](https://cdn.elifesciences.org/articles/53268/elife-53268-fig4-v2.jpg)

**Figure 4.:** (A) Distribution of FIM elements, for all epochs, all neuronal ensembles, and all rats. (B) Eigenvalues of the FIM, average across epochs and neuronal ensembles, for an example rat (# 1). Shaded areas represent SEM. Stiff and sloppy dimensions correspond to FIM eigenvectors of lowest and highest ranks, respectively. (C) Projection of $Ω(t')$ into the first three eigenvectors of the FIM from a given epoch $t$, for all $t'\neqt$. Data from one neuronal ensemble from rat 1. (D) Projection of $Ω(t')$ into the first and the 20th eigenvectors of the FIM from epoch $t$, noted $ν_{t,1}$ and $ν_{t,20}$, respectively, for all $t'\neqt$. Top inset: distribution of projections into $ν_{t,1}$. Right inset: distribution of projections into $ν_{t,20}$. Note higher variance of projections into $ν_{t,20}$ than into $ν_{t,1}$. Data from one neuronal ensemble from rat 1. (E) Average variance of projections of $Ω(t')$ into the different eigenvectors of the FIM at epoch $t$ (for all $t'\neqt$), for the different rats. Traces represent average over neuronal ensembles and shaded areas represent SEM.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/53268/elife-53268-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** The variance of projections of $Ω(t^{′})$ into the different eigenvectors of the Fisher information matrix (FIM) for spiking data was compared to the one obtained from stationary surrogates. (A) The average variance of projections of model parameters into the different eigenvectors of the FIMs was calculated for the spiking data (parameters $Ω(t')$) and for the stationary surrogates (parameters $Ω^{′}(t^{′})$), as a function of the rank $k$ of the eigenvectors. Variances were noted $Var(k)$ and $Var_{stat}(k)$ for the spiking data and the stationary surrogates, respectively. Traces represent average over neuronal ensembles and shaded areas represent SEM. Note logarithmic scale on the y-axis. We found that parameter fluctuations were larger than expected by estimation errors in the stationary case for all eigenvectors (i.e., $Var(k)>Var_{stat}(k)$, for all $k$). (B) The difference between variances of parameter projections estimated from the spiking data and those estimated from stationary surrogates increased with $k$. Thus, parameter fluctuations along sloppy dimensions were those that deviated the most from the stationary case. Traces represent average over neuronal ensembles and shaded areas represent SEM.

In the following we showed that the temporal evolution of the model parameters occurred predominantly along the sloppy dimensions. For this, we projected the parameters $Ω(t^{′})$, calculated at time $t'$, into the eigenvectors of the FIM at time $t$, denoted $ν_{t,1},ν_{t,2},…,ν_{t,k},…$, where $k$ is the rank of the eigenvector (Figure 4C). For each dimension, or eigenvector, we obtained a distribution of projections of parameters $Ω(t^{′})$ (Figure 4D). To quantify how much the parameters varied along each eigenvector, we calculated the average variance of each projection as a function of the rank of the eigenvector. We found that the projection variance increased as a function of the eigenvector’s rank for all datasets (Figure 4E). This indicates that the model parameters predominantly evolved along sloppy dimensions (i.e., FIM eigenvectors of highest rank $k$), while they remained relatively stable along stiff dimensions (i.e., FIM eigenvectors of lowest rank $k$). Using stationary surrogate data, we controlled that these parameter fluctuations were not fully explained by estimation errors and, furthermore, that parameter fluctuations along sloppy dimensions were those that deviated the most from the stationary case (see Figure 4—figure supplement 1). Nevertheless, we noted that the projection variance into the stiff dimensions, albeit small, was not zero. This means that the model also evolved along parameter dimensions that had a strong impact on the collective activity. We hypothesized that changes in collective behavior, associated to changes in stiff parameters, were related to changes in cortical state.

### Cortical state transitions evolve along stiff dimensions

To test this hypothesis, we first measured the cortical state in each epoch $t$ using silence density, $CS(t)$, defined as the fraction of 20-ms time bins with zero population activity, that is no spikes from any neuron (see Materials and methods) (Luczak et al., 2013; Pachitariu et al., 2015; Mochol et al., 2015). To obtain the most accurate estimate of silence density, we used all the spikes from the merge of all the single-units and multi-units in the calculation of $CS(t)$. During the course of the experiment, we observed large fluctuations in silence density, with low and high values associated to desynchronized and synchronized cortical states, respectively (Figure 5A). We found that differences in collective dynamics in different epochs, quantified by $D_{JS}(t,t^{′})=D_{JS}(P_{data,t};P_{data,t^{′}})$, significantly co-varied with the changes in cortical state, given by $d=|CS(t)−CS(t^{′})|$ (averaged correlation coefficient 0.56 ± 0.08, p < 0.001) (Figure 5B–C). Thus, changes in collective behavior correlated with changes in cortical state.

![Figure 5.](https://cdn.elifesciences.org/articles/53268/elife-53268-fig5-v2.jpg)

**Figure 5.:** (A) Silence density was used to characterize the cortical state. Green inset: low values of the silence density indicate desynchronized cortical states (each row represents the spike train of a single-unit). Red inset: high values of the silence density indicate synchronized cortical states. Data from rat 1. (B) Difference in collective pattern statistics, that is DJS, between different epochs, $t$ and $t'$, as a function of the corresponding difference in silence density, noted d. Each gray dot corresponds to a pair of epochs ($t,t'$). The solid line indicates the average relation between DJS and d; error bars indicate SD. Data from all neuronal ensembles from rat 1. (C) Correlation coefficient between DJS and d, for all rats. *: p < 0.001. (D) Top: Distribution of the absolute value of the correlations between the cortical state and the activity observables, noted $r_{cs}$. Bottom: Distribution of parameter sensitivity values for biases (h parameters) and couplings (J parameters), for all models from all rats. (E) $r_{cs}$ vs. sensitivity $s$ of all activity variables (i.e., firing rates and pairwise correlations). Correlation: $r_{c}$ = 0.36; p <0.001. Data from rat 4 ($N_{pop}$ = 72). (F) Correlation between $r_{cs}$ and the sensitivity for each dataset. *: p < 0.001. Error bars indicate correlation 95% confidence interval. (G) $r_{cs}$ for sloppy and stiff variables. *: p < 0.001, paired t-test. Error bars indicate SEM.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/53268/elife-53268-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Averaged correlation between observables and cortical state, $r_{cs}$, for sloppy and stiff variables, for weighted sensitivity $s^{w}$ defined using equation 9. *: p < 0.001, paired t-test. Error bars indicate SEM.

We next asked which activity observables, that is the firing rate of each neuron and all pairwise correlations, related more to cortical state transitions. For this, we calculated the absolute correlation, $r_{cs}$, between the cortical state $CS(t)$ and the activity observables. We found that $r_{cs}$ was broadly distributed between 0 and 0.94, thus some observables correlated more with the cortical state (Figure 5D, top panel). Next, to relate the sensitivity of model parameters (their stiffness) to the activity observables, we measured the sensitivity of a given parameter by its average contribution to the first eigenvector of the FIM and we associated it to the corresponding observable (Panas et al., 2015). We defined the sensitivity $s_{ne}$ at the neuronal ensemble level and the sensitivity $s$ at the population level (see Materials and methods). Note that the ranges of the sensitivity of biases ($h$) and couplings ($J$) were similar (Figure 5D, bottom panel), and that sensitivities calculated in the first and the second halves of the recording session were highly correlated (correlation coefficient > 0.82, for all rats; average: 0.89 ± 0.03). We found a significant positive correlation between the associated sensitivity ($s$) and the correlation with the cortical state ($r_{cs}$) in 5/6 datasets (Figure 5E–F). Thus, the observables that correlated more with the cortical state were those with the highest associated sensitivity. This result led us to separate the activity observables into two classes, called 'sloppy' and 'stiff', based on whether the associated sensitivity ($s$) was lower or higher than the median of $s$. We found that stiff variables were significantly more correlated with the cortical state than the sloppy variables (p<0.01 for all datasets, paired t-test; Figure 5G). This relationship was preserved when using an alternative, more general definition of sensitivity that considered the contribution to all eigenvectors of the FIM, instead of the contribution to the first eigenvector only (see Figure 5—figure supplement 1). Altogether, these results indicate that neuronal activity and co-activity preferentially evolved along sensitive (stiff) parameter dimensions during cortical state transitions.

### Sensory-evoked activity evolves along sloppy dimensions

The above results indicate that, although intrinsic spontaneous dynamics predominantly evolved along sloppy dimensions (Figure 4F), cortical state transitions were governed by changes in stiff parameters (Figure 5G). We next investigated which parameter dimensions were explored when the neural network was driven by external sensory inputs, that is during stimulus-evoked activity (Figure 6A). We observed that evoked responses (which could be increased or decreased with respect to pre-stimulus baseline firing rate) were larger for sloppy neurons than for stiff neurons (Figure 6B–C). To quantify the responsiveness of each neuron, we calculated the modulation index (MI, see Materials and methods) of each neuron in response to acoustic stimuli. We next calculated the relation between MI, calculated during evoked activity, and the sensitivity $s$ associated to firing rates, calculated during the spontaneous activity as above. We found that the more responsive neurons were those with the lowest associated sensitivity (Figure 6D–E). This indicates that stimulus-evoked neuronal activity evolved mostly along sloppy dimensions. This result was replicated when using a more general definition of sensitivity that considered the contribution to all eigenvectors of the FIM (see Figure 6—figure supplement 1A). Finally, we evaluated the difference, noted ΔMI, between the MI of sloppy and stiff neurons as a function of cortical state $CS(t)$. Specifically, first, the MI values in each epoch were averaged according to different ranges of the silence density. Second, the MI values of sloppy and stiff neurons were compared within each range. We found that ΔMI was maximal during desynchronized activity, and minimal during synchronized activity (Figure 6F, see also Figure 6—figure supplement 1B). Thus, the cortical activity during stimulus response evolved predominantly along sloppy dimensions for the desynchronized cortical state, while, in the synchronized state, the dominance of sloppy fluctuations was reduced, and stiff fluctuations became comparable.

![Figure 6.](https://cdn.elifesciences.org/articles/53268/elife-53268-fig6-v2.jpg)

**Figure 6.:** (A) Population responses to acoustic clicks. (B–C) Median-split of sensitivity $s$ was used to separate stiff neurons and sloppy neurons. The mean responses for stiff and sloppy neurons are shown in the case of excited responses (B) and suppressed responses (C). The responses were normalized by the average pre-stimulus activity $r_{0}$. Shaded areas correspond to SEM. Data in (A), (B), and (C) correspond to one example rat (#1). (D) Modulation index (MI) as a function of associated sensitivity of firing rates ($s_{i}$, with 1 $\leqi\leqN_{pop}$), for each dataset. Each dot corresponds to a single neuron of the recorded population. The correlation between MI and sensitivity was negative for all datasets ($r_{c}$: correlation coefficient; p: p-value). Solid lines indicate exponential fits. (E) Correlation between MI(t), calculated in epoch $t$, and $ν_{t,1}$, for all neuronal ensembles of each of the rats. On each box, the central mark indicates the median, and the bottom and top edges of the box indicate the 25th and 75th percentiles, respectively. Asterisks indicate significantly negative medians (p < 0.001, two-sided signed rank test). (F) Difference of the MI of sloppy neurons minus the MI of stiff neurons as a function of cortical state (i.e., silence density), averaged for all rats (black trace; error bars indicate SEM). The gray bars indicate the distribution of silence density values.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/53268/elife-53268-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Modulation index (MI) as a function of associated weighted sensitivity of firing rates, for each dataset. The correlation between MI and $s^{w}$ was negative for all datasets ($r_{c}$: correlation coefficient; p: p-value). Solid lines indicate exponential fits. (B) Difference of the MI of sloppy neurons minus the MI of stiff neurons as a function of cortical state (i.e., silence density), averaged for all rats (black trace; error bars indicate SEM). The gray bars indicate the distribution of silence density values.

Finally, correlations between cortical state fluctuations and sensitivity and between MI and sensitivity could reflect a dependency between sensitivity and model estimation errors. To test this, we evaluated the mean error on the model estimation of the observables and test its interaction with sensitivity, cortical state fluctuations, and MI (see Appendix 1 and Appendix 1—figure 1). We found that model estimation errors correlated with sensitivity, but they could not fully explain neither the positive correlation between sensitivity and cortical state nor the negative correlation between sensitivity and MI.

### Stiff parameters were associated to central neurons within the neuronal network

In this section, we further investigate the properties of neurons and pairs of neurons with respect to their associated parameter sensitivity. As above, we separated the neurons and pairs of neurons into two classes, called 'sloppy units/pairs' and 'stiff units/pairs', based on whether the associated sensitivity ($s$) was lower or higher than the median $s$ (units were associated to parameters $h_{i}$, and pairs or links were associated to parameters $J_{ij}$). With this dichotomization, we found that stiff units were significantly more active than sloppy units (Figure 7A). We quantified this by performing receiver operating characteristic (ROC) analysis and used the area under the ROC curve (AUC) as a measure of how well the firing rates distributions of the two classes were separated (AUC = 0.961–0.998, p < 0.001, for all rats; Figure 7G). Stiff neurons were also significantly more correlated among them than sloppy neurons (AUC = 0.615–0.932, p < 0.001, for all rats; Figure 7B,G). The distributions of correlations remained well separated when calculated for the links, that is pairs of neurons with associated parameters $J_{ij}$ (AUC = 0.541–0.766, p < 0.001, for all rats; Figure 7C,G).

![Figure 7.](https://cdn.elifesciences.org/articles/53268/elife-53268-fig7-v2.jpg)

**Figure 7.:** (A) Distribution of firing rates of sloppy and stiff neurons. (B) Distribution of correlations among sloppy neurons and among stiff neurons. (C) The distribution of correlations was also calculated for the links (i.e, pairs of neurons with associated parameters $J_{ij}$). Note that, in principle, links can be related to pairs composed of one sloppy and one stiff neuron. (D) Distribution of betweenness centrality of sloppy and stiff neurons. (E) Connectivity graph: each node represents a neuron and links represent significant correlations between pairs of neurons. The graph was plotted using force-directed layout, that is using attractive forces between strongly connected nodes and repulsive forces between weakly connected nodes. Left: the nodes were colored as a function of betweenness centrality. Right: the nodes were colored as a function of associated sensitivity $s$. Note the high overlap between both color labeling methods, indicating that sensitivity was highly predictive of the centrality of the nodes. (F) Distribution of neuron-to-population couplings of sloppy and stiff units. Panels A–F show data from rat 1. (G) Area under the receiver operating curve (AUC) quantifying the separation of distributions of sloppy and stiff classes. All AUC values were significantly higher than 0.5 (p < 0.001).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/53268/elife-53268-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Area under the receiver operating curve (AUC) quantifying the separation of distributions of sloppy and stiff classes using the weighted sensitivity $s^{w}$ defined using equation 9. All AUC values were significantly higher than 0.5 (p < 0.001).

To further investigate the structure of correlations, we evaluated the centrality of stiff and sloppy neurons within the observed network of neurons. For this we used the betweenness centrality (BC), a measure of node centrality in a graph or network, which in our case was given by the functional connectivity matrix among the recorded neurons (see Materials and methods). The BC measures the extent to which a node in the graph tends to lay on the shortest path between other nodes. Thus, a node with higher BC has more influence over the network, because more information passes through that node. We found that stiff neurons had significantly more centrality in the functional connectivity graph than sloppy neurons (AUC = 0.740–0.831, p<0.001, for all rats; Figure 7D,G). This indicates that stiff neurons were part of the core of the graph, while sloppy neurons were part of the graph periphery, as clearly shown using graph visualization (Figure 7E; Fruchterman and Reingold, 1991). BC values were correlated with firing rates (correlation coefficient: 0.59 ± 0.11), which could suggest that differences in BC between stiff and sloppy neurons were simply a consequence of differences in firing rates. However, using surrogate data that preserved the observed firing rates and produced correlations through global modulations, we found that neither the structure of correlations nor the BC values could be trivially predicted by globally modulated firing rates but they were rather suggestive of functional interactions (see Appendix 1 and Appendix 1—figure 2). Thus, in addition to different firing rates, different correlations and BC values were supplementary features of stiff and sloppy neurons.

Moreover, previous work has shown that cortical neurons differ in their coupling to the population activity, with neurons that activate most often when many others are active and neurons that tend to activate more frequently when others are silent (Okun et al., 2015). Thus, along with centrality, we calculated the neuron-to-population coupling, given by the Pearson correlation between the activity of each neuron $i$ and the number of coactive neurons (excluding neuron $i$; see Materials and methods). We found that stiff neurons were significantly more coupled to the population activity than sloppy neurons (AUC = 0.603–0.939, p < 0.001, for all rats; Figure 7F,G). In summary, stiff units were more active, more central, more coupled among them, and more coupled to the population activity than sloppy units. The same results were found when using a more general definition of sensitivity that considered the contribution to all eigenvectors of the FIM (Figure 7—figure supplement 1).

## Discussion

We here studied the changes in activity caused by intrinsic (i.e. cortical state) and extrinsic (i.e., stimulus-evoked) sources in A1 neuronal ensembles in an estimated parameter space. The parameter space was obtained using the maximum entropy principle, providing a handful number of parameters describing the probability of all possible binary activity patterns. These parameters differed in their impact on collective activity that was sensitive to a few combinations of parameters, called stiff dimensions, but insensitive to many others called sloppy dimensions. Our results suggest that spontaneous cortical state transitions and stimulus-driven activity evolved along different parameter dimensions. Indeed, in one hand, while most of the fluctuations during spontaneous activity evolved along sloppy dimensions, some residual ongoing fluctuations evolved along stiff dimensions, and these fluctuations were correlated with synchronized/desynchronized cortical state transitions. On the other hand, stimulus-induced activity was larger in sloppy dimensions than in stiff dimensions, an effect that was most prominent during the desynchronized cortical state. Note that the observation that both spontaneous and stimulus-driven activities predominantly evolve along sloppy dimensions results from the strong similarity of spontaneous and evoked activity, reported in several previous studies (Arieli et al., 1996; Kenet et al., 2003; MacLean et al., 2005; Luczak et al., 2009). Finally, by classifying the neurons as stiff versus sloppy neurons (i.e., those contributing more or less to the principal stiff dimension) we found that the firing rates and the functional connectivity topology significantly differed between the two classes of neurons. It should be noted, however, that, since sensitivity is a continuous variable, the two classes of neurons that we defined here do not represent two disjoint groups but rather represent two parts of a continuum.

The observation that stimulus-induced activity evolved along sloppy dimensions can have important functional implications. It suggests that a stimulus can modulate the activity of a subset of sloppy neurons without entirely affecting the collective activity. This could be an efficient functional architecture to encode sensory information without perturbing other ongoing or memory-stored processes. Consistent with this view and with previous studies (Margolis et al., 2012; Mizuseki and Buzsáki, 2013; Panas et al., 2015), our results suggest that the integrity of the network is ensured by a core of highly active stiff neurons, which have strong functional connections among them (either through anatomical connections or common inputs), while topologically peripheral sloppy neurons (within the functional connectivity graph) can be largely modulated by external inputs. A similar sub-network of highly active, interconnected neurons has been recently identified in the mice neocortex (Yassin et al., 2010). Importantly, sensory input was not required to drive these cells. Previous studies of complex systems have derived general principles of core/periphery network structures: the network periphery is more variable, evolvable, and plastic than the network core, while the network core facilitates system robustness (Kitano, 2004; Csermely et al., 2013). Thus, we hypothesize that sloppy neurons could also be more affected by synaptic plasticity, allowing for network reconfiguration without loss of stability. Consistent with this, previous work on whole-brain fMRI has observed core stability and peripheral flexibility over the course of learning (Bassett et al., 2013), and recent analyses of functional networks from calcium imaging data recorded in mouse primary auditory cortex revealed a stable core and a variable periphery over time (Betzel et al., 2019). Furthermore, we observed that stimulus responses evolved more pronouncedly along sloppy dimensions in the desynchronized state, while in the synchronized state fluctuations along sloppy and stiff dimensions were comparable (Figure 6F). This supports the view that responses along sloppy dimensions provide information processing benefits, since previous studies have shown that auditory stimuli in rodents (Marguet and Harris, 2011; Pachitariu et al., 2015) and visual stimuli in both rats (Goard and Dan, 2009) and monkeys (Beaman et al., 2017) are better represented in the desynchronized state as compared to the synchronized state.

The properties of spontaneous and induced cortical dynamics observed in the present anesthetized condition are likely to be relevant also during wakefulness. Indeed, several studies reported the existence of synchronized cortical states during wakefulness (for review see Zagha and McCormick, 2014), and global fluctuation resembling transitions between up and down periods during alert or quiescent wakefulness (Petersen et al., 2003; Luczak et al., 2007; Poulet and Petersen, 2008; Zagha et al., 2013; Tan et al., 2014; Engel et al., 2016) or even during task engagement (Sachidhanandam et al., 2013). Moreover, sloppiness has been observed in asynchronous spontaneous activity under light anesthesia (Panas et al., 2015), we thus expect to observe a similar stiff-sloppy architecture in the awake state. However, we believe that the comparison of Fisher information matrices during wakefulness and during different levels of anesthesia could provide valuable information about the principles governing vigilance.

We found that stiff neurons were more linked to the observed neuronal population activity than sloppy neurons. Stiff neurons had higher centrality in the functional connectivity graph and higher coupling to the population activity than sloppy neurons. Previous research showed that neurons differ in their coupling to the population activity, with neurons that activate most often when many others are active, called ‘choristers’, and neurons that tend to activate more frequently when others are silent, called ‘soloists’ (Okun et al., 2015). Our results suggest that stiff and sloppy neurons are chorister and soloist neurons, respectively. In other words, changes in the activity of stiff/chorister neurons lead to changes in collective behavior (i.e., cortical states), while the activity of sloppy/soloist neurons can spontaneously fluctuate or respond to stimuli without strongly affecting the collective behavior. Thus, we believe that the roles of stiff/chorister neurons and sloppy/soloist neurons are important to understand tradeoffs between responsiveness and stability of the network. Furthermore, we here studied the evolution of neuronal activity on the time scale of hours and found that fluctuations on stiff parameter dimensions were the weakest and were related to cortical state transitions, which time scale is in the order of tens of minutes (Hahn et al., 2017; Mochol et al., 2015). Previous studies have reported prominent changes on neuronal activity and tuning properties over days, but with stable decoding performances of population activity (Chestek et al., 2007; Ziv et al., 2013; Panas et al., 2015). However, we hypothesize that learning or adaptation to changing environments could lead to large changes in collective activity. In that case, particular attention could be paid to the influence of high-order areas on the activity of subsets of stiff and sloppy neurons from sensory areas, as top-down regulation might be a mechanism to control the stabilizing network core.

The existence of cortical neurons with different sensitivities (from sloppy to stiff neurons) provides new valuable architectural constrains for models of the brain state and its transitions. Several past studies have modeled the synchronized brain dynamics as transitions between two attractors. Depending on the model specificity those transitions could be noise driven (Mejias et al., 2010; Mochol et al., 2015; Jercog et al., 2017) or caused by some fatigue mechanism (Compte et al., 2003; Hill and Tononi, 2005; Mattia and Sanchez-Vives, 2012). To make the system works in a desynchronized regime it was enough to increase the background input to the network (Bazhenov et al., 2002; Hill and Tononi, 2005; Curto et al., 2009; Destexhe, 2009; Mochol et al., 2015). Given our present results, the models could be extended to include a network core/periphery architecture, a non-homogeneous background input preferentially targeting the network core, and different stimulus spatial distributions. Such a model would provide insights on the interplay between cortical state transitions and sensory representation. Moreover, our findings question the view that the mechanisms by which background and stimulus inputs impact the dynamics are similar, as assumed in the simple bi-stable rate model (Mochol et al., 2015).

Finally, we here described the patterned activity of small ($N$ = 10) neuronal ensembles using MEMs. It is known that MEMs of small sizes can present departures from the observed distribution of summed activities and higher-order correlations (Tkačik et al., 2014). Recent advancements on learning algorithms allow to construct MEMs of ∼100 neurons. However, these models cannot be used in a time-resolved manner, as we did here, due to limited data in each epoch. Small model sizes are thus the cost to pay to study the evolution of collective activity over time in a meaningful time scale (i.e., the one of cortical state transitions).

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
      <td>Biological sample (Sprague–Dawley rat)</td>
      <td>Sprague–Dawley rat</td>
      <td>https://doi.org/10.1073/pnas.1410509112</td>
      <td></td>
      <td>six rats, 250–400 g</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Matlab</td>
      <td>MathWorks</td>
      <td>RRID:SCR_001622</td>
      <td>All analyses</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Klustakwik</td>
      <td>http://klustakwik.sourceforge.net/</td>
      <td>RRID:SCR_014480</td>
      <td>Spike sorting (detection and initial clustering)</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>EToS</td>
      <td>http://etos.sourceforge.net/</td>
      <td></td>
      <td>Spike sorting (detection and initial clustering)</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Klusters</td>
      <td>http://neurosuite.sourceforge.net/</td>
      <td></td>
      <td>Spike sorting (clustering)</td>
    </tr>
  </tbody>
</table>

### Ethics statement

All experiments were carried out in accordance with protocols approved by the Animal Ethics Committee of the University of Barcelona (Comité d’Experimentació Animal, Universitat de Barcelona, Ref 116/13).

### Experimental techniques

We analyzed the neuronal activity recorded in the primary auditory cortex (A1) of 6 anesthetized rats (Sprague–Dawley; 250–400 g). The experimental procedures and spikes sorting procedures have been previously described in Mochol et al. (2015). Briefly, rats were anesthetized with urethane (1.5 g/kg body weight) and silicon microelectrodes (Neuronexus) with 32 or 64 channels were inserted in deep layers (depth, 600–1,200 μm) of the primary auditory cortex. The spiking activity from single units and multi-units (i.e., neurons that were not well isolated) was simultaneously recorded during spontaneous activity and in response to acoustic ‘clicks’ (5 ms square pulses; interstimulus interval, 2.5 or 3.5 s; see Table 1). In some datasets, double clicks (5 ms square pulses; 50- or 100 ms inter-click interval) were also presented, but, in the present study, we analyzed only the responses to single click. The spiking data is publicly available here: https://github.com/adrianponce/Spont_stim_spiking_A1.

**Table 1.**
 Number of neurons (SU: single-units, MU: multi-unit), number of 100 s epochs, number of stimulus presentations in 100 s epochs, and number of neuronal ensembles, for each dataset.


<table>
  <thead>
    <tr>
      <th></th>
      <th>No. of neurons</th>
      <th>No. of 100 s epochs</th>
      <th>Stimulus presentations in 100 s epochs</th>
      <th>No. of neuronal ensembles (Q)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Rat 1</td>
      <td>SU: 81; MU: 3</td>
      <td>163</td>
      <td>12–14</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Rat 2</td>
      <td>SU: 147; MU: 13</td>
      <td>74</td>
      <td>12–14</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Rat 3</td>
      <td>SU: 44; MU: 30</td>
      <td>70</td>
      <td>12–20</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Rat 4</td>
      <td>SU: 72; MU: 103</td>
      <td>59</td>
      <td>10–20</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Rat 5</td>
      <td>SU: 58; MU: 39</td>
      <td>29</td>
      <td>28–29</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Rat 6</td>
      <td>SU: 112; MU: 83</td>
      <td>28</td>
      <td>17–29</td>
      <td>20</td>
    </tr>
  </tbody>
</table>

### Cortical state

Long continuous recordings (mean, ∼2 h) were divided into $N_{E}$ 100-s epochs, and cortical state was estimated in each epoch based on spontaneous pooled population activity, that is the merge of single and multiunit spike trains during the 1.5-s intervals preceding each stimulus presentation. Cortical state was quantified using silence density defined as the fraction of 20-ms time bins with no population activity. Silent and active periods were obtained from the merge of consecutive empty and nonempty bins, respectively.

### Maximum entropy models

The spontaneous spiking activity of ensembles of $N$ single neurons was studied using statistical modeling based on maximum entropy principle. The ensemble activity was binarized in non-overlapping time bins of dt = 10 ms, during which neuron i either did ($\sigma_{i}=+1$) or did not ($\sigma_{i}=-1$) generate one or more spikes. The state of the neural ensemble is described by a binary pattern $\sigma→=\sigma_{1},\sigma_{2},…,\sigma_{N}$, and thus the collective activity is described by the probability distribution $P\sigma→$ over all 2N possible binary patterns. We estimated $P\sigma→$ using a Maximum entropy model (MEM). The MEM finds $P\sigma→$ by maximizing its entropy under the constraint that some empirical statistics are preserved. A pairwise-MEM provides a solution under the constraint that the activation rates ($<\sigma_{i}>$) and the pairwise correlations ($<\sigma_{i}\sigma_{j}>$) are preserved. The maximum entropy distribution $P\sigma→$ that is consistent with these expectation values is given by the Boltzmann distribution (Schneidman et al., 2006; Tkačik et al., 2015):

$$
P(\sigma→)=\frac{e^{−E( \sigma→ )}}{\sum{\sigma→}e^{−E( \sigma→ )}},
$$

where $E\sigma→$ is the energy of the pattern $\sigma→$, given by:

$$
E(\sigma→)=−\sumi=1Nh_{i}\sigma_{i}−\frac{1}{2}\sumi=1N\sumj=1NJ_{ij}\sigma_{i}\sigma_{j},
$$

and $Z=\sum{\sigma→}e^{−E( \sigma→ )}$ is the partition function.

The model parameter $h_{i}$, called intrinsic bias, represents the intrinsic tendency of neuron i towards activation ($\sigma_{i}=+1$) or silence ($\sigma_{i}=-1$) and the parameter $J_{ij}$ represents the effective interaction between neurons i and j. The estimation of the model parameters $Ω={h,J}$ was achieved through a gradient descent algorithm (see below). For each recording session, we constructed models for $Q$ ensembles of $N=10$ randomly selected single neurons from the entire population of $N_{pop}$ single neurons and learned the model parameters using the spontaneous binarized activity within each 100-s epoch. Thus, for each recording session, we built $Q\timesN_{E}$ models of 10 units. We were interested on the evolution of the model parameters over time, that is $Ω(t)$. Note that, for a given model, the number of free parameters is the sum of intrinsic biases and effective couplings, $N+N(N-1)/2=$ 55, that is $Ω=[h_{1}, h_{2}, …, h_{N},J_{12}, J_{13},…]$.

### Estimation of MEM parameters

The MEM parameters $Ω={h,J}$ were iteratively adjusted to minimize the absolute difference between the empirical activation rates ($\sigma_{i}$) and correlations ($\sigma_{i}\sigma_{j}$) and those ($\sigma_{i}_{model}$, $\sigma_{i}\sigma_{j}_{model}$) predicted by the model through Metropolis Monte Carlo simulations (100,000 samples). Specifically, each iteration is given by: $h_{i}^{new}=h_{i}^{old}-\alpha\sigma_{i}_{model}-\sigma_{i}$, and $J_{ij}^{new}=J_{ij}^{old}-\alpha\sigma_{i}\sigma_{j}_{model}-\sigma_{i}\sigma_{j}$, where α is the learning rate ($\alpha=$ 0.1). In our study we stopped the re-estimations once the differences between the empirical and model values are less than a tolerance threshold (0.005) or if this tolerance was not reached within a maximum number of iterations (100).

### MEM goodness-of-fit

The goodness-of-fit of the MEMs was evaluated using the Jensen–Shannon divergence (DJS) between the probability distribution of the empirical and model binary patterns (Marre et al., 2009). DJS is a symmetric version of the Kullback-Leibler divergence (DKL) and is given as:

$$
D_{JS}(P_{data};P_{MEM})=\frac{1}{2}D_{KL}[P_{data};\frac{(P_{data}+P_{MEM})}{2}]+\frac{1}{2}D_{KL}[P_{MEM};\frac{(P_{data}+P_{MEM})}{2}],
$$

Where $P_{MEM}$ was given by the Boltzmann distribution of the model, $P_{data}$ was estimated from the $N$-dimensional binary patterns observed in the data, and:

$$
D_{KL}(P_{1};P_{2})=\sum{x}P_{1}(x)log⁡\frac{P_{1}(x)}{P_{2}(x)}.
$$

The fitting of MEM (second-order model) was compared to the fit obtained using independent-MEM, that is in which only for which only the activation rates ($<\sigma_{i}>$) are preserved (i.e., only $h$ is optimized; first-order model). In this case, the pattern energy is given by: $E\sigma→=-\sumi=1Nh_{i}\sigma_{i}$.

Furthermore, the performance of the model can be evaluated using the Kullback-Leibler ratio, $R$ (Shlens et al., 2009). This ratio is given by comparing the Kullback-Leibler divergence between the distribution $P_{1}$ of the first-order model (i.e., independent-MEM) and the distribution of the actual data, $D_{1}=D_{KL}P_{1};P_{data}$, with the Kullback-Leibler divergence between the distribution $P_{2}$ of the second-order model and the distribution of the actual data, $D_{2}=D_{KL}P_{2};P_{data}$. Specifically, the Kullback-Leibler ratio is defined as:

$$
R=\frac{D_{1}−D_{2}}{D_{1}}.
$$

This ratio can range between 0 and 1, with one giving the highest performance.

### Fisher information matrix

Because in the MEM, all the information about the collective activity is contained in the probability distribution of the binary patterns, $P\sigma→$, one can define the model parameter space as $P(\sigma→|Ω)$. We were interested in knowing which parameters, or combination of parameters, have a strong effect on the collective activity. To measure how distinguishable two models, with parameters $Ω$ and $Ω+\deltaΩ$, are based on their predictions, we used the Fisher information matrix (FIM). Indeed, the Kullback-Leibler divergence between the two models can be written as:

$$
D_{KL}(Ω;Ω+\deltaΩ)=FIM_{kl}\deltaΩ_{k}\deltaΩ_{l}+𝒪(\deltaΩ^{3}),
$$

where 1 $\leqk,l\leq$ 55, and the matrix $FIM$ is given by:

$$
FIM_{kl}=\sum{\sigma→}P(\sigma→|Ω)\frac{∂log⁡P(\sigma→|Ω)}{∂Ω_{k}}\frac{∂log⁡P(\sigma→|Ω)}{∂Ω_{l}}.
$$

The FIM represents the curvature of the log-likelihood of the model, $log⁡P(\sigma→|Ω)$, with respect to the model parameters. It quantifies the sensitivity of the model to changes in parameters. By calculating the eigenvalues of the FIM, we can determine which combinations of parameters affect the most the model's behavior.

In the case of MEM, the FIM can be easily obtained by using Equations 1, 2, and 7. As a result, the FIM is given by the covariance matrix of observables associated to the parameters which can be calculated from the model through Metropolis Monte Carlo simulations (500,000 steps), that is:

$$
FIM_{kl}=⟨x_{k}x_{l}⟩−⟨x_{k}⟩⟨x_{l}⟩,
$$

with 1 $\leqk,l\leq$ 55 and $x→=[\sigma_{1}, \sigma_{2}, …, \sigma_{N}, \sigma_{1}\sigma_{2}, \sigma_{1}\sigma_{3},…]$.

### Sensitivity measures

The FIM was calculated for every neuronal ensemble at every 100-s epoch and it was decomposed into eigenvectors, noted $ν_{t,1},ν_{t,2},…,ν_{t,k},…$, where $k$ is the rank of the eigenvector and $t$ denotes the epoch. Following Panas et al. (2015), within each neuronal ensemble, we measured the sensitivity of a given parameter by its averaged contribution to the first eigenvector of the FIM, that is the sensitivity of i-th parameter is given by $s_{ne,i}=\frac{1}{N_{E}}\sum_{t}ν_{t,1}(i)$, with $1\leqi\leqN$.

We next constructed a sensitivity measure for the entire population of $N_{pop}$ neurons. For this, we defined the set of all single neuron indices and all pairs of neurons $I=1,…,N_{pop},1,2,1,3,…$. This set has $L=N_{pop}+\frac{N_{pop}(N_{pop}-1)}{2}$ elements. For each element $j$ of $I$, we defined the sensitivity $s_{j}$ as the average of $s_{en,i}$ over the neuronal ensembles that contained the $j$-th single neuron or the pair of neurons (i.e., those neuronal ensembles for which $i$ maps to $j$). In other words, $s_{ne}$ denotes the sensitivity within an ensemble of $N=10$ neurons and has 55 elements, and $s$ denotes the sensitivity within the entire population of $N_{pop}$ neurons and has $L$ elements. This allows comparison of $s$ with statistics derived from the population of $N_{pop}$ neurons.

Parameters that contributed less to the first eigenvector could in principle contribute to the other stiff dimensions (those with lower rank $k$, e.g., $k=$ 2). For this reason, we also considered an alternative definition of sensitivity that considers the weighted contribution to all eigenvectors of the FIM. For each neuronal ensemble and each 100-s epoch $t$, we defined the weighted sensitivity of the parameter $i$ as the temporal average of its contribution to the eigenvectors of the FIM, weighted by the associated eigenvalues ($a_{t,1},…,a_{t,55}$):

$$
s_{ne,i}^{w}=\frac{1}{N_{E}}\sumt=1N_{E}\sumk=155\frac{a_{t,k}|ν_{t,k}(i)|}{a_{t,1}+a_{t,2}+… +a_{t,55}}.
$$

As previous, from $s_{ne}^{w}$ one can construct a weighted sensitivity $s^{w}$ at the population level.

Finally, we separated the activity observables into two classes, called “sloppy” and “stiff”, based on whether the associated sensitivity $s$ was lower or higher than the median sensitivity.

### Similarity measures

Temporal variations of model parameters and data statistics were quantified using the average correlation between the parameters/statistics at time t and the parameters/statistics at time $t+Δt$. For example, let $r→(t)$ the average firing rates of the neurons during the epoch $t$, the similarity measure is given by:

$$
\gamma(Δt)=\frac{1}{N_{E}−Δt}\sumt=1N_{E}−Δtρ[r→(t),r→(t+Δt)],
$$

Where $N_{E}$ is the number of epochs and $ρ$ is the Pearson correlation coefficient. In the case of FIM, the matrix was vectorized to calculate $ρ$.

To evaluated how well the data in a given epoch $t$ could be explained by the MEM constructed using the data at time $t+Δt$. Specifically, we defined the similarity measure $D_{JS}Δt$, given by the average Jensen-Shannon divergence between the distribution of data binary patterns in epoch $t$, that is $P_{data, t}$, and the distribution of binary patterns predicted by the MEM constructed using the data in epoch $t+Δt$, that is $P_{MEM,t+Δt}$. This measure is given as:

$$
⟨D_{JS}⟩(Δt)= \frac{1}{N_{E}−Δt}\sumt=1N_{E}−ΔtD_{JS}(P_{data,t};P_{MEM,t+Δt}).
$$

In other words, $1/D_{JS}Δt$ quantifies how well, on average, the model with parameters $Ω(t+Δt)$ represents the data from epoch $t$.

### Modulation index

We quantified the responsiveness of the neurons to sensory stimuli through the modulation index (MI) defined as:

$$
MI= \frac{|r_{stim}−r_{spon}|}{r_{stim}+r_{spon}},
$$

where $r_{spon}$ is the pre-stimulus average spike count, calculated in the 0.5-s pre-stimulus interval, and $r_{stim}$ is the average spike count calculated from stimulus onset to 0.5 s after stimulus onset. With this definition, strongly increased or suppressed stimulus responses, with respect to pre-stimulus activity, lead to high MI values.

### Betweenness centrality

For each recording session, we analyzed the network defined by the Pearson correlation matrix of the activities of all single units. The centrality of a neuron, or node, within the network was quantified using the betweenness centrality (BC) measure. BC is given by the number of shortest paths that pass through a given node. The correlation matrix was compute for all 100-s epochs and, for each matrix element, we tested whether the mean of the $N_{E}$ correlation values differs from 0 (t test followed by Bonferroni correction), resulting in a binary graph $G$ with entries equal to 1 if correlation were significantly different from zero (corrected p-value < 0.05) and 0 otherwise. The BC for each node of the graph was given by:

$$
BC(i)=\sumk\neqi\neql\frac{p(kl;i)}{p(kl)}
$$

where $p(kl)$ is the total number of shortest paths from node $k$ to node $l$ and $p(kl;i)$ is the number of those paths that pass through $i$.

### Neuron-to-population coupling

To quantify the coupling of each neuron to the activity of the neuronal population, we calculated, for each epoch, the Pearson correlation between the activity of each neuron ($\sigma_{i}$) and the number of coactive neurons (i.e., with $\sigma_{i}=+1$) at each time bin ($dt$ = 10 ms) from the neuronal population of single units (without including the neuron $i$). The neuron-to-population coupling was given by the average of the correlation coefficient across epochs.

### ROC analysis

We used the receiver operating characteristic curve (ROC) to evaluate the separation between the distributions of observables from sloppy and stiff classes. Let $X_{sloppy}$ and $X_{stiff}$ be the sloppy variables, that is those variables with associated sensitivity ($s$) lower than the median $s$, and the stiff variables, that is those variables with associated sensitivity ($s$) higher than the median $s$, respectively. The ROC curve, $f(c)$, is build by plotting the probability of $P(X_{sloppy}>c)$ against the probability of $P(X_{stiff}>c)$, for each all $c$. The area under the ROC curve (AUC) is a measure of separation between $P(X_{sloppy})$ and $P(X_{stiff})$, and it is given by:

$$
AUC= \intf(c)dc.
$$

AUC ranges between 0 and 1, with AUC = 0 if $P(X_{sloppy})$ and $P(X_{stiff})$ are completely separated and $X_{sloppy}>X_{stiff}$, AUC = 1 if $P(X_{sloppy})$ and $P(X_{stiff})$ are completely separated and $X_{stiff}>X_{sloppy}$, and AUC = 0.5 if $P(X_{sloppy})$ and $P(X_{stiff})$ are undistinguishable. We used a permutation test (1000 re-samples), in which observables and classes were randomly associated, to assess AUC values that were significantly different from 0.5.

### Stationary surrogates

To construct the stationary surrogates we first randomly selected a reference epoch $t$. Second, we generated binary data using the MEM estimated from the spiking data at this reference epoch, that isusing parameters $Ω(t)$, through Monte Carlo simulations of the model to obtain 5000 binary patterns. Third, we repeated the Monte Carlo simulations $N_{E}$ times. Finally, for each of the $N_{E}$ pieces of surrogate data, we estimated new MEM parameters, $Ω^{′}$, using gradient descend, and we calculated the corresponding Fisher Information Matrix (FIM) using 500,000 Monte Carlo steps as described above. By construction, the obtained surrogate data were stationary and had the same length of the original spiking data. Thus, parameter fluctuations in the surrogate data were only due to model estimation errors.
