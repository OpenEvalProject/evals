# Subunit exchange enhances information retention by CaMKII in dendritic spines

## Authors

- Dilawar Singh<sup>1</sup> ([ORCID: 0000-0002-4645-3211](https://orcid.org/0000-0002-4645-3211))
- Upinder Singh Bhalla<sup>1</sup> ([ORCID: 0000-0003-1722-5188](https://orcid.org/0000-0003-1722-5188)) †

### Affiliations

1. National Centre for Biological Sciences Tata Institute of Fundamental Research Bangalore India

† Corresponding author

## Abstract

Molecular bistables are strong candidates for long-term information storage, for example, in synaptic plasticity. Calcium/calmodulin-dependent protein Kinase II (CaMKII) is a highly expressed synaptic protein which has been proposed to form a molecular bistable switch capable of maintaining its state for years despite protein turnover and stochastic noise. It has recently been shown that CaMKII holoenzymes exchange subunits among themselves. Here, we used computational methods to analyze the effect of subunit exchange on the CaMKII pathway in the presence of diffusion in two different micro-environments, the post synaptic density (PSD) and spine cytosol. We show that CaMKII exhibits multiple timescales of activity due to subunit exchange. Further, subunit exchange enhances information retention by CaMKII both by improving the stability of its switching in the PSD, and by slowing the decay of its activity in the spine cytosol. The existence of diverse timescales in the synapse has important theoretical implications for memory storage in networks.

## Introduction

Memories are believed to be stored in synapses, encoded as changes in synaptic strength (Hebb, 2005; Takeuchi et al., 2014; Choi et al., 2018). Long-term potentiation (LTP), an activity-dependent change in synaptic strength, is considered to be the primary post-synaptic memory mechanism (Bliss and Collingridge, 2013; Mayford et al., 2012). Various behavioral experiments strongly suggest a critical role for CaMKII in induction of LTP (Lucchesi et al., 2011; Giese et al., 1998). In the CA1 region of the hippocampus, blocking CaMKII activity blocks the induction of LTP (Chang et al., 2017). After LTP induction, several other pathways including protein synthesis (Aslam et al., 2009), clustering of receptors (Shouval, 2005), receptor translocation (Hayer and Bhalla, 2005) and PKM-$ζ$ activation (Sacktor, 2012), have been suggested as mechanisms for long-term maintenance of synaptic state. Recent evidence from behavioral assays suggests that CaMKII may also be involved in long-term maintenance of memory (Rossetti et al., 2017; but see Chang et al., 2017).

Any putative molecular mechanism involved in long-term maintenance of memory must be able to maintain its state despite the potent resetting mechanisms of chemical noise and protein turnover. In the small volume of the synapse (∼0.02 µm3 [Bartol et al., 2015]), the number of molecules involved in biochemical processes range from single digits to a few hundred, thereby increasing the effect of chemical noise. John Lisman proposed that a kinase and its phosphatase could form a bistable molecular switch able to maintain its state for a very long time despite turnover (Lisman, 1985). It has been shown by various mathematical models that CaMKII and its phosphatase protein phosphatase 1 (PP1) may form a bistable switch (Zhabotinsky, 2000) which can retain its state for years despite stochastic chemical noise and protein turnover (Miller et al., 2005; Hayer and Bhalla, 2005). Although there is experimental evidence that CaMKII/PP1 is bistable in in vitro settings (Bradshaw et al., 2003; Urakubo et al., 2014), experimental evidence for in vivo bistability is lacking. In spine cytosol, CaMKII has been shown not to act like a bistable switch but rather a leaky integrator of calcium activity (Chang et al., 2017). However, CaMKII may be bistable in special micro-environments such as the ‘core’ PSD where it attaches to the NMDA receptor (Dosemeci et al., 2016; Petersen et al., 2003).

From a computational perspective, the CaMKII/PP1 bistable system is an attractive candidate for memory storage (Koch, 2004). Bistability provides a plausible solution to the problem of state maintenance. Previous modeling work has shown that the CaMKII/PP1 system may form a very stable switch despite protein turnover and stochastic noise in the small volume of the synapse. The stability increases exponentially with the number of holoenzymes (Miller et al., 2005). It is important to note that this model exhibits bistable behavior only in a narrow range of PP1 concentrations in the PSD. This strict restriction may be met because phosphorylated CaMKII is protected from phosphatases in PSD except PP1 (Strack et al., 1997a), which is tightly regulated in the PSD (Bollen et al., 2010).

CaMKII has another remarkable property which was hypothesized by Lisman (Lisman, 1994) but discovered only recently, namely, subunit exchange. In this process, two CaMKII holoenzymes can exchange active subunits leading to spread of CaMKII activation (Stratton et al., 2014).

In this paper, we adapt the Miller and Zhabotinksy (MZ) model (Miller et al., 2005) to include subunit exchange and diffusion, and quantify the effects of subunit exchange on the properties of the CaMKII-PP1 system in two adjacent neuronal micro-environments: PSD and spine cytosol.

In the PSD, PP1 is tightly regulated and CaMKII is protected from other phosphatases. But in the spine cytosol, CaMKII is accessible to other phosphatases along with PP1. We examined how state switching lifetimes in the PSD are affected by subunit exchange in different contexts of PP1 levels, turnover, and clustering of CaMKII. In the spine cytosol, we show how the integration of calcium stimuli generates two time-courses of CaMKII activity as a result of subunit exchange (Chang et al., 2017).

## Results

### Model validation

The basic computational units in our model are individual CaMKII subunits, and the CaMKII ring consisting of six or seven CaMKII subunits. We treat the CaMKII ring as a proxy for the CaMKII holoenzyme, which consists of two such rings stacked over each other (Woodgett et al., 1983; Hoelz et al., 2003; Chao et al., 2011). We define Active CaMKII as a holoenzyme (ring of six or seven subunits) in which at least two subunits are phosphorylated at Thr286. In our model, CaMKII exists in 15 possible states compared to two in the MZ model (see Materials and methods). This leads to many more reactions than the MZ model. We also replaced the Michaelis-Menten approximation in the MZ model by equivalent mass-action kinetics (e.g. Equation 2). Since analytical comparison of the two models was not possible, we first compared numerical results from our model without diffusion and without subunit exchange with the MZ model (Figure 1).

![Figure 1.](https://cdn.elifesciences.org/articles/41412/elife-41412-fig1-v2.jpg)

**Figure 1.:** (A) CaMKII/PP1 pathway described in System Biology Graphical Notation (SBGN) – Process Description (PD) Language (Le Novère et al., 2009). (B) (above) Major chemical reactions in the CaMKII/PP1 pathway. (below) Subunit exchange between two CaMKII holoenzymes. Blue and red balls represent phosphorylated and un-phosphorylated subunits respectively. (C) Basal Ca2+ profile in spine and PSD. Basal Ca2+ level is 80 nM with fluctuations every 2 s, lasting for 2 s. These fluctuations (represented by symbol $ϵ$) are sampled from a uniform distribution with median of 120 nM and range of 40 nM (see Materials and methods). (D) Without diffusion and subunit exchange, CaMKII in our model is bistable. Two trajectories of CaMKII activity (fraction of total CaMKII holoenzymes with at least two subunits phosphorylated) are shown for different system sizes NCaMKII = 15 (top) and NCaMKII = 35 (bottom). (E) Switch stability (measured as average residence time in the stable states) increases exponentially with system size NCaMKII. Turnover rate $v_{t}=30h^{−1}$. Panels C, D, and E show key properties of our model that are very similar to those of the MZ model. Source data are available at https://github.com/dilawar/SinghAndBhalla_CaMKII_SubunitExchange_2018/tree/master/PaperFigures/elifeFigure1 (Singh and Bhalla, 2018).

Our model exhibited all the key properties of the MZ model: (1) In the PSD, under basal calcium (Ca2+) stimulus conditions, CaMKII/PP1 formed a bistable switch (Figure 1C,D), (2) The stability of the switch increased exponentially with system size (Figure 1E), (3) Increased number of PP1 molecules (NPP1) shut off the switch (Figure 2), and (4) Bistability was robust to slow turnover of CaMKII (Figure 3).

![Figure 2.](https://cdn.elifesciences.org/articles/41412/elife-41412-fig2-v2.jpg)

**Figure 2.:** (A) Two representative bistable trajectories (NCaMKII = 12) are shown with subunit exchange (+SE, blue) and without subunit exchange (-SE, red) respectively (Dsub = 0.1 µm2 s−1, and DPP1 = 0.5 µm2 s−1 for both blue (+SE) and red (-SE); and NPP1 = 168 for blue (+SE) and 72 for red (-SE), respectively). (B) Blue and red solid lines represent the fraction of total time spend by the switch in the ON state with and without subunit exchange, respectively. The lines are fitted with the function $a/(1+e^{k⁢(x-x_{0})})$. Dotted red and blue lines show the fraction of time that the switch spends in intermediate states ($x_{a}y_{n−a}$, 2 < a < n-2) with and without subunit exchange, respectively. Due to subunit exchange, the switch tolerated a larger amount of PP1 ($x_{0}$ value 6.35 vs 13.46 that is a change of 7.11$\timesN_{CaMKII}$NCaMKII). The range of PP1 for which switch remained bistable saw a moderate change ($k$, 1.32 vs. 2.3). The fraction of time spent in intermediate states (dashed lines) is much smaller when subunit exchange is enabled (blue dashed line), that is the switching time is shorter. (C) Due to subunit exchange, relaxation time becomes independent of NPP1 (blue vs red). Shaded area represents standard deviation. Source data are available at https://github.com/dilawar/SinghAndBhalla_CaMKII_SubunitExchange_2018/tree/master/PaperFigures/elifeFigure2 (Singh and Bhalla, 2018).

![Figure 3.](https://cdn.elifesciences.org/articles/41412/elife-41412-fig3-v2.jpg)

**Figure 3.:** (A,B) Three sample trajectories are shown for a switch of size NCaMKII = 10 without subunit exchange (-SE, red) and with it (+SE, blue). We consider three different turnover rates of 1 per 30 h, 1 per 3 h, and 1 per 0.5 h. As turnover is increased, the state stability of the ON state of the switch decreases. (C, left) Normalized residence time of the ON state vs. turnover rate for two switches of size 6 and 12. Without subunit exchange, switch stability decreases steeply with turnover rate (red); however, when subunit exchange is enabled, switch stability is not affected by turnover rates as high as 1 h-1 (blue). (C, right) In the bistable regime (solid lines), the number of switching events increases monotonically with turnover rate. Source data are available at https://github.com/dilawar/SinghAndBhalla_CaMKII_SubunitExchange_2018/tree/master/PaperFigures/elifeFigure3 (Singh and Bhalla, 2018).

Thus, our baseline model exhibited all the key properties that had previously been predicted for the bistable CaMKII switch. However, subunit exchange and diffusion introduced several interesting additional properties, which we examine below.

### Subunit exchange increases the tolerance of the CaMKII switch to PP1 and to turnover

We first analyzed the switch sensitivity to PP1. In our model as well in the MZ model, the number of PP1 molecules (NPP1) has an upper limit for the switch to exhibit bistability. This constraint arises because PP1 must saturate in the ON state of the switch, that is the maximal enzymatic turnover of PP1 must be smaller than the rate of activation of CaMKII subunits. However, unlike the MZ model where the addition of one extra PP1 molecule changed the residence time of the ON state by roughly 90% (Figure 2C in Miller et al., 2005), we did not find the residence time of the ON state to be this sensitive to PP1. In our model, on average it required half the number of holoenzymes (i.e. 0.5× NCaMKII) extra PP1 molecules to cause a similar 90% change in the residence time of the ON state. This number is roughly equal to the maximum number of CaMKII subunits (released from CaMKII holoenzymes during subunit exchange Equation 3) that can exist at any given time in our model. We conjecture that this reduced sensitivity to PP1 is due to the fact that PP1 participates in many more reactions in our model.

We found that a system consisting of NCaMKII = 12 holoenzymes remained bistable for NPP1 = 3× to 8× NCaMKII without subunit exchange, and for NPP1 = 12× to 16× NCaMKII with subunit exchange for Dsub = 0.1, and DPP1 = 0.5 µm2 s−1 (Figure 2B). Thus, subunit exchange shifted the middle of the bistable range to higher values of PP1. The width of the range of PP1 over which bistability was present saw a moderate increase in the presence of subunit exchange (blue and red sigmoidal fit in Figure 2B). A similar trend was observed for other values of DPP1 and Dsub (data not shown).

In the presence of subunit exchange, the ON state of the switch has a tighter distribution (blue vs. red histogram, Figure 2A), that is, there are fewer holoenzymes that are completely de-phosphorylated by PP1. We interpret this as follows: In the presence of subunit exchange, any subunit in a holoenzyme de-phosphorylated by the PP1 is likely to be rapidly re-phosphorylated. This is because, when the switch is in ON state, most diffusing subunits present in the PSD are in the phosphorylated state. Hence, in addition to auto-phosphorylation, the exchange reactions (Equation 3) turn unphosphorylated holoenzymes to phosphorylated holoenzymes with a significant rate. Taken together, subunit exchange acts as a compensatory mechanism for dephosphorylation by PP1 in the ON state of the switch.

Subunit exchange also had a strong effect on time spent by the switch in transition from one stable state to another (relaxation time). When subunit exchange was enabled, the relaxation time was reduced (red vs. blue dashed line in Figure 2B) and also became independent of NPP1. As mentioned previously, due to subunit exchange, the ON state has a tighter distribution (blue vs. red histogram in Figure 2A). This means that there were fewer ineffective transitions from the ON to the OFF state. As expected, the standard deviation of the relaxation time was also greatly reduced in the presence of subunit exchange (red and blue curve, Figure 2C). Thus, subunit exchange makes the switch’s ON state less noisy and more robust to dephosphorylation by PP1.

Parallel results were obtained for the effect of subunit exchange on CaMKII switch robustness in the context of protein turnover. Turnover acts at a constant rate to replace any active CaMKII holoenzyme with an inactive holoenzyme (Equation 6), thus decreasing the stability of the ON state. Without subunit exchange, switch stability as measured by residence time of the ON state decreased exponentially with increasing turnover rate. With subunit exchange, however, residence time of the ON state remained roughly constant upto a $∼$10 fold increase in turnover (Figure 3B), after which subunit exchange could not phosphorylate all the inactive holoenzymes produced by turnover. At this point, the switch started to show a similar steep decay of stability as was seen without subunit exchange. As expected, turnover increased the number of switching events in the regime of bistability in both cases.

Thus, subunit exchange broadens the zone of bistability of the switch, both with respect to the range of NPP1, and the turnover rate over which the switch remains bistable. It also reduces fluctuations in the ON state of the switch.

### Subunit exchange facilitates the spread of CaMKII activity

As suggested in Stratton et al., 2014, we found that subunit exchange facilitated the spread of CaMKII activation (Figure 4). When subunits were allowed to diffuse, an active subunit could be picked by a neighboring inactive CaMKII holoenzyme, making it partially phosphorylated. This process overcomes the first slow step of CaMKII phosphorylation (Equation 1), especially when subunit exchange makes many phosphorylated subunits available, thereby facilitating the spread of activation.

![Figure 4.](https://cdn.elifesciences.org/articles/41412/elife-41412-fig4-v2.jpg)

**Figure 4.:** (A) 18 CaMKII holoenzymes were simulated in a cylindrical arena of volume 0.0275 µm3, discretized into 18 voxels, each separated by 30 nm. Red and blue balls represent unphosphorylated and phosphorylated subunits, respectively. (B) Activation profile of CaMKII at mean basal calcium level of 80 nM+$ϵ$ ($ϵ$ is fluctuation in basal Ca2+ levels Figure 1A) for various values of Dsub with NPP1 = 15× NCaMKII. For this value of NPP1, we see moderate or no mean activity of CaMKII for various values of Dsub for basal Ca2+ = 80 nM + $ϵ$. This serves as the baseline for comparisons. (C) At a slightly higher level of basal Ca2+ (120 nM+$ϵ$), subunit exchange has a stronger effect on CaMKII activation. When subunits were modeled with zero or very small diffusion coefficients (Dsub = 0 and Dsub = 10-8 µm2 s−1), the effect of subunit exchange was smaller than when subunits were tested with moderate-to-high diffusion coefficients (Dsub = 0.001 and 0.1 µm2 s−1), (D) Quantification of the effect of subunit exchange (shown in B and C) as measured by the time taken by CaMKII to rise from 10% to 90% of its maximum value (rise time) in hours vs Dsub and basal Ca2+ levels. The effect of subunit exchange is greater (i.e. shorter rise times) at higher calcium levels for all values of Dsub. Rise time is also shorter for larger Dsub for all values of [Ca2+]. Error bars represents standard deviation (n = 40 trajectories). (E) The time to onset of CaMKII activity is independent of Dsub and depends only on [Ca2+]. The time to onset of activity is measured as the time taken by inactive CaMKII to rise from 0 to 10% of its maximum value. Average time for the onset of activity decreased with increasing basal [Ca2+] levels but remained independent of Dsub suggesting that subunit exchange does not play a significant role at the beginning of activation of CaMKII by Ca2+. Error bar represents standard deviation (n = 40 trajectories). DPP1 = 0.5 µm2 s−1 for all simulations. Source data are available at https://github.com/dilawar/SinghAndBhalla_CaMKII_SubunitExchange_2018/tree/master/PaperFigures/elifeFigure4 (Singh and Bhalla, 2018).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/41412/elife-41412-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Sample trajectories of CaMKII activation for basal Ca2+ concentration of $100⁢nM$+$ϵ$.In all simulations, DPP1 was set to 0.5 µm2 s−1 and Dsub was varied. Each plot contains 40 trajectories. Dark black trajectory in each plot shows the average trajectory.

We simulated NCaMKII = 18 inactive holoenzymes in a cylindrical arena with a volume of 0.0275 µm3 and a length of 540 nm representing the PSD. The cylinder was divided into 18 voxels (one holoenzyme in each voxel). Each voxel was separated by 30 nm, which is the average nearest-neighbour distance for CaMKII holoenzymes (Feng et al., 2011). Each voxel was considered to be a well-mixed environment that is diffusion was instantaneous within the voxel. Between voxels, diffusion was implemented as cross-voxel jump reactions (see Materials and methods). We did not try 2D/3D diffusion because of its simulation complexity and because it would be expected to be qualitatively similar (Fange et al., 2010).

We fixed the diffusion coefficient of PP1 (DPP1) to quantify the effect of varying the diffusion coefficient of subunits (Dsub) and basal calcium levels. We used NPP1 = 0.5 µm2 s−1 which is the observed value of the diffusion coefficient of Ras, a similar sized protein (Harvey et al., 2008). We ran simulations for 4 h at basal calcium concentration [Ca2+] = 80 nM+$ϵ$ (where $ϵ$ is the fluctuation in basal calcium levels, see Figure 1C), and without subunit exchange (i.e. Dsub = 0). We set NPP1 = 15× NCaMKII to make sure the system showed no significant CaMKII activity (Figure 4B, red curve). This served as the baseline to quantify the effect of subunit exchange. When we enabled subunit exchange by setting Dsub to a non-zero value, CaMKII activity rose to a maximum within 4 h even for a low value of Dsub = 0.001 µm2 s−1 (Figure 4C, black curve).

The first step of CaMKII phosphorylation (Equation 1) is slow since it requires binding of two calcium/calmodulin complex (Ca2+/CaM) simultaneously (at basal [Ca2+] = 80 nM+$ϵ$ , $v_{1}$ = 1.27 × 10-5 s-1). However, subunit exchange can also phosphorylate a subunit in a holoenzyme by adding an available phosphorylated subunit to it (Equation 3). Note that a Dsub value as low as 0.001 µm2 s−1 is good enough for subunit exchange to be effective. With this value of Dsub, it takes roughly 0.9 s for the subunit to reach another holoenzyme which is, on average, 30 nm away. Under these conditions, the rate of picking up available active subunits (given in Equation 3) is faster than $v_{1}$. Expectedly, for larger Dsub values (e.g., 0.001 and 0.1 µm2 s−1), subunit exchange becomes more effective (compare red and blue with the rest in Figure 4D).

As expected, at higher basal Ca2+ levels (120 nM), the system showed higher CaMKII activity for all values of Dsub (Figure 4D). Increasing Dsub increased the effect of subunit exchange, as measured by the decreased rise time of CaMKII activity from 10% to 90% (Figure 4D). However, the time of onset of CaMKII activation as measured by rise time from 0% to 10% was dependent only on basal Ca2+ levels but not on Dsub (Figure 4E).

Thus, subunit exchange facilitates the spread of kinase activity following CaMKII activation but does not affect the onset of CaMKII activation.

### Subunit exchange synchronizes switching activity of clustered CaMKII

Next, we probed the effect of subunit exchange between spatially separated CaMKII clusters. We considered NCaMKII holoenzymes organized into three clusters of size NCaMKII/3, each separated by a distance d. This configuration corresponds to cases where receptors and CaMKII holoenzymes are clustered at the synapse.

When there is no subunit exchange across voxels (Dsub = 0), these switches are expected to switch independently like multiple coins flipped together, resulting in a binomial distribution of activity. The clustered system had three relatively stable bistable systems (long residence time, Figure 1E). As expected, without subunit exchange, activity in this system had a binomial distribution (Figure 5B, red plot).

![Figure 5.](https://cdn.elifesciences.org/articles/41412/elife-41412-fig5-v2.jpg)

**Figure 5.:** (A) Three clusters, each of size 6 (i.e., NCaMKII = 6) separated by distance $d$ were simulated in a cylindrical arena of volume 0.0275 µm3 discretized into three voxels. CaMKII subunits are shown as red (unphosphorylated) and blue (phosphorylated) balls. (B) (left) Without subunit exchange, all three switches flipped independently with a low residence time, resulting in a binomial distribution of states (Bar chart on right, in red). (right) With subunit exchange, all switches synchronized their activity that is they acted as a single bistable switch with a longer residence time. (C) Strength of synchronization ($k_{s}$) vs. diffusion constant Dsub for a system consisting of three switches each separated from each other by a distance of 30 nm. Variable $k_{s}=1-t_{i}$ where $t_{i}$ is the fraction of total time spent by the switches in the intermediate states xayn-a; 1 < a < n. Synchronization is strong if ks > 0.4. (D) 2-D plot of $k_{s}$ vs. Dsub and $d$. The effect of synchronization $k_{s}$ due to subunit exchange is strong (red region) and robust to changes in Dsub, and effective for inter-cluster distance ($d$) as large as 100 nm. DPP1 = 0.5 µm2 s−1 for all simulations. Source data are available at https://github.com/dilawar/SinghAndBhalla_CaMKII_SubunitExchange_2018/tree/master/PaperFigures/elifeFigure5 (Singh and Bhalla, 2018).

Then we allowed PP1 and CaMKII subunits to undergo linear diffusion. We set DPP1 = $0.5$ µm2 s−1 as before and varied Dsub to quantify effect of subunit exchange. Subunit exchange led to synchronization of switching activity. The population of clustered CaMKII acted as a single bistable switch (Figure 5B, blue plot). This effect was strong and robust to variation in Dsub. Even for a very small value of Dsub = 0.01 µm2 s−1, we observed strong synchronization (Figure 5D). The synchronization disappeared completely for Dsub less than 0.0001 µm2 s−1, and for $d$ greater than 100 nm (Figure 5D).

Thus, for most physiologically plausible values of diffusion coefficient Dsub, subunit exchange causes synchronization of switching activity of clustered CaMKII.

### Subunit exchange may account for the observed dual decay rate of CaMKII phosphorylation

Finally, we asked if subunit exchange might account for the complex time-course of CaMKII dynamics in spine as observed in recent experiments (Chang et al., 2017). We designed a simulation to replicate an experiment where CaMKII was inhibited by a genetically encoded photoactivable inhibitory peptide after activating CaMKII by glutamate uncaging (Murakoshi et al., 2017). In the spine, CaMKII is more accessible to phosphatases than in the PSD, where our previous calculations had been located. To model the increased availability of phosphatases, we increased the concentration of PP1 by an order of magnitude, and increased the volume of the compartment to match the volume of a typical spine head that is 0.02 µm3 (Bartol et al., 2015). We found that CaMKII acted as a leaky integrator of the calcium activity with a typical exponential decay dynamics (Figure 6A). We then enabled the diffusion of CaMKII subunits (Dsub = 1 µm2 s−1) and PP1 (DPP1 = 0.5 µm2 s−1). These conditions decreased the rate of dephosphorylation roughly by a factor of 5 (41.65 s vs. 200.82 s) (Figure 6B).

![Figure 6.](https://cdn.elifesciences.org/articles/41412/elife-41412-fig6-v2.jpg)

**Figure 6.:** The clustered CaMKII population decays more slowly than the non-clustered population, due to subunit exchange. Thus, a mixed population of clustered and non-clustered CaMKII can explain observed two time-constants of CaMKII decay (Chang et al., 2017). (A) Trajectories of CaMKII activity (fraction of all CaMKII which are active) when a strong periodic Ca2+ pulse of 3 s duration was applied to the system after every 1000 s ($↓$). After the pulse, Ca2+ levels were brought down to 80 nM. Three trajectories are shown: without subunit exchange (red), with subunit exchange (blue), and a weighed sum of red and blue (74% red +24% blue as estimated in [Chang et al., 2017]). (B) Average decay dynamics after the onset of strong Ca2+ pulse ($↓$). When there was no subunit exchange, CaMKII decayed with a time- course of approximately 41.65 s (red and dashed yellow [fit]). When subunit exchange was enabled, CaMKII decay had a slower time-constant of 200.82 s (blue and dashed blue [fit]). (C) Average dynamics of the mixed population (black). This was fit to a double exponential that is $a⁢e^{-t/\tau_{1}}+(1-a)⁢e^{-t/\tau_{2}}$ for $a=0.74$ (dashed red). For a given $a=0.74$ (estimated in [Chang et al., 2017]), our estimate of time-constants (8.4 s, 86.2 s) matched well with experimentally estimated time-constants (6.4 s ± 0.7, 92.6 s ± 50.7). Shaded areas are the standard deviation. Number of voxels Nv = 10, Dsub = 1 µm2 s−1, DPP1 = 0.5 µm2 s−1. Source data are available at https://github.com/dilawar/SinghAndBhalla_CaMKII_SubunitExchange_2018/tree/master/PaperFigures/elifeFigure6 (Singh and Bhalla, 2018).

We expected that subunit exchange should have a strong effect on the time-course of decay of activity of clustered CaMKII in spine cytosol (e.g. CaMKII bound to actin) because the proximity of holoenzymes would lead to rapid exchange. Thus, if there are populations of clustered as well as non-clustered CaMKII in the spine, we expected that they would exhibit long and short time-courses of activity decay, respectively. Therefore a mixed population of clustered and non-clustered CaMKII should decay with two time-constants. Our simulations supported this prediction.

In Chang et al. (2017), the decay kinetics of CaMKII were obtained by curve fitting of experimental data. It was given by a double-exponential function: $F⁢(t)=P_{f⁢a⁢s⁢t}⁢e^{-t/\tau_{f⁢a⁢s⁢t}}+P_{s⁢l⁢o⁢w}⁢e^{-t/\tau_{s⁢l⁢o⁢w}}$ where $P_{fast}=0.74$, $P_{slow}=0.26$, $\tau_{fast}=6.4\pm0.7s$, $\tau_{slow}=92.6\pm50.7s$ (Figure 6C, magenta). We used their estimate of $P_{f⁢a⁢s⁢t}$ and $P_{s⁢l⁢o⁢w}$ to construct a mixed population of slow and fast decaying CaMKII (Figure 6A, black), and simulated the decay kinetics of CaMKII for this system. We fit the resulting decay curve with a double-exponential function (Figure 6C, dashed red). The time-constants obtained (8.4 s, 86.2 s) matched well with experimentally estimated time-constants of (6.4 s ± 0.7, 92.6 s ± 50.7).

Thus, we suggest that subunit exchange may be a mechanism that leads to CaMKII$\alpha$ activity decaying with two time-courses in spine cytosol.

## Discussion

Here, we have shown that subunit exchange strongly affects the properties of the CaMKII/PP1 pathway, both in its role as a bistable switch in the PSD and as a leaky integrator of Ca2+ activity in spine cytosol. In the PSD, where the model was tuned to elicit bistable dynamics from clustered CaMKII, subunit exchange improved the stability of the CaMKII/PP1 switch by synchronizing the kinase activity across the PSD (Figure 6). It also improved active CaMKII tolerance of PP1, and of turnover rate (Figure 2 and Figure 3). In the case where CaMKII was uniformly distributed in PSD, subunit exchange facilitated more rapid activation of CaMKII (Figure 4B–D) (Stratton et al., 2014). These simulation results predict that a CaMKII mutant lacking subunit exchange would be deficient in switch stability and slower to be activated by Ca2+, thereby resulting in degraded memory retention and deficient learning in memory-related behavioral experiments, respectively.

In the spine head, subunit exchange facilitated integration by prolonging the decay time-course of kinase activity (Figure 6). The fact that CaMKII dynamics changed from an integrator to bistable switch as we moved from spine cytosol (a phosphatase rich environment) to the PSD (where PP1 is tightly controlled) suggests an interesting sub-compartmentalization of functions in these microdomains. Furthermore, we observed that the clustering of CaMKII had important implications for its sustained activity.

Subunit exchange is unlikely to have any impact on neighbouring spines. The mean escape time of a single CaMKII subunit from a typical spine is between 8 s to 33 s (Holcman and Schuss, 2011). Any phosphorylated subunit is almost certain to be de-phosphorylated by PP1 during this time. We therefore predict that the effects of synchronization are local to each PSD, where PP1 is known to be tightly controlled. Subunit exchange loses its potency in the phosphatase rich region of the bulk spine head or dendrite. We therefore consider it unlikely that CaMKII subunit exchange plays any role in intra-spine information exchange such as synaptic tagging.

CaMKII is non-uniformly distributed in the PSD where it is mostly concentrated in a small region of 16 nm to 36 nm below the synaptic cleft (Petersen et al., 2003). In the PSD, CaMKII may exist in large clusters given that the PSD is rich in CaMKII binding partners. Our study predicts that subunit exchange may lead to synchronization when CaMKII is clustered, or more rapid activation by Ca2+ when it is uniformly distributed. Given that CaMKII can form clusters with N-methyl-D-asparate (NMDA) receptors, it would be interesting to study the mixed case where some CaMKII is clustered and the rest is uniformly distributed. This would require a detailed 3D simulation and is beyond the scope of this study.

Finally, we suggest that the existence of diverse time-scales of CaMKII activity – bistable and highly stable synchronized bistable in PSD, slow and fast decaying leaky integrator in spine head (Table 1) – has important theoretical implications. A very plastic synapse is good at registering activity dependent changes (learning) but poor at retaining old memories. On the other hand, a rigid synapse is good at retaining old memories but is not efficient at learning. A theoretical meta-model which sought to strike a balance between these two competing demands requires that a diversity of timescales must exist at the synapse (Benna and Fusi, 2016) for optimum performance. In this model, complex synapses with state variables with diverse time-scales are shown to form a memory network in which storage capacity scales linearly with the number of synapses, and memory decay follows $1/\sqrt{t}$ — a power-law supported by psychological studies (Wixted and Ebbesen, 1991). This model requires the memory trace to be first stored in a fast variable and then progressively and efficiently transferred to slower variables. Our study suggests a concrete mechanism for such a process. Here, the Ca2+ concentration in the PSD can be mapped to the fastest variable. The CaMKII integrator in the cytosol could represent the second slower variable to which the trace is transferred from Ca2+. Further, the state information is transferred to the third slower CaMKII bistable switch. The dynamics of CaMKII in the PSD forms an even slower bistable variable for longer retention of the memory trace. It is possible that memory is transferred from here to even slower variables, such as sustained receptor insertion (Hayer and Bhalla, 2005), PKM-$ζ$ activation (Sacktor, 2012), or local protein synthesis (Aslam et al., 2009).

**Table 1.**
 Diverse timescales of activity shown by CaMKII


<table>
  <thead>
    <tr>
      <th>Type</th>
      <th>Location</th>
      <th>Timescale</th>
      <th>Ref/Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Leaky integrator</td>
      <td>Spine cytosol</td>
      <td>~10 s</td>
      <td>Chang et al., 2017, This paper</td>
    </tr>
    <tr>
      <td>Leaky integrator decaying slowly due to subunit exchange</td>
      <td>Spine cytosol</td>
      <td>~100 s</td>
      <td>This paper, Chang et al., 2017</td>
    </tr>
    <tr>
      <td>Small bistable (Size 4 to 10)</td>
      <td>PSD</td>
      <td>Few hours to days</td>
      <td>This paper</td>
    </tr>
    <tr>
      <td>Large bistable (Size 12 to 20)</td>
      <td>PSD</td>
      <td>Few weeks to months</td>
      <td>This paper</td>
    </tr>
    <tr>
      <td>Synchronized population of bistables coupled by subunit exchange</td>
      <td>PSD</td>
      <td>Years</td>
      <td>This paper</td>
    </tr>
  </tbody>
</table>

## Materials and methods

We extended Miller and Zhabotinksy (MZ model; Miller et al., 2005) to incorporate subunit exchange and diffusion. We assume that vertical dimers are inserted and released together (Bhattacharyya et al., 2016). We also assume that both subunits of a vertical dimer phosphorylate and de-phosphorylate together. Under this assumption, we can treat the CaMKII ring as the proxy for the CaMKII holoenzyme and the subunit as the proxy for the CaMKII dimer. Without this assumption, the simulation cost of the increased complexity would be very significant.

In our model, a CaMKII ring with $n$ subunits (n = 6 or 7) can exist in 15 different states enumerated as $x_{a}⁢y_{n-a}$ for $0\leqa\leqn$ where $x$ and $y$ represent un-phosphorylated and phosphorylated subunits respectively. We ignore all rotational permutations and kinetically unlikely cases where there are discontiguous phosphorylated subunits in the ring. We assumed that the phosphorylation of neighbouring subunit proceeds clockwise.

### Ca2+ background activity (ϵ)

We assumed the resting Ca2+ level in spine to be 80 nM (Berridge, 1998). In the MZ model, Miller et al. assumed that Ca2+ entry through NMDA receptors can be approximated by a Poisson train with an average rate of 0.5 Hz. Since, on average, $∼$0.5 NMDA receptors open (Nimchinsky et al., 2004) upon pre-synaptic stimulation, we reduced the frequency of NMDA opening events to 0.25 Hz. We used a periodic pulse with a time-period of 4 s and duty cycle of 50%. To model NMDA activity in the 2 s long ON period of our 4 s long periodic pulse, we sampled from a uniform distribution with median of 120 nM (50% change, on average) and range of 40 nM (Figure 1C). This distribution is informed by Figure 2B,C from (Nimchinsky et al., 2004).

We did not consider decay dynamics of Ca2+ influx through the NMDA channel since the timescale of decay (roughly 100 ms) is much shorter than our simulation runtimes of days, and including this detail would have made the simulations very slow. The effect of ignoring decay dynamics are expected to be negligible given that the time-scale of CaMKII activation is much larger than the time course of Ca2+ decay dynamics. Furthermore, we did not consider contributions to background Ca2+ fluctuations by other channels. This background activity is represented by $ϵ$ in the figures and text.

### Phosphorylation and dephosphorylation of CaMKII ring

The activation of CaMKII in our study follows the same dynamics as in the MZ model (Equation 1). In our paper, by phosphorylation/activation of a CaMKII subunit or a holoenzyme, we mean phosphorylation at Thr286. The first step in CaMKII activation requires simultaneous binding of two (Ca2+/CaM) to the two adjacent subunits of CaMKII. Once a subunit is phosphorylated, it catalyzes phosphorylation of its neighbour (auto-phosphorylation) which requires binding of only one (Ca2+/CaM). Therefore, further phosphorylation proceeds at much faster rate. The phosphorylation of CaMKII is given by Equation 1 (Bradshaw et al., 2003; Miller et al., 2005).

$$
x_{a}y_{n−a}→v_{1}x_{a−1}y_{n−a+1}→v_{2}x_{a−2}y_{n−a+2}v_{1}=k_{1}[\frac{H^{3}}{1+H^{3}}]^{2},v_{2}=k_{1}\frac{H^{3}}{1+H^{3}},whereH=\frac{Ca^{2+}}{K_{H1}}
$$

where $n$ = 6 or 7 for $1\leqa\leqn;k_{1}=1.5s^{−1}$ (Hanson et al., 1994), and $k_{H1}=0.7µM$ (De Koninck and Schulman, 1998; Miller et al., 2005). At resting Ca2+ concentration of 100 nM, $v_{1}=1.27\times10^{−5}s^{−1}$ and $v_{2}=4.36\times10^{−3}s^{−1}$ (i.e., $v_{2}/v_{1}≈343$). The rate constant $v_{1}$ above defines the initial rate of phosphorylation. Furthermore, addition of phosphorylated subunits can happen through subunit exchange (Equation 3). We treat these as independent variables. The phosphorylation rates $v_{1}$ and $v_{2}$ are relatively well constrained by the experimental literature. The subunit exchange rates were estimated (Materials and methods) to be in the range of 1 s-1.

Once fully phosphorylated, CaMKII moves to the PSD where it binds to the NMDA receptor. Upon binding, it is no longer accessible other phosphatases except PP1.

The dephosphorylation of the CaMKII ring, and the subunit are given by Equation 2.

$$
PP1+x_{a}y_{n−a}⇌k^{−}k^{+}PP1.x_{a}y_{n−a}→k_{2}PP1+x_{a+1}y_{n−a−1}PP1+x⇌k^{−}k^{+}PP1.x→k_{2}PP1+y
$$

where $n$ = 6 or 7, and $1\leqa\leqn$. Following (Miller et al., 2005), we also assumed $k^{-}=0$. This gave us $k^{+}=\frac{k_{2}}{k_{M}}$ = 1/µM/s. We could not find any experimental estimate of $k_{M}$ in recent literature, therefore we used the same value of $k_{M}$ as in the MZ model (Miller et al., 2005).

### Subunit exchange

Since CaMKII ring consists of either 6 or 7 subunits in our model, any ring with six subunits cannot lose a subunit, and a ring with seven subunits cannot gain a subunit. The reactions which result in either gain or loss of a subunit are given by Equation 3 where $0\leqa\leq6or7$.

$$
x_{a}y_{7−a}+x⇌k_{x}^{−}k_{x}^{+}x_{a+1}y_{6−a}x_{a}y_{6−a}+y⇌k_{y}^{−}k_{y}^{+}x_{a}y_{7−a}
$$

We were not able to find values for $k_{x}^{+}$, $k_{x}^{-}$, $k_{y}^{+}$, and $k_{y}^{-}$ in the literature. We used the data in Stratton et al. (2014) to estimate the possible timescale of subunit exchange rate. (Bhattacharyya et al., 2016) speculate that upon activation, the hub of the holoenzyme becomes less stable and more likely to open up and lose a subunit that is an active holoenzyme loses subunits at a faster rate. Therefore, we maintained the following ratio $k_{x}^{−}≈10k_{x}^{+}N_{CaMKII}$ and $k_{y}^{−}≈10k_{y}^{+}N_{CaMKII}$ in all simulations where $N_{CaMKII}$ is the number of holoenzymes in the system.

#### Estimation of subunit exchange rate

To estimate reaction rates of Equation 3, we modeled the 'single molecule assay’ used in Stratton et al., 2014. In this assay, two distinct populations of CaMKII labelled by either green or red fluorophores were mixed together. The holoenzymes were not free to move but they could release subunits which could move freely. A green holoenzyme may pick up a red subunit and vice versa thereby giving rise to a mixed colored population. The readout from this assay is the ‘colocalization’ which is the fraction of total holoenzymes containing subunits of both colors.

In our model of this assay, a CaMKII holoenzyme is represented by $R_{a}⁢G_{n-a}$ where $R$ and $G$ represent a red and a green subunit in the holoenzyme respectively, and n = 6 or 7. The green population consists of holoenzymes with only green subunits (i.e., $R_{0}⁢G_{6}$ and $R_{0}⁢G_{7}$) and the red population has holoenzymes with all red subunits (i.e., $R_{6}⁢G_{0}$ or $R_{7}⁢G_{0}$). We assume that each color population has equal number of dodecameric (n = 6 $\times$ 2) and tetradecameric (n = 7 $\times$ 2) holoenzymes. Upon mixing red and green populations, the following reactions take place.

$$
R_{a}G_{b}⇌r_{g}r_{l}R_{a−1}G_{b}+Rforalla>0,b\geq0s.t.a+b=6R_{a}G_{b}⇌r_{g}r_{l}R_{a}G_{b−1}+Gforalla\geq0,b>0s.t.a+b=7
$$

The value of colocalization is equal to the percentage of all holoenzymes containing at least one red and one green subunit that is $\frac{\sum_{a\geq1,b\geq1}[R_{a}⁢G_{b}]}{\sum_{a\geq0,b\geq0}[R_{a}⁢G_{b}]}$. The dynamics of colocalization was fit by $100⁢(1-e^{-t/\tau})$. We first computed $\tau$ for experimental data when [CaMKII] = 8 µM (Figure 7A). This served as the baseline for further analysis.

![Figure 7.](https://cdn.elifesciences.org/articles/41412/elife-41412-fig7-v2.jpg)

**Figure 7.:** (A) Colocalization dynamics as reported in Stratton et al., 2014 (all data scraped from figures) at CaMKII = 8 µM (blue dots). Solid blue line shows a best fit $100⁢(1-e^{-t/\tau})$ with $\tau$=62.7 min. (B) Phase plot of $\tau$ of colocalization trajectories generated for various values of $r_{g}$ and $r_{l}$ (Equation 4). Black dots show values of $r_{g}$ and $r_{l}$ for which $\tau$ = 62.7 ± 20% (S.E.M.). Red $⊕$ marks show the values of rate constants (Equation 3) used in this study at various volumes and NCaMKII. (C) For the fixed values of $r_{g}$ and $r_{l}$, three trajectories are shown at different CaMKII concentrations. As seen in the experimental data, the rate of colocalization increases with increasing CaMKII concentration. (D) For typical values of exchange rates used in this paper, we plotted simulation results (solid lines) with experimental values (dots) and their best exponential fit (dashed lines). The $d\tau/d[CaMKII]$ was −10.06 min/µM (data) and −18.54 min/µM (simulation). Source data are available at https://github.com/dilawar/SinghAndBhalla_CaMKII_SubunitExchange_2018/tree/master/PaperFigures/elifeFigure7 (Singh and Bhalla, 2018).

Next, we explored the space of $r_{l}$ and $r_{g}$ for which the time constant $\tau$ of colocalization dynamics matched well with the baseline case (i.e. $\tau$ for these trajectories were $\tau$[CaMKII] = 8 ± 20% (Figure 7B, black dots). From these values, we chose a combination of $r_{g}$ and $r_{l}$ which best explained the concentration-dependent changes in the rate of colocalization (Figure 7D). When compared with the data from Stratton et al., 2014), the time scale of colocalization and the concentration-dependent decrease in the rate of colocalization matched reasonably well for $r_{l}$ and $r_{g}$ that is, $\tau$ = 49.1 min (data) vs $\tau$ = 21.0 min (simulation) when [CaMKII] = 8 µM and $\tau$ = 119.0 min (data) vs $\tau$ = 150.0 min (simulation) when [CaMKII] = 1 µM, and, $\frac{d\tau}{d[CaMKII]}$ = -10.06 min/µM (data) vs $\frac{d\tau}{d[CaMKII]}$ = -18.05 min/µM (simulation) (Figure 7D). Note that we do not model the effect of diffusion, labelling efficiency, and experimental errors in the readout mechanism. Our values of $k_{x}^{+},k_{y}^{+},k_{x}^{-},k_{y}^{-}$ used in Equation 3 are close to estimated values of $r_{g}$ and $r_{l}$ (red cross vs. black dots in Figure 7B). Note that $r_{g}$ and $r_{l}$ are proxies for $k_{x}^{+},k_{y}^{+}$ and $k_{x}^{-},k_{y}^{-}$ respectively.

Thus, we are confident that rate parameters used in Equation 3 in our model are likely to be within the physiologically relevant range.

### PP1 deactivation

In the PSD, PP1 is the primary – and perhaps only – phosphatase known to dephosphorylate CaMKII (Strack et al., 1997b). We followed the MZ model for Equation 5 where inhibitor-1 (I1) inactivates PP1. Phosphorylated inhibitor-1 (I1P) renders PP1 inactive by forming I1P-PP1 complex (I1P.PP1).

$$
PP1+I1P⇌k_{4}k_{3}I1P.PP1I1P=I1\frac{v_{PKA}}{v_{CaN}}\frac{1+(\frac{Ca}{k_{H2}})^{3}}{(\frac{Ca}{k_{H2}})^{3}}
$$

where k3 = 100 /µM/s, k4 = 0.1 s-1 (Endo et al., 1996), and $v_{PKA}/v_{CaN}$ = 1 (Miller et al., 2005).

### Turnover

The turnover of CaMKII is a continuous process given by Equation 6 with rate $v_{t}=30⁢h^{-1}$ (Ehlers, 2003).

$$
x_{a}y_{6−a}→v_{t}x_{6}y_{0}for6\geqa\geq1x_{a}y_{7−a}→v_{t}x_{7}y_{0}for7\geqa\geq1
$$

### Diffusion and simulation method

Diffusion is implemented as a cross voxel jump reaction. Diffusion of a species X with diffusion-coefficient $D_{X}$ between voxel A and B separated by distance $h$ is modelled as a reaction $X_{A}⇌kkX_{B}$ where $k=D_{X}/h^{2}$, and $[X_{A}]=[X_{B}]=[X]/2$ (Erban et al., 2007). Based on our own numerical results (Appendix 1—figure 2) and other studies (Isaacson, 2009; Erban and Chapman, 2009), we are confident that $h\geq10⁢h_{c⁢r⁢i⁢t}$ where $h_{c⁢r⁢i⁢t}=\frac{k^{+}}{D_{P⁢P⁢1}+D_{s⁢u⁢b}}$ is a good value. We have hcrit ≤ 3.2 nm whenever DPP1 + Dsub ≥ 0.5 µm2 s−1. For all simulations presented in main text, we maintained $h\geqh_{c⁢r⁢i⁢t}$. For a few illustrative examples where $h$ is smaller than $h_{c⁢r⁢i⁢t}$, see Figure 4—figure supplement 1D,E.

All simulations were performed using the stochastic solver based on the Gillespie method, in the MOOSE simulator (https://moose.ncbs.res.in, version 3.1.4; Ray and Bhalla, 2008). This model is available at https://github.com/dilawar/SinghAndBhalla_CaMKII_SubunitExchange_2018 (copy archived at https://github.com/elifesciences-publications/SinghAndBhalla_CaMKII_SubunitExchange_2018). The table of parameters is in SI (Table 2).

### Method validation

To validate our implementation of diffusion, we compared trajectories of two systems: one in a single well-mixed cylinder with parameters tuned to elicit bistable behavior (henceforth, we call it the reference bistable), and a spatial system implemented as a discretized cylinder as described above. We expect the later to converge to reference bistable system when the diffusion constants become large such that the molecules are effectively well-mixed.

We put six CaMKII holoenzymes in a cylinder of length 180 nm discretized into six voxels, separated by a distance of 30 nm. The long-term behavior of discretized system was most sensitive to DPP1 (Figure 8B) and almost independent of Dsub (Figure 8A). The discretized system converges to reference bistable for DPP1 ≥ 0.5µm2s-1 (Figure 8C).

![Figure 8.](https://cdn.elifesciences.org/articles/41412/elife-41412-fig8-v2.jpg)

**Figure 8.:** NCaMKII = 6 holoenzymes as described in Figure 4 were simulated in a cylindrical arena divided into six voxels separated by 30 nm. Basal Ca2+ was set to 100 nM+$ϵ$. (A, above) For a typical value of DPP1 = 0.5 µm2 s−1 used in our model, varying Dsub did not result in loss of bistability of CaMKII activity. The distribution of state occupancy is shown for the case of Dsub = 0.1 µm2 s−1 in bar chart on the right. (A, below) Reference well-mixed system for comparison. Six holoenzyme were simulated in a single well-mixed cylinder of same length and volume, and with same parameter values as above. The distribution of state occupancy is shown on the right. (B) Cumulative histograms of CaMKII activity for various values of DPP1 and Dsub (unit µm2 s−1). The red and blue lines represent spatially discretized and well-mixed reference system (shown in A, black) respectively. The spatially discretized system (red) converges to the well-mixed system (blue) for higher DPP1 values. For fixed value of DPP1, changing Dsub has little or no effect on convergence. For a typical value of DPP1 = 0.5 µm2 s−1 , the system shows reasonable convergence (second row, also see A). (C) Quantification of convergence to well-mixed case. We used Kullback-Leibler divergence (relative entropy) to quantify the similarity between the state occupancy histograms (e.g. as in panel A) for the spatially extended case, and the reference well-mixed system, respectively. Identical histograms will have zero Kullback-Leibler divergence. The phase plot shows Kullback-Leibler divergence between the histograms for the spatially extended system and the reference bistable system. Black dots represent bistable configurations with at least four transitions observed in a simulation of the spatially discretized system, lasting 20 days. Thus, the spatially extended, discretized system converged to the behavior of the reference bistable system. Source data are available at https://github.com/dilawar/SinghAndBhalla_CaMKII_SubunitExchange_2018/tree/master/PaperFigures/elifeFigure8 (Singh and Bhalla, 2018).

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/41412/elife-41412-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** CaMKII/PP1 system was simulated in a cylindrical arena discretized into 6 voxels of equal volume separated by distance $h$ = 30 nm. (A) (above) For each voxel, the trajectory of active PP1 vs. time is plotted in blue. (below) Cross-correlation matrix of PP1 activity that is the $i⁢j$ entry of the matrix shows the value of correlation coefficient of PP1 activity inside voxel $i$ and inside voxel $j$ (Pearson product-moment correlation coefficient, using numpy.corrcoef function). (B,C) Same as A but with different value of DPP1 , 0.001 µm2 s−1 and 0.1 µm2 s−1, respectively. PP1 activity reduced in all voxels with increased DPP1. The correlation of PP1 activity among voxels did not improve with increased DPP1 therefore non-uniform distribution of PP1 in voxels is unlikely to be a significant contributor to the observed loss of PP1 potency. (D) PP1 activity decreased with increased DPP1 but remained independent of diffusion coefficient of subunit (Dsub). On the y-axis, PP1 activity is measured as ratio of sum of number of all active PP1 in all voxels during the simulation divided by the simulation time in hours. On top, dashed blue line (labeled blue DPP1 = 0) represents the case where PP1 was not allowed to diffuse. At bottom, dashed blue line (labeled blue1-voxel) shows the case where the cylinder consists only of 1 voxel and diffusion is instantaneous that is it is a well-mixed system. As expected, as DPP1 increased, the six voxels system converged to a well-mixed system of 1 voxel of 6x volume. Note that a similar effect is seen for a range of Dsub, including Dsub = $5$ µm2 s−1, for which $h_{crit}$ = 0.33 nm, satisfying the condition $h≫h_{c⁢r⁢i⁢t}$ (Isaacson, 2009; Erban and Chapman, 2009; also see Appendix 1—figure 2). Thus, we do not expect that this is a numerical artifact due to our use of cross-voxel jump reactions to approximate diffusion (Isaacson, 2009).

### Table of parameters

Table 2 summarizes the parameters of our model.

**Table 2.**
 Table of parameters used in model.


<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Parameter</th>
      <th>Value</th>
      <th>Reference/Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Vspine</td>
      <td>Volume of Spine</td>
      <td>1 to 5×10-20 m3</td>
      <td>(Bartol et al., 2015)</td>
    </tr>
    <tr>
      <td>VPSD</td>
      <td>Volume of PSD (Thickness 100⁢nm. Surface area 0.05µm2)</td>
      <td>1 to 5×10-21 m3</td>
      <td>Farley, 2015; Bartol et al., 2015</td>
    </tr>
    <tr>
      <td>NCaMKII</td>
      <td>Total CaMKII holoenzymes in PSD/Spine</td>
      <td>100 ± 18</td>
      <td>Farley, 2015</td>
    </tr>
    <tr>
      <td>NPP1</td>
      <td>Total PP1 in PSD Total PP1 in Spine</td>
      <td>4 to 20× NCaMKII 10 to 100× NCaMKII</td>
      <td>This paper This paper</td>
    </tr>
    <tr>
      <td>I1</td>
      <td>Concentration of free I1</td>
      <td>10 µM</td>
      <td>Miller et al., 2005</td>
    </tr>
    <tr>
      <td>VCaN</td>
      <td>Activity of calcineurin divided by its</td>
      <td>1</td>
      <td>Miller et al., 2005</td>
    </tr>
    <tr>
      <td>VCaM</td>
      <td>Activity of PKA divided by its Michaelis constant</td>
      <td>1 s-1</td>
      <td>Miller et al., 2005</td>
    </tr>
    <tr>
      <td>KM</td>
      <td>The Michaelis constant of PP1</td>
      <td>10 µM</td>
      <td>0.4 to 20 µM (Zhabotinsky, 2000)</td>
    </tr>
    <tr>
      <td>KH1</td>
      <td>Hill constant of CaMKII (Ca2+ ) activation)</td>
      <td>0.7 µM</td>
      <td>(De Koninck and Schulman, 1998)</td>
    </tr>
    <tr>
      <td>nH1</td>
      <td>Hill constant of CaMKII (Ca2+ ) activation)</td>
      <td>3</td>
      <td>(Stemmer and Klee, 1994)</td>
    </tr>
    <tr>
      <td>KH2</td>
      <td>Hill constant of CaMKII (Ca2+ ) activation)</td>
      <td>0.3 µM</td>
      <td>(Stemmer and Klee, 1994)</td>
    </tr>
    <tr>
      <td>nH2</td>
      <td>Hill constant of CaMKII (Ca2+ ) activation)</td>
      <td>3</td>
      <td>(Stemmer and Klee, 1994)</td>
    </tr>
    <tr>
      <td>k1</td>
      <td>The catalytic constant of autophospho-rylation</td>
      <td>1.5 s-1</td>
      <td>(Hanson et al., 1994)</td>
    </tr>
    <tr>
      <td>k2</td>
      <td>The catalytic constant of autophospho-rylation</td>
      <td>1 s-1</td>
      <td>(Bradshaw et al., 2003; Ichikawa et al., 1996)</td>
    </tr>
    <tr>
      <td>k3</td>
      <td>The association rate constant of PP1.I1P complex</td>
      <td>100 µM-1s-1</td>
      <td>(Endo et al., 1996; Miller et al., 2005)</td>
    </tr>
    <tr>
      <td>k4</td>
      <td>The dissociation rate constant of PP1.I1P complex</td>
      <td>0.1 s-1</td>
      <td>(Endo et al., 1996; Miller et al., 2005)</td>
    </tr>
    <tr>
      <td>kx+</td>
      <td>The rate of adding unphosphorylated subunit x</td>
      <td>1 s-1 per NCaMKII</td>
      <td>This paper</td>
    </tr>
    <tr>
      <td>ky+</td>
      <td>The rate of adding phosphorylated sub- unit y</td>
      <td>1 s-1 per NCaMKII</td>
      <td>This paper</td>
    </tr>
    <tr>
      <td>kx-</td>
      <td>The rate of losing unphosphorylated subunit x</td>
      <td>0.1 s-1</td>
      <td>This paper</td>
    </tr>
    <tr>
      <td>ky-</td>
      <td>The rate of losing phosphorylated sub- unit y</td>
      <td>0.1 s-1</td>
      <td>This paper</td>
    </tr>
    <tr>
      <td>vt</td>
      <td>Turnover rate of CaMKII</td>
      <td>30 h-1</td>
      <td>(Ehlers, 2003; Miller et al., 2005)</td>
    </tr>
    <tr>
      <td>DPP1</td>
      <td>Diffusion coefficient of PP1</td>
      <td>0.5 µm2 s−1</td>
      <td>This paper and (Harvey et al., 2008)</td>
    </tr>
    <tr>
      <td>Dsub</td>
      <td>Diffusion coefficient of CaMKII subunits</td>
      <td>10-5 – 10µm2 s−1</td>
      <td>This paper</td>
    </tr>
  </tbody>
</table>
