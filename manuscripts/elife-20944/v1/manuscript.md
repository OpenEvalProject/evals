# Rules and mechanisms for efficient two-stage learning in neural circuits

## Authors

- Tiberiu Teşileanu<sup>1</sup> ([ORCID: 0000-0003-3107-3088](https://orcid.org/0000-0003-3107-3088))
- Bence Ölveczky<sup>3</sup> ([ORCID: 0000-0003-2499-2705](https://orcid.org/0000-0003-2499-2705))
- Vijay Balasubramanian<sup>1</sup> ([ORCID: 0000-0002-6497-3819](https://orcid.org/0000-0002-6497-3819)) †

### Affiliations

1. Initiative for the Theoretical Sciences CUNY Graduate Center New York United States
2. David Rittenhouse Laboratories, University of Pennsylvania Philadelphia United States
3. Department of Organismic and Evolutionary Biology and Center for Brain Science Harvard University Cambridge United States
4. Theoretische Natuurkunde Vrije Universiteit Brussel & International Solvay Institutes Brussels Belgium

† Corresponding author

## Abstract

Trial-and-error learning requires evaluating variable actions and reinforcing successful variants. In songbirds, vocal exploration is induced by LMAN, the output of a basal ganglia-related circuit that also contributes a corrective bias to the vocal output. This bias is gradually consolidated in RA, a motor cortex analogue downstream of LMAN. We develop a new model of such two-stage learning. Using stochastic gradient descent, we derive how the activity in ‘tutor’ circuits (e.g., LMAN) should match plasticity mechanisms in ‘student’ circuits (e.g., RA) to achieve efficient learning. We further describe a reinforcement learning framework through which the tutor can build its teaching signal. We show that mismatches between the tutor signal and the plasticity mechanism can impair learning. Applied to birdsong, our results predict the temporal structure of the corrective bias from LMAN given a plasticity rule in RA. Our framework can be applied predictively to other paired brain areas showing two-stage learning.

## Introduction

Two-stage learning has been described in a variety of different contexts and neural circuits. During hippocampal memory consolidation, recent memories, that are dependent on the hippocampus, are transferred to the neocortex for long-term storage (Frankland and Bontempi, 2005). Similarly, the rat motor cortex provides essential input to sub-cortical circuits during skill learning, but then becomes dispensable for executing certain skills (Kawai et al., 2015). A paradigmatic example of two-stage learning occurs in songbirds learning their courtship songs (Andalman and Fee, 2009; Turner and Desmurget, 2010; Warren et al., 2011). Zebra finches, commonly used in birdsong research, learn their song from their fathers as juveniles, and keep the same song for life (Immelmann, 1969).

The birdsong circuit has been extensively studied; see Figure 1A for an outline. Area HVC is a timebase circuit, with projection neurons that fire sparse spike bursts in precise synchrony with the song (Hahnloser et al., 2002; Lynch et al., 2016; Picardo et al., 2016). A population of neurons from HVC projects to the robust nucleus of the arcopallium (RA), a pre-motor area, which then projects to motor neurons controlling respiratory and syringeal muscles (Leonardo and Fee, 2005; Simpson and Vicario, 1990; Yu and Margoliash, 1996). A second input to RA comes from the lateral magnocellular nucleus of the anterior nidopallium (LMAN). Unlike HVC and RA activity patterns, LMAN spiking is highly variable across different renditions of the song (Kao et al., 2008; Ölveczky et al., 2005). LMAN is the output of the anterior forebrain pathway, a circuit involving the song-specialized basal ganglia (Perkel, 2004).

![Figure 1.](https://cdn.elifesciences.org/articles/20944/elife-20944-fig1-v1.jpg)

**Figure 1.:** (A) Diagram of the major brain regions involved in birdsong. (B) Conceptual model inspired by the birdsong system. The line from output to tutor is dashed because the reinforcement signal can reach the tutor either directly or, as in songbirds, indirectly. (C) Plasticity rule measured in bird RA (measurement done in slice). When an HVC burst leads an LMAN burst by about $100⁢ms$, the HVC–RA synapse is strengthened, while coincident firing leads to suppression. Figure adapted from Mehaffey and Doupe (2015). (D) Plasticity rule in our model that mimics the Mehaffey and Doupe (2015) rule.

Because of the variability in its activity patterns, it was thought that LMAN’s role was simply to inject variability into the song (Ölveczky et al., 2005). The resulting vocal experimentation would enable reinforcement-based learning. For this reason, prior models tended to treat LMAN as a pure Poisson noise generator, and assume that a reward signal is received directly in RA (Fiete et al., 2007). More recent evidence, however, suggests that the reward signal reaches Area X, the song-specialized basal ganglia, rather than RA (Gadagkar et al., 2016; Hoffmann et al., 2016; Kubikova et al., 2010). Taken together with the fact that LMAN firing patterns are not uniformly random, but rather contain a corrective bias guiding plasticity in RA (Andalman and Fee, 2009; Warren et al., 2011), this suggests that we should rethink our models of song acquisition.

Here we build a general model of two-stage learning where one neural circuit ‘tutors’ another. We develop a formalism for determining how the teaching signal should be adapted to a specific plasticity rule, to best instruct a student circuit to improve its performance at each learning step. We develop analytical results in a rate-based model, and show through simulations that the general findings carry over to realistic spiking neurons. Applied to the vocal control circuit of songbirds, our model reproduces the observed changes in the spiking statistics of RA neurons as juvenile birds learn their song. Our framework also predicts how the LMAN signal should be adapted to properties of RA synapses. This prediction can be tested in future experiments.

Our approach separates the mechanistic question of how learning is implemented from what the resulting learning rules are. We nevertheless demonstrate that a simple reinforcement learning algorithm suffices to implement the learning rule we propose. Our framework makes general predictions for how instructive signals are matched to plasticity rules whenever information is transferred between different brain regions.

## Results

### Model

We considered a model for information transfer that is composed of three sub-circuits: a conductor, a student, and a tutor (see Figure 1B). The conductor provides input to the student in the form of temporally precise patterns. The goal of learning is for the student to convert this input to a predefined output pattern. The tutor provides a signal that guides plasticity at the conductor–student synapses. For simplicity, we assumed that the conductor always presents the input patterns in the same order, and without repetitions. This allowed us to use the time $t$ to label input patterns, making it easier to analyze the on-line learning rules that we studied. This model of learning is based on the logic implemented by the vocal circuits of the songbird (Figure 1A). Relating this to the songbird, the conductor is HVC, the student is RA, and the tutor is LMAN. The song can be viewed as a mapping between clock-like HVC activity patterns and muscle-related RA outputs. The goal of learning is to find a mapping that reproduces the tutor song.

Birdsong provides interesting insights into the role of variability in tutor signals. If we focus solely on information transfer, the tutor output need not be variable; it can deterministically provide the best instructive signal to guide the student. This, however, would require the tutor to have a detailed model of the student. More realistically, the tutor might only have access to a scalar representation of how successful the student rendition of the desired output is, perhaps in the form of a reward signal. A tutor in this case has to solve the so-called ‘credit assignment problem’—it needs to identify which student neurons are responsible for the reward. A standard way to achieve this is to inject variability in the student output and reinforce the firing of neurons that precede reward (see for example (Fiete et al., 2007) in the birdsong context). Thus, in our model, the tutor has a dual role of providing both an instructive signal and variability, as in birdsong.

We described the output of our model using a vector ya⁢(t) where a indexed the various output channels (Figure 2A). In the context of motor control a might index the muscle to be controlled, or, more abstractly, different features of the motor output, such as pitch and amplitude in the case of birdsong. The output ya⁢(t) was a function of the activity of the student neurons sj⁢(t). The student neurons were in turn driven by the activity of the conductor neurons ci⁢(t). The student also received tutor signals to guide plasticity; in the songbird, the guiding signals for each RA neuron come from several LMAN neurons (Canady et al., 1988; Garst-Orozco et al., 2014; Herrmann and Arnold, 1991). In our model, we summarized the net input from the tutor to the jth student neuron as a single function gj⁢(t).

![Figure 2.](https://cdn.elifesciences.org/articles/20944/elife-20944-fig2-v1.jpg)

**Figure 2.:** (A) Conductor neurons fire precisely-timed bursts, similar to HVC neurons in songbirds. Conductor and tutor activities, $c⁢(t)$ and $g⁢(t)$, provide excitation to student neurons, which integrate these inputs and respond linearly, with activity $s⁢(t)$. Student neurons also receive a constant inhibitory input, $x_{inh}$. The output neurons linearly combine the activities from groups of student neurons using weights $M_{a⁢j}$. The linearity assumptions were made for mathematical convenience but are not essential for our qualitative results (see Appendix). (B). The conductor–student synaptic weights $W_{i⁢j}$ are updated based on a plasticity rule that depends on two parameters, $\alpha$ and $\beta$, and two timescales, $\tau_{1}$ and $\tau_{2}$ (see Equation (1) and Materials and methods). The tutor signal enters this rule as a deviation from a constant threshold $\theta$. The figure shows how synaptic weights change ($Δ⁢W$) for a student neuron that receives a tutor burst and a conductor burst separated by a short lag. Two different choices of plasticity parameters are illustrated in the case when the threshold $\theta=0$. (C) The amount of mismatch between the system’s output and the target output is quantified using a loss (error) function. The figure sketches the loss landscape obtained by varying the synaptic weights $W_{i⁢j}$ and calculating the loss function in each case (only two of the weight axes are shown). The blue dot shows the lowest value of the loss function, corresponding to the best match between the motor output and the target, while the orange dot shows the starting point. The dashed line shows how learning would proceed in a gradient descent approach, where the weights change in the direction of steepest descent in the loss landscape.

We started with a rate-based implementation of the model (Figure 2A) that was analytically tractable but averaged over tutor variability. We further took the neurons to be in a linear operating regime (Figure 2A) away from the threshold and saturation present in real neurons. We then relaxed these conditions and tested our results in spiking networks with initial parameters selected to imitate measured firing patterns in juvenile birds prior to song learning. The student circuit in both the rate-based and spiking models included a global inhibitory signal that helped to suppress excess activity driven by ongoing conductor and tutor input. Such recurrent inhibition is present in area RA of the bird (Spiro et al., 1999). In the spiking model we implemented the suppression as an activity-dependent inhibition, while for the analytic calculations we used a constant negative bias for the student neurons.

### Learning in a rate-based model

Learning in our model was enabled by plasticity at the conductor–student synapses that was modulated by signals from tutor neurons (Figure 2B). Many different forms of such hetero-synaptic plasticity have been observed. For example, in rate-based synaptic plasticity high tutor firing rates lead to synaptic potentiation and low tutor firing rates lead to depression (Chistiakova and Volgushev, 2009; Chistiakova et al., 2014). In timing-dependent rules, such as the one recently measured by Mehaffey and Doupe (2015) in slices of zebra finch RA (see Figure 1C), the relative arrival times of spike bursts from different input pathways set the sign of synaptic change. To model learning that lies between these rate and timing-based extremes, we introduced a class of plasticity rules governed by two parameters $\alpha$ and $\beta$ (see also Materials and methods and Figure 2B):

$$
\frac{dW_{ij}}{dt}=ηc~_{i}(t)(g_{j}(t)−\theta),(1)c~_{i}(t)=\int_{0}^{t}dt^{′}c_{i}(t^{′})[\frac{\alpha}{\tau_{1}}e^{−(t−t^{′})/\tau_{1}}−\frac{\beta}{\tau_{2}}e^{−(t−t^{′})/\tau_{2}}],
$$

where $W_{i⁢j}$ is the weight of the synapse from the $i$th conductor to the $j$th student neuron, $η$ is a learning rate, $\theta$ is a threshold on the firing rate of tutor neurons, and $\tau_{1}$ and $\tau_{2}$ are timescales associated with the plasticity. This is similar to an STDP rule, except that the dependence on postsynaptic activity was replaced by dependence on the input from the tutor. Thus plasticity acts heterosynaptically, with activation of the tutor–student synapse controlling the change in the conductor–student synaptic weight. The timescales $\tau_{1}$ and $\tau_{2}$, as well as the coefficients $\alpha$ and $\beta$, can be thought of as effective parameters describing the plasticity observed in student neurons. As such, they do not necessarily have a simple correspondence in terms of the biochemistry of the plasticity mechanism, and the framework we describe here is not specifically tied to such an interpretation.

If we set $\alpha$ or $\beta$ to zero in our rule, Equation (1), the sign of the synaptic change is determined solely by the firing rate of the tutor $g_{j}⁢(t)$ as compared to a threshold, reproducing the rate rules observed in experiments. When $\alpha/\beta≈1$, if the conductor leads the tutor, potentiation occurs, while coincident signals lead to depression (Figure 2B), which mimics the empirical findings from Mehaffey and Doupe (2015). For general $\alpha$ and $\beta$, the sign of plasticity is controlled by both the firing rate of the tutor relative to the baseline, and by the relative timing of tutor and conductor. The overall scale of the parameters $\alpha$ and $\beta$ can be absorbed into the learning rate $η$ and so we set $\alpha-\beta=1$ in all our simulations without loss of generality (see Materials and methods). Note that if $\alpha$ and $\beta$ are both large, it can be that $\alpha-\beta=1$ and $\alpha/\beta≈1$ also, as needed to realize the Mehaffey and Doupe (2015) curve.

We can ask how the conductor–student weights $W_{i⁢j}$ (Figure 2A) should change in order to best improve the output $y_{a}⁢(t)$. We first need a loss function $L$ that quantifies the distance between the current output $y_{a}⁢(t)$ and the target $y¯_{a}⁢(t)$ (Figure 2C). We used a quadratic loss function, but other choices can also be incorporated into our framework (see Appendix). Learning should change the synaptic weights so that the loss function is minimized, leading to a good rendition of the targeted output. This can be achieved by changing the synaptic weights in the direction of steepest descent of the loss function (Figure 2C).

We used the synaptic plasticity rule from Equation (1) to calculate the overall change of the weights, $Δ⁢W_{i⁢j}$, over the course of the motor program. This is a function of the time course of the tutor signal, $g_{j}⁢(t)$. Not every choice for the tutor signal leads to motor output changes that best improve the match to the target. Imposing the condition that these changes follow the gradient descent procedure described above, we derived the tutor signal that was best matched to the student plasticity rule (detailed derivation in Materials and methods). The result is that the best tutor for driving gradient descent learning must keep track of the motor error

$$
ϵ_{j}⁢(t)=\sumaM_{a⁢j}⁢(y_{a}⁢(t)-y¯_{a}⁢(t))
$$

integrated over the recent past

$$
g_{j}(t)=\theta−\frac{ζ}{\alpha−\beta}\frac{1}{\tau_{tutor}}\int_{0}^{t}ϵ_{j}(t^{′})e^{−(t−t^{′})/\tau_{tutor}}dt^{′},
$$

where $M_{a⁢j}$ are the weights describing the linear relationship between student activities and motor outputs (Figure 2A) and $ζ$ is a learning rate. Moreover, for effective learning, the parameter $\tau_{tutor}$ appearing in Equation (3), which quantifies the timescale on which error information is integrated into the tutor signal, should be related to the synaptic plasticity parameters according to

$$
\tau_{tutor}=\tau_{tutor}^{∗},where\tau_{tutor}^{∗}≡\frac{\alpha\tau_{1}−\beta\tau_{2}}{\alpha−\beta}
$$

is the optimal timescale for the error integration.

In short, motor learning with a heterosynaptic plasticity rule requires convolving the motor error with a kernel whose timescale is related to the structure of the plasticity rule, but is otherwise independent of the motor program. As explained in more detail in Materials and methods, this result is derived in an approximation that assumes that the tutor signal does not vary significantly over timescales of the order of the student timescales $\tau_{1}$ and $\tau_{2}$. Given Equation (4), this implies that we are assuming $\tau_{tutor}≫\tau_{1,2}$. This is a reasonable approximation because variations in the tutor signal that are much faster than the student timescales $\tau_{1,2}$ have little effect on learning since the plasticity rule (1) blurs conductor inputs over these timescales.

### Matched vs. unmatched learning

Our rate-based model predicts that when the timescale on which error information is integrated into the tutor signal ($\tau_{tutor}$) is matched to the student plasticity rule as described above, learning will proceed efficiently. A mismatched tutor should slow or disrupt convergence to the desired output. To test this, we numerically simulated the birdsong circuit using the linear model from Figure 2A with a motor output $y_{a}$ filtered to more realistically reflect muscle response times (see Materials and methods). We selected plasticity rules as described in Equation (1) and Figure 2B and picked a target output pattern to learn. The target was chosen to resemble recordings of air-sac pressure from singing zebra finches in terms of smoothness and characteristic timescales (Veit et al., 2011), but was otherwise arbitrary. In our simulations, the output typically involved two different channels, each with its own target, but for brevity, in figures we typically showed the output from only one of these.

For our analytical calculations, we made a series of assumptions and approximations meant to enhance tractability, such as linearity of the model and a focus on the regime $\tau_{tutor}≫\tau_{1,2}$. These constraints can be lifted in our simulations, and indeed below we test our numerical model in regimes that go beyond the approximations made in our derivation. In many cases, we found that the basic findings regarding tutor–student matching from our analytical model remain true even when some of the assumptions we used to derive it no longer hold.

We tested tutors that were matched or mismatched to the plasticity rule to see how effectively they instructed the student. Figure 3A and online Video 1 show convergence with a matched tutor when the sign of plasticity is determined by the tutor’s firing rate. We see that the student output rapidly converged to the target. Figure 3B and online Video 2 show convergence with a matched tutor when the sign of plasticity is largely determined by the relative timing of the tutor signal and the student output. We see again that the student converged steadily to the desired output, but at a somewhat slower rate than in Figure 3A.

![Figure 3.](https://cdn.elifesciences.org/articles/20944/elife-20944-fig3-v1.jpg)

**Figure 3.:** (A) Error trace showing how the average motor error evolved with the number of repetitions of the motor program for a rate-based ($\alpha=0$) plasticity rule paired with a matching tutor. (See online Video 1). (B) The error trace and final motor output shown for a timing-based learning rule matched by a tutor with a long integration timescale. (See online Video 2.) In both A and B the inset shows the final motor output for one of the two output channels (thick orange line) compared to the target output for that channel (dotted black line). The output on the first rendition and at two other stages of learning indicated by orange arrows on the error trace are also shown as thin orange lines. (C) Effects of mismatch between student and tutor on reproduction accuracy. The heatmap shows the final reproduction error of the motor output after 1000 learning cycles in a rate-based simulation where a student with parameters $\alpha$, $\beta$, $\tau_{1}$, and $\tau_{2}$ was paired with a tutor with memory timescale $\tau_{tutor}$. On the $y$ axis, $\tau_{1}$ and $\tau_{2}$ were kept fixed at $80⁢ms$ and $40⁢ms$, respectively, while $\alpha$ and $\beta$ were varied (subject to the constraint $\alpha-\beta=1$; see text). Different choices of $\alpha$ and $\beta$ lead to different optimal timescales $\tau_{tutor}^{*}$ according to Equation (4). The diagonal elements correspond to matched tutor and student, $\tau_{tutor}=\tau_{tutor}^{*}$. Note that the color scale is logarithmic. (D) Error evolution curves as a function of the mismatch between student and tutor. Each plot shows how the error in the motor program changed during 1000 learning cycles for the same conditions as those shown in the heatmap. The region shaded in light pink shows simulations where the mismatch between student and tutor led to a deteriorating instead of improving performance during learning.

![Video 1.](https://cdn.elifesciences.org/articles/20944/elife-20944-media1.mp4.jpg)

**Video 1.:** Evolution of motor output during learning in a rate-based simulation using a rate-based ($\alpha=0$) plasticity rule paired with a matching tutor.This video relates to Figure 3A.

![Video 2.](https://cdn.elifesciences.org/articles/20944/elife-20944-media2.mp4.jpg)

**Video 2.:** Evolution of motor output during learning in a rate-based simulation using a timing-based ($\alpha≈\beta$) plasticity rule paired with a matching tutor.This video relates to Figure 3B.

To test the effects of mismatch between tutor and student, we used tutors with timescales that did not match Equation (4). All student plasticity rules had the same effective time constants $\tau_{1}$ and $\tau_{2}$, but different parameters $\alpha$ and $\beta$ (see Equation 1), subject to the constraint $\alpha-\beta=1$ described in the previous section. Different tutors had different memory time scales $\tau_{tutor}$ (Equation 3). Figure 3C and D demonstrate that learning was more rapid for well-matched tutor-student pairs (the diagonal neighborhood, where $\tau_{tutor}≈\tau_{tutor}^{*}$). When the tutor error integration timescale was shorter than the matched value in Equation (4), $\tau_{tutor} < \tau_{tutor}^{∗}$, learning was often completely disrupted (many pairs below the diagonal in Figure 3C and D). When the tutor error integration timescale was longer than the matched value in Equation (4), $\tau_{tutor} > \tau_{tutor}^{∗}$ learning was slowed down. Figure 3C also shows that a certain amount of mismatch between the tutor error integration timescale $\tau_{tutor}$ and the matched timescale $\tau_{tutor}^{*}$ implied by the student plasticity rule is tolerated by the system. Interestingly, the diagonal band over which learning is effective in Figure 3C is roughly of constant width—note that the scale on both axes is logarithmic, so that this means that the tutor error integration timescale $\tau_{tutor}$ has to be within a constant factor of the optimal timescale $\tau_{tutor}^{*}$ for good learning. We also see that the breakdown in learning is more abrupt when $\tau_{tutor} < \tau_{tutor}^{∗}$ than in the opposite regime.

An interesting feature of the results from Figure 3C and D is that the difference in performance between matched and mismatched pairs becomes less pronounced for timescales shorter than about $100⁢ms$. This is due to the fact that the plasticity rule (Equation 1) implicitly smooths over timescales of the order of $\tau_{1,2}$, which in our simulations were equal to $\tau_{1}=80⁢ms$, $\tau_{2}=40⁢ms$. Thus, variations of the tutor signal on shorter timescales have little effect on learning. Using different values for the effective timescales $\tau_{1,2}$ describing the plasticity rule can increase or decrease the range of parameters over which learning is robust against tutor–student mismatches (see Appendix).

### Robust learning with nonlinearities

In the model above, firing rates for the tutor were allowed to grow as large as necessary to implement the most efficient learning. However, the firing rates of realistic neurons typically saturate at some fixed bound. To test the effects of this nonlinearity in the tutor, we passed the ideal tutor activity (Equation 3) through a sigmoidal nonlinearity,

$$
g~_{j}⁢(t)=\theta-ρ⁢tanh⁡\frac{ζ}{\alpha-\beta}⁢\frac{1}{\tau_{tutor}}⁢\int_{0}^{t}ϵ_{j}⁢(t^{′})⁢e^{-(t-t^{′})/\tau_{tutor}}⁢d⁢t^{′}.
$$

where 2⁢ρ is the range of firing rates. We typically chose θ=ρ=80⁢Hz to constrain the rates to the range 0–160 Hz (Ölveczky et al., 2005; Garst-Orozco et al., 2014). Learning slowed down with this change (Figure 4A and online Video 3) as a result of the tutor firing rates saturating when the mismatch between the motor output and the target output was large. However, the accuracy of the final rendition was not affected by saturation in the tutor (Figure 4A, inset). An interesting effect occurred when the firing rate constraint was imposed on a matched tutor with a long memory timescale. When this happened and the motor error was large, the tutor signal saturated and stopped growing in relation to the motor error before the end of the motor program. In the extreme case of very long integration timescales, learning became sequential: early features in the output were learned first, before later features were addressed, as in Figure 4B and online Video 4. This is reminiscent of the learning rule described in (Memmesheimer et al., 2014).

![Figure 4.](https://cdn.elifesciences.org/articles/20944/elife-20944-fig4-v1.jpg)

**Figure 4.:** (A) Learning was slowed down by the firing rate constraint, but the accuracy of the final rendition stayed the same (inset, shown here for one of two simulated output channels). Here $\alpha=0$, $\beta=-1$, and $\tau_{tutor}=\tau_{tutor}^{*}=40⁢ms$. (See online Video 3.) (B) Sequential learning occurred when the firing rate constraint was imposed on a matched tutor with a long memory scale. The plots show the evolution of the motor output for one of the two channels that were used in the simulation. Here $\alpha=24$, $\beta=23$, and $\tau_{tutor}=\tau_{tutor}^{*}=1000⁢ms$. (See online Video 4.).

![Video 3.](https://cdn.elifesciences.org/articles/20944/elife-20944-media3.mp4.jpg)

**Video 3.:** The plasticity rule here was rate-based ($\alpha=0$). This video relates to Figure 4A.

![Video 4.](https://cdn.elifesciences.org/articles/20944/elife-20944-media4.mp4.jpg)

**Video 4.:** This video relates to Figure 4B.

Nonlinearities can similarly affect the activities of student neurons. Our model can be readily extended to describe efficient learning even in this case. The key result is that for efficient learning to occur, the synaptic plasticity rule should depend not just on the tutor and conductor, but also on the activity of the postsynaptic student neurons (details in Appendix). Such dependence on postsynaptic activity is commonly seen in experiments (Chistiakova and Volgushev, 2009; Chistiakova et al., 2014).

The relation between student neuron activations $s_{j}⁢(t)$ and motor outputs $y_{a}⁢(t)$ (Figure 2A) is in general also nonlinear. Compared to the linear assumption that we used, the effect of a monotonic nonlinearity, $y_{a}=N_{a}⁢(\sum_{j}M_{a⁢j}⁢s_{j})$, with $N_{a}$ an increasing function, is similar to modifying the loss function $L$, and does not significantly change our results (see Appendix). We also checked that imposing a rectification constraint that conductor–student weights $W_{i⁢j}$ must be positive does not modify our results either (see Appendix). This shows that our model continues to work with biologically realistic synapses that cannot change sign from excitatory to inhibitory during learning.

### Spiking neurons and birdsong

To apply our model to vocal learning in birds, we extended our analysis to networks of spiking neurons. Juvenile songbirds produce a ‘babble’ that converges through learning to an adult song strongly resembling the tutor song. This is reflected in the song-aligned spiking patterns in pre-motor area RA, which become more stereotyped and cluster in shorter, better-defined bursts as the bird matures (Figure 5A). We tested whether our model could reproduce key statistics of spiking in RA over the course of song learning. In this context, our theory of efficient learning, derived in a rate-based scenario, predicts a specific relation between the teaching signal embedded in LMAN firing patterns, and the plasticity rule implemented in RA. We tested whether these predictions continued to hold in the spiking context.

![Figure 5.](https://cdn.elifesciences.org/articles/20944/elife-20944-fig5-v1.jpg)

**Figure 5.:** (A) Spike patterns recorded from zebra finch RA during song production, for a juvenile (top) and an adult (bottom). Each color corresponds to a single neuron, and the song-aligned spikes for six renditions of the song are shown. Adapted from Ölveczky et al. (2011). (B) Spike patterns from model student neurons in our simulations, for the untrained (top) and trained (bottom) models. The training used $\alpha=1$, $\beta=0$, and $\tau_{tutor}=80⁢ms$, and ran for 600 iterations of the song. Each model neuron corresponds to a different output channel of the simulation. In this case, the targets for each channel were chosen to roughly approximate the time course observed in the neural recordings. (C) Progression of reproduction error in the spiking simulation as a function of the number of repetitions for the same conditions as in panel B. The inset shows the accuracy of reproduction in the trained model for one of the output channels. (See online Video 5.) (D) Effects of mismatch between student and tutor on reproduction accuracy in the spiking model. The heatmap shows the final reproduction error of the motor output after 1000 learning cycles in a spiking simulation where a student with parameters $\alpha$, $\beta$, $\tau_{1}$, and $\tau_{2}$ was paired with a tutor with memory timescale $\tau_{tutor}$. On the $y$ axis, $\tau_{1}$ and $\tau_{2}$ were kept fixed at $80⁢ms$ and $40⁢ms$, respectively, while $\alpha$ and $\beta$ were varied (subject to the constraint $\alpha-\beta=1$; see section "Learning in a rate-based model"). Different choices of $\alpha$ and $\beta$ lead to different optimal timescales $\tau_{tutor}^{*}$ according to Equation (4). The diagonal elements correspond to matched tutor and student, $\tau_{tutor}=\tau_{tutor}^{*}$. Note that the color scale is logarithmic.

![Video 5.](https://cdn.elifesciences.org/articles/20944/elife-20944-media5.mp4.jpg)

**Video 5.:** The plasticity rule parameters were $\alpha=1$, $\beta=0$, and the tutor had a matching timescale $\tau_{tutor}=\tau_{tutor}^{*}=80⁢ms$. This video relates to Figure 5C.

Following the experiments of Hahnloser et al. (2002), we modeled each neuron in HVC (the conductor) as firing one short, precisely timed burst of 5–6 spikes at a single moment in the motor program. Thus the population of HVC neurons produced a precise timebase for the song. LMAN (tutor) neurons are known to have highly variable firing patterns that facilitate experimentation, but also contain a corrective bias (Andalman and Fee, 2009). Thus we modeled LMAN as producing inhomogeneous Poisson spike trains with a time-dependent firing rate given by Equation (5) in our model. Although biologically there are several LMAN neurons projecting to each RA neuron, we again simplified by ‘summing’ the LMAN inputs into a single, effective tutor neuron, similarly to the approach in (Fiete et al., 2007). The LMAN-RA synapses were modeled in a current-based approach as a mixture of AMPA and NMDA receptors, following the songbird data (Garst-Orozco et al., 2014; Stark and Perkel, 1999). The initial weights for all synapses were tuned to produce RA firing patterns resembling juvenile birds (Ölveczky et al., 2011), subject to constraints from direct measurements in slice recordings (Garst-Orozco et al., 2014) (see Materials and methods for details, and Figure 5B for a comparison between neural recordings and spiking in our model). In contrast to the constant inhibitory bias that we used in our rate-based simulations, for the spiking simulations we chose an activity-dependent global inhibition for RA neurons. We also tested that a constant bias produced similar results (see Appendix).

Synaptic strength updates followed the same two-timescale dynamics that was used in the rate-based models (Figure 2B). The firing rates $c_{i}⁢(t)$ and $g_{j}⁢(t)$ that appear in the plasticity equation were calculated in the spiking model by filtering the spike trains from conductor and tutor neurons with exponential kernels. The synaptic weights were constrained to be non-negative. (See Materials and methods for details.)

As long as the tutor error integration timescale was not too large, learning proceeded effectively when the tutor error integration timescale and the student plasticity rule were matched (see Figure 5C and online Video 5), with mismatches slowing down or abolishing learning, just as in our rate-based study (compare Figure 5D with Figure 3C). The rate of learning and the accuracy of the trained state were lower in the spiking model compared to the rate-based model. The lower accuracy arises because the tutor neurons fire stochastically, unlike the deterministic neurons used in the rate-based simulations. The stochastic nature of the tutor firing also led to a decrease in learning accuracy as the tutor error integration timescale $\tau_{tutor}$ increased (Figure 5D). This happens through two related effects: (1) the signal-to-noise ratio in the tutor guiding signal decreases as $\tau_{tutor}$ increases once the tutor error integration timescale is longer than the duration $T$ of the motor program (see Appendix); and (2) the fluctuations in the conductor–student weights lead to some weights getting clamped at 0 due to the positivity constraint, which leads to the motor program overshooting the target (see Appendix). The latter effect can be reduced by either allowing for negative weights, or changing the motor output to a push-pull architecture in which some student neurons enhance the output while others inhibit it. The signal-to-noise ratio effect can be attenuated by increasing the gain of the tutor signal, which inhibits early learning, but improves the quality of the guiding signal in the latter stages of the learning process. It is also worth emphasizing that these effects only become relevant once the tutor error integration timescale $\tau_{tutor}$ becomes significantly longer than the duration of the motor program, $T$, which for a birdsong motif would be around 1 s.

Spiking in our model tends to be a little more regular than that in the recordings (compare Figure 5A and Figure 5B). This could be due to sources of noise that are present in the brain which we did not model. One detail that our model does not capture is the fact that many LMAN spikes occur in bursts, while in our simulation LMAN firing is Poisson. Bursts are more likely to produce spikes in downstream RA neurons particularly because of the NMDA dynamics, and thus a bursty LMAN will be more effective at injecting variability into RA (Kojima et al., 2013). Small inaccuracies in aligning the recorded spikes to the song are also likely to contribute apparent variability between renditions in experiments. Indeed, some of the variability in Figure 5A looks like it could be due to time warping and global time shifts that were not fully corrected.

### Robust learning with credit assignment errors

The calculation of the tutor output in our rule involved estimating the motor error ϵj from Equation (2). This required knowledge of the assignment between student activities and motor output, which in our model was represented by the matrix Ma⁢j (Figure 2A). In our simulations, we typically chose an assignment in which each student neuron contributed to a single output channel, mimicking the empirical findings for neurons in bird RA. Mathematically, this implies that each column of Ma⁢j contained a single non-zero element. In Figure 6A, we show what happened in the rate-based model when the tutor incorrectly assigned a certain fraction of the neurons to the wrong output. Specifically, we considered two output channels, y1 and y2, with half of the student neurons contributing only to y1 and the other half contributing only to y2. We then scrambled a fraction ρ of this assignment when calculating the motor error, so that the tutor effectively had an imperfect knowledge of the student–output relation. Figure 6A shows that learning is robust to this kind of mis-assignment even for fairly large values of the error fraction ρ up to about 40%, but quickly deteriorates as this fraction approaches 50%.

![Figure 6.](https://cdn.elifesciences.org/articles/20944/elife-20944-fig6-v1.jpg)

**Figure 6.:** (A) Effects of credit mis-assignment on learning in a rate-based simulation. Here, the system learned output sequences for two independent channels. The student–output weights $M_{a⁢j}$ were chosen so that the tutor wrongly assigned a fraction of student neurons to an output channel different from the one it actually mapped to. The graph shows how the accuracy of the motor output after 1000 learning steps depended on the fraction of mis-assigned credit. (B) Learning curve and trained motor output (inset) for one of the channels showing two-stage reinforcement-based learning for the memory-less tutor ($\tau_{tutor}=0$). The accuracy of the trained model is as good as in the case where the tutor was assumed to have a perfect model of the student–output relation. However, the speed of learning is reduced. (See online Video 6.) (C) Learning curve and trained motor output (inset) for one of the output channels showing two-stage reinforcement-based learning when the tutor circuit needs to integrate information about the motor error on a certain timescale. Again, learning was slow, but the accuracy of the trained state was unchanged. (See online Video 7.) (D) Evolution of the average number of HVC inputs per RA neuron with learning in a reinforcement example. Synapses were considered pruned if they admitted a current smaller than 1 nA after a pre-synaptic spike in our simulations.

![Video 6.](https://cdn.elifesciences.org/articles/20944/elife-20944-media6.mp4.jpg)

**Video 6.:** Here the tutor was memory-less ($\tau_{tutor}=0$). This video relates to Figure 6B.

![Video 7.](https://cdn.elifesciences.org/articles/20944/elife-20944-media7.mp4.jpg)

**Video 7.:** Here the tutor needed to integrate information about the motor error on a timescale $\tau_{tutor}=440⁢ms$. This video relates to Figure 6C.

Due to environmental factors that affect development of different individuals in different ways, it is unlikely that the student–output mapping can be innate. As such, the tutor circuit must learn the mapping. Indeed, it is known that LMAN in the bird receives an indirect evaluation signal via Area X, which might be used to effect this learning (Andalman and Fee, 2009; Gadagkar et al., 2016; Hoffmann et al., 2016; Kubikova et al., 2010). One way in which this can be achieved is through a reinforcement paradigm. We thus considered a learning rule where the tutor circuit receives a reward signal that enables it to infer the student–output mapping. In general the output of the tutor circuit should depend on an integral of the motor error, as in Equation (3), to best instruct the student. For simplicity, we start with the memory-less case, $\tau_{tutor}=0$, in which only the instantaneous value of the motor error is reflected in the tutor signal; we then show how to generalize this for $\tau_{tutor} > 0$.

As before, we took the tutor neurons to fire Poisson spikes with time-dependent rates $f_{j}⁢(t)$, which were initialized arbitrarily. Because of stochastic fluctuations, the actual tutor activity on any given trial, $g_{j}⁢(t)$, differs somewhat from the average, $g¯_{j}⁢(t)$. Denoting the difference by $ξ_{j}⁢(t)=g_{j}⁢(t)-g¯_{j}⁢(t)$, the update rule for the tutor firing rates was given by

$$
Δ⁢f_{j}⁢(t)=η_{tutor}⁢(R⁢(t)-R¯)⁢ξ_{j}⁢(t),
$$

where $η_{tutor}$ is a learning rate, $R⁢(t)$ is the instantaneous reward signal, and $R¯$ is its average over recent renditions of the motor program. In our implementation, $R¯$ is obtained by convolving $R⁢(t)$ with an exponential kernel (timescale = 1 s). The reward $R⁢(t_{max})$ at the end of one rendition becomes the baseline at the start of the next rendition $R⁢(0)$. The baseline $g¯_{j}⁢(t)$ of the tutor activity is calculated by averaging over recent renditions of the song with exponentially decaying weights (one $e$-fold of decay for every five renditions). Further implementation details are available in our code at https://github.com/ttesileanu/twostagelearning (Teşileanu, 2016) (with a copy archived at https://github.com/elifesciences-publications/twostagelearning).

The intuition behind this rule is that, whenever a fluctuation in the tutor activity leads to better-than-average reward ($R(t) > R¯$), the tutor firing rate changes in the direction of the fluctuation for subsequent trials, ‘freezing in’ the improvement. Conversely, the firing rate moves away from the directions in which fluctuations tend to reduce the reward.

To test our learning rule, we ran simulations using this reinforcement strategy and found that learning again converges to an accurate rendition of the target output (Figure 6B, inset and online Video 6). The number of repetitions needed for training is greatly increased compared to the case in which the credit assignment is assumed known by the tutor circuit (compare Figure 6B to Figure 5C). This is because the tutor needs to use many training rounds for experimentation before it can guide conductor–student plasticity. The rate of learning in our model is similar to the songbird (i.e., order $10 000$ repetitions for learning, given that a zebra finch typically sings about 1000 repetitions of its song each day, and takes about one month to fully develop adult song).

Because of the extra training time needed for the tutor to adapt its signal, the motor output in our reward-based simulations tends to initially overshoot the target (leading to the kink in the error at around 2000 repetitions in Figure 6B). Interestingly, the subsequent reduction in output that leads to convergence of the motor program, combined with the positivity constraint on the synaptic strengths, leads to many conductor–student connections being pruned (Figure 6D). This mirrors experiments on songbirds, where the number of connections between HVC and RA first increases with learning and then decreases (Garst-Orozco et al., 2014).

The reinforcement rule described above responds only to instantaneous values of the reward signal and tutor firing rate fluctuations. In general, effective learning requires that the tutor keep a memory trace of its activity over a timescale $\tau_{tutor} > 0$, as in Equation (4). To achieve this in the reinforcement paradigm, we can use a simple generalization of Equation (6) where the update rule is filtered over the tutor memory timescale:

$$
Δ⁢f_{j}⁢(t)=η_{tutor}⁢\frac{1}{\tau_{tutor}}⁢\int^{t}d⁢t^{′}⁢(R⁢(t^{′})-R¯)⁢ξ_{j}⁢(t^{′})⁢e^{-(t-t^{′})/\tau_{tutor}}.
$$

We tested that this rule leads to effective learning when paired with the corresponding student, i.e., one for which Equation (4) is obeyed (Figure 6C and online Video 7).

The reinforcement rules proposed here are related to the learning rules from (Fiete and Seung, 2006; Fiete et al., 2007) and (Farries and Fairhall, 2007). However, those models focused on learning in a single pass, instead of the two-stage architecture that we studied. In particular, in Fiete et al. (2007), area LMAN was assumed to generate pure Poisson noise and reinforcement learning took place at the HVC–RA synapses. In our model, which is in better agreement with recent evidence regarding the roles of RA and LMAN in birdsong (Andalman and Fee, 2009), reinforcement learning first takes place in the anterior forebrain pathway (AFP), for which LMAN is the output. A reward-independent heterosynaptic plasticity rule then solidifies the information in RA.

In our simulations, tutor neurons fire Poisson spikes with specific time-dependent rates which change during learning. The timecourse of the firing rates in each repetition must then be stored somewhere in the brain. In fact, in the songbird, there are indirect projections from HVC to LMAN, going through the basal ganglia (Area X) and the dorso-lateral division of the medial thalamus (DLM) in the anterior forebrain pathway (Figure 1A) (Perkel, 2004). These synapses could store the required time-dependence of the tutor firing rates. In addition, the same synapses can provide the timebase input that would ensure synchrony between LMAN firing and RA output, as necessary for learning. Our reinforcement learning rule for the tutor area, Equation (6), can be viewed as an effective model for plasticity in the projections between HVC, Area X, DLM, and LMAN, as in Fee and Goldberg (2011). In this picture, the indirect HVC–LMAN connections behave somewhat like the ‘hedonistic synapses’ from Seung (2003), though we use a simpler synaptic model here. Implementing the integral from Equation (7) would require further recurrent circuitry in LMAN which is beyond the scope of this paper, but would be interesting to investigate in future work.

## Discussion

We built a two-stage model of learning in which one area (the student) learns to generate a patterned motor output under guidance from a tutor area. This architecture is inspired by the song system of zebra finches, where area LMAN provides a corrective bias to the song that is then consolidated in the HVC–RA synapses. Using an approach rooted in the efficient coding literature, we showed analytically that, in a simple model, the tutor output that is most likely to lead to effective learning by the student involves an integral over the recent magnitude of the motor error. We found that efficiency requires that the timescale for this integral should be related to the synaptic plasticity rule used by the student. Using simulations, we tested our findings in more general settings. In particular, we demonstrated that tutor-student matching is important for learning in a spiking-neuron model constructed to reproduce spiking patterns similar to those measured in zebra finches. Learning in this model changes the spiking statistics of student neurons in realistic ways, for example, by producing more bursty, stereotyped firing events as learning progresses. Finally, we showed how the tutor can build its error-correcting signal by means of reinforcement learning.

If the birdsong system supports efficient learning, our model can predict the temporal structure of the firing patterns of RA-projecting LMAN neurons, given the plasticity rule implemented at the HVC–RA synapses. These predictions can be directly tested by recordings from LMAN neurons in singing birds, assuming that a good measure of motor error is available, and that we can estimate how the neurons contribute to this error. Moreover, recordings from a tutor circuit, such as LMAN, could be combined with a measure of motor error to infer the plasticity rule in a downstream student circuit, such as RA. This could be compared with direct measurements of the plasticity rule obtained in slice. Conversely, knowledge of the student plasticity rule could be used to predict the time-dependence of tutor firing rates. According to our model, the firing rate should reflect the integral of the motor error with the timescale predicted by the model. A different approach would be to artificially tutor RA by stimulating LMAN neurons electrically or optogenetically. We would predict that if the tutor signal is delivered appropriately (e.g., in conjunction with a particular syllable [Tumer and Brainard, 2007]), then the premotor bias produced by the stimulation should become incorporated into the motor pathway faster when the timescale of the artificial LMAN signal is properly matched to the RA synaptic plasticity rule.

Our model can be applied more generally to other systems in the brain exhibiting two-stage learning, such as motor learning in mammals. If the plasticity mechanisms in these systems are different from those in songbirds, our predictions for the structure of the guiding signal will vary correspondingly. This would allow a further test of our model of ‘efficient learning’ in the brain. It is worth pointing out that our model was derived assuming a certain hierarchy among the timescales that model the student plasticity and the tutor signal. A mismatch between the model predictions and observations could also imply a breakdown of these approximations, rather than failure of the hypothesis that the particular system under study evolved to support efficient learning. Of course our analysis could be extended by relaxing these assumptions, for example by keeping more terms in the Taylor expansion that we used in our derivation of the matched tutor signal.

Applied to birdsong, our model is best seen as a mechanism for learning song syllables. The ordering of syllables in song motifs seems to have a second level of control within HVC and perhaps beyond (Basista et al., 2014; Hamaguchi et al., 2016). Songs can also be distorted by warping their timebase through changes in HVC firing without alterations of the HVC–RA connectivity (Ali et al., 2013). In view of these phenomena, it would be interesting to incorporate our model into a larger hierarchical framework in which the sequencing and temporal structure of the syllables are also learned. A model of transitions between syllables can be found in Doya and Sejnowski (2000), where the authors use a ‘weight perturbation’ optimization scheme in which each HVC–RA synaptic weight is perturbed individually. We did not follow this approach because there is no plausible mechanism for LMAN to provide separate guidance to each HVC–RA synapse; in particular, there are not enough LMAN neurons (Fiete et al., 2007).

In this paper we assumed a two-stage architecture for learning, inspired by birdsong. An interesting question is whether and under what conditions such an architecture is more effective than a single-step model. Possibly, having two stages is better when a single tutor area is responsible for training several different dedicated controllers, as is likely the case in motor learning. It would then be beneficial to have an area that can learn arbitrary behaviors, perhaps at the cost of using more resources and having slower reaction times, along with the ability to transfer these behaviors into low-level circuitry that is only capable of producing stereotyped motor programs. The question then arises whether having more than two levels in this hierarchy could be useful, what the other levels might do, and whether such hierarchical learning systems are implemented in the brain.

## Materials and methods

### Equations for rate-based model

The basic equations we used for describing our rate-based model (Figure 2A) are the following:

$$
y_{a}(t)=\sumjM_{aj}s_{j}(t),s_{j}(t)=\sumiW_{ij}c_{i}(t)+wg_{j}(t)−x_{inh}.
$$

In simulations, we further filtered the output using an exponential kernel,

$$
y~_{a}(t)=\sumjM_{aj}\int_{0}^{t}s_{j}(t^{′})e^{−(t−t^{′})/\tau_{out}}dt^{′},
$$

with a timescale $\tau_{out}$ that we typically set to 25 ms. The smoothing produces more realistic outputs by mimicking the relatively slow reaction time of real muscles, and stabilizes learning by filtering out high-frequency components of the motor output. The latter interfere with learning because of the delay between the effect of conductor activity on synaptic strengths vs. motor output. This delay is of the order $\tau_{1,2}-\tau_{out}$ (see the plasticity rule below).

The conductor activity in the rate-based model is modeled after songbird HVC (Hahnloser et al., 2002): each neuron fires a single burst during the motor program. Each burst corresponds to a sharp increase of the firing rate $c_{i}⁢(t)$ from 0 to a constant value, and then a decrease $10⁢ms$ later. The activities of the different neurons are spread out to tile the whole duration of the output program. Other choices for the conductor activity also work, provided no patterns are repeated (see Appendix).

### Mathematical description of plasticity rule

In our model the rate of change of the synaptic weights obeys a rule that depends on a filtered version of the conductor signal (see Figure 2B). This is expressed mathematically as

$$
\frac{d⁢W_{i⁢j}}{d⁢t}=η⁢c~_{i}⁢(t)⁢(g_{j}⁢(t)-\theta),
$$

where $η$ is a learning rate and $c~_{i}=K*c_{i}$, with the star representing convolution and $K$ being a filtering kernel. We considered a linear combination of two exponential kernels with timescales $\tau_{1}$ and $\tau_{2}$,

$$
K⁢(t)=\alpha⁢K_{1}⁢(t)-\beta⁢K_{2}⁢(t),
$$

with $K_{i}⁢(t)$ given by

$$
K_{i}(t)={\tau_{i}^{−1}e^{−t/\tau_{i}}fort\geq0,0else.
$$

Different choices for the kernels give similar results (see Appendix). The overall scale of $\alpha$ and $\beta$ can be absorbed into the learning rate $η$ in Equation (10). In our simulations, we fix $\alpha-\beta=1$ and keep the learning rate constant as we change the plasticity rule (see Equation 3).

In the spiking simulations with and without reinforcement learning in the tutor circuit, the firing rates $c_{i}⁢(t)$ and $g_{j}⁢(t)$ were estimated by filtering spike trains with exponential kernels whose timescales were in the range $5⁢ms$–$40⁢ms$. The reinforcement studies typically required longer timescales for stability, possibly because of delays between conductor activity and reward signals.

### Derivation of the matching tutor signal

To find the tutor signal that provides the most effective teaching for the student, we first calculate how much synaptic weights change according to our plasticity rule, Equation (10). Then we require that this change matches the gradient descent direction. We have

$$
Δ⁢W_{i⁢j}=\int_{0}^{T}\frac{d⁢W_{i⁢j}}{d⁢t}⁢d⁢t=η⁢\int_{0}^{T}c~_{i}⁢(t)⁢(g_{j}⁢(t)-\theta)⁢d⁢t.
$$

Because of the linearity assumptions in our model, it is sufficient to focus on a case in which each conductor neuron, $i$, fires a single short burst, at a time $t_{i}$. We write this as $c_{i}⁢(t)=\delta⁢(t-t_{i})$, and so

$$
Δ⁢W_{i⁢j}=\int_{0}^{T}\frac{d⁢W_{i⁢j}}{d⁢t}⁢d⁢t=η⁢\int_{0}^{T}K⁢(t-t_{i})⁢(g_{j}⁢(t)-\theta)⁢d⁢t,
$$

where we used the definition of $c~_{i}⁢(t)$. If the time constants $\tau_{1}$, $\tau_{2}$ are short compared to the timescale on which the tutor input $g_{j}⁢(t)$ varies, only the values of $g_{j}⁢(t)$ around time $t_{i}$ will contribute to the integral. If we further assume that $T≫t_{i}$, we can use a Taylor expansion of $g_{j}⁢(t)$ around $t=t_{i}$ to perform the calculation:

$$
ΔW_{ij}≈η\int_{t_{i}}^{∞}K(t−t_{i})(g_{j}(t_{i})−\theta+(t−t_{i})g_{j}^{′}(t_{i}))dt=η(g_{j}(t_{i})−\theta)\int_{0}^{∞}K(t)dt+ηg_{j}^{′}(t_{i})\int_{0}^{∞}tK(t)dt=η(g_{j}(t_{i})−\theta)\int_{0}^{∞}(\alphaK_{1}(t)−\betaK_{2}(t))dt+ηg_{j}^{′}(t_{i})\int_{0}^{∞}t(\alphaK_{1}(t)−\betaK_{2}(t))dt.
$$

Doing the integrals involving the exponential kernels $K_{1}$ and $K_{2}$, we get

$$
Δ⁢W_{i⁢j}=η⁢[(\alpha-\beta)⁢(g_{j}⁢(t_{i})-\theta)+(\alpha⁢\tau_{1}-\beta⁢\tau_{2})⁢g_{j}^{′}⁢(t_{i})].
$$

We would like this synaptic change to optimally reduce a measure of mismatch between the output and the desired target as measured by a loss function. A generic smooth loss function $L⁢(y_{a}⁢(t),y¯_{a}⁢(t))$ can be quadratically approximated when $y_{a}$ is sufficiently close to the target $y¯_{a}⁢(t)$. With this in mind, we consider a quadratic loss

$$
L=\frac{1}{2}⁢\suma\int_{0}^{T}[y_{a}⁢(t)-y¯_{a}⁢(t)]^{2}⁢d⁢t.
$$

The loss function would decrease monotonically during learning if synaptic weights changed in proportion to the negative gradient of $L$:

$$
Δ⁢W_{i⁢j}=-\gamma⁢\frac{\partial⁡L}{\partial⁡W_{i⁢j}},
$$

where $\gamma$ is a learning rate. This implies

$$
Δ⁢W_{i⁢j}=-\gamma⁢\suma\int_{0}^{T}M_{a⁢j}⁢[y_{a}⁢(t)-y¯_{a}⁢(t)]⁢c_{i}⁢(t).
$$

Using again $c_{i}⁢(t)=\delta⁢(t-t_{i})$, we obtain

$$
Δ⁢W_{i⁢j}=-\gamma⁢ϵ_{j}⁢(t_{i}),
$$

where we used the notation from Equation (2) for the motor error at student neuron $j$.

We now set Equations (16) and (20) equal to each other. If the conductor fires densely in time, we need the equality to hold for all times, and we thus get a differential equation for the tutor signal $g_{j}⁢(t)$. This identifies the tutor signal that leads to gradient descent learning as a function of the motor error $ϵ_{j}⁢(t)$, Equation (3) (with the notation $ζ=\gamma/η$).

### Spiking simulations

We used spiking models that were based on leaky integrate-and-fire neurons with current-based dynamics for the synaptic inputs. The magnitude of synaptic potentials generated by the conductor–student synapses was independent of the membrane potential, approximating AMPA receptor dynamics, while the synaptic inputs from the tutor to the student were based on a mixture of AMPA and NMDA dynamics. Specifically, the equations describing the dynamics of the spiking model were:

$$
\tau_{m}\frac{dV_{j}}{dt}=(V_{R}−V_{j})+R(I_{j}^{AMPA}+I_{j}^{NMDA})−V_{inh},(except during refractory period)\frac{dI_{j}^{AMPA}}{dt}=−\frac{I_{j}^{AMPA}}{\tau_{AMPA}}+\sumiW_{ij}\sumk\delta(t−t_{k}^{ conductor \#i})+(1−r)w\sumk\delta(t−t_{k}^{tutor}),\frac{dI_{j}^{NMDA}}{dt}=−\frac{I_{j}^{NMDA}}{\tau_{NMDA}}+rwG(V_{j})\sumk\delta(t−t_{k}^{tutor}),V_{inh}=\frac{g_{inh}}{N_{ student}}\sumjS_{j}(t),\frac{dS_{j}}{dt}=−\frac{S_{j}}{\tau_{inh}}+\sumk\delta(t−t_{k}^{student}),G(V)=[1+\frac{[Mg]}{3.57mM}exp⁡(−V/16.13mV)]^{−1}.
$$

Here $V_{j}$ is the membrane potential of the $j^{th}$ student neuron and $V_{R}$ is the resting potential, as well as the potential to which the membrane was reset after a spike. Spikes were registered whenever the membrane potential went above a threshold $V_{th}$, after which a refractory period $\tau_{ref}$ ensued. Apart from excitatory AMPA and NMDA inputs modeled by the $I_{j}^{AMPA}$ and $I_{j}^{NMDA}$ variables in our model, we also included a global inhibitory signal $V_{inh}$ which is proportional to the overall activity of student neurons averaged over a timescale $\tau_{inh}$. The averaging is performed using the auxiliary variables $S_{j}$ which are convolutions of student spike trains with an exponential kernel. These can be thought of as a simple model for the activities of inhibitory interneurons in the student.

Table 1 gives the values of the parameters we used in the simulations. These values were chosen to match the firing statistics of neurons in bird RA, as described below.

**Table 1.**
 Values for parameters used in the spiking simulations.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Symbol</th>
      <th>Value</th>
      <th>Parameter</th>
      <th>Symbol</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>No. of conductor neurons</td>
      <td></td>
      <td>300</td>
      <td>No. of student neurons</td>
      <td></td>
      <td>80</td>
    </tr>
    <tr>
      <td>Reset potential</td>
      <td>VR</td>
      <td>-72.3⁢mV</td>
      <td>Input resistance</td>
      <td>R</td>
      <td>353⁢M⁢Ω</td>
    </tr>
    <tr>
      <td>Threshold potential</td>
      <td>Vth</td>
      <td>-48.6⁢mV</td>
      <td>Strength of inhibition</td>
      <td>ginh</td>
      <td>1.80⁢mV</td>
    </tr>
    <tr>
      <td>Membrane time constant</td>
      <td>τm</td>
      <td>24.5⁢ms</td>
      <td>Fraction NMDA receptors</td>
      <td>r</td>
      <td>0.9</td>
    </tr>
    <tr>
      <td>Refractory period</td>
      <td>τref</td>
      <td>1.1⁢ms</td>
      <td>Strength of synapses from tutor</td>
      <td>w</td>
      <td>100⁢nA</td>
    </tr>
    <tr>
      <td>AMPA time constant</td>
      <td>τAMPA</td>
      <td>6.3⁢ms</td>
      <td>No. of conductor synapses per student neuron</td>
      <td></td>
      <td>148</td>
    </tr>
    <tr>
      <td>NMDA time constant</td>
      <td>τNMDA</td>
      <td>81.5⁢ms</td>
      <td>Mean strength of synapses from conductor</td>
      <td></td>
      <td>32.6⁢nA</td>
    </tr>
    <tr>
      <td>Time constant for global inhibition</td>
      <td>τinh</td>
      <td>20⁢ms</td>
      <td>Standard deviation of conductor–student weights</td>
      <td></td>
      <td>17.4⁢nA</td>
    </tr>
    <tr>
      <td>Conductor firing rate during bursts</td>
      <td></td>
      <td>632⁢Hz</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

The voltage dynamics for conductor and tutor neurons was not simulated explicitly. Instead, each conductor neuron was assumed to fire a burst at a fixed time during the simulation. The onset of each burst had additive timing jitter of $\pm0.3⁢ms$ and each spike in the burst had a jitter of $\pm0.2⁢ms$. This modeled the uncertainty in spike times that is observed in in vivo recordings in birdsong (Hahnloser et al., 2002). Tutor neurons fired Poisson spikes with a time-dependent firing rate that was set as described in the main text.

The initial connectivity between conductor and student neurons was chosen to be sparse (see Table 1). The initial distribution of synaptic weights was log-normal, matching experimentally measured values for zebra finches (Garst-Orozco et al., 2014). Since these measurements are done in the slice, the absolute number of HVC synapses per RA neuron is likely to have been underestimated. The number of conductor–student synapses we start with in our simulations is thus chosen to be higher than the value reported in that paper (see Table 1), and is allowed to change during learning. We checked that the learning paradigm described here is robust to substantial changes in these parameters, but we have chosen values that are faithful to birdsong experiments and which are thus able to imitate the RA spiking statistics during song.

The synapses projecting onto each student neuron from the tutor have a weight that is fixed during our simulations reflecting the finding in Garst-Orozco et al. (2014) that the average strength of LMAN–RA synapses for zebra finches does not change with age. There is some evidence that individual LMAN–RA synapses undergo plasticity concurrently with the HVC–RA synapses (Mehaffey and Doupe, 2015) but we did not seek to model this effect. There are also developmental changes in the kinetics of NMDA-mediated synaptic currents in both HVC–RA and LMAN–RA synapses which we do not model (Stark and Perkel, 1999). These, however, happen early in development, and thus are unlikely to have an effect on song crystallization, which is what our model focuses on. Stark and Perkel, 1999 also observed changes in the relative contribution of NMDA to AMPA responses in the HVC–RA synapses. We do not incorporate such effects in our model since we do not explicitly model the dynamics of HVC neurons in this paper. However, this is an interesting avenue for future work, especially since there is evidence that area HVC can also contribute to learning, in particular in relation to the temporal structure of song (Ali et al., 2013).

### Matching spiking statistics with experimental data

We used an optimization technique to choose parameters to maximize the similarity between the statistics of spiking in our simulations and the firing statistics observed in neural recordings from the songbird. The comparison was based on several descriptive statistics: the average firing rate; the coefficient of variation and skewness of the distribution of inter-spike intervals; the frequency and average duration of bursts; and the firing rate during bursts. For calculating these statistics, bursts were defined to start if the firing rate went above 80 Hz and last until the rate decreased below 40 Hz.

To carry out such optimizations in the stochastic context of our simulations, we used an evolutionary algorithm—the covariance matrix adaptation evolution strategy (CMA-ES) (Hansen, 2006). The objective function was based on the relative error between the simulation statistics $x_{i}^{sim}$ and the observed statistics $x_{i}^{obs}$,

$$
error=[\sumi(\frac{x_{i}^{sim}}{x_{i}^{obs}}-1)^{2}]^{1/2}.
$$

Equal weight was placed on optimizing the firing statistics in the juvenile (based on a recording from a 43 dph bird) and optimizing firing in the adult (based on a recording from a 160 dph bird). In this optimization there was no learning between the juvenile and adult stages. We simply required that the number of HVC synapses per RA neuron, and the mean and standard deviation of the corresponding synaptic weights were in the ranges seen in the juvenile and adult by Garst-Orozco et al. (2014). The optimization was carried out in Python (RRID:SCR_008394), using code from https://www.lri.fr/~hansen/cmaes_inmatlab.html. The results fixed the parameter choices in Table 1 which were then used to study our learning paradigm. While these choices are important for achieving firing statistics that are similar to those seen in recordings from the bird, our learning paradigm is robust to large variations in the parameters in Table 1.

### Software and data

We used custom-built Python (RRID:SCR_008394) code for simulations and data analysis. The software and data that we used can be accessed online on GitHub (RRID:SCR_002630) at https://github.com/ttesileanu/twostagelearning.
