# Mechanisms underlying the response of mouse cortical networks to optogenetic manipulation

## Authors

- Alexandre Mahrach<sup>1</sup> ([ORCID: 0000-0002-9077-5808](https://orcid.org/0000-0002-9077-5808))
- Guang Chen<sup>2</sup>
- Nuo Li<sup>2</sup>
- Carl van Vreeswijk<sup>1</sup>
- David Hansel<sup>1</sup> ([ORCID: 0000-0002-1352-6592](https://orcid.org/0000-0002-1352-6592)) †

### Affiliations

1. CNRS-UMR 8002, Integrative Neuroscience and Cognition Center Paris France
2. Department of Neuroscience Baylor College of Medicine Houston United States

† Corresponding author

## Abstract

GABAergic interneurons can be subdivided into three subclasses: parvalbumin positive (PV), somatostatin positive (SOM) and serotonin positive neurons. With principal cells (PCs) they form complex networks. We examine PCs and PV responses in mouse anterior lateral motor cortex (ALM) and barrel cortex (S1) upon PV photostimulation in vivo. In ALM layer five and S1, the PV response is paradoxical: photoexcitation reduces their activity. This is not the case in ALM layer 2/3. We combine analytical calculations and numerical simulations to investigate how these results constrain the architecture. Two-population models cannot explain the results. Four-population networks with V1-like architecture account for the data in ALM layer 2/3 and layer 5. Our data in S1 can be explained if SOM neurons receive inputs only from PCs and PV neurons. In both four-population models, the paradoxical effect implies not too strong recurrent excitation. It is not evidence for stabilization by inhibition.

## Introduction

Local cortical circuits comprise several subclasses of GABAergic interneurons which together with the excitatory neurons form complex recurrent networks (Goldberg et al., 2004; Jiang et al., 2015; Karnani et al., 2016; Markram et al., 2004; Moore et al., 2010; Pfeffer et al., 2013; Tasic et al., 2018; Tremblay et al., 2016). The architecture of these networks depends on the cortical area and layer (Beierlein et al., 2003; Jiang et al., 2013; Rudy et al., 2011; Xu et al., 2013; Xu and Callaway, 2009).

Optogenetics is now classically used to reversibly inactivate a particular cortical area or neuronal population to get insights into their functions (Atallah et al., 2012; Guo et al., 2014b; Lee et al., 2012; Li et al., 2015; Svoboda and Li, 2018). Optogenetics has also been applied to isolate the different components (e.g. feedforward vs. recurrent) of the net input into cortical neurons (Lien and Scanziani, 2018; Lien and Scanziani, 2013). It can also be used to experimentally probe the architecture of local cortical circuits (Moore et al., 2018; Xu et al., 2013). However, because of the complexity of these networks and of their nonlinear dynamics, qualitative intuition and simple reasoning (e.g. ‘box-and-arrow’ diagrams) are of limited use to interpret the results of these manipulations.

‘Paradoxical effect’ designates the phenomenon that stimulation of a GABAergic interneuron population not only decreases the average activity of the principal cells (PCs) but also decreases the activity of the stimulated population (Murphy and Miller, 2009; Ozeki et al., 2009; Tsodyks et al., 1997). Intuitively, paradoxical effect arises when the stimulation induces a strong activity suppression in the PCs (Kato et al., 2017; Moore et al., 2018), such that the overall (synaptic+stimulus) excitation to the stimulated population decreases. However, the precise conditions under which the paradoxical effect occurs are difficult to establish without mathematical modeling.

In simple models consisting of only two populations (one excitatory and one inhibitory) these conditions have been mathematically derived. The paradoxical effect occurs when the networks operates in the regime known as inhibition stabilized (inhibition stabilized networks, ISN) in which the total the total recurrent excitation is so strong that inhibition is necessary to prevent a blow up in the activity (Murphy and Miller, 2009; Ozeki et al., 2009; Tsodyks et al., 1997). Networks, with several inhibitory populations have been recently investigated (Garcia Del Molino et al., 2017; Litwin-Kumar et al., 2016; Sadeh et al., 2017). These studies considered network models with synaptic currents small compared to neuronal rheobase currents (Gerstner et al., 2014; Lapicque, 1909). However, interactions in cortex are stronger than what is assumed in these studies (Shadlen and Newsome, 1994).

Simple networks with strong interactions comprising one excitatory and one inhibitory population have been studied extensively. In a broad parameter range not requiring fine-tuning, such networks dynamically evolve into a state in which strong excitation is balanced by strong inhibition such that the net input into the neurons is comparable to their rheobases (van Vreeswijk and Sompolinsky, 1998; van Vreeswijk and Sompolinsky, 1996). The theory of balanced networks has been developed for a variety of single neuronal models including binary neurons (van Vreeswijk and Sompolinsky, 1998; van Vreeswijk and Sompolinsky, 1996), rate models (Harish and Hansel, 2015; Kadmon and Sompolinsky, 2015), leaky-integrate-and fire neurons (Hansel and Mato, 2013; Mongillo et al., 2012; Rosenbaum and Doiron, 2014; Roxin et al., 2011; Van Vreeswijk and Sompolinsky, 2005) and conductance-based models (Hansel and van Vreeswijk, 2012; Pattadkal et al., 2018).

In the present study, we investigate experimentally the effects of the photostimulation of PV interneurons on the anterior lateral motor cortex (ALM) and barrel cortex (S1) of the mouse. We show that two-population network models do not suffice to account for these effects. To overcome this limitation, we develop a theory for the paradoxical effect in balanced networks that takes into account the multiplicity of GABAergic neuronal populations. Combining analytical calculations and numerical simulations, we study the responses of these networks at population and single neuron level. For two-population balanced networks it has been shown that the paradoxical effect only occurs when the network is inhibition stabilized (Pehlevan and Sompolinsky, 2014; Wolf et al., 2014). Here we show that in contrast, in four-population networks, the paradoxical effect can occur even if the network is not inhibition stabilized. We conclude with prescriptions for experiments that according to the theory can be informative about network architectures in cortex.

## Results

## ALM layer 5 and S1 exhibit paradoxical effect but not ALM layer 2/3

We expressed a red-shifted channelrhodopsin (ReaChR) in PV interneurons to optogenetically drive local inhibition in the barrel cortex (S1) and anterior lateral motor cortex (ALM) of awake mice (Hooks et al., 2015). We used orange light (594 nm) to illuminate a large area of ALM or S1 (2 mm diameter), photostimulating a large proportion of PV interneurons (Figure 1A). We measured the light-induced effects on neural activity using silicon probe recordings. In both brain areas, putative PCs and putative PV neurons were identified based on spike width (Methods). Neurons with wide spikes were likely mostly PCs. Units with narrow spikes were fast spiking (FS) neurons and likely expressed parvalbumin (Cardin et al., 2009; Guo et al., 2014b; Olsen et al., 2012; Resulaj et al., 2018). We investigated the responses of these neurons as a function of the photostimulation intensity in ALM layer 2/3 and layer 5, and in S1.

![Figure 1.](https://cdn.elifesciences.org/articles/49967/elife-49967-fig1-v3.jpg)

**Figure 1.:** (
A) Scheme of the experiment. (B–C) Normalized spike rate as a function of laser intensity in different layers and brain areas. Top, individual neuron responses of the PCs (red) and PV (blue) neurons; bottom, population average responses. (B) ALM: layer 2/3: n = 26 (PCs), n = 9(PV); (C) ALM layer 5: n = 62 (PCs), n = 12 (PV). (D) S1: n = 52 (PCs), n = 8 (PV). Mean ± s.e.m. across neurons, bootstrap. (E) Comparison of PV neurons’ normalized spike rates between ALM Layer 2/3 and Layer five at laser intensity 0.5 mW/mm2. (F).Slope of PCs and PVs’ normalized spike rate as a function of laser intensity. Data from ALM layer 5. Slopes are computed using data from 0.3 mW/mm2 and below, before the spike rate of PV neurons begin to increase. Mean ± SEM, bootstrap (Methods). (G) Same as (F) but for data from S1. In (F and G) the difference between the slopes for the PC and PV populations is not significant.

We found that in all recorded layers and areas, the population average activity of the PCs decreased with the optogenetic drive (Figure 1B, Figure 2). In contrast in ALM, the PV population exhibited a behavior which depended on the recorded layer.

![Figure 2.](https://cdn.elifesciences.org/articles/49967/elife-49967-fig2-v3.jpg)

**Figure 2.:** Dots correspond to individual neurons. Laser intensity is 0.5 mW/mm
2. Pie charts represent the fraction of neurons with different types of changes. Mean ± s.e.m. bootstrap. Black, fraction of neurons with activity increase larger than 0.1 Hz. Light gray, fraction of neurons with activity decrease larger than 0.1 Hz. Dark gray, fraction of neurons with activity change smaller than 0.1 Hz. White, fraction of neurons with activity smaller than 0.1 Hz upon PV photostimulation.

In ALM layer 2/3, the population average firing rate of PV neurons monotonically increased with the photostimulation intensity. However, individual neuron responses were heterogeneous. Most PV neurons increased their spike rates from baseline with increased photostimulation intensity. Some PV neurons initially decreased their spike rates below baseline for low light intensity.

In ALM layer 5, the response of the PV population was non-monotonic. For low laser intensity, their activity paradoxically decreased with the optogenetic drive. The slope of the normalized firing rate v.s. laser intensity was significantly different from zero for both the PC and PV populations (Figure 1F). The ratio of their slopes was 0.62 ± 0.28. At high photostimulation intensity, the activity of the PV population increased. At intermediate photostimulation intensity (0.5 mW/mm2), the response of the PV neurons was significantly different between layer 2/3 and layer 5 (Figure 1E, p<0.005, unpaired t-test, two-tailed test).

Paradoxical decrease in PV neurons activity with the optogenetic drive was also observed in S1. Remarkably, the concomitant decrease of the PC and the PV population activities was proportional (Figure 1G, ratio of slopes PV/PC, mean ± SEM; S1, 1 ± 0.29).

In both ALM layer 5 and S1, there was also a large diversity of responses. Most PV neurons decreased their activity at low photostimulation intensity. At high laser intensity (5 mW/mm2), a fraction of PV neurons (6/12 in ALM layer 5 and 6/10 in S1) had a larger response than baseline, while the rest remained suppressed. Figure 2 shows the spike rates of PCs and PV neurons at an intermediate light intensity (0.5 mW.mm-2).

## Network models

To assess the network mechanisms which may account for the experimental data from ALM and S1, we first considered models consisting of one excitatory and one inhibitory population. Since it is well established that cortical circuits involve a variety of inhibitory subpopulations, we later extended the theory to network models of four populations of neurons representing PCs and three subtypes of GABAergic interneurons in cortex. In all our models, neurons are described as integrate-and-fire elements. The data we seek to account for, were obtained in optogenetic experiments in which the laser diameter was substantially larger than the spatial range of neuronal interactions and comparable to the size of the area in which activity was recorded. Therefore, in all our models, we assume for simplicity that the connectivity is unstructured. We modeled the ReachR-optogenetic stimulation of the PV population as an additional external input, 



I


o
p
t
o



, into PV neurons. We assumed that it depends on the intensity of the laser, 



Γ


o
p
t
o



, as 



I


o
p
t
o


=


I


0


l
o
g


1
+




Γ


o
p
t
o






Γ


0







 where 



I


0



 and 



Γ


0



 are parameters (Figure 3—figure supplement 1; Hooks et al., 2015).

## Two-population model

The two-population network is depicted in Figure 3A. It is characterized by four recurrent interaction parameters, 



J


α
β



, and two feedforward interaction parameters, 



J


α
0



, 

α
,
β
∈
{
E
,
I
}

 (see Materials and methods).

Results from numerical simulations of the model are depicted in Figure 3B and C where, the dependence of the population activities normalized to baseline, are plotted against the intensity of the laser, 



Γ


o
p
t
o



. Figure 3B shows the response of the network where the recurrent excitation, JEE
, is non zero. The activity of the PV population, r1
 varies non-monotonically with the laser intensity. For small intensities, r1
 paradoxically decreases together with the activity of the PCs, rE
. This paradoxical effect stems from the fact that the decrease in the activity of the PCs yields a reduction in the excitation to PV neurons which is not compensated for by the optogenetic drive. As a result, the net excitation to PV neurons diminishes yielding a decrease in rI
. When rE
 becomes very small, this mechanism does not operate anymore and consequently, rI
 increases as 



Γ


o
p
t
o



 is increased further. In Figure 3C, JEE
 is zero, rI
 monotonically increases with the light intensity whereas rE
 monotonically decreases. For small intensities, rI
 is close to a constant. It starts to increase appreciably only when 



r


E


≃
0

. Therefore, the PV response is not paradoxical.

Qualitatively this model seems to account for our experimental data from ALM layer 2/3, ALM layer 5 and S1. It would imply that in layer 5, JEE
 is sufficiently large to generate the paradoxical effect, while in layer 2/3 this is not the case. On closer inspection however, there are major discrepancies between the simulation results and the experimental data. In our recordings in both ALM layer 5 and S1, the PV population activity reaches a minimum while the PCs are still significantly active: relative to baseline the activity is 40% in ALM and 25% in S1. In contrast, in the two-population model, the minimum of the PV activity is reached (Appendix 1B) when excitatory neurons are virtually completely silenced (Figure 3B, Figure 3—figure supplement 2A). In fact one can show that for sufficiently large K, when rI
 is minimum, the activity of the excitatory population is exponentially small in K. As a result, to account for the data one needs to assume that 

K
≃
10

.

In addition, in the experimental data the activities of the PC and PV populations in S1 decrease in equal proportions before the minimum of the PV activity (Figure 1B). This cannot be accounted for in a two-population model unless parameters are fine-tuned (Figure 3—figure supplement 3). Analytical calculations (Appendix 1B) supplemented with numerical simulations show that this proportional decrease only happens when the determinant of the interaction matrix, J
αβ, is close to zero. Moreover, the external input must also be fine-tuned so that the neurons have biologically realistic firing rates (Figure 3—figure supplement 3).

The experimental data from ALM layer 2/3 show that for already small light intensity the activity of PV neurons increases appreciably. This is in contrast with Figure 3C. In Figure 3—figure supplement 2B, we show that the two-population model can account for this feature only if the recurrent excitation is very weak in that layer and the connectivity is extremely sparse.

These discrepancies prompted us to investigate whether models with several populations of inhibitory neurons can account for our experimental data without fine-tuning. We focus on two four-population network models. Both consist of three populations representing PCs, PV and SOM neurons and a fourth population representing other inhibitory neurons. The main difference between the two models lies in the inhibitory populations from which SOM neurons receive inputs.

## A four-population model with V1-like architecture (Model 1)

We first investigated the dynamics of a four-population network with an architecture that is similar to the one reported in layer 2/3 in V1 (Pfeffer et al., 2013) and S1 (Lee et al., 2013) (Figure 4A). The model consists of four populations representing PCs, PV, SOM and VIP neurons. SOM neurons do not interact with each other (Adesnik et al., 2012; Gibson et al., 1999; Hu et al., 2011). VIP neurons only project to the SOM population (Jiang et al., 2015; Pfeffer et al., 2013). All neurons except SOM receive inputs from sources external to the network (e.g. thalamus) (Beierlein et al., 2003; Beierlein et al., 2000; Cruikshank et al., 2010; Ma et al., 2006; Xu et al., 2013). The same architecture was considered in Litwin-Kumar et al. (2016).

Following Pfeffer et al. (2013), the PV population does not project to the SOM population. Other studies have reported such a connection (Jiang et al., 2015). However, adding such a connection to Model 1 does not qualitatively affect the PC and PV responses (see Appendix 1C).

We considered parameter sets such that: 1) At baseline, the network is operating in the balanced state with all populations active; 2) the activity of the PC population decreases with the laser intensity as observed in our experiments.

## Theory in the large N, K limit

It is instructive to consider the limit in which the number of neurons in the network, N, and the average number of connections per neuron, K, go to infinity. In this limit, the analysis of the stationary state of the network simplifies (see Materials and methods). This stems from the fact that when interactions are numerous, excitatory and inhibitory inputs are strong and only populations for which excitation is balanced by inhibition have a finite and non-zero activity. The average activities of the four populations are then completely determined by four linear equations, the balance equations, which reflect this balance. Solving this system of equations yields the population activities, rα
, α = E, I, S, V, as a function of the external inputs to the network. In particular, when the laser intensity is sufficiently small, the four populations are active and their firing rates vary linearly with the current induced by the photostimulation (Appendix 1C).

Figure 4 plots the activities of the populations vs. the optogenetic input into PV neurons, Iopto
, for two sets of interaction parameters. In Figure 4B, the activity of the PV population, rI
, increases with Iopto
. In contrast, in Figure 4C, rI
 decreases with Iopto
: the response of the PV population is paradoxical.

To characterize for which interaction parameters the PV response is paradoxical, we consider the 4 × 4 susceptibility matrix 





χ


α
β





. The element 



χ


α
β




α
,
β
=
E
,
I
,
S
,
V



 is the derivative of the population activity,



r


α



, with respect to a small additional input, into population 

β

, 



I


β



. Evaluated for small 



I


β



, 



χ


α
β



 characterizes by how much rα
 varies with an increasing but weak extra input into population β. Its sign indicates whether rα
 increases or decreases with I
β. The elements of the susceptibility matrix can be decomposed in several terms corresponding to the contributions of different recurrent loops embedded in the network (Appendix 1C). Using this decomposition one can show whether the PV response is paradoxical or not depends on the interplay between two terms. One is the gain of the disinhibitory feedback loop PC-VIP-SOM-PC and the other is the product of the recurrent excitation, JEE
, with the gain of the disinhibitory feedback loop VIP-SOM-VIP (Figure 4—figure supplement 1). Remarkably, PV neurons are not involved in these two terms. A straightforward calculation (Equation A37) then shows that the response of PV neurons increases with Iopto
 if the recurrent excitation is sufficiently strong, namely if
(1)




J

E
E


>

J

E
E


∗


=

J

V
E



J

E
S



/


J

V
S

The denominator in 



J


E
E


*



 is the strength of the connection from the SOM population to the VIP population. The numerator is the gain of the pathway which connects these two populations via the PCs. When 




J

E
E


>

J

E
E


*





 the negative contribution of the disinhibitory loop PC-VIP-SOM-PC dominates in the expression of 



χ


I
I



. It is the opposite when 




J

E
E


<

J

E
E


∗





. The stability of the balanced state provides other necessary conditions that the interactions must satisfy (see Materials and methods). In particular, the determinant of the interaction matrix, J, must be positive.

The difference between the behaviors in Figure 4B and C can now be understood as follows: in Figure 4B, 




J

E
E


>

J

E
E


*





 and 




χ

I
I


=
1.6
>
0



, thus, 



r


I



 increases with Iopto
; in Figure 4C, 




J

E
E


<

J

E
E


∗





 and 




χ

I
I


=
−
5.1
<
0



 and thus, rI
 decreases. Remarkably, in both cases the activities of the PC and VIP populations normalized to baseline, are always equal (Figure 4B–C, right panel). This is a consequence of the balance of excitatory and inhibitory inputs into the SOM population which implies that rE
 and rV
 are proportional (see Materials and methods, Equation 19.3).

In Figure 4B, the activity of the SOM population decreases with the laser intensity. This also stems from the fact that 




J

E
E


>

J

E
E


*





 (Appendix 1C, Equations A31-34). This qualitative behavior is therefore independent of parameter sets, provided that inequality (1) is satisfied. In contrast, for parameters for which 




J

E
E


<

J

E
E


∗





 the activity of the SOM population either decreases or increases with Iopto
 depending on other parameters. Moreover, it is straightforward to prove that if 




J

E
E


>

J

E
E


*





, the product 



χ


E
I




χ


I
E



 is positive (Appendix 1C). Since we assumed that rE
 decreases upon photostimulation of PV neurons, namely 




χ

E
I


<
0



, this implies that 



χ


I
E



 is also negative. In other words, in Model 1, a non-paradoxical response of the PV population upon PV photostimulation implies that the PV activity decreases when PCs are photostimulated.

When Iopto
 is sufficiently large, the solution of the four balance equations will contain one or more populations for which rα
 < 0. Obviously such a solution is inconsistent. Instead, other solutions should be considered where at least one population has a firing rate which is zero and the firing rates of the other populations is determined by a new system of linear equations with lower dimensions (see Materials and methods, Appendix 1C). Consistency requires that in these solutions the net input is hyperpolarizing for the populations with rα
 = 0. As a consequence, the network population activities are in general piecewise linear in Iopto
 (Figure 4—figure supplement 2).

The large N, K analysis provides precious insights into the dynamics of networks with reasonable size and connectivity. In particular, we will show that the criterion for the paradoxical effect, Equation 1, remains valid up to small corrections. Although it is possible to treat analytically the dependence of rα
 on Iopto
 for finite K, these calculations are very technical and beyond the scope of this paper. Instead here, we proceed with numerical simulations.

## Numerical simulations for 




J

E
E


>

J

E
E


*

Figure 5 depicts the results of our numerical simulations of Model 1 for the same parameters as in Figure 4B (see Materials and methods, Tables 3–4). The response of PV neurons is non-paradoxical: the activity of the PV population increases monotonically with 



Γ


o
p
t
o



 in the whole range (Figure 5A). Concurrently, the population activities of PC, SOM and VIP neurons monotonically decrease with 



Γ


o
p
t
o



 (Figure 5A-B). For sufficiently large 



Γ


o
p
t
o



, PCs become very weakly active and the SOM and VIP populations dramatically reduce their firing rates. The variations with 



Γ


o
p
t
o



 of rE, rI, rS
 and rV
 and are robust to changes in the average connectivity, K (Figure 5—figure supplement 1) and in qualitative agreement with the predictions of the large N, K limit (Figure 4B Appendix 1C, Figure 4—figure supplement 2).

To test the robustness of our results with respect to changes in the interaction strengths, we generated 100 networks with J
αβ chosen at random within a range of ±10% of those of Figure 4B. All the networks exhibited a balanced state which was stable with respect to slow rates fluctuations in the large N, K limit. We simulated those networks with K = 500 and computed the population activity at baseline and for 



Γ


o
p
t
o


=
0.07
m
W
.
m


m


-
2



. For all these networks, the results were consistent with the one of the control set: for 



Γ


o
p
t
o


=
0.07
m
W
.
m


m


-
2



, 



r


I



 was larger and rE, rS, rV
 were smaller than baseline (Figure 5—figure supplement 2). However, a small percentage of these networks (10%) exhibited oscillations with at most an amplitude 20% of their mean in the firing rates. Apart from that, the results were robust to changes in J
αβ.

In contrast to what happens in the large N, K limit (Figure 4B, right panel), in the results depicted in Figure 5 the activity of the PC and VIP populations are not proportional. Moreover, in the large K limit, PC and VIP neurons are inactivated before the SOM population is. For K = 500, VIP is the first population to be silenced followed by the SOM and finally the PC population. Simulations with increasing values of K show that these differences are due to substantial finite K effects (Figure 5—figure supplement 1).

Figure 5 also depicts the changes in the firing rates (normalized to baseline) with 



Γ


o
p
t
o



 for several example neurons. These changes are highly heterogeneous across neurons within each population. Whereas the population average varies monotonically, individual cells activity can either increase or decrease and the response can even be non-monotonic with 



Γ


o
p
t
o



.

The heterogeneity in the single neuronal responses are also clear in Figure 6A–B that plots, for two different light intensities, the perturbed firing rate vs. baseline for PCs and PV neurons. Remarkably, in both populations a significant fraction of neuron exhibits a response which is incongruous with the population average. The pie charts in Figure 6 depict the fraction of PCs and PV neurons which increased, decreased, or did not change their firing rates. The fraction of neurons whose activity is almost completely suppressed, is also shown. Remarkably, even for 



Γ


o
p
t
o


=
1.0
m
W
.
m


m


-
2



, some of the PCs show an activity increase. Moreover, the fraction of PV neurons whose firing rate increases is less for 



Γ


o
p
t
o


=
1.0
m
W
.
m


m


-
2



 than 



Γ


o
p
t
o


=
0.5
m
W
.
m


m


-
2



. It should be noted that in the model all PV neurons receive the same optogenetic input, therefore, the heterogeneity in the response is not due to whether or not the PV neurons were “infected”. This heterogeneity is solely due to the randomness in the connectivity.

![Figure 6.](https://cdn.elifesciences.org/articles/49967/elife-49967-fig6-v3.jpg)

**Figure 6.:** ).







J


E
E
>


J


E
E


*
(
A) Single neuron firing rates at baseline vs. at 
. (





Γ


o
p
t
o
=
0.5
m
W
.
m




m


-
2
B) Same for 
. Top: PCs (red). Bottom: PV neurons (blue). Scatter plots of 300 randomly chosen PC and PV neurons. Pie charts for the whole population. The pie charts show the fraction of neurons which increase (black) or decrease (light gray) their activity compared to baseline. Dark gray: Fraction of neurons with relative change smaller than 0.1Hz. White: fraction of neurons with activity smaller than 0.1Hz upon PV photostimulation. Firing rates were estimated over 100s. Neurons with rates smaller than 0.01Hz are plotted at 0.01Hz. Parameters as in 





Γ


o
p
t
o
=
1
m
W
.
m




m


-
2
Figure 5.

## Numerical simulations for 




J

E
E


<

J

E
E


∗

Figure 7 depicts the results of our numerical simulations of Model 1 when 




J

E
E


<

J

E
E


∗





. Parameters are the same as in Figure 4C (see Materials and methods, Tables 3–5). The population activities of PCs and VIP neurons, rE
 and rV
, decrease monotonically with the laser intensity, 



Γ


o
p
t
o



. Conversely, the variations of the activities of the PV and SOM populations, rI
 and rS
, are non-monotonic with 



Γ


o
p
t
o



. For small light intensities, rI
 decreases and then abruptly increases with larger 



Γ


o
p
t
o



; rS
 exhibits the opposite behavior. Remarkably, when rI
 is minimum, rS
 is maximum for nearly the same value of 



Γ


o
p
t
o



. We show in Figure 7—figure supplement 1 that this proportional decrease only happens in a small region of parameter space when the determinant of the interaction matrix, 



J


α
β



 
ϵ


β



, is close to zero.

This behavior is qualitatively similar to the one derived in the large N, K limit (Figure 4—figure supplement 2). As suggested by the large N, K analysis, the paradoxical response of the PV neurons in the simulations, is driven by the positive feedback loop PC-VIP-SOM-PC (Figure 4—figure supplement 1). Remarkably, when the activity of the PV neurons is minimum, the PCs are still substantially active (40% of baseline level). This is due to finite K corrections to the large N, K predictions (Figure 7—figure supplement 2). These corrections are strong and scale as 



1



K




 (Appendix 1C). Indeed, even for K as large as 2000, rE
 is still 25% of the baseline when 



r


I



 is minimum.

We checked the robustness of these results with respect to changes in the interaction parameters as we did for 




J

E
E


>

J

E
E


*





. We found that for small light intensity all the 100 simulated networks were operating in the balanced state and exhibited the paradoxical effect (Figure 7—figure supplement 3).

Finally, the single neuron responses are highly heterogeneous. Figure 8 plots the perturbed activities of PCs and PV neurons vs. their baseline firing rates for two light intensities. In Figure 8A, the PV response is paradoxical. This is not the case in Figure 8B. Interestingly, the fraction of PV neurons incongruous with the population activity is larger for 



Γ


o
p
t
o


=
0.5
m
W
.
m


m


-
2



 than for 



Γ


o
p
t
o


=
1.0
m
W
.
m


m


-
2



. For both light intensities the activity of almost all the PCs is decreased.

![Figure 8.](https://cdn.elifesciences.org/articles/49967/elife-49967-fig8-v3.jpg)

**Figure 8.:** ).







J


E
E
<


J


E
E


∗
(
A) Single neuron firing rates at baseline vs. at 
. (





Γ


o
p
t
o
=
0.5
m
W
.
m




m


-
2
B) Same for 
. Top: PCs. Bottom: PV neurons. Scatter plots of 300 randomly chosen PC and PV neurons. Pie charts for the whole population. Firing rates were estimated over 100s simulation time. Neurons with rates smaller than 0.01Hz are plotted at 0.01Hz. Color code as in 





Γ


o
p
t
o
=
1
m
W
.
m




m


-
2
Figure 6. Parameters as in Figure 7.

## Four-population network: Model 2

In S1, in the range of laser intensities in which the PV response is paradoxical, the decrease of the PC and PV activity is proportional. This feature of the data can be accounted for in Model 1 but only with a fine-tuning of the interaction parameters (Figure 7—figure supplement 1 and Figure 7—figure supplement 4). This prompted us to investigate whether a different architecture could account robustly for this remarkable property. Our hypothesis is that this property is a direct consequence of the balance of excitation and inhibition.

## Theory in the large 

N
,
K

 limit

We first considered the three-population model depicted in Figure 9A. It consists of the PC, PV and SOM populations. SOM neurons receive strong inputs from PCs and PV neurons, but do not interact with each other and do not receive feedforward external inputs. In the large N, K limit, the balance of excitation and inhibition of the SOM population reads (see Materials and methods, Equation 20.2).
(2)



J


S
E




r


E


-


J


S
I




r


I


=
0

Therefore, the activities of the PC and PV populations are always proportional. However, as we show in (Appendix 1D) a three-population network with such an architecture cannot exhibit the paradoxical effect.

We therefore considered a network model in which a third inhibitory population, referred to as ‘X’, is added without violating Equation (3) (Figure 9B). This requires that SOM neurons do not receive inputs from X neurons (Appendix 1D). This network exhibits the paradoxical effect if and only if 




J

S
E



J

E
X



J

X
S


>

J

X
X



J

E
S



J

S
E





, that is if the gain of the positive feedback loop, SOM-X-PC-SOM, is sufficiently strong (Appendix 1D). Obviously, this condition simplifies and reads
(3)




J

E
X



J

X
S


>

J

X
X



J

E
S

Remarkably, this inequality does not depend on JEE
. This is in contrast to what happens in Model 1 where the paradoxical effect occurs only if JEE
 is small enough (see Equation (2)).

As in Model 1, we further required that the activity of the PC population increases with its feedforward external input. This adds the constraint (Appendix 1D):
(4)




J

I
X



J

X
S


>

J

X
X



J

I
S

Equations (3-5) do not depend on JXI
. For simplicity, we take JXI 
=0 and refer to the resulting architecture as Model 2.

In Figure 9C, the slope of the PV population activity changes from negative to positive while PCs are still active. This is because if SOM neurons are completely suppressed, the loop SOM-X-PC-SOM which is responsible for the paradoxical effect, is not effective anymore. Interestingly, the analytical calculations also show that, when the SOM population activity vanishes, the activity of the X population is maximum. Since the SOM population is inactive before PCs, there is a range of laser intensities where the activity of the latter keeps decreasing while the activity of the PV population increases. Once PCs are inactive, the activity of the X population do not vary with Iopto
. This is because then they only receive a constant feedforward excitation from outside the network which is balanced by their strong recurrent mutual coupling, JXX
.

## Simulations for finite K

These features are also observed in our simulations depicted in Figure 10. For small laser intensities, the network exhibits a paradoxical effect where the activities of the PC and PV populations decrease with 



Γ


o
p
t
o



 and in a proportional manner (Figure 10A), until the SOM neurons become virtually inactive (Figure 10B). At that value, rI
 is minimum and rX
 is maximum. For larger 



Γ


o
p
t
o



, rI
 increases while rE
 keeps decreasing and is still substantial. After rE
 has vanished, rX
 saturates but rI
 continues to increase. All these results are robust to changes in the connectivity, K (Figure 10—figure supplement 1) as well as to changes in the interaction parameters (Figure 10—figure supplement 2). Single neuron responses are more heterogeneous than in the experimental data (Figure 11). It should be noted however that we did not tune parameters to match the experimental heterogeneity.

![Figure 11.](https://cdn.elifesciences.org/articles/49967/elife-49967-fig11-v3.jpg)

**Figure 11.:** (
A) Single neuron firing rates at baseline vs. at 
. (





Γ


o
p
t
o
=
0.5
m
W
.
m




m


-
2
B) Same for 
. Top: PCs. Bottom: PV neurons. Scatter plots of 300 randomly chosen PC and PV neurons. Pie charts for the whole population. Firing rates were estimated over 100s. Neurons with rates smaller than 0.01Hz are plotted at 0.01Hz. Color code as in 





Γ


o
p
t
o
=
1
m
W
.
m




m


-
2
Figure 6. Parameters as in Figure 10.

## Discussion

We studied the response of cortex to optogenetic stimulation of parvalbumin positive (PV) neurons and provided a mechanistic account for it. We photostimulated the PV interneurons in layer 2/3 and layer 5 of the mouse anterior motor cortex (ALM). In layer 2/3 photostimulation increased PV activity and decreased the response of the PCs on average. In contrast, in layer five the response of the PV population was paradoxical: both PC and PV activity decreased on average. This is similar to what we found in the mouse somatosensory cortex (S1) (Li et al., 2019). To account for these results, we first investigated the dynamics of networks of one excitatory and one inhibitory population of spiking neurons. We showed that two-population network models of strongly interacting neurons do not fully account for the experimental data. This prompted us to investigate the dynamics of networks consisting of more than one inhibitory population.

We considered two network models both consisting of one excitatory and three inhibitory populations. Interneurons are known to be unevenly distributed throughout the cortex. For instance, SOM neurons have been reported to be most prominent in layer five whereas VIP neurons are mostly found in layer 2/3 (Tremblay et al., 2016). Instead of giving a complete description of these layers and all neuronal populations they include, we propose here models with the minimal number of inhibitory populations that can account for the data.

The three inhibitory populations in Model 1 represent PV, somatostatin positive (SOM) and vasoactive intestinal peptide (VIP) interneurons with a connectivity similar to the one reported in primary visual cortex (Pfeffer et al., 2013) and S1 layer 2/3 (Lee et al., 2013). In Model 2, the first two inhibitory populations likewise represent PV and SOM neurons and the third population, denoted as X, represents an unidentified inhibitory subtype. The main difference with Model one is that here, the third population does not project to SOM neurons.

Depending on network parameters, the response of PV neurons in Model one can be paradoxical or not. To have equal relative suppression of the PCs and PV activities, however, interaction parameters have to be fine-tuned. In Model 2, the relative changes in the PC and PV activity are the same independent of interaction parameters.

For a two-population network, the paradoxical effect only occurs when it is inhibition stabilized (Pehlevan and Sompolinsky, 2014; Wolf et al., 2014). This is because the mechanism requires strong recurrent excitation. In the four-population networks we studied, however, the mechanism responsible for paradoxical effect is different. It involves a disinhibitory loop. In fact, strong recurrent excitation prevents the paradoxical effect in these networks. Therefore, the observation of the paradoxical effect upon PV photo-excitation is not a proof that the network operates in the ISN regime.

## Strong vs. weak interactions

Cortical networks consist of a large number (N) of neurons each receiving a large number of inputs (K). Because N and K are large, one expects that a network behaves similar to a network where N and K are infinite. In this limit the analysis is simplified and the mechanisms underlying the dynamics are highlighted. When taking the large K limit one needs to decide how the interaction strengths scale with K. Two canonical scalings can be used: in one the interactions scale as 1/K (Hansel and Sompolinsky, 1992; Hennequin et al., 2018; Knight, 1972; Rubin et al., 2015), in the other as 



1

/


K




 (Darshan et al., 2017; Renart et al., 2010; Rosenbaum et al., 2017; van Vreeswijk and Sompolinsky, 1996). These differ in the strength of the interactions. For instance, for K = 900 interactions are weaker by a factor 30 in the first scaling than in the second. Importantly, these two scalings give rise to qualitatively different dynamical regimes.

When interactions are strong, the excitatory and inhibitory inputs are both very large (of the order of 

K
.


1



K



=
1

). They, however, dynamically balance so that the temporal average of the net input and its spatial and temporal fluctuations are comparable to the rheobase (Van Vreeswijk and Sompolinsky, 2005; van Vreeswijk and Sompolinsky, 1998), Appendix 1A). In this balanced regime, the average firing rates of the populations are determined by a set of linear equations: the “balance equations”. These do not depend on the neuronal transfer function. For large but finite 

K

, the network operates in an approximately balanced regime. In this regime, the population activities are well approximated by the balance equations, interspike intervals are highly irregular and firing rates are heterogeneous across neurons.

When the interactions are weak, excitatory and inhibitory inputs are both comparable to the rheobase even when K is large, but their spatial and temporal fluctuations vanish as K increases. The activity of the network is determined by a set of coupled non-linear equations which depends on the neuronal transfer function. For large but finite K, the firing of the neurons is weakly irregular and heterogeneities mostly arise from differences in the intrinsic properties of the neurons.

In which of these regimes does cortex operate in-vivo? This may depend on the cortical area and on whether the neuronal activity is spontaneous or driven (e.g. sensory, associative, or motor related). There are, however, several facts indicating that the approximate balanced regime may be ubiquitous. Many cortical areas exhibit highly irregular spiking (Shinomoto et al., 2009) and heterogeneous firing rates (Hromádka et al., 2008; Roxin et al., 2011). Excitatory and inhibitory postsynaptic potentials (PSPs) are typically of the order of 0.2 to 2mV or larger (Levy and Reyes, 2012; Ma et al., 2012; Pala and Petersen, 2015; Seeman et al., 2018). Model networks with PSPs of these sizes and reasonable number of neurons and connections exhibit all the hallmarks of the balanced regime (Amit and Brunel, 1997; Hansel and Mato, 2013; Hansel and van Vreeswijk, 2012; Lerchner et al., 2006; Pehlevan and Sompolinsky, 2014; Argaman and Golomb, 2018; Rao et al., 2019; Roudi and Latham, 2007; Roxin et al., 2011 Van Vreeswijk and Sompolinsky, 2005). Moreover, there is experimental evidence of co-variation of excitatory and inhibitory inputs into cortical neurons (Haider et al., 2006; Shu et al., 2003). Finally, in cortical cultures synaptic strengths have been shown to approximately scale as 



1

/


K




 (Barral and D Reyes, 2016). Therefore in this paper we focused on cortical network models in which interactions are strong, that is of the order of 



1

/


K




.

## Model 1 accounts for the responses in ALM layer 2/3 and layer 5

In Model 1, whether the network exhibits a paradoxical effect depends on the value of the ratio 

ρ
=




J


E
E



/



J


E
E


*





 where 



J


E
E


*


≡


J


V
E






J


E
S



/



J


V
S





. Here, 



J


α
β


,  
α
,
β
∈
{
E
,
S
,
V
}

, is the strength of the connection from population β to population 

α

. When ρ > 1, the PV response is non-paradoxical and its activity increase can be substantial well before suppression of the PC activity. On the other hand when ρ > 1, the PV response is paradoxical and the PV activity reaches its minimum for light intensities at which the PCs are still substantially active.

In ALM layer 2/3, the activity of the PV population increases with the light intensity while the activity of the PC decreases on average. Remarkably, our experiments showed that the increase in the PV activity was already substantial for small light intensities, where the PCs were still significantly active. In ALM layer 5 the activity of the PV population initially decreased with the light intensity together with the activity of the PC population. As the light intensity is further increased, the PV activity reaches a minimum after which it increases. At this minimum, the PC activity is still substantial.

Thus, Model 1 accounts for our experimental findings in ALM layer 2/3 provided that JEE
 is sufficiently large. It accounts for the paradoxical effect in layer 5 provided that JEE
 is sufficiently small. Note that this does not mean that JEE
, is larger in the former layer as compared to the latter. The interactions JVE, JES
 and JVS
 are likely to be layer dependent (Jiang et al., 2015) and therefore so is the value of 



J


E
E


*



.

## Model 2 accounts for the paradoxical effect in S1 while model 1 would require fine-tuning

Similar to ALM layer 5, the PV response in S1 is paradoxical. Remarkably however, in S1 the relative suppression of the PC and PV activities is the same for low light intensity. Model 1 can account for this feature only when the interaction parameters are fine-tuned. In contrast, in Model 2 the co-modulation of the PC and PV activities stems from the architecture and therefore occurs in a robust manner. Furthermore, it can equally well account for the fact that in S1 the PV activity reaches its minimum when the PC population is active.

Note that in ALM layer 5 the difference between the slopes of the PC and PV population activities is not significantly different (p>0.05). Therefore, we cannot exclude that Model 2 describes ALM layer 5.

The main difference between Models 1 and 2 is that in Model 1, the third inhibitory population (VIP) projects to SOM neurons while in Model 2, the third population (X) does not. This suggests that population X is not the VIP population. For example, X could be chandelier cells that do not express the PV marker (Jiang et al., 2015) Alternatively, population X could describe the effective interaction of several inhibitory populations with PC and PV neurons.

## Models 1 and 2 account for the heterogeneity of single neuron responses

The responses of PCs and PV neurons in the experimental data are highly heterogeneous across cells. Indeed in ALM layer 5 and S1, PV neurons on average show a paradoxical response but at the single neuron level the effect of the laser stimulation is very diverse. Moreover, the firing rate of a neuron can vary monotonically or non-monotonically with the laser intensity. For instance, when stimulated, the firing rates of many PV neurons increase, although, on average the activity is substantially smaller than baseline. Conversely, for some PV neurons the paradoxical effect is so strong that the laser completely suppresses their activity.

We observed an even larger diversity in single neuron responses in our simulations of Model 1 and 2. We should emphasize that in the simulated networks all the neurons were identical and the cells in the same population received the same feedforward constant external input. The only possible source of heterogeneity therefore comes from the randomness in the network connectivity. The effect of this randomness on the network recurrent dynamics is however non-trivial: one may think that the effect of the fluctuations in the number of connections from neuron to neuron should average out since in the models the number of recurrent inputs per neuron is large (K = 500 or more). This is not what happens because in our simulations populations which are active operate in the balanced excitation/inhibition regime (Roxin et al., 2011; van Vreeswijk and Sompolinsky, 1998; van Vreeswijk and Sompolinsky, 1996). In this state, relatively small homogeneity in the number of connections per neuron is amplified to a substantial inhomogeneity in the response. Thus, strong heterogeneity in the response of neurons is not a prima facie evidence for the heterogeneity of the level of Channelrhodopsin expression in the cells nor is it for the diversity of the single neuron intrinsic properties.

## Limitations

We give here a qualitative account for the mechanisms underlying the responses of different cortical areas to optical stimulation. A quantitative analysis of the data, in particular of the heterogeneity is beyond our scope. Such an analysis would require a much larger number of PV neurons. Moreover, it would necessitate the use of more complicated neuronal models making the mathematical analysis intractable, limiting the investigation to simulations only and thus obscuring the mechanisms.

In our experiments, we expressed ReaChR in all PV neurons and in all layers in ALM. In particular, all PV neurons in layer 2/3 and layer five were simultaneously affected by the photostimulus. PCs in layer 2/3 project to layer 5 and receive feedback from the latter (Hooks et al., 2013; Naka and Adesnik, 2016). Interlaminar interactions are likely to also contribute to the effect of the photostimulation.

In our models, we did not take into account such interactions. Including strong connections from layer 2/3 PCs to neurons in layer 5 and/or feedback connections from layer 5 neurons to layer 2/3, could alter our interpretations. In the absence of data that reveal the nature of interlaminar interactions, extending our model to incorporate these is impractical given the large number of parameters to vary. Experiments in ALM and S1 where the optogenetic marker is expressed in only one layer at a time would constraint models which include interlaminar interactions and facilitate their analysis (Moore et al., 2018).

There is a large amount of experimental evidence indicating that different synapses can exhibit diverse dynamics depending on their pre and postsynaptic populations (Ma et al., 2012). For instance, recent studies have shown that PCs to PV synapses are depressing while the PCs to SOM synapses are highly facilitating (Karnani et al., 2016; Xu et al., 2013). Synaptic facilitation and depression mechanisms could give rise to dynamics which will make the network responses depend on the duration of the photostimulation. Here, we did not take into account short term plasticity. Mice neocortex mostly comprises PV, SOM and 5HT3aR expressing interneurons. There is a growing amount of experimental evidence indicating that these populations include different subtypes which may have distinct connectivity patterns (Naka and Adesnik, 2016; Nigro et al., 2018; Tremblay et al., 2016). In the present work, we only considered three populations of identical interneurons: PV, SOM and VIP or X. As the number of populations increases, the number of interaction parameters increases quadratically, making it a great challenge to uncover even simple mechanisms that could underlie the network responses.

## Comparison with previous theoretical work

The paradoxical effect was first described in Tsodyks et al. (1997) and Ozeki et al. (2009) for weak interactions using coarse grained two-population rate models (Wilson and Cowan, 1972). These models were extended in Rubin et al. (2015) to a spatially structured network to explain center-surround interactions and other contextual effects in primary visual cortex. They found that these effects can be accounted for if the neuronal transfer function is supralinear and the network is operating in the inhibition stabilized regime (ISN). With supralinear transfer functions, whether or not the network exhibits a paradoxical effect depends on the background rate of the inhibitory neurons. These models were further extended by Litwin-Kumar et al. (2016) to networks consisting of PC, PV, SOM and VIP neurons with an architecture similar to Pfeffer et al. (2013). They studied the effect of photostimulation of the different inhibitory populations on the responses and orientation tuning properties of the neurons. In a recent study (Sadeh et al., 2017) have investigated the effects of partial activation of PV neurons upon photostimulation in an ISN. They argued that depending on the degree of viral expression, the average response of the infected neurons can decrease or increase with the light intensity: it decreases only if a large proportion of the population is infected. (Garcia Del Molino et al., 2017) showed that due to the non-linearity in the neuronal transfer function, the response of the network to stimulation can be different for different background rates. In particular, they showed that it can reverse the response of SOM neurons to VIP stimulation.

All these works considered inhibition stabilized networks in which the total recurrent excitation is so strong that the activity would blow up in the absence of inhibitory feedback. With our notations, this means that 




G

E



j

E
E


>
1

/

K



, where GE
 is the gain of the noise average transfer function (f-I curve) of the excitatory neurons. In fact, in these models all the interactions j
αβ are of order 1/K so they are weak in our sense. Moreover, these studies considered networks that are so small that it is impossible to extrapolate their results to mouse cortex size networks. Here we studied large network models (N = 76800) with strong interactions, that is j
αβ are of order 



1

/


K




 operating in the balanced regime. Note that such networks are ISNs provided that 



j


E
E


≠
0

. We showed that paradoxical effect can be present or not depending on the interaction parameters.

Since we used static synapses, changes in the background rates cannot reverse the paradoxical effect in our models. This is because with static synapses the balance equations are linear. One can recover this reversal if one introduces short-term plasticity which will make the balance equations nonlinear. We did not consider partial expression of channelrhodopsin in the PV population because our goal was to account for experimental data where virtually all neurons were infected. These effects have been studied in Gutnisky et al. (2017); Sanzeni et al. (2019) in strongly coupled networks of two populations yielding to the same conclusions as (Sadeh et al., 2017).

## Predictions

Our theory (Model 1) predicts that in ALM layer 2/3 the activity of the SOM and VIP populations will decrease upon PV photostimulation (Figure 4B). It also predicts that upon PC photoinhibition, the PV activity will increase whereas the activity of the SOM and VIP populations will decrease (Figure 12A). This is because in Model 1 when the PV response is non-paradoxical (




χ

I
I


>
0



) the product XEI XIE
﻿ is also positive (see Appendix 1C). Furthermore, in ALM layer 2/3 the population activity of PCs decreases upon PV photostimulation, XEI
 < 0. Hence, XIE
 is negative. The balance of the PC and the VIP inputs into SOM neurons implies that VIP and PC activity covary. Finally, in Appendix 1C we show that if XEE 
 > 0 and XIE
 < 0 then necessarily XSE
 > 0. Thus, in ALM layer 2/3, the SOM population activity should decrease upon PC photoinhibition (Figure 12A).

![Figure 12.](https://cdn.elifesciences.org/articles/49967/elife-49967-fig12-v3.jpg)

**Figure 12.:** (
A) In ALM layer 2/3, the activity of the PV population decreases upon photoinhibition of the PCs. (B) In ALM layer 2/3, photostimulation of VIP neurons increases the activity of the PV population. (C) In S1, PV and PC activity decrease proportionally upon photoinhibition of the latter. (D) In S1, the PC and PV responses are not proportional upon photoinhibition of the SOM population. (E) In S1, upon photostimulation of PV neurons and photoinhibition of the SOM population with a constant input, the PV response is paradoxical but PC and PV responses are no longer proportional.

In auditory and prefrontal cortex (Pi et al., 2013) as well as in S1 (Lee et al., 2013), photostimulation of VIP neurons, activates them (XVV
 > 0) and disinhibits the PCs (XEV
 > 0) through an inhibition of the SOM population (XSV
 > 0). If this is also true in ALM layer 2/3, our model predicts that photostimulation of VIP neurons should increase the PV activity (XIV
 > 0) (Appendix 1C, Figure 12B).

In S1 our theory (Model 2) predicts that the PC and PV activities will proportionally decrease upon PC photoinhibition (Equation (3), Appendix 1D, Figure 12C). Photostimulation of the SOM neurons modifies Equation (3) and consequently, the changes in PC and PV activity no longer covary (Figure 12D). Thus, our theory can be tested by photostimulating PV neurons as in our experiment, while also photostimulating SOM neurons with a second laser with constant power. In this case, the model predicts that S1 will still exhibit the paradoxical effect but that the responses of the PC and PV populations will no longer be proportional (Figure 12E).

## Perspectives

We only considered response of the neurons for a large radius of the laser beam. In a recent study Li et al. (2019), have investigated the spatial profile of the response and its dependence on the light intensity. Our theory can be extended to incorporate spatial dependencies. Studying the interplay between the connectivity pattern and laser beam width in the response profile of the networks will provide further constraints on cortical architectures.

Due to the strong interactions in our models, the nonlinearity of the single neuron f-I curves hardly affects the population average responses. However, it influences the response heterogeneity that naturally arises in our theory (Figures 6–8). An alternative model for the paradoxical effect is the supralinear stabilized network (SSN) (Rubin et al., 2015) which relies on an expansive non-linearity of the input-output transfer function of the inhibitory populations. Whether this mechanism can account for our experimental data is an issue for further study. In particular, it would be interesting to know whether the SSN scenario can account for the strong heterogeneity in the responses and for the proportionality of the PC and PV population activities in S1. Answering these questions may provide a way to discriminate between the balance network and SSN theory.

## Materials and methods

## Animals and surgery

The experimental data are from 9 PV-Ires-Cre x R26-CAG-LSL-ReaChR-mCitrine mice (age >P60, both male and female mice) (Hooks et al., 2015). three mice were used for photoinhibition in somatosensory cortex (S1). six mice were used for photoinhibition in anterior lateral motor cortex (ALM). All procedures were in accordance with protocols approved by the Janelia Research Campus and Baylor College of Medicine Institutional Animal Care and Use Committee.

Mice were prepared for photostimulation and electrophysiology with a clear-skull cap and a headpost (Guo et al., 2014a; Guo et al., 2014b). The scalp and periosteum over the dorsal surface of the skull were removed. A layer of cyanoacrylate adhesive (Krazy glue, Elmer’s Products Inc) was directly applied to the intact skull. A custom made headbar was placed on the skull (approximately over visual cortex) and cemented in place with clear dental acrylic (Lang Dental Jet Repair Acrylic; Part# 1223-clear). A thin layer of clear dental acrylic was applied over the cyanoacrylate adhesive covering the entire exposed skull, followed by a thin layer of clear nail polish (Electron Microscopy Sciences, Part# 72180).

## Photostimulation

Light from a 594 nm laser (Cobolt Inc, Colbolt Mambo 100) was controlled by an acousto-optical modulator (AOM; MTS110-A3-VIS, Quanta Tech; extinction ratio 1:2000; 1µs rise time) and a shutter (Vincent Associates), coupled to a 2D scanning galvo system (GVA002, Thorlabs), then focused onto the brain surface (Guo et al., 2014a). The laser at the brain surface had a diameter of 2 mm. We tested photoinhibition in barrel cortex (bregma posterior 0.5 mm, 3.5 mm lateral) and ALM (bregma anterior 2.5 mm, 1.5 mm lateral).

To prevent the mice from detecting the photostimulus, a ‘masking flash’ pulse train (40 1 ms pulses at 10 Hz) was delivered using a LED driver (Mightex, SLA-1200–2) and 590 nm LEDs (Luxeon Star) positioned near the eyes of the mice. The masking flash began before the photostimulus started and continued through the end of the epoch in which photostimulation could occur.

The photostimulus had a near sinusoidal temporal profile (40 Hz) with a linear attenuation in intensity over the last 100–200 ms (duration: 1.3 s including the ramp). The photostimulation was delivered at ~7 s intervals. The power (0.5, 1.2, 2.2, 5, 12 mW for S1 photostimulation; 0.3, 0.5, 1, 1.5, 2, 3.3, 5, 8, 15 mW for ALM photostimulation) were chosen randomly. Because we used a time-varying photostimulus, the power values reported here reflect the time-average.

## Electrophysiology

All recordings were carried out while the mice were awake but not engaged in any behavior. Extracellular spiking activity was recorded using silicon probes. We used 32-channel NeuroNexus silicon probes (A4 × 8–5 mm-100-200-177) or 64-channel Cambridge NeuroTech silicon probes (H2 acute probe, 25 μm spacing, two shanks). The 32-channel voltage signals were multiplexed, digitized by a PCI6133 board at 400 kHz (National Instruments) at 14 bit, demultiplexed (sampling at 25,000 Hz) and stored for offline analysis. The 64-channel voltage signals were amplified and digitized on an Intan RHD2164 64-Channel Amplifier Board (Intan Technology) at 16 bit, recorded on an Intan RHD2000-Series Amplifier Evaluation System (sampling at 20,000 Hz) using Open-Source RHD2000 Interface Software from Intan Technology (version 1.5.2), and stored for offline analysis.

A 1 mm diameter craniotomy was made over the recording site. The position of the craniotomy was guided by stereotactic coordinates for recordings in ALM (bregma anterior 2.5 mm, 1.5 mm lateral) or barrel cortex (bregma posterior 0.5 mm, 3.5 mm lateral).

Prior to each recording session, the tips of the silicon probe were brushed with DiI in ethanol solution and allowed to dry. The surface of the craniotomy was kept moist with saline. The silicon probe was positioned on the surface of the cortex and advanced manually into the brain at ~3 µm/s, normal to the pial surface. The electrode depth was inferred from manipulator depth and verified with histology. For ALM recordings, putative layer 2/3 units were above 450 µm and putative layer 5 units were below 450 µm (Hooks et al., 2013). For S1, our recording did not distinguish layers.

## Data analysis

The extracellular recording traces were band-pass filtered (300–6 kHz). Events that exceed an amplitude threshold (four standard deviations of the background) were subjected to manual spike sorting to extract single units (Guo et al., 2014a).

Our final data set comprised of 204 single units (S1, 95; ALM, 109). For each unit, its spike width was computed as the trough to peak interval in the mean spike waveform (Guo et al., 2014a). We defined units with spike width <0.35 ms as FS neurons (31/204) and units with spike width >0.45 ms as putative pyramidal neurons (170/204). Units with intermediate values (0.35–0.45 ms, 3/204) were excluded from our analyses.

To quantify photoinhibition strength, we computed ‘normalized spike rate’ during photostimulation. For each neuron, we computed its spike rate during the photostimulus (1 s time window) and its baseline spike rate (500 ms time window before photostimulus onset). The spike rates under photostimulation were divided by the baseline spike rate. The ‘normalized spike rate’ thus reports the total fraction of spiking output under photostimulation. For normalized spike rate of individual neurons, each neuron’s spike rate with photostimulation was normalized by dividing its baseline spike rate (Figure 1B–D, top). For normalized spike rate of the neuronal population (Figure 1B–D, bottom), the spike rates with photostimulation were first averaged across the population (without normalization) and then normalized by dividing the averaged baseline spike rate.

Bootstrap was performed over neurons to obtain standard errors of the mean. For each round of bootstrapping, repeated 1000–10000 times, we randomly sampled with replacement neurons in the dataset. We computed the means of the resampled datasets. The standard error of the mean was the standard deviation of the mean estimates from bootstrap.

## Network models

All the models we consider consist of strongly interacting leaky integrate-and-fire neurons. We first study networks of one excitatory (E) and one inhibitory (I) population. We then investigate two models comprising three inhibitory populations, namely parvalbumin positive (PV or I), somatostatin positive (SOM or S) and a third population either corresponding to the vasoactive intestinal peptide positive (VIP or V) neurons (Model 1) or to an unidentified population denoted by X (Model 2).

In all models the total number of neurons is N = 76800. In the two population model, 75% are excitatory and 25% inhibitory. In the four-population networks, 75% are excitatory and the number of cells is the same, N/12, for all GABAergic inhibitory population.

The data we seek to account for, were obtained in optogenetic experiments in which the laser diameter was substantially larger than the spatial range of neuronal interactions and comparable to the size of the cortical area were the recordings were performed. Therefore, in all models we assume for simplicity that the connectivity is unstructured: neuron (i, α), (α = E, I, S, V/X), is postsynaptically connected to neuron (j) (j, β) with probability
(5)



P


i
j


α
β


=




K


α
β






N


β

For simplicity, we take 



K


α
β



 the same for all populations, 



K


α
β


=
K

.

Neuron dynamics: The dynamics between spikes of the membrane potential of the neuron (i, α) is given by
(6)



C


M




d


V


i


α




t




d
t


=
-


g


l
e
a
k


α






V


i


α




t


-


V


R




+


I


r
e
c


α
i




t




+
Λ


e
x
t


α


+


Λ


o
p
t
o


α
i

Here, 



I


r
e
c


α
i




t



 is the net recurrent input into neuron 



i
,
α



, 



Λ


e
x
t


α



 represents inputs from outside the circuit (e.g. thalamic excitation) to population α, and 



Λ


o
p
t
o


α
i



 is the optogenetic input into neuron (i, α).

We assumed that the capacitance, CM
, is identical for all neurons and the leak conductance, 



g


l
e
a
k


α



, is identical for all the cells in the same population. We take 



C


M


=
1
μ
F
.
c


m


-
2



, 



g


l
e
a
k


I


=
0.1
m
S
.
c


m


-
2



 and 



g


l
e
a
k


E



=



g


l
e
a
k


S



=



g


l
e
a
k




V

/

X




=
0.05
m
S
.
c


m


-
2



.

Equation (2) has to be supplemented by a reset condition: if at time 

t

 the membrane potential of the neuron (i, α) crosses the threshold 




V

i


α


(

t

−


)

=


V

t
h



=

−
50
m
V



, the neuron fires a spike and its voltage is reset to the resting potential 




V

i


α


(

t

+


)

=


V

R



=

−
70
m
V



.

Recurrent inputs: The net recurrent input into neuron (i, α) is
(7)



I


r
e
c


α
i




t


=


∑

β
,
j





j


α
β

 


ϵ


β

 


C


i
j


α
β



 
S


j


α
β




t





where C
αβ is the connectivity matrix between (presynaptic) population β and (postsynaptic) population α, such that 



C


i
j


α
β


=
1

 if neuron (j, β) projects to neuron (i, α) and 



C


i
j


α
β


=
0

 otherwise. The parameter j
αβ is the strength of the interaction from neurons in population β to neurons population α. We assumed it to depend on the pre and postsynaptic populations only. The polarity (excitation or inhibition) of the interaction is denoted by εβ. Therefore if β = E, εβ = 1 and εβ = -1 otherwise.

The function 



S


j


α
β




t



 is
(8)



S


j


α
β




t


=


∑

k





f


α
β




t
-


t


β
j


k







where 



t


β
j


k



 is the time at which neuron (j, β) has emitted its k
th spike, the sum is over all the spikes emitted by neuron (j, β) prior to time t and
(9)



f


α
β




t


=


1




τ


α
β






e




-
t

/



τ


α
β







where ταβ is the synaptic time constant of the interactions between neurons in population β and α.

External and optogenetic inputs: The feedforward input, 



Λ


e
x
t


α



, into the neurons in population 

α

 is described by inputs from 2K external neurons with constant firing rate r
0 = 5 Hz and an interaction strength j
α0, therefore, 



Λ


e
x
t


α


=


2
K
j


α
0




r


0



.

We model the ReachR photostimulation as an additional external constant input to the stimulated population. For simplicity, we assume that this input, 



Λ


o
p
t
o


α
i


=


Λ


o
p
t
o


α



, is the same for all stimulated neurons. Unless specified otherwise, we only consider 



Λ


o
p
t
o


I


=


Λ


o
p
t
o



 and 



Λ


o
p
t
o


α


=
0

 for 

α
≠
I

.

In qualitative agreement with Figure 3, and Figures 5, 7, Figure 7—figure supplement 1, Figure 10; (Hooks et al., 2015) we take
(10)



Λ


o
p
t
o


=


Λ


0


α


l
o
g


1
+




Γ


o
p
t
o






Γ


0


α







where 



Γ


o
p
t
o



 is the laser intensity and 



Λ


0



 and 



Γ


0



 are parameters.

## Architectures of the four-population models

The network of Model one is depicted in Figure 4A. In line with the results of Pfeffer et al. (2013), there are no connections from PV to SOM, VIP to PC and VIP to PV neurons. There is no mutual inhibition between SOM as well as between VIP neurons. All the populations except SOM receive feedforward external input.

The interaction matrix of the network is
(11)


[

j

A
B



ε
B

]
=

[ 





j

E
E






−

j

E
I






−

j

E
S





0






j

I
E






−

j

I
I






−

j

I
S





0






j

S
E





0


0



−

j

S
V









j

V
E






−

j

V
I






−

j

V
S





0



 ]

The network of Model two is depicted in Figure 9B. SOM only receives projections from PCs and PV neurons. X neurons are recurrently connected and project to PCs and PV neurons. The PC and SOM populations project to the population X. All the populations except SOM receive feedforward external input.

The interaction matrix is
(12)


[

j

A
B



ε
B

]
=

[ 





j

E
E






−

j

E
I






−

j

E
S






−

j

E
X









j

I
E






−

j

I
I






−

j

I
S






−

j

I
X









j

S
E






−

j

S
I





0


0






j

X
E





0



−

j

X
S






−

j

X
X






 ]

Numerical simulations: The dynamics of the models was integrated numerically using a second-order Runge-Kutta scheme (Press et al., 1986) without spike time interpolation. Unless specified otherwise the time step was Δt = 0.01 ms and the temporally averaged firing rates were estimated over 100s.

## The balance equations

We consider recurrent networks of strongly interacting neurons (van Vreeswijk and Sompolinsky, 1996) in which order 


K


 excitatory synaptic inputs are sufficient to bring the voltage above threshold. To understand the behavior of such networks, it is imperative to analyse how it behaves when K goes to infinity. To this end, we scale the interactions as
(13)




j

α
β


=


J

α
β



K





where J
αβ does not depend on K. Since a neuron receives on average K inputs from each of its presynaptic populations, the total interaction from population β to a neuron in population α is 



J


α
β



K


. To keep the relative strength of the optogenetic input, 



Λ


o
p
t
o


α



, as 

K

 increases we take
(14)



Λ


o
p
t
o


α


=


I


o
p
t
o


α



K


where 



I


o
p
t
o


α



 depends on the intensity of the laser:
(15)



I


o
p
t
o


α


=


I


0


α


l
o
g


1
+




Γ


o
p
t
o






Γ


0


α

We take: 



I


0


α


=


I


0


=
8
n
A

 and 



Γ


0


α


=


Γ


0


=
0.5
m
W
.
m


m


-
2



.

The net input into the neurons must remain finite in the infinite K limit. This implies that up to corrections which are of the order of 



1



K




,
(16)

2 


J


α
0

 


r


0


+


I


o
p
t
o


α


+


∑

β





J


α
β

 


ϵ


β 




r


β


=
0

In a n-population network, these 

n

 equations determine the 

n

 firing rates, 



r


α


, 
α
∈
{
1
,
.
.
.
,
n
}

.

This set of linear equations express the fact that, for the population activities to be finite, excitatory and inhibitory inputs to the neurons must compensate. These 'balance' equations have a unique solution (unless the determinant of the matrix 



J


α
β




ϵ


β



 is zero). To be meaningful the solution must be such that all population activities are positive. This constrains the feedforward and recurrent interaction parameters.

The stability of this balanced solution further constraints the interaction parameters and synaptic time constants. A necessary condition for the stability is that 



d
e
t

[


J

α
β



ϵ

β



]

>
0



. This condition guarantees that the 'balanced state' is stable with respect to divergence of the firing rates. A complete study of these constraints for our LIF networks is beyond the scope of this paper.

In all the models, we study parameter ranges in which, at baseline (



I


o
p
t
o


α


=
0

), the network operates in a stable balanced state where distributions of rates exhibit a quasi-lognormal shape and spikes are emitted irregularly as in a Poisson process (Figure 5—figure supplement 3; Figure 7—figure supplement 5; Figure 10—figure supplement 3). For 



I


o
p
t
o


α



 sufficiently large, it may happen that one or more population activity reaches zero. In this case, the network evolves to a partially balanced state in which the rates of the populations that remain active satisfy a reduced set of balanced equations. For example, if we consider a solution were the rate of population 

γ

, 



r


γ



 is zero and all other rates are positive, the reduced balance equations are
(17)



2
 

J

α
0


 

r

0


+

I

o
p
t
o


α


+

∑

β
≠
γ



J

α
β


 

ϵ

β


 

r

β


=
0


,

f
o
r



α
≠
γ
.

Consistency of this solution leads to the requirement that the input into population 

γ

 is hyperpolarizing.
(18)



2
 

J

γ
0
 



r

0


+

I

o
p
t
o


γ


+

∑

β
≠
γ



J

γ
β


 

ϵ

β


 

r

β


<
0

Note that they may be multiple self-consistent solutions which are partially balanced.

Upon photostimulation of PV, in Model 1, the balanced equations are
(19.1)

2 


J


E
0



 
r


0


+


J


E
E

 


r


E


-


J


E
I

 


r


I


-


J


E
S

 


r


S


=
0



(19.2)

2 




J


I
0

 


r


0


+


I


o
p
t
o


I


+
J


I
E

 


r


E


-


J


I
I

 


r


I


-


J


I
S

 


r


S


=
0



(19.3)



J


S
E

 


r


E


-


J


S
V

 


r


V


=
0



(19.4)



2 
J


V
0

 


r


0


+


J


V
E

 


r


E


-


J


V
I

 


r


I


-


J


V
S

 


r


S


=
0

In particular, Equation (19.3) implies that 



r


E



 and 



r


V



 are always proportional (




J

S
E


,

J

S
V


>
0



).

Similarly, in Model 2, the balanced equations are
(20.1)



2 
J


E
0

 


r


0


+


J


E
E

 


r


E


-


J


E
I



 
r


I


-


J


E
S 




r


S


-


J


E
X

 


r


X


=
0



(20.2)



2 
J


I
0

 


r


0


+


I


o
p
t
o


I


+


J


I
E




r


E


-


J


I
I

 


r


I


-


J


I
S

 


r


S


-


J


I
X 




r


X


=
0



(20.3)



J


S
E

 


r


E


-


J


S
I 




r


I


=
0



(20.4)



2 
J


X
0

 


r


0


+


J


V
E

 


r


E


-


J


V
S

 


r


S


-


J


X
X

 


r


X


=
0

Equation (20.3) implies that in this network 



r


E



 and 



r


I



 are always proportional 




(


J

S
E


,
 

J

S
I


>
0

)




.
