# Peer review - Round 1

Editors:
- Alex Fornito, https://ror.org/02bfwt286 Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74921.sa0](https://doi.org/10.7554/eLife.74921.sa0)

This paper investigates the emergence of complex network organization in neuronal circuits grown in vitro. Network analysis of neuronal activity recordings allowed a detailed assessment of how neurons self-organise into clusters of functionally segregated models while also retaining a capacity for integrated communication through a subset of highly active neurons. This work is of interest to researchers working on neuronal connectivity, brain development, and self-organisation in complex systems.


---

# Peer review - Round 1

Editors:
- Alex Fornito, https://ror.org/02bfwt286 Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74921.sa1](https://doi.org/10.7554/eLife.74921.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Self-organization of in vitro neuronal assemblies drives to complex network topology" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jordi Soriano (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please clarify the following experimental details:

– According to Results and Methods, there were 424 networks used, which comprised from DIV 6 to 35. However, it is not clear whether the same cultures were present in the different days of analysis. For instance, some DIVs could include networks that were not present in the others. Since there at least 9 networks in each DIV, do these 9 correspond to 9 cultures that are present in all the other days?

– Please clarify the influence of the degree of neuronal aggregation in the neuronal cultures, i.e., whether neurons cover homogeneously the substrate or they group in islands. Is such information available? Aggregation could locally increase the density of neurons and potential connections. Different experimental studies have indeed shown that fluctuations in spatial neuronal density substantially affect network development and effective/functional connectivity traits (Okujeni et al., J Neurosci 2017; Tibau et al., IEEE Trans Net Sci Eng 2020). If the information is not available, the authors could mention such a limitation, and even explain that calcium imaging data (with all neurons accessible) could provide additional insight.

– From the spacing between electrodes, one gets about 1.5x1.5 mm^2 total square area. The lateral size of the square is of the order of the axonal length of neurons grown in culture, so potentially any neuron can easily connect with any other in the culture, making the approximation of a random connectivity in the simulations valid. This should be discussed. There are indeed works pointing out the importance of spatially embedding in cultures (e.g., Hernández-Navarro et al., Phys Rev Lett 2017), in which metric correlations can be neglected in small networks.

2) The authors seem to use the "effective connectivity validation" analysis to associate the inferred effective connections with structural ones, or at least a substantial part of them. This is a strong assumption that is later treated in the "Neuronal networks self-organization" section of the Discussion. However, it can be confusing when reading the Results, so an earlier clarification (in Results) of the limitations of effective connectivity inference is necessary, and the authors should explain that 'connections' in the article reflect strong paths for information flow rather than actual structural connections. Indeed, not all possible dynamical states of the network are present in a raster plot that portrays solely spontaneous activity; i.e., that information flow (from which effective connectivity is extracted) does not explore all possible structural paths. With inhibition active, several communication paths may be inactive or silent, although structural connections may exist. The extreme difficulty of inferring structure from dynamics has motivated experimentalists to compare effective connectivity inferred from evoked activity with spontaneous activity, to later compare with physiological information (see e.g., Bauer et a., Cerebral Cortex 2018), observing that evoked activity better captures the network's underlying circuitry.

3) Related to the above, it would be useful for the authors to run additional simulations of the same network with and without inhibition (i.e., by completely silencing the inhibitory neurons) and compare how many connections in the excitation-pure network are present in the excitation-inhibition one. A test relative to non-random graphs would also be helpful; in particular, spatial graphs in which connectivity probability depends on Euclidean distance (Orlandi et al., Nat Phys 2013) would be useful, and even help construct a model to explain the overall results, particularly in understanding that nearby neurons shape spatially compact communities.

4) Figures 1e shows the distribution of connections. The distribution shifts to higher k values as maturation progresses, indicating an increase of connectivity along development. The authors should include an inset showing the p(k) value for a given k (e.g., k=10, 20, and 40) to illustrate that p(k) gradually goes up.

5) Figure 1g shows the evolution of Euclidean connectivity distances along DIV. This is an important result since it illustrates the gradual evolution from a segregated to an integrated network. The authors could place the 'probability' color bar at the top of the figure in a horizontal manner and leave the bottom-right corner to plot the average connectivity distance as a function of DIV. Additionally, the panel of Figure 1g contains the results averaged over recordings. Can the authors show as a supplementary figure the evolution of the same network along DIV?

6) Neuronal circuits in vivo and in vitro experience GABA switch (Soriano et al., PNAS 2008; Tibau et al., Front Neur Circ 2013; Tibau et al., IEEE Trans Net Sci Eng 2020) in which inhibition behaves as excitatory up to DIV 7-8, and afterwards has its normal inhibitory role. In panel 1g, connections seem to extend a larger distance at DIV 6 than at DIV 9, and I think GABA switch is the explanation. At DIV 6, GABA structural connections (behaving as excitatory) could extend longer distances than the excitatory ones and lead to the emergence of long-distance effective connections, which suddenly vanish at DIV 9. If so, this could be explained in the discussion, also addressing the fact that GABA switch is not analyzed in this work. The authors address GABA switch in line 386, but they could extend the discussion a bit more.

7) Please clarify why most of the motifs (Figure 2f) to drop after DIV 27?

8) Many neural mechanisms including silent synapses and STDP are discussed in this manuscript. However, neither generative network model nor neural circuit model is developed to directly illustrate possible mechanisms underlying network formation and development. In the absence of a generative model providing insights into causal relationships between the modular organization, neuronal hubs and segregation/integration, the authors should clear state that their discussion of mechanisms is primarily speculative, and suggest strategies for gaining further mechanistic insight.

9) Effective connectivity is inferred by using a transfer entropy analysis of electrophysiological signals. However, it has been questioned that the transfer entropy (James, et al., 2016) does not quantify the flow of information as commonly assumed. Given this concern, some clarifications or comparisons with state-of-art methods need to be provided.

10) What is the relation between the log-normal distribution of coupling weights and that of firing rate? What do these heavy-tailed distributions mean for collective network states and whether they are related to the key connectivity properties such as neuronal hubs? Given that all these phenomena have been reported in previous studies, without an in-depth investigation of the problems, the novel contribution of this study is somewhat unclear to me.

11) In Figure 1c and Figure 1d, the log normal distribution is used to fit the data. Is this distribution better than other heavy-tailed distribution such as truncated Pareto distribution?

12) Line 88 – "the term neuronal network to refer to the neuronal assemblies coupled to electrodes and effective networks to refer to the network inferred from the neural recordings". This sentence is not correctly highlighting these two central concepts of the paper. Considering what was written a few lines above, and by also looking at the Results and Methods sections, maybe it would be easier for the reader to follow something along these lines: "the term neuronal networks to refer to transiently coupled neuronal assemblies and effective networks to refer to the circuits inferred from neural recordings". Of course, this is just a suggestion. The aim is to make as clear as possible the intentions of the authors to disentangle a dynamical aspect ('neuronal assembly') and a structural aspect ('effective network').

13) Line 145 – "Only some connections extended for long distances, and these connections were more likely to also have a weight close to the geometric mean. Connections with lower and higher weight values were more likely to have shorter lengths." Very interesting! Can the authors provide a statistical characterization of these effects and a corresponding figure? In particular it is important to test if this feature is also present in the two other models (Watts-Strogatz and Kwok et al.). If yes, it should be mentioned. If not, then it is an important distinguishing feature, and in this case, this aspect should be considerably expanded.

14) Line 290 – "the higher the neuron score, the higher the median firing rate over all DIVs." The authors took care of choosing the best inferring method available (transfer entropy). However, a big issue of the structure-from-dynamic approach is its circularity. Dynamical information is used to infer the structure of a network and to draw conclusions concerning how the dynamically-derived structure affects network dynamic itself. Therefore the correlation between firing rate and neuron 'hub' scoring (sentence at the beginning of this paragraph) more than being a result of the study might be a side-effect of the analysis approach. The authors already took the care of searching the available literature to find support (like Sung et al. 2005 for the firing rates of neurons), they are invited to expand their discussion on this point, and suggest experimental and analytical solutions, e.g. use electron microscopy to validate (at least a portion of) the activity-derived networks, or the literature they found to also compare their motifs results, or, in case, why their results cannot be compared with the available literature and electron microscopy data. The use of a spiking network to test the validity of the inference procedure is interesting and valid as a preliminary test, but would require an entire separate work to be able to use it to break the structure-from-dynamic circularity. So this point too needs to be clearly discussed.

15) Line 350 – Even though it is the discussion, it should be clearly indicated that by "self-organization", in the context of the experimental strategy and presented results, the authors cannot mean functional connectivity (as it is hinted by the first paragraph, line 352-257), but only self-organization as self-reinforcement of synaptic connections between neurons with correlated firing (as it is done in the following paragraphs of discussion). If, for example, spatially organized stimuli through the electrode were used, and effects on the network structure were observed, it could have been possible to advance the idea that the network self-organization would be functional. In any case, the silent synapses hypothesis they suggest is fundamental to understand also functional results. They could maybe move the first paragraph to the end?

16) Line 62 "The spontaneous emergence of spatio-temporal patterns driven by neuronal activity is characteristic of a self-organizing system." maybe could be a little expanded given that the rest of the article will be a balance of structure and dynamic running over it.

17) Line 75 "DIV" is first used without being defined. The definition (days in vitro) comes for the first time in the caption of figure 3 (line 1211)

18) Line 194, "only 5 of the 13 patterns (5, 8, 11, 12, and 13), were", the comma after the right bracket should be dropped.

19) Line 216 "Subgraphs", "modules", and "communities" seem to be used interchangeably. However they underlie different meanings (respectively theoretical, architectural, and functional). Wouldn't it be easier for the reader to stick to one term, if just one meaning is intended, or explain the term and its use, where appropriate?

The clustering grows towards the 12 DIV then decreases, as path length and small-worldness (Figure 2cde). Is this backed up by other data? We are in use with the idea that brain networks are small-world, it looks like these networks, towards the 20 DIVs are not.

20) Line 290, "Figure 4d shows that the higher…". It should be "Figure 4e". Additionally, for clarity in the presentation of results, panel 4f (participation coefficient) should go above panel 4e (firing rate).

21) Line 346 "neuron loss drastically impacted the topological organization of the effective networks, resulting in a breakup of the networks into different components" In addition (and before) pathological conditions, the neuron loss can also be a (functional) feature of the multi-stage process of circuit refinement, as the authors found in the formation of communities.

22) Lines 428,429 There is a list of properties but is written in a series of sentences (lacking verbs). "… Strogatz, 2001). A short path …" should be ".. Strogatz, 2001), a short path …". One line below, "… Ottino, 2004). And the presence …" should be: "… Ottino, 2004), and the presence …"

23) Line 774, the fonts for variables and text are the same, making difficult to read the equation.
