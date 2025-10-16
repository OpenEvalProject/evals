# RatInABox, a toolkit for modelling locomotion and neuronal activity in continuous environments

## Authors

- Tom M George<sup>1</sup> ([ORCID: 0000-0002-4527-8810](https://orcid.org/0000-0002-4527-8810)) †
- Mehul Rastogi<sup>1</sup>
- William John de Cothi<sup>2</sup>
- Claudia Clopath<sup>1</sup> ([ORCID: 0000-0003-4507-8648](https://orcid.org/0000-0003-4507-8648))
- Kimberly Stachenfeld<sup>4</sup>
- Caswell Barry<sup>2</sup>

### Affiliations

1. https://ror.org/02jx3x895 Sainsbury Wellcome Centre, University College London London United Kingdom
2. https://ror.org/02jx3x895 Department of Cell and Developmental Biology, University College London London United Kingdom
3. https://ror.org/041kmwe10 Department of Bioengineering, Imperial College London London United Kingdom
4. Google DeepMind London United Kingdom
5. https://ror.org/00hj8s172 Columbia University New York United States

† Corresponding author

## Abstract

Generating synthetic locomotory and neural data is a useful yet cumbersome step commonly required to study theoretical models of the brain’s role in spatial navigation. This process can be time consuming and, without a common framework, makes it difficult to reproduce or compare studies which each generate test data in different ways. In response, we present RatInABox, an open-source Python toolkit designed to model realistic rodent locomotion and generate synthetic neural data from spatially modulated cell types. This software provides users with (i) the ability to construct one- or two-dimensional environments with configurable barriers and visual cues, (ii) a physically realistic random motion model fitted to experimental data, (iii) rapid online calculation of neural data for many of the known self-location or velocity selective cell types in the hippocampal formation (including place cells, grid cells, boundary vector cells, head direction cells) and (iv) a framework for constructing custom cell types, multi-layer network models and data- or policy-controlled motion trajectories. The motion and neural models are spatially and temporally continuous as well as topographically sensitive to boundary conditions and walls. We demonstrate that out-of-the-box parameter settings replicate many aspects of rodent foraging behaviour such as velocity statistics and the tendency of rodents to over-explore walls. Numerous tutorial scripts are provided, including examples where RatInABox is used for decoding position from neural data or to solve a navigational reinforcement learning task. We hope this tool will significantly streamline computational research into the brain’s role in navigation.

## Introduction

Computational modelling provides a means to understand how neural circuits represent the world and influence behaviour, interfacing between experiment and theory to express and test how information is processed in the brain. Such models have been central to understanding a range of neural mechanisms, from action potentials (Hodgkin and Huxley, 1952) and synaptic transmission between neurons (del Castillo and Katz, 1954), to how neurons represent space and guide complex behaviour (Hartley et al., 2000; Hartley et al., 2004; Byrne et al., 2007; Banino et al., 2018; de Cothi et al., 2022). Relative to empirical approaches, models can offer considerable advantages, providing a means to generate large amounts of data quickly with limited physical resources, and are a precise means to test and communicate complex hypotheses. To fully realise these benefits, computational modelling must be accessible and standardised, something which has not always been the case.

Spurred on by the proposition of a ‘cognitive map’ (Tolman and Honzik, 1930), and the discovery of neurons with position-(O’Keefe and Dostrovsky, 1971), velocity-(Sargolini et al., 2006; Kropff et al., 2015) and head direction-(Taube et al., 1990) selective receptive fields in the hippocampal formation, understanding the brain’s role in navigation and spatial memory has been a key goal of the neuroscience, cognitive science, and psychology communities. In this field, it is common for theoretical or computational models to rely on artificially generated data sets. For example, for the direct testing of a normative model, or to feed a learning algorithm with training data from a motion model used to generate a time series of states, or feature-vectors. Not only is this data more cost-effective, quicker to acquire, and less resource-intensive than conducting spatial experiments (no rats required), but it also offers the advantage of being flexibly hand-designed to support the validation or refutation of theoretical propositions. Indeed, many past (Mehta et al., 2000; Burak et al., 2009; Gustafson and Daw, 2011) and recent (Stachenfeld et al., 2017; de Cothi and Barry, 2020; Bono et al., 2023; George et al., 2022; Banino et al., 2018; Schaeffer et al., 2022; Benna and Fusi, 2021) models have relied on artificially generated movement trajectories and neural data.

Artificially generating data can still be a bottleneck in the scientific process. We observe a number of issues: First, the lack of a universal standard for trajectory and cell activity modelling hinders apples-to-apples comparisons between theoretical models whose conclusions may differ depending on the specifics of the models being used. Secondly, researchers must begin each project reinventing the wheel, writing software capable of generating pseudo-realistic trajectories and neural data before the more interesting theoretical work can begin. Thirdly, inefficiently written software can significantly slow down simulation time or, worse, push users to seek solutions which are more complex and power-intensive (multithreading, GPUs, etc.) than the underlying task requires, decreasing reproducibility. Finally, even the relatively modest complexities of motion modelling in continuous environments raises the technical entry barrier to computational research and can impel researchers towards studying only one-dimensional environments or biologically unrealistic ‘gridworlds’ with tabularised state spaces. Not only can gridworld models scale poorly in large environments but they typically disregard aspects of motion which can be non-trivial, for example speed variability and inertia. Whilst there are valid reasons why gridworld and/or tabularised state-space models may be preferred – and good open source packages for modelling this (Maxime et al., 2023; Juliani et al., 2022) – we suspect that coding simplicity, rather than theory-based justifications, remain a common reason these are used over continuous analogs.

To overcome these issues we built RatInABox (https://github.com/RatInABox-Lab/RatInABox) (George, 2022): an open source Python toolkit for efficient and realistic motion modelling in complex continuous environments and concurrent simulation of neuronal activity data for many cell types including those typically found in the hippocampal formation (Figure 1).

![Figure 1.](https://cdn.elifesciences.org/articles/85274/elife-85274-fig1-v1.jpg)

**Figure 1.:** (a) One minute of motion in a 2D Environment with a wall. By default the Agent follows a physically realistic random motion model fitted to experimental data. (b) Premade neuron models include the most commonly observed position/velocity selective cells types (6 of which are displayed here). Users can also build more complex cell classes based on these primitives. Receptive fields interact appropriately with walls and boundary conditions. (c) As the Agent explores the Environment, Neurons generate neural data. This can be extracted for downstream analysis or visualised using in-built plotting functions. Solid lines show firing rates, and dots show sampled spikes. (d) One minute of random motion in a 1D environment with solid boundary conditions. (e) Users can easily construct complex Environments by defining boundaries and placing walls, holes and objects. Six example Environments, some chosen to replicate classic experimental set-ups, are shown here.

## RatInABox

RatInABox is an open source software package comprising three component classes:

A typical workflow would be as follows: Firstly, an Environment is initialised with parameters specifying its dimensionality, size, shape and boundary conditions. Walls, holes and objects (which act as ‘visual cues’) can be added to make the Environment more complex. Secondly, an Agent is initialised with parameters specifying the characteristics of its motion (mean/standard deviation of its speed and rotational velocity, as well as behaviour near walls). Thirdly, populations of Neurons are initialised with parameters specifying their characteristics (number of cells, receptive field parameters, maximum firing rates etc.).

Next, a period of simulated motion occurs: on each step the Agent updates its position and velocity within the Environment, given the duration of the step, and Neurons update their firing rates to reflect the new state of the Agent. After each step, data (timestamps, position, velocities, firing rates and spikes sampled according to an inhomogenous Poisson process) are saved into their respective classes for later analysis, Figure 1.

RatInABox is fundamentally continuous in space and time. Position and velocity are never discretised but are instead stored as continuous values and used to determine cell activity online, as exploration occurs. This differs from other models which are either discrete (e.g. ‘gridworld’ or Markov decision processes) (Maxime et al., 2023; Juliani et al., 2022) or approximate continuous rate maps using a cached list of rates precalculated on a discretised grid of locations (de Cothi and Barry, 2020). Modelling time and space continuously more accurately reflects real-world physics, making simulations smooth and amenable to fast or dynamic neural processes which are not well accommodated by discretised motion simulators. Despite this, RatInABox is still fast; to simulate 100 PlaceCells for 10 min of random 2D motion (dt = 0.1 s) it takes about 2 s on a consumer grade CPU laptop (or 7 s for boundary vector cells).

By default the Agent follows a temporally continuous smooth random motion model, closely matched to the statistics of rodent foraging in an open field (Sargolini et al., 2006, Figure 2); however, functionality is also provided for non-random velocity control via a user provided control signal or for the Agent to follow an imported trajectory (Figure 3a). Once generated, data can be plotted using in-built plotting functions (which cover most of the figures in this manuscript) or extracted to be used in the theoretical model being constructed by the user.

![Figure 2.](https://cdn.elifesciences.org/articles/85274/elife-85274-fig2-v1.jpg)

**Figure 2.:** (a) An example 5-min trajectory from the Sargolini et al., 2006. dataset. Linear velocity (Rayleigh fit) and rotational velocity (Gaussian fit) histograms and the temporal autocorrelations (exponential fit) of their time series’. (b) A sampled 5-min trajectory from the RatInABox motion model with parameters matched to the Sargolini data. (c) Figure reproduced from Figure 8D in Satoh et al., 2011 showing 10 min of open-field exploration. ‘Thigmotaxis’ is the tendency of rodents to over-explore near boundaries/walls and has been linked to anxiety. (d) RatInABox replicates the tendency of agents to over-explore walls and corners, flexibly controlled with a ‘thigmotaxis’ parameter. (e) Histogram of the area-normalised time spent in annuli at increasing distances, , from the wall. RatInABox and real data are closely matched in their tendency to over-explore locations near walls without getting too close.d

![Figure 3.](https://cdn.elifesciences.org/articles/85274/elife-85274-fig3-v1.jpg)

**Figure 3.:** (a) Low temporal-resolution trajectory data (2 Hz) imported into RatInABox is upsampled (‘augmented’) using cubic spline interpolation. The resulting trajectory is a close match to the ground truth trajectory (Sargolini et al., 2006) from which the low resolution data was sampled. (b) Movement can be controlled by a user-provided ‘drift velocity’ enabling arbitrarily complex motion trajectories to be generated. Here, we demonstrate how circular motion can be achieved by setting a drift velocity (grey arrows) which is tangential to the vector from the centre of the Environment to the Agent’s position. (c) Egocentric VectorCells can be arranged to tile the Agent’s field of view, providing an efficient encoding of what an Agent can ‘see’. Here, two Agents explore an Environment containing walls and an object. Agent-1 (purple) is endowed with three populations of Boundary- (grey), Object- (red), and Agent- (green) selective field of view VectorCells. Each circle represents a cell, its position (in the head-centred reference frame of the Agent) corresponds to its angular and distance preferences and its shading denotes its current firing rate. The lower panel shows the firing rate of five example cells from each population over time. (d) A Neurons class containing a feed forward neural network learns, from data collect online over a period of 300 min, to approximate a complex target receptive field from a set of grid cell inputs. This demonstrates how learning processes can be incorporated and modelled into RatInABox. (e) RatInABox used in a simple reinforcement learning example. A policy iteration technique converges onto an optimal value function (heatmap) and policy (trajectories) for an Environment where a reward is hidden behind a wall. State encoding, policy control and the Environment are handled naturally by RatInABox. (f) Compute times for common RatInABox (purple) and non-RatInABox (red) operations on a consumer grade CPU. Updating the random motion model and calculating boundary vector cell firing rates is slower than place or grid cells (note log-scale) but comparable, or faster than, size-matched non-RatInABox operations. Inset shows how the total update time (random motion model and place cell update) scales with the number of place cells.

## Intended use-cases

RatInABox can be used whenever locomotion and/or populations of cells need to be modelled in continuous one- or two-dimensional environments. These functionalities are coupled (locomotion directly adjusts the cell firing rates) but can also be used independently (for example an Environment and Agent can be modelled without any Neurons if users only require the motion model, or alternatively users can calculate cell activity on an imported trajectory without using the random motion model).

We envisage use cases falling into two broad categories. (i) Data generation: The user is interested in generating realistic trajectories and/or neural data for use in a downstream analysis or model training procedure (Lee et al., 2023). (ii) Advanced modelling: The user is interested in building a model of the brain’s role in navigation (George et al., 2023), including how behaviour and neural representations mutually interact.

Below we briefly describe the most important details and features of RatInABox, divided into their respective classes. We leave all mathematical details to the Methods. Additional details (including example scripts and figures) can be found in the supplementary material and on the GitHub repository. The codebase itself is comprehensively documented and can be referenced for additional understanding where necessary.

## The Environment

Unlike discretised models, where environments are stored as sets of nodes (‘states’) connected by edges (‘actions’)(Juliani et al., 2022), here Environments are continuous domains containing walls (1D line segments through which locomotion is not allowed) and objects (which are 0-dimensional and act as visual cues). Boundaries and visual cues are thought to provide an important source of sensory data into the hippocampus (O’Keefe and Burgess, 1996; Hartley et al., 2000; Barry et al., 2006; Solstad et al., 2008) and play an important role in determining cell activity during navigation (Stachenfeld et al., 2017; de Cothi and Barry, 2020). An Environment can have periodic or solid boundary conditions and can be one- or two-dimensional (Figure 1a, d).

## The Agent

## Physically realistic random motion

Smooth and temporally continuous random motion can be difficult to model. To be smooth (and therefore physically plausible), a trajectory must be continuous in both position and velocity. To be temporally continuous, the statistics of the motion must be independent of the integration timestep being used. To be random, position and velocity at one time must not be reliable predictors of position and velocity at another time, provided these times are seperated by a sufficiently long interval. Implementations of random motion models typically fail to satisfy one, or sometimes two, of these principles (Raudies and Hasselmo, 2012; Benna and Fusi, 2021).

Ornstein-Uhlenbeck processes, which sit at the heart of the RatInABox random motion model, are continuous-in-time random walks with a tendency to return to a central drift value. The decorrelation timescale can be also be controlled. We use these to update the velocity vector (linear and rotational velocities are updated independently) on each update step. Position is then updated by taking a step along the velocity vector with some additional considerations to avoid walls. This method ensures both position and velocity are continuous, yet evolve ‘randomly’ (Figure 1a, d), and the statistics of the motion is independent of the size of the discretisation timestep being used.

Reanalysing rat locomotion data from Sargolini et al., 2006 (as has been done before, by Raudies and Hasselmo, 2012) we found that the histograms of linear speeds are well fit by a Rayleigh distributions whereas rotational velocities are approximately fit by normal distributions (Figure 2a). Unlike Raudies and Hasselmo, 2012, we also extract the decorrelation timescale of these variables and observe that rotational velocity in real locomotion data decorrelates nearly an order of magnitude faster than linear velocity (0.08 s vs. 0.7 s). We set the default parameters of our Ornstein-Uhlenbeck processes (including applying a transform on the linear velocity so its long-run distribution also follows a Rayleigh distribution, see Methods) to those measured from the Sargolini et al., 2006 dataset (Figure 2b).

## Motion near walls

Animals rarely charge head-first into a wall, turn around, then continue in the opposite direction. Instead, they slow down smoothly and turn to avoid a collision. Additionally, during random foraging, rodents are observed to show a bias towards following walls, a behaviour known as thigmotaxis (Satoh et al., 2011; Figure 2c). To replicate these observations, walls in the Environment lightly repel the Agent when it is close. Coupled with the finite turning speed this creates (somewhat counter-intuitively) a thigmotactic effect where the agent over-explores walls and corners, matching what is observed in the data (Figure 2e). A user-defined parameter called ‘thigmotaxis’ can be used to control the strength of this emergent effect (Figure 2d).

## Imported trajectories

RatInABox supports importing trajectory data which can be used instead of the inbuilt random motion model. Imported trajectory data points which may be of low temporal-resolution are interpolated using cubic splines and smoothly upsampled to user-define temporal precision (Figure 3a). This upsampling is essential if one wishes to use low temporal resolution trajectory data to generate high temporal resolution neural data.

## Trajectory control

RatInABox supports online velocity control. At each integration step a target drift velocity can be specified, towards which the Agent accelerates. We anticipate this feature being used to generate complex stereotyped trajectories or to model processes underpinning complex spatial behaviour (as we demonstrate in Figure 3b, e).

## Neurons

RatInABox provides multiple premade Neurons subclasses chosen to replicate the most popular and influential cell models and state representations across computational neuroscience and machine learning. A selection of these are shown in Figure 1b. See Methods for mathematical details. These currently include:

A dedicated space containing additional cell classes not described here, is made available for community contributions to this list.

## Customizable and trainable neurons

Any single toolkit cannot contain all possible neural representations of interest. Besides, static cell types (e.g. PlaceCells, GridCells etc.) which have fixed receptive fields are limiting if the goal is to study how representations and/or behaviour are learned. RatInABox provides two solutions: Firstly, being open-source, users can write and contribute their own bespoke Neurons (instructions and examples are provided) with arbitrarily complicated rate functions. Secondly, two types of function-approximator Neurons are provided which map inputs (the firing rate of other Neurons) to outputs (their own firing rate) through a parameterised function which can be hand-tuned or trained to represent an endless variety of receptive field functions including those which are mixed selective, non-linear, dynamic, and non-stationary.

Naturally, function-approximator Neurons can be used to model how neural populations in the brain communicate, how neural representations are learned or, in certain cases, neural dynamics. In an online demo, we show how GridCells and HeadDirectionCells can be easily combined using a FeedForwardLayer to create head-direction selective grid cells (aka. conjunctive grid cells Sargolini et al., 2006). In Figure 3d and associated demo GridCells provide input to a NeuralNetworkNeurons class which is then trained, on data generated during exploration, to have a highly complex and non-linear receptive field. Function-approximator Neurons can themselves be used as inputs to other function-approximator Neurons allowing multi-layer and/or recurrent networks to be constructed and studied.

## Field of view encodings

Efficiently encoding what an Agent can ‘see’ in its local vicinity, aka. its field of view, is crucial for many modelling studies. A common approach is to use a convolutional neural network (CNN) to process a rendered image of the nearby environment and extract activations from the final layer. However, this method is computationally expensive and necessitates training the CNN on a large dataset of visual images.

RatInABox offers a more efficient alternative through the use of VectorCells. Three variants – FieldOfViewBVCs, FieldOfViewOVCs, and FieldOfViewAVCs – comprise populations of egocentric Boundary-, Object-, and AgentVectorCells with angular and distance preferences specifically set to tile the Agent’s field of view. Being egocentric means that the cells remained fixed in the reference frame of the Agent as it navigates the Environment. Users define the range and resolution of this field of view. Plotting functions for visualising the field of view cells, as shown in Figure 3c, are provided.

## Geometry and boundary conditions

In RatInABox, PlaceCells and VectorCells are sensitive to walls in the Environment. Three distance geometries are supported: ‘euclidean’ geometry calculates the Euclidean distance to a place field centre and so cell activity will ‘bleed’ through boundaries as if they weren’t there. ‘line_of_sight’ geometry allows a place cell to fire only if there is direct line-of-sight to the place field centre from the current location. Finally ‘geodesic’ geometry (default) calculates distance according to the shortest boundary-avoiding path to the cell centre (notice smooth wrapping of the third place field around the wall in Figure 1b). The latter two geometries respect the observation that place fields don’t typical pass through walls, an observation which is thought to support efficient generalisation in spatial reinforcement learning (Gustafson and Daw, 2011). Boundary conditions can be periodic or solid. In the former case, place fields near the boundaries of the environment will wrap around.

## Rate maps

RatInABox simplifies the calculation and visualization of rate maps through built-in protocols and plotting functions. Rate maps can be derived explicitly from their known analytic firing functions or implicitly from simulation data. The explicit method computes rate maps by querying neuron firing rates at all positions simultaneously, utilizing ’array programming’ to rapidly compute the rate map. In the implicit approach, rate maps are created by plotting a smoothed histogram of positions visited by the Agent, weighted by observed firing rates (a continuous equivalent of a smoothed spike raster plot). Additionally, the tool offers the option to visualize spikes through raster plots.

## Results

The default parameters of the random motion model in RatInABox are matched to observed statistics of rodent locomotion, extracted by reanalysing data from Sargolini et al., 2006 (data freely available at: https://doi.org/10.11582/2017.00019, exact filename used: 8F6BE356-3277-475C-87B1-C7A977632DA7_1/11084–03020501_t2c1.mat). Trajectories and statistics from the real data (Figure 2a) closely compare to the artificially generated trajectories from RatInABox (Figure 2b). Further, data (Satoh et al., 2011) shows that rodents have a tendency to over-explore walls and corners, a bias often called ‘thigmotaxis’ which is particularly pronounced when the animal is new to the environment (Figure 2c). This bias is correctly replicated in the artificial trajectories generated by RatInABox - the strength of which can be controlled by a single parameter Agent.thigmotaxis (Figure 2d, e).

RatInABox can import and smoothly interpolate user-provided trajectory data. This is demonstrated in Figure 3a where a low-resolution trajectory is imported into RatInABox and smoothly upsampled using cubic spline interpolation. The resulting trajectory is a close match to the ground truth. Note that without upsampling, this data (2 Hz) would be far too low in temporal-resolution to usefully simulate neural activity. For convenience, the exact datafile Sargolini et al., 2006 used in Figures 3a and 2a is uploaded with permission to the GitHub repository and can be imported using Agent.import_trajectory(dataset="sargolini"). An additional trajectory dataset from a much larger environment is also supplied with permission from Tanni et al., 2022.

RatInABox is computationally efficient. We compare compute times for typical RatInABox operations (Figure 3f, purple bars) to typical non-RatInABox operations representing potential ‘bottlenecking’ operations in a downstream analysis or model-training procedure for which RatInABox is providing data (Figure 3f, red bars). These were multiplying a matrix by a vector using the numpy (Harris et al., 2020) package and a forward and backward pass through a small feedforward artificial neural network using the pytorch package (Paszke et al., 2019). PlaceCells, GridCells and the random motion model all update faster than these two operations. BoundaryVectorCells (because they require integrating around a 360° field-of-view) are significantly slower than the other cells but still outpace the feedforward neural network. All vector, matrix, and cell populations were size n=100, the feed forward network had layer sizes nL=(100,1000,1000,1), the Environment was 2D with no additional walls and all operations were calculated on a consumer-grade CPU (MacBook Pro, Apple M1). These results imply that, depending on the details of the use-case, RatInABox will likely not be a significant computational bottleneck.

Our testing (Figure 3f, inset) reveals that the combined time for updating the motion model and a population of PlaceCells scales sublinearly O(1) for small populations n>1000 where updating the random motion model dominates compute time, and linearly for large populations n<1000. PlaceCells, BoundaryVectorCells and the Agent motion model update times will be additionally affected by the number of walls/barriers in the Environment. 1D simulations are significantly quicker than 2D simulations due to the reduced computational load of the 1D geometry.

## Case studies

We envisage RatInABox being used to support a range of theoretical studies by providing data and, if necessary, infrastructure for building models powered by this data. This ‘Bring-Your-Own-Algorithm’ approach makes the toolkit generally applicable, not specialised to one specific field. Two examplar use-cases are provided in the supplement and are briefly described below. The intention is to demonstrate the capacity of RatInABox for use in varied types of computational studies and to provide tutorials as a tool for learning how to use the package. Many more demonstrations and accompanying notebooks are provide on the Github repository.

In our first example, we perform a simple experiment where location is decoded from neural firing rates (Appendix 1—figure 1). Data – the location and firing rate trajectories of an Agent randomly exploring a 2D Environment – are generated using RatInABox. Non-parameteric Gaussian process regression is used to predict position from firing rates on a held-out testing dataset. We compare the accuracy of decoding using different cell types; place cells, grid cells and boundary vector cells.

Next, we demonstrate the application of RatInABox to a simple reinforcement learning (RL) task (Appendix 1—figure 2, summarised in Figure 3e). A small network capable of model-free RL is constructed and trained using RatInABox. First a neuron calculates and learns – using a continuous variant of temporal difference learning – the value function Vπ(x)=∑iwiFipc(x) as a linear combination of place cell basis features. Then a new ‘improved’ policy is defined by setting a drift velocity – which biases the Agent’s motion – proportional to the gradient of the value function vdrift(x)=π(x)∝∇xVπ. The Agent is therefore encouraged to move towards regions with high value. Iterating between these stages over many episodes (‘policy iteration’) results in convergence towards near optimal behaviour where the Agent takes the shortest route to the reward, avoiding the wall (Figure 3e).

Additional tutorials, not described here but available online, demonstrate how RatInABox can be used to model splitter cells, conjunctive grid cells, biologically plausible path integration, successor features, deep actor-critic RL, whisker cells and more. Despite including these examples we stress that they are not exhaustive. RatInABox provides the framework and primitive classes/functions from which highly advanced simulations such as these can be built.

## Discussion

RatInABox is a lightweight, open-source toolkit for generating realistic, standardised trajectory and neural data in continuous environments. It should be particularly useful to those studying spatial navigation and the role of the hippocampal formation. It remains purposefully small in scope - intended primarily as a means for generating data. We do not provide, nor intend to provide, a set of benchmark learning algorithms to use on the data it generates. Its user-friendly API, inbuilt data-plotting functions and general yet modular feature set mean it is well placed to empower a wide variety of users to more rapidly build, train and validate models of hippocampal function (Lee et al., 2023) and spatial navigation (George et al., 2023), accelerating progress in the field.

Our package is not the first to model neural data (Stimberg et al., 2019; Hepburn et al., 2012; Hines and Carnevale, 1997) or spatial behaviour (Todorov et al., 2012; Merel et al., 2019), yet it distinguishes itself by integrating these two aspects within a unified, lightweight framework. The modelling approach employed by RatInABox involves certain assumptions:

In conclusion, while no single approach can be deemed the best, we believe that RatInABox’s unique positioning makes it highly suitable for normative modelling and NeuroAI. We anticipate that it will complement existing toolkits and represent a significant contribution to the computational neuroscience toolbox.

## Materials and methods

The following section describes in mathematical detail the models used within RatInABox. Table 1, below compiles a list of all important parameters along with their default values, allowed ranges and how they can be adjusted. These are up to date as of the time/version of publication but later versions may differ, see the GitHub repository for the most up-to-date list.

## Motion model

## Temporally continuous random motion

Our random motion model is based on the Ornstein Uhlenbeck (OU) process, Xθ,λ,μ(t), a stochastic process satisfying the Langevin differential equation(1)Xθ,λ,μ(t+dt)=Xθ,λ,μ(t)+dXθ,λ,μ(t),dXθ,λ,μ(t)=θ(μ−Xθ,λ,μ(t))dt+λη(t)dt

where η(t)∼N(0,1) is Gaussian white noise and θ, λ and μ are constants. The first term in the update equation drives decay of Xθ,λ,μ(t) towards the mean μ. The second term is a stochastic forcing term, driving randomness. These stochastic processes are well studied; their unconditioned covariance across time is(2)⟨Xθ,λ,μ(t)Xθ,λ,μ(t′)⟩=λ22θe−θ|t−t′|.

Thus Xθ,λ,μ(t) decorrelates smoothly over a timescale of τ=1/θ. Over long periods Xθ,λ,μ(t) is stochastic and therefore unpredictable. Its long-run stationary probability distribution is a Gaussian with mean μ and standard deviation σ=λ2/2θ. We can re-parameterise the Ornstein Uhlenbeck process in terms of these more intuitive parameters (the decoherence timescale τ and the long-run standard deviation σ) using the transformations(3)θ=1τ,λ=2σ2τ,

to give(4)Xτ,σ,μ(t+dt)=Xτ,σ,μ(t)+dXτ,σ,μ(t),dXτ,σ,μ(t)=1τ(μ−Xτ,σ,μ(t))dt+2σ2τη(t)dt.

Ornstein Uhlenbeck processes have the appealing property that they are temporally continuous (their statistics are independent of dt) and allow for easy control of the long-run standard deviation and the decoherence timescale of the stochastic variable. For these reasons, we use use them to model rotational and linear velocities within RatInABox.

## 2D motion

For 2D locomotion, we sample the Agent’s rotational velocity ω(t)=θ˙v(t) and linear speed, v2D(t)=‖v(t)‖, from independent OU processes. This is because, as shown in the Results section, they have decoherence timescales differing by an order of magnitude. Rotational velocity is sampled from a standard Ornstein Uhlenbeck process with zero mean. Linear speed is also sampled from an Ornstein Uhlenbeck process with one additional transform applied in order to match the observation that linear speeds have a Rayleigh, not normal, distribution.(5)ω(t)∼Xτω,αω,0(t),(6)v2D(t)=Rσv(z(t))wherez(t)∼Xτv,1,0(t),

where Rσ(x) is a monotonic transformation which maps a normally distributed random variable x∼N(0,1) to one with a Rayleigh distribution of scale parameter σ corresponds to the mode, or ≈0.8 times the mean, of the Rayleigh distribution.(7)Rσ(x)=σ−2ln⁡(1−12[1+erf(x2)]).

The parameters {τω,σω,τv,σv} are fitted from real open field 2D locomotion data in Figure 2 or can be set by the user (see Table 1, below).

Full trajectories are then sampled as follows: First the rotational and linear velocities are updated according to Equations 5, 6 (and additional considerations for walls, see next section). Next the velocity direction, θv(t) – defined as the angle of the velocity vector measured anticlockwise from the x-direction – is updated according to the rotational velocity, ω(t).(8)θv(t)=(θv(t−dt)+ω(t)dt)mod2π.

This is combined with the linear speed, v2D(t) to calculate new total velocity vector, v(t).(9)v(t)=v2D(t)[cos⁡θv(t)sin⁡θv(t)].

Finally position, x(t), is updated by integrating along the total velocity vector to give a continuous and smooth, but over long time periods random, motion trajectory.(10)x(t)=x(t−dt)+v(t)dt.

## 1D motion

Motion in 1D is more simple than motion in 2D. Velocity is also modelled as an Ornstein Uhlenbeck process without the Rayleigh transform. In this case a non-zero mean, μv, corresponding to directional bias in the motion, can be provided by the user. In summary:(11)v1D(t)∼Xτv,αv,μv(t),(12)x(t)=x(t−dt)+v1D(t)dt.

## External velocity control

It is possible to provide an external velocity signal controlling the Agent’s motion. After the random motion update (as described above) is applied, if an external velocity vdrift(t) is provided by the user, an additional update to the velocity vector is performed(13)dv(t+dt)=1τdrift(vdrift(t)−v(t))dt.

In cases where τdrift>>τv the net update to the velocity (random update and drift update) is dominated by the random component. When τdrift<<τv the update is dominated by the drift component. We define τdrift:=τv/k where k is an argument also provided by the user. To good approximation for large k>>1 the Agent velocity closely tracks the drift velocity at all times and is not random whilst for k<<1 the drift velocity is ignored and the motion is entirely random.

## Motion near walls in 2D

An important feature is the ability to generate Environments with arbitrary arrangements of walls (aka ‘barriers’ or ‘boundaries’). Walls are meaningful only if they appropriately constrain the motion of the Agent. For biological agents this means three things:

Our motion model replicates these three effects as follows:

## Collision detection

To avoid travelling through walls, if a collision is detected the velocity is elastically reflected off the wall (normal component is flipped). The speed is then scaled to one half the average motion speed, v2D(t)=0.5σv.

## Wall repulsion

Spring-deceleration model. In order to slow down before colliding with a wall the Agent feels an acceleration, perpendicular to the wall, whenever it is within a small distance, dwall, of the wall.(14)v˙(t)=k1∑walls,jnj{(s⋅σv)2dwall2⋅(dwall−d⊥,j(t))if d⊥,j(t)≤dwall,0if d⊥,j(t)>dwall.

d⊥,j(t) is the perpendicular distance from the Agent to the jth wall, nj is the perpendicular norm of the jth wall (the norm pointing towards the Agent) and k1 & s are constants (explained later). dwall is the distance from the wall at which the Agent starts to feel the deceleration, defaulting to dwall=0.1 m.

Note that this acceleration is identical to that of an oscillating spring-mass where the base of the spring is attached a distance dwall from the wall on a perpendicular passing through the Agent. The spring constant is tuned such that a mass starting with initial velocity towards the wall of −sσvnj would stop just before the wall. In summary, for k1=1, if the Agent approaches the wall head-on at speed of sσv (s times its mean speed) this deceleration will just be enough to avoid a collision.

s is the unitless wall repel strength parameter (default s=1). When it is high, walls repel the agent strongly (only fast initial speeds will result in the agent reaching the wall) and when it is low, walls repel weakly (even very slow initial speeds will not be slowed done by the spring dynamics). When s=0 wall repulsion is turned off entirely.

Conveyor-belt model. A second (similar, but not exactly equivalent) way to slow down motion near a wall is to consider a hypothetical conveyor belt near the wall. This conveyor belt has a non-uniform velocity pointing away from the wall of(15)x˙(t)=k2∑walls,jnj{s⋅σv(1−1−(dwall−d⊥,j(t))2dwall2)if d⊥,j(t)≤dwall,0if d⊥,j(t)>dwall.

When the Agent is close to the wall the hypothetical conveyor-belt moves it backwards on each time step, effectively slowing it down. Note that this velocity is identical to that of a spring-mass attached to the wall with initial velocity sσvnj away from the wall and spring constant tuned to stop the mass just before it reaches a distance dwall. In summary, for k2=1, if the Agent approaches the wall head-on at speed of sσv the conveyor belt will just be fast enough to bring it to a halt at the location of the wall.

Wall attraction (thigmotaxis). Although similar, there is an exploitable difference between the ‘spring-deceleration’ and ‘conveyor-belt’ models: the ‘conveyor-belt’ changes the Agents position, x(t), on each step but not its internal velocity variable v(t). As as result (and as the conveyor-belt intuition suggests) it will slow down the Agent’s approach towards the wall without causing it to turn around. This creates a ‘lingering’ or ‘thigmotactic’ effect whereby whenever the Agent heads towards a wall it may carry on doing so, without collision, for some time until the stochastic processes governing its motion (section ‘Temporally continuous random motion’) cause it to turn. Conversely the ‘spring-deceleration’ model has no ‘thigmotactic’ effect since it actively changes the internal velocity variable causing the Agent to turn around or ‘bounce’ off the walls.

The relative strengths of these two effects, k1 and k2, are controlled by a single thigmotaxis parameter, λthig∈[0,1] which governs the trade-off between these two models.(16)k1=3(1−λthig)2,k2=6λthig2.

When λthig=1 only the conveyor belt model is active giving a strong thigmotactic effects. When λthig=0 only the spring-deceleration model is active giving no thigmotactic effect. By default λthig=0.5. The constants 3 and 6 are tuning parameters chosen by hand in order that direct collisions with the walls are rare but not impossible.

Although this procedure, intended to smoothly slow the Agent near a wall, may seem complex, it has a two advantages: Firstly, deceleration near walls is smooth, becoming stronger as the Agent gets nearer and so induces no physically implausible discontinuities in the velocity. Secondly, it provides a tunable way by which to control the amount of thigmotaxis (evidenced in Figure 2c, d). Recall that these equations only apply to motion very near the wall (<dwall) and they can be turned off entirely (s=0) (see Table 1, below).

## Importing trajectories

Users can override the random motion model by importing their own trajectory with Agent.import_trajectory(times,positions) where times is an array of times (not necessarily evenly spaced) and positions is an array of positions at each time. The trajectory is then interpolated using scipy.interpolate’s interp1d function following which the standard RatInABox Agent.update(dt) API is called to move the Agent to a new position a time dt along the imported trajectory.

When moving along imported trajectories the Agent will not be subject to the wall repel nor wall collision effects described above.

## Head direction

As well as position and velocity Agents have a head direction, h^(t). Head direction is used by various cell types to determine firing rate including HeadDirectionCells and (egocentric) VectorCells. By default, head direction is just the smoothed-then-normalised velocity vector, updated on each timestep as follows:(17)h(t+dt)=(1−dtτh)h^(t)+dtτhv(t)‖v(t)‖(18)h^(t+dt)=h(t+dt)‖h(t+dt)‖.

By default the amount of smoothing is very small (in 2D τh=0.15, in 1D there is no smoothing at all) meaning that, to a good approximation, head direction is simply the normalised velocity vector at time t, h^(t)≈v^(t). However by storing head direction as an independent variable, we make available the possibility for users to craft their own, potenitally more complex, head direction dynamics if desired.

We also define the head direction angle ϕh(t) aka. the angle of head direction vector measured clockwise from the x-axis.

## Distance measures

In many of the cell models, it is necessary to calculate the ‘distance’ between two locations in the Environment (for example to calculate the firing rate of a Gaussian PlaceCell). This might depend on the type of geometry being used and the arrangement of walls in the Environment. There are three types of geometry currently supported:(19)euclidean:d(x1,x2)=‖x1−x2‖(20)geodesic:d(x1,x2)=length of shortest wall-avoiding path between x1 and x2(21)line_of_sight:d(x1,x2)={‖x1−x2‖,if no wall obstructs the straight line between x1 and x2∞,otherwise

By default RatInABox typically uses geodesic distance, except in Environments with more than one additional wall where calculating the shortest path becomes computationally expensive. In these cases, line_of_sight distance is typically used instead. Furthermore, in Environments with periodic boundary conditions these distance measures will respect the periodicity by always using the shortest path between two points, wrapping around boundaries if necessary. These geometry considerations are what allow RatInABox cell classes to interact sensibly with walls (e.g. by default place cells won’t bleed through walls, as observed in the brain). Hereon we refer to this as the ‘environmental-distance’.

## Cell models

In the following section, we list mathematical models for some of the default provided Neurons subclasses, including all those covered in this manuscript. More cell types and documentation can be found on the codebase. Readers will note that, oftentimes, parameters are set randomly at the point of initialisation (e.g. where the place cells are located, the orientation of grid cells, the angular preference of boundary vector cells etc.). Many of these random parameters are all set as class attributes and so can be redefined after initialisation if necessary. For simplicity here we describe default behaviour only – the default values for all parameters and how to change them are given in Table 1, below.

Maximum and minimum firing rates. For most cell classes it is also possible to set their maximum and minimum firing rates (fmax, fmin). For simplicity, the formulae provided below are written such that they have a maximum firing rate of 1.0 Hz and minimum firing rate of 0.0 Hz but readers should be aware that after evaluation these firing rates are linearly scaled according to(22)F(t)←(fmax−fmin)F(t)+fmin.

Noise. By default all Neurons are noiseless with their firing rates entirely determined by the deterministic mathematical models given below. Smooth Ornstein Uhlenbeck sampled random noise of coherence timescale τη and magnitude ση can be added:(23)η(t)∼Xτη,ση,0(t)(24)F(t)←F(t)+η(t)

Rates vs. Spikes. RatInABox Neurons are fundamentally rate-based. This means that their firing rate is a continuous function of time. Simultaneously, at every time-step, spikes are sampled from this firing rate and saved into the history dataframe in case spiking data is required:(25)P(Neuronispikesin[t,t+dt])=Fi(t)dt.

## PlaceCells

A set of locations (the centre of the place fields), {xiPC}, is randomly sampled from the Environment. By default these locations sit on a grid uniformly spanning the Environment to which a small amount of random jitter, half the scale of the sampled grid, is added. Thus, place cell locations appear ‘random’ but initialising in this way ensures all parts of the Environment are approximately evenly covered with the same density of place fields.

The environmental-distance from the Agent to the place field centres is calculated (di(t)=d(xiPC,x(t))). The firing rate is then determined by one of the following functions (defaulting to F{gaussian}):(26)Figaussian(t)=e−di2/2wi2(27)Figaussian_threshold(t)=max(0,e−di2/2wi2−e−1/21−e−1/2)(28)Fidiff_of_gaussians(t;r=1.5)=e−di2/2wi2−(1/r2)e−di2/2(rwi)21−1/r2(29)Fitop_hat(t)={1if di≤wi0otherwise(30)Fione_hot(t)=δ(i==argminj(dj)).

Where used, wi is the user-provided radius (aka. width) of the place cells (defaulting to 0.2 m).

## GridCells

Each grid cell is assigned a random wave direction θi∼U[0,2π], gridscale λi∼U[0.5 m,1.0 m] and phase offset ϕi∼U[0,2π]. The firing rate of each grid cell is given by the thresholded sum of three cosines(31)Fi(t)=13max(0,cos⁡(2πx(t)⋅eθiλi+ϕi)+cos⁡(2πx(t)⋅eθi+π/3λi+ϕi)+cos⁡(2πx(t)⋅eθi+2π/3λi+ϕi)).

eθ is the unit vector pointing in the direction θ. We also provide a shifted (as opposed to rectified) sum of three cosines grid cell resulting in softer grid fields(32)Fi(t)=23(13(cos⁡(2πx(t)⋅eθiλi+ϕi)+cos⁡(2πx(t)⋅eθi+π/3λi+ϕi)+cos⁡(2πx(t)⋅eθi+2π/3λi+ϕi))+12)

eθ is the unit vector pointing in the direction θ.

## VectorCells (parent class only)

VectorCells subclasses include BoundaryVectorCells, ObjectVectorCells and AgentVectorCells as well as FieldOfView versions of these three classes. The common trait amongst all types of VectorCell is that each cell is responsive to a feature of the environment (boundary segments, objects, other agents) at a preferred distance and angle. The firing rate of each vector cell is given by the product of two functions; a Gaussian radial function and a von Mises angular function. When the agent is a euclidean distance d(t) from the feature, at an angle ϕ(t) the contribution of that feature to the total firing rate is given by(33)gi(r(t),θ(t))=exp⁡(−(di−d(t))22σd,i2)⋅fVM(ϕ(t)|ϕi,κi)

where fVM is the radial von Mises distribution (a generalisation of a Gaussian for periodic variables)(34)fVM(ϕ(t)|ϕi,κi):=exp⁡(κicos⁡(ϕ(t)−ϕi)).

Total firing rate is calculated by summing/integrating these contributions over all features in the Environment as described in the following sections. Distance and angular tuning parameters and defined/sampled as follows:

The asymptotic equivalence between a Gaussian and a von Mises distribution (true for small angular tunings whereby von Mises distributions of concentration parameter κ approach Gaussian distributions of variance σ2=1/κ) means this model is effectively identical to the original boundary vector cell model proposed by Hartley et al., 2000 but with the difference that our vector cells (BVCs included) will not show discontinuities if they have wide angular tunings of order 360∘.

All vector cells can be either

## BoundaryVectorCells

The environmental features which BoundaryVectorCells (BVCs) respond to are the boundary segments (walls) of the Environment. The total firing rate of of each cell is given by integrating (computationally we use a default value of dθ=2∘ to numerically approximate this integral) the contributions from the nearest line-of-sight boundary segments (walls occluded by other walls are not considered) around the full 2π field-of-view;(35)Fi(t)=Ki∫02πgi(r,θ)dθ,

(computationally we use a default value of dθ=2∘ to numerically approximate this integral). Ki=1/maxxFi(x) is a normalisation constant calculated empirically at initialisation such that each BVC has a maximum firing rate (before scaling) of 1.0 Hz.

## ObjectVectorCells

ObjectVectorCells (OVCs) respond to objects in the Environment. Objects are zero-dimensional and can be added anywhere within the Environment, each object, j, comes with a “type” attribute, tj. Each object vector cell has a tuning type, ti, and is only responsive to objects of this type. The total firing rate of of each cell is given by the sum of the contributions from all objects of the correct type in the Environment;(36)Fi(t)=∑objects,j if tj=tigi(rj(t),θj(t)).

Since Equation 33 has a maximum value of 1 by definition the maximum firing rate of an object vector cell is also 1 Hz (unless multiple objects are closeby) and no normalisation is required.

## AgentVectorCells

AgentVectorCells respond to other Agents in the Environment. All cells in a given class are selective to the same Agent, index j. The firing rate of each cell is then given by;(37)Fi(t)=gi(rj(t),θj(t)).

## FieldOfViewBVCs, FieldOfViewOVCs, and FieldOfViewAVCs

FieldOfViewBVCs/OVCs/AVCs are a special case of the above vector cells where the tuning parameters (di, σd,i, ϕi, σϕ,i) for a set of VectorCells are carefully set so that cells tile a predefined ‘field of view’. By default these cells are egocentric and so the field of view (as the name implies) is defined relative to the heading direction of the Agent; if the Agent turns the field of view turns with it.

Users define the angular and radial extent of the field of view as well as the resolution of the cells which tile it. There is some flexiblity for users to construct complex fields of view but baic API simplifies this process, exposing a few key parameters:

More complex field of views can be constructed and a tutorial is provided to show how.

## HeadDirectionCells

In 2D Environments each head direction cell has an angular tuning mean θi and width σi:=1/κi. The response function is then a von Mises in the head direction of the Agent:(38)Fi(t)=exp⁡(κicos⁡(θh(t)−θi)).

By default all cells have the same angular tuning width of 3° and tuning means even spaced from 0° to 360∘.

In 1D Environments there is always and only exactly n=2 HeadDirectionCells; one for leftward motion and one for rightward motion.(39)F1(t)=max(0,sgn(v1D(t)))F2(t)=max(0,sgn(−v1D(t)))

## VelocityCells

VelocityCells are a subclass of HeadDirectionCells which encode the full velocity vector rather than the (normalised) head direction. In this sense they are similar to HeadDirectionCells but their firing rate will increase with the speed of the Agent.

In 2D their firing rate is given by:(40)Fi(t)=v2Dσvexp⁡(κicos⁡(θv(t)−θi))

where θv(t) is the angle of the velocity vector v(t) anticlockwise from the x-direction and σv is the likely speed scale of the Agent moving under random motion (this is chosen so the firing rate of the velocity cell before scaling is approximately O(1) Hz).

In 1D environments:(41)F1(t)=max(0,v1D(t)σv+μv),F2(t)=max(0,−v1D(t)σv+μv)

where the addition of μv accounts for any bias in the motion.

## SpeedCell

A single cell encodes the scaled speed of the Agent(42)F(t)=‖v(t)‖σv

where, same as with the VelocityCells, σv (or σv+μv in 1D) is the typical speed scale of the Agent moving under random motion giving these cells ad pre-scaled maximum firing rate of O(1) Hz.

## PhasePrecessingPlaceCells

PhasePrecessingPlaceCells (a subclass of PlaceCells) display a phenomena known as phase precession with respect to an underlying theta oscillation; within each theta cycle the firing rate of a place cell peaks at a phase dependent on how far through the place field the Agent has travelled. Specifically, as the Agent enters the receptive field the firing rate peaks at a late phase in the cycle and as the Agent leaves the receptive field the firing rate peaks at an early phase in the cycle, hence the name phase precession. Phase precession is implemented by modulating the spatial firing rate of PlaceCells with a phase precession factor, Fiθ(t),(43)Fi(t)←Fi(t)⋅Fiθ(t),

which rises and falls each theta cycle, according to:(44)Fiθ(t)=2πfVM(ϕθ(t)|ϕi∗(x(t),x˙(t)),κθ).

This is a von Mises factor where ϕθ(t)=2πνθtmod2π is the current phase of the νθ Hz theta-rhythm and ϕi∗(x(t),x˙^(t)) is the current ‘preferred’ theta phase of a cell which is a function of it’s position x(t) and direction of motion x˙^(t). This preferred phase is calculated by first establishing how far through a cells spatial receptive field the Agent has travelled along its current direction of motion;(45)di(x(t),x˙^(t))=(x(t)−xi)⋅x˙^(t),

and then mapping this to a uniform fraction βθ of the range [0,2π];(46)ϕi∗(t)=π−βθπdi(t)σi.

σi is the width of the cell at its boundary, typically defined as σi=wi, except for gaussian place cells where the boundary is arbitrarily drawn at two standard deviations σi=2wi.

The intuition for this formula can be found by considering an Agent travelling straight through the midline of a circular 2D place field. As the Agent enters into the receptive field (at which point (x(t)−xi)⋅x˙^(t)=−σi) the firing rate will peak at a theta phase of π+βπ. This then precesses backwards as it passes through the field until the moment it leaves ((x(t)−xi)⋅x˙^(t)=σi) when the firing rate peaks at a phase of π−βπ. This generalises to arbitrary curved paths through 2D receptive fields. This model has been used and validated before by Jeewajee et al., 2014 . κθ determines the spread of the von Mises, i.e. how far from the preferred phase the cell is likely to fire.

## RandomSpatialNeurons

RandomSpatialNeurons provide spatially ‘tuned’ inputs for use in instances where PlaceCells, GridCells, BoundaryVectorCells etc. These neurons have smooth but, over long distances, random receptive fields (approximately) generated by sampling from a Gaussian process with a radial basis function kernel of lengthscale l (default l=0.1 m). The kernel is given by:(47)k(x,x′)=exp−d(x,x′)22l2

where d(x,x′) is the environmental-distance between two points in the environment. This distance measure (same as used for PlaceCells, and VectorCells etc.) accounts for walls in the environment and so the receptive fields of these neurons are smooth everywhere except across walls (see Section ‘Distance measures’).

Firing rates are calculated as follows: At initialisation an array of target locations, at least as dense as the lengthscale, is sampled across the environment {xj}. For each neuron, i, j target values, [F~i]:, is sampled from the multivariate Normal distribution(48)[F~i]:∼N(0,K)

where K is the covariance matrix with elements Klm=k(xl,xm). This creates a sparse set of locations, {xj}, and targets, F~ij, across the Environment: locations close to each other are likely to have similar targets (and hence similar firing rates) whereas locations far apart will be uncorrelated.

At inference time the firing rate at an arbitrary position in the Environment, x(t) (which will not neccesarily be one of the pre-sampled targets) is estimated by taking the mean of the targets weighted by the kernel function between the position and the target location:(49)Fi(x(t))=∑jk(x(t),xj)F~i,j∑jk(x(t),xj)

This weighted average is a cheap and fast approximation to the true Bayesian Gaussian process which would require the inversion of the covariance matrix K at each time-step and which we find to be numerically unstable around exposed walls.

## FeedForwardLayer

FeedForwardLayer and NeuralNetworkNeurons are different from other RatInABox classes; their firing rates are not textitexplicitly determined by properties (position, velocity, head direction etc.) of their Agent but by the firing rates of a set of input layers (other ratinabox.Neurons). They allow users to create arbitrary and trainable ‘function approximator’ Neurons with receptive fields depending non-trivially on the states of one or many Agent(s).

Each FeedForwardLayer has a list of inputs {Lj}j=1N which must be other ratinabox.Neurons subclasses (e.g. PlaceCells, BoundaryVectorCells, FeedForwardLayer). For input layer j with nj neurons of firing rates FkLj(t) for k∈[1,nj], a weight matrix is initialised by drawing weights randomly wikLj∼N(0,g/nj) (for default weight intialisation scale g=1). The firing rate of the ith FeedForwardLayer neuron is given by weighted summation of the inputs from all layers plus a bias term:(50)ri(t)=∑j=1N∑k=1njwikLjFkLj(t)+bi(51)Fi(t)=ϕ(ri(t))

where ϕ(x) is a potentially non-linear activation function defaulting to a linear identity function of unit gain. bi is a constant bias (default zero). A full list of available activations and their defining parameters can be found in the utils.py file; these include ReLU, sigmoid, tanh, Retanh, softmax and linear (the default) functions or users can pass their own bespoke activation function.

Alongside ϕ(ri(t)) this layer also calculates and saves ϕ′(ri(t)) where ϕ′ is the derivative of the activation function, a necessary quantity for many learning rules and training algorithms.

## NeuralNetworkNeurons

NeuralNetworkNeurons are a generalisation of FeedForwardLayer. Like FeedForwardLayer they are initialised with a list of inputs ith. This class also recieves, at the point of initialisation, a neural network, NN. This can be any pytorch.nn.module. To calculate teh firing rate this class takes the firing rates of all input layers, concatenates them, and passes them through the neural network. The firing rate of the NeuralNetworkNeurons neuron is given by the activity of the neuron in the output layer of neural network:(52)Fi(t)=NNi(F→L1(t),F→L2(t),...⏟inputs;w⏟weights)

If no neural network is provided by the user a default network with two hidden ReLU layers of size 20 is used.

In order to be compatible with the rest of the RatInABox API the firing rate returned by this class is a numpy array, however, on each update the output of the pytorch neural network is additionally saved as a torch tensor. By accessing this tensor, users can take gradients back through the embedded neural network and train is as we demonstrate in Figure 3e.

In Figure 3e and an associated demo script a NeuralNetworkNeurons layer is initialised with N=1 neuron/output. The inputs to the network come from a layer of 200 GridCells, ranging in grid scale from 0.2 m to 0.5 m. These are passed through a neural network with three hidden ReLU layers of size 100 and a linear readout. As the Agent randomly explores its Environment the network is trained with gradient descent to reduce the L2 error between the firing rate of the network and that of a ‘target’ rate map (a vector image of the letters ‘RIAB’). We use gradient descent with momentum and a learning rate of η=0.002⋅dt2 (which makes the total rate of learning time-step independent). Momentum is set to μ=(1−dtτet) where τet is the eligibility trace timescale of 10 s which smoothes the gradient descent, improving convergence. We find learning converges after approximately 2 hr and a good approximation of the target function is achieved.

## Tutorials and demonstrations

We provide numerous resources, some of which are listed here, to streamline the process of learning RatInABox. Next to each we describe the key features – which you may be interested in learning – covered by the resource.

In addition, scripts reproducing all figures in the GitHub readme and this paper are provided too. The code comments are nearly comprehensive and can be referenced for additional understanding where needed.

## A simple script

See the GitHub repository for instructions on how to install RatInABox. The following is a Python script demonstrating a very basic use-case.

Import RatInABox and necessary classes. Initialise a 2D Environment. Initialise an Agent in the Environment. Initialise some PlaceCells. Simulate for 20 s. Print table of times, position and firing rates. Plot the motion trajectory, the firing rate timeseries’ and place cell rate maps.

# Import RatInABox 
import ratinabox from ratinabox.Environment import Environment 
from ratinabox.Agent import Agent 
from ratinabox.Neurons import PlaceCells 
import pandas as pd

# Run a very simple simulation 
Env = Environment() 
Ag = Agent(Env) 
PCs = PlaceCells(Ag) 
for i in range(int(20/Ag.dt)): 
Ag.update() 
PCs.update()

# Export data into a dataframe 
pd.DataFrame(Ag.history)

# Plot data 
Ag.plot_trajectory() 
PCs.plot_rate_timeseries() 
PCs.plot_rate_map()

## Table of default parameters

Table 1 lists the RatInABox parameters and their default values. The ‘Key’ column give the key in a parameters dictionary which can be passed to each class upon initialisation. Any variables not present in the parameters dictionary at initialisation will be taken as default. For example, initialising an Environment of size 2 m (which is not the default size) and adding an Agent with a mean speed of 0.3ms-1 (which is not the default size) would be done as follows:

import ratinaboxfrom ratinabox.Environment import Environment
from ratinabox.Agent import Agent

Env=Environment(params = "scale":2.0) # initialise non-default Environment
Ag=Agent(Env, params = "speed_mean":0.3) # initialise non-default Agent

## License

RatInABox is currently distributed under an MIT License, meaning users are permitted to use, copy, modify, merge publish, distribute, sublicense and sell copies of the software.
