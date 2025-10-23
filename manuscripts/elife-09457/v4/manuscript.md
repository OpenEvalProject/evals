# Unified pre- and postsynaptic long-term plasticity enables reliable and flexible learning

## Authors

- Rui Ponte Costa<sup>1</sup> ([ORCID: 0000-0003-2595-2027](https://orcid.org/0000-0003-2595-2027)) †
- Robert C Froemke<sup>5</sup>
- P Jesper Sjöström<sup>3</sup> ([ORCID: 0000-0001-7085-2223](https://orcid.org/0000-0001-7085-2223))
- Mark CW van Rossum<sup>1</sup> ([ORCID: 0000-0001-6525-6814](https://orcid.org/0000-0001-6525-6814))

### Affiliations

1. Institute for Adaptive and Neural Computation, School of Informatics University of Edinburgh Edinburgh United Kingdom
2. Neuroinformatics Doctoral Training Centre, School of Informatics University of Edinburgh Edinburgh United Kingdom
3. The Research Institute of the McGill University Health Centre, Department of Neurology and Neurosurgery McGill University Montreal Canada
4. Centre for Neural Circuits and Behaviour University of Oxford Oxford United Kingdom
5. Skirball Institute for Biomolecular Medicine, Departments of Otolaryngology, Neuroscience and Physiology New York University School of Medicine New York United States
6. Center for Neural Science New York University New York United States

† Corresponding author

## Abstract

10.7554/eLife.09457.001 Although it is well known that long-term synaptic plasticity can be expressed both pre- and postsynaptically, the functional consequences of this arrangement have remained elusive. We show that spike-timing-dependent plasticity with both pre- and postsynaptic expression develops receptive fields with reduced variability and improved discriminability compared to postsynaptic plasticity alone. These long-term modifications in receptive field statistics match recent sensory perception experiments. Moreover, learning with this form of plasticity leaves a hidden postsynaptic memory trace that enables fast relearning of previously stored information, providing a cellular substrate for memory savings. Our results reveal essential roles for presynaptic plasticity that are missed when only postsynaptic expression of long-term plasticity is considered, and suggest an experience-dependent distribution of pre- and postsynaptic strength changes. DOI: http://dx.doi.org/10.7554/eLife.09457.001

## Materials and methods

## Short- and long-term synaptic plasticity model

## Short-term plasticity model

To model short-term synaptic plasticity, we used the Tsodyks-Markram model with facilitation (Markram et al., 1998). This model is defined by the following ODEs(1)dr(t)dt=1−r(t)D−p(t)r(t)X(t),(2)dp(t)dt=P−p(t)F+P[1−p(t)]X(t).

The first equation models the vesicle depletion process, where the (normalized) number of vesicles r is decreased by an amount p(t)r(t) after a presynaptic spike from the train X(t)=∑tpreδ(t−tpre). Between spikes r recovers to 1 with a depression time constant D. The second equation models the dynamics of the presynaptic factor p which increases an amount P[1 − p] after every presynaptic spike, decaying back to baseline presynaptic factor P with a facilitation time constant F. By varying the synaptic dynamics parameters D, F and P, one can obtain different synaptic dynamics. We used typical values for pyramidal-onto-pyramidal synapses (Costa et al., 2013), D = 200 ms and F = 50 ms, while P is modified by long-term plasticity as below. The average number of vesicles released per spike is r(t)p(t), which can be interpreted as the presynaptic strength.

## Long-term plasticity model

In layer-5 pyramidal to pyramidal cell synapses, timing-dependent LTD is presynaptically expressed. It is mediated by the coincidence between a postsynaptic signal (eCB release) and a presynaptic signal (presynaptic NMDA receptor activation) (Sjöström et al., 2003, 2004; Bender and Feldman, 2006; Yang and Calakos, 2013). LTP is driven by postsynaptic coincidence detection of the combined binding of glutamate and postsynaptic depolarization (Bender and Feldman, 2006; Sjöström et al., 2007; Shouval et al., 2010), promoting an increase in the number and/or properties of postsynaptic AMPA receptors (Malinow and Malenka, 2002). However, timing-dependent LTP also has a presynaptic component, mediated by postsynaptic diffusion of NO (Hardingham and Fox, 2006; Sjöström et al., 2007; Hardingham et al., 2013; Yang and Calakos, 2013).

Our phenomenological triplet model of long-term modification of pre- and postsynaptic components has three synaptic traces, two postsynaptic (y+ and y−) and one presynaptic (x+), which increase upon a post- or presynaptic spike, respectively (see Appendix 1 for a more detailed comparison with the triplet model (Pfister and Gerstner, 2006)). The traces are obtained by filtering the spike trains with a first-order low-pass filter. We defined the postsynaptic depression trace(3)dy−(t)dt=−y−(t)τy−+Y(t),

the postsynaptic potentiation trace(4)dy+(t)dt=−y+(t)τy++Y(t),

and the presynaptic potentiation trace(5)dx+(t)dt=−x+(t)τx++X(t).

The long-term modification in the weight is achieved by modifying the postsynaptic factor q and the presynaptic factor P. The postsynaptic factor is modified with every postsynaptic spike Y according to(6)Δq=c+x+(t)y_(t−ϵ)Y(t)⏟TripletpostLTP,

where c+ is a constant that sets the amount of postsynaptic LTP. The y− trace is evaluated at (t − ϵ), so that the value of the respective synaptic trace is readout before being updated. The triplet character of this rule is expressed by the fact that it contains the presynaptic component once, but the postsynaptic activity twice (Y and filtered version y−). This ensures that LTP only takes place when the postsynaptic spike follows both a presynaptic spike and a preceding postsynaptic spike (Pfister and Gerstner, 2006). As a result, low pairing frequencies do not lead to LTP, as y− will have decayed, consistent with data (Sjöström et al., 2001).

Similarly, the presynaptic factor is modified whenever the presynaptic cell is active according to(7)ΔP=−d_y_(t)y+(t)X(t)⏟TripletpreLTD+d+x+(t−ϵ)y+(t)X(t)⏟TripletpreLTP.

For plasticity in P to occur, the presynaptic spikes X readout the postsynaptic traces (presynaptic coincidence detection), y−y+ for presynaptic LTD and x+y+ for presynaptic LTP. d− and d+ are constants that set the amount of presynaptic LTD and LTP, respectively. While presynaptic LTD has a triplet form, it contains two postsynaptic traces and the raw presynaptic spike train. Therefore it does not vanish at low frequencies. Equivalently, this term could be written as a doublet rule with a double exponential as the presynaptic trace.

The total synaptic strength is a product of both pre- and postsynaptic factors(8)w(t)=qp(t)r(t).

For a synapse that has not been stimulated recently this simplifies to w = Pq.

Being a probability we hard-bounded P = [0, 1]. The postsynaptic factor q had a lower bound of 0, and an upper bound of 2. Alternatively a soft-bounded rule could be used (van Rossum et al., 2012). In the data used to fit the model (see below), postsynaptic homosynaptic LTD was not apparent on the timescale of the experiment. Because it seems unrealistic that the postsynaptic factor q never decreases, slow homeostasic scaling of the postsynaptic factor was included for network simulations (Turrigiano et al., 1998). This prevents weakly active synapses from potentiating the postsynaptic factor q. It was modelled as a postsynaptic subtractive normalization, so that the total change in q of synapse i was equal to Δqi−α1N∑j=1NΔqj (Miller and MacKay, 1994). The only condition on the speed α for it to be consistent with the data, is that it should not lead to noticable homeostasis on the timescale of the experiments. For computational efficiency we used α = 0.075, which is still orders of magnitude faster than what has been observed in homeostasis experiments. The exact form of slow normalization (α → 0) does not affect the qualitative behavior of the model. Note that the timescale of the slow normalization determines how long the memory savings effects are present.

To speed up the numerical implementations, we integrated the synaptic traces between the pre- and postsynaptic spikes. In the following equations, we label the presynaptic spikes with k and the postsynaptic ones with l.(9)y−l+1=y− l exp(−Δtpostτy−)+1,(10)y+l+1=y+ l exp(−Δtpostτy+)+1,(11)x+k+1=x+k  exp(−Δtpreτx+)+1.

We subsequently integrated the model between pre- and postsynaptic spikes(12)ql+1=ql+c+x+ k exp(−Δtpost−preτx+)y− l exp(−Δtpostτy−),(13)Pk+1=Pk−d−y−l exp(−Δtpre−postτy−)y+ l exp(−Δtpre−postτy+)+d+y+ l exp(−Δtpre−postτy+)x+ k exp(−Δtpreτx+),

where Δtpost−pre is the time between the current postsynaptic spike and the last presynaptic spike, Δtpost is the time between the current postsynaptic spike and the last one, and similarly for Δtpre−post and Δtpre. Finally, we also integrated the STP (Equations 1, 2) between presynaptic spikes k and k + 1, a time Δtpre apart, yielding(14)rk+1=1−[1−rk(1−pk)]exp(−ΔtpreD),(15)pk+1=P+pk[1−P]exp(−ΔtpreF).

with initial conditions r0 = 1 and p0 = P.

## Model fitting to in vitro plasticity data

We fitted the free parameters of the long-term plasticity model θ = {d−, τy−, d+, τy+, c+, τx+} to the frequency- and timing-dependent slice STDP data of layer-5 pyramidal cells (Sjöström et al., 2001). Parameters are shown in Table 1. Rather than fitting to changes in the weight w, we fitted directly to modifications in P and q (see Equations 21, 22 for our estimators of P and q). This was done by minimizing the mean squared error between the data and the experiments for both P and q (as shown in Figure 1)(16)θ=argminθ1N∑jN[(PmodelafterPmodelbefore−PdataafterPdatabefore)2+(qmodelafterqmodelbefore−qdataafterqdatabefore)2],

where N denotes the number of protocols fitted, 10 in total (5 different pairing frequencies with −10 ms or +10 ms relative timing, see below). For induction protocols at high frequencies (≥10 Hz), pre- and postsynaptic spike trains consisted of five spikes that were paired 15 times at 0.1 Hz. Low-frequency pairings (0.1 Hz) were done with a single pre- and postsynaptic spike (as in Sjöström et al., 2001). Before plasticity induction, P and q were set to 0.5 and 1, respectively. For the interaction of STP and STDP simulations (Figure 1F,G), we used a standard passive neuron model with a membrane time constant of 25 ms.10.7554/eLife.09457.012Table 1.Unified pre- and postsynaptic spike-timing-dependent plasticity (STDP) model parametersDOI: http://dx.doi.org/10.7554/eLife.09457.012Parameterd−τy− (ms)d+τy+ (ms)c+τx+ (ms)Young rat visual cortex0.177132.70.1548230.20.061866.6The model was fitted to data from young rat visual cortex (Sjöström et al., 2001).10.7554/eLife.09457.013Table 2.Comparison between unified pre- and postsynaptic STDP model and different versions of the triplet model (for simplicity we removed the function arguments) (Pfister and Gerstner, 2006)DOI: http://dx.doi.org/10.7554/eLife.09457.013LTDLTP1LTP2pre-post STDPX d−y−y+X d+y+x+Y c+x+y−minimal HC TripletX A2−y1Y A2+x1Y A3+x1y2minimal VC TripletX A2−y1–Y A3+x1y2

Without further fitting this model also captured pharmacological blockade of the plasticity traces. In the model, we simulated the experimental effects of pharmacological blockade by setting the relevant parameter or variable to 0. Specifically, we simulated the effects of blocking two different retrograde messenger systems shown to be involved in STDP in layer-5 pyramidal cell pairs, eCB signaling (Sjöström et al., 2003) and NO signaling (Sjöström et al., 2007). To reproduce pharmacological blockade experiments, we used high-frequency pairing (50 Hz) with +10 ms delay, which is comparable with our frequency-dependent results and approximates the long depolarizing currents used in Sjöström et al. (2007). Blocking eCB receptors prevents presynaptic LTD (Sjöström et al., 2003). By setting d− = 0 presynaptic LTD was disabled. This reveals presynaptic LTP and enhances short-term depression (Figure 1—figure supplement 3), consistent with experimental evidence (Sjöström et al., 2007), as the drugs used are likely to block presynaptic eCB receptors. In contrast, blocking NO decreases LTP but does not affect short-term synaptic dynamics (Sjöström et al., 2007) (Figure 1—figure supplement 3A). We simulated this by setting y+ = 0, so that both presynaptic components were absent.

## Stochastic synaptic responses and in vitro P and q estimation

The release of neurotransmitter was assumed to follow a standard binomial model (Del Castillo and Katz, 1954)(17)Psyn(X=k)=(Nk)Pk(1−P)N−k,

which defines the probability of having k successful events (neurotransmitter release) given N trials (release sites) with equal probability P.

The mean synaptic response is scaled by a postsynaptic factor q, which can be related to the quantal amplitude so that(18)μsyn=PqN,

and the variance is(19)σsyn2=q2NP(1−P).

Following the binomial release model (Equation 18), μsyn (Equation 19) and σsyn2 (Equation 20),(20)P=μsynNq,

and(21)q=σsyn2μsyn+μsynN.

The number of release sites N is believed to change only after a few hours (Bolshakov et al., 1997; Saez and Friedlander, 2009). As the slice synaptic plasticity experiments analysed here lasted only up to 1.5 hr (Sjöström et al., 2001) and we were interested in the relative changes we assumed constant N = 5.5 in our analysis below, as estimated in Markram et al. (1997) using data from the same connection type we used to fit our model. Equations 21, 22 were used to estimate P and q from in vitro plasticity data (see above), respectively (dataset deposited at Dryad data repository at http://dx.doi.org/10.5061/dryad.p286g [Costa et al., 2015]). Note that because the data had to be reanalized in full there are minor differences in the mean weights previously published (Sjöström et al., 2001).

We verified our P and q extraction method by analysing short-term plasticity experiments with pharmacological manipulation of presynaptic release or of postsynaptic gain (Figure 1—figure supplement 2A, Sjöström et al., 2003), and experiments with pharmacological blockade of pre- or postsynaptic long-term plasticity (Figure 1—figure supplement 2B, Sjöström et al., 2007) (Figure 1—figure supplement 2A,B). In addition, long-term changes in P but not in q were inversely correlated with changes in paired-pulse ratio, as expected (Figure 1—figure supplement 2C,D). Taken together, these results lend experimental support to our binomial-distribution-based approach for extracting P and q to tune changes in the pre- and postsynaptic modifications of our unified STDP model (Figure 1D,E).

## Analysis of in vivo data

We extracted the effective P and q from the in vivo data obtained by Froemke et al. (2013). Again using a binomial model, we obtained estimators for their variability measure given by v = q (1 − P) and the mean by μ = PqN. To ease comparison with our simulations we set the initial P to the same initial condition used in our simulations P = 0.5 (Costa et al., 2013). We then obtained the initial N=|μ|qP and the initial q=v(1−P). For the after pairing data we allowed both pre- and postsynaptic factors P and q to change, while N was fixed to the values extracted before pairing (Bolshakov et al., 1997). The estimations after learning were obtained as q=v+|μ|N and P=|μ|Nq. We used these estimators to extract q and P from measurements for both the depression experienced for the unpaired (best before pairing) receptive field position and the potentiated paired position (Froemke et al., 2013). After pairing, the effective q of the potentiated (‘on’) response increased from qbeforeon=23.3 pA to qafteron=27.1 pA (+16.3%), while P increased from Pbeforeon=0.5 to Pafteron=0.73 (+46%). Responses that were depressed (‘off’), typically the original best frequency, yielded no statistically significant change in qbeforeoff, while Pbeforeoff=0.5 and Pafteroff=0.40 (−20%) (Figures 2, Figure 2—figure supplement 1 and Figure 2—figure supplement 3). To ease comparison with the postsynaptic factor in the simulations we scaled the experimentally obtained q such that before plasticity it was 1. We compared models where we allowed both P and q to change or only one of them, the lower variability estimation error was obtained by the one where both factors change (Figure 2—figure supplement 3E). The estimation error was calculated as 1N∑​iN(vreali−vestimatedi)2, where N is the number of data points.

## Synaptic signal detection

We calculated the SNR of a synaptic response defined here by a random variable s, amidst additive background noise defined by the random variable n as follows(22)SNRsyn=2(⟨s⟩−⟨n⟩)2σs2+σn2,

It is assumed that n∼𝒩(0,σn2) and we also used the Gaussian approximation to the binomial release model specified above, s∼𝒩(PqN,q2NP(1−P)+σn2), from which follows the SNR of the first postsynaptic response(23)SNRsyn=2(PqN)2q2NP(1−P)+2σn2.

In Figure 2, we used σn2=0.5. Variance of the k-th postsynaptic response is given by σsynk2=q2Nrkpk(1−rkpk) (Figure 2—figure supplement 2A). The SNR of the k-th postsynaptic response is(24)SNRsynk=2(rkpkqN)2q2Nrkpk(1−rkpk)+2σn2,

where pk and rk are given by Equations 15, 16, respectively. The SNR of the sum of the first K responses, evoked at a given presynaptic firing rate ρ therefore equals(25)SNRsynρ=2(∑k=0K−1rkpkqN)2∑k=0K−1q2Nrkpk(1−rkpk)+2∑k=0K−1σn2.

After unified STDP the first response has a higher amplitude and the second one a much lower amplitude due to synaptic depression. Combined with the background noise, the SNR can drop when the second or further responses are included. However, the SNR of the summed response will always be larger than when only postsynaptic modifications are made (see Figure 2—figure supplement 2B). This holds for any frequency, Figure 2—figure supplement 2C and carries over to an information theoretic analysis of the response, Figure 2—figure supplement 2D.

Next, we used ROC analysis to compute the false alarm and detection probability of the first postsynaptic response(26)pfalse alarm=∫T+∞Pn(r)dr=12erfc(T2σn2)​,(27)pdetection=∫T+∞Ps(r)dr=12erfc(T−PqN2q2NP(1−P)+σn2)​.

where T is the discrimination threshold, and erfc is the complementary error function defined as erfc(x)=2π∫x∞e−t2dt. To assess the overall discriminability, we used pdiscrimination, which is the area under the ROC curve (AUC). The AUC was computed by integrating over the ROC curve using the trapezoid method (see Figure 2D). Given that N is a simple constant we set it to 1, unless otherwise stated (see data inference above).

## Receptive field development

For the receptive field development simulations, we used a feedforward network with 100 presynaptic neurons j with Poisson statistics and a single integrate-and-fire postsynaptic neuron. The postsynaptic neuron was modelled as an adaptive exponential integrate-and-fire neuron model (Brette and Gerstner, 2005). Model parameters were as reported in Brette and Gerstner (2005); Badel et al. (2008) and synapses were modelled as input currents. The firing rate of the presynaptic Poisson neurons was modelled using a Gaussian profile, defined as(28)ρ(j;p,σ)=ρmin+(ρmax−ρmin)e−(j−p)22σ2.

where ρ is the rate in the Poisson neuron model j, p the input position for which the rate is maximal, and σ = 5 Hz the distribution spread. ρmax and ρmin are the maximum and minimum rates, and were set to ρmax = 50 Hz and ρmin = 3 Hz. We scaled d−, d+ and c+ by a factor 0.15 to yield a smoother receptive field development. q was bounded between 0 nA and 20 nA, so that the synaptic input is appropriately scaled for the neuron model used. The network was simulated for 100 s to achieve convergence. For the memory savings experiment, we interleaved two receptive field positions. Results for receptive development and memory savings were averaged over 10 runs. The response of the postsynaptic neuron (Figure 3C) was assessed by presenting each stimulus alone with long-term synaptic plasticity inactive. Receptive field simulations were implemented in simulator Brian 1.41 (Goodman and Brette, 2008). Code for running and plotting the savings experiment is available online (http://modeldb.yale.edu/184487).

## Statistical comparison

Results are reported as mean ± SEM. Statistical comparisons were made with Student's t-test for equal means, if data was normally distributed as assessed using Kolmogorov–Smirnov test, Mann–Whitney U non-parametric test was used otherwise. For multiple comparisons we applied ANOVA or Kruskal–Wallis test for normally or non-normally distributed data, respectively. For correlation analysis the Spearman's coefficient was used together with one-tailed Student's t-test. Significance levels are *p < 0.05, **p < 0.01, and ***p < 0.001.
