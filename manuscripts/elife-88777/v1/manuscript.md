# Structural constraints on the emergence of oscillations in multi-population neural networks

## Authors

- Jie Zang<sup>1</sup> ([ORCID: 0000-0003-2655-3343](https://orcid.org/0000-0003-2655-3343))
- Shenquan Liu<sup>1</sup> †
- Pascal Helson<sup>2</sup> ([ORCID: 0000-0002-2877-3705](https://orcid.org/0000-0002-2877-3705))
- Arvind Kumar<sup>2</sup> ([ORCID: 0000-0002-8044-9195](https://orcid.org/0000-0002-8044-9195)) †

### Affiliations

1. https://ror.org/0530pts50 School of Mathematics, South China University of Technology Guangzhou China
2. https://ror.org/026vcq606 Division of Computational Science and Technology, School of Electrical Engineering and Computer Science, KTH Royal Institute of Technology Stockholm Sweden

† Corresponding author

## Abstract

Oscillations arise in many real-world systems and are associated with both functional and dysfunctional states. Whether a network can oscillate can be estimated if we know the strength of interaction between nodes. But in real-world networks (in particular in biological networks) it is usually not possible to know the exact connection weights. Therefore, it is important to determine the structural properties of a network necessary to generate oscillations. Here, we provide a proof that uses dynamical system theory to prove that an odd number of inhibitory nodes and strong enough connections are necessary to generate oscillations in a single cycle threshold-linear network. We illustrate these analytical results in a biologically plausible network with either firing-rate based or spiking neurons. Our work provides structural properties necessary to generate oscillations in a network. We use this knowledge to reconcile recent experimental findings about oscillations in basal ganglia with classical findings.

## Introduction

Oscillations are ubiquitous in dynamical systems Strogatz, 2018; Pikovsky et al., 2002. They have important functional consequences but can also cause system malfunction. In the brain for instance, oscillations take part in information transfer Fries, 2015; Hahn et al., 2019. However, persistent beta band (13-30 Hz) oscillations are associated with the pathological symptoms of Parkinson’s disease (PD) Brown et al., 2001. Therefore, it is important to determine when and how a system of many interacting nodes (network) oscillates.

This question is usually very difficult to answer analytically. The main tool that can be used is the Poincaré–Bendixson theorem Poincaré, 1880; Bendixson, 1901 which is only valid in two dimensions, which drastically reduces its applicability. In some cases, when we know the model parameters, it is possible to calculate whether the system will oscillate or not. However, often such parameters cannot be measured experimentally. For example, in most physical, chemical, and biological networks, it is usually not possible to get the correct value of connectivity strength. By contrast, it is much easier to know whether two nodes in a system are physically connected and what is the sign (positive or negative) of their interactions. Therefore, it is much more useful to identify necessary structural conditions for the emergence of oscillations in a system without delays. A good example is the conjecture postulated by Thomas, 1980 which relies on the sign of the loops present in the network. A loop (or a cycle) is said to be negative (resp. positive) when it has an odd (resp. even) number of inhibitory connections. According to Thomas’ conjecture, when considering a coupled dynamical system (x˙=f⁢(x) and x⁢(0)∈ℝn) with a Jacobian matrix that has elements of fixed sign, the system can exhibit oscillations only if the directed graph obtained from the nodes’ connectivity (Jacobian matrix) admits a negative loop of two or more nodes. This conjecture has been proven using graph theory for smooth functions f Snoussi, 1998; Gouzé, 1998.

Thomas also conjectured that the assumption on the constant sign of the Jacobian matrix may not be necessary Thomas, 2006, that is having a negative loop in some domain of the phase space should be sufficient to generate oscillations. This condition is more realistic due to the ubiquity of the non-linearity in biological systems. For example, in the brain, even though neurons are (usually) either excitatory or inhibitory, the transfer function linking neurons is non-linear and can thus lead to elements of the Jacobian matrix having a non-constant sign. To the best of our knowledge, this last conjecture has not been proved yet but there are many examples of it. For instance, oscillations can emerge from a simple two populations, excitatory and inhibitory (EI), network Wilson-Cowan model (Ledoux and Brunel, 2011).

Here, we study the long-term behavior of the TLN model in the case of a single cycle interaction (without transmission delays). We show analytically that regardless of the sign of this loop, the system cannot oscillate when connections are too weak as the system possesses a unique globally asymptotically stable fixed point. However, when connections are strong enough (see Theorem 2), the system either possesses two asymptotically stable fixed points (positive loop) or a unique unstable fixed point (negative loop). In addition, the system can be shown to be bounded and thus, it has one of the following long term behavior: limit cycle, quasi-periodic or chaotic behavior. Interestingly, we can show that such dynamics can be shut down by introducing a positive external input to excited nodes.

We prove this conjecture for the threshold-linear network (TLN) model Hartline and Ratliff, 1958 without delays which can closely capture the dynamics of neural populations. Therefore, it is implicit that our results do not hold at the neuronal level but rather at the level of neuron populations/brain regions for example the basal ganglia (BG) network which can be described a network of different nuclei.

In fact, we use our analytical results to explain recent experimental findings about the emergence of oscillations in the BG during PD. To this end, we used simulations of BG network models with either firing rate-based or spiking neurons. Within the framework of the odd-cycle theory, distinct nuclei are associated with either excitatory or inhibitory nodes. Traditionally, the subthalamic nucleus and globus pallidus (STN-GPe) subnetwork is considered to be the key network underlying the emergence of oscillations in PD (Plenz and Kitai, 1996; Terman et al., 2002; Kumar et al., 2011). However, recent experiments have shown that near complete inhibition of GPe but not of STN is sufficient to quench oscillations (Crompe et al., 2020). This observation contradicts several previous models and even clinical observations in which surgical removal of STN is used to alleviate PD symptoms. Our theory suggests that there are at least six possible cycles in the Cortex-BG network that have the potential to drive oscillations based on the connectivity structure. We show that even if STN is inhibited, other cycles can sustain pathological oscillations. Interestingly, we found that GPe is involved in five out of six oscillatory cycles and therefore GPe inhibition is likely to affect PD-related oscillations in most cases.

## Results

We study how the emergence of oscillations in a network of excitatory and inhibitory populations depends on the connectivity structure. We first consider a network of nodes with dynamics representing the average firing rate of a population. We derive structural conditions for the emergence of oscillations when the dynamics of individual nodes are described according to the threshold-linear network (TLN) model. Next, we use numerical simulations to test whether such results might still hold on two other models: the Wilson-Cowan population rate-based model (Wilson and Cowan, 1972) and a network model of the BG with spiking neurons (see Methods).

## Structural conditions to generate oscillations

## Intuition behind the analytical results

There exist many ways to generate oscillations in a network. Oscillation can arise from individual nodes due to their intrinsic dynamics (e.g. a spiking neuron can exhibit a periodic behavior given its ionic channel composition Lee et al., 2018) or from the weights’ dynamics when considering synaptic plasticity Izhikevich and Edelman, 2008 or from transmission delays. Here, we assume that the system’s ability to oscillate only depends on the connectivity structure: the presence of positive or negative loops and the connections strength (Jacobian matrix) within them. That is, we ignore node properties, weight dynamics and transmission delays. The main reason we ignore these important properties is that we want to know the structural properties that can induce oscillations – this question can only be asked when all other potential sources of oscillation are removed. Given the importance of delays in biological network such as BG, we will consider them in the simulations.

In this following, we give simple examples of the possibility of oscillation (or not) based on the connectivity characteristics of small networks without delays. Let us start with a network of two nodes. If we connect them mutually with excitatory synapses, intuitively we can say that the two-population network will not oscillate. Instead, the two populations will synchronize. The degree of synchrony will, of course, depend on the external input and the strength of mutual connections. If both these nodes are inhibitory, one of the nodes will emerge as a winner and the other will be suppressed Ermentrout, 1992. Hence, a network of two mutually connected inhibitory populations cannot oscillate either. We can extend this argument to three population networks with three connections that form a closed loop (or cycle; see top of Figure 1a). When all three connections in the cycle are excitatory, the three populations will synchronize. Essentially, we will have a single population. Thus, these two and three population motifs are not capable of oscillations.

![Figure 1.](https://cdn.elifesciences.org/articles/88777/elife-88777-fig1-v1.jpg)

**Figure 1.:** (a) Examples of oscillating motifs and non-oscillating motifs in Wilson-Cowan model. Motifs that cannot oscillate show features of Winner-take-all: the winner will inhibit other nodes with a high activity level. Inversely, the oscillatory ones all show features of winner-less competition, which may contribute to oscillation. (b) The odd inhibitory cycle rule for oscillation prediction with the sign condition of a network. (c) Illustrations of oscillation in complex networks. Based on the odd inhibitory cycle rule, Network I can’t oscillate, while Network II could oscillate by calculating the sums of their motifs. The red or black arrows indicate inhibition or excitation, respectively. Hollow nodes and solid nodes represent excitatory and inhibitory nodes, respectively.

The simplest network motif which is capable of oscillating thus consists of two mutually connected nodes: one excitatory and one inhibitory (EI motif: Figure 1a, bottom; Ledoux and Brunel, 2011). When there are three populations connected with three connections to form a cycle, the potential to oscillate depends on the number of inhibitory connections. A cycle with one inhibitory connection (EEI motif) can be effectively reduced to an EI motif and can therefore oscillate. However, when there are two inhibitory connections (EII motif, Figure 1a, top), the two inhibitory neurons engage in a winner-take-all type dynamics and the network is not capable of oscillations. Finally, if there are three inhibitory connections (i.e. all three nodes are inhibitory, III motif) the network enters in a winner-less-competition Rabinovich et al., 2001 and can exhibit oscillations (Figure 1a, bottom).

These examples of two or three nodes suggest that a network can generate oscillations if there are one or three inhibitory connections in the network. We can generalize these results to cycles of any size, categorizing them into two types based on the count of their inhibitory connections in one direction (referred to as the odd cycle rule, as illustrated in Figure 1b). More complex networks can also be decomposed into cycles of size 2 N (where N is number of nodes), and predict the ability of the network to oscillate (as shown in Figure 1c).

These observations form the basis for the conjecture of Thomas, 1980 that gives a necessary condition for oscillations to emerge. This condition is of course not sufficient. In the following we find additional constraints (input and minimum connection strength) needed to determine the emergence of oscillations in a network. To this end, we use the TLN model which captures the neural population dynamics to a great extent. After proving the key theorems, we test with simulation whether similar results hold on a more realistic Wilson-Cowan model and a model of BG with spiking neurons.

## Threshold linear network model

We consider the TLN(W,b) in which individual nodes follow the dynamics(1)dxidt=−xi+[∑j=1nWijxj+bi]+,i=1,…,n

where n is the number of nodes, xi⁢(t) is the activity level of the ith node at time t≥0, Wi⁢j is the connection strength from node j to node i and [⋅]+⁢=def⁢max⁢{⋅,0} is the threshold non-linearity. For all i∈[n]⁢=def⁢{1,…,n}, the external inputs bi∈ℝ are assumed to be constant in time. We refer to a n neurons network with dynamics given by Equation 1 as TLN(W,b).

In order to help the definition of cycle connectivity matrices, we defineCn=def{(i,j)∈[n]2∣i−j=1}∪{(1,n)}.

We denote by δi,I the Kronecker delta which equals 1 when node i is inhibitory and 0 otherwise (node i is excitatory). In the following, we use the convention that node 0 is node n and node n+1 is node 1. For a given set of elements {yk}k∈ℕ in ℝ, we will use the convention:(2)∏k=ijyk=1 when j<i.

We define A={a1,…,anI} as the ensemble of inhibited nodes ({k∈[n]∣δk−1,I=1}) put in order such that a1<⋯<anI. Denoting by card⁢(⋅) the cardinal function, we have that card⁢(a)=nI. We also use the cycle convention for A:anI+1=a1.

## Analytical results

## Theorem 1

Let a network of inhibitory and excitatory nodes be connected through a graph G which does not contain any directed cycle. Assume that its nodes follow TLN(W,b) dynamics (Equation 1) withWij={wij(−1)δj,Iwhenedge i←j∈G0otherwise,

where wi⁢j∈ℝ+∀i,j∈[n]

Then, TLN(W,b) has a unique globally asymptotically stable fixed point.

## Theorem 2

Let G be a cyclical graph with nI∈ℕ+ inhibitory nodes and nE∈ℕ excitatory nodes such that nI+nE≥2 (≥3 when nI=1). Assume that the nodes follow the TLN(W,b) dynamics (Equation 1) with for all i,j∈[n], wj∈ℝ+,Wij={wj(−1)δj,Iwhen (i,j)∈Cn0otherwise,

and bi=0 when the node i-1 is excitatory and bi>0 otherwise. Moreover, using convention (Equation 2), assume that the initial state is bounded,(3)∀j∈{ak,…,ak+1−1},xj(0)∈[0,bak∏i=akj−1wi].

Then, the long-term behavior of the network depends on the following conditions,(4)∀k∈[nI],   ∏i=akak+1−1wi<bak+1bak,(5)∏i=akak+1−1wi>bak+1bak,(6)∏i=1nwin<1cos(π/n),(7)∏i=1nwin>1cos(π/n),

If nI is even and

If nI is odd and

## Remark 1

First, note that Equation 4 implies(8)∏i=1nwin<1,

and similarly, Equation 5 implies(9)∏i=1nwin>1.

In addition, the bound on the initial state Equation 3 can be easily removed. We use it because it eases the proof as we then don’t need to introduce technical details that are not interesting for this study.

Then, Theorem 2 says that a possible condition for the one cycle TLN to oscillate is that the number of inhibitory nodes is odd when the connection strength are strong enough (i.e. Equation 5 and Equation 7). In that case, the system has no stable fixed point and from Lemma 1 it is bounded so it has one of limit cycle, quasi-periodic or chaotic behaviors. In particular, Theorem 2 states that the odd number of inhibitory nodes is not sufficient. Indeed, when Equation 4 holds and nI is odd, no oscillations are possible as the fixed point is globally stable. It is also the case when nI is even which corresponds to Thomas’ conjecture.

Finally, there is a gap in between the conditions (between Equation 4 and Equation 5 for example) for which the long-term behavior is not determined.

## Remark 2

In particular, if for all i∈[n], wi=w∈ℝ+* and for all k∈[nI], bak=b∈ℝ+*, then the dynamics of the system only depends on w. When nI is even: w<1 implies that TLN(W,b) have a unique globally asymptotically stable fixed point; w>1 implies that the fixed point for w<1 becomes unstable and TLN(W,b) has two more asymptotically stable fixed point. If nI is odd, TLN(W,b) only has a unique fixed point which is asymptotically stable when w<1cos(π/n) (globally when w<1) and unstable when w>1cos(π/n).

## Remark 3

In Theorem 2, we assume that the external inputs are absent for excited nodes. Assume that the external input to any excited node, say node ak<i<ak+1, is strictly positive. Then, bounding its dynamics as in Lemma 1, we know that its activity will be more than bi. Hence, the next inhibited node ak+1 can be silenced forever ifbi∏j=iak+1−1wj>bak+1,

thus destroying the cycle structure and thus preventing oscillation from emerging.

On the other hand, if the external inputs to excited nodes are strictly negative, Theorem 2 conclusion will be similar but now with condition described in Equation 4 replaced bybak∏i=akak+1−1wi−∑j=ak+1ak+1−1bj∏i=jak+1−1wi<bak+1.

This means that cycles with even (odd) inhibitory nodes need strong enough connections to generate multi-stability (limit cycle). We now clarify that the latter condition relates to weights’ strength. With w=(w1,⋯,wn) and using the set of functions increasing functions (fi)1≤i≤n such thatfiw,b(x)=wi−1xi−1−bi

one can write the last condition asfak+1w,b∘⋯∘fakw,b(bak)<0.

Hence, the left term is increasing with any weight strength.

One should also note that under this negative input assumption to excited nodes, when weights are weak, the support of the fixed point might be different from [n]. In particular, some excited nodes might not belong to the support.

## Remark 4

When the decay rates are not the same (here all of them are −1), similar results hold but then the conditions for stability are more difficult to state precisely. Finally, when considering the EI network (two nodes), the system always admits to a unique globally asymptotically stable fixed point with support {1,2}. Indeed, it is easy to show that the system will always reach the domain where the inhibitory node is small enough so that one can remove the threshold function in Equation 1 and thus the eigenvalues of the Jacobian matrix are ±i⁢w1⁢w2-1. No oscillations are then possible, which is an easy example to show that negative loops are not sufficient to generate oscillation in non smooth dynamical systems.

Similar results have been shown by Gouzé, 1998; Snoussi, 1998. Considering dynamical systems of the form x˙=f⁢(x) where f is a continuously differentiable function on a given open convex set and f has a constant sign Jacobian matrix, they used graph theory methods to show that negative loop in this matrix is a necessary condition to generate oscillations. In our case, f is not continuously differentiable, the Jacobian matrix elements can change sign within the state space and we show that there is a need of additional constraints for oscillations to arise. A formal proof of the aforementioned theorems is provided in Appendix A by using classical dynamical theory tools.

## Intuition behind the proof of the theorems

The idea behind our proof can be explained graphically. We assume that nodes cannot oscillate due to their intrinsic activity and a fixed external input only drives them to a non-zero activity which does not change over time. Therefore, they need input from their pre-synaptic (upstream) nodes to change their state in a periodic manner to generate oscillations. In such a network, if we perturb the node i with a pulse-like input, it is necessary that the perturbation travels through the network and returns to the node i with a 180° phase shift (i.e. with an inverted sign). Otherwise, the perturbation dies out and each node returns to a state imposed by its external input.

In a network without directed cycles, it is possible to sort the nodes into smaller groups where nodes do not connect to each other (Figure 2a). That is, a network with no directed cycles, can be rendered as a feed-forward network in which the network response by definition does not return to the node (or group) that was perturbed. Such a network can only oscillate when the intrinsic dynamics of individual nodes allow for oscillatory dynamics.

![Figure 2.](https://cdn.elifesciences.org/articles/88777/elife-88777-fig2-v1.jpg)

**Figure 2.:** (a) A visual representation of why directed cycles are important in network oscillation. By rearranging all nodes, any network without directed cycles can be seen as a feed-forward network which will make the system reach a stable fixed point. (b) An intuitive explanation of the odd inhibitory cycle rule by showing the activities of two 6-node-loops. Odd inhibitory connections (bottom) can help the system oscillate, while even inhibitory connections has the opposite effect.

However, having a directed cycle is no guarantee of oscillations because network activity must return to the starting node with a 180° phase shift. This requirement puts a constraint on the number of inhibitory connections in the cycles. When we assume that there are no delays (or the delay is constant) in the connections, excitatory connections do not introduce any phase shift, however, inhibitory connections shift the phase by 180° (in the simplest case invert the sign of the perturbation). Given this, when a cycle has an even number of inhibitory connections the cycle cannot exhibit oscillations (Figure 2b,top). However, replacing an inhibitory connection by an excitatory one can render this cycle with an ability to oscillate (Figure 2b, bottom). Therefore, odd number of inhibitory appears to be necessary for oscillation to emerge.

## The effect of network parameters on oscillations

To test the validity of our theorems in more realistic biological neuronal networks, we numerically simulated the dynamics of the Wilson-Cowan model. Specifically, we investigated the role of synaptic transmission delays, synaptic weights, external inputs and self-connection in shaping the oscillations when the network has directed cycles. In particular, we focused on two networks: the III motif with three inhibitory nodes (odd inhibitory links) and the EII motif with one excitatory and two inhibitory nodes (even inhibitory links).

Our numerical simulation showed that for a wide range of parameters (synaptic delays, synaptic weights, external input and self-inhibition), while III network showed oscillations, EII network only resulted in transient oscillations (Figure 3, Figure 3—figure supplements 1 and 2). The oscillation frequency however depended on the exact value of the synaptic delays, synaptic weights and external inputs. For instance, increasing the synaptic delay reduced the oscillation frequency (Figure 3b). Synaptic delays play a more important role in shaping the oscillations in an EI type network (see Figure 3—figure supplement 3, Appendix 2—table 1). In networks with even number of inhibitory connections (e.g. EII, EEE, II), synaptic delays are the sole mechanism for initiating oscillations, however, unless delays are precisely tuned such oscillations will remain be transient (see Figure 3—figure supplement 2). The effect of increasing the synaptic strength was contingent on the external inputs. In general, increasing the synaptic strength resulted in a reduction in the oscillation frequency (Figure 3c). Next, oscillation frequency changed in a non-monotonic fashion as a function of external input irrespective of the choice of other parameters (Figure 3d). Typically, a mid-range input strength resulted in maximum oscillation frequency. Finally, increasing the self-connection of nodes increased the oscillation frequency but beyond a certain self-connection the node was completely silenced and it changed the network topology and oscillations disappeared (Figure 3e).

Overall, these results are consistent with our rule that odd number of inhibitory nodes and strong enough connections are necessary to induce oscillations in a directed cycle. The actual frequency of oscillations depends on specific network parameters.

## Oscillators in the cortex-basal ganglia network

Next, we use our theorem to explain recent experimental observations about the mechanisms underlying the emergence of oscillations in the BG. Emergence of 15–30  Hz (beta band) oscillations in the cortico-basal ganglia (CBG) network is an ubiquitous feature of PD Raz et al., 2000; Bergman et al., 1998; Sharott et al., 2014; Neumann et al., 2016. Based on their connectivity and activity subthalamic nucleus (STN) and the globus pallidus externa (GPe) subnetwork has emerged as the most likely generator of beta oscillations Plenz and Kital, 1999; Bevan et al., 2002. The STN-GPe subnetwork becomes oscillatory when their mutual connectivity is altered Terman et al., 2002; Holgado et al., 2010 or neurons become bursty Tachibana et al., 2011; Bahuguna et al., 2020 or striatal inputs to GPe increase Kumar et al., 2011; Mirzaei et al., 2017; Sharott et al., 2017; Chakravarty et al., 2022. However, oscillations might also be generated by the striatum McCarthy et al., 2011, by the interaction between the direct and hyperdirect pathways Leblois et al., 2006 and even by cortical networks that project to the BG (Brittain and Brown, 2014). Recently, Crompe et al., 2020 used optogenetic manipulations to shed light on the mechanisms underlying oscillation generation in PD. They showed that GPe is essential to generate beta band oscillations while motor cortex and STN are not. These experiments force us to rethink the mechanisms by which beta band oscillations are generated in the CBG network.

To better understand when GPe and/or STN are essential for beta band oscillations, we identified the network motifs which fulfill the odd inhibitory cycle rule. For this analysis, we excluded D1 SPNs because they have a very low firing rate in the PD condition Sharott et al., 2017. In addition, cortex is assumed as a single node in the CBG network.

The CBG network can be partitioned into 246 subnetworks with 2, 3, 4, 5, 6, or 7 nodes (see Figure 4—figure supplements 1–6). Among these partitions, there are five loops (or cycles) in the CBG network with one or three inhibitory projections: Proto-STN, STN-GPi-Th-cortex, STN-Arky-D2-Proto, Proto-Arky-D2, Proto-FSN-D2, and Proto-GPi-Th-Cortex-D2 (Figure 4a). One or more of these 6 loops appeared in 96 (out of 246) subnetworks of CBG (see Figure 4b, colors indicate different loops). Larger subnetworks consisting of 5 and 6 nodes have multiple smaller subnetworks (with 2 or 3 nodes) that can generate oscillations (boxes with multiple colors in Figure 4b).

Based on our odd inhibitory cycles in BG, we found three oscillatory subnetworks which do not involve the STN (Figure 4a, cyan, green and purple subnetworks). However, each of these oscillatory subnetworks involves Prototypical neurons (from the GPe) which receive excitatory input from STN. Therefore, it is not clear whether inhibition of STN can affect oscillations or not. To address this question, we first simulated the dynamics of a four-node motif (Figure 4c top) using the Wilson-Cowan type model (see Methods). In this subnetwork, we have three cycles: Proto-STN loop with one inhibitory connection, Proto-STN-Arky-D2 loop with three inhibitory connections and Proto-Arky-D2 with three inhibitory connections.

We systematically varied external inputs to the STN and D2-SPNs and measured the frequency of oscillations (see Methods). We found that for weak inputs to the D2-SPNs, the Proto-STN subnetwork generated oscillations for weak positive input (Figure 4c bottom). However, as the input to D2-SPNs increased, the oscillation frequency decreased and oscillations were observed even for very strong drive to STN (Figure 4c bottom). That is, in this model, both Proto-STN and Proto-D2-Arky subnetworks compete for oscillations, which subnetwork wins depending on their inputs. To disentangle the oscillations of each of these two subnetworks, we performed ‘lesion’ experiments in our model (see Methods). These experiments also mimicked lesions performed in non-human primates Tachibana et al., 2011.

When we removed the D2-SPN to Proto projections, the network could oscillate but only because of the Proto-STN subnetwork (Figure 4d). In this setting, we get relatively high-frequency beta band oscillations but only for a small range of excitatory inputs to the STN (Figure 4d, bottom). In this setting, inhibition of STN would certainly abolish any oscillation. Next, we removed the STN output (equivalent to inhibition of STN), the Proto-D2-Arky subnetwork generated oscillations for weak positive inputs to the D2-SPNs (Figure 4e, bottom). Note that unlike in Figure 4c, here we injected additional input to Proto to compensate for the loss of excitatory input from STN and to ensure that it had sufficient baseline activity. The frequency of Proto-D2-Arky oscillations was smaller than that observed for the Proto-STN subnetwork because the former involves a three synapses loop. However, as we have shown earlier, frequency of oscillation can be changed by scaling the connection weights or external inputs (Figure 3). Overall, these results suggest that, in principle, it is possible for CBG network to oscillate even when STN is removed from the network.

## Oscillations in model of basal ganglia with spiking neurons

Thus far we have only illustrated the validity of our theorems in a firing rate-based model. To be of any practical value to brain science, it is important to check whether our theorems can also help in a network with spiking neurons. To this end, we simulated the two subnetworks with 3 inhibitory connections: Proto-D2-FSN and Proto-D2-Arky (see Methods). These subnetworks were simulated using a previous model of BG with spiking neurons Chakravarty et al., 2022.

The subnetworks Proto, Arky, D2-SPN, FSN have very little recurrent connectivity to oscillate on their own. We provided Poisson type external input. All neurons in a subnetwork received the same input rate but a different realization of the Poisson process. Both Proto-D2-FSN (Figure 5a) and Proto-D2-Arky (Figure 5b) subnetworks showed β-band oscillations. In the loop Proto-D2-FSN, D2-SPN neurons have a relatively high firing rate. This could be a criterion to exclude this loop as a potential contributor to the beta oscillations.

![Figure 5.](https://cdn.elifesciences.org/articles/88777/elife-88777-fig5-v1.jpg)

**Figure 5.:** (a-b) Average peristimulus time histograms (PSTH) of all neurons in a Proto-FSN-D2 and (b) Proto-Arky-D2 motifs under Parkinson condition with power spectral density (PSD) at the top right. (c) PSTH of Proto and STN in a BG subnetwork with motif Proto-Arky-D2 as the oscillator during different STN inhibition. (d) Same thing as (c) but changing the oscillator from Proto-Arky-D2 to Proto-STN.

Next, we mimicked the STN inhibition experiments performed by Crompe et al., 2020 in our model. To this end, we simulated the dynamics of BG network excluding D1-SPNs (because of their low firing rate in PD condition) and FSN (because with FSNs in the oscillation loop, D2-SPNs may have non-physiological firing rates). In this reduced model of BG, we changed inputs to operate in a mode where either Proto-D2-Arky (Figure 5c) or Proto-STN (Figure 5d) loop was generating the oscillations. In both cases, we systematically increased the inhibition of STN neurons.

In the Proto-D2-Arky mode, as we inhibited STN neurons, firing rate of the Proto neurons decreased and oscillations in STN population diminished but Proto neurons showed clear beta band oscillations (Figure 5c). By contrast, and as expected when STN-Proto loop was generating the oscillations, increasing the STN inhibition abolished the oscillations in both STN and Proto neurons (Figure 5d). In STN-Proto loop, when STN is inhibited, there is no cycle left in the network and therefore oscillations diminished, whereas the Proto-D2-Arky loop remains unaffected by the STN inhibition (except for a change in the firing rate of the Proto neurons). As shown in Figure 4c, whether oscillations are generated by the Proto-D2-Arky or STN-Proto loop depends on the relative input to the D2 or STN neurons. So it is possible that in rodents, D2-SPN have stronger input from the cortex than STN and therefore, oscillations survive despite near complete inhibition of STN.

## Discussion

Here, we prove in a single cycle TLN model and illustrate with numerical simulations of biological networks that when the number of inhibitory nodes in a directed cycle is odd and connections are strong enough, then the system has the potential to oscillate. In 1981, Thomas, 1980 conjectured that at least one negative feedback loop (i.e. a loop with an odd number of repressors) is needed for gene regulatory networks to have periodic oscillating behavior. This conjecture was proven for Boolean dynamical systems by Snoussi, 1998 and Gouzé, 1998. But their proof required that node transfer-function is differentiable everywhere. We here prove a more complete theorem for a case where node transfer-function is threshold-linear as is the case for many network in the brain. Thus, together with previous results of Snoussi, 1998 and Gouzé, 1998 we further expand the scope within which we can comment on the potential of a network to generate oscillation based only on the connectivity structure alone. In addition, we complete this condition by one on weights’ strength stating that the latter needs to be strong enough for the system to possibly oscillate. Eventually, oscillations can be quenched by adding positive external input to excited nodes.

A key assumption of our analysis is that there are no delays in the network. Indeed, delays within and between subnetwork connections can have a big effect on the oscillations Kim et al., 2020. In the numerical simulations of BG network, we included biologically realistic synaptic delays (i.e. connection delays were shorter than the time constants of the neurons). Our results suggest that such delays do not influence our results and they only determine the oscillation frequency. But it is not possible to comment on how the results may change when delays become longer than the time constant of the node.

## Interactions between input and network structure

Previous models suggest that when we excite the excitatory node or inhibit the inhibitory node oscillations can emerge and strengthen Kumar et al., 2011; Ledoux and Brunel, 2011. By contrast, when we inhibit the excitatory node or excite the inhibitory node, oscillations are quenched. This can be summarised as the ’Oscillations Sign Rule’. Let us label the excitatory population as positive and inhibitory as negative. Let us also label excitatory inputs as positive and inhibitory inputs as negative. Now if we multiple the sign of the node and sign of the stimulation, we can comment on the fate of oscillations in a qualitative manner. For example, inhibition of inhibitory nodes would be − × − = + that is oscillations should be increased and when we inhibit excitatory nodes, it would be − × + = − that is oscillations should be decreased. The ’Oscillation sign rule’ scales to larger network with more nodes. With the ’Odd Cycle Rule’ as we have shown we can comment on whether a directed cycle will oscillate or not from the count of inhibitory links. When we combine the ’Oscillations Sign Rule’ with the ’Odd Cycle Rule’ we can get a more complete qualitative picture of whether a stimulating a node in a network will generate oscillations or not.

## Interaction between node properties and network structure

In our proof we have assumed that nodes follow rather simple dynamics and have a threshold-linear transfer-function. In reality nodes in physical, chemical and biological systems can have more complex dynamics. For instance, biological neurons have the property of spike frequency adaptation or rebound spiking. Similarly, synapses in the brain can increase or decrease their weights based on the recent history of inputs which is referred to as the short-term-facilitation or short-term-depression of synapses Stevens and Wang, 1995. Such biological properties can be absorbed in the network structure in the form of an extra inhibitory or excitatory connection. When nodes can oscillate given their intrinsic dynamics then the question becomes more about whether a network structure can propagate oscillations to other nodes.

## Oscillations in the basal ganglia

We applied our results to understand the mechanisms underlying the emergence of PD-related pathological oscillations in the BG. Given that there are 8 key neuron populations in the BG, we enumerated 238 possible directed cycles. From 2-node-motifs to 6-node-motifs, our odd cycle rule identified 88 potential directed cycles that can generate oscillations. Among these, 81 cycles feature GPe (either Proto or Arky type or both) and 66 feature STN. Which specific cycle underlies oscillations depends on the exact input structure. For instance, when input to STN is higher than the D2 neurons, the STN-GPe network generates oscillations. But when inputs to D2 neurons are stronger, the D2-Proto-Arky cycle can become the oscillator. That is, STN is not necessary to generate oscillations in the BG. Our results also suggest that besides focusing on the network connectivity, we should also estimate the inputs to different nodes in order to pinpoint the key nodes underlying the PD-related pathological oscillations - that would be the way to reconcile the recent findings of Crompe et al., 2020 with previous results.

We would like to note that recently, Ortone et al., 2023 and Azizpour Lindi et al., 2023 have provided a more quantitative explanation of the experimental observation by Crompe et al., 2020. They also eventually resort to the D2-Proto-Arky cycle to explain BG oscillations in the absence of STN. Our work provides the necessary theory to explain their results.

## Beyond neural networks

In this work, we have used the odd cycle rule to study oscillations in BG. However, oscillatory dynamics and the odd cycle rule show up in many chemical, biological and even social systems such as neuronal networks Bel et al., 2021, psychological networks Greenwald et al., 2002, social and political networks Leskovec et al., 2010; Milo et al., 2004; Heider, 1946; Cartwright and Harary, 1956, resting-state networks in autism Moradimanesh et al., 2021 and gene networks Farcot and Gouzé, 2010; Allahyari et al., 2022. In fact, originally Thomas’ conjecture Thomas, 1980 about the structural conditions for oscillations was made for gene regulatory networks. Therefore, we think that insights obtained from our analytical work can be extended to many other chemical, biological and social networks. It would be interesting to check to what extent our prediction of quenching oscillation by exciting the excitatory nodes holds in other systems besides biological neuronal networks.

## Methods

To study the emergence of oscillations in the BG, we used three models: Threshold-Linear Network (TLN), Wilson-Cowan model and network with spiking neurons. TLN model (Equation 1) was used here to rigorously prove that simple conditions, such as the odd inhibitory cycle rule, can lead to oscillations (Theorems 1 and 2). Wilson-Cowan type firing rate-based model was used to find the structural constraints on oscillations and to determine the effect of network properties (such as delays, synaptic weights, external inputs, and self-inhibition) on the emergence of oscillations. Finally, to demonstrate the validity of the odd inhibitory cycle rule in a more realistic model, we use a network with spiking neurons.

## Wilson-Cowan dynamics

In the firing rate-based models, we reduced each CBG subnetwork to a single node. To describe firing rate dynamics of such a node, we used the classic Wilson-Cowan model Wilson and Cowan, 1972(10)τdri(t)dt=−ri(t)+F(∑j=1nwijrj+Iiext)

where ri⁢(t) is the firing rate of the ith node, τ is the time constant of the population activity, n is the number of nodes (or subnetworks), wi⁢j is the strength of connection from node j to i, and Iie⁢x⁢t is the external input to the population. F is a nonlinear activation function relating output firing rate to input, given by(11)F(x)=11+e−a(x−θ)−11+eaθ

where the parameter θ is the position of the inflection point of the sigmoid, and a/4 is the slope at θ. Here, τ, θ, and a are set as 20, 1.5, and 3. Other parameters of the model varied with each simulation. The simulation specific parameters for Figure 3 are shown in Tables 1 and 2 and for Figure 4 are shown in Table 3, respectively.

## Network model with spiking neurons

The BG network with spiking neurons was taken from a previous model by Chakravarty et al., 2022. Here, we describe the model briefly and for details we refer the reader to the paper by Chakravarty et al., 2022.

## Spiking neuron model

Here, we excluded D1-SPNs because they have a rather small firing rate in PD conditions. The striatal D2-type spiny neurons (D2-SPN), fast-spiking neurons (FSNs) and STN neurons were modelled as standard LIF neurons with conductance-based synapses. The membrane potential Vx⁢(t) of these neurons was given by:(12)CmxdVx(t)dt=Ie(t)+Isyn(t)−gLx[Vx(t)−Vresetx]

where x∈{D2−SPN,FSN,andSTN}, Ie⁢(t) is the external current induced by Poisson type spiking inputs (see below), Is⁢y⁢n⁢(t) is the total synaptic input (including both excitatory and inhibitory inputs). When Vx reached the threshold potential Vt⁢hx, the neuron was clamped to Vr⁢e⁢s⁢e⁢tx for a refractory duration  tr⁢e⁢f = 2ms. All the parameter values and their meaning for D2-SPN, FSN, and STN are summarized in Appendix 2—tables 2–4, respectively.

We used the LIF model with exponential adaptation (AdEx) to simulate Proto and Arky neurons of the globus pallidus externa (GPe), with their dynamics defined asCxVx(t)dt=−gLx[Vx(t)−Vresetx]−wx+Isynx(t)+Ie+gLxΔTexp⁡(Vx(t)−VTxΔT)τww˙x=a(Vx(t)−Vresetx)−wx

where x∈{Proto,Arky}. Here when Vx⁢(t) reaches the threshold potential (Vt⁢hx), a spike is generated and Vx⁢(t) as well as wx will be reset as Vresetx, wx+b, respectively, where b denotes the spike-triggered adaptation. The parameter values and their meaning for Proto and Arky are specified in Appendix 2—table 5. Neurons were connected by static conductance-based synapses. The transient of each incoming synaptic current is given by:Isyn x(t)=gsyn x(t)[Vx(t)−Erevx]

where x∈{D2−SPN,FSN,STN,Arky,andProto} is the synaptic reversal potential and gsynx⁢(t) is the time course of the conductance transient, given as follows:gsynx(t)={Jsynxtτsynexp⁡(−(t−τsyn)τsyn), for t≥00, for t<0,

where syn∈{exc,inh}, Js⁢y⁢nx is the peak of the conductance transient and τsyn is synaptic time constant. The synaptic parameters are shown in Appendix 2—table 6.

Some of model parameters were changed to operate the BG model in specific modes dominated by a 2 or 3 nodes cycle. The Appendix 2—table 7 and Appendix 2—table 8 show the parameters of Figure 5c and Figure 5d, respectively.

## External input

Each neuron in each sub-network of the BG received external input in the form of excitatory Poisson-type spike trains. This input was provided to achieve a physiological level of spiking activity in the network. For more details please see Chakravarty et al., 2022. Briefly, the external input was modelled as injection of Poisson spike-train for a brief period of time by using the inhomogeneous_poisson_generator device in NEST. The strength of input stimulation can be controlled by varying the amplitude of the EPSP from the injected spike train.

## STN inhibition experiment

We set a subnetwork of BG to study how STN inhibition affects oscillation when different motifs dominate the system. The connections and external inputs to each neuron in Figure 5c and 5d are shown in Appendix 2—tables 7 and 8. To simulate the increasing inhibition to STN, the external input to STN was reduced from 1 pA to –99 pA in Figure 5c and from 30 pA to –50 pA in Figure 5d.

## Data analysis

The estimate of oscillation frequency of the firing rate-based model was done using the power spectral density calculated by pwelch function of MATLAB. The spiking activity of all the neurons in a sub-population were pooled and binned (rectangular bins, bin width = 0.1ms). The spectrum of spiking activity was then calculated for the binned activity using pwelch function of MATLAB.

## Simulation tools

Wilson-Cowan type firing rate-based model was simulated using Matlab. All the relevant differential equations were integrated using Euler method with a time step of 0.01ms. The network of spiking neurons was simulated in Python 3.0 with the simulator NEST 2.20 Fardet et al., 2020. During the simulation, differential equations of BG neurons were integrated using Runga–Kutta method with a time step of 0.1ms.

## Code availability

The code to simulate key results is available at https://github.com/jiezang97/Code-for-Structural-constraints-on-the-emergence-of-oscillations, copy archived at Zang, 2024.
