# Self-configuring feedback loops for sensorimotor control

## Authors

- Sergio Oscar Verduzco-Flores<sup>1</sup> ([ORCID: 0000-0002-0712-145X](https://orcid.org/0000-0002-0712-145X)) †
- Erik De Schutter<sup>1</sup> ([ORCID: 0000-0001-8618-5138](https://orcid.org/0000-0001-8618-5138))

### Affiliations

1. https://ror.org/02qg15b79 Computational Neuroscience Unit, Okinawa Institute of Science and Technology Okinawa Japan

† Corresponding author

## Abstract

How dynamic interactions between nervous system regions in mammals performs online motor control remains an unsolved problem. In this paper, we show that feedback control is a simple, yet powerful way to understand the neural dynamics of sensorimotor control. We make our case using a minimal model comprising spinal cord, sensory and motor cortex, coupled by long connections that are plastic. It succeeds in learning how to perform reaching movements of a planar arm with 6 muscles in several directions from scratch. The model satisfies biological plausibility constraints, like neural implementation, transmission delays, local synaptic learning and continuous online learning. Using differential Hebbian plasticity the model can go from motor babbling to reaching arbitrary targets in less than 10 min of in silico time. Moreover, independently of the learning mechanism, properly configured feedback control has many emergent properties: neural populations in motor cortex show directional tuning and oscillatory dynamics, the spinal cord creates convergent force fields that add linearly, and movements are ataxic (as in a motor system without a cerebellum).

## Introduction

## The challenge

Neuroscience has made great progress in decoding how cortical regions perform specific brain functions like primate vision (Kaas and Collins, 2003; Ballard and Zhang, 2021 and rodent navigation Chersi and Burgess, 2015; Moser et al., 2017). Conversely, the evolutionary much older motor control system still poses fundamental questions, despite a large body of experimental work. This is because, in mammals, in addition to areas in cortex like premotor and motor areas and to some degree sensory and parietal ones, many extracortical regions have important and unique functions: basal ganglia, thalamus, cerebellum, pons, brain stem nuclei like the red nucleus and spinal cord (Eccles, 1981; Loeb and Tsianos, 2015). These structures are highly interconnected by fast conducting axons and all show strong dynamic activity changes, related to the ongoing dynamics of the performed motor act. Clinical and lesion studies have confirmed the necessity of each of these regions for normal smooth motor control of arm reaching (Shadmehr and Wise, 2005; Arber and Costa, 2018).

Fully understanding motor control will thus entail understanding the simultaneous function and interplay of all brain regions involved. Little by little, new experimental techniques will allow us to monitor more neurons, in more regions, and for longer periods (Tanaka et al., 2018, e.g.). But to make sense of these data computational models must step up to the task of integrating all those regions to create a functional neuronal machine.

Finally, relatively little is known about the neural basis of motor development in infants (Hadders-Algra, 2018). Nevertheless, a full understanding of primate motor control will not only require explanation of how these brain regions complement and interact with each other but also how this can be learned during childhood.

With these challenges in mind we recently developed a motor control framework based on differential Hebbian learning (Verduzco-Flores et al., 2022). A common theme in physiology is the control of homeostatic variables (e.g. blood glucose levels, body temperature, etc.) using negative feedback mechanisms (Woods and Ramsay, 2007). From a broad perspective, our approach considers the musculoskeletal system as an extension of this homeostatic control system: movement aims to make the external environment conducive to the internal control of homeostatic variables (e.g. by finding food, or shelter from the sun).

Our working hypothesis (see Verduzco-Flores et al., 2022) is that control of homeostatic variables requires a feedback controller that uses the muscles to produce a desired set of sensory perceptions. The motosensory loop, minimally containing motor cortex, spinal cord, and sensory cortex may implement that feedback controller. To test this hypothesis we implemented a relatively complete model of the sensorimotor loop (Figure 1), using the learning rules in Verduzco-Flores et al., 2022 to produce 2D arm reaching. The activity of the neural populations and the movements they produced showed remarkable consistency with the experimental observations that we describe next.

![Figure 1.](https://cdn.elifesciences.org/articles/77216/elife-77216-fig1-v2.jpg)

**Figure 1.:** In the left panel, each box stands for a neural population, except for P, which represents the arm and the muscles. Arrows indicate static connections, open circles show input correlation synapses, and the two colored circles show possible locations of synapses with the learning rule in Verduzco-Flores et al., 2022. In the spinal learning model the green circle connections are plastic, and the red circle connections are static. In the cortical learning model the red circle connections are plastic, whereas the green circle connections are static. In the static network all connections are static. A : afferent population.  : Somatosensory cortex, modulated by afferent input. SA : somatosensory cortex, prescribed pattern. SP : population signaling the difference between SPA and SP : primary motor cortex. SA : spinal cord. Inside the C box the circles represent the excitatory (C) and inhibitory (E) interneurons, organized into six pairs. The interneurons in each pair innervate an alpha motoneuron (I), each of which stimulates one of the six muscles in the arm, numbered from 0 to 5. The trios consisting of α, E, I units are organized into agonists and antagonists, depending on whether their α motoneurons cause torques in similar or opposite directions. These relations are shown in the right-side panel.α

## Relevant findings in motor control

Before describing our modeling approach, we summarize some of the relevant experimental data that will be important to understanding the results. We focus on three related issues: (1) the role of the spinal cord in movement, (2) the nature of representations in motor cortex, and (3) muscle synergies, and how the right pattern of muscle activity is produced.

For animals to move, spinal motoneurons must activate the skeletal muscles. In general, descending signals from the corticospinal tract do not activate the motoneurons directly, but instead provide input to a network of excitatory and inhibitory interneurons (Bizzi et al., 2000; Lemon, 2008; Arber, 2012; Asante and Martin, 2013; Alstermark and Isa, 2012; Jankowska, 2013; Wang et al., 2017; Ueno et al., 2018). Learning even simple behaviors involves long-term plasticity, both at the spinal cord (SC) circuit, and at higher regions of the motor hierarchy (Wolpaw et al., 1983; Grau, 2014; Meyer-Lohmann et al., 1986; Wolpaw, 1997; Norton and Wolpaw, 2018). Despite its obvious importance, there are comparatively few attempts to elucidate the nature of the SC computations, and the role of synaptic plasticity.

The role ascribed to SC is closely related to the role assumed from motor cortex, particularly M1. One classic result is that M1 pyramidal neurons of macaques activate preferentially when the hand is moving in a particular direction. When the preferred directions of a large population of neurons are added as vectors, a population vector appears, which points close to the hand’s direction of motion (Georgopoulos et al., 1982; Georgopoulos et al., 1986). This launched the hypothesis that M1 represents kinematic, or other high-level parameters of the movement, which are transformed into movements in concert with the SC. This hypothesis mainly competes with the view that M1 represents muscle forces. Much research has been devoted to this issue (Kakei et al., 1999; Truccolo et al., 2008; Kalaska, 2009; Georgopoulos and Stefanis, 2007; Harrison and Murphy, 2012; Tanaka, 2016; Morrow and Miller, 2003; Todorov, 2000, e.g.).

Another important observation is that the preferred directions of motor neurons cluster around one main axis. As shown in Scott et al., 2001, this suggests that M1 is mainly concerned with dynamical aspects of the movement, rather than representing its kinematics.

A related observation is that the preferred directions in M1 neurons experience random drifts that overlap learned changes (Rokni et al., 2007; Padoa-Schioppa et al., 2004). This leads to the hypothesis that M1 is a redundant network that is constantly using feedback error signals to capture the task-relevant dimensions, placing the configuration of synaptic weights in an optimal manifold.

A different perspective for studying motor cortex is to focus on how it can produce movements, rather than describing its activity (Shenoy et al., 2013). One specific proposal is that motor cortex has a collection of pattern generators, and specific movements can be created by combining their activity (Shenoy et al., 2013; Sussillo et al., 2015). Experimental support for this hypothesis came through the surprising finding of rotational dynamics in motor cortex activity (Churchland et al., 2012), suggesting that oscillators with different frequencies are used to produce desired patterns. This begs the question of how the animal chooses its desired patterns of motion.

Selecting a given pattern of muscle activation requires planning. Motor units are the final actuators in the motor system, but they number in the tens of thousands, so planning movements in this space is unfeasible. A low-dimensional representation of desired limb configurations (such as the location of the hand in Euclidean coordinates) is better. Movement generation likely involves a coordinate transformation, from the endpoint coordinates (e.g. hand coordinates) into actuator coordinates (e.g. muscle lengths), from which motor unit activation follows directly. Even using pure engineering methods, as for robot control, computing this coordinate transformation is very challenging. For example, this must overcome kinematic redundancies, as when many configurations of muscle lengths put the hand in the same location.

The issue of coordinate transformation is central for motor control (Shadmehr and Wise, 2005; Schöner et al., 2018; Valero-Cuevas, 2009; motor primitives and muscle synergies are key concepts in this discussion). Representing things as combinations of elementary components is a fundamental theme in applied mathematics. For example, linear combinations of basis vectors can represent any vector, and linear combinations of wavelets can approximate any smooth function (Keener, 1995). In motor control, this idea arises in the form of motor primitives. Motor primitives constitute a set of basic motions, such that that any movement can be decomposed into them (Giszter, 2015; Mussa–Ivaldi and Bizzi, 2000; Bizzi et al., 1991). This is closely related to the concept of synergies. The term ‘synergy’ may mean several things (Kelso, 2009; Bruton and O’Dwyer, 2018), but in this paper, we use it to denote a pattern of muscle activity arising as a coherent unit. Synergies may be composed of motor primitives, or they may be the motor primitives themselves.

A promising candidate for motor primitives comes in the form of convergent force fields, which have been observed for the hindlimbs of frogs and rats (Giszter et al., 1993; Mussa-Ivaldi et al., 1994, or in the forelimbs of monkeys Yaron et al., 2020). In experiments where the limb is held at a particular location, local stimulation of the spinal cord will cause a force to the limb’s endpoint. The collection of these force vectors for all of the limb endpoint’s positions forms a force field, and these force fields have two important characteristics: (1) they have a unique fixed point and (2) simultaneous stimulation of two spinal cord locations produces a force field which is the sum of the force fields from stimulating the two locations independently. It is argued that movement planning may be done in terms of force fields, since they can produce movements that are resistant to perturbations, and also permit a solution to the problem of coordinate transformation with redundant actuators (Mussa–Ivaldi and Bizzi, 2000).

The neural origin of synergies, and whether they are used by the motor system is a matter of ongoing debate (Tresch and Jarc, 2009; de Rugy et al., 2013; Bizzi and Cheung, 2013). To us, it is of interest that single spinal units found in the mouse (Levine et al., 2014 and monkey Takei et al., 2017) spinal cord (sometimes called Motor Synergy Encoders, or MSEs) can reliably produce specific patterns of motoneuron activation.

## Model concepts

We believe that it is impossible to understand the complex dynamical system in biological motor control without the help of computational modeling. Therefore, we set out to build a minimal model that could eventually control an autonomous agent, while still satisfying biological plausibility constraints.

Design principles and biological-plausibility constraints for neural network modeling have been proposed before (Pulvermüller et al., 2021; O’Reilly, 1998; Richards et al., 2019). Placing emphasis on the motor system, we compiled a set of characteristics that cover the majority of these constraints. Namely:

Our aim is hierarchical control of homeostatic variables, with the spinal cord and motor cortex at the bottom of this hierarchy. At first glance, spinal plasticity poses a conundrum, because it changes the effect of corticospinal inputs. Cortex is playing a piano that keeps changing its tuning. A solution comes when we consider the corticospinal loop (e.g. the long-loop reflex) as a negative control system, where the spinal cord activates the effectors to reduce an error. The role of cortex is to produce perceptual variables that are controllable, and can eventually improve homeostatic regulation. In this regard, our model is a variation of Perceptual Control Theory (Powers, 1973; Powers, 2005), but if the desired value of the controller is viewed as a prediction, then this approach resembles active inference models (Adams et al., 2013). Either way, the goal of the system is to reduce the difference between the desired and the perceived value of some variable.

If cortex creates representations for perceptual variables, the sensorimotor loop must be configured so those variables can be controlled. This happens when the error in those variables activates the muscles in a way that brings the perceived value closer to the desired value. In other words, we must find the input-output structure of the feedback controller implicit in the long-loop reflex. We have found that this important problem can be solved by the differential Hebbian learning rules introduced in Verduzco-Flores et al., 2022. We favor the hypothesis that this learning takes place is in the connections from motor cortex to interneurons and brainstem. Nevertheless, we show that all our results are valid if learning happens in the connections from sensory to motor cortex.

In the Results section we will describe our model, its variations, and how it can learn to reach. Next we will show that many phenomena described above are present in this model. These phenomena emerge from having a properly configured neural feedback controller with a sufficient degree of biological realism. This means that even if the synaptic weights of the connections are set by hand and are static, the phenomena still emerge, as long as the system is configured to reduce errors. In short, we show that a wealth of phenomena in motor control can be explained simply by feedback control in the sensorimotor loop, and that this feedback control can be configured in a flexible manner by the learning rules presented in Verduzco-Flores et al., 2022.

## Results

## A neural architecture for motor control

The model in this paper contains the main elements of the long-loop reflex, applied to the control of a planar arm using six muscles. The left panel of Figure 1 shows the architecture of the model, which contains 74 firing rate neurons organized in six populations. This architecture resembles a feedback controller that makes the activity in a neural population SA approach the activity in a different population SP.

The six firing-rate neurons (called units in this paper) in SA represent a region of somatosensory cortex, and its inputs consist of the static gamma (II) afferents. In steady state, activity of the II afferents is monotonically related to muscle length (Mileusnic et al., 2006), which in turn can be used to prescribe hand location. Other afferent signals are not provided to SA in the interest of simplicity.

SP represents a different cortical layer of the same somatosensory region as SA, where a ‘desired’ or ‘predicted’ activity has been caused by brain regions not represented in the model. Each firing rate neuron in SA has a corresponding unit in SP, and they represent the mean activity at different levels of the same microcolumn (Mountcastle, 1997). SP⁢A is a region (either in sensory or motor cortex) that conveys the difference between activities in SP and SA, which is the error signal to be minimized by negative feedback control.

Population A represents sensory thalamus and dorsal parts of the spinal cord. It contains 18 units with logarithmic activation functions, each receiving an input from a muscle afferent. Each muscle provides proprioceptive feedback from models of the Ia, Ib, and II afferents. In rough terms, Ia afferents provide information about contraction velocity, and Ib afferents signal the amount of tension in the muscle and tendons.

Population M represents motor cortex. Ascending inputs to M arise from population A, and use a variation of the input correlation learning rule (Porr and Wörgötter, 2006), where the SP⁢A inputs act as a learning signal. The input correlation rule enhances the stability of the controller. More details are presented in Methods. The SP⁢A inputs to M can either be static, or use a learning rule to be described below.

To represent positive and negative values, both M and SP⁢A use a ‘dual representation’, where each error signal is represented by two units. Let ei=sPi-sAi be the error associated with the i-th muscle. One of the two SP⁢A units representing ei is a monotonic function of max⁢(ei,0), whereas the other unit increases according to max⁢(-ei,0). These opposing inputs, along with mutual inhibition between the two units creates dynamics where sensorimotor events cause both excitatory and inhibitory responses, which agrees with experimental observations (Shafi et al., 2007; Steinmetz et al., 2019; Najafi et al., 2020), and allows transmitting ‘negative’ values using excitatory projections. Dual units in M receive the same inputs, but with the opposite sign.

Plasticity mechanisms within the sensorimotor loop should specify which muscles contract in order to reduce an error signaled by SP⁢A. We suggest that this plasticity could take place in the spinal cord and/or motor cortex. To show that our learning mechanisms work regardless of where the learning takes place, we created two main configurations of the model. In the first configuration, called the ‘spinal learning’ model, a ‘spinal’ network C transforms the M outputs into muscle stimulation. C learns to transform sensory errors into appropriate motor commands using a differential Hebbian learning rule (Verduzco-Flores et al., 2022). In this configuration, the error input to each M unit comes from one of the SP⁢A activities. A second configuration, called the ‘cortical learning’ model, has ‘all-to-all’ connections from SP⁢A to M using the differential Hebbian rule, whereas the connections from M to C use appropriately patterned static connections. Both configurations are basically the same model; the difference is that one configuration has our learning rule on the inputs to C, whereas the other has it on the inputs to M (Figure 1).

While analyzing our model we reproduced several experimental phenomena (described below). Interestingly, these phenomena did not arise because of the learning rules. To make this explicit, we created a third configuration of our model, called the ‘static network’. This configuration does not change the weight of any synaptic connection during the simulation. The initial weights were hand-set to approximate the optimal solution everywhere (see Methods). We will show that all emergent phenomena in the paper are also present in the static network.

We explain the idea behind the differential Hebbian rule as applied in the connections from M to C.C contains N interneurons, whose activity vector we denote as c=[c1,…,cN]. The input to each of these units is an M dimensional vector e=[e1,…,eM]. Each unit in C has an output ci=σ⁢(∑jωi⁢j⁢ej), where σ⁢(⋅) is a positive sigmoidal function. The inputs are assumed to be errors, and to reduce them we want ej to activate ci when ci can reduce ej. One way this could happen is when the weight ωi⁢j from ej to ci is proportional to the negative of their sensitivity derivative:(1)ωij∝−∂ej∂ci.

Assuming a monotonic relation between the motor commands and the errors, relation 1 entails that errors will trigger an action to cancel them, with some caveats considered in Verduzco-Flores et al., 2022. Synaptic weights akin to Equation 1 can be obtained using a learning rule that extracts correlations between the derivatives of ci and ej (see Methods). Using this rule, the commands coming from population C can eventually move the arm so that SA activity resembles SP activity.

C is organized to capture the most basic motifs of spinal cord connectivity using a network where balance between excitation and inhibition is crucial (Berg et al., 2007; Berg et al., 2019; Goulding et al., 2014). Each one of six α motoneurons stimulate one muscle, and is stimulated by one excitatory (C⁢E), and one inhibitory (C⁢I) interneuron. C⁢E and C⁢I stimulate one another, resembling the classic Wilson-Cowan model (Cowan et al., 2016). The trios composed of α,C⁢E, and C⁢I neurons compose a group that controls the activation of one muscle, with C⁢E and C⁢I receiving convergent inputs from M. This resembles the premotor network model in Petersen et al., 2014. (α,C⁢E,C⁢I) trios are connected to other trios following the agonist-antagonist motif that is common in the spinal cord (Pierrot-Deseilligny and Burke, 2005). This means that C⁢E units project to the C⁢E units of agonists, and to the C⁢I units of antagonists (Figure 1, right panel). When the agonist/antagonist relation is not strongly defined, muscles can be ‘partial’aASaS agonists/antagonists, or unrelated.

Connections from A to C (the ‘short-loop reflex’) use the input correlation learning rule, analogous to the connections from A to M.

Direct connections from M to alpha motoneurons are not necessary for the model to reach, but they were introduced in new versions because in higher primates these connections are present for distal joints (Lemon, 2008). Considering that bidirectional plasticity has been observed in corticomotoneural connections (Nishimura et al., 2013), we chose to endow them with the differential Hebbian rule of Verduzco-Flores et al., 2022.

Because timing is essential to support the conclusions of this paper, every connection has a transmission delay, and all firing rate neurons are modeled with ordinary differential equations.

All the results in this paper apply to the three configurations described above (spinal learning, cortical learning, and static network). To emphasize the robustness and potential of the learning mechanisms, in the Appendix we introduce two variations of the spinal learning model (in the Variations of the spinal learning model section). All results in the paper also apply to those two variations. In one of the variations (the ‘synergistic’ network), each spinal motoneuron stimulates two muscles rather than one. In the second variation (the ‘mixed errors’ network), the inputs from SP⁢A to M are not one-to-one, but instead come from a matrix that combines multiple error signals as the input to each M unit.

Since most results apply to all configurations, and since results could depend on the random initial weights, we report simulation results using three means and three standard deviations (m1±σ1⁢|m2±σ2|⁢m3±σ3), with the understanding that these three value pairs correspond respectively to the spinal learning, motor learning, and static network models. The statistics come from 20 independent simulations with different initial conditions.

A reference section in the Appendix (the Comparison of the 5 configurations section) summarizes the basic traits of all different model configurations (including the two variations of the spinal learning model), and compiles all their numerical results.

For each configuration, a single simulation was used to produce all the representative plots in different sections of the paper.

## The model can reach by matching perceived and desired sensory activity

Reaches are performed by specifying an SP pattern equal to the SA activity when the hand is at the target. The acquisition of these SP patterns is not in the scope of this paper (but see Verduzco-Flores et al., 2022).

We created a set of random targets by sampling uniformly from the space of joint angles. Using this to set a different pattern in SP every 40 s, we allowed the arm to move freely during 16 SP target presentations. To encourage exploratory movements we used noise and two additional units described in the Methods.

All model configurations were capable of reaching. To decide if reaching was learned in a trial we took the average distance between the hand and the target (the average error) during the last four target presentations. Learning was achieved when this error was smaller than 10 cm.

The system learned to reach in 99 out of 100 trials (20 for each configuration). One simulation with the spinal learning model had an average error of 14 cm during the last 4 reaches of training. To assess the speed of learning we recorded the average number of target presentations required before the error became less than 10 cm for the first time. This average number of failed reaches before the first success was: (1.8±2⁢|1.2±.9|⁢0±0).

Figure 2A shows the error through 16 successive reaches (640 s of in silico time) in a typical case for the spinal learning model. A supplementary video (Appendix 1—Video 1) shows the arm’s movements during this simulation. Figures similar to Figure 2 can be seen for all configurations as figure supplements (Figure 2—figure supplement 1) (Figure 2—figure supplement 2).

In Figure 2A, the error increases each time a new target was presented (yellow vertical lines), but as learning continues it was consistently reduced below 10 cm.

Panel B also shows the effect of learning, as the hand’s Cartesian coordinates eventually track the target coordinates whenever they change. This is also reflected as the activity in SA becoming similar to the activity in SP (panel C).

Panels D and E of Figure 2 show the activity of a few units in population M and population C during the 640 s of this training phase. During the first few reaches, M shows a large imbalance between the activity of units and their duals, reflecting larger errors. Eventually these activities balance out, leading to a more homogeneous activity that may increase when a new target appears. M1 activation patterns that produce no movement are called the null-space activity (Kaufman et al., 2014). In our case, this includes patterns where M units have the same activity as their duals. This, together with the noise and oscillations intrinsic to the system cause the activity in M and C to never disappear.

In panel E, the noise in the C units becomes evident. It can also be seen that inhibition dominates excitation (due to C⁢E to C⁢I connections), which promotes stability in the circuit.

We tested whether any of the novel elements in the model were superfluous. To this end, we removed each of the elements individually and checked if the model could still learn to reach. In conclusion, removing individual elements generally deteriorated performance, but the factor that proved essential for all configurations with plasticity was the differential Hebbian learning in the connections from M to C or from SP⁢A to M. For details, see the the Appendix section titled The model fails when elements are removed.

## Center-out reaching 1: The reach trajectories present traits of cerebellar ataxia

In order to compare our model with experimental data, after the training phase we began a standard center-out reaching task. Switching to this task merely consisted of presenting the targets in a different way, but for the sake of smoother trajectories we removed the noise from the units in C or M.

Figure 3A shows the eight peripheral targets around a hand rest position. Before reaching a peripheral target, a reach to the center target was performed, so the whole experiment was a single continuous simulation controlled by the SP pattern.

Peripheral targets were selected at random, each appearing six times. This produced 48 reaches (without counting reaches to the center), each one lasting 5 s. Panels B through D of Figure 3 show the trajectories followed by the hand in the three configurations. During these 48 reaches the average distance between the hand and the target was (3.3±.01⁢|2.9±.001|⁢2.9±.0003) centimeters.

Currently our system has neither cerebellum nor visual information. Lacking a ‘healthy’ model to make quantitative comparisons, we analyzed and compared them to data from cerebellar patients.

For the sake of stability and simplicity, our system is configured to perform slow movements. Fast and slow reaches are different in cerebellar patients (Bastian et al., 1996). Slow reaches undershoot the target, follow longer hand paths, and show movement decomposition (joints appear to move one at a time). In Figure 3 the trajectories begin close to the 135 degree axis, indicating a slower response at the elbow joint. With the parameters used, the spinal learning and cortical learning models tend to undershoot the target, whereas in the static network the hand can oscillate around the target.

The traits of the trajectories can be affected by many hyperparameters in the model, but the dominant factor seems to be the gain in the control loop. Our model involves delays, activation latencies, momentum, and interaction torques. Unsurprisingly, increasing the gain leads to oscillations along with faster reaching. On the other hand, low gain leads to slow, stable reaching that often undershoots the target. Since we do not have a cerebellum to overcome this trade off, the gain was the only hyperparameter that was manually adjusted for all configurations (See Methods). In particular, we adjusted the slope of the M and SA units so the system was stable, but close to the onset of oscillations. Gain was allowed to be a bit larger in the static network so oscillations could be observed. The figure supplements for Figure 3 shows more examples of configurations with higher gain (See Gain and oscillations in Appendix 1 for details).

The shape of the trajectory also depends on the target. Different reach directions cause different interaction forces, and encounter different levels of viscoelastic resistance from the muscles.

Figure 4 reveals that the approach to the target is initially fast, but gradually slows down. Healthy subjects usually present a bell-shaped velocity profile, with some symmetry between acceleration and deceleration. This symmetry is lost with cerebellar ataxia (Becker et al., 1991; Gilman et al., 1976).

![Figure 4.](https://cdn.elifesciences.org/articles/77216/elife-77216-fig4-v2.jpg)

**Figure 4.:** Thick lines show the average over 48 reaches (8 targets, 6 repetitions). Filled stripes show standard deviation. For the spinal and cortical learning configurations (left and center plots) the hand initially moves quickly to the target, but the direction is biased, so it needs to gradually correct the error from this initial fast approach; most of the variance in error and velocity appears when these corrections cause small-amplitude oscillations. In the case of the static network (right plots) oscillations are ongoing, leading to a large variance in velocity.

We are not aware of center-out reaching studies for cerebellar patients in the dark, but (Day et al., 1998) does examine reaching in these conditions. Summarizing its findings:

From Figures 3 and 4 we can observe constant endpoint errors when the gain is low, in the spinal and cortical learning models. Circuitous trajectories with a pronounced turn around the end of the third quarter are also observed. Individual trajectories can present variations. A higher gain, as in the static network on the right plots, can increase these variations, as illustrated in the figure supplements for Appendix 1.

## Center-out reaching 2: Directional tuning and preferred directions

To find whether directional tuning could arise during learning, we analyzed the M population activity for the 48 radial reaches described in the previous subsection.

For each of the 12 units in M, Figure 5A shows the mean firing rate of the unit when reaching each of the 8 targets. The red arrows show the Preferred Direction (PD) vectors that arise from these distributions of firing rates. For the sake of exposition, Figure 5 shows data for the simpler case of one-to-one connectivity between SP⁢A and M in the spinal learning model, but these results generalize to the case when each M unit receives a linear combination of the SP⁢A activities (the ‘mixed errors’ variation presented in the Variations of the spinal learning model section of the Appendix.)

![Figure 5.](https://cdn.elifesciences.org/articles/77216/elife-77216-fig5-v2.jpg)

**Figure 5.:** for a simulation with the spinal learning model.M(A) Average firing rate per target, and preferred direction (see Methods) for each of the 12 units in . Each polar plot corresponds to a single unit, and each of the 8 purple wedges corresponds to one of the 8 targets. The length of a wedge indicates the mean firing rate when the hand was reaching the corresponding target. The red arrow indicates the direction and relative magnitude of the PD vector. The black arrow shows the predicted PD vector, in this case just the corresponding arrows from panel B. (MB) For each muscle and target, a wedge shows the muscle’s length at rest position minus the length at the target, divided by the rest position length. The red arrow comes from the sum of the wedges taken as vectors, and represents the muscle’s direction of maximum contraction. Plots corresponding to antagonist muscles are connected by red lines. (C) Average activity of the 6  units indicating muscle tension. The black arrows come from the sum of wedges taken as vectors, showing the relation between muscle tension and preferred direction.A

We found that (11.8±.4⁢|12±0|⁢12±0) units were significantly tuned to reach direction (p<0.001, bootstrap test), with PD vectors of various lengths. The direction of the PD vectors is not mysterious. Each M unit controls the length error of one muscle. Figure 5B shows that the required contraction length depends on both the target and the muscle. The PD vectors of units 0–5 point to the targets that require the most contraction of their muscle. Units 6–11 are the duals of 0–5, and their PD is in the opposite direction. Figure 5C shows that the PD may also be inferred from the muscle activity, reflected as average tension.

In the case when each M unit receives a linear combination of SP⁢A errors, its PD can be predicted using a linear combination of the ‘directions of maximum contraction’ shown in Figure 5B, using the same weights as the SP⁢A inputs. When accounting for the length of the PD vectors, this can predict the PD angle with a coefficient of determination R2≈(.74±.18⁢|.88±.14|⁢.86±.01).

As mentioned in the Introduction, the PDs of motor cortex neurons tend to align in particular directions Scott et al., 2001. This is almost trivially true for this model, since the PD vectors are mainly produced by linear combinations of the vectors in Figure 5B.

Figure 6 shows the PD for all the M units in a representative simulation for each of the configurations. In every simulation, the PD distribution showed significant bimodality (p<0.001). The main axis of the PD distribution (see Methods) was (59±7⁢|52±2|⁢54±.5) degrees.

![Figure 6.](https://cdn.elifesciences.org/articles/77216/elife-77216-fig6-v2.jpg)

**Figure 6.:** units.MIn all three plots the arrows denote the direction and magnitude of the preferred direction (PD) for an individual unit. The gray dotted lines shows the main axis of the distribution. The red dotted lines are a 45 degree rotation of the gray line, for comparison with Scott et al., 2001. It can be seen that all configurations display a strong bimodality, especially when considering the units with a larger PD vector. The axis where the PD vectors tend to aggregate is in roughly the same position for the three configurations.

To compare with (Scott et al., 2001) we rotate this line 45 degrees so the targets are in the same position relative to the shoulder (e.g. Lillicrap and Scott, 2013 Figure 1, Kurtzer et al., 2006 Figure 1). This places the average main axes above in a range between 99 and 104 degrees, comparable to the 117 degrees in Scott et al., 2001.

The study in Lillicrap and Scott, 2013 suggested that a rudimentary spinal cord feedback system should be used to understand why the PD distribution arises. Our model is the first to achieve this.

The PD vectors are not stationary, but experience random fluctuations that become more pronounced in new environments (Rokni et al., 2007; Padoa-Schioppa et al., 2004). The brain is constantly remodeling itself, without losing the ability to perform its critical operations (Chambers and Rumpel, 2017). Our model is continuously learning, so we tested the change in the PDs by setting 40 additional center-out reaches (no intrinsic noise) after the previous experiment, once for each configuration.

To encourage changes we set 10 different targets instead of 8. After a single trial for each configuration the change in angle for the 12 PD vectors had means and standard deviations of (3.3±2.4⁢|4.9±2.1|⁢.3±.2) degrees. Larger changes (around 7 degrees) could be observed in the ‘mixed errors’ variation of the model, presented in the Appendix (Variations of the spinal learning model section). We also measured the change in the preferred directions of the muscles, obtained as in Figure 5C. This yielded differences and standard deviations (3.8±2.1⁢|6.4±2.9|⁢.2±.2) degrees.

The average distance between hand and target during the 40 reaches was (3⁢|3.6|⁢2.9) cm, showing that the hand was still moving towards the targets, although with different errors due to their new locations.

## Center-out reaching 3: Rotational dynamics

Using a dynamical systems perspective, (Shenoy et al., 2013) considers that the muscle activity c⁢(t) (a vector function of time) arises from the cortical activity vector c⁢(t) after it is transformed by the downstream circuitry:(2)m(t)=G[r(t)].

It is considered that the mapping G⁢[⋅] may consist of sophisticated controllers, but for the sake of simplicity this mapping is considered static, omitting spinal cord plasticity. The cortical activity arises from a dynamical system:(3)τr˙(t)=h(r(t))+u(t),

where u⁢(t) represents inputs to motor cortex from other areas, and h⁢(⋅) is a function that describes how the state of the system evolves.

A difficulty associated with Equation 3 is explaining how c⁢(t) generates a desired muscle pattern c⁢(t) when the function h⁢(⋅) represents the dynamics of a recurrent neural network. One possibility is that M1 has intrinsic oscillators of various frequencies, and they combine their outputs to shape the desired pattern. This prompted the search for oscillatory activity in M1 while macaques performed center-out reaching motions. A brief oscillation (in the order of 200ms, or 5 Hz) was indeed found in the population activity (Churchland et al., 2012, and the model in Sussillo et al., 2015) was able to reproduce this result, although this was done in the open-loop version of Equations 2 and 3, where u⁢(t) contains no afferent feedback (this is further commented in the Supplemental Discussion).

Recently it was shown that the oscillations in motor cortex can arise when considering the full sensorimotor loop, without the need of recurrent connections in motor cortex (Kalidindi et al., 2021). A natural question is whether our model can also reproduce the oscillations in Churchland et al., 2012 without requiring M1 oscillators or recurrent connections.

The analysis in Churchland et al., 2012 is centered around measuring the amount of rotation in the M1 population activity. The first step is to project the M1 activity vectors onto their first six principal components. These six components are then rotated so the evolution of the activity maximally resembles a pure rotation. These rotated components are called the ‘jPCA vectors’. The amount of variance in the M1 activity explained by the first two jPCA vectors is a measure of rotation. The Methods section provides more details of this procedure.

Considering that we have a low-dimensional, non-spiking, slow-reaching model, we can only expect to qualitatively replicate the essential result in Churchland et al., 2012, which is most of the variance being contained in the first jPCA plane.

We replicated the jPCA analysis, with adjustments to account for the smaller number of neurons, the slower dynamics, and the fact that there is no delay period before the reach (See Methods). The result can be observed in Figure 7, where 8 trajectories are seen in the plots. Each trajectory is the average activity of the 12 M units when reaching to one of the 8 targets, projected onto the jPCA plane. The signature of a rotational structure in these plots is that most trajectories circulate in a counterclockwise direction. Quantitatively, the first jPCA plane (out of six) captures (.42±.04⁢|.42±.04|⁢.46±.03) of the variance.

![Figure 7.](https://cdn.elifesciences.org/articles/77216/elife-77216-fig7-v2.jpg)

**Figure 7.:** Each plot shows the first two jPCA components during 0.25 s, for each of the 8 conditions/targets. Traces are colored according to the magnitude of their initial  component, from smallest (green) to largest (red).j⁢P⁢C⁢A1

With this analysis we show that our model does not require intrinsic oscillations in motor cortex to produce rotational dynamics, in agreement with (Kalidindi et al., 2021 and DeWolf et al., 2016).

## The effect of changing the mass

Physical properties of the arm can change, not only as the arm grows, but also when tools or new environments come into play. As a quick test of whether the properties in this paper are robust to moderate changes, we changed the mass of the arm and forearm from 1 to 0.8 kg and ran one simulation for each of the five configurations.

With a lighter arm the average errors during center-out reaching were (2.5⁢|3.2|⁢3) cm. The hand trajectories with a reduced mass can be seen in the top 3 plots of Figure 8. We can observe that the spinal learning model slightly reduced its mean error, whereas the cortical learning model increased it. This can be understood by noticing that a reduction in mass is akin to an increase in gain. The spinal learning model with its original gain was below the threshold of oscillations at the endpoint, and a slight mass decrease did not change this. The cortical learning model with the original gain was already oscillating slightly, and an increase in gain increased the oscillations.

![Figure 8.](https://cdn.elifesciences.org/articles/77216/elife-77216-fig8-v2.jpg)

**Figure 8.:** Plots are as in Figure 3. The spinal learning model and the static network show qualitatively similar trajectories compared to those in Figure 3. In contrast, the cortical learning model began to display considerable endpoint oscillations for several targets after its mass was reduced. These oscillations persist after the mass has been increased.

In the same simulation, after the center-out reaching was completed, we once more modified the mass of the arm and forearm, from 0.8 to 1.2 kg, after which we began the center-out reaching again. This time the center-out reaching errors were (2.4⁢|3.3|⁢2.9) cm. The hand trajectories for this high mass condition are in the bottom 3 plots in Figure 8. It can be seen that the spinal learning and cortical learning models retained their respectively improved and decreased performance, whereas the static network performed roughly the same for all mass conditions. A tentative explanation is that with reduced mass the synaptic learning rules tried to compensate for faster movements with weights that effectively increased the gain in the loop. After the mass was increased these weights did not immediately revert, leading to similar trajectories after the increase in mass.

The results of the paper still held after our mass manipulations. For all configurations, PD vectors could be predicted with a coefficient of determination between.74 and.92; All units in M were significantly tuned to direction; the main axis of the PD distribution ranged between 56 and 61 degrees, and the first jPCA plane captured between 33% and 58% of the variance.

## Spinal stimulation produces convergent direction fields

Due to the viscoelastic properties of the muscles, the mechanical system without active muscle contraction will have a fixed point with lowest potential energy at the arm’s rest position. Limited amounts of muscle contraction shift the position of that fixed point. This led us to question whether this could produce convergent force fields, which as discussed before are candidate motor primitives, and have been found experimentally.

To simulate local stimulation of an isolated spinal cord we removed all neuronal populations except for those in C, and applied inputs to the individual pairs of C⁢E,C⁢I units projecting to the same motoneuron. Doing this for different starting positions of the hand, and recording its initial direction of motion, produces a direction field. A direction field maps each initial hand location to a vector pointing in the average direction of the force that initially moves the hand.

The first two panels of Figure 9 show the result of stimulating individual E-I pairs in C, which will indeed produce direction fields with different fixed points.

![Figure 9.](https://cdn.elifesciences.org/articles/77216/elife-77216-fig9-v2.jpg)

**Figure 9.:** C1.(A) Direction Field (DF) from stimulation of the interneurons for muscle 0 (biarticular biceps). The approximate location of the fixed point is shown with a blue dot. (B) DF from stimulation of muscle 3 (biarticular triceps) interneurons. A red dot shows the fixed point. (C) Panels A and B overlapped. (D) In green, the DF from stimulating the interneurons for muscles 0 and 3 together. In purple, the sum of the DFs from panels A and B. Dots show the fixed points. The average angle between the green and purple vectors is 4 degrees.

We found that these direction fields add approximately linearly (Figure 9D). More precisely, let D⁢(a+b) be the direction field from stimulating spinal locations a and b simultaneously, and αa+b⁢(x,y) be the angle of D⁢(a+b) at hand coordinates (x,y). Using similar definitions for D⁢(a),D⁢(b),αa⁢(x,y),αb⁢(x,y), we say the direction fields add linearly if αa+b⁢(x,y)=αa⁢(x,y)+αb⁢(x,y),∀(x,y).

We define the mean angle difference between D⁢(a+b) and D⁢(a)+D⁢(b) as(4)γa,b=∑x,yαa+b(x,y)−(αa(x,y)+αb(x,y))Ns,

where Ns is the number of (x,y) sample points. We found that when averaged over the 15 (C1) or 144 (C2) possible (a,b) pairs, the mean of γa,b was 13.5 degrees.

Randomly choosing two possibly different pairs (a,b) and (c,d) for the stimulation locations leads to a mean angle difference of 37.6 degrees between the fields D⁢(a+b) and D⁢(c)+D⁢(d). A bootstrap test showed that these angles are significantly larger (p<0.0001) than in the previous case where (a,b)=(c,d).

The resting field is defined as the direction field when no units are stimulated. Removing the resting field from D⁢(a+b),D⁢(a), and D⁢(b) does not alter these results.

Recent macaque forelimb experiments (Yaron et al., 2020) show that the magnitude of the vectors in the D⁢(a+b) fields is larger than expected from D⁢(a)+D⁢(b) (supralinear summation). We found no evidence for this effect, suggesting that it depends on mechanisms beyond those present in our model.

## Discussion

## Summary of findings and predictions

We have presented a model of the long loop reflex with a main assumption: negative feedback configured with two differential Hebbian learning rules. One novel rule sets the loop’s input-output structure, and the other rule (input correlation) promotes stability. We showed that this model can make arm reaches by trying to perceive a given afferent pattern.

Our study made two main points:

The first main point above was made using a feedback control network with no learning (called the static network in the Results). We showed that in this static network: (1) reaching trajectories are similar to models of cerebellar ataxia, (2) motor cortex units are tuned to preferred directions, (3) those preferred directions follow a bimodal distribution, (4) motor cortex units present rotational dynamics, (5) reaching is still possible when mass is altered, and (6) spinal stimulation produces convergent direction fields.

The second main point was made using two separate models, both using the same differential Hebbian learning rules, but applied at different locations. The spinal learning model presents the hypothesis that the spinal cord learns to adaptively configure the input-output structure of the feedback controller. The cortical learning model posits that configuring this structure could instead be a function of motor cortex; this would not disrupt our central claims. These two models should not be considered as incompatible hypotheses. Different elements performing overlapping functions are common in biological systems (Edelman and Gally, 2001).

Two variations of the spinal learning model in the Appendix show that this learning mechanism is quite flexible, opening the doors for certain types of synergies, and for more complex errors (that still maintian the constraint of monotonicity).

We list some properties of the model, and possible implications:

Since our relatively simple model reproduces these phenomena, we believe it constitutes a good null hypothesis for them. But beyond explaining experimental observations, this model makes inroads into the hard problem of how the central nervous system (CNS) can generate effective control signals, recently dubbed the ‘supraspinal pattern formation’ problem (Bizzi and Ajemian, 2020). From our perspective, the CNS does not need to generate precise activation patterns for muscles and synergies; it needs to figure out which perceptions need to change. It is subcortical structures that learn the movement details. The key to make such a model work is the differential Hebbian learning framework in Verduzco-Flores et al., 2022, which handles the final credit assignment problem.

We chose not to include a model of the cerebellum at this stage. Our model reflects the brain structure of an infant baby who can make clumsy reaching movements. At birth the cerebellum is incomplete and presumably not functional. It requires structured input from spinal cord and cortex to establish correct synaptic connections during postnatal development and will contribute to smooth reaching movements at a later age.

Encompassing function, learning, and experimental phenomena in a single simple model is a promising start towards a more integrated computational neuroscience. We consider that such models have the potential to steer complex large-scale models so they can also achieve learning and functionality from scratch.

## Methods

Simulations were run in the Draculab simulator (Verduzco-Flores and De Schutter, 2019). All the parameters from the equations in this paper are presented in the Appendix. Parameters not shown can be obtained from Python dictionaries in the source code. This code can be downloaded from: https://gitlab.com/sergio.verduzco/public_materials/-/tree/master/adaptive_plasticity.

## Unit equations

With the exception of the A and SP populations, the activity ui of any unit in Figure 1 has dynamics:(5)τuui˙=σ(I)−ui,(6)σ(I)=11+exp⁡(β(I−η)),

where τ is a time constant, β is the slope of the sigmoidal function, η is its threshold, and I=∑jωi⁢j⁢uj⁢(t-Δ⁢tj) is the sum of delayed inputs times their synaptic weights.

Units in the C⁢E,C⁢I populations (in the spinal learning model) or in M (in the cortical learning model) had an additional noise term, which turned Equation 5 into this Langevin equation:(7)dui(t)=1τu(σ(I)−ui(t))+ςdW(t),

where W⁢(t) is a Wiener process with unit variance, and ς is a parameter to control the noise amplitude. This equation was solved using the Euler-Maruyama method. All other unit equations were integrated using the forward Euler method. The equations for the plant and the muscles were integrated with SciPy’s (https://scipy.org/) explicit Runge-Kutta 5(4) method.

Units in the A population use a rectified logarithm activation function, leading to these dynamics for their activity:(8)τaa˙=log⁡([1+I−T]+)−a,

where τa is a time constant, I is the scaled sum of inputs, T is a threshold, and [x]+=max(x,0) is the "positive part" function.

## Learning rules

The learning rule for the connections from M to C⁢E,C⁢I units in the spinal learning model was first described in Verduzco-Flores et al., 2022. It has an equation:(9)ω˙i⁢j⁢(t)=-(e¨j⁢(t)-⟨e¨⁢(t)⟩)⁢(c˙i⁢(t-Δ⁢t)-⟨c˙⁢(t-Δ⁢t)⟩).

In this equation, ej⁢(t) represents the activity of the j-th unit in M at time t, and e¨j⁢(t) is its second derivative. Angle brackets denote averages, so that ⟨e¨⟩≡1NM⁢∑ke¨k, where NM is the number of M units. c˙i⁢(t) is the derivative of the activity for the postsynaptic unit, and Δ⁢t is a time delay ensuring that the rule captures the proper temporal causality. In the Supplementary Discussion of the Appendix we elaborate on how such a learning rule could be present in the spinal cord.

The learning rule in 9 was also fitted with soft weight-bounding to prevent connections from changing sign, and multiplicative normalization was used to control the magnitude of the weights by ensuring two requirements: (1) all weights from projections of the same M unit should add to ws⁢a, (2) all weights ending at the same C unit should add to ws⁢b. With this, the learning rule adopted the form:(10)ω˙ij=−αωij(−Δ+λ[(0.5(ζsa+ζsb)−1)]),

In this equation α is a constant learning rate, Δ is the right-hand side expression of Equation 9, and λ is a scalar parameter. The value ζs⁢a is ws⁢a divided by the sum of outgoing weights from the j-th M unit, and ζs⁢b is ws⁢b divided by the sum of incoming M weights on ci. This type of normalization is meant to reflect the competition for resources among synapses, both at the presynaptic and postsynaptic level.

The synapses in the connections from A to M and from A to C used the input correlation rule (Porr and Wörgötter, 2006):(11)w˙=αICwIAI˙PA,

where IA is the scaled sum of inputs from the A population, αI⁢C is the learning rate, IP⁢A is the scaled sum of inputs from SP⁢A or M, and I˙P⁢A is its derivative. Unlike the original input correlation rule, this rule uses soft weight bounding to avoid weights changing signs. Moreover, the sum of the weights was kept close to a ωs value. In practice this meant dividing the each individual w value by the sum of weights from A-to-M (or A-to-C) connections, and multiplying times ωs at each update. In addition, weight clipping was used to keep individual weights below a value ωm⁢a⁢x.

The learning rule in the cortical learning model was the same, but the presynaptic units were in SP⁢A, and the postsynaptic units in M.

## Exploratory mechanism

Without any additional mechanisms the model risked getting stuck in a fixed arm position before it could learn. We included two mechanisms to permit exploration in the system. We describe these two mechanisms as they were applied to the spinal learning model and its two variations. The description below also applies to the case of the cortical learning model, with the M units (instead of the C units) receiving the noise and extra connections.

The first exploratory mechanism consists of intrinsic noise in the C⁢E and C⁢I interneurons, which causes low-amplitude oscillations in the arm. We have observed that intrinsic oscillations in the C⁢E,C⁢I units are also effective to allow learning (data not shown), but the option of intrinsic noise permits the use of simple sigmoidal units in C, and contributes to the discussion regarding the role of noise in neural computation.

The second mechanism for exploration consists of an additional unit, called A⁢C⁢T. This unit acted similarly to a leaky integrator of the total activity in SP⁢A, reflecting the total error. If the leaky integral of the SP⁢A activity crossed a threshold, then A⁢C⁢T would send a signal to all the C⁢E and C⁢I units, causing adaptation. The adaptation consisted of an inhibitory current that grew depending on the accumulated previous activity.

To model this, C⁢E and C⁢I units received an extra input Ia⁢d⁢a⁢p⁢t. When the input from the A⁢C⁢T unit was larger than 0.8, and Iadapt<0.2, the value of Ia⁢d⁢a⁢p⁢t would be set to (uis⁢l⁢o⁢w)2. This is the square of a low-passed filtered version of ui. More explicitly,(12)τs⁢l⁢o⁢w⁢u˙is⁢l⁢o⁢w=ui-uis⁢l⁢o⁢w.

If the input from A⁢C⁢T was smaller than 0.8, or Ia⁢d⁢a⁢p⁢t became larger than 0.2, then Ia⁢d⁢a⁢p⁢t would decay towards zero:(13)τs⁢l⁢o⁢w⁢I˙a⁢d⁢a⁢p⁢t=-Ia⁢d⁢a⁢p⁢t.

With this mechanism, if the arm got stuck then error would accumulate, leading to adaptation in the spinal interneurons. This would cause the most active interneurons to receive the most inhibition, shifting the ‘dominant’ activities, and producing larger amplitude exploratory oscillations.

When a new target is presented, A⁢C⁢T must reset its own activity back to a low value. Given our requirement to fully implement the controller using neural elements, we needed a way to detect changes in SP. A unit denominated C⁢H⁢G can detect these changes using synapses that react to the derivative of the activity in SP units. C⁢H⁢G was connected to A⁢C⁢T in order to reset its activity.

More precisely, when inputs from C⁢H⁢G were larger than 0.1, the activity of A⁢C⁢T had dynamics:(14)a˙(t)=−40a(t).

Otherwise it had these dynamics:(15)a˙(t)=a(t)(σ(I)−θACT), if σ(I)<θACT,(16)τA⁢C⁢T⁢a˙⁢(t)=(σ⁢(I)-θA⁢C⁢T)⁢[1-a⁢(t)+γ⁢σ˙⁢(I)], otherwise.

As before, σ⁢(⋅) is a sigmoidal function, and I is the scaled sum of inputs other than C⁢H⁢G. When σ⁢(I) is smaller than a threshold θA⁢C⁢T the value of a actually decreases, as this error is deemed small enough. When σ(I)>θACT the activity increases, but the rate of increase is modulated by a rate of increase σ˙⁢(I)≡σ⁢(I)-σ⁢(I~), where I~ is a low-pass filtered version of I is a constant parameter.

C⁢H⁢G was a standard sigmoidal unit receiving inputs from SP, with each synaptic weight obeying this equation:(17)ωj(t)=α|s˙j(t)|−ωj(t),

where sj represents the synapse’s presynaptic input.

## Plant, muscles, afferents

The planar arm was modeled as a compound double pendulum, where both the arm and forearm were cylinders with 1 kg. of mass. No gravity was present, and a moderate amount of viscous friction was added at each joint (3 N⁢m⁢sr⁢a⁢d). The derivation and validation of the double pendulum’s equations can be consulted in a Jupyter notebook included with Draculab’s source code (in the tests folder).

The muscles used a standard Hill-type model, as described in Shadmehr and Wise, 2005, Pg. 99. The muscle’s tension T obeys:(18)T˙=KSEb[g⋅I+KPEΔx+bx˙−(1+KPEKSE)T],

where I is the input, g an input gain, KP⁢E the parallel elasticity constant, KS⁢E the series elasticity constant, b is the damping constant for the parallel element, x is the length of the muscle, and Δ⁢x=x-x1*-x2*. In here, x1* is the resting length of the series element, whereas x2* is the resting length of the parallel element. All resting lengths were calculated from the steady state when the hand was located at coordinates (0.3, 0.3).

We created a model of the Ia and II afferents using simple structural elements. This model includes, for each muscle one dynamic nuclear bag fiber, and one static bag fiber. Both of these fibers use the same tension equation as the muscle, but with different parameters. For the static bag fiber:(19)T˙s=KSEsbs[KPEsΔx+bsx˙−(1+KPEsKSEs)Ts].

The dynamic bag fiber uses the same equation, with the s superscript replaced by d. No inputs were applied to the static or dynamic bag fibers, so they were removed from these equations. The rest lengths of the static and dynamic bag fibers where those of their corresponding muscles times factors l0s,l0d, respectively.

The Ia afferent output is proportional to a linear combination of the lengths for the serial elements in both dynamic and static bag fibers. The II output has two components, one proportional to the length of the serial element, and one approximately proportional to the length of the parallel element, both in the static bag fiber. In practice this was implemented through the following equations:(20)Ia=gIa[(fsIaKSEs)Ts+(1−fsIaKSEd)Td],(21)II=gII[(fsIIKSEs)Ts+(1−fsIIKPEs)(Ts−bsx˙)].

In here, gIa and gI⁢I are gain factors. fsIa and fsI⁢I are constants determining the fraction of Ia and I⁢I output that comes from the serial element.

The model of the Golgi tendon organ producing the Ib outputs was taken from Lin and Crago, 2002. First, a rectified tension was obtained as:(22)r=gIblog⁡(T+/T0+1).

gIb is a gain factor, T0 is a constant that can further alter the slope of the tension, and T+=max⁡(T,0) is the tension, half-rectified. The Ib afferent output followed dynamics:(23)τIbI˙b=r−Ib.

## Static connections

In all cases, the connections to SA used one-to-one connectivity with the A units driven by the II afferents, whereas connections from A to M and C used all-to-all projections from the units driven by the Ia and Ib afferents. Projections from SA to SP⁢A used one-to-one excitatory connections to the first 6 units, and inhibitory projections to the next six units. Projections from SP to SP⁢A used the opposite sign from this.

Connections from SP⁢A to M were one-to-one, so the j-th unit in SP⁢A only sent a projection to unit j in M. A variation of this connectivity is presented in the Appendix (See Variations of the spinal learning model).

We now explain how we adjusted the synaptic weights of the static network. To understand the projections from M to C and to the alpha motoneurons it is useful to remember that each C⁢E,C⁢I,α trio is associated with one muscle, and the M units also control the error of a single muscle. This error indicates that the muscle is longer than desired. Thus, the M unit associated with muscle i sent excitatory projections to the C⁢E and α units associated with muscle i, and to the C⁢I units of the antagonists of i. Additionally, weaker projections were sent to the C⁢E,α units of muscle i’s agonists. Notice that only excitatory connections were used.

The reverse logic was used to set the connections from A to C and M. If muscle i is tensing or elongating, this can predict an increase in the error for its antagonists, which is the kind of signal that the input correlation rule is meant to detect. Therefore, the I⁢b afferent (signaling tension) of muscle i sent an excitatory signal to the C⁢I unit associated with muscle i, and to the C⁢E,α units associated with i’s antagonists. Moreover, this I⁢b afferent also sent an excitatory projection to the dual of the M unit associated with muscle i. Connections from I⁢a afferents (roughly signaling elongation speed) followed the same pattern, but with slightly smaller connection strengths.

## Rotational dynamics

We explain the method to project the activity of M onto the jPCA plane. For all units in M we considered the activity during a 0.5 s sample beginning 50 ms after the target onset. Unlike (Churchland et al., 2012), we did not apply PCA preprocessing, since we only have 12 units in M. Let mi,j,k,t be the activity at time t of the unit i in M, when reaching at target j for the k-th repetition. By mi,j,⟨k⟩,t we denote the average over all repeated reaches to the same target, and by mi,⟨j⟩,⟨k⟩,t we indicate averaging over both targets and repetitions. The normalized average trace per condition is defined as: mi,j⁢(t)≡mi,j,⟨k⟩,t-mi,⟨j⟩,⟨k⟩,t. Let I stand for the number of units in M, T for the number of time points, and J for the number of targets. Following (Churchland et al., 2012), we unroll the set of mi,j⁢(t) values into a matrix X∈RJ⁢T×I, so we may represent the data through a matrix M that provides the least-squares solution to the problem X˙=X⁢M. This solution comes from the equation M^=(XT⁢X)-1⁢XT⁢X˙. Furthermore, this matrix can be decomposed into symmetric and anti-symmetric components Ms⁢y⁢m⁢m=(M^+M^T)/2,Ms⁢k⁢e⁢w=(M^-M^T)/2. The jPCA plane comes from the complex conjugate eigenvalues of Ms⁢k⁢e⁢w.

In practice, our source code follows the detailed explanation provided in the Supplementary Information of Churchland et al., 2012, which reformulates this matrix problem as a vector problem.

## Parameter search

We kept all parameter values in a range where they still made biological sense. Parameter values that were not constrained by biological data were adjusted using a genetic algorithm, and particle swarm optimization (PSO). We used a separate optimization run for each one of the configurations, consisting of roughly 30 iterations of the genetic and PSO algorithms, with populations sizes of 90 and 45 individuals respectively. After this we manually adjusted the gain of the control loop by increasing or decreasing the slope of the sigmoidal units in the M and SA populations. This is further described in the Appendix (Gain and oscillations section).

The parameters used can affect the results in the paper. We chose parameters that minimized either the error during the second half of the learning phase, or the error during center-out reaching. Both of these measures are agnostic to the other results.

## Preferred direction vectors

Next we describe how PD vectors were obtained for the M units.

Let mj⁢k denote the firing rate of the j-th M unit when reaching for the k-th target, averaged over 4 s, and across reaches to the same target. We created a function hj:ℝ2→ℝ that mapped the X,Y coordinates of each target to its corresponding mj⁢k value, but in the domain of hj the coordinates were shifted so the center location was at the origin.

Next we approximated hj with a plane, using the least squares method, and obtained a unit vector uj normal to that plane, starting at the intersection of the z-axis and the plane, and pointing towards the XY plane. The PD vector was defined as the projection of uj on the XY plane.

In order to predict the PD vectors, we first obtained for each muscle the ‘direction of maximum contraction’, verbally described in panel B of Figure 5. More formally, let li⁢k denote the length of the i-th muscle when the hand is at target k, and let li0 denote its length when the hand is at the center location. With r¯k we denote the unit vector with base at the center location, pointing in the direction of the k-th target. The direction of maximum length change for the i-th muscle comes from the following vector sum:(24)v¯i=∑k=18[li0−likli0]+r¯k,

where [x]+=max⁡(x,0).

For the j-th unit in M, its predicted PD vector comes from a linear combination of the v¯i vectors. Let the input to this unit be ∑iwj⁢i⁢ei, where ei is the output of the i-th SPF unit (representing the error in the i-th muscle). The predicted PD vector is:(25)d¯j=∑i=05wjiv¯i

To obtain the main axis of the PD distribution, the i-th PD vector was obtained in the polar form (ri,θi), with θ∈[−π,π]. We reflected vectors in the lower half using the rule: θi*=θi+π if θi<0,θi∗=θi otherwise. The angle of the main axis was the angle of the average PD vector using these modified angles: θm⁢a⁢i⁢n=arctan⁡(∑iri⁢sin⁡θi*∑iri⁢cos⁡θi*).

## Statistical tests

To find whether M units were significantly tuned to the reach direction we used a bootstrap procedure. For each unit we obtained the length of its PD vector 10,000 times when the identity of the target for each reach was randomly shuffled. We considered there was significant tuning when the length of the true PD vector was longer than 99.9% of these random samples.

To obtain the coefficient of determination for the predicted PD angles, let θt⁢r⁢u⁢ej denote the angle of the true PD for the j-th M unit, and θp⁢r⁢e⁢dj be the angle of its predicted PD. We obtained residuals for the angles as ϵj=θt⁢r⁢u⁢ej-θp⁢r⁢e⁢dj, where this difference is actually the angle of the smallest rotation that turns one angle into the other. Each residual was then scaled by the norm of its corresponding PD vector, to account for the fact that these were not homogeneous. Denoting these scaled residuals as ϵj* the residual sum of squares is S⁢Sr⁢e⁢s=∑j(ϵj*)2. The total sum of squares was: S⁢St⁢o⁢t=∑j(θt⁢r⁢u⁢ej-θ¯t⁢r⁢u⁢e)2, where θ¯t⁢r⁢u⁢e is the mean of the θt⁢r⁢u⁢ej angles. The coefficient of determination comes from the usual formula R2=1-S⁢Sr⁢e⁢sS⁢St⁢o⁢t.

To assess bimodality of the PD distribution we used a version of the Rayleigh statistic adapted to look for bimodal distributions where the two modes are oriented at 180 degrees from each other, introduced in Lillicrap and Scott, 2013. This test consists of finding an modified Rayleigh r statistic defined as:(26)r=1N((∑i=1Ncos(2ϕi))2+(∑i=1Ncos(2ϕi))2),

where the ϕi angles are the angles for the PDs. A bootstrap procedure is then used, where this r statistic is produced 100,000 times by sampling from the uniform distribution on the (0,π) interval. The PD distribution was deemed significantly bimodal if its r value was larger than 99.9% of the random r values.

We used a bootstrap test to find whether there was statistical significance to the linear addition of direction fields. To make this independent of the individual pair of locations stimulated, we obtained the direction fields for all 15 possible pairs of locations, and for each pair calculated the mean angle difference between D⁢(a+b) and D⁢(a)+D⁢(b) as described in the main text. We next obtained the mean of these 15 average angle deviations, to obtain a global average angle deviation γg⁢l⁢o⁢b⁢a⁢l.

We then repeated this procedure 400 times when the identities of the stimulation sites a,b were shuffled, to obtain 400 global average angle deviations γg⁢l⁢o⁢b⁢a⁢lj. We declared statistical significance if γg⁢l⁢o⁢b⁢a⁢l was smaller than 99% of the γg⁢l⁢o⁢b⁢a⁢lj values.
