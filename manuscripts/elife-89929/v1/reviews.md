# Peer review - Round 1

Editors:
- Matthieu Louis, https://ror.org/02t274463 University of California, Santa Barbara United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89929.sa0](https://doi.org/10.7554/eLife.89929.sa0)

Inspired by bee's visual behavior, this manuscript develops a model of visual scanning, processing, and pattern recognition learning. The work shows how pre-training with natural images creates spatiotemporal receptive fields in lobula neurons that enhance pattern discrimination through sparse encoding. The authors provide a solid analysis of neural responses, model performance across tasks, and the contributions of components like scanning strategies and lateral inhibition. While the model represents a functional circuit for active vision, its biological plausibility is somewhat limited by intentional simplifications. The systematic evaluation of necessary components and comparisons with bee behavioral data strengthen the findings. This important work offers insights into motion-driven visual processing in compact neural systems.


---

# Peer review - Round 1

Editors:
- Matthieu Louis, https://ror.org/02t274463 University of California, Santa Barbara United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89929.sa1](https://doi.org/10.7554/eLife.89929.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A neuromorphic model of active vision reveals how spatio-temporal encoding in lobula neurons can aid pattern recognition in bees" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Claude Desplan as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

The reviewers agree that the model developed by the authors tackles an important problem in machine learning and visual neuroscience. The model is based on visual scanning, which represents a novel and exciting phenomenology in the bee. Unfortunately, the main conclusions of the work must be watered down until the authors demonstrate that alternative, equally plausible, models of the visual and mushroom body circuits are not sufficient to solve the tasks under consideration. We believe that the manuscript can be a valuable and important contribution to the field if the following weaknesses are thoroughly addressed.

1) The neural circuitry underlying the model does not adequately integrate the wealth of Drosophila connectome data that has been published during the past 10 years. While the model is definitely bio-inspired, layers of its architecture are built very differently from the connectivity of real insect brains. As a result, many features of the model's architecture appear to be arbitrary. Clarifications should be provided about circuit-function relationships of the bee MB versus the Drosophila MB, and their implications on the model.

2) Given the repeated claims that the authors present the "minimal circuit" required for the visual tasks explored, the work ought to rigorously and systematically assess the necessity and sufficiency of the different components included in the circuitry of the model. In particular, could a simpler learning rule be sufficient to explain discrimination? In what sense is the presented circuit "minimal"? Varying the number of lobula neurons of the model is a good first step, but the same should be done for other components of the model.

3) The presentation of model's results and its interpretation should explain the successes and failures of the model in reproducing the actual behavior. It should include a more in-depth comparison of the performances of the model and real bees.

4) The description of the methodology is incomplete, which prevents a proper interpretation of the model's results.

Reviewer #1 (Recommendations for the authors):

The introduction talks about natural scenes such that their specific features are critical to neural processing and pattern recognition. However, the manuscript does not thoroughly assess if the model is particularly suited for handling natural scenes. To demonstrate this, it appears to require using non-natural images for non-associative learning and comparing the performance with the model trained with natural scenes. Otherwise, I would recommend rephrasing the introduction.

Line 217: why does restricting the scan field improve the performance dramatically? This may be intuitively reasonable, but it would be nice to have an explicit explanation based on the model's structure.

Discussion:

The insect lobula is not necessarily only composed of wide-field neurons. It would be nice to have some discussion about how other types of neurons, such as small object-detecting neurons, could contribute to the same visual task.

Reviewer #2 (Recommendations for the authors):

Line 1 – title – is it really substantiated in this paper that the spatiotemporal lobula encoding "aids" pattern recognition? Relative to what? Can these tasks not be solved by models such as that in Ardin et al. (2016) that use low resolution pixel values as input to the KC and associate the corresponding sparse code with the MBON for selected images?

Line 6 – abstract – in what sense is the presented circuit 'minimal'? The paper explores reducing the number of lobula neurons, but not any other reduction in complexity.

Line 11 – the alignment to neurobiological observations does not seem all that compelling. It is already known that using non-associative adaptive processes that favour sparse coding, trained with natural images, produces output that resembles complex cell receptive fields. Does this study produce results that are notably more aligned with data from insect lobula recordings, for example?

Line 40 – the "cognitive feats in visual learning" explored in this paper do not seem all that "remarkable".

Lines 52-72 This passage seems to interchangeably use three different senses of 'adaptive': adaptive in the sense of ongoing change in neurons due to the experience of the individual (lines 55-57); adaptive in the sense of being evolutionarily well adapted (lines 57-59); and adaptive in the sense of being versatile and robust (lines 59-61). It would be helpful to keep these differences clear, especially as the claim in this paper is that adaption in the first sense is needed to support adaption in the last sense.

Lines 84 and 92-93 It is not clear why it is stated that sampling "builds up a representation/picture of the environment". Indeed the authors' own work here and previously clearly demonstrates how active sampling can be used to solve visual problems without "building up" a picture.

Line 99 – This is an explicit claim that the paper explores "the necessary and minimally sufficient circuit". However, the paper does not demonstrate necessity or minimality of the circuit elements.

Line 104 – again a claim that the lobula encoding used here is "necessary".

Line 110 – here and later it is claimed the lobula representation is "efficient" but efficiency is never explicitly defined or shown.

Lines 115-116 It seems extremely strange to cite no papers later than 2012 for "neural mechanisms of associative learning in insect brains".

116-117 "visual flight dynamics" in this paper are hugely simplified to a five-step constant speed horizontal scan, so their influence on the model seems overstated here.

121-122 another list of citations going no later than 2013, in an area of very active research.

Line 143 is there "recurrent neural connectivity" between photoreceptors and the lamina (in the model or reality)?

147-148 If I have understood this correctly, the connectivity between medulla and lobula is fixed in advance to be exactly five inputs, arranged in space, and with delay times, to match the standard scanning process used in these experiments. So it assumes the movement of the bee is known? This seems a very arbitrary wiring, is there any evidence to support it? Possibly I have misunderstood but if the spatial extent and timing of these connections is actually created through the non-associative adaptation process, then this has not been well explained in the paper (including the methods).

Figure 1 caption – is it correct that there are random connections (not all-to-one connections) from KCs to the single MBON? Or is the meaning here that the connections have initial random weights? Please clarify.

Figure 2 (and 3) it would be nice to include (where possible) data from actual bee behaviour – how well do they perform relative to the model?

Figure 2 I assume the paired columns in C are similar to those in D, I.e. showing the result if the positive training is to one symbol or the other. If so, it would help to have the same pattern and legend in C.

210-212 I find it mystifying why this circuit should be unable to do the discrimination task when the whole pattern is scanned. Do the lobula neuron responses look the same for both stimuli in this case? Why? Isn't this a significant weakness for the model – that some types of (rather simple) patterns cannot be learned? Frankly, this is much more striking than the fact that the face stimuli can be learned. Please discuss.

Figure 3B the text says the test cases were "a novel grating and a single bar" but the picture appears to show a grating pair that were used in training.

Also, Figure 3, the caption says "except for (A) all simulations were conducted at the default distance …etc." so what was used for A, and why not the default?

Line 241-242 it seems like an overinterpretation of these very mixed results to say "the model was able to extract more than a single feature during its scan of the pattern".

Line 261 and following, there are several claims here that the lobula encoding is efficient. But how is efficiency defined and measured here? Similarly, line 282-284 says the representation is 'decorrelated and sparse' but the only evidence provided seems to be that in example 4B, only a few lobula neurons have high activity.

309-310 If variability between lobula neurons is reduced with fewer neurons, doesn't that argue against the claim that the adaptive process makes them 'decorrelated and sparse'?

See my public review for comments on the claims made in the Discussion that I believe to be insufficiently supported.

Reviewer #3 (Recommendations for the authors):

I believe that this very interesting manuscript would benefit greatly from a more in-depth consideration of the terminology and a clearer description of the model and the methods.

I will provide here some more specific points. Below that are the in-line comments.

General notes:

It can be confusing to show the whole pattern when the actual input to the network is only a part of it. A suggestion would be to show, in the graphs, only the actual input to the network.

Should the model architecture used for the results be specified earlier? First mention of number of neurons in lobula is at line 306 (maybe give a name/code to the model variants and refer to those in the method section)

The videos showing the evolution of the receptive fields over the training steps are appreciated, and they could benefit by including a title that describes what is being watched (similar to the caption for images). Possibly, also report the number of training examples over the total of training examples, to show how the receptive fields evolve over time (e.g. Video 5).

Methodology:

In general, the methodology is described somewhat sparsely. Some crucial steps and details are not reported fully, and the full mathematical model of the network is not immediately clear. This is a pity, as it affects the interpretation and may undermine the meaningfulness of the results.

The authors specify that the model considers only green photoreceptors. It is unclear whether this is obtained by processing only the green channel of an original RGB image or by other means.

Lines 488-489. The mathematical notation does not look coherent. Does $A_0$ refer to the $a$ in $f(x; a, b)$? Also, it is not clear whether $A_0$ and the other parameters of the sigmoid activation function ($m$ and $b$) have fixed values or are parametrized and learned. The reviewer assumes they are fixed. Finally, it can be slightly confusing what does $r_p$ represent in the equation. I assume it represents the activity of one green photoreceptor $p$, and that $P$ represents the total amount of photoreceptors (pixels in the image) considered as input to one lamina neuron (as such, P=9).

Line 486-489. The tiling of the receptive field of each Lamina unit is not specified. Given the reported numbers (of pixels and units), the reviewer assumes that the tiling is formed by 625 squares of 3x3 pixels, each adjacent but non-overlapping with the others.

It is not written how the output of each photoreceptor ($r_p$) is obtained from the input image, nor whether it is a continuous or discrete value.

The superscripts are never mentioned explicitly, and the reader is left to infer that they refer to the different components of the network architecture (e.g., $La$ = Lamina). Albeit not critical, this could become an issue when considering that other parts of the mathematical notation are also not detailed, leaving possibly too much room for interpretation.

Line 500-501. What is the parameter $\λ$ of the Poisson distribution used to generate the noise in the activation?

The topology of connection from Lamina units to Medulla units is unclear to this reviewer. Lines 505-507 specify that Medulla units have a small (receptive) field, each one being activated by a different region of the image patch. From Figure 1B, the image patch seems to be one full 75x75 frame. The manuscript, however, does not report what is the small field (selected from this patch) to which one Medulla unit is said to respond. The total number of Medulla units also seems not to be reported.

The topology of connections from Medulla units to Lobula units is unclear to this reviewer. Lines 503-505 state that a total of M Medulla units is connected to each Lobula unit. However, the Methods do not describe how these M units are selected from those in the Medulla. Are they adjacent to each other? If so, in what order is the temporal delay applied?

It is not clear whether, when observing half or a corner of a pattern, the amount of Medulla units changes to reflect a lower number of pixels in the image, or the original image is enlarged to keep the current network configuration, changing the scale of the observed features, or neither of the above. The lack of clarity about the topology of connections from Lamina to Medulla and from Medulla to Lobula makes it difficult to interpret what happens in this case.

It is not reported from which distribution is the random connectivity matrix S initialized, nor whether it is randomly reinitialized for each simulated bee.

It is not reported how the laterally inhibitory connections in the lobula, Q, mathematically affects the neurons activity.

It is not reported over which window of time is the mean firing rate computed, nor if it computed as a static condition of the leaky integrate-and-fire model assuming a fixed value of activity in the input layer (Medulla) during the current training step.

When the receptive fields are shown in figures, the weights seem to be clipped in the range [-1, +1]. However, no clipping is reported in the Methods.

A formal description of all the initialization, training, and testing steps is not reported, and it's left to be inferred from different parts of the manuscript.

Discussion

The Discussion section of this work is somewhat lacking when it comes to analyzing the variation of performance of the proposed network over the whole spectrum of tested conditions.

It is the belief of this reviewer that the underperformance of the network in those cases, and with some type of patterns (even in the best-performing scenario, such as with the gratings in Figure 3D), could be attributed to the receptive fields that are formed during the non-associative learning procedure. Specifically, the receptive fields shown seem to all be responsive to a specific orientation and velocity. However, they are all "global" (or "large" scale), in the sense that they all have only one big contiguous area of positive weights along one big contiguous area of negative weights.

The question that naturally arises is whether the non-associative learning employed here can produce more refined patterns in the receptive fields, or whether it can learn to be sensitive over different scales of features by combining (at the level of the lobula) different large-scale receptive fields in non-trivial ways. Also, why do patterns learned, when scanning whole images, perform best when not applied to a whole image.

The reviewer acknowledges the difficulty in showing the receptive fields when they include both a spatial and temporal component, and as such also that this sensitivity on a varying scale could already be present in the network, as a combination of larger scale receptive fields (albeit the results with different speeds and different distances from the image seems to suggest some specificity in the scale of visual feature that the network can identify). This could warrant a more in-depth study of the performance of the proposed network architecture when varying the training set and training conditions (e.g., speed).

In-Line comments

L134-136: but is the scanning order selected by the model, or is it fixed? At the moment it seems to be implied that the 5 frames are given. Is there reason to assume this is the optimal order? Is there any optimal order? P.S. I see that this is touched upon below. See comment to L210-219

L185-188: Videos 1 and 2 are missing. I assume they are present in MaBouDi et al. 2021, but if they are referenced here with this indication they should be included. Alternatively, you could add in the text a general reference to the previous paper.

L196-197: writing here "during the initial experiment" seems to refer to the first experiment you are doing in this paper. Instead, it seems you want to refer to your previous paper. This should be made more clear.

Figure 2B – In the caption, there seem to be typos on what is rewarding and what is punishing.

200-201 – This wording may be interpreted as the model having active control, which is however not the case.

L201-219: statistical analysis should be done and reported. In an attempt to comparing this model with living animals, I believe every step should be taken to follow the same procedure. How many simulated bees have been tested in the + vs X task? Are they 20 per shape or 20 per scanning pattern? Is the data collected after how many visits? Reporting percentage is I believe insufficient, and a binomial test against chance level should be performed. This is the case for all experiments in this paper.

Figure 2B: is this SD or CI?

L210-219: the authors here refer to an initial poor performance. In figure 2C, is this the last two bars of the graph? This should be made clear.

Overall, the experiments here described aimed at finding the best scanning procedure, but I am not sure if how this was evaluated is appropriate. First, how is the training on natural images organized? Are they all scanned in the bottom half, left to right? If that is the case, the highest efficiency of lower-half scanning may be linked to the highest similarity to training, not to the real efficiency of the technique, and it would as such suggest low generalizability of the model. If instead training is repeated for all experiments following that presentation pattern, and thus the scanning procedure has an effect of learning effectiveness, this may be a property of this network, but not necessarily of living bees (as L216 somewhat suggests). It could in fact be a self-fulfilling prophecy (behavioral experiments suggest the need for scanning, the network is designed with a recurrent layer to enable shape reconstruction, and the network is most effective with scanning).

If you want to suggest that scanning from the bottom left is indeed more effective, you need to also include conditions other than the confirmatory one. These could be scanning right to left, or scanning left to right in the top half, or scanning top to bottom, or even diagonally (which I suspect are going to produce identical results). As of now, the experimental conditions only allow us to conclude that scanning sections is more effective than seeing the whole image, which again is to me included as a property of the network. Also, I may be wrong about this, but bees visual field is not centered frontally on the animal, but points upward (https://www.researchgate.net/publication/326717773_Bumblebee_visual_allometry_results_in_locally_improved_resolution_and_globally_improved_sensitivity). Being this the case, a bee moving across the bottom of a stimulus wouldn't it actually be looking at it fully, with the visual field centered on the horizontal symmetry line?

A similar reasoning should be made for scanning speed. Velocity is tangled with stimulus size. 0.1m/s may work best with this size but will change drastically depending on how much of the stimulus occupies the virtual bee visual field.

I want to point out that none of these points are detrimental to the effectiveness of the model itself, which seems to present good performances. But if claims want to be made about the best scanning strategy, especially if confronted with real animals, these points should be tested and addressed. As of now, we can say that the current model best performs under certain conditions, but we can't generalize the effectiveness of such conditions to be the best for the task, nor the best for bees.

L221-252: I believe also here binomial statistics should be produced. I understand it seems to be redundant for performances nearing 100%, but this becomes more relevant for the 60% and 40% reported in Fig3E. On the same note, specific values should be reported, both for averages and SD.

246-251 – Repetition of a period.

It would be helpful if Figure 3 also reported the real bees data, as taken from the various papers. This would give a sense of how closely the model follows the bees behavior. Of course, bees are more complex and are subject to, among others, motivational effects which will make the choice percentage less clean, but I still think this would be appreciable.

311-312 – "When the model is limited to only four neurons in the lobula, it lacks the capability to encode the entire spatio-temporal structure that is naturally present in the training patterns". This wording seems to suggest that with more neurons it can encode the entire spatio-temporal structure of the training patterns, which may be an overstatement.

L314-316: I agree that these neurons are sufficient for the discrimination task in hand, but I am unsure whether is appropriate to extend this to bees, as the paragraph title implies. Bees have to use the system to respond to much more complex patterns, like photorealistic ones. For example, is 16 neurons still enough for the face discrimination task?

355-356 – It is unclear how the study would suggest a crucial role of movement in the ability to efficiently analyze and encode the environment. In this work, movement of the input pattern is taken as a given condition under which the network is trained, and not as a tool that can be exploited to have an advantage in the encoding and analysis of the pattern itself.

Discussion: In general, I am not fully convinced that your model can say anything about the bees or the optimal performance in general, but should focus on the effectiveness of the model itself. This is because of what I have reported above about how the model performance is at least partially dependent on the model design, and not on how bees actually behave (which is hypothesized)

374-375 – In these lines, it is claimed that the model acts as a linear generative model, however, this is not shown in the results and these generative capabilities are not demonstrated.

487 – Calling $r_l^{La}$ as "the output of one lamina neuron" instead of "one lamina neuron" could improve clarity.

498 – I have not clear what "however" refers to, in this context

498 – Similarly. Rewording "the input of the m −the medulla neuron is calculated" to something like "the input to the $m$-th medulla neuron, $I_m{Me}$, is calculated as"

506-507 – Could reference to Figure 3B be a typo?

528-530 "At each step of training, a set of five patches with size 75x75 pixels, selected by shifting 15 pixels over the image from the left or right or the reverse orientation (Figures1B, 2A), was considered as the input of the model." This wording could be a bit confusing, especially as, coincidentally, 15*5=75. It could be improved to make it clear that one input to the network is (a concatenation?) of 5 patches of 75x75 pixels each, obtained by shifting a window of 75x75 pixels by 15 pixels, 5 times (if this is actually the case).

Reviewer #1 (Recommendations for the authors):

The revised manuscript incorporates my comments well. The added analysis better clarified that local visual features are essential for learning using this scanning strategy. The description was also significantly revised, and the claim sounds reasonable now. I do not have further comments.
