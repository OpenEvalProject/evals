# Presynaptic stochasticity improves energy efficiency and helps alleviate the stability-plasticity dilemma

## Authors

- Simon Schug<sup>1</sup> ([ORCID: 0000-0002-5305-2547](https://orcid.org/0000-0002-5305-2547)) †
- Frederik Benzing<sup>2</sup> ([ORCID: 0000-0001-6580-8690](https://orcid.org/0000-0001-6580-8690))
- Angelika Steger<sup>2</sup>

### Affiliations

1. Institute of Neuroinformatics, University of Zurich & ETH Zurich Zurich Switzerland
2. Department of Computer Science, ETH Zurich Zurich Switzerland

† Corresponding author

## Abstract

When an action potential arrives at a synapse there is a large probability that no neurotransmitter is released. Surprisingly, simple computational models suggest that these synaptic failures enable information processing at lower metabolic costs. However, these models only consider information transmission at single synapses ignoring the remainder of the neural network as well as its overall computational goal. Here, we investigate how synaptic failures affect the energy efficiency of models of entire neural networks that solve a goal-driven task. We find that presynaptic stochasticity and plasticity improve energy efficiency and show that the network allocates most energy to a sparse subset of important synapses. We demonstrate that stabilising these synapses helps to alleviate the stability-plasticity dilemma, thus connecting a presynaptic notion of importance to a computational role in lifelong learning. Overall, our findings present a set of hypotheses for how presynaptic plasticity and stochasticity contribute to sparsity, energy efficiency and improved trade-offs in the stability-plasticity dilemma.

## Introduction

It has long been known that synaptic signal transmission is stochastic (del Castillo and Katz, 1954). When an action potential arrives at the presynapse, there is a high probability that no neurotransmitter is released – a phenomenon observed across species and brain regions (Branco and Staras, 2009). From a computational perspective, synaptic stochasticity seems to place unnecessary burdens on information processing. Large amounts of noise hinder reliable and efficient computation (Shannon, 1948; Faisal et al., 2005) and synaptic failures appear to contradict the fundamental evolutionary principle of energy-efficient processing (Niven and Laughlin, 2008). The brain, and specifically action potential propagation consume a disproportionately large fraction of energy (Attwell and Laughlin, 2001; Harris et al., 2012) – so why propagate action potentials all the way to the synapse only to ignore the incoming signal there?

To answer this neurocomputational enigma various theories have been put forward, see Llera-Montero et al., 2019 for a review. One important line of work proposes that individual synapses do not merely maximise information transmission, but rather take into account metabolic costs, maximising the information transmitted per unit of energy (Levy and Baxter, 1996). This approach has proven fruitful to explain synaptic failures (Levy and Baxter, 2002; Harris et al., 2012), low average firing rates (Levy and Baxter, 1996) as well as excitation-inhibition balance (Sengupta et al., 2013) and is supported by fascinating experimental evidence suggesting that both presynaptic glutamate release (Savtchenko et al., 2013) and postsynaptic channel properties (Harris et al., 2015; Harris et al., 2019) are tuned to maximise information transmission per energy.

However, so far information-theoretic approaches have been limited to signal transmission at single synapses, ignoring the context and goals in which the larger network operates. As soon as context and goals guide network computation certain pieces of information become more relevant than others. For instance, when reading a news article the textual information is more important than the colourful ad blinking next to it – even when the latter contains more information in a purely information-theoretic sense.

Here, we study presynaptic stochasticity on the network level rather than on the level of single synapses. We investigate its effect on (1) energy efficiency and (2) the stability-plasticity dilemma in model neural networks that learn to selectively extract information from complex inputs.

We find that presynaptic stochasticity in combination with presynaptic plasticity allows networks to extract information at lower metabolic cost by sparsely allocating energy to synapses that are important for processing the given stimulus. As a result, presynaptic release probabilities encode synaptic importance. We show that this notion of importance is related to the Fisher information, a theoretical measure for the network’s sensitivity to synaptic changes.

Building on this finding and previous work (Kirkpatrick et al., 2017), we explore a potential role of presynaptic stochasticity in the stability-plasticity dilemma. In line with experimental evidence (Yang et al., 2009; Hayashi-Takagi et al., 2015), we demonstrate that selectively stabilising important synapses improves lifelong learning. Furthermore, these experiments link presynaptically induced sparsity to improved memory.

### Model

Our goal is to understand how information processing and energy consumption are affected by stochasticity in synaptic signal transmission. While there are various sources of stochasticity in synapses, here, we focus on modelling synaptic failures where action potentials at the presynapse fail to trigger any postsynaptic depolarisation. The probability of such failures is substantial (Branco and Staras, 2009; Hardingham et al., 2010; Sakamoto et al., 2018) and, arguably, due to its all-or-nothing-characteristic has the largest effect on both energy consumption and information transmission.

As a growing body of literature suggests, artificial neural networks (ANNs) match several aspects of biological neuronal networks in various goal-driven situations (Kriegeskorte, 2015; Yamins and DiCarlo, 2016; Kell et al., 2018; Banino et al., 2018; Cueva and Wei, 2018; Mattar and Daw, 2018). Crucially, they are the only known model to solve complex vision and reinforcement learning tasks comparably well as humans. We therefore choose to extend this class of models by explicitly incorporating synaptic failures and study their properties in a number of complex visual tasks.

### Model details

The basic building blocks of ANNs are neurons that combine their inputs $a_{1},…,a_{n}$ through a weighted sum $w_{1}⁢a_{1}+…⁢w_{n}⁢a_{n}$ and apply a nonlinear activation function $\sigma⁢(⋅)$. The weights $w_{i}$ naturally correspond to synaptic strengths between presynaptic neuron $i$ and the postsynaptic neuron. Although synaptic transmission is classically described as a binomial process (del Castillo and Katz, 1954) most previous modelling studies assume the synaptic strengths to be deterministic. This neglects a key characteristic of synaptic transmission: the possibility of synaptic failures where no communication between pre- and postsynapse occurs at all.

In the present study, we explicitly model presynaptic stochasticity by introducing a random variable $r_{i}∼Bernoulli(p_{i})$, whose outcome corresponds to whether or not neurotransmitter is released. Formally, each synapse $w_{i}$ is activated stochastically according to

$$
w_{i}=r_{i}⏟\frac{stochastic}{release}⋅m_{i}⏟\frac{synaptic}{strength},wherer_{i}∼Bernoulli(p_{i})⏟\frac{release}{probability}
$$

so that it has expected synaptic strength $w¯_{i}=p_{i}⁢m_{i}$. The postsynaptic neuron calculates a stochastic weighted sum of its inputs with a nonlinear activation

$$
a^{post}⏟\frac{postsynaptic}{activation}=\sigma(\sumi=1nw_{i}a_{i}^{pre}⏟\frac{i-thpresynaptic}{input}).
$$

During learning, synapses are updated and both synaptic strength and release probability are changed. We resort to standard learning rules to change the expected synaptic strength. For the multilayer perceptron, this update is based on stochastic gradient descent with respect to a loss function $L⁢(w¯,p)$, which in our case is the standard cross-entropy loss. Concretely, we have

$$
w¯_{i}^{(t+1)}=w¯_{i}^{(t)}−ηg_{i},whereg_{i}=\frac{∂L(w¯^{(t)},p)}{∂w¯_{i}^{(t)}}
$$

where the superscript corresponds to time steps. Note that this update is applied to the expected synaptic strength $w_{i}¯$, requiring communication between pre- and postsynape, see also Discussion. For the explicit update rule of the synaptic strength $m_{i}$ see Materials and methods, Equation (8). For the standard perceptron model, $g_{i}$ is given by its standard learning rule (Rosenblatt, 1958). Based on the intuition that synapses which receive larger updates are more important for solving a given task, we update $p_{i}$ using the update direction $g_{i}$ according to the following simple scheme

$$
p_{i}^{(t+1)}={p_{i}^{(t)}+p_{up},if|g_{i}|>g_{_{lim}},p_{i}^{(t)}−p_{down},if|g_{i}|\leqg_{_{lim}},
$$

Here, $p_{up},p_{down},g_{lim}$ are three metaplasticity parameters shared between all synapses. (We point out that in a noisy learning setting the gradient $g$ does not decay to, so that the learning rule in (4) will maintain network function by keeping certain release probabilities high. See also Materials and methods for a theoretical analysis.) To prevent overfitting and to test robustness, we tune them using one learning scenario and keep them fixed for all other scenarios, see Materials and methods. To avoid inactivated synapses with release probability $p_{i}=0$, we clamp $p_{i}$ to stay above 0.25, which we also use as the initial value of $p_{i}$ before learning.

On top of the above intuitive motivation, we give a theoretical justification for this learning rule in Materials and methods, showing that synapses with larger Fisher information obtain high release probabilities, also see Figure 2d.

### Measuring energy consumption

For our experiments, we would like to quantify the energy consumption of the neural network. Harris et al., 2012 find that the main constituent of neural energy demand is synaptic signal transmission and that the cost of synaptic signal transmission is dominated by the energy needed to reverse postsynaptic ion fluxes. In our model, the component most closely matching the size of the postsynaptic current is the expected synaptic strength, which we therefore take as measure for the model’s energy consumption. In the Appendix, we also measure the metabolic cost incurred by the activity of neurons by calculating their average rate of activity.

### Measuring information transmission

We would like to measure how well the neural network transmits information relevant to its behavioural goal. In particular, we are interested in the setting where the complexity of the stimulus is high relative to the amount of information that is relevant for the behavioural goal. To this end, we present complex visual inputs with high information content to the network and teach it to recognise the object present in the image. We then measure the mutual information between network output and object identity, see Box 1.

## Results

### Presynaptic stochasticity enables energy-efficient information processing

We now investigate the energy efficiency of a network that learns to classify digits from the MNIST handwritten digit dataset (LeCun, 1998). The inputs are high-dimensional with high entropy, but the relevant information is simply the identity of the digit. We compare the model with plastic, stochastic release to two controls. A standard ANN with deterministic synapses is included to investigate the combined effect of presynaptic stochasticity and plasticity. In addition, to isolate the effect of presynaptic plasticity, we introduce a control which has stochastic release, but with a fixed probability. In this control, the release probability is identical across synapses and chosen to match the average release probability of the model with plastic release after it has learned the task.

All models are encouraged to find low-energy solutions by penalising large synaptic weights through standard $ℓ_{2}$-regularisation. Figure 1a shows that different magnitudes of $ℓ_{2}$-regularisation induce different information-energy trade-offs for all models, and that the model with plastic, stochastic release finds considerably more energy-efficient solutions than both controls, while the model with non-plastic release requires more energy then the deterministic model. Together, this supports the view that a combination of presynaptic stochasticity and plasticity promotes energy-efficient information extraction.

![Figure 1.](https://cdn.elifesciences.org/articles/69884/elife-69884-fig1-v2.jpg)

**Figure 1.:** (a) Different trade-offs between mutual information and energy are achievable in all network models. Generally, stochastic synapses with learned release probabilities are more energy-efficient than deterministic synapses or stochastic synapses with fixed release probability. The fixed release probabilities model was chosen to have the same average release probability as the model with learned probabilities. (b) Best achievable ratio of information per energy for the three models from (a). Error bars in (a) and (b) denote the standard error for three repetitions of the experiment.

In addition, we investigate how stochastic release helps the network to lower metabolic costs. Intuitively, a natural way to save energy is to assign high release probabilities to synapses that are important to extract relevant information and to keep remaining synapses at a low release probability. Figure 2a shows that after learning, there are indeed few synapses with high release probabilities, while most release probabilities are kept low. We confirm that this sparsity develops independently of the initial value of release probabilities before learning, see Appendix 1—figure 1d. To test whether the synapses with high release probabilities are most relevant for solving the task we perform a lesion experiment. We successively remove synapses with low release probability and measure how well the lesioned network still solves the given task, see Figure 2b. As a control, we remove synapses in a random order independent of their release probability. We find that maintaining synapses with high release probabilities is significantly more important to network function than maintaining random ones. Moreover, we find, as expected, that synapses with high release probabilities consume considerably more energy than synapses with low release probability, see Figure 2c. This supports the hypothesis that the model identifies important synapses for the task at hand and spends more energy on these synapses while saving energy on irrelevant ones.

![Figure 2.](https://cdn.elifesciences.org/articles/69884/elife-69884-fig2-v2.jpg)

**Figure 2.:** (a) Histogram of release probabilities before and after learning, showing that the network relies on a sparse subset of synapses to find an energy-efficient solution. Dashed line at $p=0.9$ indicates our boundary for defining a release probability as ‘low’ or ‘high’. We confirmed that results are independent of initial value of release probabilities before learning (see Appendix 1—figure 2d). (b) Accuracy after performing the lesion experiment either removing synapses with low release probabilities first or removing weights randomly, suggesting that synapses with high release probability are most important for solving the task. (c) Distribution of synaptic energy demand for high and low release probability synapses. (d) Distribution of the Fisher information for high and low release probability synapses. It confirms the theoretical prediction that high release probability corresponds to high Fisher information. All panels show accumulated data for three repetitions of the experiment. Shaded regions in (b) show standard error.

We have seen that the network relies on a sparse subset of synapses to solve the task efficiently. However, sparsity is usually thought of on a neuronal level, with few neurons rather than few synapses encoding a given stimulus. Therefore, we quantify sparsity of our model on a neuronal level. For each neuron, we count the number of ‘important’ input- and output synapses, where we define ‘important’ to correspond to a release probability of at least $p=0.9$. Note that the findings are robust with respect to the precise value of $p$, see Figure 2a. We find that the distribution of important synapses per neuron is inhomogeneous and significantly different from a randomly shuffled baseline with a uniform distribution of active synapses (Kolmogorov-Smirnoff test, $D=0.505,p<0.01$), see Figure 3a. Thus, some neurons have disproportionately many important inputs, while others have very few, suggesting sparsity on a neuronal level. As additional quantification of this effect, we count the number of highly important neurons, where we define a neuron to be highly important if its number of active inputs is two standard deviations below or above the mean (mean and standard deviation from shuffled baseline). We find that our model network with presynaptic stochasticity has disproportionate numbers of highly important and unimportant neurons, see Figure 3b. Moreover, we check whether neurons with many important inputs tend to have many important outputs, indeed finding a correlation of $r=0.93$, see Figure 3c. These analyses all support the claim that the network is sparse not only on a synaptic but also on a neuronal level.

![Figure 3.](https://cdn.elifesciences.org/articles/69884/elife-69884-fig3-v2.jpg)

**Figure 3.:** (a) Histogram of the fraction of important input synapses per neuron for second layer neurons after learning for true and randomly shuffled connectivity (see Appendix 1—figure 2a for other layers). (b) Same data as (a), showing number of low/medium/high importance neurons, where high/low importance neurons have at least two standard deviations more/less important inputs than the mean of random connectivity. (c) Scatter plot of first layer neurons showing the number of important input and output synapses after learning on MNIST, Pearson correlation is $r=0.9390$ (see Appendix 1—figure 2b for other layers). Data in (a) and (c) are from one representative run, error bars in (b) show standard error over three repetitions.

Finally, we investigate how release probabilities evolve from a theoretical viewpoint under the proposed learning rule. Note that the evolution of release probabilities is a random process, since it depends on the random input to the network. Under mild assumptions, we show (Materials and methods) that release probabilities are more likely to increase for synapses with large Fisher information (In this context, the Fisher information is a measure of sensitivity of the network to changes in synapses, measuring how important preserving a given synapse is for network function.). Thus, synapses with large release probabilities will tend to have high Fisher information. We validate this theoretical prediction empirically, see Figure 2d.

### Presynaptically driven consolidation helps alleviate the stability-plasticity dilemma

While the biological mechanisms addressing the stability-plasticity dilemma are diverse and not fully understood, it has been demonstrated experimentally that preserving memories requires maintaining the synapses which encode these memories (Yang et al., 2009; Hayashi-Takagi et al., 2015; Cichon and Gan, 2015). In this context, theoretical work suggests that the Fisher information is a useful way to quantify which synapses should be maintained (Kirkpatrick et al., 2017). Inspired by these insights, we hypothesise that the synaptic importance encoded in release probabilities can be used to improve the network’s memory retention by selectively stabilising important synapses.

We formalise this hypothesis in our model by lowering the learning rate (plasticity) of synapses according to their importance (release probability). Concretely, the learning rate $η=η⁢(p_{i})$ used in (3) is scaled as follows

$$
η(p_{i})=η_{0}⋅(1−p_{i}).
$$

such that the learning rate is smallest for important synapses with high release probability. $η_{0}$ denotes a base learning rate that is shared by all synapses. We complement this consolidation mechanism by freezing the presynaptic release probabilities $p_{i}$ once they have surpassed a predefined threshold $p_{freeze}$. This ensures that a synapse whose presynaptic release probability was high for a previous task retains its release probability even when unused during consecutive tasks. In other words, the effects of presynaptic long-term depression (LTD) are assumed to act on a slower timescale than learning single tasks. Note that the freezing mechanism ensures that all synaptic strengths $w¯_{i}$ retain a small degree of plasticity, since the learning rate modulation factor $(1-p_{i})$ remains greater than 0.

To test our hypothesis that presynaptically driven consolidation allows the network to make improved stability-plasticity trade-offs, we sequentially present a number of tasks and investigate the networks behaviour. We mainly focus our analysis on a variation of the MNIST handwritten digit dataset, in which the network has to successively learn the parity of pairs of digits, see Figure 4a. Additional experiments are reported in the Appendix, see Appendix 1—table 1.

![Figure 4.](https://cdn.elifesciences.org/articles/69884/elife-69884-fig4-v2.jpg)

**Figure 4.:** (a) Schematic of the lifelong learning task Split MNIST. In the first task the model network is presented 0 s and 1 s, in the second task it is presented 2 s and 3 s, etc. For each task the model has to classify the inputs as even or odd. At the end of learning, it should be able to correctly classify the parity of all digits, even if a digit has been learned in an early task. (b) Accuracy of the first task when learning new tasks. Consolidation leads to improved memory preservation. (c) Average accuracies of all learned tasks. The presynaptic consolidation model is compared to a model without consolidation and two state-of-the-art machine learning algorithms. Differences to these models are significant in independent t-tests with either $p<0.05$ (marked with *) or with $p<0.01$ (marked with **). Dashed line indicates an upper bound for the network’s performance, obtained by training on all tasks simultaneously. Panels (b) and (c) show accumulated data for three repetitions of the experiment. Shaded regions in (b) and error bars in (c) show standard error.

First, we investigate whether presynaptic consolidation improves the model’s ability to remember old tasks. To this end, we track the accuracy on the first task over the course of learning, see Figure 4b. As a control, we include a model without consolidation and with deterministic synapses. While both models learn the first task, the model without consolidation forgets more quickly, suggesting that the presynaptic consolidation mechanism does indeed improve memory.

Next, we ask how increased stability interacts with the network’s ability to remain plastic and learn new tasks. To assess the overall trade-off between stability and plasticity, we report the average accuracy over all five tasks, see Figure 4c.

We find that the presynaptic consolidation model performs better than a standard model with deterministic synapses and without consolidation. In addition, we compare performance to two state-of-the art machine learning algorithms: The well-known algorithm Elastic Weight Consolidation (EWC) (Kirkpatrick et al., 2017) explicitly relies on the Fisher information and performs a separate consolidation phase after each task. Bayesian Gradient Descent (BGD) (Zeno et al., 2018) is a Bayesian approach that models synapses as distributions, but does not capture the discrete nature of synaptic transmission. The presynaptic consolidation mechanism performs better than both these state-of-the-art machine learning algorithms, see Figure 4c. Additional experiments in the Appendix suggest overall similar performance of Presynaptic Consolidation to BGD and similar or better performance than EWC.

To determine which components of our model contribute to its lifelong learning capabilities, we perform an ablation study, see Figure 5a. We aim to separate the effect of (1) consolidation mechanisms and (2) presynaptic plasticity.

![Figure 5.](https://cdn.elifesciences.org/articles/69884/elife-69884-fig5-v2.jpg)

**Figure 5.:** (a) Ablation of the Presynaptic Consolidation model on two different lifelong learning tasks, see full text for detailed description. Both presynaptic plasticity and synaptic stabilisation significantly improve memory. (b+c) Lifelong Learning in a Standard Perceptron akin to Figure 4b,c, showing the accuracy of the first task when learning consecutive tasks in (b) as well as the average over all five tasks after learning all tasks in (c). Error bars and shaded regions show standard error of three respectively ten repetitions, in (a), respectively (b+c). All pair-wise comparisons are significant, independent t-tests with $p<0.01$ (denoted by **) or with $p<0.05$ (denoted by *).

First, we remove the two consolidation mechanisms, learning rate modulation and freezing release probabilities, from the model with stochastic synapses. This yields a noticeable decrease in performance during lifelong learning, thus supporting the view that stabilising important synapses contributes to addressing the stability-plasticity dilemma.

Second, we aim to disentangle the effect of presynaptic plasticity from the consolidation mechanisms. We therefore introduce a control in which presynaptic plasticity but not consolidation is blocked. Concretely, the control has ‘ghost release probabilities’ $p~_{i}$ evolving according to Equation (4) and modulating plasticity according to Equation (5); but the synaptic release probability is fixed at 0.5. We see that this control performs worse than the original model with a drop in accuracy of 1.4 on Split MNIST ($t=3.44$, $p<0.05$) and a drop of accuracy of 5.6 on Permuted MNIST ($t=6.72,p<0.01$). This suggests that presynaptic plasticity, on top of consolidation, helps to stabilise the network. We believe that this can be attributed to the sparsity induced by the presynaptic plasticity which decreases overlap between different tasks.

The above experiments rely on a gradient-based learning rule for multilayer perceptrons. To test whether presynaptic consolidation can also alleviate stability-plasticity trade-offs in other settings, we study its effects on learning in a standard perceptron (Rosenblatt, 1958). We train the perceptron sequentially on five pattern memorisation tasks, see Materials and methods for full details. We find that the presynaptically consolidated perceptron maintains a more stable memory of the first task, see Figure 5b. In addition, this leads to an overall improved stability-plasticity trade-off, see Figure 5c and shows that the effects of presynaptic consolidation in our model extend beyond gradient-based learning.

## Discussion

### Main contribution

Information transmission in synapses is stochastic. While previous work has suggested that stochasticity allows to maximise the amount of information transmitted per unit of energy spent, this analysis has been restricted to single synapses. We argue that the relevant quantity to be considered is task-dependent information transmitted by entire networks. Introducing a simple model of the all-or-nothing nature of synaptic transmission, we show that presynaptic stochasticity enables networks to allocate energy more efficiently. We find theoretically as well as empirically that learned release probabilities encode the importance of weights for network function according to the Fisher information. Based on this finding, we suggest a novel computational role for presynaptic stochasticity in lifelong learning. Our experiments provide evidence that coupling information encoded in the release probabilities with modulated plasticity can help alleviate the stability-plasticity dilemma.

### Modelling assumptions and biological plausibility

#### Stochastic synaptic transmission

Our model captures the occurrence of synaptic failures by introducing a Bernoulli random variable governing whether or not neurotransmitter is released. Compared to classical models assuming deterministic transmission, this is one step closer to experimentally observed binomial transmission patterns, which are caused by multiple, rather than one, release sites between a given neuron and dendritic branch. Importantly, our simplified model accounts for the event that there is no postsynaptic depolarisation at all. Even in the presence of multiple release sites, this event has non-negligible probability: Data from cultured hippocampal neurons (Branco et al., 2008, Figure 2D) and the neocortex (Hardingham et al., 2010, Appendix 1—figure 2c) shows that the probability $(1-p)^{N}$ that none of $N$ release sites with release probability $p$ is active, is around 0.3–0.4 even for $N$ as large as 10. More recent evidence suggests an even wider range of values depending on the extracellular calcium concentration (Sakamoto et al., 2018).

#### Presynaptic long-term plasticity

A central property of our model builds on the observation that the locus of expression for long-term plasticity can both be presynaptic and postsynaptic (Larkman et al., 1992; Lisman and Raghavachari, 2006; Bayazitov et al., 2007; Sjöström et al., 2007; Bliss and Collingridge, 2013; Costa et al., 2017). The mechanisms to change either are distinct and synapse-specific (Yang and Calakos, 2013; Castillo, 2012), but how exactly pre- and postsynaptic forms of long-term potentiation (LTP) and long-term depression (LTD) interact is not yet fully understood (Monday et al., 2018). The induction of long-term plasticity is thought to be triggered postsynaptically for both presynaptic and postsynaptic changes (Yang and Calakos, 2013; Padamsey and Emptage, 2014) and several forms of presynaptic plasticity are known to require retrograde signalling (Monday et al., 2018), for example through nitric oxide or endocannabinoids (Heifets and Castillo, 2009; Andrade-Talavera et al., 2016; Costa et al., 2017). This interaction between pre- and postsynaptic sites is reflected by our learning rule, in which both pre- and postsynaptic changes are governed by postsynaptic updates and require communication between pre- and postsynapse. The proposed presynaptic updates rely on both presynaptic LTP and presynaptic LTD. At least one form of presynaptic long-term plasticity is known to be bidirectional switching from potentiation to depression depending on endocannabinoid transients (Cui et al., 2015; Cui et al., 2016).

#### Link between presynaptic release and synaptic stability

Our model suggests that increasing the stability of synapses with large release probability improves memory. Qualitatively, this is in line with observations that presynaptic boutons, which contain stationary mitochondria (Chang et al., 2006; Obashi and Okabe, 2013), are more stable than those which do not, both on short (Sun et al., 2013) and long timescales of at least weeks (Lees et al., 2019). Quantitatively, we find evidence for such a link by re-analysing data (Data was made publicly available in Costa et al., 2017). from Sjöström et al., 2001 for a spike-timing-dependent plasticity protocol in the rat primary visual cortex: Appendix 1—figure 4 shows that synapses with higher initial release probability are more stable than those with low release probabilities for both LTP and LTD.

#### Credit assignment

In our multilayer perceptron model, updates are computed using backpropagated gradients. Whether credit assignment in the brain relies on backpropagation – or more generally gradients – remains an active area of research, but several alternatives aiming to increase biological plausibility exist and are compatible with our model (Sacramento et al., 2018; Lillicrap et al., 2016; Lee et al., 2015). To check that the proposed mechanism can also operate without gradient information, we include an experiment with a standard perceptron and its gradient-free learning rule (Rosenblatt, 1958), see Figure 5b, c.

#### Correspondence to biological networks

We study general rate-based neural networks raising the question in which biological networks or contexts one might expect the proposed mechanisms to be at work. Our experiments suggest that improved energy efficiency can at least partly be attributed to the sparsification induced by presynaptic stochasticity (cf. Olshausen and Field, 2004). Networks which are known to rely on sparse representations are thus natural candidates for the dynamics investigated here. This includes a wide range of sensory networks (Perez-Orive et al., 2002; Hahnloser et al., 2002; Crochet et al., 2011; Quiroga et al., 2005) as well as areas in the hippocampus (Wixted et al., 2014; Lodge and Bischofberger, 2019).

In the context of lifelong learning, our learning rule provides a potential mechanism that helps to slowly incorporate new knowledge into a network with preexisting memories. Generally, the introduced consolidation mechanism could benefit the slow part of a complementary learning system as proposed by McClelland et al., 1995; Kumaran et al., 2016. Sensory networks in particular might utilize such a mechanism as they require to learn new stimuli while retaining the ability to recognise previous ones (Buonomano and Merzenich, 1998; Gilbert et al., 2009; Moczulska et al., 2013). Indeed, in line with the hypothesis that synapses with larger release probability are more stable, it has been observed that larger spines in the mouse barrel cortex are more stable. Moreover, novel experiences lead to the formation of new, stable spines, similar to our findings reported in Appendix 1—figure 3b.

### Related synapse models

#### Probabilistic synapse models

The goal of incorporating and interpreting noise in models of neural computation is shared by many computational studies. Inspired by a Bayesian perspective, neural variability is often interpreted as representing uncertainty (Ma et al., 2006; Fiser et al., 2010; Kappel et al., 2015; Haefner et al., 2016), or as a means to prevent overfitting (Wan et al., 2013). The Bayesian paradigm has been applied directly to variability of individual synapses in neuroscience (Aitchison et al., 2014; Aitchison and Latham, 2015; Aitchison et al., 2021) and machine learning (Zeno et al., 2018). It prescribes decreasing the plasticity of synapses with low posterior variance. A similiar relationship can be shown to hold for our model as described in the Material and Methods. In contrast to common Bayesian interpretations (Zeno et al., 2018; Aitchison and Latham, 2015; Kappel et al., 2015) which model release statistics as Gaussians and optimise complex objectives (see also Llera-Montero et al., 2019) our simple proposal represents the inherently discrete nature of synaptic transmission more faithfully.

#### Complex synapse models

In the context of lifelong learning, our model’s consolidation mechanism is similar to Elastic Weight Consolidation (EWC) (Kirkpatrick et al., 2017), which explicitly relies on the Fisher information to consolidate synapses. Unlike EWC, our learning rule does not require a task switch signal and does not need a separate consolidation phase. Moreover, our model can be interpreted as using distinct states of plasticity to protect memories. This general idea is formalised and analysed thoroughly by theoretical work on cascade models of plasticity (Fusi et al., 2005; Roxin and Fusi, 2013; Benna and Fusi, 2016). The resulting model (Benna and Fusi, 2016) has also been shown to be effective in lifelong learning settings (Kaplanis et al., 2018).

### Synaptic importance may govern energy-information trade-offs

Energy constraints are widely believed to be a main driver of evolution (Niven and Laughlin, 2008). From brain size (Isler and van Schaik, 2009; Navarrete et al., 2011), to wiring cost (Chen et al., 2006), down to ion channel properties (Alle et al., 2009; Sengupta et al., 2010), presynaptic transmitter release (Savtchenko et al., 2013) and postsynaptic conductance (Harris et al., 2015), various components of the nervous system have been shown to be optimal in terms of their total metabolic cost or their metabolic cost per bit of information transmitted.

Crucially, there is evidence that the central nervous system operates in varying regimes, making different trade-offs between synaptic energy demand and information transmission: Perge et al., 2009; Carter and Bean, 2009; Hu and Jonas, 2014 all find properties of the axon (thickness, sodium channel properties), which are suboptimal in terms of energy per bit of information. They suggest that these inefficiencies occur to ensure fast transmission of highly relevant information.

We propose that a similar energy/information trade-off could govern network dynamics preferentially allocating more energy to the most relevant synapses for a given task. Our model relies on a simple, theoretically justified learning rule to achieve this goal and leads to overall energy savings. Neither the trade-off nor the overall savings can be accounted for by previous frameworks for energy-efficient information transmission at synapses (Levy and Baxter, 2002; Harris et al., 2012).

This view of release probabilities and related metabolic cost provides a way to make the informal notion of ‘synaptic importance’ concrete by measuring how much energy is spent on a synapse. Interestingly, our model suggests that this notion is helpful beyond purely energetic considerations and can in fact help to maintain memories during lifelong learning.

## Materials and methods

### Summary of learning rule

Our learning rule has two components, an update for the presynaptic release probability $p_{i}$ and an update for the postsynaptic strength $m_{i}$. The update of the synaptic strength $m_{i}$ is defined implicitly through updating the expected synaptic strength $w¯$

$$
w¯_{i}^{(t+1)}=w¯_{i}^{(t)}−ηg_{i},whereg_{i}=\frac{∂L(w¯^{(t)},p^{(t)})}{∂w¯_{i}^{(t)}}
$$

and the presynaptic update is given by

$$
p_{i}^{(t+1)}={p_{i}^{(t)}+p_{up},if|g_{i}|>g_{_{lim}},p_{i}^{(t)}−p_{down},if|g_{i}|\leqg_{_{lim}}.
$$

This leads to the following explicit update rule for the synaptic strength $m_{i}=\frac{w¯_{i}}{p_{i}}$

$$
m_{i}^{(t+1)}=\frac{1}{p_{i}^{(t+1)}}(p_{i}^{(t)}m_{i}^{(t)}−ηg_{i})
$$



$$
=\frac{p_{i}^{(t)}}{p_{i}^{(t+1)}}⁢m_{i}^{(t)}-\frac{η}{p_{i}^{(t+1)}⁢p_{i}^{(t)}}⁢\frac{\partial⁡L⁢(m^{(t)},p^{(t)})}{\partial⁡m_{i}^{(t)}}
$$

where we used the chain rule to rewrite $g_{i}=\frac{\partial⁡L}{\partial⁡w_{i}¯}=\frac{\partial⁡L}{\partial⁡m_{i}}⋅\frac{\partial⁡m_{i}}{\partial⁡w_{i}¯}=\frac{\partial⁡L}{\partial⁡m_{i}}⋅\frac{1}{p_{i}}$. For the lifelong learning experiment, we additionally stabilise high release probability synapses by multiplying the learning rate by $(1-p_{i})$ for each synapse and by freezing release probabilities (but not strengths) when they surpass a predefined threshold $p_{freeze}$.

### Theoretical analysis of presynaptic learning rule

As indicated in the results section the release probability $p_{i}$ is more likely to be large when the Fisher information of the synaptic strength $w_{i}$ is large as well. This provides a theoretical explanation to the intuitive correspondence between release probability and synaptic importance. Here, we formalise this link starting with a brief review of the Fisher information.

#### Fisher information

The Fisher information is a measure for the networks sensitivity to changes in parameters. Under additional assumptions it is equal to the Hessian of the loss function (Pascanu and Bengio, 2013; Martens, 2014), giving an intuitive reason why synapses with high Fisher information should not be changed much if network function is to be preserved.

Formally, for a model with parameter vector $\theta$ predicting a probability distribution $f_{\theta}⁢(X,y)$ for inputs $X$ and labels $y$ drawn from a joint distribution $𝒟$, the Fisher information matrix is defined as

$$
E_{X∼𝒟}E_{y∼f_{\theta}(y∣X)}[(\frac{∂ln⁡f_{\theta}(X,y)}{∂\theta})(\frac{∂ln⁡f_{\theta}(X,y)}{∂\theta})^{T}].
$$

Note that this expression is independent of the actual labels $y$ of the dataset and that instead we sample labels from the model’s predictions. If the model makes correct predictions, we can replace the second expectation, which is over $y∼f_{\theta}⁢(y∣X)$, by the empirical labels $y$ of the dataset for an approximation called the Empirical Fisher information. If we further only consider the diagonal entries – corresponding to a mean-field approximation – and write $g_{i}⁢(X,y)=\frac{\partial⁡ln⁡f_{\theta}⁢(X,y)}{\partial⁡\theta_{i}}$ we obtain the following expression for the $i$-th entry of the diagonal Empirical Fisher information:

$$
F_{i}=𝔼_{X,y∼𝒟}⁢[g_{i}⁢(X,y)^{2}].
$$

Note that this version of the Fisher information relies on the same gradients that are used to update the parameters of the multilayer perceptron, see Equations (3), (4).

Under the assumption that the learned probability distribution $f(⋅∣X,\theta)$ equals the real probability distribution, the Fisher information equals the Hessian of the cross entropy loss (i.e. the negative log-probabilities) with respect to the model parameters (Pascanu and Bengio, 2013; Martens, 2014). The Fisher information was previously used in machine learning to enable lifelong learning (Kirkpatrick et al., 2017; Huszár, 2018) and it has been shown that other popular lifelong learning methods implicitly rely on the Fisher information (Benzing, 2020).

#### Link between release probabilities and Fisher information

We now explain how our learning rule for the release probability is related to the Fisher information. For simplicity of exposition, we focus our analysis on a particular sampled subnetwork with deterministic synaptic strengths. Recall that update rule (4) for release probabilities increases the release probability, if the gradient magnitude $|g_{i}|$ is above a certain threshold, $g_{i}>|g_{lim}|$, and decreases them otherwise. Let us denote by $p_{i}^{+}$ the probability that the $i$-th release probability is increased. Then

$$
p_{i}^{+}:=Pr[|g_{i}|>g_{lim}]=Pr[g_{i}^{2}>g_{lim}^{2}],
$$

where the probability space corresponds to sampling training examples. Note that $𝔼⁢[g_{i}^{2}]=F_{i}$ by definition of the Empirical Fisher information $F_{i}$. So if we assume that $Pr⁡[g_{i}^{2}>g_{lim}^{2}]$ depends monotonically on $𝔼⁢[g_{i}^{2}]$ then we already see that $p_{i}^{+}$ depends monotonically on $F_{i}$. This in turn implies that synapses with a larger Fisher information are more likely to have a large release probability, which is what we claimed. We now discuss the assumption made above.

### Assumption: Pr[gi2>glim2] depends monotonically on 𝔼⁢[gi2]

While this assumption is not true for arbitrary distributions of $g$, it holds for many commonly studied parametric families and seems likely to hold (approximately) for realistic, non-adversarially chosen distributions. For example, if each $g_{i}$ follows a normal distribution $g_{i}∼𝒩⁢(\mu_{i},\sigma_{i}^{2})$ with varying $\sigma_{i}$ and $\sigma_{i}≫\mu_{i}$, then

$$
F_{i}=𝔼⁢[g_{i}^{2}]≈\sigma_{i}^{2}
$$

and

$$
p_{i}^{+}=Pr[g_{i}^{2}>g_{lim}^{2}]≈erfc(\frac{g_{lim}}{\sigma_{i}\sqrt{2}})
$$

so that $p_{i}^{+}$ is indeed monotonically increasing in $F_{i}$. Similar arguments can be made for example for a Laplace distribution, with scale larger than mean.

### Link between learning rate modulation and Bayesian updating

Recall that we multiply the learning rate of each synapse by $(1-p_{i})$, see Equation (5). This learning rate modulation can be related to the update prescribed by Bayesian modelling. As shown before, synapses with large Fisher information tend to have large release probability, which results in a decrease of the plasticity of synapses with large Fisher information. We can treat the (diagonal) Fisher information as an approximation of the posterior precision based on a Laplace approximation of the posterior likelihood (Kirkpatrick et al., 2017) which exploits that the Fisher information approaches the Hessian of the loss as the task gets learned (Martens, 2014). Using this relationship, our learning rate modulation tends to lower the learning rate of synapses with low posterior variance as prescribed by Bayesian modelling.

### Practical approximation

The derivation above assumes that each gradient $g$ is computed using a single input, so that $𝔼⁢[g^{2}]$ equals the Fisher information. While this may be the biologically more plausible setting, in standard artificial neural network (ANN) training the gradient is averaged across several inputs (mini-batches). Despite this modification, $g^{2}$ remains a good, and commonly used, approximation of the Fisher, see for example Khan et al., 2018; Benzing, 2020.

### Perceptron for lifelong learning

To demonstrate that our findings on presynaptic stochasticity and plasticity are applicable to other models and learning rules, we include experiments for the standard perceptron (Rosenblatt, 1958) in a lifelong learning setting.

#### Model

The perceptron is a classical model for a neuron with multiple inputs and threshold activation function. It is used to memorise the binary labels of a number of input patterns where input patterns are sampled uniformly from ${-1,1}^{N}$ and their labels are sampled uniformly from ${-1,1}$. Like in ANNs, the output neuron of a perceptron computes a weighted sum of its inputs followed by nonlinear activation $\sigma⁢(⋅)$:

$$
a^{post}⏟\frac{postsynaptic}{activation}=\sigma(\sumi=1nw_{i}a_{i}^{pre}⏟\frac{i-thpresynaptic}{input}).
$$

The only difference to the ANN model is that the nonlinearity is the sign function and that there is only one layer. We model each synapse $w_{i}$ as a Bernoulli variable $r_{i}$ with synaptic strength $m_{i}$ and release probability $p_{i}$ just as before, see Equation (1). The expected strengths $w¯_{i}$ are learned according to the standard perceptron learning rule (Rosenblatt, 1958). The only modification we make is averaging weight updates across 5 inputs, rather than applying an update after each input. Without this modification, the update size $g_{i}$ for each weight $w_{i}$ would be constant according to the perceptron learning rule. Consequently, our update rule for $p_{i}$ would not be applicable. However, after averaging across five patterns we can apply the same update rule for $p_{i}$ as previously, see Equation (4), and also use the same learning rate modification, see Equation (5). We clarify that $g_{i}$ now refers to the update of expected strength $w¯_{i}$. In the case of ANN this is proportional to the gradient, while in the case of the non-differentiable perceptron it has no additional interpretation.

#### Experiments

For the lifelong learning experiments, we used five tasks, each consisting of 100 randomly sampled and labelled patterns of size $N=1000$. We compared the perceptron with learned stochastic weights to a standard perceptron. For the standard perceptron, we also averaged updates across five patterns. Both models were sequentially trained on five tasks, using 25 passes through the data for each task.

We note that for more patterns, when the perceptron gets closer to its maximum capacity of $2⁢N$, the average accuracies of the stochastic and standard perceptron become more similar, suggesting that the benefits of stochastic synapses occur when model capacity is not fully used.

As metaplasticity parameters we used $g_{lim}=0.1,p_{up}=p_{down}=0.2$ and $p_{min}=0.25,p_{freeze}=0.9$. These were coarsely tuned on an analogous experiment with only two tasks instead of five.

### Experimental setup

#### Code availability

Code for all experiments is publicly available at github.com/smonsays/presynaptic-stochasticity (Schug, 2021, copy archived at swh:1:rev:de0851773cd1375b885dcdb18e711a2fb6eb06a4).

#### Metaplasticity parameters

Our method has a number of metaplasticity parameters, namely $p_{up}$, $p_{down}$, $g_{lim}$ and the learning rate $η$. For the lifelong learning experiments, there is an additional parameter $p_{freeze}$. For the energy experiments, we fix $p_{up}=p_{down}=0.07$, $g_{lim}=0.001$ and choose $η=0.05$ based on coarse, manual tuning. For the lifelong learning experiments, we choose $η_{0}\in{0.01,0.001}$ and optimise the remaining metaplasticity parameters through a random search on one task, namely Permuted MNIST, resulting in $p_{up}=0.0516$, $p_{down}=0.0520$ and $g_{lim}=0.001$. We use the same fixed parametrisation for all other tasks, namely Permuted Fashion MNIST, Split MNIST and Split Fashion MNIST (see below for detailed task descriptions). For the ablation experiment in Figure 5a, metaplasticity parameters were re-optimised for each ablation in a random search to ensure a fair, meaningful comparison.

#### Model robustness

We confirmed that the model is robust with respect to the exact choice of parameters. For the energy experiments, de- or increasing $p_{up},p_{down}$ by 25 does not qualitatively change results.

For the lifelong learning experiment, the chosen tuning method is a strong indicator of robustness: The metaplasticitiy parameters are tuned on one setup (Permuted MNIST) and then transferred to others (Split MNIST, Permuted and Split Fashion MNIST). The results presented in Appendix 1—table 1 show that the parameters found in one scenario are robust and carry over to several other settings. We emphasise that the differences between these scenarios are considerable. For example, for permuted MNIST consecutive input distributions are essentially uncorrelated by design, while for Split (Fashion) MNIST input distributions are strongly correlated. In addition, from MNIST to Fashion MNIST the number of ‘informative’ pixels changes drastically.

#### Lifelong learning tasks

For the lifelong learning experiments, we tested our method as well as baselines in several scenarios on top of the Split MNIST protocol described in the main text.

### Permuted MNIST

In the Permuted MNIST benchmark, each task consists of a random but fixed permutation of the input pixels of all MNIST images (Goodfellow et al., 2013). We generate 10 tasks using this procedure and present them sequentially without any indication of task boundaries during training. A main reason to consider the Permuted MNIST protocol is that it generates tasks of equal difficulty.

### Permuted and split fashion MNIST

Both the Split and Permuted protocol can be applied to other datasets. We use them on the Fashion MNIST dataset (Xiao et al., 2017) consisting of 60,000 greyscale images of 10 different fashion items with $28\times28$ pixels.

### Continuous permuted MNIST

We carry out an additional experiment on the continuous Permuted MNIST dataset (Zeno et al., 2018). This is a modified version of the Permuted MNIST dataset which introduces a smooth transition period between individual tasks where data from both distributions is mixed. It removes the abrupt change between tasks and allows us to investigate if our method depends on such an implicit task switch signal. We observe a mean accuracy over all tasks of $0.8539\pm0.006$ comparable to the non-continuous case suggesting that our method does not require abrupt changes from one task to another.

#### Neural network training

Our neural network architecture consists of two fully connected hidden layers of 200 neurons without biases with rectified linear unit activation functions $\sigma⁢(x)$. The final layer uses a softmax and cross-entropy loss. Network weights were initialised according to the PyTorch default for fully connected layers, which is similar to Kaiming uniform initialisation (Glorot and Bengio, 2010; He et al., 2015) but divides weights by an additional factor of √6. We use standard stochastic gradient descent to update the average weight $w¯_{i}$ only altered by the learning rate modulation described for the lifelong learning experiments. We use a batch size of 100 and train each task for 10 epochs in the lifelong learning setting. In the energy-information experiments we train the model for 50 epochs.
