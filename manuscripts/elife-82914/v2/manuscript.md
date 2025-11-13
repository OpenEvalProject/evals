# Task-dependent optimal representations for cerebellar learning

## Authors

- Marjorie Xie<sup>1</sup> ([ORCID: 0000-0003-1456-4811](https://orcid.org/0000-0003-1456-4811))
- Samuel P Muscinelli<sup>1</sup> ([ORCID: 0000-0002-5256-2289](https://orcid.org/0000-0002-5256-2289))
- Kameron Decker Harris<sup>2</sup> ([ORCID: 0000-0002-3716-6173](https://orcid.org/0000-0002-3716-6173))
- Ashok Litwin-Kumar<sup>1</sup> ([ORCID: 0000-0003-2422-6576](https://orcid.org/0000-0003-2422-6576)) †

### Affiliations

1. Zuckerman Mind Brain Behavior Institute, Columbia University New York United States ([ROR:00hj8s172](https://ror.org/00hj8s172))
2. Department of Computer Science, Western Washington University Bellingham United States ([ROR:05wn7r715](https://ror.org/05wn7r715))

† Corresponding author

## Abstract

The cerebellar granule cell layer has inspired numerous theoretical models of neural representations that support learned behaviors, beginning with the work of Marr and Albus. In these models, granule cells form a sparse, combinatorial encoding of diverse sensorimotor inputs. Such sparse representations are optimal for learning to discriminate random stimuli. However, recent observations of dense, low-dimensional activity across granule cells have called into question the role of sparse coding in these neurons. Here, we generalize theories of cerebellar learning to determine the optimal granule cell representation for tasks beyond random stimulus discrimination, including continuous input-output transformations as required for smooth motor control. We show that for such tasks, the optimal granule cell representation is substantially denser than predicted by classical theories. Our results provide a general theory of learning in cerebellum-like systems and suggest that optimal cerebellar representations are task-dependent.

## Introduction

A striking property of cerebellar anatomy is the vast expansion in number of granule cells compared to the mossy fibers that innervate them (Eccles et al., 1967). This anatomical feature has led to the proposal that the function of the granule cell layer is to produce a high-dimensional representation of lower-dimensional mossy fiber activity (Marr, 1969; Albus, 1971; Cayco-Gajic and Silver, 2019). In such theories, granule cells integrate information from multiple mossy fibers and respond in a nonlinear manner to different input combinations. Detailed theoretical analysis has argued that anatomical parameters such as the ratio of granule cells to mossy fibers (Babadi and Sompolinsky, 2014), the number of inputs received by individual granule cells (Litwin-Kumar et al., 2017; Cayco-Gajic et al., 2017), and the distribution of granule-cell-to-Purkinje-cell synaptic weights Brunel et al., 2004 have quantitative values that maximize the dimension of the granule cell representation and learning capacity. Sparse activity, which increases dimension, is also cited as a key property of this representation (Marr, 1969; Albus, 1971; Babadi and Sompolinsky, 2014; but see Spanne and Jörntell, 2015). Sparsity affects both learning speed (Cayco-Gajic et al., 2017) and generalization, the ability to predict correct labels for previously unseen inputs (Barak et al., 2013; Babadi and Sompolinsky, 2014; Litwin-Kumar et al., 2017).

Theories that study the effects of dimension on learning typically focus on the ability of a system to perform categorization tasks with random, high-dimensional inputs (Barak et al., 2013; Babadi and Sompolinsky, 2014; Litwin-Kumar et al., 2017; Cayco-Gajic et al., 2017). In this case, increasing the dimension of the granule cell representation increases the number of inputs that can be discriminated. However, cerebellar circuits participate in diverse behaviors, including dexterous movements, inter-limb coordination, the formation of internal models, and cognitive behaviors (Ito and Itō, 1984; Wolpert et al., 1998; Strick et al., 2009). Cerebellum-like circuits, such as the insect mushroom body and the electrosensory system of electric fish, support other functions such as associative learning (Modi et al., 2020) and the cancellation of self-generated sensory signals (Kennedy et al., 2014), respectively. This diversity raises the question of whether learning high-dimensional categorization tasks is a sufficient framework for probing the function of granule cells and their analogs.

Several recent studies have reported dense activity in cerebellar granule cells in response to sensory stimulation or during motor control tasks (Jörntell and Ekerot, 2006; Knogler et al., 2017; Wagner et al., 2017; Giovannucci et al., 2017; Badura and De Zeeuw, 2017; Wagner et al., 2019), at odds with classical theories (Marr, 1969; Albus, 1971). Moreover, there is evidence that granule cell firing rates differ across cerebellar regions (Heath et al., 2014; Witter and De Zeeuw, 2015). In contrast to this reported dense activity in cerebellar granule cells, odor responses in Kenyon cells, the analogs of granule cells in the Drosophila mushroom body, are sparse, with 5–10% of neurons responding to odor stimulation (Turner et al., 2008; Honegger et al., 2011; Lin et al., 2014).

We propose that these differences can be explained by the capacity of representations with different levels of sparsity to support learning of different tasks. We show that the optimal level of sparsity depends on the structure of the input-output relationship of a task. When learning input-output mappings for motor control tasks, the optimal granule cell representation is much denser than predicted by previous analyses. To explain this result, we develop an analytic theory that predicts the performance of cerebellum-like circuits for arbitrary learning tasks. The theory describes how properties of cerebellar architecture and activity control these networks’ inductive bias: the tendency of a network toward learning particular types of input-output mappings (Sollich, 1998; Jacot et al., 2018; Bordelon et al., 2020; Canatar et al., 2021b; Simon et al., 2021). The theory shows that inductive bias, rather than the dimension of the representation alone, is necessary to explain learning performance across tasks. It also suggests that cerebellar regions specialized for different functions may adjust the sparsity of their granule cell representations depending on the task.

## Results

In our model, a granule cell layer of $M$ neurons receives connections from a random subset of $N$ mossy fiber inputs. Because $M≫N$ in the cerebellar cortex and cerebellum-like structures (approximately $M=200,000$ and $N=7,000$ for the neurons presynaptic to a single Purkinje cell in the cat brain; Eccles et al., 1967), we refer to the granule cell layer as the expansion layer and the mossy fiber layer as the input layer (Figure 1A and B).

![Figure 1.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig1-v2.jpg)

**Figure 1.:** (A) Mossy fiber inputs (blue) project to granule cells (green), which send parallel fibers that contact a Purkinje cell (black). (B) Diagram of neural network model. $D$ task variables are embedded, via a linear transformation $A$, in the activity of $N$ input layer neurons. Connections from the input layer to the expansion layer are described by a synaptic weight matrix $J$. (C) Illustration of task subspace. Points $x$ in a $D$-dimensional space of task variables are embedded in a $D$-dimensional subspace of the $N$-dimensional input layer activity $n$ ($D$=2, $N$=3 illustrated).

A typical assumption in computational theories of the cerebellar cortex is that inputs are randomly distributed in a high-dimensional space (Marr, 1969; Albus, 1971; Brunel et al., 2004; Babadi and Sompolinsky, 2014; Billings et al., 2014; Litwin-Kumar et al., 2017). While this may be a reasonable simplification in some cases, many tasks, including cerebellum-dependent tasks, are likely best-described as being encoded by a low-dimensional set of variables. For example, the cerebellum is often hypothesized to learn a forward model for motor control (Wolpert et al., 1998), which uses sensory input and motor efference to predict an effector’s future state. Mossy fiber activity recorded in monkeys correlates with position and velocity during natural movement (van Kan et al., 1993). Sources of motor efference copies include motor cortex, whose population activity lies on a low-dimensional manifold (Wagner et al., 2019; Huang et al., 2013; Churchland et al., 2010; Yu et al., 2009). We begin by modeling the low dimensionality of inputs and later consider more specific tasks.

We therefore assume that the inputs to our model lie on a $D$-dimensional subspace embedded in the $N$-dimensional input space, where $D$ is typically much smaller than $N$ (Figure 1B). We refer to this subspace as the ‘task subspace’ (Figure 1C). A location in this subspace is described by a $D$ dimensional vector $x$, while the corresponding input layer activity is given by $n=Ax$, with $A$ an $N\timesD$ matrix describing the embedding of the task variables in the input layer. An $M\timesD$ effective weight matrix $J^{eff}=JAJ^{eff}$, which describes the selectivity of expansion layer neurons to task variables, is determined by $A$ and the $M\timesN$ input-to-expansion-layer synaptic weight matrix $J$. The activity of neurons in the expansion layer is given by:

$$
h=ϕ(J^{eff}x−\theta),
$$

where $ϕ$ is a rectified linear activation function $ϕ⁢(u)=max⁢(u,0)$ applied element-wise. Our results also hold for other threshold-polynomial activation functions. The scalar threshold $\theta$ is shared across neurons and controls the coding level, which we denote by $f$, defined as the average fraction of neurons in the expansion layer that are active. We show results for $f<0.5$, since extremely dense codes are rarely observed in experiments (Olshausen and Field, 2004; see Discussion). For analytical tractability, we begin with the case where the entries of $J^{eff}$ are independent Gaussian random variables, as in previous theories (Rigotti et al., 2013; Barak et al., 2013; Babadi and Sompolinsky, 2014). This holds when the columns of $A$ are orthonormal (ensuring that the embedding of the task variables in the input layer preserves their geometry) and the entries of $J$ are independent and Gaussian. Later, we will show that networks with more realistic connectivity behave similarly to this case.

### Optimal coding level is task-dependent

In our model, a learning task is defined by a mapping from task variables $x$ to an output $f(x)$, representing a target change in activity of a readout neuron, for example a Purkinje cell. The limited scope of this definition implies our results should not strongly depend on the influence of the readout neuron on downstream circuits. The readout adjusts its incoming synaptic weights from the expansion layer to better approximate this target output. For example, for an associative learning task in which sensory stimuli are classified into categories such as appetitive or aversive, the task may be represented as a mapping from inputs to two discrete firing rates corresponding to the readout’s response to stimuli of each category (Figure 2A). In contrast, for a forward model, in which the consequences of motor commands are computed using a model of movement dynamics, an input encoding the current sensorimotor state is mapped to a continuous output representing the readout neuron’s tuning to a predicted sensory variable (Figure 2B).

![Figure 2.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig2-v2.jpg)

**Figure 2.:** (A) A random categorization task in which inputs are mapped to one of two categories (+1 or –1). Gray plane denotes the decision boundary of a linear classifier separating the two categories. (B) A motor control task in which inputs are the sensorimotor states $x(t)$ of an effector which change continuously along a trajectory (gray) and outputs are components of predicted future states $x(t+\delta)$. (C) Schematic of random categorization tasks with $P$ input-category associations. The value of the target function $f(x)$ (color) is a function of two task variables x1 and x2. (D) Schematic of tasks involving learning a continuously varying Gaussian process target parameterized by a length scale $\gamma$. (E) Error rate as a function of coding level for networks trained to perform random categorization tasks similar to (C). Arrows mark estimated locations of minima. (F) Error as a function of coding level for networks trained to fit target functions sampled from Gaussian processes. Curves represent different values of the length scale parameter $\gamma$. Standard error of the mean is computed across 20 realizations of network weights and sampled target functions in (E) and 200 in (F).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Error as a function of coding level for networks trained to perform random categorization tasks (as in Figure 2E but with a wider range of associations $P$). Performance is measured for noisy instances of previously seen inputs. $D=50$. Dashed lines indicate the performance of a readout of the input layer. Standard error of the mean was computed across 20 realizations of network weights and tasks. (B) Same as in (A) but fixing the number of associations and varying the noise $ϵ$ which controls the deviation of test patterns from training patterns. $D=50$. (C) Same as in (A) but varying the input dimension $D$. To improve performance for small $D$, we fixed the coding level for each pattern. $P=200,ϵ=0.1$ For small $D$, the curve of error rate against coding level is more flat, but low coding levels are still sufficient to saturate performance.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Error as a function of coding level for networks with (A) Heaviside and (B) rectified power-law (with power 2, $ϕ⁢(u)=max⁢(u,0)^{2}$) nonlinearity in the expansion layer. Networks learned Gaussian process targets. Dashed lines indicate the performance of a readout of the input layer. Standard error of the mean was computed across 10 realizations of network weights and tasks in (A) and 50 in (B). Parameters: $M=20,000$, $P=30$, $D=3$.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Error as a function of coding level for networks learning Gaussian process targets with input dimension $D=5$ (A) and $D=7$ (B). Dashed lines indicate the performance of a readout of the input layer. Standard error of the mean was computed across 10 realizations of network weights and tasks. Parameters: $M=20,000$, $P=30$.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** Error as a function of coding level across different values of $P$ and $\gamma$.Dots denote performance of a readout of the expansion layer in simulations. Thin lines denote performance of a readout of the input layer in simulations. Thick lines denote theory for expansion layer readout performance. Standard error of the mean was computed across 10 realizations of network weights and tasks. Parameters: $D=3$, $M=20,000$.

To examine how properties of the expansion layer representation influence learning performance across tasks, we designed two families of tasks: one modeling categorization of random stimuli, which is often used to study the performance of expanded neural representations (Rigotti et al., 2013; Barak et al., 2013; Babadi and Sompolinsky, 2014; Litwin-Kumar et al., 2017; Cayco-Gajic et al., 2017), and the other modeling learning of a continuously varying output. The former we refer to as a ‘random categorization task’ and is parameterized by the number of input pattern-to-category associations $P$ learned during training (Figure 2C). During the training phase, the network learns to associate random input patterns $x^{\mu}\inR^{D}$ for $\mu=1,…,P$ with random binary categories $y^{\mu}=\pm1$. The elements of $x^{\mu}$ are drawn i.i.d. from a normal distribution with mean 0 and variance $1/D$. We refer to $x^{\mu}$ as ‘training patterns’. To assess the network’s generalization performance, it is presented with ‘test patterns’ generated by adding noise (parameterized by a noise magnitude $ϵ$; see Methods) to the training patterns. Tasks with continuous outputs (Figure 2D) are parameterized by a length scale that determines how quickly the output changes as a function of the input (specifically, input-output functions are drawn from a Gaussian process with length scale $\gamma$ for variations in $f(x)$ as a function of $x$; see Methods). In this case, both training and test patterns are drawn uniformly on the unit sphere. Later, we will also consider tasks implemented by specific cerebellum-like systems. See Table 1 for a summary of parameters throughout this study.

**Table 1.**
 Summary of simulation parameters.$M$: number of expansion layer neurons. $N$: number of input layer neurons. $K$: number of connections from input layer to a single expansion layer neuron. $S$: total number of connections from input to expansion layer. $f$: expansion layer coding level. $D$: number of task variables. $P$: number of training patterns. $\gamma$: Gaussian process length scale. $ϵ$: magnitude of noise for random categorization tasks. We do not report $N$ and $K$ for simulations in which $J^{eff}$ contains Gaussian i.i.d. elements as results do not depend on these parameters in this case.


<table>
  <thead>
    <tr>
      <th>Figure panel</th>
      <th>Network parameters</th>
      <th>Task parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Figure 2E</td>
      <td>M=10,000</td>
      <td>D=50,P=1,000,ϵ=0.1</td>
    </tr>
    <tr>
      <td>Figures 2F, 4G and 5B (full)</td>
      <td>M=200,000</td>
      <td>D=3,P=30</td>
    </tr>
    <tr>
      <td>Figure 5B and E</td>
      <td>M=200,000,N=7,000,K=4</td>
      <td>D=3,P=30</td>
    </tr>
    <tr>
      <td>Figure 6A</td>
      <td>S=M⁢K=10,000,N=100,f=0.3</td>
      <td>D=3,P=200</td>
    </tr>
    <tr>
      <td>Figure 6B</td>
      <td>N=700,K=4,f=0.3</td>
      <td>D=3,P=200</td>
    </tr>
    <tr>
      <td>Figure 6C</td>
      <td>M=5,000,f=0.3</td>
      <td>D=3,P=100,γ=1</td>
    </tr>
    <tr>
      <td>Figure 6D</td>
      <td>M=1,000</td>
      <td>D=3,P=50</td>
    </tr>
    <tr>
      <td>Figure 7A</td>
      <td>M=20,000</td>
      <td>D=6,P=100; see Methods</td>
    </tr>
    <tr>
      <td>Figure 7B</td>
      <td>M=10,000,N=50,K=7</td>
      <td>D=50,P=100,ϵ=0.1</td>
    </tr>
    <tr>
      <td>Figure 7C</td>
      <td>M=20,000,N=206,1≤K≤3</td>
      <td>see Methods</td>
    </tr>
    <tr>
      <td>Figure 7D</td>
      <td>M=20,000,N=K=24</td>
      <td>D=1,P=30; see Methods</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 1</td>
      <td>M=10,000</td>
      <td>See Figure</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 2</td>
      <td>M=20,000</td>
      <td>D=3,P=30</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 3</td>
      <td>M=20,000</td>
      <td>D=3,P=30</td>
    </tr>
    <tr>
      <td>Figure 2—figure supplement 4</td>
      <td>M=20,000</td>
      <td>D=3</td>
    </tr>
    <tr>
      <td>Figure 7—figure supplement 1</td>
      <td>M=20,000</td>
      <td>D=3,P=200</td>
    </tr>
    <tr>
      <td>Figure 7—figure supplement 2</td>
      <td>M=10,000,f=0.3</td>
      <td>D=3,P=30,γ=1</td>
    </tr>
  </tbody>
</table>

We trained the readout to approximate the target output for training patterns and generalize to unseen test patterns. The network’s prediction is $f^(x)=w⋅h(x)$ for tasks with continuous outputs, or $f^(x)=sign(w⋅h(x))$ for categorization tasks, where $w$ are the synaptic weights of the readout from the expansion layer. These weights were set using least squares regression. Performance was measured as the fraction of incorrect predictions for categorization tasks, or relative mean squared error for tasks with continuous targets: $Error=\frac{E⁡[(f(x)−f^(x))^{2}]}{E⁡[f(x)^{2}]}$, where the expectation is across test patterns.

We began by examining the dependence of learning performance on the coding level of the expansion layer. For random categorization tasks, performance is maximized at low coding levels (Figure 2E), consistent with previous results (Barak et al., 2013; Babadi and Sompolinsky, 2014). The optimal coding level remains below 0.1 in the model, regardless of the number of associations $P$, the level of input noise, and the dimension $D$ (Figure 2—figure supplement 1). For continuously varying outputs, the dependence is qualitatively different (Figure 2F). The optimal coding level depends strongly on the length scale, with learning performance for slowly varying functions optimized at much higher coding levels than quickly varying functions. This dependence holds for different choices of threshold-nonlinear functions (Figure 2—figure supplement 2) or input dimension (Figure 2—figure supplement 3) and is most pronounced when the number of training patterns is limited (Figure 2—figure supplement 4). Our observations are at odds with previous theories of the role of sparse granule cell representations (Marr, 1969; Albus, 1971; Babadi and Sompolinsky, 2014; Billings et al., 2014) and show that sparse activity does not always optimize performance for this broader set of tasks.

### Geometry of the expansion layer representation

To determine how the optimal coding level depends on the task, we begin by quantifying how the expansion layer transforms the geometry of the task subspace. Later we will address how this transformation affects the ability of the network to learn a target. For ease of analysis, we will assume for now that inputs are normalized, $‖x‖=1$, so that they lie on the surface of a sphere in $D$ dimensions. The set of neurons in the expansion layer activated by an input $x$ are those neurons $i$ for which the alignment of their effective weights with the input, $J_{i}^{eff}⋅x$, exceeds the activation threshold $\theta$ (Equation 1; Figure 3A). Increasing $\theta$ reduces the size of this set of neurons and hence reduces the coding level.

![Figure 3.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig3-v2.jpg)

**Figure 3.:** (A) Effect of activation threshold on coding level. A point on the surface of the sphere represents a neuron with effective weights $J_{i}^{eff}$. Blue region represents the set of neurons activated by $x$, i.e., neurons whose input exceeds the activation threshold $\theta$ (inset). Darker regions denote higher activation. (B) Effect of coding level on the overlap between population responses to different inputs. Blue and red regions represent the neurons activated by $x$ and $x^{′}$, respectively. Overlap (purple) represents the set of neurons activated by both stimuli. High coding level leads to more active neurons and greater overlap. (C) Kernel $K(x,x^{′})$ for networks with rectified linear activation functions (Equation 1), normalized so that fully overlapping representations have an overlap of 1, plotted as a function of overlap in the space of task variables. The vertical axis corresponds to the ratio of the area of the purple region to the area of the red or blue regions in (B). Each curve corresponds to the kernel of an infinite-width network with a different coding level $f$. (D) Dimension of the expansion layer representation as a function of coding level for a network with $M=10,000$ and $D=3$.

Different inputs activate different sets of neurons, and more similar inputs activate sets with greater overlap. As the coding level is reduced, this overlap is also reduced (Figure 3B). In fact, this reduction in overlap is greater than the reduction in number of neurons that respond to either of the individual inputs, reflecting the fact that representations with low coding levels perform ‘pattern separation’ (Figure 3B, compare purple and red or blue regions).

This effect is summarized by the ‘kernel’ of the network (Schölkopf and Smola, 2002; Rahimi and Recht, 2007), which measures overlap of representations in the expansion layer as a function of the task variables:

$$
K(x,x^{′})=\frac{1}{M}h(x)⋅h(x^{′}).
$$

Equations 1 and 2 show that the threshold $\theta$, which determines the coding level, influences the kernel through its effect on the expansion layer activity $h(x)$. When inputs are normalized and the effective weights are Gaussian, we compute a semi-analytic expression for the kernel of the expansion layer in the limit of a large expansion ($M→∞$; see Appendix). In this case, the kernel depends only on the overlap of the task variables, $K(x,x^{′})=K(x⋅x^{′})$. Plotting the kernel for different choices of coding level demonstrates that representations with lower coding levels exhibit greater pattern separation (Figure 3C; Babadi and Sompolinsky, 2014). This is consistent with the observation that decreasing the coding level increases the dimension of the representation (Figure 3D).

### Frequency decomposition of kernel and task explains optimal coding level

We now relate the geometry of the expansion layer representation to performance across the tasks we have considered. Previous studies focused on high-dimensional, random categorization tasks in which inputs belong to a small number of well-separated clusters whose centers are random uncorrelated patterns. Generalization is assessed by adding noise to previously observed training patterns (Babadi and Sompolinsky, 2014; Litwin-Kumar et al., 2017; Figure 4A). In this case, performance depends only on overlaps at two spatial scales: the overlap between training patterns belonging to different clusters, which is small, and the overlap between training and test patterns belonging to the same cluster, which is large (Figure 4B). For such tasks, the kernel evaluated near these two values—specifically, the behavior of $K(x⋅x^{′})$ near $x⋅x^{′}=0$ and $x⋅x^{′}=1−Δ$, where $Δ$ is a measure of within-cluster noise—fully determines generalization performance (Figure 4C; see Appendix). Sparse expansion layer representations reduce the overlap of patterns belonging to different clusters, increasing dimension and generalization performance (Figure 3D, Figure 2E).

![Figure 4.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig4-v2.jpg)

**Figure 4.:** (A) Geometry of high-dimensional categorization tasks where input patterns are drawn from random, noisy clusters (light regions). Performance depends on overlaps between training patterns from different clusters (green) and on overlaps between training and test patterns from the same cluster (orange). (B) Distribution of overlaps of training and test patterns in the space of task variables for a high-dimensional task ($D=200$) with random, clustered inputs as in (A) and a low-dimensional task ($D=5$) with inputs drawn uniformly on a sphere. (C) Overlaps in (A) mapped onto the kernel function. Overlaps between training patterns from different clusters are small (green). Overlaps between training and test patterns from the same cluster are large (orange). (D) Schematic illustration of basis function decomposition, for eigenfunctions on a square domain. (E) Kernel eigenvalues (normalized by the sum of eigenvalues across modes) as a function of frequency for networks with different coding levels. (F) Power $c_{\alpha}^{2}$ as a function of frequency for Gaussian process target functions. Curves represent different values of $\gamma$, the length scale of the Gaussian process. Power is averaged over 20 realizations of target functions. (G) Generalization error predicted using kernel eigenvalues (E) and target function decomposition (F) for the three target function classes shown in (F). Standard error of the mean is computed across 100 realizations of network weights and target functions.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Frequency is indexed by $k$. Errors are calculated using analytically using Equation 4 and represent the predictions of the theory for an infinitely large expansion. Curves are symmetric around $f=0.5$ except for $k=0$ and $k=1$. Results are shown for $D=3$.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Power as a function of frequency for random categorization tasks (colors) and for Gaussian process task (black). Power is averaged over realizations of target functions.

We study tasks where training patterns used for learning and test patterns used to assess generalization are both drawn according to a distribution over a low-dimensional space of task variables. While the mean overlap between pairs of random patterns remains zero regardless of dimension, fluctuations around the mean increase when the space is low dimensional, leading to a broader distribution of overlaps (Figure 4B). In this case, generalization performance depends on values of the kernel function evaluated across this entire range of overlaps. Methods from the theory of kernel regression (Sollich, 1998; Jacot et al., 2018; Bordelon et al., 2020; Canatar et al., 2021b; Simon et al., 2021) capture these effects by quantifying a network’s performance on a learning task through a decomposition of the target function into a set of basis functions (Figure 4D). Performance is assessed by summing the contribution of each mode in this decomposition to generalization error.

The decomposition expresses the kernel as a sum of eigenfunctions weighted by eigenvalues, $K(x,x^{′})=\sum\alpha\lambda_{\alpha}ψ_{\alpha}(x)ψ_{\alpha}(x^{′})$. The eigenfunctions are determined by the network architecture and the distribution of inputs. As we show below, the eigenvalues $\lambda_{\alpha}$ determine the ease with which each corresponding eigenfunction $ψ_{\alpha}(x)$—one element of the basis function decomposition—is learned by the network. Under our present assumptions of Gaussian effective weights and uniformly distributed, normalized input patterns, the eigenfunctions are the spherical harmonic functions. These functions are ordered by increasing frequency, with higher frequencies corresponding to functions that vary more quickly as a function of the task variables. Spherical harmonics are defined for any input dimension; for example, in two dimensions they are the Fourier modes. We find that coding level substantially changes the frequency dependence of the eigenvalues associated with these eigenfunctions (Figure 4E). Higher coding levels increase the relative magnitude of the low frequency eigenvalues compared to high-frequency eigenvalues. As we will show, this results in a different inductive bias for networks with different coding levels.

To calculate learning performance for an arbitrary task, we decompose the target function in the same basis as that of the kernel:

$$
f(x)=\sum\alphac_{\alpha}ψ_{\alpha}(x)
$$

The coefficient $c_{\alpha}$ quantifies the weight of mode $\alpha$ in the decomposition. For the Gaussian process targets, we have considered, increasing length scale corresponds to a greater relative contribution of low versus high frequency modes (Figure 4F). Using these coefficients and the eigenvalues (Figure 4E), we obtain an analytical prediction of the mean-squared generalization error (‘Error’) for learning any given task (Figure 4G; see Methods):

$$
Error=C_{1}\sum\alpha(\frac{c_{\alpha}}{C_{2}+\lambda_{\alpha}})^{2},
$$

where C1 and C2 do not depend on $\alpha$ (Canatar et al., 2021b; Simon et al., 2021; see Methods). Equation 4 illustrates that for equal values of $c_{\alpha}$, modes with greater $\lambda_{\alpha}$ contribute less to the generalization error.

Our theory reveals that the optima observed in Figure 2F are a consequence of the difference in eigenvalues of networks with different coding levels. This reflects an inductive bias (Sollich, 1998; Jacot et al., 2018; Bordelon et al., 2020; Canatar et al., 2021b; Simon et al., 2021) of networks with low and high coding levels toward the learning of high and low frequency functions, respectively (Figure 4E, Figure 4—figure supplement 1). Thus, the coding level’s effect on a network’s inductive bias, rather than dimension alone, determines learning performance. Previous studies that focused only on random categorization tasks did not observe this dependence, since errors in such tasks are dominated by the learning of high frequency components, for which sparse activity is optimal (Figure 4—figure supplement 2).

### Performance of sparsely connected expansions

To simplify our analysis, we have so far assumed full connectivity between input and expansion layers without a constraint on excitatory or inhibitory synaptic weights. In particular, we have assumed that the effective weight matrix $J^{eff}$ contains independent Gaussian entries (Figure 5A, top). However, synaptic connections between mossy fibers and granule cells are sparse and excitatory (Sargent et al., 2005), with a typical in-degree of $K=4$ mossy fibers per granule cell (Figure 5A, bottom). We therefore analyzed the performance of model networks with more realistic connectivity. Surprisingly, when $J$ is sparse and nonnegative, both overall generalization performance and the task-dependence of optimal coding level remain unchanged (Figure 5B).

![Figure 5.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig5-v2.jpg)

**Figure 5.:** (A) Top: Fully connected network. Bottom: Sparsely connected network with in-degree $K<N$ and excitatory weights with global inhibition onto expansion layer neurons. (B) Error as a function of coding level for fully connected Gaussian weights (gray curves) and sparse excitatory weights (blue curves). Target functions are drawn from Gaussian processes with different values of length scale $\gamma$ as in Figure 2. (C) Distributions of synaptic weight correlations $Corr(J_{i}^{eff},J_{j}^{eff})$, where $J_{i}^{eff}$ is the ith row of $J^{eff}$, for pairs of expansion layer neurons in networks with different numbers of input layer neurons $N$ (colors) when $K=4$ and $D=3$. Black distribution corresponds to fully connected networks with Gaussian weights. We note that when $D=3$, the distribution of correlations for random Gaussian weight vectors is uniform on $[-1,1]$ as shown (for higher dimensions the distribution has a peak at 0). (D) Schematic of the selectivity of input layer neurons to task variables in distributed and clustered representations. (E) Error as a function of coding level for networks with distributed (black, same as in B) and clustered (orange) representations. (F) Distributions of $Corr(J_{i}^{eff},J_{j}^{eff})$ for pairs of expansion layer neurons in networks with distributed and clustered input representations when $K=4$, $D=3$, and $N=1,000$. Standard error of the mean was computed across 200 realizations in (B) and 100 in (E), orange curve.

To understand this result, we examined how $J$ and $A$ shape the statistics of the effective weights onto the expansion layer neurons $J^{eff}$. A desirable property of the expansion layer representation is that these effective weights sample the space of task variables uniformly (Figure 3A), increasing the heterogeneity of tuning of expansion layer neurons (Litwin-Kumar et al., 2017). This occurs when $J^{eff}$ is a matrix of independent random Gaussian entries. If the columns of $A$ are orthornormal and $J$ is fully-connected with independent Gaussian entries, $J^{eff}$ has this uniform sampling property.

However, when $J$ is sparse and nonnegative, expansion layer neurons that share connections from the same input layer neurons receive correlated input currents. When $N$ is small and $A$ is random, fluctuations in $A$ lead to biases in the input layer’s sampling of task variables which are inherited by the expansion layer. We quantify this by computing the distribution of correlations between the effective weights for pairs of expansion layer neurons, $Corr(J_{i}^{eff},J_{j}^{eff})$. This distribution indeed deviates from uniform sampling when $N$ is small (Figure 5C). However, even when $N$ is moderately large (but much less than $M$), only small deviations from uniform sampling of task variables occur for low dimensional tasks as long as $D<K≪N$ (see Appendix). In contrast, for high-dimensional tasks ($D∼N$), $K≪D$ is sufficient, in agreement with previous findings (Litwin-Kumar et al., 2017). For realistic cerebellar parameters ($N=7,000$ and $K=4$), the distribution is almost indistinguishable from that corresponding to uniform sampling (Figure 5C), consistent with the similar learning performance of these two cases (Figure 5B).

In the above analysis, an important assumption is that $A$ is dense and random, so that the input layer forms a distributed representation in which each input layer neuron responds to a random combination of task variables (Figure 5D, top). If, on the other hand, the input layer forms a clustered representation containing groups of neurons that each encode a single task variable (Figure 5D, bottom), we may expect different results. Indeed, with a clustered representation, sparse connectivity dramatically reduces performance (Figure 5E). This is because the distribution of $Corr(J_{i}^{eff},J_{j}^{eff})$ deviates substantially from that corresponding to uniform sampling (Figure 5F), even as $N→∞$ (see Appendix). Specifically, increasing $N$ does not reduce the probability of two expansion layer neurons being connected to input layer neurons that encode the same task variables and therefore receiving highly correlated currents. As a result, expansion layer neurons do not sample task variables uniformly and performance is dramatically reduced.

Our results show that networks with small $K$, moderately large $N$, and a distributed input layer representation approach the performance of networks that sample task variables uniformly. This equivalence validates the applicability of our theory to these more realistic networks. It also argues for the importance of distributed sensorimotor representations in the cortico-cerebellar pathway, consistent with the distributed nature of representations in motor cortex (Shenoy et al., 2013; Muscinelli et al., 2023).

### Optimal cerebellar architecture is consistent across tasks

A history of theoretical modeling has shown a remarkable correspondence between anatomical properties of the cerebellar cortex and model parameters optimal for learning. These include the in-degree $K$ of granule cells (Marr, 1969; Litwin-Kumar et al., 2017; Cayco-Gajic et al., 2017), the expansion ratio of the granule cells to the mossy fibers $M/N$(Babadi and Sompolinsky, 2014; Litwin-Kumar et al., 2017), and the distribution of synaptic weights from granule cells to Purkinje cells (Brunel et al., 2004; Clopath et al., 2012; Clopath and Brunel, 2013). In these studies, model performance was assessed using random categorization tasks. We have shown that optimal coding level is dependent on the task being learned, raising the question of whether optimal values of these architectural parameters are also task-dependent.

Sparse connectivity ($K$=4, consistent with the typical in-degree of cerebellar granule cells) has been shown to optimize learning performance in cerebellar cortex models (Litwin-Kumar et al., 2017; Cayco-Gajic et al., 2017). We examined the performance of networks with different granule cell in-degrees learning Gaussian process targets. The optimal in-degree is small for all the tasks we consider, suggesting that sparse connectivity is sufficient for high performance across a range of tasks (Figure 6A). This is consistent with the previous observation that the performance of a sparsely connected network approaches that of a fully connected network (Figure 5B).

![Figure 6.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig6-v2.jpg)

**Figure 6.:** (A) Error as a function of in-degree $K$ for networks learning Gaussian process targets. Curves represent different values of $\gamma$, the length scale of the Gaussian process. The total number of synaptic connections $S=M⁢K$ is held constant. This constraint introduces a trade-off between having many neurons with small synaptic degree and having fewer neurons with large synaptic degree (Litwin-Kumar et al., 2017). $S=10^{4}$, $D=3$, $f=0.3$. (B) Error as a function of expansion ratio $M/N$ for networks learning Gaussian process targets. $D=3$, $N=700$, $f=0.3$. (C) Distribution of granule-cell-to-Purkinje cell weights $w$ for a network trained on nonnegative Gaussian process targets with $f=0.3$, $D=3$, $\gamma=1$. Granule-cell-to-Purkinje cell weights are constrained to be nonnegative (Brunel et al., 2004). (D) Fraction of granule-cell-to-Purkinje cell weights that are silent in networks learning nonnegative Gaussian process targets (blue) and random categorization tasks (gray).

Previous studies also showed that the expansion ratio from mossy fibers to granule cells $M/N$ controls the dimension of the granule cell representation (Babadi and Sompolinsky, 2014; Litwin-Kumar et al., 2017). The dimension increases with expansion ratio but saturates as expansion ratio approaches the anatomical value ($M/N≈30$ when $f≈0.1$ for the inputs presynaptic to an individual Purkinje cell). These studies assumed that mossy fiber activity is uncorrelated ($D=N$) rather than low-dimensional ($D<N$). This raises the question of whether a large expansion is beneficial when $D$ is small. We find that when the number of training patterns $P$ is sufficiently large, performance still improves as $M/N$ approaches its anatomical value, showing that Purkinje cells can exploit their large number of presynaptic inputs even in the case of low-dimensional activity (Figure 6B).

Brunel et al., 2004 showed that the distribution of granule-cell-to-Purkinje cell synaptic weights is consistent with the distribution that maximizes the number of random binary input-output mappings stored. This distribution exhibits a substantial fraction of silent synapses, consistent with experiments. These results also hold for analog inputs and outputs (Clopath and Brunel, 2013) and for certain forms of correlations among binary inputs and outputs (Clopath et al., 2012). However, the case we consider, where targets are a smoothly varying function of task variables, has not been explored. We observe a similar weight distribution for these tasks (Figure 6C), with the fraction of silent synapses remaining high across coding levels (Figure 6D). The fraction of silent synapses is lower for networks learning Gaussian process targets than those learning random categorization tasks, consistent with the capacity of a given network for learning such targets being larger (Clopath et al., 2012).

Although optimal coding level is task-dependent, these analyses suggest that optimal architectural parameters are largely task-independent. Whereas coding level tunes the inductive bias of the network to favor the learning of specific tasks, these architectural parameters control properties of the representation that improve performance across tasks. In particular, sparse connectivity and a large expansion support uniform sampling of low-dimensional task variables (consistent with Figure 5C), while a large fraction of silent synapses is a consequence of a readout that maximizes learning performance (Brunel et al., 2004).

### Modeling specific behaviors dependent on cerebellum-like structures

So far, we have considered analytically tractable families of tasks with parameterized input-output functions. Next, we extend our results to more realistic tasks constrained by the functions of specific cerebellum-like systems, which include both highly structured, continuous input-output mappings and random categorization tasks.

To model the cerebellum’s role in predicting the consequences of motor commands (Wolpert et al., 1998), we examined the optimal coding level for learning the dynamics of a two-joint arm (Fagg et al., 1997). Given an initial state, the network predicts the change in the future position of the arm (Figure 7A). Performance is optimized at substantially higher coding levels than for random categorization tasks, consistent with our previous results for continuous input-output mappings (Figure 2E and F).

![Figure 7.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig7-v2.jpg)

**Figure 7.:** (A) Left: Schematic of two-joint arm. Center: Cerebellar cortex model in which sensorimotor task variables at time $t$ are used to predict hand position at time $t+\delta$. Right: Error as a function of coding level. Black arrow indicates location of optimum. Dashed line indicates performance of a readout of the input layer. (B) Left: Odor categorization task. Center: Drosophila mushroom body model in which odors activate olfactory projection neurons and are associated with a binary category (appetitive or aversive). Right: Error rate, similar to (A), right. (C) Left: Schematic of electrosensory system of the mormyrid electric fish, which learns a negative image to cancel the self-generated feedback from electric organ discharges sensed by electroreceptors. Center: Electrosensory lateral line lobe (ELL) model in which MG cells learn a negative image. Right: Error as a function of coding level. Gray arrow indicates location of coding level estimated from biophysical parameters (Kennedy et al., 2014). (D) Left: Schematic of the vestibulo-cular reflex (VOR). Head rotations with velocity $H$ trigger eye motion in the opposite direction with velocity $E$. During VOR adaptation, organisms adapt to different gains ($E/H$). Center: Cerebellar cortex model in which the target function is the Purkinje cell’s firing rate as a function of head velocity. Right: Error, similar to (A), right.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Error as a function of coding level in a spiking model. The firing rate of neuron i (in Hz) is given by $h_{i}^{\mu}=ϕ(gJ_{i}^{eff}x^{\mu}−\theta)$, where $g$ is a gain term that adjusts the amplitude of the activity and $\theta$ is the activation threshold. The spike count si for a neuron $i$ in response to pattern µ is sampled from a Poisson distribution: $s_{i}=Pois(h_{i}^{\mu}\tau)$ represents the time window in which a Purkinje cell integrates spikes, and is set to 0.1 s. Coding level is measured as the fraction of cells with a nonzero spike count. Coding level is adjusted by tuning either the activation threshold $\theta$ (top) or the gain $g$ (bottom). Black curve shows the performance of a rate model as in the main text. Standard error of the mean was computed across 10 realizations of network weights. (B) Mean spike count of active expansion layer neurons during the time window $\tau$ as a function of coding level.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/82914/elife-82914-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** During each epoch of training, the network is presented with all patterns in a randomized order, and the learned weights are updated with each pattern (see Methods). Networks were presented with 30 patterns and trained for 20,000 epochs, with a learning rate of $η=0.7/M$. Other parameters: $D=3,M=10,000$. (A) Performance of an example network during online learning, measured as relative mean squared error across training epochs. Parameters: $f=0.3$, $\gamma=1$. (B) Generalization error as a function of coding level for networks trained with online learning (solid lines) or unregularized least squares (dashed lines) for Gaussian process tasks with different length scales (colors). Standard error of the mean was computed across 20 realizations.

The mushroom body, a cerebellum-like structure in insects, is required for learning of associations between odors and appetitive or aversive valence (Modi et al., 2020). This behavior can be represented as a mapping from random representations of odors in the input layer to binary category labels (Figure 7B). The optimal coding level in a model with parameters consistent with the Drosophila mushroom body is less than 0.1, consistent with our previous results for random categorization tasks (Figure 2E) and the sparse odor-evoked responses in Drosophila Kenyon cells (Turner et al., 2008; Honegger et al., 2011; Lin et al., 2014).

The prediction and cancellation of self-generated sensory feedback has been studied extensively in mormyrid weakly electric fish and depends on the electrosensory lateral line lobe (ELL), a cerebellum-like structure (Bell et al., 2008). Granule cells in the ELL provide a temporal basis for generating negative images that are used to cancel self-generated feedback (Figure 7C). We extended a detailed model of granule cells and their inputs (Kennedy et al., 2014) to study the influence of coding level on the effectiveness of this basis. The performance of this model saturated at relatively high coding levels, and notably the coding level corresponding to biophysical parameters estimated from data coincided with the value at which further increases in performance were modest. This observation suggests that coding level is also optimized for task performance in this system.

A canonical function of the mammalian cerebellum is the adjustment of the vestibulo-ocular reflex (VOR), in which motion of the head is detected and triggers compensatory ocular motion in the opposite direction. During VOR learning, Purkinje cells are tuned to head velocity, and their tuning curves are described as piecewise linear functions (Lisberger et al., 1994; Figure 7D). Although in vivo population recordings of granule cells during VOR adaptation are not, to our knowledge, available for comparison, our model predicts that performance for learning such tuning curves is high across a range of coding levels and shows that sparse codes are sufficient (although not necessary) for such tasks (Figure 7D).

These results predict diverse coding levels across different behaviors dependent on cerebellum-like structures. The odor categorization and VOR tasks both have input-output mappings that exhibit sharp nonlinearities and can be efficiently learned using sparse representations. In contrast, the forward modeling and feedback cancellation tasks have smooth input-output mappings and exhibit denser optima. These observations are consistent with our previous finding that more structured tasks favor denser coding levels than do random categorization tasks (Figure 2E and F).

## Discussion

We have shown that the optimal granule cell coding level depends on the task being learned. While sparse representations are suitable for learning to categorize inputs into random categories, as predicted by classic theories, tasks involving structured input-output mappings benefit from denser representations (Figure 2). This reconciles such theories with the observation of dense granule cell activation during movement (Knogler et al., 2017; Wagner et al., 2017; Giovannucci et al., 2017; Badura and De Zeeuw, 2017; Wagner et al., 2019). We also show that, in contrast to the task-dependence of optimal coding level, optimal anatomical values of granule cell and Purkinje cell connectivity are largely task-independent (Figure 6). This distinction suggests that a stereotyped cerebellar architecture may support diverse representations optimized for a variety of learning tasks.

### Relationship to previous theories

Previous studies assessed the learning performance of cerebellum-like systems with a model Purkinje cell that associates random patterns of mossy fiber activity with one of two randomly assigned categories (Marr, 1969; Albus, 1971; Brunel et al., 2004; Babadi and Sompolinsky, 2014; Litwin-Kumar et al., 2017; Cayco-Gajic et al., 2017), a common benchmark for artificial learning systems (Gerace et al., 2022). In this case, a low coding level increases the dimension of the granule cell representation, permitting more associations to be stored and improving generalization to previously unseen inputs. The optimal coding level is low but not arbitrarily low, as extremely sparse representations introduce noise that hinders generalization (Barak et al., 2013; Babadi and Sompolinsky, 2014).

To examine a broader family of tasks, our learning problems extend previous studies in several ways. First, we consider inputs that may be constrained to a low-dimensional task subspace. Second, we consider input-output mappings beyond random categorization tasks. Finally, we assess generalization error for arbitrary locations on the task subspace, rather than only for noisy instances of previously presented inputs. As we have shown, these considerations require a complete analysis of the inductive bias of cerebellum-like networks (Figure 4). Our analysis generalizes previous approaches (Barak et al., 2013; Babadi and Sompolinsky, 2014; Litwin-Kumar et al., 2017) that focused on dimension and noise alone. In particular, both dimension and noise for random patterns can be directly calculated from the kernel function (Figure 3C; see Appendix).

Our theory builds upon techniques that been developed for understanding properties of kernel regression (Sollich, 1998; Jacot et al., 2018; Bordelon et al., 2020; Canatar et al., 2021b; Simon et al., 2021). Kernel approximations of wide neural networks are a major area of current research providing analytically tractable theories (Rahimi and Recht, 2007; Jacot et al., 2018; Chizat et al., 2018). Prior studies have analyzed kernels corresponding to networks with zero (Cho and Saul, 2010) or mean-zero Gaussian thresholds (Basri et al., 2019; Jacot et al., 2018), which in both cases produce networks with a coding level of 0.5. Ours is the first kernel study of the effects of nonzero average thresholds. Our full characterization of the eigenvalue spectra and their decay rates as a function of the threshold extends previous work (Bach, 2017; Bietti and Bach, 2021). Furthermore, artificial neural network studies typically assume either fully-connected or convolutional layers, yet pruning connections after training barely degrades performance (Han et al., 2015; Zhang et al., 2018). Our results support the idea that sparsely connected networks may behave like dense ones if the representation is distributed (Figure 5), providing insight into the regimes in which pruning preserves performance.

Other studies have considered tasks with smooth input-output mappings and low-dimensional inputs, finding that heterogeneous Golgi cell inhibition can improve performance by diversifying individual granule cell thresholds (Spanne and Jörntell, 2013). Extending our model to include heterogeneous thresholds is an interesting direction for future work. Another proposal states that dense coding may improve generalization (Spanne and Jörntell, 2015). Our theory reveals that whether or not dense coding is beneficial depends on the task.

### Assumptions and extensions

We have made several assumptions in our model for the sake of analytical tractability. When comparing the inductive biases of networks with different coding levels, our theory assumes that inputs are normalized and distributed uniformly in a linear subspace of the input layer activity. This allows us to decompose the target function into a basis in which we can directly compare eigenvalues, and hence learning performance, for different coding levels (Figure 4E–G). A similar analysis can be performed when inputs are not uniformly distributed, but in this case the basis is determined by an interplay between this distribution and the nonlinearity of expansion layer neurons, making the analysis more complex (see Appendix). We have also assumed that generalization is assessed for inputs drawn from the same distribution as used for learning. Recent and ongoing work on out-of-distribution generalization may permit relaxations of this assumption (Shen et al., 2021; Canatar et al., 2021a).

When analyzing properties of the granule cell layer, our theory also assumes an infinitely wide expansion. When $P$ is small enough that performance is limited by number of samples, this assumption is appropriate, but finite-size corrections to our theory are an interesting direction for future work. We also have not explicitly modeled inhibitory input provided by Golgi cells, instead assuming such input can be modeled as a change in effective threshold, as in previous studies (Billings et al., 2014; Cayco-Gajic et al., 2017; Litwin-Kumar et al., 2017). This is appropriate when considering the dimension of the granule cell representation (Litwin-Kumar et al., 2017), but more work is needed to extend our model to the case of heterogeneous inhibition.

Another key assumption concerning the granule cells is that they sample mossy fiber inputs randomly, as is typically assumed in Marr-Albus models (Marr, 1969; Albus, 1971; Litwin-Kumar et al., 2017; Cayco-Gajic et al., 2017). Other studies instead argue that granule cells sample from mossy fibers with highly similar receptive fields (Garwicz et al., 1998; Brown and Bower, 2001; Jörntell and Ekerot, 2006) defined by the tuning of mossy fiber and climbing fiber inputs to cerebellar microzones (Apps et al., 2018). This has led to an alternative hypothesis that granule cells serve to relay similarly tuned mossy fiber inputs and enhance their signal-to-noise ratio (Jörntell and Ekerot, 2006; Gilbert and Chris Miall, 2022) rather than to re-encode inputs. Another hypothesis is that granule cells enable Purkinje cells to learn piece-wise linear approximations of nonlinear functions (Spanne and Jörntell, 2013). However, several recent studies support the existence of heterogeneous connectivity and selectivity of granule cells to multiple distinct inputs at the local scale (Huang et al., 2013; Ishikawa et al., 2015). Furthermore, the deviation of the predicted dimension in models constrained by electron-microscopy data as compared to randomly wired models is modest (Nguyen et al., 2023). Thus, topographically organized connectivity at the macroscopic scale may coexist with disordered connectivity at the local scale, allowing granule cells presynaptic to an individual Purkinje cell to sample heterogeneous combinations of the subset of sensorimotor signals relevant to the tasks that Purkinje cell participates in. Finally, we note that the optimality of dense codes for learning slowly varying tasks in our theory suggests that observations of a lack of mixing (Jörntell and Ekerot, 2002) for such tasks are compatible with Marr-Albus models, as in this case nonlinear mixing is not required.

We have quantified coding level by the fraction of neurons that are above firing threshold. We focused on coding levels $f<0.5$, as extremely dense codes are rarely found in experiments (Olshausen and Field, 2004), but our theory applies for $f>0.5$ as well. In general, representations with coding levels of $f$ and $1-f$ perform similarly in our model due to the symmetry of most of their associated eigenvalues (Figure 4—figure supplement 1 and Appendix). Under the assumption that the energetic costs associated with neural activity are minimized, the $f<0.5$ region is likely the biologically plausible one. We also note that coding level is most easily defined when neurons are modeled as rate, rather than spiking units. To investigate the consistency of our results under a spiking code, we implemented a model in which granule cell spiking exhibits Poisson variability and quantify coding level as the fraction of neurons that have nonzero spike counts (Figure 7—figure supplement 1; Figure 7C). In general, increased spike count leads to improved performance as noise associated with spiking variability is reduced. Granule cells have been shown to exhibit reliable burst responses to mossy fiber stimulation (Chadderton et al., 2004), motivating models using deterministic responses or sub-Poisson spiking variability. However, further work is needed to quantitatively compare variability in model and experiment and to account for more complex biophysical properties of granule cells (Saarinen et al., 2008).

For the Purkinje cells, our model assumes that their responses to granule cell input can be modeled as an optimal linear readout. Our model therefore provides an upper bound to linear readout performance, a standard benchmark for the quality of a neural representation that does not require assumptions on the nature of climbing fiber-mediated plasticity, which is still debated. Electrophysiological studies have argued in favor of a linear approximation (Brunel et al., 2004). To improve the biological applicability of our model, we implemented an online climbing fiber-mediated learning rule and found that optimal coding levels are still task-dependent (Figure 7—figure supplement 2). We also note that although we model several timing-dependent tasks (Figure 7), our learning rule does not exploit temporal information, and we assume that temporal dynamics of granule cell responses are largely inherited from mossy fibers. Integrating temporal information into our model is an interesting direction for future investigation.

### Implications for cerebellar representations

Our results predict that qualitative differences in the coding levels of cerebellum-like systems, across brain regions or across species, reflect an optimization to distinct tasks (Figure 7). However, it is also possible that differences in coding level arise from other physiological differences between systems. In the Drosophila mushroom body, which is required for associative learning of odor categories, random and sparse subsets of Kenyon cells are activated in response to odor stimulation, consistent with our model (Figure 7B; Turner et al., 2008; Honegger et al., 2011; Lin et al., 2014). In a model of the electrosensory system of the electric fish, the inferred coding level of a model constrained by the properties of granule cells is similar to that which optimizes task performance (Figure 7C). Within the cerebellar cortex, heterogeneity in granule cell firing has been observed across cerebellar lobules, associated with both differences in intrinsic properties (Heath et al., 2014) and mossy fiber input (Witter and De Zeeuw, 2015). It would be interesting to correlate such physiological heterogeneity with heterogeneity in function across the cerebellum. Our model predicts that regions involved in behaviors with substantial low-dimensional structure, for example smooth motor control tasks, may exhibit higher coding levels than regions involved in categorization or discrimination of high-dimensional stimuli.

Our model also raises the possibility that individual brain regions may exhibit different coding levels at different moments in time, depending on immediate behavioral or task demands. Multiple mechanisms could support the dynamic adjustment of coding level, including changes in mossy fiber input (Ozden et al., 2012), Golgi cell inhibition (Eccles et al., 1966; Palay and Chan-Palay, 1974), retrograde signaling from Purkinje cells (Kreitzer and Regehr, 2001), or unsupervised plasticity of mossy fiber-to-granule cell synapses (Schweighofer et al., 2001). The predictions of our model are not dependent on which of these mechanisms are active. A recent study demonstrated that local synaptic inhibition by Golgi cells controls the spiking threshold and hence the population coding level of cerebellar granule cells in mice (Fleming et al., 2022). Further, the authors observed that granule cell responses to sensory stimuli are sparse when movement-related selectivity is controlled for. This suggests that dense movement-related activity and sparse sensory-evoked activity are not incompatible.

While our analysis makes clear qualitative predictions concerning comparisons between the optimal coding levels for different tasks, in some cases it is also possible to make quantitative predictions about the location of the optimum for a single task. Doing so requires determining the appropriate time interval over which to measure coding level, which depends on the integration time constant of the readout neuron. It also requires estimates of the firing rates and biophysical properties of the expansion layer neurons. In the electrosensory system, for which a well-calibrated model exists and the learning objective is well-characterized (Kennedy et al., 2014), we found that the coding level estimated based on the data is similar to that which optimizes performance (Figure 7C).

If coding level is task-optimized, our model predicts that manipulating coding level artificially will diminish performance. In the Drosophila mushroom body, disrupting feedback inhibition from the GABAergic anterior paired lateral neuron onto Kenyon cells increases coding level and impairs odor discrimination (Lin et al., 2014). A recent study demonstrated that blocking inhibition from Golgi cells onto granule cells results in denser granule cell population activity and impairs performance on an eye-blink conditioning task (Fleming et al., 2022). These examples demonstrate that increasing coding level during sensory discrimination tasks, for which sparse activity is optimal, impairs performance. Our theory predicts that decreasing coding level during a task for which dense activity is optimal, such as smooth motor control, would also impair performance.

While dense activity has been taken as evidence against theories of combinatorial coding in cerebellar granule cells (Knogler et al., 2017; Wagner et al., 2019), our theory suggests that the two are not incompatible. Instead, the coding level of cerebellum-like regions may be determined by behavioral demands and the nature of the input to granule-like layers (Muscinelli et al., 2023). Sparse coding has also been cited as a key property of sensory representations in the cerebral cortex (Olshausen and Field, 1996). However, recent population recordings show that such regions exhibit dense movement-related activity (Musall et al., 2019), much like in cerebellum. While the theory presented in this study does not account for the highly structured recurrent interactions that characterize cerebrocortical regions, it is possible that these areas also operate using inductive biases that are shaped by coding level in a similar manner to our model.

## Methods

### Network model

The expansion layer activity is given by $h=ϕ(J^{eff}x−\theta),$ where $J^{eff}=JA$ describes the selectivity of expansion layer neurons to task variables. For most simulations, $A$ is an $N\timesD$ matrix sampled with random, orthonormal columns and $J$ is an $M\timesN$ matrix with i.i.d. unit Gaussian entries. The nonlinearity $ϕ$ is a rectified linear activation function $ϕ⁢(u)=max⁢(u,0)$ applied element-wise. The input layer activity $n$ is given by $n=Ax.$

#### Sparsely connected networks

To model sparse excitatory connectivity, we generated a sparse matrix $J^{E}$, where each row contains precisely $K$ nonzero elements at random locations. The nonzero elements are either identical and equal to 1 (homogeneous excitatory weights) or sampled from a unit truncated normal distribution (heterogeneous excitatory weights). To model global feedforward inhibition that balances excitation, $J=J^{E}−J^{I}$, where $J^{I}$ is a dense matrix with every element equal to $\frac{1}{M⁢N}⁢\sum_{i⁢j}J_{i⁢j}^{E}$.

For Figure 5B, Figure 6A and B, Figure 7B, sparsely connected networks were generated with homogeneous excitatory weights and global inhibition. For Figure 5E, the network with clustered representations was generated with homogeneous excitatory weights without global inhibition. For Figure 5C and F, networks were generated with heterogeneous excitatory weights and global inhibition.

#### Clustered representations

For clustered input-layer representations, each input layer neuron encodes one task variable (that is, $A$ is a block matrix, with nonoverlapping blocks of $N/D$ elements equal to 1 for each task variable). In this case, in order to obtain good performance, we found it necessary to fix the coding level for each input pattern, corresponding to winner-take-all inhibition across the expansion layer.

#### Dimension

The dimension of the expansion layer representation (Figure 3D) is given by Abbott et al., 2011; Litwin-Kumar et al., 2017:

$$
d=\frac{(\sumi\lambda_{i})^{2}}{(\sumi\lambda_{i}^{2})},
$$

where $\lambda_{i}$ are the eigenvalues of the covariance matrix $C_{ij}^{h}=Cov(h_{i},h_{j})$ of expansion layer responses (not to be confused with $\lambda_{\alpha}$, the eigenvalues of the kernel operator). The covariance is computed by averaging over inputs $x$.

### Learning tasks

#### Random categorization task

In a random categorization task (Figure 2E, Figure 7B), the network learns to associate a random input pattern $x^{\mu}\inR^{D}$ for $\mu=1,…,P$ with a random binary category $y^{\mu}=\pm1$. The elements of $x^{\mu}$ are drawn i.i.d. from a normal distribution with mean 0 and variance $1/D$. Test patterns $x^^{\mu}$ are generated by adding noise to the training patterns:

$$
x^^{\mu}=\sqrt{1−ϵ^{2}}x^{\mu}+ϵη,
$$

where $η∼N(0,\frac{1}{D}I)$. For Figure 2E, Figure 7B, and Figure 4—figure supplement 2, we set $ϵ=0.1$.

#### Gaussian process tasks

To generate a family of tasks with continuously varying outputs (Figure 2D and F, Figure 4F and G, Figure 5B, and Figure 6), we sampled target functions from a Gaussian process (Rasmussen and Williams, 2006), $f(x)∼GP(0,C)$, with covariance

$$
C(x^{\mu},x^{ν})=exp⁡(−\frac{1}{2\gamma^{2}}‖x^{\mu}−x^{ν}‖^{2}),
$$

where $\gamma$ determines the spatial scale of variations in $f(x)$. Training and test patterns are drawn uniformly on the unit sphere.

#### Learning of readout weights

With the exception of the ELL task and Figure 7—figure supplement 2, we performed unregularized least squares regression to determine the readout weights $w$. For the ELL sensory cancellation task (Figure 7C), we used $ℓ^{2}$ regularization, a.k.a. ridge regression:

$$
w=argminw^{′}\sum\mu=1P‖f(x^{\mu})−w^{′}⋅h(x^{\mu})‖^{2}+M\alpha_{ridge}‖w^{′}‖_{2}^{2},
$$

where $\alpha_{ridge}$ is the regularization parameter. Solutions were found using Python’s scikit-learn package (Pedregosa, 2011).

In Figure 7—figure supplement 2, we implement a model of an online climbing fiber-mediated plasticity rule. The climbing fiber activity $c$ is assumed to encode the error between the target and the network prediction $c=f(x)−f^(x)$. During each of $N_{epochs}$ training epochs, the $P$ training patterns are shuffled randomly and each pattern is presented one at a time. For each pattern µ, the weights are updated according to $Δw^{\mu}=η⋅c⋅h(x^{\mu})$. Parameter values were $P=30,η=0.7/M,M=10,000,N_{epochs}=20,000$.

#### Performance metrics

For tasks with continuous targets, the prediction of the network is given by $f^(x)=w⋅h(x)$, where $w$ are the synaptic weights of the readout from the expansion layer. Error is measured as relative mean squared error (an expectation across patterns $x$ in the test set): $Error=\frac{E⁡[(f(x)−f^(x))^{2}]}{x[f(x)^{2}]}$. In practice we use a large test set to estimate this error over $x$ drawn from the distribution of test patterns. For categorization tasks, the network’s prediction is given by $f^(x)=sign(w⋅h(x))$. Performance is measured as the fraction of incorrect predictions. Error bars represent standard error of the mean across realizations of network weights and tasks.

#### Optimal granule–Purkinje cell weight distribution

We adapted our model to allow for comparisons with Brunel et al., 2004 by constraining readout weights $w$ to be nonnegative and adding a bias, $f(x)=w⋅h(x)+b$. To guarantee that the target function is nonnegative, we set $f(x)\in{0,1}$ for the random categorization task and $f(x)←|f(x)|$ for the Gaussian process tasks. The weights and bias were determined with the Python convex optimization package cvxopt (Andersen et al., 2011).

### Model of two-joint arm

We implemented a biophysical model of a planar two-joint arm (Fagg et al., 1997). The state of the arm is specified by six variables: joint angles $\theta_{1}$ and $\theta_{2}$, angular velocities $\theta˙_{1}$ and $\theta˙_{2}$, and torques u1 and u2. The upper and lower segments of the arm have lengths l1 and l2 and masses m1 and m2, respectively. The arm has the following dynamics:

$$
M(\theta)\theta¨+C(\theta,\theta˙)\theta˙=u,
$$

where $M(\theta)$ is the inertia matrix and $C(\theta,\theta˙)$ is the matrix of centrifugal, Coriolis, and friction forces:

$$
M(\theta)=(I_{1}+I_{2}+m_{2}l_{1}^{2}+2m_{2}l_{1}l¯_{2}cos(\theta_{2})I_{2}+m_{2}l_{1}l¯_{2}cos(\theta_{2})I_{2}+m_{2}l_{1}l_{2}cos(\theta_{2})I_{2}),
$$



$$
C(\theta,\theta˙)=m_{2}l_{1}l_{2}sin(\theta_{2})(−2\theta_{2}˙−\theta_{2}˙\theta_{1}˙0)+(D_{1}00D_{2}),
$$

where $l¯_{2}$ is the center of mass of the lower arm, I1 and I2 are moments of inertia and D1 and D2 are friction terms of the upper and lower arm respectively. These parameters were $m_{1}=3⁢ kg$, $m_{2}=2.5⁢ kg$, $l_{1}=0.3⁢ m$, $l_{2}=0.35⁢ m$, $l¯_{2}=0.21⁢ m$, $I_{1}=0.1⁢ kg m^{2}$, $I_{2}=0.12⁢ kg m^{2}$, $D_{1}=0.05⁢ kg m^{2}/s$ and $D_{2}=0.01⁢ kg m^{2}/s$.

The task is to predict the position of the hand based on the forward dynamics of the two-joint arm system, given the arm initial condition and the applied torques. More precisely, the $P$ network inputs $x^{\mu}$ were generated by sampling 6-dimensional Gaussian vectors with covariance matrix $C=diag(\sigma_{\theta},\sigma_{\theta},\sigma_{\theta˙},\sigma_{\theta˙},\sigma_{u},\sigma_{u})$, to account for the fact that angles, angular velocities and torques might vary on different scales across simulations. For our results, we used $\sigma_{\theta}=\sigma_{\theta˙}=0.1$ and $\sigma_{u}=1$. Each sample $x^{\mu}$ was then normalized and used to generate initial conditions of the arm, by setting $\theta_{1}^{\mu}=\frac{\pi}{4}+x_{1}^{\mu}$, $\theta_{2}^{\mu}=\frac{\pi}{4}+x_{2}^{\mu}$, $\theta˙_{1}^{\mu}=x_{3}^{\mu}$, and $\theta˙_{2}^{\mu}=x_{4}^{\mu}$. Torques were generated by setting $u_{1}^{\mu}=x_{5}^{\mu}$ and $u_{2}^{\mu}=x_{6}^{\mu}$. The target was constructed by running the dynamics of the arm forward in time for a time $\delta=0.2⁢ s$, and by computing the difference in position of the “hand” (i.e. the end of the lower segment) in Cartesian coordinates. As a result, the target in this task is two-dimensional, with each target dimension corresponding the one of the two Cartesian coordinates of the hand. The overall performance is assessed by computing the error on each task separately and then averaging the errors.

### Model of electrosensory lateral line lobe (ELL)

We simulated 20,000 granule cells using the biophysical model of Kennedy et al., 2014. We varied the granule cell layer coding level by adjusting the spiking threshold parameter in the model. For each choice of threshold, we generated 30 different trials of spike rasters. Each trial is 160ms long with a 1ms time bin and consists of a time-locked response to an electric organ discharge command. Trial-to-trial variability in the model granule cell responses arises from noise in the mossy fiber responses. To generate training and testing data, we sampled 4 trials ($P=640$ patterns) from the 30 total trials for training and 10 trials for testing (1600 patterns). Coding level is measured as the fraction of granule cells that spike at least once in the training data. We repeated this sampling process 30 times.

The targets were smoothed broad-spike responses of 15 MG cells time-locked to an electric organ discharge command measured during experiments (Muller et al., 2019). The original data set consisted of 55 MG cells, each with a 300ms long spike raster with a 1ms time bin. The spike rasters were trial-averaged and then smoothed with a Gaussian-weighted moving average with a 10ms time window. Only MG cells whose maximum spiking probability across all time bins exceeded 0.01 after smoothing were included in the task. The same MG cell responses were used for both training and testing. To match the length of the granule cell data, we discarded MG cell data beyond 160ms and then concatenated 4 copies of the 160ms long responses for training and 10 copies for testing. We measured the ability of the model to construct MG cell targets out of granule cell activity, generalizing across noise in granule cell responses. Errors for each MG cell target were averaged across the 30 repetitions of sampling of training and testing data, and then averaged across targets. Standard error of the mean was computed across the 30 repetitions.

### Model of vestibulo-ocular reflex (VOR)

Recordings of Purkinje cell activity in monkeys suggest that these neurons exhibit piecewise-linear tuning to head velocity (Lisberger et al., 1994). Thus, we designed piecewise-linear target functions representing Purkinje cell firing rate as a function of head velocity $v$, a one-dimensional input:

$$
f(v)={m_{1}(v−c)+bx<cm_{2}(v−c)+bx\geqc.
$$

Inputs $v$ were sampled uniformly from $[-1,1]$ 100 times. We generated 25 total target functions using all combinations of slopes m1 and m2 sampled from 5 equally spaced points on the interval $[-2,2]$. We set $b=0.1$ and $c=-0.2$.

Mossy fiber responses to head velocity input were modeled as exponential tuning curves:

$$
n_{j}(v)=g_{j}exp⁡(vr_{j})+b_{j},
$$

where gj is a gain term, $r_{j}\in\pm1$ determines a mossy fiber preference for positive or negative velocities, and bj is the baseline firing rate. We generated 24 different tuning curves from all combinations of the following parameter values: The gain gj was sampled from 6 equally spaced points on the interval $[0.1,1]$, rj was set to either –1 or 1, and bj was set to either 0 or 1. Qualitative results did not depend strongly on this parameterization. Mossy fiber to granule cell weights were random zero-mean Gaussians. Errors were averaged across targets.
