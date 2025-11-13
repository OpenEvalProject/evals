# An incentive circuit for memory dynamics in the mushroom body of Drosophila melanogaster

## Authors

- Evripidis Gkanias<sup>1</sup> ([ORCID: 0000-0003-3343-9039](https://orcid.org/0000-0003-3343-9039)) †
- Li Yan McCurdy<sup>2</sup> ([ORCID: 0000-0002-8862-6715](https://orcid.org/0000-0002-8862-6715))
- Michael N Nitabach<sup>2</sup>
- Barbara Webb<sup>1</sup> †

### Affiliations

1. Institute of Perception Action and Behaviour, School of Informatics, University of Edinburgh Edinburgh United Kingdom ([ROR:01nrxwf90](https://ror.org/01nrxwf90))
2. Department of Cellular and Molecular Physiology, Yale University New Haven United States ([ROR:03v76x132](https://ror.org/03v76x132))
3. Department of Genetics, Yale University New Haven United States ([ROR:03v76x132](https://ror.org/03v76x132))
4. Department of Neuroscience, Yale University New Haven United States ([ROR:03v76x132](https://ror.org/03v76x132))

† Corresponding author

## Abstract

Insects adapt their response to stimuli, such as odours, according to their pairing with positive or negative reinforcements, such as sugar or shock. Recent electrophysiological and imaging findings in Drosophila melanogaster allow detailed examination of the neural mechanisms supporting the acquisition, forgetting, and assimilation of memories. We propose that this data can be explained by the combination of a dopaminergic plasticity rule that supports a variety of synaptic strength change phenomena, and a circuit structure (derived from neuroanatomy) between dopaminergic and output neurons that creates different roles for specific neurons. Computational modelling shows that this circuit allows for rapid memory acquisition, transfer from short term to long term, and exploration/exploitation trade-off. The model can reproduce the observed changes in the activity of each of the identified neurons in conditioning paradigms and can be used for flexible behavioural control.

## Introduction

Animals deal with a complicated and changing world, and they need to adapt their behaviour according to their recent experience. Rapid changes in behaviour to stimuli accompanied by intense reinforcement require memories in the brain that are readily susceptible to alteration. Yet associations experienced consistently should form long-term memories (LTMs) that are hard to change. Memories that are no longer valid should be forgotten. Every neuron cannot have all of these properties, but they must be connected in a circuit, playing different roles such as supporting short-term memory (STM) or LTM, and enabling processes to form, retain, and erase memories. This complex interaction of memory processes is familiar in principle, but its implementation at the single-neuron level is still largely a mystery.

The fruit fly Drosophila melanogaster is able to form, retain, and forget olfactory associations with reinforcements, for example, electric shock. The key neural substrate is known to lie in the neuropils of their brain called the mushroom bodies (MBs) (Davis, 1993; Heisenberg, 2003; Busto et al., 2010). There are two MBs in the insect brain, one in each hemisphere, composed of intrinsic and extrinsic neurons. Extrinsic projection neurons (PN) deliver sensory input to the only intrinsic neurons of the MBs, the Kenyon cells (KCs), whose long parallel axons travel through the pendunculus and then split forming the vertical (α/α′) and medial (β/β′ and γ) MB lobes (see Figure 1). The extrinsic mushroom body output neurons (MBONs) extend their dendrites in different regions of the lobes, receiving input from the KCs and forming 15 distinct compartments (Turner et al., 2008; Tanaka et al., 2008; Campbell et al., 2013; Aso et al., 2014a). Their activity is thought to provide motivational output that modulates the default behaviour of the animal (Aso et al., 2014b). Different groups of extrinsic dopaminergic neurons (DANs) terminate their axons in specific compartments of the MB and modulate the connections between KCs and MBONs (Aso et al., 2014a). Many of the DANs respond to a variety of reinforcement signals (Mao and Davis, 2009; Schwaerzel et al., 2003; Claridge-Chang et al., 2009; Liu et al., 2012; Lin et al., 2014), and therefore, they are considered the main source of reinforcement signals in the MB. Finally, many of the MBON axons and DAN dendrites meet in the convergence zones (CZs), where they create interconnections, such that the motivational output can also influence the activity of the reinforcement neurons (Li et al., 2020).

![Figure 1.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig1-v1.jpg)

**Figure 1.:** Left: the main anatomical pathways. In the illustration, the presented odour activates the Kenyon cells (KCs) through the projection neurons (PNs). The parallel axons of KCs propagate this signal to the lobes of the mushroom body. The mushroom body output neurons (MBONs) extend their dendrites in the mushroom body lobes, receiving input from the KCs. Electric shock creates a punishing signal that excites some dopaminergic neurons (DANs), whose axons terminate in the lobes and modulate the synaptic weights between KCs and MBONs. Right: schematic of potential connections between punishment/reward DANs and approach/avoidance MBONs. Note that although DANs transferring punishing signals modulate the KC activation of MBONs that encode positive motivations (decreasing attraction to the presented odour and increasing attraction to odours not present [the dopaminergic plasticity rule]), MBONs that encode negative motivations will also gain higher responses due to release of inhibition between MBONs, and the feedback connections from MBONs to other DANs. In our model, we further decompose these functions using three DANs and three MBONs for each motivation (positive or negative) and map these units to specific identified neurons and microcircuits in the brain of Drosophila. These circuits include some direct (but not mutual) MBON-MBON connections (dashed inhibitory connections).

Several computational models have tried to capture the structure and function of the MBs, usually abstracting the common features of this network across various insect species. Modellers have treated the MBs as performing odour discrimination (Huerta et al., 2004), olfactory conditioning (Balkenius et al., 2006; Smith et al., 2008; Finelli et al., 2008; Young et al., 2011; Wessnitzer et al., 2012; Peng and Chittka, 2017; Faghihi et al., 2017; Zhao et al., 2021; Springer and Nawrot, 2021; Eschbach et al., 2020; Bennett et al., 2021), or calculating the scene familiarity (Wu and Guo, 2011; Baddeley et al., 2012; Arena et al., 2013; Bazhenov et al., 2013; Ardin et al., 2016). However, it seems like they can subserve all these functions, depending on context (or experience), that is, what is driving the activity of the KCs (Cohn et al., 2015). This suggests that the output neurons of the MB do not just inform the animal whether an odour is known or attractive, or if a scene is familiar, but they actually motivate the animal to take an action like approach, avoid, escape, or forage. There is emerging evidence supporting this idea of the MBONs driving non-binary but antagonistic motivations (Schwaerzel et al., 2003; Krashes et al., 2009; Gerber et al., 2009; Waddell, 2010; Lin et al., 2014; Perisse et al., 2016; Senapati et al., 2019), which has started to be explored in recent models.

In addition to the structural and functional depiction of the MBs, a variety of plasticity rules have been used in order to explain the effect of dopamine emitted by the DANs on the KC→MBON synapses. Although the best supported biological mechanism is that coincidence of DAN and KC activity depresses the output of KCs to MBONs, most of the models mentioned before use variations of the Hebbian rule (Hebb, 2005), where the coincidence of the input (KCs) and output (MBONs) activation strengthens the synaptic weight (or weakens it for the anti-Hebbian case) and this is gated by the reinforcement (DANs). More recent approaches that try to model the activity of DANs and MBONs in the brain have used plasticity rules (Zhao et al., 2021) or circuit structures (Springer and Nawrot, 2021; Bennett et al., 2021; Eschbach et al., 2020) that implement a reward prediction error (RPE) (Rescorla and Wagner, 1972), which is the most widely accepted psychological account of associative learning with strong validation evidence in the vertebrate brain (Niv, 2009). For the MB, this plasticity rule is interpreted as the output (MBON) being the prediction of the reinforcement (DAN), so their difference (gated by the activity of the input, KC) drives the synaptic plasticity. However, details of neuronal dynamics in fruit flies (Hige et al., 2015; Dylla et al., 2017; Berry et al., 2018) suggest that neither Hebbian nor RPE plasticity rules capture the plasticity dynamics in the MBs (also in larva: Schleyer et al., 2018; Schleyer et al., 2020) as both rules need the conditional stimuli (CS) to occur (KCs to be active) for synaptic weight change. This highlights the importance of investigating new plasticity rules that are a closer approximation to the actual dopaminergic function.

In this work, we propose such a novel plasticity rule, named the dopaminergic plasticity rule (DPR), which reflects a recent understanding of the role of dopamine in depression and potentiation of synapses. Based on the evidence of existing MBON→DAN connections, we build a 12-neuron computational model, which we call the incentive circuit (IC), and uses the proposed plasticity rule. In this model, we name three types of DANs (‘discharging’, ‘charging’, and ‘forgetting’) and three types of MBONs (‘susceptible’, ‘restrained’, and ‘LTM’) for each of the two opposing motivational states. We demonstrate that the neural responses generated by this model during an aversive olfactory learning paradigm replicate those observed in the animal; and that simulated flies equipped with the IC generate learned odour preferences comparable to real flies. Finally, we suggest that such a model could work as a motif that extends the set of motivations from binary (e.g., avoidance vs. attraction) to a spectrum of motivations whose capabilities are equivalent to ‘decision-making’ in mammals.

## Results

### The dopaminergic plasticity rule

We implement a novel dopaminergic plasticity rule (DPR) to update the KC→MBON synaptic weights proportionally to the dopamine level, KC activity, and current state of the synaptic weight with respect to its default (rest) value. Our DPR is based on recent findings regarding the role of dopamine (and co-transmitters) in altering synaptic efficacy in the fruit fly MB (see methods section ‘Derivation of the dopaminergic plasticity rule’). Instead of calculating the error between the reinforcement and its prediction, DPR uses the reinforcement to maximise the separation between the synaptic weights of reinforced inputs, which is functionally closer to the information maximisation theory (Bell and Sejnowski, 1995; Lee et al., 1999; Lulham et al., 2011) than the RPE principle. While this rule, in combination with some specific types of circuits, can result in the prediction of reinforcements, it can also support a more flexible range of responses to stimulus-reinforcement contingencies, as we will show in what follows.

The dopaminergic learning rule is written formally as

$$
ΔW_{k2m}^{ij}(t)=\delta^{j}(t)[k^{i}(t)+W_{k2m}^{ij}(t)−w_{rest}]
$$

where $Δ⁢W_{k⁢2⁢m}^{i⁢j}$ is the change in the synaptic weight connecting a KC, i, to an MBON, $j$. The KC→MBON synaptic weight, $W_{k⁢2⁢m}^{i⁢j}\geq0$, and the KC response, $k^{i}⁢(t)\geq0$, have a lower bound of 0, while the resting weight, $w_{rest}=1$, is a fixed parameter. The rule alters the connection weight between each KC and MBON on each time-step depending on the dopaminergic factor, $\delta^{j}⁢(t)$, which is determined by the responses of the DANs targeting this MBON. The dopaminergic factor can be positive [$\delta^{j}(t)>0$] or negative [$\delta^{j}(t)<0$], which we motivate from recent observations of the differential roles in synaptic plasticity of DopR1 and DopR2 receptors (Handler et al., 2019), as detailed in ‘Materials and methods’. When combined with two possible states of KC activity (active or inactive), this results in four different plasticity effects: depression, potentiation, recovery, and saturation.

These effects can be inferred directly from Equation 1. If the dopaminergic factor is zero (contributing DANs are inactive or mutually cancelling), no learning occurs. If the dopaminergic factor is negative and the KC is active (positive), the KC→MBON synaptic weight is decreased (depression effect of the plasticity rule, see Figure 2A). However, if the synaptic weight is already low, the synaptic weight cannot change further. The recovery effect takes place when the dopaminergic factor is negative and the KC is inactive ($k^{i}⁢(t)=0$), in which case the synaptic weights tend to reset to the resting weight (see Figure 2C). When the dopaminergic factor is positive and the KC is active, we have the potentiation effect, which causes an increase in the synaptic weights (see Figure 2B). In contrast to the depression effect, as the synaptic weight becomes stronger, it further enhances this effect. If the KC is inactive and the dopaminergic factor is positive, then we have the saturation effect, where if the current synaptic weight is higher than its resting weight, the synaptic weight continues to increase, while if it is lower then it continues to decrease (see Figure 2D). This effect enhances diversity in the responses of the MBON to the different past and current CS experiences, which is essential for memory consolidation (i.e., continued strengthening of a memory) and the formation of long-term memories (i.e., slower acquisition and resistance to further change).

![Figure 2.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig2-v1.jpg)

**Figure 2.:** The dopaminergic plasticity rule (DPR) can cause four different effects that work in harmony or discord to maximise the information captured in each experience and allow different types of memories to be formed for each KC→MBON synapse. In each box, time-step $t=t_{pre}$ shows the initial KC→MBON synaptic weights (thickness of the arrows); electric shock activates the DAN in time-step $t=t_{learn}$ causing modulation of the synaptic weights (red: increase; blue: decrease), while time-step $t=t_{post}$ shows the synaptic weights after the shock delivery. (A) Example of the depression effect – the synaptic weight decreases when $\delta^{j}(t)<0$ and the KC is active. (B) Example of the potentiation effect – the synaptic weight increases when $\delta^{j}(t)>0$ and the KC is active. (C) Example of the recovery effect – the synaptic weight increases when $\delta^{j}(t)<0$ and the KC is inactive. (D) Example of the saturation effect – the synaptic weight increases further (when $W_{k2m}^{ij}(t)>w_{rest}$) or decreases further (when $W_{k2m}^{ij}(t)<w_{rest}$) when $\delta^{j}(t)>0$ and the KC is inactive. MBON: mushroom body output neuron.

The different effects described above can work together in single KC→MBON synapses (i.e., through the influence of multiple DANs), leading to more complicated effects like the formation of short-term memories (e.g., combining the depression/potentiation and recovery effects) or long-term memories (e.g., combining the potentiation and saturation effects). However, we will see that by adding MBON→DAN feedback connections a very wide range of circuit properties can be implemented. We next introduce a set of microcircuits that have been found in the fruit fly MBs and describe how they could interlock and interact in one IC to control the motivation and hence the behaviour of the animal.

### The incentive circuit

What we call the IC is a circuit in the MB of the fruit fly D. melanogaster that allows complicated memory dynamics through self-motivation. We have identified and modelled this circuit (shown in Figure 3) which consists of six MBONs that receive KC input and six DANs that modulate the KC-MBON connections. The circuit includes some MBON-MBON connections and some feedback connections from MBONs to DANs. All the neurons and connections in this circuit are mapped to identified connectivity in the MB as summarised in Table 1. We will describe each of the microcircuits and the biological justification for their assumed function in detail below, but here we provide an initial overview of the IC function.

![Figure 3.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig3-v1.jpg)

**Figure 3.:** It combines the susceptible, restrained, reciprocal short- and long-term memories and the memory assimilation mechanism microcircuits in one circuit that is able to form, consolidate, and forget different types of memories that motivate the animal to take actions. $d_{av}$ and $d_{at}$: avoidance- and attraction-driving discharging dopaminergic neurons (DANs); $c_{av}$ and $c_{at}$: avoidance- and attraction-driving charging DANs; $f_{av}$ and $f_{at}$: avoidance- and attraction-driving forgetting DANs; $s_{av}$ and $s_{at}$: avoidance- and attraction-driving susceptible mushroom body output neurons (MBONs); $r_{av}$ and $r_{at}$: avoidance- and attraction-driving restrained MBONs; $m_{av}$ and $m_{at}$: avoidance- and attraction-driving long-term memory MBONs.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Testing the performance of the incentive circuit in the experiments of Bennett et al., 2021, Figure 5, Bennett et al., 2021 collected behavioural data ($Δ⁢f$ measure) from 92 experiments, summarised in Figure 3—source data 1, and calculated their correlation coefficient to the behaviour produced by their model (VSλmodel: $r=0.68$, $p<10^{−4}$; MV model: $r=0.65$, $p<10^{−4}$). The behavioural data involve intervention (e.g., activation or silencing) in different mushroom body output neurons (MBONs) or dopaminergic neurons (DANs), which are grouped by colour codes. Here we use the same colour codes as in the original paper for convenience. For the details of this analysis, please refer to Bennett et al., 2021. We test the behaviour of the incentive circuit when using two different learning rules: (A) the dopaminergic plasticity rule (DPR) and (B) the reward prediction error (RPE). As we do not know what type the intervened MBON or DAN is, we test for all the types (and groups of them) and report the ones with the highest correlation under the ‘Best fit’ plot. We also try to guess the type by the identity of the neuron (or group of neurons) intervened and report the correlation coefficient under the ‘Selected neuron types’ plot. The types selected for each experiment can also be found in Figure 3—source data 1. (C) Examples of the genetic intervention as coloured in (A) and (B). We run 10 trials of odour A + shock or sugar (indicated with a thunder or cubes, respectively) or without reinforcement (absence of thunder and sugar cubes), followed by 10 trials of odour B without reinforcement (acquisition phase). Then we proceed with two trials of testing odour A vs. odour B (extinction phase). In addition, we model genetic intervention by targeting selected neurons of our model and silence them via the shibire blockage or excite them through the dTrpA1 channel (timing of the intervention is shown by the coloured lines). The colours of the lines correspond to the different examples of the coloured samples of (A) and (B).

**Table 1.**
 Connections among neurons in the Drosophila mushroom body mapped to the connections of the incentive circuit.Connection types: ‘⊸’, modulates the synaptic weights of the KC→MBON connections terminating in that MBON; ‘→’, excitatory connection; ‘⊣’, inhibitory connection. Microcircuit – SM: susceptible memory; RM: restrained memory; RSM: reciprocal short-term memories; LTM: long-term memory; RLM: reciprocal long-term memories; MAM: memory assimilation mechanism. Evidence – A: anatomical connection is known (i.e., using light or electron microscopy); F: functional connection is known (i.e., whether activating the presynaptic neuron leads to an excitatory or inhibitory effect on the postsynaptic neuron and/or the neurotransmitter released by the presynaptic neuron); KC: Kenyon cell; MBON: mushroom body output neuron; IC: incentive circuit.


<table>
  <thead>
    <tr>
      <th>Connection in the MB</th>
      <th>Connection in the IC</th>
      <th>Microcircuit</th>
      <th>Evidence</th>
      <th>References</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PPL1-γ1ped ⊸ MBON-γ1ped</td>
      <td>dav⊸sat</td>
      <td>SM</td>
      <td>A, F</td>
      <td>Aso et al., 2014a; Pavlowsky et al., 2018</td>
    </tr>
    <tr>
      <td>MBON-γ1ped ⊣ PPL1-γ1ped</td>
      <td>sat⊣dav</td>
      <td>SM</td>
      <td>A, F</td>
      <td>Aso et al., 2014a; Pavlowsky et al., 2018</td>
    </tr>
    <tr>
      <td>PAM-γ4&lt;γ1γ2 ⊸ MBON-γ4&gt;γ1γ2</td>
      <td>dat⊸sav</td>
      <td>SM</td>
      <td>A</td>
      <td>Aso et al., 2014a</td>
    </tr>
    <tr>
      <td>MBON-γ4&gt;γ1γ2 ⊣ PAM-γ4&lt;γ1γ2</td>
      <td>sav⊣dat</td>
      <td>SM</td>
      <td>A, F</td>
      <td>Aso et al., 2014a; Cohn et al., 2015</td>
    </tr>
    <tr>
      <td>MBON-γ1ped ⊣ MBON-γ5β′2a</td>
      <td>sat⊣rav</td>
      <td>RM</td>
      <td>A, F</td>
      <td>Aso et al., 2014a; Felsenberg et al., 2018</td>
    </tr>
    <tr>
      <td>MBON-γ4&gt;γ1γ2 ⊣ MBON-γ2α′1</td>
      <td>sav⊣rat</td>
      <td>RM</td>
      <td>A</td>
      <td>Aso et al., 2014a</td>
    </tr>
    <tr>
      <td>PPL1-γ2α’12 ⊸ MBON-γ2α′1</td>
      <td>cav⊸rat</td>
      <td>RSM</td>
      <td>A, F</td>
      <td>Aso et al., 2014a; McCurdy et al., 2021</td>
    </tr>
    <tr>
      <td>MBON-γ2α′1 → PAM-β′2a</td>
      <td>rat→cat</td>
      <td>RSM</td>
      <td>A, F</td>
      <td>Aso et al., 2014a; McCurdy et al., 2021</td>
    </tr>
    <tr>
      <td>PAM-β′2a ⊸ MBON-γ5β′2a</td>
      <td>cat⊸rav</td>
      <td>RSM</td>
      <td>A, F</td>
      <td>Aso et al., 2014a; McCurdy et al., 2021</td>
    </tr>
    <tr>
      <td>MBON-γ5β′2a → PPL1-γ2α’12</td>
      <td>rav→cav</td>
      <td>RSM</td>
      <td>A</td>
      <td>Li et al., 2020</td>
    </tr>
    <tr>
      <td>PPL1-γ2α’12 ⊸ MBON-α’1</td>
      <td>cav⊸mav</td>
      <td>LTM</td>
      <td>A</td>
      <td>Aso et al., 2014a</td>
    </tr>
    <tr>
      <td>MBON-α’1 → PPL1-γ2α’12</td>
      <td>mav→cav</td>
      <td>LTM</td>
      <td>A</td>
      <td>Aso et al., 2014a; Li et al., 2020</td>
    </tr>
    <tr>
      <td>PAM-β’2a ⊸ MBON-β2β′2a</td>
      <td>cat⊸mat</td>
      <td>LTM</td>
      <td>A</td>
      <td>Aso et al., 2014a</td>
    </tr>
    <tr>
      <td>MBON-β2β′2 a → PAM-β′2a</td>
      <td>mat→cat</td>
      <td>LTM</td>
      <td>A</td>
      <td>Aso et al., 2014a; Li et al., 2020</td>
    </tr>
    <tr>
      <td>PPL1-γ2α’11 ⊸ MBON-α’1</td>
      <td>fat⊸mav</td>
      <td>RLM</td>
      <td>A</td>
      <td>Aso et al., 2014a</td>
    </tr>
    <tr>
      <td>MBON-α’1 → PAM-β2β′2a</td>
      <td>mav→fav</td>
      <td>RLM</td>
      <td>A</td>
      <td>Li et al., 2020</td>
    </tr>
    <tr>
      <td>PAM-β2β′2a ⊸ MBON-β2β′2a</td>
      <td>fav⊸mat</td>
      <td>RLM</td>
      <td>A</td>
      <td>Aso et al., 2014a</td>
    </tr>
    <tr>
      <td>MBON-β2β′2a → PPL1-γ2α’11</td>
      <td>mat→fat</td>
      <td>RLM</td>
      <td>A</td>
      <td>Li et al., 2020</td>
    </tr>
    <tr>
      <td>PPL1-γ2α’11 ⊸ MBON-γ2α’1</td>
      <td>fat⊸rat</td>
      <td>MAM</td>
      <td>A</td>
      <td>Aso et al., 2014a</td>
    </tr>
    <tr>
      <td>PAM-β2β′2a ⊸ MBON-γ5β′2a</td>
      <td>fav⊸rav</td>
      <td>MAM</td>
      <td>A</td>
      <td>Aso et al., 2014a</td>
    </tr>
  </tbody>
</table>

As presented in Figure 3, for each motivation (attraction or avoidance), the IC has three types of MBON — susceptible, restrained, and LTM — and three types of DAN — discharging, charging, and forgetting. More specifically, working from the outer edges of the model, we have ‘discharging’ DANs that respond to punishment (left side) or reward (right side) and influence the ‘susceptible’ MBONs, which by default respond to all KC inputs (not shown). These in turn inhibit the responses of the ‘restrained’ MBONs of opposite valence. When the discharging DANs depress the response of the susceptible MBONs of opposite valence, they release the restrained MBONs of the same valence, and also decrease the inhibitory feedback to the discharging DANs from the susceptible MBONs. The restrained MBONs activate their respective ‘charging’ DANs, which start to potentiate the LTM MBONs of the same valence, while also depressing the response (to KC input) of the restrained MBON of opposite valence. Similarly, the LTM MBONs enhance the activity of the charging DANs, increasing the momentum of LTM, while simultaneously activating their respective ‘forgetting’ DANs, to decrease the momentum of the opposite valence LTM. The forgetting DANs also depress the restrained MBONs, which makes space for the acquisition of new memories while preserving old ones.

In the following sections, we show in detail how each simulated neuron of this circuit responds during acquisition and forgetting in the aversive olfactory conditioning paradigm shown in Figure 4 and compare this to observed responses in the corresponding identified neurons in the fly from calcium imaging under the same paradigm. We then describe the behaviour of simulated flies under the control of this circuit and learning rule in a naturalistic setting with two odour gradients, paired singly or jointly with punishment or reward. By using more abstracted behavioural modelling, following the approach of Bennett et al., 2021, we are also able to create closely matching results for 92 different olfactory conditioning intervention experiments, that is, the observed effects on fly learning of silencing or activating specific neurons (Figure 3—figure supplement 1, $Δ⁢f$ of the model and experiments are correlated with correlation coefficient $r=0.76,p=2.2\times10^{-18}$).

![Figure 4.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig4-v1.jpg)

**Figure 4.:** (A) Setup for visualising neural activity via Ca2+ imaging during aversive olfactory memory acquisition and reversal. Flies are head-fixed and cuticle dissected for ratiometric imaging of Ca2+-sensitive GCaMP6f and Ca2+-insensitive tdTomato. (B) The aversive olfactory conditioning experimental paradigm. 5 s presentations of odours A (3-octanol [OCT]; coloured pink) and B (4-methylcyclohexanol [MCH]; coloured yellow) continuously alternate, separated by fresh air, while the shock input (100 ms of 120 V) forms the different phases: one repeat of pre-training, where no shock is delivered; five repeats of acquisition, where shock (thin red line) is delivered in the last second of odour B; two repeats of reversal where shock is paired with odour A. (C) Abstract representation of the computational model as an electronic chip. The model receives the conditional (odour) and unconditional stimuli (electric shock) and produces the dopaminergic neuron (DAN) and mushroom body output neuron (MBON) responses using the incentive circuit and the dopaminergic plasticity rule. (D) The aversive olfactory conditioning experimental paradigm modified for testing the model. Odours A (coloured pink) and B (coloured yellow) are presented for two time-steps each, in alternation, separated by one time-step fresh air, while the shock input forms the different phases and forgetting conditions: one repeat of pre-training, where no shock is delivered; five repeats of acquisition, where shock is delivered in the second time-step of odour B; five repeats of forgetting that can be either extinction (lightest shade of odour colour) where shock is not presented, unpaired (mid shade of odour colour) where shock (thin red line) is paired with the fresh air ‘break’, or reversal (dark shade of odour colour) where shock is paired with odour A.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** In each row, we present the driver of the recorded neurons and a schematic representation of where they innervate the mushroom body; the median responses of the neuron for each odour (coloured as pink for odour A or yellow for odour B) over a number of flies, denoted as $n$, and the 25% and 75% quantiles marked by the coloured region.

### Microcircuits of the mushroom body

#### Susceptible and restrained memories

Pavlowsky et al., 2018 identified a microcircuit in the MB, where a punishment-encoding DAN (PPL1-γ1pedc) depresses the KC synapses onto an attraction-driving MBON (MBON-γ1pedc>α/β), which in turn inhibits the same DAN. They argue that this is a memory consolidation mechanism as the drop in the MBON response will reduce its inhibition of the DAN, enhancing the formation of the memory if the same odour-punishment pairing is continued. Felsenberg et al., 2018 further showed that the same MBON directly inhibits an avoidance-driving MBON (MBON-γ5β′2a), such that its activity increases (driving avoidance) after punishment as the inhibition is released. Figure 5A shows these neurons in the MB and Figure 5B a schematic representation of their interconnections. Note that the MBON⊣MBON inhibition is not reciprocal, rather we assume (see Figure 3 and below) that there is a different microcircuit in which an avoidance-driving MBON inhibits an attraction-driving MBON. Figure 5C–E shows the responses of these neurons from experimental data (left) and from our model (right) during aversive conditioning (the paradigm shown in Figure 4), which follow a similar pattern.

![Figure 5.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig5-v1.jpg)

**Figure 5.:** (A) Image of the attraction-driving susceptible and avoidance-driving restrained memory microcircuits made of the PPL1-γ1pedc, MBON-γ1pedc, and MBON-γ5β′2a neurons – created using the Virtual Fly Brain software (Milyaev et al., 2012). (B) Schematic representation of the susceptible and restrained memories microcircuits connected via the susceptible mushroom body output neuron (MBON). The responses of (C) the punishment-encoding discharging dopaminergic neuron (DAN), $d_{av}$, (D) the attraction-driving susceptible MBON, $s_{at}$, and (E) the avoidance-driving restrained MBON, $r_{av}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. For each trial, we report two consecutive time-steps: the off-shock (i.e., odour only) followed by the on-shock (i.e., paired odour and shock) when available (i.e., odour B in acquisition and odour A in reversal phase); otherwise, a second off-shock time-step (i.e., all the other phases).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** The susceptible and restrained microcircuits of the mushroom body. (A) Image of the avoidance-driving susceptible and attraction-driving restrained memory microcircuits made of the PAM-γ4γ1γ2 and MBON-γ2α′1 neurons – created using the Virtual Fly Brain software (Milyaev et al., 2012). (B) Schematic representation of the susceptible and restrained memories microcircuits connected via the susceptible mushroom body output neuron (MBON). The responses of (C) the reward-encoding discharging dopaminergic neuron (DAN), $d_{at}$, (D) the avoidance-driving susceptible MBON, $s_{av}$, and (E) the attraction-driving restrained MBON, $r_{at}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. For each trial, we report two consecutive time-steps: the off-shock (i.e., odour only) followed by the on-shock (i.e., paired odour and shock) when available (i.e., odour B in acquisition and odour A in reversal phase); otherwise, a second off-shock time-step (i.e., all the other phases).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** The responses of (A) the punishment-encoding discharging dopaminergic neuron (DAN), $d_{av}$, (B) the attraction-driving susceptible mushroom body output neuron (MBON), $s_{at}$, (C) the avoidance-driving restrained MBON, $r_{av}$, (D) the attraction-driving restrained MBON, $r_{at}$, (E) the avoidance-driving susceptible MBON, $s_{av}$, and (F) the reward-encoding discharging DAN, $d_{at}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. The first row of responses (coloured pink) corresponds to responses associated with odour A, and the second (coloured yellow) to those associated with odour B. For each trial, we report two consecutive time-steps: the off-shock (i.e., odour only) followed by the on-shock (i.e., paired odour and shock) when available (i.e., odour B in acquisition and odour A in reversal phase); otherwise, a second off-shock time-step (i.e., all the other phases).

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** The synaptic weights of (A) the attraction-driving susceptible mushroom body output neuron (MBON), $s_{at}$, (B) the avoidance-driving susceptible MBON, $s_{av}$, (C) the attraction-driving restrained MBON, $r_{at}$, and (D) the avoidance-driving restrained MBON, $r_{av}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. The first row of weights (coloured pink) corresponds to Kenyon cells (KCs) associated with odour A, the second (coloured yellow) to KCs associated with odour B, and the third (coloured orange) to KCs associated with both odours. For each trial, we report two consecutive time-steps: the off-shock (i.e., odour only) followed by the on-shock (i.e., paired odour and shock) when available (i.e., odour B in acquisition and odour A in reversal phase); otherwise, a second off-shock time-step (i.e., all the other phases).

Learning in this circuit is shown by the sharp drop (in both experimental data and model) of the response of MBON-γ1pedc>α/β (Figure 5D) to odour B already from the second trial of the acquisition phase. There is a similar drop in the response to odour A in the reversal phase. This rapid decrease is due to the depressing effect of the DAN on the KC→MBON synaptic weight. Note that we name this a ‘discharging’ DAN as the target synaptic strengths are high or ‘charged’ by default. However, due to our plasticity rule, if the unconditional stimuli (US) subsequently occurs without the CS (see unpaired phase in the model, for which we do not have experimental data), the MBON synaptic weights reset due to the recovery effect (see Figure 5—figure supplement 3A, odour B). This is consistent with the high learning rate and low retention time observed in Aso and Rubin, 2016, and it results in a memory that is easily created and erased: a ‘susceptible memory’ (SM). The response of MBON-γ5β′2a (Figure 5E) can be observed to have the opposite pattern, that is, it starts to respond to odour B from the second trial of acquisition as it is no longer ‘restrained’. Note, however, that the response it expresses, when the restraint is removed, also depends on its own synaptic weights for KC input, which, as we will see, may be affected by other elements in the IC. In Figure 5C, the experimental data shows a slight drop in the shock response (first paired with odour B, then with odour A) of the DAN, PPL1-γ1pedc, during the whole experiment, although it remains active throughout. We assume that this drop may reflect a sensory adaptation to shock but have not included it in our model. Consequently, the model data shows a positive feedback effect: the DAN causes depression of the MBON response to odour, reducing inhibition of the DAN, which increases its response, causing even further depression in the MBON. Note that this is opposite to the expected effects of reward prediction error.

Similar microcircuits in the MB can be extracted from the connectome described in Aso et al., 2014a and Li et al., 2020 (also identified in larvae; Eichler et al., 2017). This leads us to the assumption that there are exactly corresponding susceptible and restrained memory microcircuits with opposite valence, that is, a reward-encoding DAN that discharges the response to odour of an avoidance-driving MBON, which in turn releases its restraint on an attraction-driving MBON (see Figure 5—figure supplement 1B and right side of the IC in Figure 3, which mirrors the left side, with opposite valence). We further suggest specific identities for the neurons forming this circuit: PAM-γ4<γ1γ2 as the reward-encoding discharging DAN; MBON-γ4>γ1γ2 as the avoidance-driving susceptible MBON; and MBON-γ2α’1 as the attraction-driving restrained MBON (see Figure 5—figure supplement 1A). The latter identification is based on the possibility of inhibiting connections from MBONs in the γ4 compartment to the ones in the γ2 compartment suggested by Aso et al., 2019 and Cohn et al., 2015. Although MBON-γ4>γ1γ2 is characterised by the glutamate neurotransmitter, it is possible that it can inhibit MBON-γ2α′1 through glutamate-gated chloride channels (Cleland, 1996; Liu and Wilson, 2013; McCarthy et al., 2011).

#### Reciprocal short-term memories

McCurdy et al., 2021 suggest that the attraction-driving restrained MBON in the previous circuit (MBON-γ2α′1) indirectly decreases the synaptic weights from KCs to the avoidance-driving restrained MBON (MBON-γ5β′2a) via an attraction-encoding DAN (PAM-β′2a). This microcircuit is also supported by Felsenberg et al., 2018 and Berry et al., 2018. Cohn et al., 2015 and Li et al., 2020 suggest that the corresponding avoidance-driving restrained MBON (MBON-γ5β′2a) excites an avoidance-encoding DAN (PPL1-γ2α′1), which closes the loop by affecting the KC connections to the attraction-driving restrained MBON, forming what we call the ‘reciprocal short-term memories’ microcircuit as shown in Figure 6A (actual neurons in the MBs) and Figure 6B (schematic representation of the described connections).

![Figure 6.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig6-v1.jpg)

**Figure 6.:** (A) Image of the reciprocal short-term memories microcircuit made of the MBON-γ5β′2a, PAM-β′2a, PPL1-γ2α′1, and MBON-γ2α′1 neurons – created using the Virtual Fly Brain software (Milyaev et al., 2012). (B) Schematic representation of the reciprocal short-term memories microcircuit (coloured) connected to the susceptible memories via the restrained mushroom body output neurons (MBONs). The responses of (C) the punishment-encoding charging dopaminergic neuron (DAN), $c_{av}$, the (D) attraction-driving restrained MBON, $r_{at}$, and (E) the reward-encoding charging DAN, $c_{at}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. For each trial, we report two consecutive time-steps: the off-shock (i.e., odour only) followed by the on-shock (i.e., paired odour and shock) when available (i.e., odour B in acquisition and odour A in reversal phase); otherwise, a second off-shock time-step (i.e., all the other phases).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** The responses of (A) the punishment-encoding discharging dopaminergic neuron (DAN), $d_{av}$, (B) the attraction-driving susceptible mushroom body output neuron (MBON), $s_{at}$, (C) the avoidance-driving restrained MBON, $r_{av}$, (D) the reward-encoding charging DAN, $c_{at}$, (E) the reward-encoding discharging DAN, $d_{at}$, (F) the avoidance-driving susceptible MBON, $s_{av}$, (G) the attraction-driving restrained MBON, $r_{at}$, and (H) the punishment-encoding charging DAN, $c_{av}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. The first row of responses (coloured pink) corresponds to responses associated with odour A, and the second (coloured yellow) to those associated with odour B. For each trial, we report two consecutive time-steps: the off-shock (i.e., odour only) followed by the on-shock (i.e., paired odour and shock) when available (i.e., odour B in acquisition and odour A in reversal phase); otherwise, a second off-shock time-step (i.e., all the other phases).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** The synaptic weights of (A) the attraction-driving susceptible mushroom body output neuron (MBON), $s_{at}$, (B) the avoidance-driving susceptible MBON, $s_{av}$, (C) the attraction-driving restrained MBON, $r_{at}$, and (D) the avoidance-driving restrained MBON, $r_{av}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. The first row of weights (coloured pink) corresponds to Kenyon cells (KCs) associated with odour A, the second (coloured yellow) to KCs associated with odour B, and the third (coloured orange) to KCs associated with both odours. For each trial, we report two consecutive time-steps: the off-shock (i.e., odour only) followed by the on-shock (i.e., paired odour and shock) when available (i.e., odour B in acquisition and odour A in reversal phase); otherwise, a second off-shock time-step (i.e., all the other phases).

The ‘charging’ DANs, PAM-β′2a and PPL1-γ2α′1 (named after their long-term memory charging property, i.e., potentiation effect on another KC→MBON synapse, as we describe in the long-term memory microcircuit section), should be activated directly by reinforcement as well as the restrained MBONs. This allows for memories to be affected directly by the reinforcement, but also by the expression of the opposite valence memories. The latter feature keeps the balance between the memories by automatically erasing a memory when a memory of the opposite valence starts building up and results in the balanced learning rate and retention time as observed in Aso and Rubin, 2016. Because the memories in this pair of restrained MBONs are very fragile, we predict that these MBONs store short-term memories.

The effects of this circuit, as shown in Figure 6C–E, are relatively subtle. During acquisition, the shock activates the punishment-encoding charging DAN (see Figure 6C), which decreases the synaptic weights of the KC onto the attraction-driving restrained MBON (see Figure 6—figure supplement 2C), but this cannot be seen in Figure 6D because this MBON is already strongly inhibited (i.e., by the avoidance-driving susceptible MBON). This low response means that the opposing reward-encoding charging DAN Figure 6E is largely unaffected for this conditioning paradigm. In our model, the non-zero activity level of this DAN is a consequence of input from the LTM microcircuit which we describe next and the activation is similar for both odours because our network starts in a balanced state (no preference for either odour). The different response to the two odours seen in the experimental data might therefore represent an unbalanced starting state of its LTM for these odours due to previous experiences of the fly.

#### Long-term memory

Ichinose et al., 2015 describe a microcircuit where a reward-encoding DAN (PAM-α1) potentiates the KC→MBON synapses of MBON-α1, and MBON-α1 in turn excites PAM-α1. Using data from Li et al., 2020, we find numerous similar microcircuits, and in particular, MBONs that appear to have this recurrent arrangement of connectivity to the ‘charging’ DANs we have introduced to the circuit in the previous section. Specifically, we assume that the reward-encoding charging DAN (PAM-β′2a) can potentiate the response of the attraction-driving MBON-β2β′2a; and similarly the punishment-encoding charging DAN (PPL1-γ2α′1) potentiates the avoidance-driving MBON-α′1 (see Figure 7A and B; Figure 7C shows these connections schematically, with the KCs omitted for convenience). Crucially, these connections form positive feedback circuits — the DAN potentiates the response of the MBON to the odour, which increases its excitation of the DAN. As a consequence, even when the reinforcement ceases, the learning momentum can continue — this is the saturation effect of the learning rule (see Figure 2D) and results in long-term memory consolidation and enhancement.

![Figure 7.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig7-v1.jpg)

**Figure 7.:** (A) Image of the avoidance-encoding long-term memory microcircuit made of the MBON-α′1 and PPL1-γ2α′1 – created using the Virtual Fly Brain software (Milyaev et al., 2012). (B) Schematic representation of the long-term memory microcircuits (coloured) connected to the reciprocal short-term memory (RSM) via the charging dopaminergic neurons (DANs). (C) Image of the attraction-encoding long-term memory microcircuit made of the MBON-β2β′2a and PAM-β2a – created using the Virtual Fly Brain software (Milyaev et al., 2012). The responses of the (D) avoidance-driving long-term memory mushroom body output neuron (MBON), $m_{av}$, and (E) the attraction-driving long-term memory MBON, $m_{at}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. For each trial, we report two consecutive time-steps: the off-shock (i.e., odour only) followed by the on-shock (i.e., paired odour and shock) when available (i.e., odour B in acquisition and odour A in reversal phase); otherwise, a second off-shock time-step (i.e., all the other phases).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** The responses of (A) the punishment-encoding discharging dopaminergic neuron (DAN), $d_{av}$, (B) the attraction-driving susceptible mushroom body output neuron (MBON), $s_{at}$, (C) the avoidance-driving restrained MBON, $r_{av}$, (D) the reward-encoding charging DAN, $c_{at}$, (E) the attraction-driving LTM MBON, $m_{at}$, (F) the reward-encoding discharging DAN, $d_{at}$, (G) the avoidance-driving susceptible MBON, $s_{av}$, (H) the attraction-driving restrained MBON, $r_{at}$, (I) the punishment-encoding charging DAN, $c_{av}$, and (J) the avoidance-driving LTM MBON, $m_{av}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. The first row of responses (coloured pink) corresponds to responses associated with odour A, and the second (coloured yellow) to those associated with odour B. For each trial, we report two consecutive time-steps: the off-shock (i.e., odour only) followed by the on-shock (i.e., paired odour and shock) when available (i.e., odour B in acquisition and odour A in reversal phase); otherwise, a second off-shock time-step (i.e., all the other phases).

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig7-figsupp2-v1.jpg)

**Figure 7—figure supplement 2.:** The synaptic weights of (A) the attraction-driving susceptible mushroom body output neuron (MBON), $s_{at}$, (B) the avoidance-driving susceptible MBON, $s_{av}$, (C) the attraction-driving restrained MBON, $r_{at}$, (D) the avoidance-driving restrained MBON, $r_{av}$, (E) the attraction-driving LTM MBON, $m_{at}$, and (F) the avoidance-driving LTM MBON, $m_{av}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. The first row of weights (coloured pink) corresponds to Kenyon cells (KCs) associated with odour A, the second (coloured yellow) to KCs associated with odour B, and the third (coloured orange) to KCs associated with both odours. For each trial, we report two consecutive time-steps: the off-shock (i.e., odour only) followed by the on-shock (i.e., paired odour and shock) when available (i.e., odour B in acquisition and odour A in reversal phase); otherwise, a second off-shock time-step (i.e., all the other phases).

Figure 7D (right) demonstrates the charging of the avoidance-driving LTM MBON during the acquisition (for odour B) and its continued increase during the forgetting phases. However, these trends are not evident in the experimental data as illustrated in Figure 7D (left). We suggest this is because responses of LTM neurons depend on the overall experience of the animal and are thus hard to predict during one experiment. For example, it could be the case that the animal has already built some long-term avoidance memory for odour A, such that its presentation without reinforcement in our experiment continues its learning momentum, leading to the observed increasing response. Note that the decreasing response to odour A during acquisition in the model, as well as the observed effects in Figure 7E for the attraction-driving LTM MBON, is due to influence from additional microcircuits to be described in the next section. Figure 7—figure supplement 1 shows the responses of these neurons using only the microcircuits that have been introduced so far. In this case, the responses of both LTM MBONs saturate instantly, which shows that another mechanism must exist and regulate them in order for them to become useful for the behaviour of the animal.

#### Reciprocal long-term memories

As described so far, once the LTM microcircuit begins to charge, it will have a self-sustaining increase in the weights during odour delivery, preventing any subsequent adaptation to altered reward contingencies. To allow these weights to decrease, specifically, to decrease in response to charging of the LTM of opposite valence, we connect the two LTM MBONs via respective ‘forgetting’ DANs (see Figure 8B). Note that these forgetting DANs do not receive any direct reinforcement signals. Instead, as long as an LTM MBON is active, its respective forgetting DAN is also active and causes synaptic depression for the opposite LTM MBON (forgetting the learnt memory; see Figure 8C and D). This counteracts any potentiation effect due to the LTM MBON’s respective charging DAN (see Figure 8—figure supplement 1E and F). As a consequence, sustained reinforcement of one valence can gradually overcome the positive feedback of the LTM circuit of opposite valence, causing the charging momentum to drop and eventually negate. The LTMs are thus in long-term competition.

![Figure 8.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig8-v1.jpg)

**Figure 8.:** (A) Image of the reciprocal long-term memory microcircuit in the mushroom body made of the MBON-α′1, PAM-β2β′2a, MBON-β2β′2a, and PPL1-γ2α′1 – created using the Virtual Fly Brain software (Milyaev et al., 2012). (B) Schematic representation of the reciprocal long-term memories microcircuit (coloured). The responses of (C) the punishment-encoding forgetting dopaminergic neuron (DAN), $f_{av}$, the (D) reward-encoding forgetting DAN, $f_{at}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. For each trial, we report two consecutive time-steps: the off-shock (i.e., odour only) followed by the on-shock (i.e., paired odour and shock) when available (i.e., odour B in acquisition and odour A in reversal phase); otherwise, a second off-shock time-step (i.e., all the other phases).

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** The responses of (A) the punishment-encoding discharging dopaminergic neuron (DAN), $d_{av}$, (B) the attraction-driving susceptible mushroom body output neuron (MBON), $s_{at}$, (C) the avoidance-driving restrained MBON, $r_{av}$, (D) the reward-encoding charging DAN, $c_{at}$, (E) the attraction-driving LTM MBON, $m_{at}$, (F) the avoidance-driving forgetting DAN, $f_{av}$, (G) the reward-encoding discharging DAN, $d_{at}$, (H) the avoidance-driving susceptible MBON, $s_{av}$, (I) the attraction-driving restrained MBON, $r_{at}$, (J) the punishment-encoding charging DAN, $c_{av}$, (K) the avoidance-driving LTM MBON, $m_{av}$, and (L) the attraction-driving forgetting DAN, $f_{at}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. The first row of responses (coloured pink) corresponds to responses associated with odour A, and the second (coloured yellow) to those associated with odour B. For each trial, we report two consecutive time-steps: the off-shock (i.e., odour only) followed by the on-shock (i.e., paired odour and shock) when available (i.e., odour B in acquisition and odour A in reversal phase); otherwise, a second off-shock time-step (i.e., all the other phases).

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig8-figsupp2-v1.jpg)

**Figure 8—figure supplement 2.:** The synaptic weights of (A) the attraction-driving susceptible mushroom body output neuron (MBON), sat, (B) the avoidance-driving susceptible MBON, sav, (C) the attraction-driving restrained MBON, rat, (D) the avoidance-driving restrained MBON, sav, (E) the attraction-driving LTM MBON, mat, and (F) the avoidance-driving LTM MBON, mav, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. The first row of weights (coloured pink) corresponds to Kenyon cells (KCs) associated with odour A, the second (coloured yellow) to KCs associated with odour B, and the third (coloured orange) to KCs associated with both odours. For each trial, we report two consecutive time-steps: the off-shock (i.e., odour only) followed by the on-shock (i.e., paired odour and shock) when available (i.e., odour B in acquisition and odour A in reversal phase); otherwise, a second off-shock time-step (i.e., all the other phases).

We have identified the reciprocal LTMs microcircuit of Figure 8B in the descriptions of Aso et al., 2014a and Li et al., 2020, where MBON-α′1 is the avoidance-driving LTM MBON, MBON-β2β′2a is the attraction-driving LTM MBON, PAM-β2β′2a is the avoidance-driving forgetting DAN, and PPL1-γ2α′1 is the attraction-driving forgetting DAN, as shown in Figure 8A. One problem with this identification is that there is only one PPL1-γ2α′1 per hemisphere, and we have already suggested that it should be identified as the punishment-encoding charging DAN in our model. However, there are multiple axon terminals of this neuron in the MB (e.g., MB296B1 and MB296B2) and each one of them seems to communicate a different response (see Figure 4—figure supplement 1, row 5, columns 6 and 7). Interestingly, the responses communicated by the MB296B1 terminal are close to the ones produced by the punishment-encoding charging DAN (see Figure 6C), and the ones of the MB296B2 are close to the ones produced by the attraction-driving forgetting DAN (see Figure 8D). This implies that different axons of the same DA neuron might create responses that depend on where the axon terminates and actually work as separate processing units. Figure 8C and D shows that the reconstructed responses of these neurons from our model are surprisingly similar to the ones observed in the data.

#### Memory assimilation mechanism

The forgetting DANs allow the developing LTM of one valence to induce forgetting of the LTM of the opposite valence. However, the forgetting DANs can also be used for another critical function to maintain flexibility for future learning, which is to erase the memory of the same valence from their respective restrained MBONs. We thus predict that the forgetting DANs also suppress the KC synaptic weights of their respective restrained MBONs, forming the ‘memory assimilation mechanism’ (MAM) microcircuit (see Figure 9C). This effectively allows memory transfer between the restrained and the LTM MBONs, enhancing both the adaptability and the capacity of the circuit. This effect can be observed in the difference of the responses of the same neurons in Figures 7 and 8 and Figure 8—figure supplement 1, where the restrained memory becomes weaker as the LTM becomes stronger, driven by the respective forgetting and charging DANs.

![Figure 9.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig9-v1.jpg)

**Figure 9.:** (A) Image of the avoidance-specific MAM microcircuit in the mushroom body made of the MBON-γ5β′2a, PPL1-γ2α′1, MBON-α′1, and PAM-β2β′2a – created using the Virtual Fly Brain software (Milyaev et al., 2012). (B) Image of the attraction-specific MAM microcircuit in the mushroom body made of the MBON-γ2α’1, PAM-β’2a, MBON-β2β′2a, and PPL1-γ2α’1 – created using the Virtual Fly Brain software (Milyaev et al., 2012). (B) Schematic representation of the MAM microcircuits (coloured). The forgetting dopaminergic neurons (DANs) connect to the restrained mushroom body output neurons (MBONs) of the same valence, hence increasing long-term memory (LTM) strength reduces (assimilates) the restrained memory, constituting the MAM microcircuits.

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig9-figsupp1-v1.jpg)

**Figure 9—figure supplement 1.:** The synaptic weights of (A) the attraction-driving susceptible mushroom body output neuron (MBON), $s_{at}$, (B) the avoidance-driving susceptible MBON, $s_{av}$, (C) the attraction-driving restrained MBON, $r_{at}$, (D) the avoidance-driving restrained MBON, $r_{av}$, (E) the attraction-driving long-term memory MBON, $m_{at}$, and (F) the avoidance-driving long-term memory MBON, $m_{av}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. The first row of weights (coloured pink) corresponds to Kenyon cells (KCs) associated with odour A, the second (coloured yellow) to KCs associated with odour B, and the third (coloured orange) to KCs associated with both odours.

![Figure 9—figure supplement 2.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig9-figsupp2-v1.jpg)

**Figure 9—figure supplement 2.:** The reconstructed responses of (A) the punishment-encoding discharging dopaminergic neuron (DAN), $d_{av}$, (B) the attraction-driving susceptible MBON, $s_{at}$, (C) the avoidance-driving restrained mushroom body output neuron (MBON), $r_{av}$, (D) the reward-encoding charging DAN, $c_{at}$, (E) the attraction-driving long-term memory MBON, $m_{at}$, (F) the punishment-encoding forgetting DAN, $f_{av}$, (G) the reward-encoding discharging DAN, $d_{at}$, (H) the avoidance-driving susceptible MBON, $s_{av}$, (I) the attraction-driving restrained MBON, $r_{at}$, (J) the punishment-encoding charging DAN, $c_{av}$, (K) the avoidance-driving long-term memory MBON, $m_{av}$, and (L) the reward-encoding forgetting DAN, $f_{at}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase.

![Figure 9—figure supplement 3.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig9-figsupp3-v1.jpg)

**Figure 9—figure supplement 3.:** The synaptic weights of (A) the attraction-driving susceptible mushroom body output neuron (MBON), $s_{at}$, (B) the avoidance-driving susceptible MBON, $s_{av}$, (C) the attraction-driving restrained MBON, $r_{at}$, (D) the avoidance-driving restrained MBON, $r_{av}$, (E) the attraction-driving long-term memory MBON, $m_{at}$, and (F) the avoidance-driving long-term memory MBON, $m_{av}$, generated by experimental data (left) and the model (right) during the olfactory conditioning paradigms of Figure 4D. Lightest shades denote the extinction, mid shades the unpaired, and dark shades the reversal phase. The first row of weights (coloured pink) corresponds to Kenyon cells (KCs) associated with odour A, the second (coloured yellow) to KCs associated with odour B, and the third (coloured orange) to KCs associated with both odours.

The depression effect of the forgetting DANs on the KC→restrained MBON synapses of the same valence is supported by Aso et al., 2014a. More specifically, the avoidance-driving forgetting DAN we have identified as PAM-β2β′2a modulates the KC→MBON-γ5β′2a synapses, while for the attraction-driving forgetting DAN, PPL1-γ2α′1, modulates the KC→MBON-γ2α′1 synapses, as show in Figure 9A and B, respectively.

### Modelling the behaviour

In the IC, three MBON types drive attraction and three avoidance. This results in six driving forces, for each available odour (see Figure 10). A simple ‘behavioural’ readout (used in many previous models) would be to take the sum of all attractive and aversive forces at some time point as a measure of the probability of animals ‘choosing’ odour A or B, and compare this to the standard two-arm maze choice assay used in many Drosophila studies. Following this approach and using the summarised data collected by Bennett et al., 2021, we have tested the performance of our model in 92 olfactory classical conditioning intervention experiments from 14 studies (Felsenberg et al., 2017; Perisse et al., 2016; Aso and Rubin, 2016; Yamagata et al., 2016; Ichinose et al., 2015; Huetteroth et al., 2015; Owald et al., 2015; Aso et al., 2014b; Lin et al., 2014; Plaçais et al., 2013; Burke et al., 2012; Liu et al., 2012; Aso et al., 2010; Claridge-Chang et al., 2009), that is, the observed effects on fly learning of silencing or activating specific neurons, including positive and negative reinforcements. The $Δ⁢f$ predicted from the IC correlated with the ones reported from the actual experiments with correlation coefficient $r=0.76$, $p=2.2\times10^{-18}$ (Figure 3—figure supplement 1).

![Figure 10.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig10-v1.jpg)

**Figure 10.:** For naive flies, the forces are balanced. When electric shock is paired with an odour, the balance changes towards the avoidance-driving MBONs, which drives the fly directly away from that odour. When sugar is paired with an odour, the balance changes to attraction, driving the fly towards that odour. Combining all attractive and repulsive forces for each odour source currently experienced by the fly produces an overall driving force, $v$, which determines the fly’s behaviour.

However, classical conditioning does not allow us to explore the full dynamics of the circuit as animals simultaneously explore, learn, express learning, and forget, while moving through a world with odours. Therefore, we further simulate the behaviour produced by the IC with simulated flies placed in a virtual arena, where they are exposed to two odour gradients, of different strengths, and variously paired with reinforcements. As we have full access to the neural responses, the synaptic weights, and the position of the simulated flies for every time-step, this allows us to identify different aspects of the produced behaviour and motivation, including the effect of the LTM on the behaviour and whether ‘choice’ occurs because the animal is attracted by one odour or repulsed by the other. We can then derive a behavioural preference index (PI) based on the time the simulated flies spent exposed in each odour during relevant time periods. Figure 11 summarises our experimental set-up and results, while details about how we generate the presented behaviours are given in the methods section ‘Modelling the behaviour’.

![Figure 11.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig11-v1.jpg)

**Figure 11.:** The $n=100$ simulated flies are exposed to a mixture of two odours, whose relative intensity depends on the position of the simulated flies in space. (A) Each experiment lasts for $100s$ where: the flies are placed at the centre of the arena in time-step $t=−20s$. During the first $20s$ (pre-training phase, $t\in[−20,0]$), the flies explore the arena without any reinforcement (blue tracks). In the next $30s$ (training phase, $t\in[0,30]$), they conditionally receive reinforcement under one of the six training cases shown on the right: using sugar (green) or shock (red); and reinforcing around odour A (shock + odour A), odour B (shock + odour B), or both odours (shock + odour A/B). During the last $50s$ (post-training phase $t\in[30,80]$), they continue being exposed to the odours without receiving a reinforcement (black tracks). We repeat this experiment (including all its phases) 10 times in order to show the effects of the long-term memory in the behaviour. (B) Behavioural summary of a subset of simulated flies that visited both odours at any time during the 10 repeats. Columns show the different conditions and the population that was recorded visiting both odours. Top row: the normalised cumulative time spent exposed in odour A (pink lines) or odour B (yellow lines; note that this line is reversed). For each repeat, we present three values (average over all the pre-training, training, and post-training time-steps, respectively) where the values associated with the training phase are marked with red or green dots when punishment or reward has been delivered to that odour, respectively. Thin lines show three representative samples of individual flies. Thick lines show the median over the simulated flies that visited both odours. Bottom row: the preference index (PI) to each odour extracted by the above cumulative times.

![Figure 11—figure supplement 1.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig11-figsupp1-v1.jpg)

**Figure 11—figure supplement 1.:** Different rows correspond to KC→MBON weights associated with a different type of MBON, from top to bottom: attraction- and avoidance-driving susceptible, restrained and long-term memory MBONs. Pink and yellow lines show synaptic weights associated with odours A and B, respectively, dashed lines show weights associated with both odours. Thin lines show three representative examples of synaptic weights in single simulated flies. Thick lines show the median of the synaptic weight over all the simulated flies that visited both odours. KC: Kenyon cells; MBON: mushroom body output neuron.

![Figure 11—figure supplement 2.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig11-figsupp2-v1.jpg)

**Figure 11—figure supplement 2.:** (A) At least one of the two odours, (B) odour A, (C) odour B, (D) only odour A, and (E) only odour B. In each panel, columns show the different conditions and the population for each group. Top row: the normalised cumulative time spent exposed in odour A (pink lines) or odour B (yellow lines; note that this line is reversed). For each repeat, we present three values (average over all the pre-training, training, and post-training time-steps, respectively) where the values associated with the training phase are marked with red or green dots when punishment or reward has been delivered to that odour, respectively. Thin lines show three representative samples of individual flies. Thick lines show the median over the simulated flies that visited both odours. Bottom row: the preference index (PI) to each odour extracted by the above cumulative times.

![Figure 11—figure supplement 3.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig11-figsupp3-v1.jpg)

**Figure 11—figure supplement 3.:** Behavioural summary of simulated flies when controlled by (A) the susceptible, (B) restrained, or (C) long-term memory (LTM) MBONs separately. In each panel, columns show the different conditions and the population for each group. Top row: the normalised cumulative time spent exposed in odour A (pink lines) or odour B (yellow lines; note that this line is reversed). For each repeat, we present three values (average over all the pre-training, training, and post-training time-steps, respectively) where the values associated with the training phase are marked with red or green dots when punishment or reward has been delivered to that odour, respectively. Thin lines show three representative samples of individual flies. Thick lines show the median over the simulated flies that visited both odours. Bottom row: the preference index (PI) to each odour extracted by the above cumulative times.

![Figure 11—figure supplement 4.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig11-figsupp4-v1.jpg)

**Figure 11—figure supplement 4.:** Blue segments show the paths of the flies during the pre-training, red and green segments show the paths during the training phase for punishment and reward conditions, respectively, and black segments show the paths during the post-training phase. Rows are for the different repeats and columns for the different conditions.

![Figure 11—figure supplement 5.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig11-figsupp5-v1.jpg)

**Figure 11—figure supplement 5.:** Columns show the different conditions and the population that was recorded visiting both odours. Top row: the normalised cumulative time spent exposed in odour A (pink lines) or odour B (yellow lines; note that this line is reversed). For each repeat, we present three values (average over all the pre-training, training, and post-training time-steps, respectively) where the values associated with the training phase are marked with red or green dots when punishment or reward has been delivered to that odour, respectively. Thin lines show three representative samples of individual flies. Thick lines show the median over the simulated flies that visited both odours. Bottom row: the preference index (PI) to each odour extracted by the above cumulative times.

![Figure 11—figure supplement 6.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig11-figsupp6-v1.jpg)

**Figure 11—figure supplement 6.:** Blue segments show the paths of the flies during the pre-training, red and green segments show the paths during the training phase for punishment and reward conditions, respectively, and black segments show the paths during the post-training phase. Rows are for the different repeats and columns for the different conditions.

![Figure 11—figure supplement 7.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig11-figsupp7-v1.jpg)

**Figure 11—figure supplement 7.:** Different rows correspond to KC→MBON weights associated with a different type of MBON, from top to bottom: attraction- and avoidance-driving susceptible, restrained and long-term memory MBONs. Pink and yellow lines show synaptic weights associated with odours A and B, respectively, dashed lines show weights associated with both odours. Thin lines show three representative examples of synaptic weights in single simulated flies. Thick lines show the median of the synaptic weight over all the simulated flies that visited both odours. KC: Kenyon cell; MBON: mushroom body output neuron.

In Figure 11—figure supplement 4, we can see that most simulated flies do not visit any of the regions that an odour can be detected in the first repeats, and therefore, in Figure 11B, we start seeing an effect in the averaged statistics after the second repeat of the experiment. However, in the first couple of repeats, the individual paths already show a small tendency to the expected behaviour of the flies: avoid the punished region and approach the rewarded one. Due to the unpredictable behaviour of the individual flies, in Figure 11B we summarise only times from simulated flies that have visited both odours for at least 1 s. In later repeats of the experiment, the PI shows that (on average) flies prefer the non-punished and rewarded odours. When both of them are punished or rewarded, they equally prefer none or both, respectively. Note that the above result does not mean that each fly spends equal time in both odours, but that most probably some flies choose to spend more time with the one and some with the other (as shown from the individual cumulative durations in Figure 11B), but their population is equal. It is interesting that almost in every repeat the flies are neutral about the odours during pre-training (time-step before the reinforced one – marked with red or green), showing a relatively small effect during training and a bigger effect during post-training. This might be because in every repeat of the experiment they are initialised in the centre, so they spend some time randomly exploring before they detect an odour.

By looking at the PIs of Figure 11B, we see a strong effect when electric shock is paired with odour A or B, but not very strong otherwise. We also see a smaller PI for flies experiencing sugar than the ones that experience electric shock, which is in line with experimental data (Krashes and Waddell, 2011). When shock is paired with both odours, we expect that the simulated flies will try to minimise the time spent exposed to any of them, which is precisely what we see in the coloured lines. In contrast, simulated flies seem to increase the time spent in both odours when paired with sugar with a slight preference towards the reinforced odour. In general, our results show that (in time) the simulated flies seem to develop some prior knowledge about both odours when experiencing at least one of them with reinforcement (see Figure 11B and Figure 11—figure supplement 2A), which we suggest is because of their overlapping KCs associated with both odours. We believe that this leads to self-reinforcement, which means that when the animal experiences the non-reinforced odour it will automatically associate the reinforcement associated with the overlapping KCs to all the KCs associated with this odour, which is effectively a form of second-order conditioning.

From the summarised synaptic weights shown in Figure 11—figure supplement 1, we can see that the susceptible MBONs immediately block the simulated flies from approaching the punishing odours, while they allow them to approach the rewarding ones, which results in the smaller PI shown in sugar-related experiments compared to the shock-related ones, as discussed before. This is partially because of the lack of reciprocal connections between the opposing susceptible MBONs, and it can be verified through the appetitive conditioning, where the synaptic weights seem to change as the simulated flies now prefer the reinforced odour site. Susceptible MBONs convulsively break the balance between attraction and avoidance created by the restrained and LTM MBONs, also affecting their responses, and allowing STM and as a result LTM formation even without the presence of reinforcement. Figure 11—figure supplement 1 also shows that the restrained MBONs seem to play an important role during the first repeats (up to five), but then they seem to reduce their influence giving up the control to the LTM MBONs, which seem to increase their influence with time. This is partially an effect of the MAM microcircuit, which verifies its function and the role of the restrained MBONs as storing STMs. Figure 11—figure supplement 3 shows that the different types of MBONs alone are also capable of controlling the behaviour. However, they seem to better work when combined as they complement one another in different stages, for example, during early or late repeats and crucial times.

### Dopaminergic plasticity rule vs. reward prediction error

We have already shown that our novel dopaminergic plasticity rule and the connectome of the incentive circuit build a powerful model for memory dynamics and behavioural control. In order to verify the importance of our DPR in the model, we run the same experiments by replacing it with the reward prediction error plasticity rule (Rescorla and Wagner, 1972).

The idea behind RPE is that the fly learns to predict how rewarding or punishing a stimulus is by altering its prediction when this does not match the actual reward or punishment experienced (Zhao et al., 2021). This can be adapted to the mushroom body circuit by assuming for a given stimulus represented by KC activation, the MBON output is the prediction, and the KC→MBON synaptic weights should be altered (for the active KC) proportionally to the difference between the MBON output and the actual reinforcement signalled by the DAN. In Equation 30, we show how our DPR can be replaced with the RPE (as described above) in our model. Note that this rule allows updates to happen only when the involved KC is active, implying synaptic plasticity even without DAN activation but not without KC activation, which is in contrast with our DPR and recent findings (Berry et al., 2018; Hige et al., 2015) (also in larva; Schleyer et al., 2018; Schleyer et al., 2020).

This effect, that is, learning when the KC is active even without DAN activation, is visible in Figure 9—figure supplement 2 and Figure 9—figure supplement 3, where we can see that, for the susceptible MBONs, the synaptic weights recover every time before the shock delivery, when the odour is presented alone, resulting in no meaningful learning and cancelling their susceptible property. Restrained MBONs look less affected (at least in this experimental set-up), while the LTM MBONs lose their charging momentum obtained by the saturation effect, resulting in more fragile memories. Furthermore, due to the KC (instead of dopamine) gating of this plasticity rule, the responses during the unpaired and extinction conditions look identical in all neurons, while the reversal makes a difference only on the responses to odour A. In general, the responses reproduced using the RPE plasticity rule have none of the properties of our model that have been shown earlier and also they cannot explain the dynamics of the responses recorded from animals.

In contrast to the responses, the behaviour of the simulated flies (as shown in Figure 11—figure supplement 5 and Figure 11—figure supplement 6) is less affected by the plasticity rule: we still see a preference to the non-punished or rewarded odours. However, there are some details in the behaviour that are different and some properties of the model that need to be mentioned. First, we see that the simulated flies now spend more time in the punished odours (compared to the non-punished ones), which might look like adaptation (in PI level), but it is actually forgetting about the odour. Figure 11—figure supplement 7 shows that synaptic weights targeting the restrained and LTM MBONs are dramatically depressed during the first three repeats and are unable to recover whatsoever, which means that this part of the circuit is knocked out by then. Hence, the behaviour is controlled solely by the susceptible MBONs, which now look more like LTM MBONs that are not reciprocally connected. Furthermore, the synaptic weights associating the odours to both motivations seem to constantly decrease, which makes us believe that both susceptible MBONs will have the same future as the restrained and LTM ones, but it will just take longer. Therefore, we see that although the RPE predicts a reasonable behaviour for inexperienced (or minor experienced) simulated flies, it could gradually result in a meaningless behaviour for experienced flies.

## Discussion

We have shown that the combination of our novel dopaminergic plasticity rule (DPR) with the incentive circuit (IC) of the mushroom body is able to generate similar neural responses and behaviours to flies in associative learning and forgetting paradigms. Regarding our model, we provide evidence for the existence of all hypothesised connections and suggest that at least three types of MB output (susceptible, restrained, and LTM) and three types of DA neurons (discharging, charging, and forgetting) exist in the fruit fly brain, discriminated by their functionality. As we show, this forms a unified system for rapid memory acquisition and transfer from STM to LTM, which could underlie the ability to make exploration/exploitation trade-offs. Box 1 summarises a number of prediction yielded by this computational modelling study.

### Advantages of the dopaminergic plasticity rule

The proposed DPR, while remaining very simple, allows the animal to express a variety of behaviours depending on their experience. The rule remains local to the synapse, that is, it depends only on information that is plausibly available in the presynaptic area of the KC axon (Equation 1): the activity of the KC, the level of DA, and the deviation of the current ‘weight’ from a set-point ‘resting weight’. We note that it was not possible to obtain good results without this third component to the rule, although the underlying biophysical mechanism is unknown; we speculate that it could involve synapsin as it has a direct role in regulating the balance of reserve and release vesicle pools, and is required in the MB for associative learning (Michels et al., 2011). The rule also introduces a bidirectional ‘dopaminergic factor’ based on the results of Handler et al., 2019, who showed the combination of DopR1 and DopR2 receptor activity can result in depression or potentiation of the synapse. In our plasticity rule, a positive or negative dopaminergic factor combined with active or inactive KCs leads to four possible effects on the synapse: depression, potentiation, recovery, and saturation. This allows substantial flexibility in the dynamics of learning in different MB compartments.

In particular, the saturation allows LTM MBONs to consolidate their memories and makes it very hard to forget. This only occurs for consistently experienced associations, which then become strongly embedded. Only a persistent change in the valence of reinforcement experienced with a given stimuli can reset the activity of LTM MBONs through the reciprocal LTMs microcircuit, which equips the circuit with flexibility even in the LTMs. Further, the fact that the DPR allows STMs (restrained) and LTMs to interact through the memory assimilation mechanism (MAM) increases the capacity of the circuit. Whatever the restrained MBONs learn is eventually assimilated by the LTM MBONs, opening up space for the formation of new memories in the restrained MBONs. When combined with sparse coding of odours in a large number of KCs, the LTM MBONs can store multiple memories for different odours. Short-term experience might occasionally affect the behaviour when the susceptible and restrained MBONs learn something new, and hence mask the LTM output, but eventually this will be smoothly integrated with the previous experience in the LTM MBONs. The DPR plays an important role in this mechanism, as we saw earlier, and the connectivity alone is not enough for it to work properly.

By contrast, the RPE plasticity rule lacks this flexibility and fails to maintain useful LTMs when applied to the same circuit architecture. A literal interpretation of RPE for the MB would require that the difference (error) between the postsynaptic MBON activity and the DA level is somehow calculated in the presynaptic KC axon. This seems inconsistent with the observation that learning is generally unaffected by silencing the MBONs during acquisition (Hige et al., 2015; Krashes et al., 2007; Dubnau et al., 2001; McGuire et al., 2001). Alternatively (and not directly requiring MBON activity in the KC plasticity rule) the RPE could be implemented by circuits (Bennett et al., 2021; Springer and Nawrot, 2021; Eschbach et al., 2020) in which DANs transmit an error signal computed by their input reinforcement plus the opposing feedback from MBONs (i.e., MBONs inhibit DANs that increase the KC→MBON synaptic weights, or they excite those that suppress the synaptic weights). However, although the evidence for MBON-DAN feedback connections is well-grounded, it is less clear that they are consistently opposing. For example, in the microcircuits we have described, based on neurophysiological evidence, some DANs that depress synaptic weights receive inhibitory feedback from MBONs (Pavlowsky et al., 2018) and some DANs that potentiate synaptic weights receive excitatory feedback from DANs (Ichinose et al., 2015). As we have shown, the DPR is able to operate with this variety of MBON-DAN connections. Note that, by using the appropriate circuit, that is, positive MBON-DAN feedback to depressing DANs, our DPR could also have an RPE effect. Although the proposed IC does not include such connections, it is still possible that they exist.

### The conditioning effects of the model

During the past decades, a variety of learning effects have been investigated in flies, including forward and backward (relief) conditioning, first- and second-order conditioning and blocking, which we could potentially use to challenge our model. In the methods section ‘Derivation of the dopaminergic plasticity rule’, we demonstrate that our model supports the backward (or relief) conditioning results presented in Handler et al., 2019. Backward conditioning is when the reinforcement is delivered just before the odour presentation and it is based on the time dependency between the two stimuli. Handler et al., 2019 suggest that the backward conditioning is a mechanism driven by ER-Ca2+ and cAMP in a KC→MBON synapse, when a single DAN releases DA on it. In our model, we assume that different time courses in the response of DopR1 and DopR2 receptors cause the different patterns of ER-Ca2+ and cAMP, resulting in the formation of opposite associations for forward and backward conditioning. We note however that in our model the effect also requires that the target MBON inhibits the respective DAN (as in our susceptible memory microcircuits) altering the time course of neurotransmitter release. This may suggest that backward conditioning does not occur in all MB compartments. We believe that this mechanism for backward conditioning is better supported than the hypothesised mechanism of post-inhibitory rebound in opposing valence DANs presented in Adel and Griffith, 2021, although some role for both mechanisms is possible.

Backward conditioning can be distinguished from the unpaired conditioning effect; the latter involves the presentation of reinforcement and a specific odour in alternation with less temporal proximity. It has been observed (Jacob and Waddell, 2020; Schleyer et al., 2018) that this procedure will produce a change in response to the odour that is opposite in valence to the reinforcement, for example, approach to an odour that is ‘unpaired’ with shock. Note that this effect can be observed both in standard two-odour CS+/CS- training paradigms (where an altered response to CS-, in the opposite direction to CS+, is often observed) but also in single-odour unpaired paradigms. Surprisingly, our model also produces unpaired conditioning, notably through a different mechanism than backward conditioning. When DANs are activated by a reinforcement without KC activation, the weights of all KCs are potentially altered, for example, restored towards their resting weight or slightly potentiated. This alteration means that subsequent presentation of odour alone can be accompanied by MBON-driven activation of DANs, resulting in specific alteration of the weights for the presented odour. In the example of Figure 12, odour A starts to self-reinforce its attractive LTM when presented in alternation with shock and will be preferred to an alternative odour B in subsequent testing. However, repeated presentation of other odours during testing, without further shock, might lead to generalisation (equal preference to all experienced odours).

![Figure 12.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig12-v1.jpg)

**Figure 12.:** During the training phase, we deliver electric shock or odour A alternately. During the test phase, we deliver odours A and B alternately. The PI is calculated by using the mushroom body output neuron (MBON) responses for each odour.

The self-reinforcing property of the positive feedback in the LTM microcircuit can also account for second-order conditioning. If a motivation has been associated to an odour, MBONs related to that motivation will have increased activity when the odour is delivered, even in the absence of reinforcement. In the LTM microcircuit, the positive MBON-DAN connection will consequently activate the charging DAN, so any additional cue (or KC activity) presented alongside the learned odour will also experience an increase in the respective KC→MBON weights, creating a similar charging momentum and resulting in a second-order association. Perhaps surprisingly, this predicts that second-order conditioning might happen directly in the LTM microcircuit without being filtered by the susceptible and restrained memories first. This would be consistent with the observation that second-order conditioning in flies requires strong induction of the first-order memory and that first-order memory does not appear to be extinguished by the absence of reinforcement during second-order training (Tabone and de Belle, 2011).

Finally, although we have not tested it explicitly here, it is clear that our plasticity rule (unlike RPE) would not produce blocking. The blocking effect, as described by Kamin, 1967, is when the conditioning to one stimulus subsequently blocks any conditioning to other elements of a mixture including that stimulus. Under RPE learning, this is explained by the first stimulus already correctly predicting the reinforcer, so there is no error to drive a change in the weights. Using the DPR, the updates are local to the synapse and do not depend on a calculation of errors summarised across different odour identities, so blocking does not happen, which is consistent with the observed behaviour of fruit flies (Young et al., 2011; Brembs and Heisenberg, 2001). Although the presentation of a learned odour along with a novel odour might, through feedback from the MBONs, alter the DAN responses to the reinforcement, in our circuit this is not generally an opponent feedback so will not cancel the reinforcing effects for the novel odour. This also highlights the difference between our susceptible, restrained, and long-term memory microcircuits from the RPE circuits described in Bennett et al., 2021, Springer and Nawrot, 2021, Eschbach et al., 2020, and Zhao et al., 2021. Nevertheless, as Wessnitzer et al., 2012 and later Bennett et al., 2021 suggest, the fact that blocking has not been observed in fruit flies could also be explained by the way that the mixture of odours is represented by the KCs, that is, that it might not be simply the superposition of the activity patterns of the individual odours.

### Additional mushroom body connections

Our model suggests that only KC→MBON, MBON⊣DAN, MBON→DAN, and DAN⊸MBON connections are essential for successful learning in the MBs. However, there are a number of additional known connections in the MBs, such as KC→APL, APL⊣KC, DAN→MBON, axoaxonic KC→KC and KC→DAN connections that have been neglected in this model, and need further consideration.

In the larval brain, there are two anterior paired lateral (APL) neurons, one for each MB. They extend their dendrites to the lobes of the MBs and terminate their axons in the calyxes releasing the inhibitory GABA neurotransmitter (Tanaka et al., 2008). Although there are still two of them, in the adult brain both their dendrites and axons are innervating the calyx and the lobes (Wu et al., 2013), suggesting that they function as both global and local inhibitory circuits. Moreover, DAN⊣APL (Liu and Davis, 2009) and APL⊣DAN (Wu et al., 2012) connections have been proposed, but there is no clear description of what their function is. Several previous models (Peng and Chittka, 2017; Delahunt et al., 2018) have demonstrated that a potential function for this global/local inhibition network is gain control such that the total number of KCs firing to different stimuli remains similar, and indeed that the same effect can be implemented using a flexible threshold for KC firing (Saumweber et al., 2018; Zhu et al., 2020; Zhao et al., 2020). In our model, we have simplified the KC input, representing just two odours as different patterns across a small number of KCs with a fixed number of them being active at all times, so the hypothesised gain control function of the APL is not useful here. However, it remains an interesting question whether there is learning between the KC and APL in the lobes (Zhou et al., 2019), or between the APL and KC in the calyx, and what role this might play in the overall dynamics of memory acquisition.

In addition, Eichler et al., 2017 suggest that most of the KCs input, that is, 60%, is from other KCs. We suggest that these connections (together with the ones from the APL) might create local winner-takes-all (WTA) networks that force a limited number of KCs per compartment to be active at one time. This predicts that it is possible for the same KC axon to be active in one compartment but inactive in another (consistent with recent data from Bilz et al., 2020), and that an almost fixed number of KCs might be active at all times, even when no odour is delivered (e.g., fresh air only) enabling the acquisition and forgetting at all times. Ito et al., 2008 show that KCs can be active even in the absence of odours but with no consistent spiking, which is a characteristic of WTA networks when the underlying distribution of spikes across the neurons is almost uniform.

Eichler et al., 2017 also observed (from electron microscopy reconstruction in larva) that within a compartment, in a ‘canonical microcircuit’, KCs make direct synapses to the axons of DANs, and that DAN pre-synapses often simultaneously contact KCs and MBONs. The same connections have been observed in adult Drosophila by Takemura et al., 2017. The extent to which KCs (and thus odour inputs) might be directly exciting DANs remains unclear. Cervantes-Sandoval et al., 2017 show that stimulating KCs results in increased DAN responses and that DANs are activated through the ACh neurotransmitter. However, we note that in our model such an effect could be explained without assuming a direct connection. For example, in the LTM microcircuit, activating the KCs results in increased activity of the LTM MBON, which excites the respective charging DAN. The DAN that Cervantes-Sandoval et al., 2017 provide evidence from is PPL1-α2α′2, which gets excited by MBON-α2α′2 neurons as it is characterised by the ACh neurotransmitter (Aso et al., 2014a). In our terms, this could be an LTM MBON that excites its respective charging DAN, PPL1-α2α′2 (Li et al., 2020), and provide the source of ACh detected on it. More generally, the altered activity of DANs in response to odours that have been observed during learning can be also observed in our model, without requiring direct KC→DAN connections or their modification. Nevertheless, such connections may possibly play a role in enhancing the specificity of dopamine-induced changes in KC→MBON connectivity. Interestingly, the depression of KC→DAN synapses, in parallel with KC→MBON synapses, could provide an alternative mechanism for implementing RPE learning (Takemura et al., 2017).

Takemura et al., 2017 demonstrate that the direct synapses observed from DANs to MBONs are functional in altering the MBON postsynaptic current to DAN activation, independently of KCs. This could be a mechanism by which learnt responses to reinforcements are coordinated with the current presence or absence of the reinforcement (Schleyer et al., 2020; Schleyer et al., 2011; Gerber and Hendel, 2006). Another possibility is that postsynaptic as well as presynaptic changes might be involved in learning at the KC→MBON synapse (Pribbenow et al., 2021).

### Beyond attraction and aversion

The IC consists of six MBONs and six DANs that link a pair of antagonistic motivations, attraction, and avoidance. However, there are ∼34 MBONs and ∼130 DANs in the MB of the adult fruit fly brain, within which the IC is an identifiable motif. We suggest the possibility that this motif could be repeated, representing additional opposing motivations, with some neurons having multiple roles depending on the motivational context as proposed by Cohn et al., 2015, working either as restrained MBONs and discharging DANs, or as LTM MBONs and forgetting DANs depending on the reinforcer identity. We have illustrated this concept of a unified system of motivations as the ‘incentive wheel’ (see Appendix 1—figure 1). This could explain how PAM-β2β′2a (i.e., MB301B; May et al., 2020) is a sugar-encoding discharging DAN in the appetitive olfactory conditioning context, but it also is an avoidance-driving forgetting DAN in a different context (e.g., aversive olfactory conditioning). In addition, two MBONs of the IC do not interact with the α′/β′ KCs of the MB. MBON-γ4>γ1γ2 and MBON-γ1pedc>α/β are part of two autonomous microcircuits, that is, the SMs, and are working under the context provided by the ∼675 γ-KCs relative to the task. This makes it possible that the KCs from the γ lobe connect to all the SMs of the flies for the approximately eight available motivations illustrated in Appendix 1—figure 1.

From a functional point of view, the MBs seem to be involved in the motivation and behaviour of the animal, especially when it comes to behaviours essential for survival. In the mammalian brain, this function is subserved by the limbic system, which is composed of a set of complicated structures, such as the thalamus, hypothalamus, hippocampus, and amygdala (Dalgleish, 2004; Roxo et al., 2011). According to Papez, 1937, sensory (and mostly olfactory) input comes in the limbic system through the thalamus, which connects to both the cingulate cortex (through the sensory cortex) and the hypothalamus (Roxo et al., 2011; Dalgleish, 2004). Responses in the cingulate cortex are guiding the emotions, while the ones in the hypothalamus are guiding the behaviour (bodily responses). Finally, the hypothalamus connects with the cingulate cortex through the anterior thalamus (forward) and the hippocampus (backward stream). Maclean, 1949 augmented this model by adding the amygdala and PFC structures that encode primitive emotions (e.g., anger and fear) and connect to the hypothalamus (Roxo et al., 2011; Dalgleish, 2004). We suggest that some of the functions we have identified in the MB IC could be mapped to limbic system structures (see Figure 13).

![Figure 13.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig13-v1.jpg)

**Figure 13.:** On the left, we show the mushroom body microcircuits that correspond to the different structures in the mammalian limbic system. In the centre, we have the connections among the different structures of the limbic system. On the right, we show the groups of mushroom body neurons we suggest that have a similar function to the ones in the limbic system.

More specifically, the α′/β′-KCs could have a similar role to the neurons in the thalamus, α/β-KCs represent a higher abstraction of the input stimuli and have a similar role to the ones in the sensory cortex, while the γ-KCs represent relatively unprocessed stimuli. This would make the susceptible MBONs parallel to neurons in the amygdala, creating responses related to primitive motivations and connecting to (inhibiting) the restrained MBONs, which we would compare to the hypothalamus as providing the main control of behaviour. As we suggest that the same MBONs could fulfil a role as LTM or restrained in different circuits (see Appendix 1—figure 1), the LTM would also correspond to hypothalamus, with input from the α′/β′-KCs, and thus the RSM, RLM, LTM, and MAM microcircuits are assumed to correspond to hypothalamus functions. Following this analogy, we predict that the function of the cingulate cortex then is represented by the α/β MBONs, encoding the ‘emotions’ of the animal towards reinforced stimuli, potentially controlling more sophisticated decision-making. This mapping would suggest the connections amongst the restrained/LTM (α′/β′) MBONs and the ‘emotional’ (α/β) MBONs are similar to the hippocampus and anterior thalamus pathways.

While it might seem startling to suggest that a compact circuit of single identified neurons in the insect MB mimics in miniature these far larger and more complex structures in the mammalian brain, the justification comes from the similarity in the behavioural demands common to all animals: surviving and adapting in a changing world.

## Materials and methods

### Implementation of the incentive circuit

We represent the connections between neurons by using synaptic weight matrices and non-linearly transform the information passing from one neuron to another by using an activation function. Next, we define these parameters and some properties of our computational model, which are not a result of unconstrained optimisation and are consistent throughout all our experiments.

#### Parameters of the model

We assume that the odour identity passes through the projection neurons (PNs) into the mushroom body and its Kenyon cells (KCs). It is not in the scope of this work to create a realistic encoding of the odour in the PNs, so we assume that the odour signal is represented by $n_{p}=2$ PNs, one for each odour, and that these project to form distinct activations in a set of $n_{k}=10$ KCs in the MB, that is, a subset of KCs that respond to the specific odours used in the experiments. Therefore, the vector $p_{A}=[1,0]$ represents the activity of the PNs when odour A is detected, $p_{B}=[0,1]$ when odour B, $p_{AB}=[1,1]$ when both odours, and $p_{∅}=[0,0]$ when none of them is detected. The responses of the KCs are calculated by

$$
k(t)=WAT_{0.5}[k^{T}(t)⋅W_{p2k}+η]whereη∼N(0,0.001)
$$

$η$ is some Gaussian noise, $W_{p2k}\inR_{+}^{2\times10}$ is the weights matrix that allows the transformation of the two-dimensional odour signal into the ten-dimensional KC responses, and t is the current time-step. The WTA0.5 [x] is an activation function that keeps the top 50% of KCs active, based on the strength of their activity. Note that the number of neurons we are using for PNs and KCs is not very important, and we could use any combination of PN and KC populations. However, the bigger the KC population the smaller percentage of them should be active. The PN→KC synaptic weights used are shown as

$$
W_{p2k}=[0.80.80.80.80.80.80.800000000.80.80.80.80.80.8].
$$

The odours are represented by different firing patterns across 10 KCs: 4 fire only for A, and 3 fire only for B, while the remaining 3 fire to either odour. This is to show the effects of the DPR when we have overlap in the KCs that respond to the two odours used in the conditioning paradigm. This assumption also created the best fit with the data, suggesting that there might be overlapping KCs encoding the real odours tested in the fly experiments.

We transform the reinforcement (US), $u⁢(t)\in{0,1}^{2}$, delivery into an input for the DANs by using the weights matrix $W_{u2d}\inℝ_{+}^{2\timesn_{d}}$. We represent the activity of the DANs, $d⁢(t)\inℝ^{6}$, with a six-dimensional vector, where each dimension represents a different neuron in our model. Specifically,

$$
d⁢(t)=[d_{at}⁢(t)d_{av}⁢(t)c_{at}⁢(t)c_{av}⁢(t)f_{at}⁢(t)f_{av}⁢(t)].
$$

The US is represented by a two-dimensional vector where the first dimension denotes rewarding signal and the second dimension denotes punishment: $u_{sugar}=[1,0]$ and $u_{shock}=[0,1]$; and the contribution of this vector to the responses of the DANs is given by

$$
W_{u2d}=[202000020200].
$$

In line with the DANs vector representation, we have a similar vector for MBONs, $m⁢(t)\inℝ^{6}$, where each dimension represents the response of a specific neuron in time $t$ as is shown in the following equation:

$$
m⁢(t)=[s_{at}⁢(t)s_{av}⁢(t)r_{at}⁢(t)r_{av}⁢(t)m_{at}⁢(t)m_{av}⁢(t)].
$$

The weight matrix that encodes the contribution of KCs to the MBON responses, $W_{k2m}⁢(t)\inℝ^{10\times6}$, is initialised as

$$
W_{k2m}⁢(t=0)=1⁢(n_{k},n_{m})=1⁢(10,6),
$$

which effectively is a $10\times6$ matrix of ones. In other words, all KCs connect to all MBONs, and their initial weight is positive and the same for all connections. As these are plastic weights, their value depends on the time-step, and therefore we provide time, $t$, as a parameter. Note that also $w_{rest}=1$, which initially results in the absence of memory, $W_{k⁢2⁢m}^{i⁢j}⁢(t=0)-w_{rest}=0$. Thus, any deviation of the synaptic weights from their resting value represents a stored memory with strength $v_{mem}^{i⁢j}⁢(t)=||W_{k⁢2⁢m}^{i⁢j}⁢(t)-w_{rest}||$.

There are also MBON→DAN, $W_{m2d}\inℝ^{6\times6}$, and MBON→MBON connections, $W_{m2m}\inℝ^{6\times6}$, which are given by

$$
W_{m2d}=[0-0.30000-0.300000000.50000000.500000.300.500000.300.5]
$$

and

$$
W_{m2m}=[000-10000-1000000000000000000000000000].
$$

The above matrices summarise the excitatory (positive) and inhibitory (negative) connections between MBONs and DANs or other MBONs as defined in the IC (Figure 3, see also Figure 14). The sign of the weights was fixed but the magnitude of the weights was hand-tuned in order to get the desired result, given the constraint that equivalent types of connections should be the same weight (e.g., in the reciprocal microcircuits). The magnitude of the synaptic weights specifies the effective strength of each of the described microcircuits in the overall circuit. We also add some bias to the responses of DANs, $b_{d}$, and MBONs, $b_{m}$, which is fixed as

$$
b_{d}=[-0.5-0.5-0.15-0.15-0.15-0.15]
$$



$$
b_{m}=[-2-2-0.5-0.5-0.5-0.5].
$$

![Figure 14.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig14-v1.jpg)

**Figure 14.:** Each panel corresponds to a different synaptic weights matrix of the circuit. The size of the circles when the presynaptic axon crosses the postsynaptic dendrite shows how strong a connection is, and the colour shows the sign (blue for inhibition, red for excitation). Light-green stars show where the synaptic plasticity takes place and how the dopaminergic neurons (DANs) modulate the synaptic weights between Kenyon cells (KCs) and mushroom body output neurons (MBONs).

![Figure 14—figure supplement 1.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig14-figsupp1-v1.jpg)

**Figure 14—figure supplement 1.:** Each column corresponds to the responses of a different neuron. Odd and even rows show the responses of the neurons to odours A and B, respectively. Pairs of rows (consecutive odours A and B) show the responses of the neurons for the different values of the target parameter (indicated in the first column). Black dashed line shows the responses of the neurons for the chosen (*) parameter. The different colour codes show the responses of the neurons for the different (absolute) values of the target parameter as indicated in the colour bar on the bottom left.

![Figure 14—figure supplement 2.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig14-figsupp2-v1.jpg)

**Figure 14—figure supplement 2.:** Each column corresponds to the responses of a different neuron. Odd and even rows show the responses of the neurons to odours A and B, respectively. Pairs of rows (consecutive odours A and B) show the responses of the neurons for the different values of the target parameter (indicated in the first column). Black dashed line shows the responses of the neurons for the chosen (*) parameter. The different colour codes show the responses of the neurons for the different values of the target parameter as indicated in the colour bar on the bottom left.

![Figure 14—figure supplement 3.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig14-figsupp3-v1.jpg)

**Figure 14—figure supplement 3.:** Each column corresponds to the responses of a different neuron. Odd and even rows show the responses of the neurons to odours A and B, respectively. Pairs of rows (consecutive odours A and B) show the responses of the neurons for the different values of the target parameter (indicated in the first column). Black dashed line shows the responses of the neurons for the chosen (*) parameter. The different colour codes show the responses of the neurons for the different values of the target parameter as indicated in the colour bar on the bottom left.

This bias can be interpreted as the resting value of the neurons or some external input from other neurons that are not included in our model.

Finally, we define the DAN function matrix, $W_{d2km}\inℝ^{n_{d}\timesn_{m}}$, which transforms the responses of the DANs into the dopamine factor that modulates the $W_{k2m}⁢(t)$ synaptic weights, and it is given as

$$
W_{d2km}=[0-10000-100000000-10.3000-1000.300-0.300-1000-0.3-10].
$$

All the parameters described above are illustrated in Figure 14. Figure 14—figure supplement 1, Figure 14—figure supplement 2, and Figure 14—figure supplement 3 show how each of these parameters affects the responses of the neurons in the IC. The last thing left to describe is the activation function, which is used in order to generate the DAN and MBON responses. This is

$$
ϱ(x)={2ifx\geq2,xif0<x<2,0ifx\leq0,
$$

which is the rectified linear unit (ReLU) function, bounded in $ϱ⁢(x)\in[0,2]$. The reason why we bound the activity is to avoid having extremely high values that explode during the charging of the LTM.

#### Forward propagation

For each time-step, $t$, we read the environment and propagate the information through the model in order to update the responses of the neurons and the synaptic weights. This process is called forward propagation, and we repeat it as long as the experiment runs.

First, we read the CS, $p⁢(t)$, and US, $u⁢(t)$, from the environment and calculate the KC responses by using Equation 2. In order to calculate the DANs and MBONs update, we define the differential equations as follows:

$$
\tau⁢\frac{d⁢d}{d⁢t}=-d+u^{T}⁢(t)⋅W_{u2d}+m^{T}⁢(t)⋅W_{m2d}+b_{d}
$$



$$
\tau⁢\frac{d⁢m}{d⁢t}=-m+k^{T}⁢(t)⋅W_{k2m}⁢(t)+m^{T}⁢(t)⋅W_{m2m}+b_{m}
$$

where $\tau=3$ is a time-constant that is defined by the number of time-steps associated in each trial, $T$ denotes the transpose operation of the matrix or vector, and $m=m⁢(t)$ and $d=d⁢(t)$ are functions of time. Using the above differential equations, we calculate the updated responses (i.e., responses in the next time-step, $t$) as

$$
d⁢(t)=ϱ⁢[\frac{1}{\tau}⁢d+\frac{d⁢d}{d⁢t}]
$$



$$
m⁢(t)=ϱ⁢[\frac{1}{\tau}⁢m+\frac{d⁢m}{d⁢t}].
$$

Finally, we calculate the dopaminergic factor, $\delta⁢(t)\inℝ^{6}$, and update the KC→MBON synaptic weights as

$$
\delta⁢(t)=d^{T}⁢(t)⋅W_{d2km}
$$



$$
\tau⁢\frac{d⁢W_{k2m}}{d⁢t}=\delta⁢(t)*[k^{T}⁢(t)+W_{k2m}-w_{rest}]
$$



$$
W_{k2m}⁢(t)=max⁡[W_{k2m}+\frac{d⁢W_{k2m}}{d⁢t},0]
$$

where ‘*’ denotes the element-wise multiplication, $w_{rest}=1$ is the resting value of the weights, and $W_{k2m}=W_{k2m}⁢(t)$ is a function of time. Note that element-wise multiplication means that each element of the $\delta⁢(t)$ vector will be multiplied with each column of the $W_{k2m}⁢(t)$ matrix. Also, the element-wise addition of the transposed vector, $k^{T}⁢(t)$, to the $W_{k2m}⁢(t)$ matrix, means that we add each element of $k⁢(t)$ to the corresponding row of $W_{k2m}⁢(t)$. We repeat the above procedure as many times as it is required in order to complete the running experimental paradigm routine.

#### Modelling the neural responses

To emulate the acquisition and forgetting paradigms used for flies, we run the simulated circuit in an experiment that consists of $T=73$ time-steps. Each time-step actually comprises four repeats of the forward propagation update described above to smooth out any bias due to the order of computations (value vs. weights update). After the initialisation time-step at $t=0$, there are 24 trials where each trial consists of 3 in-trial time-steps.

Within each trial, the first time-step has no odour, and in the second and third time-steps, odour is presented: odour A on even trials and odour B on odd trials. A trial can have no shock (Figure 15A), unpaired shock presented in the first time-step (Figure 15B), or paired shock presented in the third time-step (Figure 15C). The first two trials compose the ‘pre-training phase’, where we expose the model to the two odours alternately (i.e., odour A in trial 1 and odour B in trial 2) without shock delivery. Then we have the acquisition phase, where we deliver shock paired with odour B for 10 trials (five trials per odour; Figure 15D). Before we proceed to the forgetting phases, we leave two empty trials (one per odour), which we call the resting trials. The forgetting phases last for another 10 trials (five trials per odour; Figure 15E–G). During the extinction phase, no shock is delivered while we continue alternating the odours (see Figure 15E); during the unpaired phase, shock is delivered unpaired from odour A (see Figure 15F); while at the reversal phase shock is paired with odour A (Figure 15G).

![Figure 15.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig15-v1.jpg)

**Figure 15.:** A single trial is composed of three in-trial time-steps and each time-step by four repeats. Odour is provided only during the second and third in-trial time-steps, while shock delivery is optional. (A) In an extinction trial, only odour (CS) is delivered. (B) During an unpaired trial, shock is delivered during in-trail time-step 1. (C) During a paired trial, shock is delivered along with odour delivery and during in-trial time-step 3. (D) The acquisition phase has five odour A-only trials and five paired odour B trials alternating. (E) The extinction phase has five odour A-only trials and five odour B-only trials alternating. (F) The unpaired phase has five odour A unpaired trials and five odour B-only trials alternating. (G) The reversal phase has five odour A paired trials and five odour B-only trials alternating. The colours used in this figure match the ones in Figure 4.

##### The classic unpaired conditioning paradigm

In this case, during the acquisition phase we deliver only electric shock in odd trials (omission of odour B), followed by an extinction phase as described above.

### Modelling the behaviour

The experiments last for $100s$ each, and they are split into three phases as shown in Figure 11A. In pre-training, the flies are placed in the centre of arena and explore freely for $20s$. In training, either shock or sugar is associated with the region $30cm$ around odour A, odour B, or around both sources for $30s$. In post-training, we remove the reinforcement and let the flies express their learnt behaviour for another $50s$, creating an extinction forgetting condition. Figure 11B shows the normalised cumulative time spent experiencing each odour and the odour preference of the flies during the different phases for each of the six training conditions, and for 10 repeats of the experiment, when their behaviour is controlled by a combination of the attractive and repulsive forces on the two odours. The actual paths of the flies for all the 10 repeats are illustrated in Figure 11—figure supplement 4.

In practice, in order to create the experiences of $n_{fly}=100$ flies, we have created another routine that embeds the simulation of their motion and environment. We represent the position of each fly, $a⁢(t)\inℂ$, and the sources of the odours in the arena, $\mu_{A}\inℂ$ and $\mu_{B}\inℂ$ for odours A and B, respectively, in the 2D space as complex numbers in the form $x+i⁢y$. Therefore, the flies are initialised in $a⁢(t=0)=0$ and the sources of the odours are placed in $\mu_{A}=-0.6$ and $\mu_{B}=0.6$. The standard deviation of the odour distributions is $\sigma_{A}=\sigma_{B}=0.3$.

We get the odour intensity in each time-step by using the Gaussian density functions of the two odours and the position of the fly in the arena

$$
p(t)={p_{AB},ifN(a(t)|\mu_{A},\sigma_{A})>\theta_{CS}andN(a(t)|\mu_{B},\sigma_{B})>\theta_{CS},p_{A},ifN(a(t)|\mu_{A},\sigma_{A})>\theta_{CS},p_{B},ifN(a(t)|\mu_{B},\sigma_{B})>\theta_{CS},p_{∅},otherwise
$$

where $p_{A}$, $p_{B}$, $p_{A⁢B}$, and $p_{∅}$ are the identities of odours A, B, ‘A and B’, and none of them, respectively, in the PNs as described in the ‘Parameters of the model’, and $\theta_{CS}=0.2$ is the detection threshold for the odour. Note that PN responses depend only on the fact that an odour has been detected or not and it is not proportional to the detected intensity. The reinforcement is applied to the simulated fly when the position of the agent is inside a predefined area around the odour, that is, $||\mu_{CS}−a(t)||<ρ_{US}$, where $ρ_{US}=0.3$ is the radius of the reinforced area. Note that the radius of the area where the odour is detectable is roughly $ρ_{CS}≃0.58$, which is larger than the reinforced area. Then we run a forward propagation using the above inputs.

From the updated responses of the MBONs, we calculate the attraction force, $v(t)$, for the mixture of odours which modulates the velocity of the fly. This force is calculated by taking the difference between the responses of the MBONs that drive the behaviour:

$$
v_{at}(CS|t)=\frac{1}{3}[s_{at}(t)+r_{at}(t)+m_{at}(t)]⋅\frac{\mu_{CS}−a(t)}{||\mu_{CS}−a(t)||}whereCS\in{odour A, odour B}
$$



$$
v_{av}(CS|t)=\frac{1}{3}[s_{av}(t)+r_{av}(t)+m_{av}(t)]⋅\frac{\mu_{CS}−a(t)}{||\mu_{CS}−a(t)||}whereCS\in{odour A, odour B}
$$



$$
v(t)=\sumCS{A,B}P_{CS}(t)⋅v_{at}(CS|t)−\sumCS{A,B}P_{CS}(t)⋅v_{av}(CS|t)
$$

where $\mu_{CS}$ is the position of the odour source and $P_{CS}⁢(t)$ is the probability of being closer to the specific CS source calculated using the Gaussian distribution function and the Bayesian theorem. For example, given that the prior probability of being closer to odours A and B is equal at any time, that is, $P⁢(A)=P⁢(B)=0.5$, the probability of being closer to odour A is given by

$$
P_{A}⁢(t)=\frac{N⁢(a⁢(t)|\mu_{A},\sigma_{A})}{N⁢(a⁢(t)|\mu_{A},\sigma_{A})+N⁢(a⁢(t)|\mu_{B},\sigma_{B})}.
$$

The velocity of the simulated fly is updated as follows

$$
v(t)=v(t−1)+v(t)+\epsilon_{x}+i\epsilon_{y}where\epsilon_{x},\epsilon_{y}∼N(\mu=0,\sigma=0.1)
$$



$$
v^⁢(t)=0.05⋅\frac{v⁢(t)}{||v⁢(t)||}.
$$

We normalise the velocity so that we keep the direction but replace the step size with $0.05m/s$. The noise added to the velocity is introduced in order to enable the flies to move in two dimensions and not just between the two odour sources. Also, when the attraction force is $v(t)=0$, then the noise along with the previous velocity is the one that drives the flies.

We repeat the above process for $T=100$ time-steps with $1Hz$ (one time-step per second), and we provide shock or sugar (when appropriate) between time-steps 20 and 50, otherwise we use a zero-vector as US input to the DANs.

### Calculating the normalised cumulative exposure and the preference Index

In Figure 11B, for each phase (i.e., pre-training, training, and post-training), we report the normalised cumulative exposure of the flies in each odour and their PI between them. The normalised cumulative exposure is calculated by

$$
C_{CS, phase}^{R}=\sumi=1R\frac{t_{CS, phase}^{i}}{T_{phase}}
$$

where $R$ is the repeat of the experiment, i is the iterative repeat, $T_{phase}$ is the number of time-steps for the specific phase, and $t_{CS,phase}^{i}$ is the number of time-steps spent exposed in the specific CS $\in{A,B}$, phase, and repeat.

The preferences index for every repeat is calculated using the above quantities

$$
PI_{phase}^{R}⁢(t)=\frac{C_{A, phase}^{R}-C_{B, phase}^{R}}{C_{A, phase}^{R}+C_{B, phase}^{R}}.
$$

### The reward prediction error plasticity rule

In Figure 9—figure supplement 2, Figure 9—figure supplement 3, Figure 11—figure supplement 5, and Figure 11—figure supplement 6, we present the responses and synaptic weights of the IC neurons, and the behaviour of the simulated flies using the RPE plasticity rule. This was done by replacing our plasticity rule in Equation 19 with the one below:

$$
\tau\frac{dW_{k2m}}{dt}=k(t)∗[\delta(t)−m(t)+w_{rest}].
$$

### Derivation of the dopaminergic plasticity rule

Handler et al., 2019 suggest that ER-Ca2+ and cAMP play a decisive role in the dynamics of forward and backward conditioning. More specifically, they suggest that the KC→MBON synaptic change, $Δ⁢W_{k⁢2⁢m}^{i⁢j}$, is proportional to the combined ER-Ca2+ and cAMP levels, which can be written formally as

$$
ΔW_{k2m}^{ij}(t)∝−(ER-Ca^{2+})^{ij}(t)−(cAMP)^{ij}(t).
$$

We assume that ER-Ca2+ and cAMP levels are determined by information available in the local area of the target KC axon (presynaptic terminal): the dopamine (DA) level emitted by the DANs to the KC synapses of the respective (jth) MBON, $D^{j}⁢(t)\geq0$; the activity of the (ith) presynaptic KC, $k^{i}⁢(t)\geq0$; the respective KC→MBON synaptic weight; $W_{k⁢2⁢m}^{i⁢j}⁢(t)\geq0$ (assumed always positive, exciting the MBON), and the resting synaptic weights, $w_{rest}\inℝ$, which we assume are a constant parameter of the synapse. Tuning the above quantities in order to reproduce the ER-Ca2+ and cAMP levels, we postulate a mathematical formulation of the latter as a function of the available information

$$
(ER-Ca^{2+})^{ij}∝−D_{△}^{j}(t)⋅[k^{i}(t)−w_{rest}]−[D_{△}^{j}(t)−D_{▽}^{j}(t)]⋅W_{k2m}^{ij}(t)
$$



$$
(cAMP)^{i⁢j}∝D_{▽}^{j}⁢(t)⋅[k^{i}⁢(t)-w_{rest}]
$$

where $D_{▽}^{j}⁢(t)$ and $D_{△}^{j}⁢(t)$ are the depression and potentiation components of the DA, respectively (assumed to correspond to DopR1 and DopR2 receptors [Handler et al., 2019] or potentially to involve co-transmitters released by the DAN such as nitric oxide [Aso et al., 2019]). We assume two types of DAN terminals: the depressing and potentiating terminals. In depressing terminals (arrow down), $D_{▽}^{j}⁢(t)$ makes a higher peak in its activity followed by a faster diffusion than $D_{△}^{j}⁢(t)$, which seems to be the key for the backward conditioning. The opposite happens in potentiating DAN terminals. Figure 16 shows the ER-Ca2+ and cAMP levels during forward and backward conditioning for a depressing DAN [see Figure 16—figure supplement 1 for the responses of all the terms used including $D_{▽}^{j}⁢(t)$ and $D_{△}^{j}⁢(t)$], which are comparable to the data shown in Handler et al., 2019 (also Figure 16, shown in grey). Note that here we are more interested in the overall effects of learning shown in Figure 16A rather than the detailed responses of Figure 16B.

![Figure 16.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig16-v1.jpg)

**Figure 16.:** (A) Normalised mean change of the synaptic weight plotted as a function of the $Δ⁢s$ (US start – CS start), similar to Handler et al., 2019, Figure 5F (blue line). For ease of comparison, the predicted mean values are drawn on the top of the data (mean ± SEM) from the original paper (Handler et al., 2019); grey lines and error bars. (B) Detailed ER-Ca2+ and cAMP responses reproduced for the different $Δ⁢s$, and their result synaptic weight change. Black arrowhead marks the time of the CS (duration $0.5s$); red arrowhead marks the time of the US (duration $0.6s$), similar to Handler et al., 2019, Figure 5D. For ease of comparison, the predicted responses are drawn on the top of the data from the original paper (Handler et al., 2019); grey lines.

![Figure 16—figure supplement 1.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig16-figsupp1-v1.jpg)

**Figure 16—figure supplement 1.:** Black arrowhead marks the time of the CS (duration $0.5s$); red arrowhead marks the time of the US (duration $0.6s$), similar to Handler et al., 2019, Figure 5D. Predicted ER-Ca2+, cAMP, and the plasticity effect responses are drawn on top of the data from the original paper (Handler et al., 2019), grey lines.

![Figure 16—figure supplement 2.](https://cdn.elifesciences.org/articles/75611/elife-75611-fig16-figsupp2-v1.jpg)

**Figure 16—figure supplement 2.:** Parameter exploration of the $\tau_{short}$ and $\tau_{long}$ in Equation 35 and Equation 36.For the combinations of $\tau_{short}\in[1,150]$ and $\tau_{long}\in[1,150]$, we calculate the Pearson correlation coefficient between the predicted normalised mean change of the synaptic weight and the one extracted from the data of Handler et al., 2019, and we report the r and p values. With ‘x’ we mark the pair of parameters with the highest correlation.

By replacing Equation 32 and Equation 33 in Equation 31, we can rewrite the update rule as a function of known quantities, forming our DPR of Equation 1, which we rewrite for convenience

$$
ΔW_{k2m}^{ij}(t)=\delta^{i}(t)[k^{j}(t)+W_{k2m}^{ij}(t)−w_{rest}]where\delta^{j}(t)=D_{△}^{j}(t)−D_{▽}^{j}(t)
$$

The dopaminergic factor, $\delta^{j}⁢(t)$, is the difference between the $D_{▽}^{j}⁢(t)$ and $D_{△}^{j}⁢(t)$ levels, and it can be positive [$D_{△}^{j}(t)>D_{▽}^{j}(t)$] or negative [$D_{▽}^{j}(t)<D_{△}^{j}(t)$]. Combined with the state of the KC activity results in the four different weight modulation effects: depression, potentiation, recovery, and saturation.

In Figure 16B (where we assume a depressing DAN terminal), all four effects occur in four out of the six cases, creating complicated dynamics that allow forward and backward learning. Similarly, a potentiating terminal might trigger all the effects in a row but in different order and duration. Note that in the simulations run for the results of this paper, we simplify the dopaminergic factor to have a net positive or negative value for the time-step in which it influences the synaptic weight change as the time-steps used are long enough (e.g., around $5s$; see ‘Implementation of the incentive circuit’ section), and we assume less complicated interchange among the effects.

In Figure 16A, we report the normalised mean change of the synaptic weight calculated using the computed ER-Ca2+ and cAMP levels and the following formula:

$$
⟨Δ⁢W_{k⁢2⁢m}^{i⁢j}⟩∝\frac{1}{T}⁢\sumt=0T-1-(ER-Ca^{2+})^{i⁢j}⁢(t)-(cAMP)^{i⁢j}⁢(t).
$$

#### Decomposing the dopaminergic factor

In Equation 18, the dopaminergic factor, $\delta⁢(t)$, is derived from the matrix Equation 12 which captures in abstracted and time-independent form the effects of dopamine release. To model these more explicitly, as described in the ‘Derivation of the dopaminergic plasticity rule’, the dopaminergic factor can be decomposed as $\delta⁢(t)=D_{△}⁢(t)-D_{▽}⁢(t)$ where each component has a time-dependent form given by the differential equations

$$
\frac{dD_{▽}}{dt}=\frac{1}{\tau_{long}}d^{T}(t)⋅W_{d2km}^{+}−\frac{1}{\tau_{short}}d^{T}(t)⋅W_{d2km}^{−}−(2−\frac{1}{\tau_{short}}−\frac{1}{\tau_{long}})D_{▽}
$$



$$
\frac{dD_{△}}{dt}=\frac{1}{\tau_{short}}d^{T}(t)⋅W_{d2km}^{+}−\frac{1}{\tau_{long}}d^{T}(t)⋅W_{d2km}^{−}−(2−\frac{1}{\tau_{short}}−\frac{1}{\tau_{long}})D_{△}
$$

where $W_{d⁢2⁢k⁢m}^{+}$ and $W_{d2km}^{−}$ represent the positive-only (potentiation/saturation) and negative-only (depression/recovery) dopaminergic effects; $d(t)$ is a vector of the responses of all DANs as a function of time, t; $D_{▽}=D_{▽}(t)$ nd $D_{△}=D_{△}⁢(t)$ are the depression and potentiation components of the DA as functions of time, t; and $\tau_{short}$ and $\tau_{long}$ are the exponential decay time-constants that define the short (main) and long (secondary) durations of the dopamine effect. The longer the time constant, the slower the diffusion but also the lower the peak of the effect. Note that the two time constants must satisfy the constraint $0<\frac{1}{\tau_{short}}+\frac{1}{\tau_{long}}\leq2$ in order for the above differential equations to work properly.

In Figure 16, where we are interested in more detailed dynamics of the plasticity rule, and the sampling frequency is high, that is, $100Hz$, we use $\tau_{short}=60$ and $\tau_{long}=104$, which we choose after a parameter exploration available in Figure 16—figure supplement 2. This essentially means that $D_{▽}⁢(t)$ and $D_{△}⁢(t)$ are expressed as time-varying functions following DAN spike activity. Note that for the specific (susceptible) type of MBON examined there, the DAN causes depression of the synapse, so there is no positive dopaminergic effect, that is, $W_{k⁢2⁢d⁢m}^{+}=0$. By setting $W_{k⁢2⁢d⁢m}^{+}=0$ in Equation 35 and Equation 36, we have the fast update with the high peak for $D_{▽}⁢(t)$ ($0.5s$ for a full update) and a slower update with lower peak for $D_{△}⁢(t)$ ($1s$ for a full update), as described in the ‘Derivation of the dopaminergic plasticity rule’ section.

For the experiments in Figures 4 and 11, we use $\tau_{short}=1$ and $\tau_{long}=+∞$, which removes the dynamics induced by the relation between $D_{▽}⁢(t)$ and $D_{△}⁢(t)$, and Equation 18 emerges from:

$$
\delta(t)=D_{△}(t)−D_{▽}(t)=d^{T}(t)⋅W_{d2km}^{+}+d^{T}(t)⋅W_{d2km}^{−},for\tau_{short}=1and\tau_{long}=+∞=d^{T}⋅W_{d2km}
$$

This essentially means that each update represents a time-step that is longer than the effective period of backward conditioning for the responses of the ‘Microcircuits of the mushroom body’ and ‘Modelling the behaviour’ sections (where sampling frequency is low, i.e., ≤$0.5Hz$ and $1Hz$, respectively), and therefore, we use the same time constants that result in the simplified Equation 18.

### Data collection

In order to verify the plausibility of the IC, we recorded the neural activity in genetically targeted neurons during aversive olfactory conditioning which is described in more detail in McCurdy et al., 2021. We simultaneously expressed the green GCaMP6f Ca2+ indicator and red Ca2+-insensitive tdTomato in neurons of interest to visualise the Ca2+ changes which reflect the neural activity. We collected data from 357 five-to-eight-day-old female flies (2–14 per neuron; eight flies on average) and for 43 neurons, which can be found in Figure 4—source data 1 (also illustrated in Figure 4—figure supplement 1).

Each fly was head-fixed for simultaneous delivery of odours and electric shock while recording the neural activity. Their proboscis was also glued, while their body and legs were free to move (see Figure 4A). The flies were allowed to recover from the gluing process for $15min$ before placing them under the microscope. We used green ($555nm$) and blue ($470nm$) lights to record GCaMP and Tomato signals. We also used 0.1% 3-octanol (OCT) and 0.1% 4-methylcyclohexanol (MCH) for odours A and B, respectively, and the flow rate was kept constant at 500 mL/min for each odour. The flies were allowed to acclimate to the airflow for at least 1 min before starting of the experiment.

During the experiments, we alternate trials where $5s$ of each odour is presented $5s$ after the (green or red) light is on. We start with two pre-training trials (one per odour) followed by five acquisition trials per odour. During acquisition, flies receive alternating $5s$ pulses of OCT (odour A) and MCH (odour B) paired with electric shock, repeated for five trials. During reversal, OCT is presented with shock and MCH without, repeated for two trials. On trials where electric shock was delivered, it was presented $4s$ after odour onset for $100ms$ at $120V$.

### Calculating off- and on-shock values

From the data collection process described above, we get trials of 100 time-steps and at $5Hz$ ($20s$ each). Odour is delivered between time-steps 25 and 50 (between $5s$ and $10s$), and shock is delivered during time-step 45 (at $9s$). In this work, we report two values for each trial: the off-shock and on-shock values, which represent the average response to the odour before and during the period in which shock delivery could have occurred (even if shock is not delivered).

For the off-shock value, from each datastream of activity from the target neuron, we collect the values from time-steps between 28 ($5.6s$) and 42 ($8.4s$). This gives us a matrix of $n_{fly}\times15$ values, whose average and standard deviation are the reported off-shock values. Similarly, for the on-shock values, we collect the values in time-steps between 44 ($8.6s$) and 48 ($9.6s$), which gives a matrix of $n_{fly}\times5$ values, whose average and standard deviation are the on-shock values. We define ‘on-shock’ as the time window from $8.6s$ to $9.6s$, where shock onset occurs at $t=9s$.
