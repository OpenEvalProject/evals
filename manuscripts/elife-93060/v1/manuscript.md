# Aligned and oblique dynamics in recurrent neural networks

## Authors

- Friedrich Schuessler<sup>1</sup> ([ORCID: 0000-0002-6716-7492](https://orcid.org/0000-0002-6716-7492)) †
- Francesca Mastrogiuseppe<sup>3</sup> ([ORCID: 0000-0002-7682-5178](https://orcid.org/0000-0002-7682-5178))
- Srdjan Ostojic<sup>4</sup> ([ORCID: 0000-0002-7473-1223](https://orcid.org/0000-0002-7473-1223))
- Omri Barak<sup>5</sup> ([ORCID: 0000-0002-7894-6344](https://orcid.org/0000-0002-7894-6344))

### Affiliations

1. Faculty of Electrical Engineering and Computer Science, Technical University of Berlin Berlin Germany ([ROR:03v4gjf40](https://ror.org/03v4gjf40))
2. Science of Intelligence, Research Cluster of Excellence Berlin Germany
3. Champalimaud Foundation Lisbon Portugal ([ROR:03g001n57](https://ror.org/03g001n57))
4. Laboratoire de Neurosciences Cognitives et Computationnelles, INSERM U960, Ecole Normale Superieure-PSL Research University Paris France ([ROR:013cjyk83](https://ror.org/013cjyk83))
5. Rappaport Faculty of Medicine and Network Biology Research Laboratories, Technion - Israel Institute of Technology Haifa Israel ([ROR:03qryx823](https://ror.org/03qryx823))

† Corresponding author

## Abstract

The relation between neural activity and behaviorally relevant variables is at the heart of neuroscience research. When strong, this relation is termed a neural representation. There is increasing evidence, however, for partial dissociations between activity in an area and relevant external variables. While many explanations have been proposed, a theoretical framework for the relationship between external and internal variables is lacking. Here, we utilize recurrent neural networks (RNNs) to explore the question of when and how neural dynamics and the network’s output are related from a geometrical point of view. We find that training RNNs can lead to two dynamical regimes: dynamics can either be aligned with the directions that generate output variables, or oblique to them. We show that the choice of readout weight magnitude before training can serve as a control knob between the regimes, similar to recent findings in feedforward networks. These regimes are functionally distinct. Oblique networks are more heterogeneous and suppress noise in their output directions. They are furthermore more robust to perturbations along the output directions. Crucially, the oblique regime is specific to recurrent (but not feedforward) networks, arising from dynamical stability considerations. Finally, we show that tendencies toward the aligned or the oblique regime can be dissociated in neural recordings. Altogether, our results open a new perspective for interpreting neural activity by relating network dynamics and their output.

## Introduction

The relation between neural activity and behavioral variables is often expressed in terms of neural representations. Sensory input and motor output have been related to the tuning curves of single neurons (Hubel and Wiesel, 1962; O’Keefe and Dostrovsky, 1971; Hafting et al., 2005) and, since the advent of large-scale recordings, to population activity (Buonomano and Maass, 2009; Saxena and Cunningham, 2019; Vyas et al., 2020). Both input and output can be decoded from population activity (Churchland et al., 2012; Mante et al., 2013), even in real-time, closed-loop settings (Sadtler et al., 2014; Willett et al., 2021). However, neural activity is often not fully explained by observable behavioral variables. Some components of the unexplained neural activity have been interpreted as random trial-to-trial fluctuations (Galgali et al., 2023), potentially linked to unobserved behavior (Stringer et al., 2019b; Musall et al., 2019; Wang et al., 2023). Activity may further be due to other ongoing computations not immediately related to behavior, such as preparatory motor activity in a null space of the motor readout (Kaufman et al., 2014; Hennequin et al., 2014). Finally, neural activity may partially be due to other constraints, e.g., related to the underlying connectivity (Atallah and Scanziani, 2009; Okun and Lampl, 2008), the process of learning (Sadtler et al., 2014), or stability, i.e., the robustness of the neural dynamics to perturbations (Russo et al., 2020).

Here, we aim for a theoretical understanding of neural representations: Which factors might determine how strongly activity and behavioral output variables are related? To this end, we use trained recurrent neural networks (RNNs). In this setting, output variables are determined by the task at hand, and neural activity can be described by its projection onto the principal components (PCs). We show that these networks can operate between two extremes: an ‘aligned’ regime in which the output weights and the largest PCs are strongly correlated, and a second, ‘oblique’ regime, where the output weights and the largest PCs are poorly correlated.

What determines the regime in which a network operates? We show that quite general considerations lead to a link between the magnitude of output weights and the regime of the network. As a consequence, we can use output magnitude as a control knob for trained RNNs. Indeed, when we trained RNN models on different neuroscience tasks, large output weights led to oblique dynamics, and small output weights to aligned dynamics. Recent results in feedforward networks identified two regimes – rich and lazy – that can also arise from choices of output weights (Chizat et al., 2019; Jacot et al., 2018). In an extensive Methods section, we further analyze in detail how the oblique and aligned regimes arise during learning. There we show that the dynamical nature of RNNs, in particular demanding stable dynamics, leads to the replacement of unstable, lazy, solutions by oblique ones.

We then considered the functional consequences of the two regimes. Building on the concept of feedback loops driving the network dynamics (Sussillo and Abbott, 2009; Rivkind and Barak, 2017), we show that, in the aligned regime, the largest PCs and the output are qualitatively similar. In the oblique regime, in contrast, the two may be qualitatively different. This functional decoupling in oblique networks leads to a large freedom for neural dynamics. Different networks with oblique dynamics thus tend to employ different dynamics for the same tasks. Aligned dynamics, in contrast, are much more stereotypical. Furthermore, as a result of how neural dynamics and output are coupled, oblique and aligned networks react differently to perturbations of the neural activity along the output direction. In particular, oblique (but not aligned) networks develop an additional negative feedback loop that suppresses output noise. We finally show that neural recordings from different experiments can have different degrees of alignment, which indicates that our theoretical results may be useful in identifying different regimes for different experiments, tasks, or brain regions.

Altogether, our work opens a new perspective relating network dynamics and their output, yielding important insights for modeling brain dynamics as well as experimentally accessible questions about learning and dynamics in the brain.

## Results

### Aligned and oblique population dynamics

We consider an animal performing a task while both behavior and neural activity are recorded. For example, the task might be to produce a periodic motion, described by the output $z(t)$ of Figure 1A. For simplicity, we assume that the behavioral output can be decoded linearly from the neural activity (Mante et al., 2013; Sadtler et al., 2014; Gallego et al., 2017; Russo et al., 2018; Willett et al., 2021). We can thus write

$$
z(t)=\sumi=1Nw_{out,i}x_{i}(t)=w_{out}^{T}x(t),
$$

with readout weights $𝐰_{out}$. The activity of neuron $i\in{1,…,N}$ is given by $x_{i}(t)$, and we refer to the vector $𝐱$ as the state of the network.

![Figure 1.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig1-v1.jpg)

**Figure 1.:** (A) Output generated by both networks. (B) Neural activity of aligned (top) and oblique (bottom) dynamics, visualized in the space spanned by three neurons. Here, the activity (green) is three-dimensional, but most of the variance is concentrated along the two largest principal components (PCs) (blue). For aligned dynamics, the output weights (red) are small and lie in the subspace spanned by the largest PCs; they are hence correlated to the activity. For oblique dynamics, the output weights are large and lie outside of the subspace spanned by the largest PCs; they are hence poorly correlated to the activity. (C) Projection of activity onto the two largest PCs. For oblique dynamics, the output weights are orthogonal to the leading PCs. (D) Evolution of PC projections over time. For aligned dynamics, the projection on the PCs resembles the output $z(t)$, and reconstructing the output from the largest two components is possible. For the oblique dynamics, such reconstruction is not possible, because the projections oscillate much more slowly than the output.

Neural activity has to generate the output in some subspace of the state space, where each axis represents the activity of one neuron. In the simplest case (Figure 1B, top), the output is produced along the largest PCs of activity, as shown by the fact that projecting the neural activity $𝐱(t)$ onto the largest PCs returns the target oscillation (Figure 1D, top). We call such dynamics ‘aligned’ because of the alignment between the subspace spanned by the largest PCs and the output vector (red).

There is, however, another possibility. Neural activity may have many other components not directly related to the output and these other components may even dominate the overall activity. In this case (Figure 1B and D, bottom), the two largest PCs are not enough to read out the output, and smaller PCs are needed. We call such dynamics ‘oblique’ because the subspace spanned by the largest PCs and the output vector are poorly aligned.

We consider these two possibilities as distinct dynamical regimes, noting that intermediate situations are also possible. The actual regime of neural dynamics has important consequences for how one interprets neural recordings. For aligned dynamics, analyzing the dynamics within the largest PCs may lead to insights about the computations generating the output (Vyas et al., 2020). For oblique dynamics, such an analysis is hampered by the dissociation between the large PCs and the components generating the output (Russo et al., 2018).

### Magnitude of output weights controls regime in trained RNNs

What determines which regime a neural network operates in? Given that behavior is the same, but representations differ, we study this question using trained RNNs. This framework constrains what networks do, but not how they do it (Sussillo, 2014; Barak, 2017). The specific property of representation we are interested in is the alignment, or correlation, between output weights and states:

$$
ρ(t)=w_{out}^{T}x(t)/(‖w_{out}‖‖x(t)‖),
$$

where the vector norms $‖𝐰_{out}‖$ and $‖𝐱‖$ quantify the magnitude of each vector.

For aligned dynamics, the correlation is large, corresponding to the alignment between the leading PCs of the neural activity and the output weights (Figure 1B, top). In contrast, for oblique dynamics, this correlation is small (Figure 1B, bottom). Note that the concept of correlation can be generalized to accommodate multiple time points and multidimensional output (see section Generalized correlation).

Studying the same task means that the output $z$ is the same, so it is instructive to express it in terms of the correlation $ρ$:

$$
z(t)=ρ(t)‖w_{out}‖‖x(t)‖.
$$

Recent work on feedforward networks showed that $‖𝐰_{out}‖$ can have a large effect on the resulting representations (Jacot et al., 2018; Chizat et al., 2019). Equation 3 shows that $ρ$ is indeed linked to $‖𝐰_{out}‖$, but $‖𝐱(t)‖$ can also vary. In a detailed analysis in the Methods (sections Analysis of solutions under noiseless conditions to Oblique solutions arise for noisy, nonlinear systems), we show that for recurrent networks, stability considerations preclude $‖𝐱(t)‖$ from being small. This implies that if we choose a readout norm $‖𝐰_{out}‖$ and then train the RNN on a given task, the correlation must compensate.

If we choose small output weights, we expect aligned dynamics, because a large correlation is necessary to generate sufficiently large output (Figure 1B, top). If instead we choose large output weights, we expect oblique dynamics, because only a small correlation keeps the output magnitude from growing too large.

We tested whether output weights can serve as a control knob to select dynamical regimes using an RNN model trained on an abstract version of the cycling task introduced in Russo et al., 2018. The networks were trained to generate a 2D signal that rotated in the plane spanned by two outputs $z_{1}(t)$ and $z_{2}(t)$ (Figure 2A). An input pulse at the beginning of each trial indicated the desired direction of rotation. We set up two models with either small or large output weights and trained the recurrent weights of each with gradient descent (section Details on RNN models and training).

![Figure 2.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig2-v1.jpg)

**Figure 2.:** (A) A network with two outputs was trained to generate either clockwise or anticlockwise rotations, depending on the context (top). Our model recurrent neural network (RNN) (bottom) received a context input pulse, generated dynamics $𝐱(t)$ via recurrent weights $W$, and yielded the output as linear projections of the states. We trained the recurrent weights $W$ with gradient descent. (B, C) Resulting internal dynamics for two networks with small (top) and large (bottom) output weights, corresponding to aligned and oblique dynamics, respectively. (B) Dynamics projected on the first two principal components (PCs) and the remaining direction $𝐰_{out,⟂}$ of the first output vector (for $z_{1}$). The output weights are amplified to be visible. Arrowheads indicate the direction of the dynamics. Note that for the large output weights, the dynamics in the first two PCs co-rotated, despite the counter-rotating output. (C) Output reconstructed from the largest PCs, with dimension $D=2$ (full lines) or 8 (dotted). Two dimensions already yield a fit with $R^{2}=0.99$ for aligned dynamics (top), but almost no output for oblique (bottom, $R^{2}=0.005$, no arrows shown). For the latter, a good fit with $R^{2}>90$% is only reached with $D=8$.

After both models learned the task, we projected the network activity into a three-dimensional (3D) space spanned by the two largest PCs of the dynamics $𝐱(t)$. A third direction, $𝐰_{out,⟂}$, spanned the remaining part of the first output vector $𝐰_{out,1}$. The resulting plots, Figure 2B, corroborate our hypothesis: Small output weights led to aligned dynamics with a large correlation between the largest PCs and the output weights. In contrast, the large output weights of the second network were almost orthogonal, or oblique, to the two leading PCs. Further qualitative differences between the two solutions in terms of the direction of trajectories will be discussed below.

Another way to quantify these regimes is by the ability to reconstruct the output from the large PCs of neural activity, as quantified by the coefficient of determination $R^{2}$. For the aligned network, the projection on the two largest PCs (Figure 2C, solid) already led to a good reconstruction. For the oblique networks, the two largest PCs were not sufficient. We needed the first eight dimensions (Figure 2C, dashed) to obtain a good reconstruction ($R^{2}>0.9$). In contrast to the differences in these fits, the neural dynamics themselves were much more similar between the networks. Specifically, 90% of the variance was explained by four and five dimensions for the aligned and oblique networks, respectively.

Can we use the output weights to induce aligned or oblique dynamics in more general settings? We trained RNN models with small or large initial output weights on five different neuroscience tasks (section Task details). All weights (input, recurrent, and output) were trained using the Adam algorithm (section Details on RNN models and training). After training, we measured the three quantities of Equation 3: magnitudes of neural activity and output weights, and the correlation between the two. The results in Figure 3A show that across tasks, initialization with large output weights led to oblique dynamics (small correlation), and with small output weights to aligned dynamics (large correlation). While training could, in principle, change the initially small output weights to large ones (and vice versa), we noticed that this does not happen. Small output weights did increase with training, but the large gap in norms remained. This shows that setting the output weights at initialization can serve to determine their scale after learning under realistic settings. While explaining this observation is beyond the scope of this work, we note that (1) changing the internal weights suffices to solve the task, and (2) the extent to which the output weights change during learning depends on the algorithm and specific parameterization (Jacot et al., 2018; Geiger et al., 2020; Yang and Hu, 2020).

![Figure 3.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig3-v1.jpg)

**Figure 3.:** (A) Correlation and norms of output weights and neural activity. For each task, we initialized networks with small or large output weights (dark vs light orange). The initial norms $‖𝐰_{out}‖$ are indicated by the dashed lines. Learning only weakly changes the norm of the output weights. Note that all y-axes are logarithmically scaled. (B) Variance of $𝐱$ explained and $R^{2}$ of reconstructed output for projections of $𝐱$ on increasing number of principal components (PCs). Results from one example network trained on the cycling task are shown for each condition. (C) Number of PCs necessary to reach 90% of the variance of $𝐱(t)$ or of the $R^{2}$ of the output reconstruction (top/bottom; dotted lines in B). In (A, C) violin plots show the distribution over five sample networks, with vertical bars indicating the mean and the extreme values (where visible).

In Figure 3B and C, we adopted the perspective of Figure 2C and quantified how well we can reconstruct the output from a projection of $𝐱$ onto its largest $D$ PCs (section Regression). As expected, both the variance of $𝐱$ explained and the quality of output reconstruction increased, for an increasing number of PCs $D$ (Figure 3B). How both quantities increased, however, differs between the two regimes. While the variance explained increased similarly in both cases, the quality of the reconstruction increased much more slowly for the model with large output weights. We quantified this phenomenon by comparing the dimensions at which either the variance of $𝐱$ explained or $R^{2}$ reaches 90%, denoted by $D_{x,90}$ and $D_{fit,90}$, respectively.

In Figure 3C, we compare $D_{x,90}$ and $D_{fit,90}$ across multiple networks and tasks. Generally, larger output weights led to larger numbers for both. However, for large output weights, the number of PCs necessary to obtain a good reconstruction increased much more drastically than the dimension of the data. Thus, the output was less well represented by the large PCs of the dynamics for networks with large output weights, in agreement with our notion of oblique dynamics.

Importantly, reaching the aligned and oblique regimes relies on ensuring robust and stable dynamics, which we achieve by adding noise to the dynamics during training. This yields a similar magnitude of neural activity $‖𝐱‖$ across networks and tasks (Figure 3A). We show in Methods, section Analysis of solutions under noiseless conditions, that learning in simple, noise-free conditions with large output weights can lead to solutions not captured by either aligned or oblique dynamics; those solutions, however, are unstable. Furthermore, we observed that some of the qualitative differences between aligned and oblique dynamics are less pronounced if we initialized networks with small recurrent weights and initially decaying dynamics (Appendix 1—figure 2).

### Neural dynamics decouple from the output for the oblique regime

What are the functional consequences of the two regimes? A hint might be seen in an intriguing qualitative difference between the aligned and oblique solutions for the cycling task in Figure 2. For the aligned network, the two trajectories for the two different contexts (green and purple) are counter-rotating (Figure 2B, top). This agrees with the output, which also counter-rotates as demanded by the task (Figure 2A). In contrast, the neural activity of the oblique network co-rotates in the leading two PCs (Figure 2B, bottom). This is despite the counter-rotating output, since this network also solves the task (not shown). The co-rotation also indicates why reconstructing the output from the leading two PCs is not possible (Figure 2C). Naturally, the dynamics also contain counter-rotating trajectories for producing the correct output, but these are only present in low-variance PCs. (Note also that for aligned networks, one can also observe co-rotation in low-variance PCs, see Appendix 1—figure 3.) Taken together, aligned and oblique dynamics differ in the coupling between leading neural dynamics and output. For aligned dynamics, the two are strongly coupled. For oblique dynamics, the two decouple qualitatively.

Such a decoupling for oblique, but not aligned, dynamics leads to a prediction regarding the universality of solutions (Maheswaranathan et al., 2019; Turner et al., 2021; Pagan et al., 2022). For aligned dynamics, the coupling implies that the internal dynamics are strongly constrained by the task. We thus expect different learners to converge to similar solutions, even if their initial connectivity is random and unstructured. In Figure 4A, we show the dynamics of three randomly initialized aligned networks trained on the cycling task, projected onto the three leading PCs. Apart from global rotations, the dynamics in the three networks are very similar.

![Figure 4.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig4-v1.jpg)

**Figure 4.:** (A, B) Examples of networks trained on the cycling task with small (aligned) or large (oblique) output weights. The top left and central networks, respectively, are the same as those plotted in Figure 2. (C) Dissimilarity between solutions across different tasks. Aligned dynamics (red) were less dissimilar to each other than oblique ones (yellow). The violin plots show the distribution over all possible different pairs for five samples (mean and extrema as bars).

For oblique dynamics, the task-defined output exerts weaker constraints on the internal dynamics. Any variability experienced during learning can potentially build up, and eventually create qualitatively different solutions. Three examples of oblique networks solving the cycling tasks indeed show visibly different dynamics (Figure 4B). Further analysis shows that the models also differ in the frequency components in the leading dynamics (Appendix 1—figure 4).

The degree of variability between learners depends on the task. The observable differences in the PC projections were most striking for the cycling task. For the flip-flop task, for example, solutions were generally noisier in the oblique regime than in the aligned but did not have observable qualitative differences in either regime (Appendix 1—figure 5). We quantified the difference between models for the different neuroscience tasks considered before. To compare different neural dynamics, we used a dissimilarity measure invariant under rotation (section Dissimilarity measure) (Williams et al., 2021). The results are shown in Figure 4C. Two observations stand out: First, across tasks, the dissimilarity was higher for networks in the oblique regime than for those in the aligned. Second, both overall dissimilarity and the discrepancy between regimes differed strongly between tasks. The largest dissimilarity (for oblique dynamics) and the largest discrepancy between regimes was found for the cycling. The smallest discrepancy between regimes was found for the flip-flop task. Such a difference between tasks is consistent with the differences in the range of possible solutions for different tasks, as reported in Turner et al., 2021; Maheswaranathan et al., 2019.

What are the underlying mechanisms for the qualitative decoupling in oblique, but not aligned networks? For aligned dynamics, we saw that the small output weights demand large activity to generate the output. In other words, the activity along the largest PCs must be coupled to the output. For oblique dynamics, this constraint is not present, which opens the possibility for small components outside the largest PCs to generate the output. If this is the case, we have a decoupling, such as the observed co-rotation in the cycling task, and the possible variability between solutions. We discuss this point in more detail in the Methods, section Mechanisms behind decoupling of neural dynamics and output.

In the following two sections, we will explore how the decoupling between neural dynamics and output for oblique, but not aligned, dynamics influences the response to perturbations and the effects of noise during learning.

### Differences in response to perturbations

Understanding how networks respond to external perturbations and internal noise requires some insight into how dynamics are generated. Dynamics of trained networks are mostly generated internally, through recurrent interactions. In robust networks, these internally generated dynamics are a prominent part of the largest PCs (among input-driven components; section Analysis of solutions under noiseless conditions and Oblique solutions arise for noisy, nonlinear systems). Internally generated dynamics are sustained by positive feedback loops, through which neurons excite each other. Those loops are low-dimensional, with activity along a few directions of the dynamics being amplified and fed back along the same directions. This results in dynamics being driven by effective feedback loops along the largest PCs (Figure 5A). As shown above, the largest PCs can either be aligned or not aligned, with the output weights. This leads to predictions about how aligned and oblique networks differentiate in their responses to perturbations along different directions.

![Figure 5.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig5-v1.jpg)

**Figure 5.:** (A) Cartoon illustrating the relationship between perturbations along output weights or principal components (PCs) and the feedback loops driving autonomous dynamics. (B) Output after perturbation for aligned (top) and oblique (bottom) networks trained on the cycling task. The unperturbed network (light red line) yields a sine wave along the first output direction $z_{1}$. At $t_{p}=9$, a perturbation with amplitude $‖Δ𝐱‖=34$ is applied along the output weights (dashed red) or the first PC (dashed-dotted blue). The perturbations only differ in the directions applied. While the immediate response for the oblique network to a perturbation along the output weights is much larger, $z_{1}(t_{p})≈80$, the long-term dynamics yield the same output as the unperturbed network. See also Appendix 1—figure 6 for more details. (C) Loss for perturbations of different amplitudes for the two networks in (B). Lines and shades are means and standard deviations over different perturbation times $t_{p}\in[5,15]$ and random directions spanned by the output weights (red) or the two largest PCs (blue). The loss is the mean squared error between output and target for $t>20$. The gray dot indicates an example in (B). (D) Relative susceptibility of networks to perturbation directions for different tasks and dynamical regimes. We measured the area under the curve (AUC) of loss over perturbation amplitude for perturbations along the output weights of the two largest PCs. The relative susceptibility is the ratio between the two AUCs. The example in (C) is indicated by gray triangles.

Our intuition about feedback loops suggests that networks respond strongly to a perturbation that is aligned with the directions contributing to the feedback loop, but weakly to a perturbation that is orthogonal to them. In particular, if a perturbation is applied along the output weights, aligned and oblique dynamics should dissociate, with a strong disruption of dynamics for aligned, but not for oblique dynamics (Figure 5A).

To test this, we compare the response to perturbations along the output direction and the largest PCs. We apply perturbations to the neural activity at a single point in time: $𝐱(t)$ evolves undisturbed until time $t_{p}$. At that point, it is shifted to $𝐱(t_{p})+Δ𝐱$. After the perturbation, we let the network evolve freely and compare this evolution to that of an unperturbed copy. Such a perturbation mimics a very short optogenetic perturbation applied to a selected neural population (O’Shea et al., 2022; Finkelstein et al., 2021). In Figure 5B, we show the output after such perturbations for an aligned (top) and an oblique network (bottom) trained on the cycling task. The time point and amplitude are the same for both directions and networks. For each network and type of perturbation, there is an immediate deflection and a long-term response. For both networks, perturbing along the PCs (blue) leads to a long-term phase shift. Only in the aligned network, however, perturbation along the output direction (red) leads to a visible long-term response. In the oblique network, the amplitude of the immediate response is larger, but the long-term response is smaller. Our results for the oblique network, but not for the aligned, agree with simulations of networks generating EMG data from the cycling experiments (Saxena et al., 2022).

To quantify the relative long-term susceptibility of networks to perturbations along output weights or PCs, we sampled from different times $t_{p}$ and different directions in the 2D subspaces spanned either by the two output vectors or by the two largest PCs. For each perturbation, we measured the loss of the perturbed networks on the original task (excluding the immediate deflection after the perturbation by starting to compute the loss at $t_{p}+5$). Figure 5C shows that the aligned network is almost equally susceptible to perturbations along the PCs and the output weights. In contrast, the oblique network is much more susceptible to perturbations along the PCs.

We repeated this analysis for oblique and aligned networks trained on the five different tasks. We computed the area under the curve (AUC) for both loss profiles in Figure 5C. We then defined the ‘relative susceptibility’ as the ratio $AUC_{𝐰_{out}}/AUC_{PC}$, Figure 5D. For aligned networks (red), the relative susceptibility was close to 1 indicating similarly strong responses to both types of perturbations. For oblique networks (yellow), it was much smaller than 1, indicating that long-term responses to perturbations along the output direction were weaker than those to perturbations along the PCs.

### Noise suppression for oblique dynamics

In the oblique regime, the output weights are large. To produce the correct output (and not a too large one), the large PCs of the dynamics are almost orthogonal to the output weights. The large output weights, however, pose a robustness problem: Small noise in the direction of the output weights is also amplified at the level of the readout. We show that learning leads to a slow process of sculpting noise statistics to avoid this effect (Figure 11). Specifically, a negative feedback loop is generated that suppresses fluctuations along the output direction (Figure 6A, Figure 10; Kadmon et al., 2020). Because the positive feedback loop that gives rise to the large PCs is mostly orthogonal to the output direction, it remains unaffected by this additional negative feedback loop. A detailed analysis of how learning is affected by noise shows that, for large output weights, the network first learns a solution that is not robust to noise. This solution is then transformed to increasingly stable and oblique dynamics over longer time scales (section Learning with noise for linear RNNs and Oblique solutions arise for noisy, nonlinear systems).

![Figure 6.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig6-v1.jpg)

**Figure 6.:** (A) A cartoon of the feedback loop structure for aligned (top) and oblique (bottom) dynamics. The latter develops a negative feedback loop which suppresses fluctuations along the output direction. (B) Comparing the distribution of variance of mean-subtracted activity along different directions for networks trained on the cycling task (see Appendix 1—figure 7): principal components (PCs) of trial-averaged activity (blue), readout (red), and random (gray) directions. For the PCs and output weights, we sampled 100 normalized combinations of either the first two PCs or the two output vectors. For the random directions, we drew 1000 random vectors in the full, $N$-dimensional space. (C) Noise compression across tasks as measured by the ratio between variance along output and random directions. The dashed line indicates neither compression nor expansion. Black markers indicate the values for the two examples in (B, C). Note the log-scales in (B, C).

To illustrate the effect of the negative feedback loop, we consider the fluctuations around trial averages. We take a collection of states $𝐱(t)$ and then subtract the task-conditioned averages $𝐱‾(t)$ to compute $\delta𝐱(t)=𝐱(t)−𝐱‾(t)$. We then project $\delta𝐱(t)$ onto three different direction categories: the largest PCs of the averaged data $𝐱‾(t)$, the output directions, or randomly drawn directions.

How strongly the activity fluctuates along each direction is quantified by the variance of the projections (Figure 6B). For both aligned and oblique dynamics, the variance is much larger along the PCs than along random directions. This is not necessarily expected, because the PCA was performed on the averaged activity, without the fluctuations. Instead, it is a dynamical effect: the same positive feedback that generates the autonomous dynamics also amplifies the noise (section Oblique solutions arise for noisy, nonlinear systems).

The two network regimes, however, dissociate when considering the variance along the output direction. For aligned dynamics, there is no negative feedback loop, and $𝐰_{out}$ is correlated with the PCs. The variance along the output direction is hence similar to that along the PCs, and larger than along random directions. For oblique dynamics, the negative feedback loop suppresses the fluctuations along the output direction, so that they become weaker than along random directions.

In Figure 6C, we quantify this dissociation across different tasks. We measured the ratio between variance along output and random directions. Aligned networks have a ratio much larger than one, indicating that the fluctuations along the output direction are increased due to the autonomous dynamics along the PCs. In contrast, oblique networks have a ratio smaller than 1 for all tasks, which indicates noise compression along the output.

### Different degrees of alignment in experimental settings

For the cycling task, we observed that dynamics were qualitatively different for the two regimes, with trajectories either counter- or co-rotating (Figure 2B). Interestingly, the experimental results of Russo et al., 2018, matched the oblique, but not the aligned dynamics. The authors observed co-rotating dynamics in the leading PCs of motor cortex activity despite counter-rotating activity of simultaneously recorded muscle activity. Here, we test whether our theory can help to more clearly and quantitatively distinguish between the two regimes in experimental settings.

In typical experimental settings, we do not have direct access to output weights. We can, however, approximate these by fitting neural data to simultaneously recorded behavioral output, such as hand velocity in a motor control experiment (Figure 7A, top). Following the model above, where the output is a weighted average of the states, we reconstruct the output from the neural activity with linear regression. To quantify the dynamical regime, we then compute the correlation $ρ$ between the weights from fitting and the neural data. Additionally, we can also quantify the alignment by the ‘relative fitting dimension’ $D_{fit,90}/D_{x,90}$, where $D_{fit,90}$ is the number of PCs necessary to recover the output and $D_{x,90}$ number to the number of PCs necessary to represent 90% of the variance of the neural data. We computed both the correlation and the relative fitting dimension for different publicly available data sets (Figure 7B). For details, see section Experimental data.

![Figure 7.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig7-v1.jpg)

**Figure 7.:** (A) Diagram of the two types of experimental data considered. Here, we always took the velocity as the output (hand, finger, or cursor). In motor control experiments (top), we first needed to obtain the output weights $𝐰_{out}$ via linear regression. We then computed the correlation $ρ$ and the reconstruction dimension $D_{fit,90}$, i.e., the number of principal components (PCs) of $𝐱$ necessary to obtain a coefficient of determination $R^{2}>90$%. In brain-computer interface (BCI) experiments (bottom), the output (cursor velocity) is generated from neural activity $𝐱(t)$ via output weights $𝐰_{out}$ defined by the experimenter. This allowed us to directly compute correlations and fitting dimensions. (B) Correlation $ρ$ (top) and relative fitting dimension $D_{fit,90}/D_{x,90}$ (bottom) for several publicly available data sets. The cycling task data (purple) were trial-conditioned averages, the BCI experiments (red) and Neural Latents Benchmark (NLB) tasks (yellow) single-trial data. Results for the full data sets are shown as dots. Violin plots indicate results for 20 random subsets of 25% of the data points in each data set (bars indicate mean). See small text below x-axis for the number of time points and neurons.

We started with data sets from two monkeys performing the cycling task (Russo et al., 2018). The data contained motor cortex activity, hand movement, and EMG from the arms, all averaged over multiple trials of the same condition. In Figure 7B, we show results for reconstructing the hand velocity. The correlation was small, $ρ\in[0.04,0.07]$. To obtain a good reconstruction, we needed a substantial fraction of the dimension of the neural data: The relative fitting dimension was $D_{fit,90}/D_{x,90}\in[0.7,0.8]$. Our results agree with previous studies, showing that the best decoding directions are only weakly correlated with the leading PCs of motor cortex activity (Schroeder et al., 2022).

We also analyzed data made available through the Neural Latents Benchmark (NLB) (Pei et al., 2021). In two different tasks, monkeys needed to perform movements along a screen. In a random target task, the monkeys had to point at a randomly generated target position on a screen, with a successive target point generated once the previous one was reached (Makin et al., 2018). In a maze task, the monkeys were trained to follow a trajectory through a maze with their hand (Churchland et al., 2010). In both cases, we reconstructed the finger or hand velocity from neural activity on single trials. The correlation was higher than in the cycling task, $ρ=0.13$. The relative fitting dimension was lower than in the trial-averaged cycling data, albeit still on the same order: $D_{fit,90}/D_{x,90}\in[0.4,0.5]$.

Finally, we considered brain-computer interface (BCI) experiments (Sadtler et al., 2014). In these experiments, monkeys were trained to control a cursor on a screen via activity read out from their motor cortex (Figure 7A, bottom). The output weights generating the cursor velocity were set by the experimenter (so we don’t need to fit). Importantly, the output weights were typically chosen to be spanned by the largest PCs (the ‘neural manifold’), suggesting aligned dynamics. For three example data sets (Golub et al., 2018; Hennig et al., 2018; Degenhart et al., 2020), we obtained higher correlation values, $ρ\in[0.17,0.23]$ (Figure 7B). The relative fitting dimension was much smaller than for the non-BCI data sets, especially for the two largest data sets, where $D_{fit,90}/D_{x,90}\in[0.03,0.06]$.

The higher correlation and much smaller relative fitting dimension suggest that, indeed, the neural dynamics arising in BCI experiments are more aligned, and those in non-BCI settings are more oblique. These trends also hold when decoding other behavioral outputs for the cycling task and the NLB tasks (position, acceleration, or EMG), even if the ability to decode and the numerical values for correlation and fitting dimension may fluctuate considerably (Appendix 1—figure 8). Thus, while we do not observe strongly different regimes as in the simulations, we do see an ordering between different data sets according to the alignment between outputs and neural dynamics. It would be interesting to test the differences between BCI and non-BCI data on larger data sets, and different experiments with different dimensions of neural data (Gao et al., 2017; Stringer et al., 2019a).

## Discussion

We analyzed the relationship between neural dynamics and behavior, asking to which extent a network’s output is represented in its dynamics. We identified two different limiting regimes: aligned dynamics, in which the dominant activity in a network is related to its output, and oblique dynamics, where the output is only a small modulation on top of the dominating dynamics. We demonstrated that these two regimes have different functional implications. We also examined how they arise through learning, and how they relate to experimental findings.

Linking neural activity to external variables is one of the core challenges of neuroscience (Hubel and Wiesel, 1962). In most cases, however, such links are far from perfect. The activity of single neurons can be related in a nonlinear, mixed manner, to task variables (Rigotti et al., 2013). Even when considering populations of neurons, a large fraction of neural activity is not easily accounted for by external variables (Arieli et al., 1996). Various explanations have been proposed for this disconnect. In the visual cortex, activity has been shown to be related to ‘irrelevant’ external variables, such as body movements (Stringer et al., 2019b). Follow-up work showed that, in primates, some of these effects can be explained by the induced changes on retinal images (Talluri et al., 2022), but this study still explained only half of the neural variability. An alternative explanation hinges on the redundancy of the neural code, which allows ‘null spaces’ in which activity can visit without affecting behavior (Rokni et al., 2007; Kaufman et al., 2014; Kao et al., 2021). Through the oblique regime, our study offers a simple explanation for this phenomenon: in the presence of large output weights, resistance to noise or perturbations requires large, potentially task-unrelated neural dynamics. Conversely, generating task-related output in the presence of large, task-unrelated dynamics requires large readout weights.

We showed theoretically and in simulations that, when training RNNs, the magnitude of output weights is a central parameter that controls which regime is reached. This finding is vital for the use of RNNs as hypothesis generators (Sussillo, 2014; Barak, 2017; Vyas et al., 2020), where it is often implicitly assumed that training results in universal solutions (Maheswaranathan et al., 2019) (even though biases in the distribution of solutions have been discussed; Sussillo et al., 2015). Here, we show that a specific control knob allows one to move between qualitatively different solutions of the same task, thereby expanding the control over the hypothesis space (Turner et al., 2021; Pagan et al., 2022). Note in particular that the default initialization in standard learning frameworks has large output weights, which results in oblique dynamics (or unstable solutions if training without noise, see Methods, section Analysis of solutions under noiseless conditions).

The role of the magnitude of output weights is also discussed in machine learning settings, where different learning regimes have been found (Jacot et al., 2018; Chizat et al., 2019; Mei et al., 2018; Jacot et al., 2022). In particular, ‘lazy’ solutions were observed for large output weights in feedforward networks. We show in Methods, section Analysis of solutions under noiseless conditions, that these are unstable for recurrent networks and are replaced in a second phase of learning by oblique solutions. This second, slower, phase is reminiscent of implicit regularization in overparameterized networks (Ratzon et al., 2024; Blanc et al., 2020; Li et al., 2021; Yang et al., 2023). On a broader scale, which learning regime is relevant when modeling biological learning is an open question that has only just begun to be explored (Flesch et al., 2022; Liu et al., 2023).

The particular control knob we studied has an analog in the biological circuit – the synaptic weights. We can thus use experimental data to study whether the brain might rely on oblique or aligned dynamics. Existing experimental work has partially addressed this question. In particular, the work by Russo et al., 2018, has been a major inspiration for our study. Our results share some of the key findings from that paper – the importance of stability leading to ‘untangled’ dynamics (Susman et al., 2021) and a dissociation between hidden dynamics and output. In addition, we suggest a specific mechanism to reach oblique dynamics – training networks with large output weights. Furthermore, we characterize the aligned and oblique regimes along experimentally accessible axes.

We see three avenues for exploring our results experimentally. First, simultaneous measurements of neural dynamics and muscle activity could be used to quantify noise along the output direction. This would allow checking whether noise is compressed in this direction, and in particular, whether such compression occurs on a slow time scale after initial task acquisition. We suggest how to test this in Figure 6C. Second, we show how the dynamical regimes dissociate under perturbations along specific directions. Experiments along these lines have recently become possible (Russell et al., 2022; Finkelstein et al., 2021; Chettih and Harvey, 2019). Future work is left to combine our model with biological constraints that induce additional effects during perturbations, e.g., through non-normal synaptic connectivity (O’Shea et al., 2022; Kim et al., 2023; Bondanelli and Ostojic, 2020; Logiaco et al., 2021). Third, our work connects to the setting of BCI, where the experimenter chooses the output weights at the beginning of learning (Sadtler et al., 2014; Golub et al., 2018; Willett et al., 2021; Rajeswaran et al., 2024). Typically, the output weights are set to lie ‘within the manifold’ of the leading PCs so that we expect aligned dynamics (Sadtler et al., 2014). In experiments where the output weights were rotated out of the manifold (without changing the norm), learning took longer and led to a rotation of the manifold, i.e., at least a partial alignment (Oby et al., 2019). Our theory suggests directly comparing the degree of alignment between dynamics obtained from within- and out-of-manifold initializations. Furthermore, it would be interesting to systematically change the norm of the output weights (in particular for out-of-manifold initializations) to see whether larger output weights lead to more oblique solutions. If this is the case, we suggest testing whether such more oblique solutions meet our predictions, e.g., higher variability between individuals and noise suppression.

Overall, our results provide an explanation for the plethora of relationships between neural activity and external variables. It will be interesting to see whether future studies will find hallmarks of either regime for different experiments, tasks, or brain regions.

## Methods

### Details on RNN models and training

We consider rate-based RNNs with $N$ neurons. The states $𝐱(t)\inℝ^{N}$ are governed by

$$
x˙=−x+Wϕ(x)+W_{in}s(t)+ξ(t),
$$

where $W$ is a recurrent weight matrix and $ϕ=tanh$ a nonlinearity applied element-wise. The network receives a low-dimensional input $𝐬(t)\inℝ^{N_{in}}$ via input weights $W_{in}$. It is also driven by white, isotropic noise with zero mean and covariance $𝔼[ξ_{i}(t)ξ_{j}(t^{′})]=2\sigma_{noise}^{2}\delta_{ij}\delta(t−t^{′})$. The initial states $𝐱(0)$ are drawn from a centered normal distribution with variance $\sigma_{init}^{2}$ at each trial. This serves as additional noise. The output is a low-dimensional, linear projection of the states: $𝐳(t)=W_{out}𝐱(t)$ with $W_{out}=[𝐰_{out,1},…,𝐰_{out,N_{out}}]^{T}$.

The initial output weights are drawn from centered normal distributions with variance $\sigma_{out}^{2}/N$. ‘Small’ output weights refer to $\sigma_{out}=1/\sqrt{N}$, and ‘large’ ones to $\sigma_{out}=1$. We have $‖𝐰_{out,i}‖=\sigma_{out}[1+O(1/\sqrt{N})]$ at initialization. Note that large initial output weights are the current default in standard learning environments (Paszke et al., 2017; Yang and Hu, 2020). The recurrent weights were initialized from centered normal distributions with variance $g^{2}/N$. We chose $g=1.5$ so that dynamics were chaotic before learning (Sompolinsky et al., 1988).

To simulate the noisy RNN dynamics numerically, we used the Euler-Maruyama method (Kloeden and Platen, 1992) with a time step of $Δt$. We used the Adam algorithm (Kingma and Ba, 2014) implemented in PyTorch (Paszke et al., 2017). Apart from the learning rate, we kept the parameters for Adam at the default (some filtering, no weight decay). We selected learning rates and the number of training steps such that learning was relatively smooth and converged sufficiently within the given number of trials. Learning rates were set to $η=η_{0}/N$. Details for all simulation parameters can be found in Table 1.

**Table 1.**
 Task, simulation, and network parameters for Figures 3—6.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Symbol</th>
      <th>Cycling</th>
      <th>Flip-flop</th>
      <th>Mante</th>
      <th>Romo</th>
      <th>Complex sine</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td># inputs</td>
      <td>Nin</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td># outputs</td>
      <td>Nout</td>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Trial duration</td>
      <td>T</td>
      <td>72</td>
      <td>25</td>
      <td>48</td>
      <td>29</td>
      <td>50</td>
    </tr>
    <tr>
      <td>Fixation duration</td>
      <td>tfix</td>
      <td>0</td>
      <td>U(0,1)</td>
      <td>3</td>
      <td>U(1.3)</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Stimulus duration</td>
      <td>tstim</td>
      <td>1</td>
      <td>1</td>
      <td>20</td>
      <td>1</td>
      <td>50</td>
    </tr>
    <tr>
      <td>Stimulus delay</td>
      <td>tsd</td>
      <td>–</td>
      <td>U(3,10)</td>
      <td>–</td>
      <td>U(2,12)</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Decision delay</td>
      <td>tdelay</td>
      <td>1</td>
      <td>2</td>
      <td>5</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Decision duration</td>
      <td>tdec</td>
      <td>71</td>
      <td>tsd</td>
      <td>20</td>
      <td>8</td>
      <td>50</td>
    </tr>
    <tr>
      <td>Simulation time step</td>
      <td>Δ⁢t</td>
      <td colspan="5">– 0.2 –</td>
    </tr>
    <tr>
      <td>Target time step</td>
      <td>Δ⁢ttarget</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>Activation noise</td>
      <td>2⁢σnoise</td>
      <td>0.2</td>
      <td>0.2</td>
      <td>0.05</td>
      <td>0.2</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>Initial state noise</td>
      <td>σinit</td>
      <td colspan="5">– 1.0 –</td>
    </tr>
    <tr>
      <td>Network size</td>
      <td>N</td>
      <td colspan="5">– 512 –</td>
    </tr>
    <tr>
      <td># training epochs</td>
      <td></td>
      <td>1000</td>
      <td>4000</td>
      <td>4000</td>
      <td>6000</td>
      <td>6000</td>
    </tr>
    <tr>
      <td>Learning rate aligned</td>
      <td>η0</td>
      <td>0.02</td>
      <td>0.005</td>
      <td>0.002</td>
      <td>0.005</td>
      <td>0.005</td>
    </tr>
    <tr>
      <td>Learning rate oblique</td>
      <td>η0</td>
      <td>0.02</td>
      <td>0.01</td>
      <td>0.02</td>
      <td>0.01</td>
      <td>0.005</td>
    </tr>
    <tr>
      <td>Batch size</td>
      <td></td>
      <td colspan="5">– 32 –</td>
    </tr>
  </tbody>
</table>

For the comparisons over different tasks (Figures 3—6), we trained five networks for each task. All weights ($W_{out},W,W_{in}$) were adapted. For the example networks trained on the cycling task (Figures 2, 5, and 6), we used networks with $N=256$ neurons and only changed the recurrent weights $W$. We also trained for longer (5000 training steps) and with a higher learning rate ($η=0.1/N$).

### Task details

The tasks the networks were trained on are taken from the neuroscience literature: a cycling task (Russo et al., 2018), a 3-bit flip-flop task, and a ‘complex sine’ task (with input-dependent frequencies) (Sussillo and Barak, 2013), a context-dependent decision-making task (‘Mante’) (Mante et al., 2013; Schuessler et al., 2020a), and a working memory task comparing the amplitudes of two pulse stimuli (‘Romo’) (Romo et al., 1999; Schuessler et al., 2020a). All tasks have similar structure (Schuessler et al., 2020b): A trial of length $T$ starts with a fixation period (length $t_{fix}$). This is followed by an input for $t_{stim}$. For the cycling and flip-flop task, the inputs are pulses of amplitude 1; else see below. After a delay $t_{delay}$, the output of the network is required to reach an input-dependent value during a time period $t_{dec}$. During this decision period, we set target points $t_{i}$ every $Δt_{target}$ time steps. The loss was defined as the mean squared error between network output and target at these time points. Below, we provide further details for each task.

#### Cycling task

The network receives an initial pulse, whose direction ($[1,0]^{T}$ or $[0,1]^{T}$) determines the sense of direction of the target. The target is given by a rotation in 2D, $𝐳^(t)=[sin⁡(a2\pift),cos⁡(2\pift)]^{T}$, with frequency $f=0.1$ and $a=\pm1$ for the two directions (clockwise or anticlockwise).

#### Flip-flop task

The network repeatedly receives input pulses along one of three directions, followed by decision periods. In each decision period, the output coordinate corresponding to the last input should reach ±1 depending on the sign of the input. All other coordinates should remain at ±1 as defined by the last time they were triggered. To make sure that this is well defined, we trigger all inputs at time steps $kΔt$ for $k\in[N_{in}]$ with random signs.

#### Mante task

Input channels for this task are split into two groups of size $N_{in}/2$: half of the channels for the signal and the other half for the context, indicating which of the signal channels is relevant. All signal channels $s_{i}(t)$ deliver a constant mean $s^_{i}$ plus additional white noise: $s_{i}(t)=s^_{i}+a_{noise}η_{i}(t)$. The mean is drawn uniformly from ${\pm1,\pm\frac{1}{2},\pm\frac{1}{4},\pm\frac{1}{8}}$, and the noise amplitude is $a_{noise}=0.05$. For simulations, we draw a standard normal variable $n_{i,k}∼N(0,1)$ at time step $k$, and set $η_{i,k}=n_{i,k}/\sqrt{Δt}$. Only a single contextual input is active at each trial, $s_{i+N_{in}/2}=\delta_{ij}$, with $j$ chosen uniformly from the number of context $N_{in}/2$. The target during the decision period is the sign of the relevant input, $z^(t)=sign(s^_{j})$.

#### Romo task

For the Romo task, the input consists of two input pulses separated by random delays $t_{sd}$. The amplitude of the inputs is drawn independently from $U(0.5,1.5)$ with the condition of being at least 0.2 apart (else both are redrawn). During the decision period, the network needs to yield $z^(t)=\pm1$, depending on which of the two pulses was larger.

#### Complex sine

The target is $z^(t)=sin⁡(2\pift)$, with frequency $f=(1−a)f_{min⁡}+af_{max⁡}$, and boundaries $f_{min⁡}=0.04,f_{max⁡}=0.2$, and where $a∼U(0,1)$. The input is a constant input of amplitude $s=a+0.25$.

### Generalized correlation

For Figure 3A, we used a generalized correlation measure which allows for multiple output dimensions, multiple time points, and noisy data. Consider neural activity of $N$ neurons at $P$ time points stacked into the matrix $X=[𝐱(1),…,𝐱(P)]\inℝ^{N\timesP}$. We assume the states to be centered in time, $\frac{1}{P}\sumt=1Px_{i}(t)=0$ for $i\in[N]$. The corresponding $D$-dimensional output is summarized in the $D\timesP$ matrix

$$
Z=W_{out}^{T}X,
$$

with weights $W_{out}\inℝ^{N\timesD}$. We define the generalized correlation as

$$
ρ=\frac{‖W_{out}^{T}X‖}{‖W_{out}‖‖X‖}.
$$

The norm is the Frobenius norm, $‖X‖=\sqrt{\sumijX_{ij}^{2}}$. In particular, we have

$$
‖Z‖=ρ‖W_{out}‖‖X‖.
$$

The case of 1D output and a single time step discussed in the main text, Equation 3, is recovered up to the sign, which we discard. Note that in that case, the vectors $𝐰_{out}$ and $𝐱(t)$ should be centered along coordinates to receive a valid correlation. Our numerical results did not change qualitatively when centering across coordinates only or both coordinates and time.

For trajectories with multiple conditions, we stack these instances in a matrix $X\inℝ^{N\timesN_{c}N_{t}}$, with $N_{c}$ the number of conditions, and $N_{t}$ the number of time points per trajectory. For noisy trajectories, we first average over multiple instances per condition and time point to obtain a similar matrix $X‾$.

### Regression

In Figure 3B and C we computed the number of PCs necessary to either represent the dynamics or fit the output. We simulated the trained networks again on their corresponding tasks. We did not apply noise during these simulations, since keeping the same noise as during training would reduce the quality of the output for large output weights; trial averaging yielded similar results to the ones obtained without noise (not shown).

The simulations yielded neural states $X\inℝ^{N\timesP}$ and outputs $Z\inℝ^{N_{out}}\timesP$, where $P$ is the number of data points (batch size times number of time points $T$). We applied PCA to the states $X$. The cumulative explained variance ratio obtained from PCA is plotted in Figure 3B. We then projected $X$ onto the first $k$ PCs and fitted these projections to the output with ridge regression (cross-validated, using scikit-learn’s RidgeCV Pedregosa et al., 2011).

### Dissimilarity measure

For measuring the dissimilarity between learners in Figure 4, we apply a measure following Williams et al., 2021. We define the distance between two sets with $P$ data points $X,Y\inℝ^{N\timesP}$ as

$$
d(X,Y)=argminQ\inOarccos⁡\frac{Tr(X^Y^^{T}Q)}{‖X^‖‖Y^‖},
$$

where the hat corresponds to centering along the rows, and $Q$ is an orthogonal matrix. The solution to this so-called orthogonal Procrustes’ problem is found via the singular value decomposition $X^Y^^{T}=UΣV^{T}$. The optimal transformation is $Q^{*}=VU^{T}$, and the numerator in Equation 8 is then $Tr(X^Y^^{T}Q^{*})=Tr(Σ)$.

Note that this is more restricted than canonical correlation analysis (CCA), which is also commonly used (Gallego et al., 2018; Gallego et al., 2020). In particular, CCA involves whitening the matrices $X$ and $Y$ before applying a rotation (Williams et al., 2021). This sets all singular values to 1. For originally low-D data, this mostly means amplifying the noise, unless the data was previously projected onto a small number of PCs. In the latter case, the procedure still removes the information about how much each PC contributes.

### Experimental data

We detail the analyses of neural data in section Different degrees of alignment in experimental settings. We made use of publicly available data sets: data from the cycling task of Russo et al., 2018, two data sets available through the NLB (Pei et al., 2021), and data from monkeys trained on a center-out reaching task with a BCI (Golub et al., 2018; Hennig et al., 2018; Degenhart et al., 2020). For all data sets, we first obtain firing rates $X\inℝ^{N\timesT}$, where $N$ is the number of measured neurons, and $T$ the number of data points, (see Figure 7B for these numbers). We also collect the simultaneously measured behavior in the matrix $Z\inℝ^{D\timesT}$. In Figure 7, we only analyzed cursor or hand velocity for behavior, so that the output dimension is $D=2$. See Appendix 1—figure 8 for similar results for hand position and acceleration or the largest two PCs of the EMG data recorded for the cycling task.

For the cycling task, the firing rates were binned in 1 ms bins and convolved with a 25 ms Gaussian filter. The mean firing rate was 22 and 18 Hz for the two monkeys, respectively. For the NLB data, spikes came in 1 ms bins. We binned data to 45 ms bins and applied a Gaussian filter with 45 ms width. This increased the quality of the fit, as firing rates were much lower (mean of 5 Hz for both) than in the cycling data set. For the BCI experiments, firing rates came as spike counts in 45 ms bins. The mean firing rate was (45, 45, 55) Hz for the data of Golub et al., 2018; Hennig et al., 2018; Degenhart et al., 2020, respectively. In agreement with the original BCI experiments, we did not apply a filter to the neural data.

For fitting, we centered both firing rates $X$ and output $Z$ across time (but not coordinates). We also added a delay of 100 ms between firing rates and output for the cycling and NLB data sets, which increased the quality of the fits. We then fitted the output $Z$ to the firing rates $X$ with ridge regression, with regularization obtained from cross-validation. We treated the coefficients as output weights $W_{out}$. The trial average data of the cycling tasks was very well fitted for both monkeys, $R^{2}=[0.97,0.98]$. For the NLB tasks with single-trial data, the fits were not as good, $R^{2}=[0.73,0.69]$. For two of the BCI data sets (Golub et al., 2018; Hennig et al., 2018), the output weights were also given, and we checked that the fit recovers these. For the third BCI data set (Degenhart et al., 2020), we did not have access to the output weights, and only access to the cursor velocity after Kalman filtering. Here, fitting yielded $R^{2}=0.83$.

For the fitting dimension $D_{fit,90}/D_{x,90}$ in Figure 7B, bottom, we used an adapted definition of $D_{fit,90}$: Because $R^{2}=90$% is not reached for all data sets, we asked for the number of PCs necessary to obtain 90% of the $R^{2}$ value obtained for the full data set.

We also considered whether the correlation $ρ$ scales with the number of neurons $N$. In our model, oblique and aligned dynamics can be defined in terms of such a scaling: aligned dynamics have highly correlated output weights and low-dimensional dynamics, so that $ρ∼N^{0}=1$, i.e., independent of the network size. For oblique dynamics, large output weights with norm $𝐰_{out}∼1$ lead to vanishing correlation, $ρ∼1/\sqrt{N}$. This is indeed similar to the relation between two random vectors, for which the correlation is precisely $1/\sqrt{N}$ (in the limit of large $N$). In Figure 8, we show the scaling of $R^{2}$ and $ρ$ with the number of subsampled neurons. For the cycling task and NLB data, the correlation scaled slightly weaker than $ρ∼N^{−1/2}$. For the BCI data, the scaling was closer to $ρ∼N^{−1/4}$ which is in between the aligned and oblique regimes of the model. These insights, however, are limited due to the trial averaging for the cycling task and the limited number of time points for the NLB tasks (not enough to reach $R^{2}=1$). Applying these measures to larger data sets could yield more definitive insights.

![Figure 8.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig8-v1.jpg)

**Figure 8.:** Scaling of the correlation $ρ$ with the number of neurons $N$ in experimental data. We fitted the output weights to subsets of $N$ neurons and computed the quality of fit (top) and the correlation between the resulting output weight and firing rates (bottom). To compare with random vectors, the correlation is scaled by $\sqrt{N}$. Dashed lines are $N^{p}/2$, for $p\in{1/2,1/4,0}$ for comparison. The aligned regime corresponds to $p=1/2$, and the oblique one to $p=0$.

### Analysis of solutions under noiseless conditions

In the sections below, we explore in detail under which conditions aligned and oblique solutions arise, and which other solutions arise if these conditions are not met.

We first consider small output weights and show that these lead to aligned solutions. Then, for large output weights, we show that without noise, two different, unstable solutions arise. Finally, we consider how adding noise affects learning dynamics. For a linear model, we can solve the dynamics of learning analytically and show how a negative feedback loop arises, that suppresses noise along the output direction. However, the linear model does not yield an oblique solution, so we also consider a nonlinear model for which we show in detail why oblique solutions arise.

We start by analyzing a simplified version of the network dynamics (Equation 4): autonomous dynamics without noise,

$$
x˙=−x+Wϕ(x),
$$

with fixed initial condition $𝐱(0)$. We assume a 1D output $z(t)$ and a target $z^(t_{i})$ defined on a finite set of time points $t_{i}$.

We illustrate the theory with an example of a simple sine wave task (Figure 9). We demand the network to autonomously produce a sine wave with fixed frequency $f=0.1$. At the beginning of the task, the network receives an input pulse that sets the starting point of the trajectory. We set the noise $\sigma_{init}$ on the initial state $𝐱(0)$ to zero. We define the target as 20 target points in the interval $t\in[1,21]$ (two cycles; purple dots in Figure 9).

![Figure 9.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig9-v1.jpg)

**Figure 9.:** All networks have $N=512$ neurons. Four regimes: (A) aligned for small output weights, (B) marginal for large output weights, small recurrent weights, (C) lazy for both large output and recurrent weights, (D) oblique for large output weights and noise added during training. Left: Output (dark), target (purple dots), and four states (light) of the network after training. Black bars indicate the scales for output and states (length = 1; same for all regimes). The output beyond the target interval $t\in[1,21]$ can be considered as extrapolation. The network in the oblique regime, (D), receives white noise during training, and the evaluation is shown with the same noise. Without noise, this network still produces a sine wave (not shown). Right: Projection of states on the first two principal components (PCs) and the orthogonal component $𝐰_{out,⟂}$ of the output vector. All axes have the same scale, which allows for comparison between the dynamics. Vectors show the (amplified) output weights, dotted lines the projection on the PCs (not visible for lazy and oblique). The insets for the marginal solution (B, left and right) show the dynamics magnified by $\sqrt{N}$.

#### Small weights lead to aligned solutions

For small output weights, $‖𝐰_{out}‖=1/\sqrt{N}$, gradient-based learning in such a noise-less system has been analyzed by Schuessler et al., 2020b. Learning changes the dynamics qualitatively through low-rank weight changes $ΔW$. These weight changes are spanned by existing directions such as the output weights. The resulting dynamics $𝐱(t)$ are thus aligned to the output weights. This means that the correlation between the two is large, independent of the network size, $ρ=O(1)$. The target of the task is also independent of $N$, so that after learning we have $z=O(1)$. Given the small output weights, we can thus infer the size of the states:

$$
z‖⏟O(1\sqrt{N})=ρ‖⏟O(1\sqrt{N})‖w_{out}‖⏟O(1/\sqrt{N})‖x‖⏟O(\sqrt{N}),
$$

so that $‖𝐱‖=O(\sqrt{N})$, or equivalently single neuron activations $x_{i}=O(1)$. This scaling corresponds to the aligned regime.

For the sine wave task, training with small output weights converges to an intuitive solution (Figure 9A). Neural activity evolves on a limit cycle, and the output is a sine wave that extrapolates beyond the training interval. Plotting activity and output weights along the largest two PCs and the remaining direction $𝐰_{out,⟂}$ confirms substantial correlation, $ρ=O(1)$, as expected. The solution was robust to adding noise after training (not shown). Changes in the initial dynamics or the presence of noise during training did not lead to qualitatively different solutions (Appendix 1—figure 10). A further look at the eigenvalue spectrum of the trained recurrent weights revealed a pair of complex conjugate outliers corresponding to the limit cycle (Mastrogiuseppe and Ostojic, 2018; Schuessler et al., 2020a), and a bulk of remaining eigenvalues concentrated on a disk with radius $g$, Appendix 1—figure 9.

#### Large weights, no noise: linearization of dynamics

We now consider learning with large output weights, $‖𝐰_{out}‖=1$, for noise-less dynamics, Equation 9. We start with the assumption that the activity changes for each neuron are small, $Δx_{i}(t)=O(1/\sqrt{N})$, or $‖Δ𝐱‖=O(1)$. Here, $Δ𝐱(t)=𝐱(t)−𝐱_{0}(t)$, where $𝐱_{0}(t)$ is the activity before learning. To perform a task, learning needs to induce output changes $Δz=O(1)$ to reach the target $z^(t)$. Note that a possible order-one initial output $z_{0}$ must also be compensated. Together with the output weight scale, we arrive at

$$
Δz‖⏟O(1)=ρ_{Δ}‖⏟O(1)‖w_{out}‖⏟O(1)‖Δx‖⏟O(1),
$$

where $ρ_{Δ}=corr(𝐰_{out},Δ𝐱)$. This shows that our assumption of small state changes $Δ𝐱$ is consistent – it allows for a solution – and that such small changes need to be strongly correlated to the output weights. Note that we make the distinction between the changes $Δ𝐱$ and the final activity $𝐱=𝐱_{0}+Δ𝐱$, because the latter may be dominated by $𝐱_{0}$. In the main text, we only consider the correlation between $𝐱$ and $𝐰_{out}$, because (as we show below) solutions with small $Δ𝐱$ are not robust, and the final $𝐱$ will be dominated by $Δ𝐱$.

For now, however, we ignore robustness and continue with the assumption of small $Δ𝐱$. Given this assumption, we linearize the dynamics around the initial trajectory $𝐱_{0}(t)$:

$$
\frac{dΔx}{dt}=ΔWϕ(x_{0})⏟a+[−I+(W_{0}+ΔW)R^{′}(x_{0})]Δx⏟b+O(Δx^{2}),
$$

with diagonal matrix $R^{′}(𝐱)_{ij}=\delta_{ij}ϕ^{′}(x_{i})$ and the weights changes $ΔW=W−W_{0}$ that induce $Δ𝐱$. Note that we haven’t yet constrained the weight changes $ΔW$ so we cannot discard the terms of the kind $ΔWΔ𝐱$. The next steps depend on the initial trajectories $𝐱_{0}(t)$.

#### Initially decaying dynamics lead to a marginal regime

We first consider networks with decaying dynamics before learning. This is obtained by drawing the initial recurrent weights independently from $W_{ij}∼N(0,\frac{g^{2}}{N})$, with $g<1$ (Sompolinsky et al., 1988). With such dynamics, $𝐱_{0}(t)$ vanishes exponentially in time. In Equation 12, we disregard the term $𝐚$ and have $R^{′}=I$, so that

$$
\frac{dΔx}{dt}=(−I+W_{0}+ΔW)Δx+O(Δx^{2}).
$$

To have self-sustained dynamics, the matrix $W_{0}+ΔW$ must have a leading eigenvalue $\lambda_{+}$ with real part above the stability line: $ℜ\lambda_{+}=1+ϵ$.

The distance $ϵ>0$ must be small, else the states would become large. To understand how $ϵ$ needs to scale with $N$, we turn to a simple model studied before (Mastrogiuseppe and Ostojic, 2018; Schuessler et al., 2020a): an autonomously generated fixed point and rank-one connectivity $W=\frac{1}{N}\lambda_{+}𝐮𝐮^{T}$. The vector $𝐮$ has entries $u_{i}∼N(0,1)$. A fixed point of the dynamics (Equation 9) fulfills $𝐱=\frac{1}{N}\lambda_{+}𝐮𝐮^{T}ϕ(𝐱)$. Projecting on $𝐮$ and applying partial integration in the limit $N→∞$, we obtain

$$
\lambda_{+}=\frac{1}{⟨ϕ^{′}⟩},
$$

where $⟨ϕ^{′}⟩=\intDuϕ^{′}(\sigma_{x}u)$, with standard normal measure $Du=du\frac{1}{\sqrt{2\pi}}e^{−u^{2}/2}$. Here, $\sigma_{x}$ is the scale of the states, $\sigma_{x}=‖𝐱‖/\sqrt{N}$ or $x_{i}=O(\sigma_{x})$. The fixed point is situated along the vector $𝐮$. To have the smallest possible fixed point generate some output, we set the output weights to $𝐰_{out}=\frac{1}{\sqrt{N}}𝐮$. Then, we have correlation $ρ=1$ and $z=𝐰_{out}^{T}𝐱=ρ‖𝐰_{out}‖‖𝐱‖=1⋅1⋅\sqrt{N}\sigma_{x}$. In other words, a small fixed point with $\sigma_{x}∼\frac{1}{\sqrt{N}}$. We expand $ϕ^{′}$ in Equation 14 around zero. For even $ϕ$, we have $ϕ^{′′}(0)=0$ and

$$
\lambda_{+}=\frac{1}{1+\frac{1}{2}ϕ^{‴}(0)\sigma_{x}^{2}}=1−\frac{1}{2}ϕ^{‴}(0)\sigma_{x}^{2}.
$$

Sigmoidal functions have $ϕ^{′′′}<0$, e.g., $ϕ^{′′′}(0)=−2$ for $ϕ=tanh$. Hence $\lambda=1+ϵ$, with $ϵ=\sigma_{x}^{2}∼\frac{1}{N}$. Remarkably, the perturbation leading to states with $\sigma_{x}=O(1/\sqrt{N})$ only needs to have a distance $ϵ=O(1/N)$ away from the stability line.

The insights from this simplified setting extend to the example of the sine wave task (Figure 9B). The model with large output weights, $g=0.7$, and no noise yields a limit cycle. The output extrapolates in time, but the states are very small, scaling as $x_{i}=O(1/\sqrt{N})$ (analysis over different $N$ not shown). Such a solution is only marginally stable – adding a white noise with $\sigma_{noise}=0.2$ after training destroyed the rotation (not shown). The eigenvalues were again split into two outliers and a bulk (Appendix 1—figure 9). However, the two outliers now had a real part $1+ϵ$, i.e., they were very close to the stability line of the fixed point at zero. To better illustrate the marginal solution, we also set the initial state $𝐱(t=0)$ to small values, $x_{i}(t=0)∼N(0,1/N)$. For $x_{i}(t=0)∼N(0,1)$, there would be an initial decay much larger than the limit cycle.

#### Initially chaotic dynamics lead to a lazy regime

In contrast to the situation before, initially chaotic dynamics (for $g>1$) imply order-one initial states, $(x_{0}(t))_{i}=O(1)$ for all trial times $t$. The driving term $𝐚$ in Equation 12 can thus not be ignored and we expect it to be on the same scale as $Δ𝐱$:

$$
1∼‖Δx‖∼‖ΔWϕ(x_{0})‖.
$$

The smallest possible weight changes $ΔW$ will be those for which $ϕ(𝐱_{0})$ yields a maximal response, but other vectors do not yield a strong response. This is captured by the operator norm, $‖ΔW‖_{2}=max⁡{‖ΔW𝐱‖:𝐱\inℝ^{N} with ‖𝐱‖=1}$. We can then write $‖ΔWϕ(𝐱_{0})‖∼‖ΔW‖_{2}‖𝐱_{0}‖$, and hence $‖ΔW‖_{2}∼\frac{1}{\sqrt{N}}$. The operator norm also bounds the eigenvalues $ΔW$ and hence the effect of the matrix on the dynamics of the system. For large $N$, this implies that the changes $ΔW$ are too small to change the dynamics qualitatively, and the latter remain chaotic. Note that because the network dynamics are chaotic, the term $𝐛$ in Equation 12 diverges, so that our discussion is only valid for short times. Numerically, we find small weight changes and chaotic solutions even for large target times $t_{i}$ (not shown).

For the sine wave task, the network with initially chaotic dynamics indeed converges to such a solution (Figure 9C). The output does not extrapolate beyond the training interval $t\in[1,21]$, and dynamics remain qualitatively similar to those before training. During the training interval, the dynamics also remain close to the initial trajectories (dashed line). Testing the response to small perturbations in $𝐱(0)$ indicated that the dynamics remain chaotic (not shown). No limit cycle was formed, and the spectrum of eigenvalues did not show outliers (Appendix 1—figure 9).

We called this regime ‘lazy’, following similar settings in feedforward networks (Jacot et al., 2018; Chizat et al., 2019). Note that there, the output $z(t)$ is linearized around the weights at initialization (as opposed to the dynamics, Equation 9). This can be done in our case as well:

$$
z(t)=z_{0}(t)+\sumijw_{out}^{T}\frac{dx(t)}{dW_{ij}}|_{W_{0}}ΔW_{ij}+O(ΔW^{2}).
$$

Demanding $z^(t)=z(t)$ yields a linear equation for each time point $t$. As we have $N^{2}$ parameters, this system is typically underconstrained. Gradient descent for this linear system leads to the minimal norm solution, which can also be found directly using the Moore-Penrose pseudo-inverse. Numerically, we found that the weights $ΔW_{lin}$ obtained by this linearization are very close to those found by gradient descent (GD) on the nonlinear system, $ΔW_{GD}$, with Frobenius norm $‖ΔW_{GD}−ΔW_{lin}‖∼\frac{1}{N}$ (section Linear approximation for lazy learning).

#### Marginal and lazy solutions disappear with noise during training

The deduction above hinges on the assumption that $Δ𝐱$ is small. This assumption does not hold if dynamics are noisy, Equation 4. For marginal dynamics, the noise would push solutions to different attractors or different positions along the limit cycle. For lazy dynamics, the chaotic dynamics would amplify any perturbations along the trajectory (if chaos persists under noise; Schuecker et al., 2018).

We will explore how learning is affected by noise in the sections below. Here, we only show that adding noise for our example task abolishes the marginal or lazy solutions and leads to oblique ones (Figure 9D). We added white noise with amplitude $\sigma_{noise}=1/\sqrt{2}$ to the dynamics during learning. After training, the output was a noisy sine wave. States were order one, and the 3D projection showed dynamics along a limit cycle that was almost orthogonal to the output vector. The noise in the 2D subspace of the first two PCs was small, $O(\frac{1}{\sqrt{N}})$, and thus did not disrupt the dynamics (e.g. very little phase shift). The eigenvalue spectrum had two outliers whose real part was increased in comparison to those in the aligned regime (Appendix 1—figure 9). Note that for the chosen values $g=1.5$ and $\sigma_{noise}=1/\sqrt{2}$, the network actually was not chaotic at initialization (Schuecker et al., 2018). However, the choice of $g$ does not influence the solution in the oblique regime qualitatively, so both marginal and lazy solutions cease to exist g.

### Learning with noise for linear RNNs

In the next two sections, we aim to understand how adding noise affects dynamics and training. We start with a simple setting of a linear RNN which allows us to track the learning dynamics analytically. Despite its simplicity, this setting already captures a range of observations: different time scales for learning the bias and variance part, and the rise of a negative feedback loop for noise suppression. Oblique dynamics, however, do not arise, showing that these need autonomously generated, nonlinear dynamics, covered in section Oblique solutions arise for noisy, nonlinear systems.

We consider a linear network driven by a constant input and additional white noise. The dynamics read

$$
x˙=(−I+W)x+w_{in}+ξ,
$$

with noise $𝝃$ as in Equation 4. We focus on a simplified task, which is to produce a constant nonzero output $z^$ once the average dynamics converged, i.e., for large trial times. The output is $z=𝐰_{out}^{T}𝐱=z‾+\deltaz$, where the bar denotes average over the noise, and the delta fluctuations around the average. The average is given by $z‾=𝐰_{out}^{T}(I−W)^{−1}𝐰_{in}$. We train the network by changing only the recurrent weights $W$ via gradient descent. For small output weights, the fluctuations are too small to affect training: $\deltaz=O(1/\sqrt{N})$. Apart from a small correction, learning dynamics are then the same as for small output weights and no noise, a setting analyzed in Schuessler et al., 2020b. Here, we only consider the case of large output weights.

The loss separates into two parts, $L=L_{bias}+L_{var}$ with $L_{bias}=(z‾−z^)^{2}$ and $L_{var}=\deltaz^{2}=var(\deltaz)$. Learning aims to minimize the sum. We first consider learning based on each part alone and then join both to describe the full learning dynamics.

Learning based on the bias part alone converges to a lazy solution (see section Details linear model: Bias only: lazy learning). For no initial weights, $W_{0}=0$, we have to leading order

$$
ΔW(\tau)=\frac{b_{1}(\tau)}{\sqrt{N}}w^_{out}w^_{in,⊥}^{T},
$$

with

$$
b_{1}(\tau)=(1−e^{−2Nη\tau})(z^−\sqrt{N}ρ_{io}).
$$

Thus, $ΔW$ is rank one with norm $‖ΔW‖_{2}∼\frac{1}{\sqrt{N}}$. Furthermore, for a learning rate $η$, it converges in $O(\frac{1}{ηN})$ time steps. We will see that this is very fast compared to learning the variance part.

#### Learning to reduce noise alone slowly produces a negative feedback loop

Next, we consider learning based on the variance part $L_{var}$ alone, i.e., to reduce fluctuations in the output while ignoring the mean. The network dynamics are linear, so that $\delta𝐱$ is an Ornstein-Uhlenbeck process. Its stationary variance $Σ$ is the solution to the Lyapunov equation

$$
0=AΣ+ΣA^{T}+2\sigma_{noise}^{2}I,
$$

where $A=−I+W$. The variance part of the loss is then

$$
L_{var}=w_{out}^{T}Σw_{out}.
$$

One can state the gradient of this loss in terms of a second Lyapunov equation (Yan et al., 2016):

$$
G_{var}=\frac{dL_{var}}{dW}=2ΩΣ,
$$

where Ω is the solution to

$$
0=AΩ+ΩA^{T}+w_{out}w_{out}^{T}.
$$

Generally, solving both Lyapunov equations analytically is not possible, and even results for random matrices are still sparse (e.g. for symmetric Wigner matrices $W$ Preciado and Rahimian, 2016). To gain intuition, we thus restrict ourselves to the case of no initial connectivity, which leads to the connectivity spanned by input and output weights only. We start with the simplest case of a rank-one matrix only spanned by the output weights, $W=\lambda_{−}𝐰_{out}𝐰_{out}^{T}$, and extend to rank two in the following section. The Lyapunov equations then become 1D, and we obtain

$$
Σ=\sigma_{noise}^{2}(I+\frac{\lambda_{−}}{1−\lambda_{−}}w_{out}w_{out}^{T}),
$$



$$
Ω=\frac{1}{2(1−\lambda_{−})}w_{out}w_{out}^{T}.
$$

The gradient $G_{var}=2ΩΣ$ is therefore in the same subspace as $W$, and we can evaluate the 1D dynamics

$$
\frac{d\lambda_{−}(\tau)}{d\tau}=\frac{−η\sigma_{noise}^{2}}{[1−\lambda_{−}(\tau)]^{2}},
$$

where $\tau$ is the number of update steps. We assume $\tau$ to be continuous, i.e., we assume a sufficiently small learning rate and approximate the discrete dynamics of gradient descent with gradient flow. With initial condition $\lambda_{−}(0)=0$, the solution is

$$
\lambda_{−}(\tau)=1−(3η\sigma_{noise}^{2}\tau+1)^{\frac{1}{3}},
$$

which is negative for $\tau>0$. The loss then decays as

$$
L_{var}=\sigma_{noise}^{2}(3η\sigma_{noise}^{2}\tau+1)^{−\frac{1}{3}},
$$

namely at order $O(\tau^{−1/3})$ in learning time. We thus obtained that, during the variance phase of learning, connectivity develops a negative feedback look aligned with the output weights, which serves to suppress output noise. For very long learning times, $\tau∼N^{3}/η$, learning can in principle reduce the output fluctuations to $\frac{1}{\sqrt{N}}$. Note, however, that this implies a huge negative feedback loop, $\lambda_{−}=O(N)$, which potentially leads to instability in a system with delays or discretized dynamics (Kadmon et al., 2020).

#### Optimizing mean and fluctuations occurs on different time scales

We now consider learning both the mean and the variance part. For zero initial recurrent weights, $W_{0}=0$, the input and output vectors make up the only relevant directions in space. We thus express the recurrent weights as a rank-two matrix, $W=U^MU^^{T}$, with orthonormal basis $U^=[𝐰^_{out},𝐰^_{in,⟂}]$. The hats indicate normalized vectors. For large networks and large output weights, the first vector is already normalized, $𝐰^_{out}=𝐰_{out}$. The second vector is the input weights after Gram-Schmidt. Assuming that $𝐰_{out}$ and $𝐰_{in}$ are drawn independently, we have a small, random correlation $ρ_{io}=O(1/\sqrt{N})$, and can write $𝐰^_{in,⟂}=𝐰^_{in}−𝐰_{out}ρ_{io}+O(\frac{1}{N}).$

We computed the learning dynamics in terms of the coefficient matrix $M$, using the same tools introduced above, and the insight that learning the mean is much faster than learning to reduce the variance. The details are relegated to section Details linear model: Bias and variance combined, here, we summarize the results. We obtained

$$
M(\tau)=[\lambda_{−}(\tau)\frac{b(\tau)}{\sqrt{N}}00].
$$

Before discussing the temporal evolution of the two components, we analyze the structure of the matrix. The eigenvalue $M_{11}=\lambda_{−}$ is a negative feedback loop along the eigenvector $𝐰_{out}$, and $M_{21}=b/\sqrt{N}$ is a small feedforward component $b$ which maps the input to the output. Along the input direction $𝐰^_{in}$, learning does not change the dynamics: The second eigenvalue, corresponding to this direction, is zero.

The dynamics unfold on two time scales. First, there is a very fast learning of the bias via the feedforward coefficient

$$
b(\tau)=(1−e^{−2Nη\tau})(z^−\sqrt{N}ρ_{io}).
$$

During this phase, the eigenvalue $M_{11}=\lambda_{−}$ remains at zero, so that overall weight changes remain small, $‖W‖∼1/\sqrt{N}$. The average fixed point also does not change much, $‖Δ𝐱‾(\tau)‖=b_{1}(\tau)=O(1),$ in comparison to the fixed point before learning, $‖𝐱‾_{0}‖=‖𝐰_{in}‖=\sqrt{N}.$ The loss evolves as

$$
L_{bias}=e^{−4Nη\tau}(z^−\sqrt{N}ρ_{io})^{2}.
$$

The variance part of the loss does not change during this phase.

In a second, slower learning phase, the eigenvalue $\lambda_{−}$ evolves like above, Equation 28, the case where only the variance part is learned. The second coefficient compensates for the resulting change in the output. This compensation happens at a much faster time scale ($N^{3}$ times faster than $\lambda_{−}$), so we consider its steady state:

$$
b(\tau)=z^[1−\lambda_{−}(\tau)]−\sqrt{N}ρ_{io}.
$$

Because of this compensation, the bias part of the loss always remains at zero, and the full loss $L(\tau)=L_{var}(\tau)$ evolves as before, Equation 29. Meanwhile, the average fixed point does not change anymore; we have $‖Δ𝐱‾‖=z^−ρ_{io}\sqrt{N}$.

We compare our theoretical predictions against numerical simulations in Figure 10. For the task, we let the linear network dynamics converge from $𝐱(0)=𝟎$ until $t=15$, and demand the output $z(t)$ to be at the target $z^$ during the interval $t\in[15,20]$. Because the first learning phase converges $N$ times faster than the second one (with $N=256$), using a single learning rate $η$ is problematic. One can either observe the first phase only (for small $η$) or risk unstable learning during the first phase (for large $η$). We thus split learning into two parts with adapted learning rates. For the initial phase, we set a learning rate to $η=η_{0}/N$, with $η_{0}=0.002$ (Figure 10, left column). For the second phase, we set $η=η_{0}$ (Figure 10, right column). Theory and simulation agree well for both phases. Small deviations can be observed for the second phase and long learning times: nonzero coefficients $M_{21}$ and $M_{22}$ and a corresponding increase in the norm $‖Δ𝐱‾‖$. Testing with larger network sizes showed that these errors decreased as $O(1/N)$, which is consistent with our theory above (not shown).

![Figure 10.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig10-v1.jpg)

**Figure 10.:** Learning separates into fast learning of the bias part of the loss (left), and slow learning reducing the variance part (right). Learning rates are $η=η_{0}/N$ and $η=η_{0}$, respectively, with $η_{0}=0.002$ and network size $N=256$. Learning epochs in the first phase are counted from –1000, so that the second phase starts at 0. In the right column, the initial learning phase with learning time steps multiplied by $1/N$ is shown for comparison. In all plots, simulations (full lines) are compared with theory (dashed lines). (A) Loss $L=L_{bias}+L_{var}$. The two components are obtained by averaging over a batch with 32 examples at each learning step. The full loss is not plotted in the slow phase, because it is indistinguishable from $L_{var}$. (B) Coefficients of the 2-by-2 coupling matrix $M$. $M_{11}=\lambda_{−}$ is the feedback loop along the output weights, $M_{12}=b/\sqrt{N}$ a feedforward coupling from input to output. The theory predicts $M_{21}∼M_{22}∼O(1/N)$. (C) Norm of state changes during training. The theory predicts that it remains constant during the second phase and small compared to $‖𝐱‾_{0}‖=\sqrt{N}$. Other parameters: target $z^=1$, $\sigma_{noise}=1$, overlap between input and output vectors $ρ_{io}=−0.5/\sqrt{N}$.

Our results show that learning in this linear system is a hybrid between oblique and aligned during the second phase. We have a large term that compresses the output noise, but a very small, ‘lazy’ correction in the feedforward component that corrects the output, and the states are only marginally changed. Although this system is a somewhat degenerate limiting case, we can still derive important insights. The two most striking features – the different time scales of the two learning processes, and the slow emergence of negative feedback, $\lambda_{−}(\tau)∼−\tau^{1/3}$, along the output – are found robustly also for nonlinear networks and other tasks.

### Oblique solutions arise for noisy, nonlinear systems

We now examine the origin of oblique solutions. The linear system did not yield oblique solutions, so we turn to a nonlinear model. We consider a 1D flip-flop task, where the network has to yield a constant, nonzero output $z^$ depending on the sign of the last input pulse. We further simplify the analysis by only considering the steady state of a network, not how the input pulse mediates the transition. At the output, we thus only consider the average $z‾$ and the fluctuations $\deltaz$. As for the linear network, the loss splits into a bias part $L_{bias}=(z‾−z^)^{2}$ and variance part $L_{var}=\deltaz^{2}$. As before, we assume that learning only acts on a low-dimensional parameter matrix $M$.

Because following the learning dynamics in nonlinear networks is difficult, we take a different approach. We develop a mean field theory to show how noise affects the dynamics of a nonlinear network with autonomous fixed points. This allows us to compute the loss components $L_{bias}$ and $L_{var}$ in terms of $M$. We then show that the minimum of the loss function corresponds to oblique solutions. This leads to a clear interpretation of the mechanisms pushing for oblique solutions. Finally, we show that the theory quantitatively predicts the outcome of learning with gradient descent.

#### Rank-two connectivity model with fixed point

We first introduce the connectivity model and compute the latent dynamics using mean field theory. We constrain the recurrent connectivity to a rank-two model of the form $W=\frac{1}{N}UMU^{T}$, where $M$ is a 2×2 coefficient matrix to be learned. The randomly drawn projection matrix $U\inℝ^{N\times2}$ has entries $U_{ia}$ drawn independently from a standard normal distribution. This implies orthogonality to leading order, $\frac{1}{N}U^{T}U=I_{2}+O(1/\sqrt{N})$. We will discard the correction term, as it does not change our results apart from a constant bias. We further assume that the input and output vectors are spanned by $U$, although not necessarily identified with the components of $U$ as in the previous section. Note also that for clarity we do not normalize $U$ as $U^$ before. The assumption of Gaussian connectivity greatly simplifies the math, while its restrictions are irrelevant to the task considered here (Schuessler et al., 2020a; Beiran et al., 2021; Dubreuil et al., 2021).

To understand the dynamics Equation 4 analytically, we make use of the low-rank connectivity. Following previous work (Rivkind and Barak, 2017; Kadmon et al., 2020), we split the dynamics into two parts: a parallel part $𝐱_{∥}$ in the subspace spanned by $U$, and an orthogonal part $𝐱_{⟂}$. This yields

$$
x˙_{∥}=−x_{∥}+\frac{1}{N}UMU^{T}ϕ(x_{∥}+x_{⊥})+\frac{1}{N}UU^{T}ξ,
$$



$$
x˙_{⊥}=−x_{⊥}+(I−\frac{1}{N}UU^{T})ξ.
$$

Notice that the parallel part is partially driven by the orthogonal one, but not vice versa. The parallel part can be expressed in terms of the latent variable

$$
κ=\frac{1}{N}U^{T}x=\frac{1}{N}U^{T}x_{∥}.
$$

The scaling here ensures that $𝜿$ is order one if $𝐱_{∥}$ has order-one states. Because the readout is assumed to be spanned by $U$, the output is fully determined by the parallel part. We can write

$$
z=w_{out}^{T}x_{∥}=\sqrt{N}v_{out}^{T}κ,
$$

with projected output weights $𝐯_{out}=\frac{1}{\sqrt{N}}U^{T}𝐰_{out}$. Note that we assume large output weights, $‖𝐰_{out}‖=1$, so that $𝐯_{out}$ is also normalized.

We split the latent state into its average over the noise $𝝃$ and fluctuations, $𝜿=𝜿‾+\delta𝜿$. Similarly, the output splits into $z=z‾+\deltaz.$ The loss then has two components, $L=L_{bias}+L_{var}$, with

$$
L_{bias}=(z¯−z^)^{2}=(\sqrt{N}v_{out}^{T}κ¯−z^)^{2},
$$



$$
L_{var}=\deltaz^{2}¯=Nv_{out}^{T}\deltaκ\deltaκ^{T}¯v_{out}.
$$

We want to understand situations with small loss. For the bias term, the average $𝜿‾$ must be either small or oblique to the readout weights. For the variance term, the covariance of the fluctuations, $cov(\delta𝜿)=\delta𝜿\delta𝜿^{T}$, must be compressed along the output direction: Even though the covariance is $O(1/N)$, it still projects to the output at $O(1)$, as reflected by the factor $N$ in Equation 39. Figure 11 illustrates the situation in a cartoon from this high-level perspective.

![Figure 11.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig11-v1.jpg)

**Figure 11.:** The two-dimensional subspace spanned by $U$ illustrates the main directions under consideration: the principal components (PCs) of the average trajectories (here only a fixed point $𝐱‾=U𝜿‾$), and the direction of output weights $𝐰_{out}=\frac{1}{\sqrt{N}}U𝐯_{out}$. Left: During learning, a fast process keeps the average output close to the target so that $L_{bias}=0$. Center: The variance component, $L_{var}$, is determined by the projection of the fluctuations $\delta𝜿$ onto the output vector. Note that the noise in the low-D subspace is very small, $\delta𝜿=O(1\sqrt{N})$, but the output is still affected due to the large output weights. Right: During training, the noise becomes non-isotropic. Along the average direction $𝜿‾$, the fluctuations are increased as a byproduct of the positive feedback $\lambda_{+}$. Meanwhile, a slow learning process suppresses the output variance via a negative feedback $\lambda_{−}$.

To understand the underlying mechanisms in detail, we next explore how the relevant variables $𝜿‾$ and $\delta𝜿$ are determined by the coupling matrix $M$. We do so by applying mean field theory, following previous works (Mastrogiuseppe and Ostojic, 2018; Schuessler et al., 2020a; Kadmon et al., 2020; Schuecker et al., 2018). Detailed derivations can be found in the section Details nonlinear autonomous system with noise. Here, we present the high-level results. The average dynamics converge to a fixed point determined by the equation for the latent variable,

$$
κ¯=⟨ϕ^{′}⟩Mκ¯+O(\frac{1}{\sqrt{N}}).
$$

The $O(1/\sqrt{N})$ term is a constant offset for any given network that we ignore without loss of generality. The average slope is

$$
⟨ϕ^{′}⟩=⟨ϕ^{′}(\sigma_{x}¯u)⟩=\intDuϕ^{′}(\sigma_{x}¯u),
$$

with variance

$$
\sigma_{x}^{2}¯=‖κ¯‖^{2}+\sigma_{⊥}^{2}¯.
$$

(We have $\sigma_{x}=\sqrt{\sigma_{x}^{2}}$ because the fluctuations are small.) The orthogonal variance is simply the variance of the noise, $\sigma_{⊥}^{2}¯=\sigma_{noise}^{2}$. The fixed point (Equation 40) implies that for a nonzero fixed point, the matrix $M$ must have an eigenvalue

$$
\lambda_{+}=\frac{1}{⟨ϕ^{′}⟩}.
$$

This is very similar to the noiseless situation discussed briefly above, Equation 14. However, here the additional variance $\sigma_{⟂}^{2}$ decreases the average slope due to saturation of the nonlinearity. This in turn increases the minimal eigenvalue for a nonzero fixed point, which can be found by setting $𝜿‾=𝟎$, and hence $\sigma_{x}=\sigma_{⟂}$:

$$
\lambda_{+,min}=\frac{1}{⟨ϕ^{′}(\sigma_{⊥}¯u)⟩}.
$$

In other words, the noise decreases the effective gain $⟨ϕ^{′}⟩$, and thus the connectivity eigenvalue $\lambda_{+}$ needs to compensate. From the point of view of the spectrum, we are thus pushed away from the margin $1+ϵ$. These considerations, however, do not exclude the possibility that dynamics converge to an average fixed point that is small and correlated, which is at odds with oblique dynamics. To understand why learning leads to oblique dynamics, we need to move beyond the average $𝜿‾$ and take into account the fluctuations $\delta𝜿$.

#### Fluctuations of the latent variable

The fluctuations $\delta𝜿$ around a fixed point $𝜿‾$ are driven by the noise, both directly and indirectly via the dynamics. The direct contribution is a white noise term of order $1/\sqrt{N}$ because $𝝃$ is isotropic and independent of $U$. A detailed analysis (section Details nonlinear autonomous system with noise) shows that the indirect contribution is given by a colored noise term which originates from the finite size fluctuations in the variance of the orthogonal part. This second term is also $O(1/\sqrt{N})$, which implies that the fluctuations are small, $\delta𝜿=O(1/\sqrt{N})$. We can thus linearize their dynamics around the mean $𝜿‾$, which yields

$$
\frac{d\deltaκ(t)}{dt}=A\deltaκ(t)+\frac{1}{\sqrt{N}}ζ(t),
$$

where the order-one term $𝜻$ contains both the white and the colored noise term. The Jacobian $A$ depends on $M$ and $𝜿‾$:

$$
A=−I+⟨ϕ^{′}⟩M+\frac{⟨ϕ^{‴}⟩}{⟨ϕ^{′}⟩}κ¯κ¯^{T}.
$$

The averages are again evaluated at the joint variance $\sigma_{x}^{2}=‖𝜿‾‖^{2}+\sigma_{⟂}^{2}$. Apart from the increased variance, the stability analysis yields the same results as in the noise-free case (Schuessler et al., 2020a): The Jacobian has the eigenvalues $\gamma_{+}=\frac{⟨ϕ^{′′′}⟩}{⟨ϕ^{′}⟩}‖𝜿‾‖^{2}$ and $\gamma_{−}=\frac{\lambda_{−}}{\lambda_{+}}−1$. The average over the third derivative $⟨ϕ^{′′′}⟩$ is negative, so that $\gamma_{+}<0$. We assume that the second eigenvalue is smaller than the first, $\lambda_{−}<\lambda_{+}$, so that $\gamma_{−}<0$. The fixed point under consideration is hence stable.

Next, we compute the covariance of the fluctuations at steady state, see section Details nonlinear autonomous system with noise. The outcome is

$$
\deltaκ\deltaκ^{T}¯=\frac{1}{N}[\sigma_{noise}^{2}Σ_{A}+\frac{\sigma_{noise}^{4}}{‖κ¯‖^{2}}\frac{−\gamma_{+}}{2(2−\gamma_{+})}v_{+}v_{+}^{T}],
$$

where $𝐯_{+}=𝜿‾/‖𝜿‾‖$ is the normalized eigenvector of $M$ corresponding to eigenvalue $\lambda_{+}$. The 2×2 matrix $Σ_{A}$ is the covariance introduced by the white noise part alone and obeys the Lyapunov equation

$$
0=AΣ_{A}+Σ_{A}A^{T}+2I_{2}.
$$

The second term in Equation 47 stems from the colored noise component of $𝜻$.

The loss (Equation 39) is obtained by projecting the covariance on the output weights. Importantly, the factor $1/N$ in the covariance is compensated by the factor $N$ in the loss. Hence, even if the covariance shrinks with increasing network size, the output is still affected at order one. We next explore the implications of minimizing this loss.

#### Minimizing the loss by balancing saturation and negative feedback loop

To gain an understanding of how the output fluctuations responsible for $L_{bias}$ can be reduced, we first consider the case of a symmetric coefficient matrix $M$. Simulations of networks trained with gradient descent below show that this approximation is reasonable. For symmetric $M$, the orthogonal eigenvectors $𝐯_{\pm}$ with eigenvalues $\lambda_{\pm}$ of the recurrent weights $M$ are also eigenvectors of $A$, in that case corresponding to the eigenvalues $\gamma_{\pm}$. This allows to diagonalize the Lyapunov Equation 48 and yields the solution

$$
Σ_{A}=\frac{v_{+}v_{+}^{T}}{−\gamma_{+}}+\frac{v_{−}v_{−}^{T}}{−\gamma_{−}}.
$$

For the loss (Equation 39), we further need the relation between the eigenvectors $𝐯_{\pm}$ and the output weights. Because the fixed point $𝜿‾$ is parallel to the eigenvector, we have $𝐯_{out}^{T}𝐯_{+}=ρ$. For the other eigenvector, orthogonality yields $𝐯_{out}^{T}𝐯_{−}=\sqrt{1−ρ^{2}}$. Inserting this into Equations 39 and 47 yields an expression in terms of the Jacobian eigenvalues $\gamma_{\pm}$, the correlation $ρ$, and the norm of the fixed point $‖𝜿‾‖$:

$$
L_{var}=ρ^{2}[\frac{\sigma_{noise}^{2}}{−\gamma_{+}}+\frac{\sigma_{noise}^{4}}{‖κ¯‖^{2}}\frac{\gamma_{+}}{2(\gamma_{+}−2)}]+(1−ρ^{2})\frac{\sigma_{noise}^{2}}{−\gamma_{−}}.
$$

For more explicit insight, we choose the nonlinearity $ϕ(x)=erf(\alphax)$ with $\alpha=\sqrt{\pi}/2$. Similar to $tanh$, this function is bounded between ±1 and has slope $ϕ^{′}(0)=1$ at the origin. For this function, we can explicitly compute the relevant Gaussian integrals. The minimal eigenvalue of $M$ to produce a fixed point, Equation 44, is then given by $\lambda_{+,min}=1+2\alpha^{2}\sigma_{noise}^{2}$. For $\lambda_{+}>\lambda_{+,min}$, the resulting fixed point has norm

$$
‖κ¯‖^{2}=\frac{\lambda_{+}^{2}−\lambda_{+,min}^{2}}{2\alpha^{2}},
$$

as shown in Figure 12A. The larger eigenvalue of the Jacobian is $\gamma_{+}=−(\lambda_{+}^{2}−\lambda_{+,min}^{2})/\lambda_{+}^{2}$. We next obtain the correlation between fixed point and output weights by assuming that the bias part of the loss (Equation 38) is kept at zero. This is reasonable because it requires only a small adaptation to the weights that leaves the variance part mostly untouched. The resulting correlation is

$$
ρ^{2}=\frac{1}{N}\frac{z^^{2}}{‖κ¯‖^{2}},
$$

![Figure 12.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig12-v1.jpg)

**Figure 12.:** (A–D) Mean field theory predictions as a function of positive feedback strength $\lambda_{+}$. The dotted lines indicate $\lambda_{+,min}$, the minimal eigenvalue necessary to generate fixed points. (A) Norm of fixed point $‖𝜿‾‖$. (B) Correlation $ρ$ so that $L_{bias}=0$. (C, D) Loss due to fluctuations for different $\lambda_{−}$ or networks sizes $N$. Dots indicate minima. (E–G) Latent states $𝜿$ of simulated networks for randomly drawn projections $U$. The symmetric matrix $M$ is fixed by setting $\lambda_{+}$ as noted, $\lambda_{−}=−5$, and demanding $L_{bias}=0$ (for the mean field prediction). Dots are samples from the simulation interval $t\in[20,100]$. (H–J) Histogram for the corresponding output $z$. Mean is indicated by full lines, the dashed lines indicate the target $z^$. Other parameters: $N=256$, $\sigma_{noise}=1$, $z^=1$.

so that increasing $\lambda_{+}$ also decreases the correlation (Figure 12B). Finally, we obtain an expression for the variance part of the loss only in terms of the eigenvalues of $M$:

$$
L_{var}=ρ^{2}(\frac{\sigma_{noise}^{2}\lambda_{+}^{2}}{\lambda_{+}^{2}−\lambda_{+,min}^{2}}+\frac{\sigma_{noise}^{4}\alpha^{2}}{3\lambda_{+}^{2}−\lambda_{+,min}^{2}})+(1−ρ^{2})\frac{\sigma_{noise}^{2}}{1−\frac{\lambda_{−}}{\lambda_{+}}}.
$$

We show $L_{var}$ over $\lambda_{+}$ for different negative feedback loop sizes $\lambda_{−}$ (Figure 12C) and different network sizes $N$ (Figure 12D). The first term diverges at the phase transition where the fixed point appears, $\lambda_{+}↘\lambda_{+,min}$. Learning will thus push the weights away from the phase transition toward larger $\lambda_{+}$. With such increasing $\lambda_{+}$, the fixed point norm increases, and the fixed point rotates away from the output, decreasing the correlation. This in term emphasizes the last term, scaled by $1−ρ^{2}$. The last term is reduced with increasingly negative $\lambda_{−}$, corresponding to the negative feedback loop that suppresses noise.

Learning can in principle strengthen this feedback further and further, $\lambda_{−}→−∞$ (apart from possible stability issues; Kadmon et al., 2020). However, as for the linear network, section Learning with noise for linear RNNs, this process takes time. We thus assume $\lambda_{−}$ to be fixed and search for a minimum across $\lambda_{+}$. For $\lambda_{−}<0$, the last term in Equation 53 increases with increasing $\lambda_{+}$: the effective feedback loop in the full, nonlinear system is weakened by saturation. The loss $L_{var}$ thus has a minimum at some moderate $\lambda_{+}$.

To illustrate the mechanisms described above, we simulated networks at different $\lambda_{+}$ and with $\lambda_{−}=−5$. For each $\lambda_{+}$, we compute $ρ$ according to Equation 52. Setting $𝐯_{out}=[1,0]^{T}$, we then set the resulting symmetric $M=VΛV^{T}$. For each network sample, we then draw independent random projections $U\inℝ^{N\times2}$. We started simulations at either one of the two nonzero fixed points. For $\lambda_{+}$ just above $\lambda_{+,min}$, the noise pushes activity from one basin of attraction to the next (Figure 12C). The resulting output becomes centered around zero and independent of the initial condition for long simulation times (Figure 12F). For the optimal $\lambda_{+}$, the trajectories remain close to either one fixed point (Figure 12F). The output forms two overlapping distributions, each closely matching the target on average (Figure 12I). For larger $\lambda_{+}$, the fixed points become increasingly larger (Figure 12G). While this decreases the probability of leaving the basin of attraction even further, the variance along the output weights becomes larger (slightly wider histograms in Figure 12J). Note that the mean starts to deviate from the prediction. This is not covered by our theory and is potentially due to the linearization of the fluctuations.

All-in-all, this section revealed a potential path to oblique solutions, initiated by the large fluctuations close to a phase transition, and the interplay between the negative feedback loop and saturation. In the following section, we show that learning via gradient descent actually follows this path and that the parameters predicted by the minimum of $L_{var}$ quantitatively predict solutions from learning.

#### Oblique solutions from learning are predicted by the mean field theory

We trained neural networks on the fixed points task described above by applying gradient descent to the 2×2 matrix $M$, initialized at $M_{0}=0$. The gradients $G_{M}$ with respect to $M$ are equivalent to those with respect to $W=\frac{1}{N}UMU^{T}$ restricted to the subspace spanned by $U$, i.e., $G_{M}=\frac{1}{N}UU^{T}G_{W}\frac{1}{N}UU^{T}$. Such a restriction is exact in the case of linear RNNs without random initial connectivity, and yields qualitative insights even for nonlinear networks with random initial connectivity (Schuessler et al., 2020b).

The output weights were set to $𝐰_{out}=\frac{1}{\sqrt{N}}𝐮_{1}$, where $𝐮_{1}$ is the first of the two projection vectors $U=[𝐮_{1},𝐮_{2}]$. We thus have large output weights with norm $‖𝐰_{out}‖=1$. Trajectories were initialized at $𝐱(0)=𝟎$. At the beginning of a trial with target output $z^=\pm1$, the network receives one pulse $s(t)=\pm\delta(t)$ along the input weights $𝐰_{in}=𝐮_{2}$. The input direction is hence the second available direction for the rank-two connectivity. This is a sensible choice as networks without the restriction to rank-two weights would span the recurrent weights from existing directions, and a rank-two connectivity would hence also be spanned by $𝐰_{out}$ and $𝐰_{in}$ (Schuessler et al., 2020b).

The loss over learning time for one network is shown in Figure 13A. Learning consisted of two phases: a first phase in which the network did not possess a fixed point and hence did not match the target on average, $L_{bias}>0$. At some point, $L_{bias}$ rapidly decreases, and $L_{var}$ dominates the overall loss. During the second phase, $L_{var}$ slowly decreases, with $L_{bias}$ hovering around zero.

![Figure 13.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig13-v1.jpg)

**Figure 13.:** (A–C) Learning dynamics with gradient descent for example network with $N=1024$ neurons and with noise variance $\sigma_{noise}^{2}=1$. (A) Loss with separate bias and variance components. (B) Matrix coefficients $M_{ij}$. The dotted lines almost identical to $M_{22}$ and $M_{11}$ indicate the eigenvalues $\lambda_{+}$ and $\lambda_{−}$, respectively. The dashed line indicates $\lambda_{+,min}$. (C) Fixed point norm and correlation. (D–F) Final loss, fixed point norm, and correlation for networks of different sizes $N$. Shown are mean (dots and lines) and standard deviation (shades) for five sample networks, and the prediction by the mean field theory. Gray lines indicate scaling as $aN^{k}$, with $k\in{0,−1/4,−1/2}$. Note the log-log axes for (E, F).

The coefficients of the matrix $M$ indicate the underlying learning dynamics (Figure 13B). The coefficient along the output weights, $M_{11}$, is almost identical with $\lambda_{−}$. It continually grows in the negative direction, unaffected by the different phases. Its time course is very similar to the time course observed for the linear system (Figure 10B). In contrast, the coefficient along the input weights, $M_{22}$, mirrors the two phases. It grows increasingly fast in the first phase and saturates during the second phase. Its value is very close to the larger eigenvalue, $\lambda_{+}$. The transition between the two phases of learning happens at the phase transition of the dynamical system when the fixed point emerges for $\lambda_{+}=\lambda_{+,min}$. The off-diagonal entries show that $M$ is asymmetric during the first phase and becomes symmetric later on. The coefficient $M_{12}$ corresponds to the feedforward mode mapping the state decaying from $𝐱(0)=𝐮_{2}$ after the pulse to the output weights $𝐰_{out}=\frac{1}{\sqrt{N}}𝐮_{1}$.

Tracing the fixed point norm $‖𝜿‾‖$ and the correlation $ρ$ over learning time shows what we expected (Figure 13C): The norm grows rapidly at the phase transition, which is accompanied by a decrease in the correlation. The example yields a fixed point with norm $‖𝜿‾‖≈0.7$ and correlation $ρ≈0.05$ for a network with $N=1024$. The mere numbers already suggest that we call this an oblique solution, but the theory description above is based on how these numbers scale with network size $N$. We trained networks with different $N$ but otherwise the same conditions. They reached the same loss (Figure 13A, $L_{bias}≈0$ not shown). The fixed point norm decreases weakly with $N$, with $‖𝜿‾‖=O(N^{k})$, for some $k\geq−1/4$ (Figure 13E). The correlation decreases faster, yet not quite with $1/\sqrt{N}$ (Figure 13F).

We compared the outcome of learning to our mean field theory. Given that $M$ is approximately symmetric at the end of learning, we directly applied our results from the previous sections, again assuming $L_{bias}=0$. We fixated $\lambda_{−}$ to match the value at the end of training and computed the $\lambda_{+}$ that minimized $L_{var}$, Equation 53. The results for the norm and correlation match those values obtained with gradient descent very closely.

Our high-level description of oblique and aligned dynamics did not involve scaling with network size (section Aligned and oblique population dynamics). However, the underlying assumption was that the activity of single neurons $x_{i}$ is not vanishing for large networks, i.e., $x_{i}=O(1)$. This would imply $‖𝜿‾‖=O(1)$ and $ρ=O(1/\sqrt{N})$. This is indeed what we observed for the more complex tasks when training networks of different sizes (not shown). We note that our results for the simple fixed point task deviate weakly from this (Figure 13E and F). This hints at other factors pushing solutions to $‖𝜿‾‖=O(1)$. One such factor may be that the loss function $L_{var}(\lambda_{+})$ is very flat for $\lambda_{+}$ larger than the optimum (Figure 12C and D). If learning pushes trajectories beyond the optimum at some point, e.g., due to large updates or if the optimum shifts over learning , then the learning signal to reduce $\lambda_{+}$ afterward may be too small to yield visible effects in finite learning time.

In summary, the last two sections capture the main mechanisms that drive solutions to the oblique regime in nonlinear, noise-driven networks. Although marginally small solutions seem possible for large output weights, such solutions are close to a phase transition, so the resulting system is very susceptible to noise. To accommodate robust solutions, the trajectories (here the fixed points) must increase in magnitude, while rotating away from the output weights. This further allows the implementation of a negative feedback loop that suppresses noise along the output direction. Its efficacy can be reduced by too much saturation, which in turn keeps solutions from growing ever larger. The resulting sweet spot is a network with oblique dynamics.

### Mechanisms behind decoupling of neural dynamics and output

Here, we discuss in more detail the underlying mechanisms for the qualitative decoupling in oblique networks. We make a high-level argument that splits into two parts: first the possibility of decoupling in oblique, but not aligned, networks, and second a putative mechanism driving the decoupling.

For the first part, we observe that the output in oblique networks can be obtained from the leading components of the dynamics (along the PCs), but importantly also from the non-leading ones. To see this, we unpack the output in Equation 1 in a slightly different way than before, Equation 3. Namely, we split the activity vector $𝐱$ into its component along the leading PCs, $𝐱_{lead}$, and the remaining, trailing component, $𝐱_{trail}$. By definition of the leading PCs as the directions of largest variance, the leading component is expected to be large, and the trailing one small. Inserting this decomposition $𝐱=𝐱_{lead}+𝐱_{trail}$ into Equation 1 leads to

$$
z=w_{out}^{T}(x_{lead}+x_{trail})=‖w_{out}‖(ρ_{lead}‖x_{lead}‖+ρ_{trail}‖x_{trail}‖),
$$

with separately defined correlations $ρ_{lead}=corr(𝐰_{out},𝐱_{lead})$ and $ρ_{trail}=corr(𝐰_{out},𝐱_{trail})$.

For aligned networks, we recover the results from before: $𝐰_{out}$ is small so that the output can only be generated by the leading part with large correlation $ρ_{lead}$. The trailing part is unconstrained but is also not contributing to either the output or the leading dynamics, and hence not of interest.

For oblique networks, $𝐰_{out}$ is large so that the output can be generated by either of the two terms in Equation 54. The correlation $ρ_{lead}$ has to be small because else the output would be too large. The other correlation, $ρ_{trail}$, can be large, because non-dominant component $𝐱_{trail}$ is small. Both terms are potentially of the same magnitude, which means both can potentially contribute to the output. If the dominant part alone generates the output, then neural dynamics and output are coupled and the solution is similar to an aligned one (Figure 14, right). If, however, the non-dominant part alone generates the output, and the correlation $ρ_{lead}$ is so small that the dominant part does not contribute to the output, then the dominant part is not constrained by the task (Figure 14, center right). In that case, the dominant dynamics and the output can decouple qualitatively, and we may see the large variability between learners observed above.

![Figure 14.](https://cdn.elifesciences.org/articles/93060/elife-93060-fig14-v1.jpg)

**Figure 14.:** Left: All networks produce the same output (Figure 1). Center: Unstable solutions that arise early in learning. For lazy solutions, initial chaotic activity is slightly adapted, without changing the dynamics qualitatively. For marginal solutions, vanishingly small initial activity is replaced with very small dynamics sufficient to generate the output. Right: With more learning time and noise added during the learning process, stable, oblique solutions arise. The neural dynamics along the largest principal components (PCs) can be either decoupled from the output (center right) or coupled (right). For decoupled dynamics, the components along the largest PCs (blue subspace) differ qualitatively from those generating the output (same as Figure 1B, bottom). The dynamics along the largest PCs inherit task-unrelated components from the initial dynamics or randomness during learning. Another possibility are oblique, but coupled dynamics (right). Such solutions don't inherit task-unrelated components of the dynamics at initialization. They are qualitatively similar to aligned solutions, and the output is generated by a small projection of the output weights onto the largest PCs (dashed orange arrow).

The existence of decoupled solutions for oblique dynamics leads to the second question: Why and when do such solutions arise? Understanding this requires more detailed insights into the learning process. Roughly speaking, learning in the oblique regime has two opposite goals: first, to generate the desired output as fast as possible, and hence to induce changes to activity that are as small as possible (section Analysis of solutions under noiseless conditions); and second, to generate solutions that are robust and stable, and hence to induce changes in activity that are large enough to not be disrupted by noise (section Oblique solutions arise for noisy, nonlinear systems). During the process of learning, small, unstable solutions appear first (Figure 14, center). These may be highly variable, depending strongly on random initialization or other randomness experienced during learning. Such solutions then slowly solidify into stable solutions, that may inherit the variability of the early solutions (Figure 14, right).

The process of how learning transforms small, unstable solutions to larger, robust ones is analyzed in section Learning with noise for linear RNNs and Oblique solutions arise for noisy, nonlinear systems. The details of how this process introduces variability between learners, however, are not discussed there and left for future work.
