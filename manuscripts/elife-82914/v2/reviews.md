# Peer review - Round 1

Editors:
- Jörn Diedrichsen, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82914.sa0](https://doi.org/10.7554/eLife.82914.sa0)

Models of cerebellar function and the coding of inputs in the cerebellum often assume that random stimuli are a reasonable stand-in for real stimuli. However, the important contribution of this paper is that conclusions about optimality and sparseness in these models do not generalize to potentially more realistic sets of stimuli, for example, those drawn from a low-dimensional manifold. The mathematical analyses in the paper are convincing and possible limitations, including the abstraction from biological details, are well discussed.


---

# Peer review - Round 1

Editors:
- Jörn Diedrichsen, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82914.sa1](https://doi.org/10.7554/eLife.82914.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Task-dependent optimal representations for cerebellar learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jörn Diedrichsen as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Henrik Jörntell (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. You will see that the recommended revisions most concern clarity of presentation, as well as tempering some of the claims.

Essential revisions:

1) All reviewers had questions about specific details of the study (see below comments). I hope you can use these questions as a guideline to improve the clarity and accessibility of the paper. As suggested by reviewer #2, this may involve moving some details from the supplementary materials to the main manuscript.

2) The current eLife assessment (see below) emphasizes the main limitations of the paper – namely the question of to what degree the conclusions of the paper would change if more specific (and biologically more plausible) details about the cerebellar circuit would be taken into account. I hope you will take the opportunity to respond in detail to these points in your response to the reviewer document, which will be posted alongside the revised version of the manuscript and cover the main issues in the Discussion section of the main document.Reviewer #1 (Recommendations for the authors):

This paper provides compelling and clear analyses that show that the coding level (sparsity) of the granule-cell layer of a cerebellar-like network does not only change the dimensionality of the representation, but also the inductive bias of the network: Higher sparsity biases the network to learning more high-frequency representations. Depending on the dominant frequencies of the target function, different coding levels are therefore optimal. The results are important/fundamental to theories of cerebellar learning and speak to a relevant ongoing debate in cerebellar learning, but will be of interest to readers outside of cerebellar neurophysiology.

I had two problems in understanding the paper that the authors hopefully can clarify in the revision:

Page 8: Third paragraph: At this point in the text it is a bit unclear why the K(x * x') changes shape as shown in Figure 3c. I assume the shape of the kernel K depends on the activation function in the hidden layer. It may be useful for the reader if you could give an example of the Kernel for the specific case you are showing in Figure 3c.

Page 11, 4th paragraph: Why is the distribution corr(Jeffi,Jeffj) uniform on -1 to 1? Since both are high-dimensional random vectors, should the correlation not be centered around 0? The target of uniform distribution needs to be better explained to make this analysis accessible.Reviewer #2 (Recommendations for the authors):

Here, a simple model of cerebellar computation is used to study the dependence of task performance on input type: it is demonstrated that task performance and optimal representations are highly dependent on task and stimulus type. This challenges many standard models which use simple random stimuli and concludes that the granular layer is required to provide a sparse representation. This is a useful contribution to our understanding of cerebellar circuits, though, in common with many models of this type, the neural dynamics and circuit architecture are not very specific to the cerebellum, the model includes the feed-forward structure and the high dimension of the granule layer, but little else. This paper has the virtue of including tasks that are more realistic, but by the paper's own admission, the same model can be applied to the electrosensory lateral line lobe and it could, though it is not mentioned in the paper, be applied to the dentate gyrus and large pyramidal cells of CA3. The discussion does not include specific elements related to, for example, the dynamics of the Purkinje cells or the role of Golgi cells, and, in a way, the demonstration that the model can encompass different tasks and stimuli types is an indication of how abstract the model is. Nonetheless, it is useful and interesting to see a generalization of what has become a standard paradigm for discussing cerebellar function.

I was impressed by the clarity of this manuscript. My only comment is that I found too much was deferred to the appendix, I thought the bits and pieces in the appendix were very clarifying, and given the appendix contains short pieces of extra information explaining the exact nature of the models and tasks, the manuscript would have been easier to follow and think about if these had just been integrated into the text. Often you read papers and wish some details had been shifted into an appendix since they distract from the flow of the description, but the opposite is true here, integrating the details into the text would've made it more concrete in a useful way and the tables of parameters, as tables, would not have interrupted the flow while making it much easier to see the scale of the models and their architecture.

Reviewer #3 (Recommendations for the authors):

The paper by Xie et al. is a modelling study of the mossy fiber-to-granule cell-to-Purkinje cell network, reporting that the optimal type of representations in the cerebellar granule cell layer depends on the type task. The paper stresses that the findings indicate a higher overall bias towards dense representations than stated in the literature, but it appears the authors have missed parts of the literature that already reported on this. While the modelling and analysis appear mathematically solid, the model is lacking many known constraints of the cerebellar circuitry, which makes the applicability of the findings to the biological counterpart somewhat limited.

I have some concerns with the novelty of the main conclusion, here from the abstract:

'Here, we generalize theories of cerebellar learning to determine the optimal granule cell representation for tasks beyond random stimulus discrimination, including continuous input-output transformations as required for smooth motor control. We show that for such tasks, the optimal granule cell representation is substantially denser than predicted by classic theories.'

Stated like this, this has in principle already been shown, i.e. for example:

Spanne and Jorntell (2013) Processing of multi-dimensional sensorimotor information in the spinal and cerebellar neuronal circuitry: a new hypothesis. PLoS Comput Biol. 9(3):e1002979.

Indeed, even the 2 DoF arm movement control that is used in the present paper as an application, was used in this previous paper, with similar conclusions with respect to the advantage of continuous input-output transformations and dense coding. Thus, already from the beginning of this paper, the novelty aspect of this paper is questionable. Even the conclusion in the last paragraph of the Introduction: 'We show that, when learning input-output mappings for motor control tasks, the optimal granule cell representation is much denser than predicted by previous analyses.' was in principle already shown by this previous paper.

However, the present paper does add several more specific investigations/characterizations that were not previously explored. Many of the main figures report interesting new model results. However, the model is implemented in a highly generic fashion. Consequently, the model relates better to general neural network theory than to specific interpretations of the function of the cerebellar neuronal circuitry. One good example is the findings reported in Figure 2. These represent an interesting extension to the main conclusion, but they are also partly based on arbitrariness as the type of mossy fiber input described in the random categorization task has not been observed in the mammalian cerebellum under behavior in vivo, whereas in contrast, the type of input for the motor control task does resemble mossy fiber input recorded under behavior (van Kan et al. 1993).

The overall conclusion states:

'Our results…suggest that optimal cerebellar representations are task-dependent.'

This is not a particularly strong or specific conclusion. One could interpret this statement as simply saying: ' if I construct an arbitrary neural network, with arbitrary intrinsic properties in neurons and synapses, I can get outputs that depend on the intensity of the input that I provide to that network.'

Further, the last sentence of the Introduction states: 'More broadly, we show that the sparsity of a neural code has a task-dependent inﬂuence on learning…' This is very general and unspecific, and would likely not come as a surprise to anyone interested in the analysis of neural networks. It doesn't pinpoint any specific biological problem but just says that if I change the density of the input to a [generic] network, then the learning will be impacted in one way or another.

The interpretation of the distribution of the mossy fiber inputs to the granule cells, which would have a crucial impact on the results of a study like this, is likely incorrect. First, unlike the papers that the authors cite, there are many studies indicating that there is a topographic organization in the mossy fiber termination, such that mossy fibers from the same inputs, representing similar types of information, are regionally co-localized in the granule cell layer. Hence, there is no support for the model assumption that there is a predominantly random termination of mossy fibers of different origins. This risks invalidating the comparisons that the authors are making, i.e. such as in Figure 3. This is a list of example papers, there are more:

van Kan, Gibson and Houk (1993) Movement-related inputs to intermediate cerebellum of the monkey. Journal of Neurophysiology.

Garwicz et al. (1998) Cutaneous receptive fields and topography of mossy fibres and climbing fibres projecting to cat cerebellar C3 zone. The Journal of Physiology.

Brown and Bower (2001) Congruence of mossy fiber and climbing fiber tactile projections in the lateral hemispheres of the rat cerebellum. The Journal of Comparative Neurology.

Na, Sugihara, Shinoda (2019) The entire trajectories of single pontocerebellar axons and their lobular and longitudinal terminal distribution patterns in multiple aldolase C-positive compartments of the rat cerebellar cortex. The Journal of Comparative Neurology.

The nature of the mossy fiber-granule cell recording is also reviewed here:

Gilbert and Miall (2022) How and Why the Cerebellum Recodes Input Signals: An Alternative to Machine Learning. The Neuroscientist

Further, considering the recoding idea, the following paper shows that detailed information, as it is provided by mossy fibers, is transmitted through the granule cells without any evidence of recoding: Jorntell and Ekerot (2006) Journal of Neuroscience; and this paper shows that these granule inputs are powerfully transmitted to the molecular layer even in a decerebrated animal (i.e. where only the ascending sensory pathways remains) Jorntell and Ekerot 2002, Neuron.

I could not find any description of the neuron model used in this paper, so I assume that the neurons are just modelled as linear summators with a threshold (in fact, Figure 5 mentions inhibition, but this appears to be just one big lump inhibition, which basically is an incorrect implementation). In reality, granule cells of course do have specific properties that can impact the input-output transformation, PARTICULARLY with respect to the comparison of sparse versus dense coding, because the low-pass filtering of input that occurs in granule cells (and other neurons) as well as their spike firing stochasticity (Saarinen et al. (2008). Stochastic differential equation model for cerebellar granule cell excitability. PLoS Comput. Biol. 4:e1000004) will profoundly complicate these comparisons and make them less straight forward than what is portrayed in this paper. There are also several other factors that would be present in the biological setting but are lacking here, which makes it doubtful how much information in relation to the biological performance that this modelling study provides:

What are the types of activity patterns of the inputs? What are the learning rules? What is the topography? What is the impact of Purkinje cell outputs downstream, as the Purkinje cell output does not have any direct action, it acts on the deep cerebellar nuclear neurons, which in turn act on a complex sensorimotor circuitry to exert their effect, hence predictive coding could only become interpretable after the PC output has been added to the activity in those circuits. Where is the differentiated Golgi cell inhibition?

The problem of these, in my impression, generic, arbitrary settings of the neurons and the network in the model becomes obvious here: 'In contrast to the dense activity in cerebellar granule cells, odor responses in Kenyon cells, the analogs of granule cells in the Drosophila mushroom body, are sparse…' How can this system be interpreted as an analogy to granule cells in the mammalian cerebellum when the model does not address the specifics lined up above? I.e. the 'inductive bias' that the authors speak of, defined as 'the tendency of a network toward learning particular types of input-output mappings', would be highly dependent on the specifics of the network model.

More detailed comments:

Abstract:

'In these models [Marr-Albus], granule cells form a sparse, combinatorial encoding of diverse sensorimotor inputs. Such sparse representations are optimal for learning to discriminate random stimuli.' Yes, I would agree with the first part, but I contest the second part of this statement. I think what is true for sparse coding is that the learning of random stimuli will be faster, as in a perceptron, but not necessarily better. As the sparsification essentially removes information, it could be argued that the quality of the learning is poorer. So from that perspective, it is not optimal. The authors need to specify from what perspective they consider sparse representations optimal for learning.

Introduction:

'Indeed, several recent studies have reported dense activity in cerebellar granule cells in response to sensory stimulation or during motor control tasks (Knogler et al., 2017; Wagner et al., 2017; Giovannucci et al., 2017; Badura and De Zeeuw, 2017; Wagner et al., 2019), at odds with classic theories (Marr, 1969; Albus, 1971).' In fact, this was precisely the issue that was addressed already by Jorntell and Ekerot (2006) Journal of Neuroscience. The conclusion was that these actual recordings of granule cells in vivo provided essentially no support for the assumptions in the Marr-Albus theories.

Results:

First para: There is no information about how the granule cells are modelled.

Second para: 'A typical assumption in computational theories of the cerebellar cortex is that inputs are randomly distributed in a high-dimensional space.' Yes, I agree, and this is in fact in conflict with the known topographical organization in the cerebellar cortex (see broader comment above). Mossy fiber inputs coding for closely related inputs are co-localized in the cerebellar cortex. I think for this model to be of interest from the point of view of the mammalian cerebellar cortex, it would need to pay more attention to this organizational feature.
