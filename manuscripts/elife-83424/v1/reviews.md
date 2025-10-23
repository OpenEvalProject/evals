# Peer review - Round 1

Editors:
- Michael Beyeler, https://ror.org/02t274463 University of California, Santa Barbara United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83424.sa0](https://doi.org/10.7554/eLife.83424.sa0)

This valuable study proposes a new algorithm for determining the electrical stimulation delivered through a sensory-neural/retinal implant with the aim of improving the perceptual benefit to implant users. The evidence supporting the conclusions is solid, with additional experiments and analyses submitted during the revision having significantly strengthened the study. The work will be of interest to both neuroscientists and neuroengineers.


---

# Peer review - Round 1

Editors:
- Michael Beyeler, https://ror.org/02t274463 University of California, Santa Barbara United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83424.sa1](https://doi.org/10.7554/eLife.83424.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Precise control of neural activity using temporally dithered and spatially multiplexed electrical stimulation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Mohit Shivdasani (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Included here is a brief evaluation summary and list of revisions the reviewers and review editor deem essential for the authors to address. The public summaries and full, individual reviewers' recommendations for the authors are also appended below. The authors are advised to address the public summaries briefly, and the individual recommendations in a detailed, point-by-point manner.

As you will be able to read below, reviewers appreciated the importance of the study and its potentially broad interest. The approach to formulating the problem of choosing electrical stimuli for visual prostheses as a data-driven optimization problem holds promise for several sensory-neural prostheses. The writing was relatively clear, the figures appropriate, and the methods mostly rigorous. However, reviewers raised concerns with regard to some of the claims made, particularly as it pertains to the full greedy, dithering, multiplexed algorithm and its potential to greatly improve the quality of vision delivered by a retinal implant. The key points that need to be addressed can be summarized as follows:

1) Please provide more experimental data (specifically: reconstructed images and reconstruction errors) to substantiate the claim that the algorithm can improve the quality of vision in an ex vivo setting. The main evidence that is presented about the quality of vision that might be achieved is a computer simulation; that is, the image reconstructions and reconstruction errors given in Figures 2 & 3 with the dithered, but not multiplexed version of the algorithm. However, the same cannot be said about the ex vivo experiment. While the outputs of the dithered & multiplex version were indeed applied to ex vivo retina, the output is all simulated and no experimental validation data is presented. However, it is possible that the experimentally observed retinal output might differ from (the assumption of) a linear sum of dictionary elements. All reviewers agreed that if the authors could report on the results of the experiments in which algorithmic stimulation is applied to ex vivo retina, and report this in terms of image reconstructions and reconstruction error, this would greatly improve the strength of evidence.

2) Please expand the discussion on the theoretical assumptions regarding visual processing in the brain and the perception of phosphenes through electrical stimulation that the study is based on, as it may limit the translational impact of the work. All reviewers agreed that the study relies on several significant assumptions about neural coding in the retina, the visual brain, and interactions between electrodes, some of which have been recently challenged. This includes the assumption that neural coding in the retina is solely based on a firing-rate code, that visual perception is solely based on the number of spikes within a slow temporal integration window, and that non-simultaneous interleaved electrical stimulation does not lead to neural interactions. At a minimum, the authors should address these limitations clearly in their Discussion, and comment on the potential implications of the failure of these assumptions on their algorithm performance.

3) Please clarify which figures/results are from simulations and which are from experimental data.

Reviewer #1:

Shah et al. propose an algorithm to precisely control RGC activation using electrical stimulation, using temporal dithering, and spatial multiplexing. The main assumption is that the brain has perceptual integration windows, during which a visual percept can be built up by stimulating single (or small groups of) neurons in rapid succession. Which electrodes to stimulate to achieve a desired percept is dictated by a dictionary of stimulation patterns. The authors demonstrate the effectiveness of their method on ex vivo recordings of ON and OFF parasol cells.

The biggest strengths of the study are the theoretical contributions and the experimental recordings used to demonstrate the effectiveness of their algorithm. The thinking follows a number of recent efforts in the field to think about visual prosthetic stimulation as a closed-loop data-driven optimization problem. This may have benefits over other open-loop stimulation techniques.

However, the biggest weakness of the study is a reliance on a number of controversial assumptions about the neural code of vision. The first is the existence of a slow temporal integration window during which the brain cannot distinguish the order of stimuli presented and/or sums up RGC activity to decode the presented stimulus. The paper presents only limited (and dated) evidence for this. Second, the assumption of a Bernoulli distribution is at the very least limiting, as neurons may respond with multiple spikes to a stimulation pattern and some spatial features may be encoded by the relative timing of spikes across neurons. Third, even though the temporal dithering may avoid electrical crosstalk, there may still be neuronal crosstalk on longer timescales, thus challenging the independence assumption. Extending the delay between stimuli in order to avoid neuronal crosstalk may severely limit the utility of the proposed algorithm since it would cap the number of stimuli that could be delivered in one of the assumed temporal integration windows.

Even if the assumptions hold, the presented evidence of the ex vivo recordings would need to provide some additional detail before the practical utility of the proposed algorithm could be judged accordingly. Although the study reports reconstruction errors and example reconstructed images for the simulation experiment, the same cannot be said about the ex vivo experiment. In addition, real-world implementation of the algorithm would presumably include not just stimulus delivery but also in-the-loop stimulus decoding, and it is not clear how quickly that could be done. Lastly, the linear filters would have to be estimated in a degenerated retina, where one could not rely on responses to light stimuli. The paper notes that this could be done by considering the spontaneous activity of cells – I can see how that could allow you to distinguish between ON and OFF cells, for instance, but it is not clear to me how that would allow you to determine the linear filter for each cell. For those reasons, it is somewhat hard to judge the practical utility and potential significance of the proposed algorithm.

Recommendations for the authors:

Methods: The assumption of a Bernoulli distribution seems limiting, as neurons may respond with more than one spike. The decoding overall does not take into account that (at least some) visual information may be encoded in the relative timing of spikes across neurons.

p.7 algorithm section: The major underlying assumption here is that temporally dithered stimuli will be linearly integrated by the retina. Dithering may avoid electrical crosstalk, but neurons may exhibit "crosstalk" on longer timescales due to the relatively slow (as compared to electrical stimulation) temporal dynamics of ion channels. The authors seem to be aware of that as they say "presumably" and mention the idea of a perceptual integration window. But it would have been great to refer to some existing (and more recent) literature on the topic (if any).

p.8 algorithm section: Greedy algorithms are often not guaranteed to find the global optimum. Can the authors show that their proposed algorithm does not get stuck in local optima? How is the final optimization performed at time t, given the dictionary elements?

Ex vivo experiments: It would be helpful to see reconstruction errors and reconstructed images, similar to how they were presented for the simulation study. How long does the decoding/stimulus selection take? Presumably, the dictionary is quite large given the number of neurons. Is there a more efficient way to search the dictionary than O(N)? Or how is that done, and how quickly could it be done in a real-world implementation? I am concerned that this step may severely limit the number of stimuli that could be realistically delivered in a temporal integration window.

In all equations, it would help if the authors used proper formatting to label vectors vs. matrices. For example, is the stimulus reconstruction filter in Eq. 1 a vector and the product is elementwise? What is the size of (and what are the rows/columns in) D on page 8? Etc.

Reviewer #2:

This study proposes a new algorithm for determining the electrical stimulation delivered through a sensory neural implant with the aim of improving the perceptual benefit to implant users. The algorithm is evaluated using data from an ex vivo prototype of a retinal prosthesis to computer-simulate the retinal responses expected from applying the algorithm and later by applying stimuli from the full temporally dithered, spatially multiplex algorithm to ex vivo retina.

Presently, stimulation algorithms used clinically are calibrated using limited perceptual data from the user. In contrast, the proposed algorithm uses detailed measurements of retinal responses to electrical stimulation to optimize the stimulation. This is achieved by minimizing the error between a target image and a version of that image reconstructed from the evoked response that is predicted by the algorithm based on the detailed measurements. The use of a data-driven, optimization approach is similar to several other recently proposed neural stimulation algorithms (which are not cited by the study). The distinguishing feature of the algorithm proposed in this study is that it seeks to stimulate in a way that minimizes the interactions between electrodes that can occur when stimulating neural responses. This avoids the need for the algorithm to account for such interactions.

Overall, the main advantage of the proposed approach is that it frames the problem of how to deliver perceptually beneficial electrical stimulation with an implant as a closed-loop/data-driven optimization problem. This has the potential to improve over presently used open-loop strategies. It then provides an algorithm for solving this optimization problem to a good approximation. Applying the algorithm using data recorded from ex vivo retina with a prototype implant is a strength. However, the evaluation of the efficacy of the algorithm is limited. In the first instance, it is limited to computer simulation of the retinal response for the version of the algorithm that uses just temporal dithering. While this analysis supports the conclusion that the proposed algorithm could provide improved visual perception relative to the clinical open-loop strategy, much stronger evidence would be provided by applying the optimal stimuli from the proposed algorithm directly to the ex vivo retinal preparation and measuring the retinal response. This approach to testing the algorithm directly to the ex vivo retina is done for the full version of the algorithm that combines spatial multiplexing with temporal dithering. However, in contrast to simulated results, the study does not report on the reconstructed images that result from applying the algorithm to ex vivo retina, nor on the reconstruction errors. This makes it difficult to evaluate the efficacy of the algorithm.

Section: Introduction.

The motivation for using a temporally dithered, spatially multiplexed algorithm to optimize stimulation stems from the desire to minimize the interactions caused by simultaneous stimulation of the electrodes in evoking a neural response. While this is an important strategy to investigate, the interactions are not typically as "complex" as claimed in the manuscript. Indeed, previous studies in several labs (including the Chichilnisky lab) show that these interactions can typically be described by a linear, weighted sum of the electrode currents followed by a simple static nonlinearity to predict the probability of spiking (a small minority of retinal ganglion cells require more complex nonlinear descriptions) [1 -3]. This model and others have been the basis for alternative data-driven, closed-loop stimulation strategies that optimize the stimulation in a way that seeks to take advantage of the interactions between electrodes to improve the spatial resolution of evoked retinal activity through "current steering".

Section: Greedy temporal dithering to replicate neural code.

Data-driven optimization: The data required for the proposed algorithm is of two types. An exhaustive dictionary of response probabilities to single electrode stimulation across all current amplitudes, and a set of responses used to reconstruct the target image from the predicted response to electrical stimulation. For the latter, reconstruction of the image is achieved by applying linear filters to the predicted response. In the study, these linear filters were derived from cells' receptive fields, obtained by measured responses in the retina to light stimulation. It is noted that this would not be possible in a clinical implant, as the retina is degenerate. However, it is not clear how a set of filters would be obtained in this case. The authors mention that distinct cell types can be identified from spontaneous activity. However, this does not explain how receptive field size and location would be estimated in this situation.

The reconstruction of the image is achieved through linear filtering with a matrix A, with columns, A_j, that are the (scaled) receptive field filters (Eq. 1). However, this is only correct if the receptive field filters of the different cells are orthogonal, i.e. the inner product of each pair of receptive fields is zero. More generally, appropriate linear filtering should be performed by applying the pseudo inverse of the transpose of A. This is because the retinal spike rates are being approximated as the inner product of the receptive field and the image (A_j transposed, matrix-multiplied by the image vector), half-wave rectified. For the receptive fields of ON and OFF parasol cells given in the study, it appears that the receptive fields are approximately orthogonal for the two separate populations due to the non-overlapping tiling of the visual field by each population (e.g. Figure 2). However, it is not clear whether this situation would prevail in the blind retina, as the filters have not been specified in the case.

The greedy optimization algorithm is insufficiently explained in the Methods, including the following points:

• A derivation justifying splitting the objective function into the terms due to the mean and variance is required.

• The terminology for the terms tr(var(A R_i)) is not clearly explained. I assume it is the matrix trace of the covariance matrix of the random variable A R_i.

• The assumption of a Bernoulli random variable for the response, i.e. 1 or 0 spikes, is limiting, given there may be multiple spikes in response to electrical stimulation, especially for activation via the retinal network.

• The expression that was derived for the term tr(var(A R_i)) in the case of Bernoulli random variables should be given.

• It is not explained how the algorithm performs the final optimization at time step t, given elements in a restricted dictionary D_t.

Section: Greedy temporal dithering outperforms open loop methods.

The image reconstruction shown in Figure 2 uses 500, 3000, and 10000 electrical stimuli (shown in A, B and C respectively). However, these are unrealistically large numbers of stimuli: given the temporal perceptual window of 50 ms, mentioned in the Introduction as the time over which retinal responses would be perceptually integrated, and the pulse duration of 0.15 ms used in the study, a maximum of 333 stimuli could be applied during the window. Consequently, the use of 3000 and 10,000 electrical stimuli in the simulations provides unrealistic estimates of the degree to which the image can be reconstructed.

A full comparison of the proposed greedy, closed-loop algorithm to the conventional open-loop algorithm is difficult to evaluate based on the results presented. First, the number of electrical stimuli applied in making the comparison (Figure 3H) is not given. However, it seems likely, given the data in Figure 3G that an unrealistically large 10,000 stimuli were used. If instead a realistic 300-400 stimuli were used there may be little difference between the greedy-closed loop algorithm and the conventional open-loop algorithm.

A second limitation is that, in this subsection, the greedy, closed-loop algorithm appears to have only been tested in simulation. E.g. "For random checkerboard visual stimulus targets, the greedy dithering stimulation sequence was calculated, neural responses were sampled using measured response probabilities evoked by the individual selected stimuli, and then the target image was linearly reconstructed from these responses." Given that all the relevant data required to run the algorithm for the ex vivo retina and implant prototype had been collected during the experiment, it is unclear why the algorithm was not applied to test it by directly measuring responses to the algorithm's stimulation. This would have tested a critical assumption of the greedy-temporal dithering algorithm: that the responses to successive stimuli are statistically independent. Instead, the simulation assumes this to be the case.

A third limitation is that the reconstructed image for the conventional open-loop algorithm does not resemble the phosphene images reported by most retinal implant users. Most implant users report predominantly bright, rather than dark, localized phosphenes [4]. The open-loop reconstruction shown in Figure 3d appears to be largely a gray averaging of light and dark phosphenes, likely due to the linear reconstruction method used.

Some details of the implementation of the open-loop strategy are unclear including:

• How the area that was "near" the electrode was selected when calculating the intensity of the visual stimulus.

• How the temporal sequence of the electrodes was chosen. It seems that the open-loop strategy is also likely, temporally dithered, but without the benefit of data-driven optimization.

Section: Greedy temporal dithering is nearly optimal given the interface constraints.

The comparison of the greedy, closed-loop approximately optimal algorithm to truly optimal algorithms is an important comparison in principle. However, again it is not clear if a realistic number of stimulation pulses were used in performing this comparison (i.e. < 400).

Some details of the implementation of the optimal comparison strategy are unclear including:

• The meaning and purpose of the term V^T w in the objective function.

• Whether w>=0 was required after the integer requirement was relaxed in the optimization.

Section: Spatial multiplexing for fitting multiple stimuli in a visual integration window.

The idea to use spatial multiplexing of stimuli to overcome the limitation in the number of stimuli that can be delivered during a perceptual temporal window is a good idea to investigate. The aim is to choose stimuli on different electrodes that affect neural response independently. However, the initial formulation of what is meant by independence is not correct. This is stated as: "For independence to hold, the following condition must be met: if p1 is the activation probability of a given cell with stimulation on electrode 1, and p2 is the activation probability of the same cell with electrode 2, then the activation probability with simultaneous stimulation must be p1+p2." That this is incorrect can be seen because this formulation could give a probability greater than 1. However, the subsequent description of what is actually implemented appears correct. A general, in-principle way of describing what independence means is that if p1 is the probability of stimulating one cell with electrode 1 and p2 is the probability of stimulating a different cell with electrode 2, then the probability of stimulating both cell 1 and cell 2 using simultaneous stimulation with electrodes 1 and 2 is the product of those probabilities, p1.p2.

In contrast to greedy dithering alone, the use of both greedy dithering and spatial multiplexing was tested in a closed-loop experiment by recording responses to stimuli produced by the algorithm. However, the paper does not report on the image reconstructions, nor the reconstruction errors that were obtained.

Instead, the reported results of the greedy dithering-plus-multiplexing (Figure 4) show only that it is possible to select eight multiplexed electrodes with sufficient separation to ensure minimal interference. This could potentially increase the number of electrodes stimulated with the greedy, closed-loop algorithm by a factor of 8, bringing it to around 2,700 stimuli. This is closer to the 3000 electrode stimulations used in Figure 2b that gave errors that approached the asymptotic limit. However, the results in Figure 4 were obtained using stimulation every 2 ms, not every 0.15 ms (= pulse duration). With this limitation, this reduces the number of electrode stimuli to 200 in a 50 ms perceptual window, which again is not likely to give a good reconstruction error according to the simulations.

Other Results sections.

The sections on hardware constraints, naturalistic viewing conditions, and the use of perceptual similarity measures make useful observations about the potential benefits of the optimization framework for algorithmically determining the electrical stimulation.

Discussion.

The discussion covers many important points well. Regarding the translational potential, I would agree that an important point is "First, new surgical methods must be developed to implant a tiny chip on the surface of the retina with stable contact." But add that it must also be in extremely close contact for retinal ganglion cell spikes to be recorded. Further, a very high-density array (~ 60 μm pitch) and associated electronics for both stimulation and recording must be developed which is suitable in size, form factor, and power consumption for clinical use.

References

[1] Jepson, L. H., Hottowy, P., Mathieson, K., Gunning, D. E., Dąbrowski, W., Litke, A. M., & Chichilnisky, E. J. (2014). Spatially patterned electrical stimulation to enhance resolution of retinal prostheses. Journal of Neuroscience, 34(14), 4871-4881.

[2] Lorach, H., Goetz, G., Smith, R., Lei, X., Mandel, Y., Kamins, T.,.… & Palanker, D. (2015). Photovoltaic restoration of sight with high visual acuity. Nature medicine, 21(5), 476-482.

[3] Maturana, M. I., Apollo, N. V., Hadjinicolaou, A. E., Garrett, D. J., Cloherty, S. L., Kameneva, T.,.… & Meffin, H. (2016). A simple and accurate model to predict responses to multi-electrode stimulation in the retina. PLoS Computational Biology, 12(4), e1004849.

[4] Humayun, M. S., Weiland, J. D., Fujii, G. Y., Greenberg, R., Williamson, R., Little, J., et al. (2003) Visual perception in a blind subject with a chronic microelectronic retinal prosthesis. Vision Research, 43, (2573-2581).

Recommendations for the authors:

Overall, it appears that the approach may offer some important benefits for sensory-neural implant users. However, the reporting of results is not sufficiently complete to draw strong conclusions about the potential benefits. In addition to the Public Review, I have some related suggestions below.

Reconstruction model in the blind retina.

• It would be helpful to provide more detail about how the image reconstruction would work in the blind retinas, beyond what is mentioned regarding the identification of ON and OFF retinal ganglion cell type. How would the size and location of receptive fields be estimated?

• The assumptions underlying the reconstruction model should be described, especially with respect to the orthogonality of the receptive field filters. It would be helpful to describe an approach in the methods that do not rely on this assumption, as I describe in my public comments.

Greed optimization algorithm: There are several aspects of this that could be better explained. These include:

• A derivation justifying splitting the objective function into the terms due to the mean and variance is required.

• The terminology for the terms tr(var(A R_i)) is not clearly explained. I assume it is the matrix trace of the covariance matrix of the random variable A R_i.

• The assumption of a Bernoulli random variable, i.e. 1 or 0 spikes, is limiting, given there may be multiple spikes in response to electrical stimulation, especially for activation via the retinal network.

• The expression derived for the term tr(var(A R_i)) in the case of Bernoulli random variables should be given.

• It is not explained how the algorithm performs the final optimization at time step t, given elements in a restricted dictionary D_t.

• It is not explained how to determine the time for which recently used dictionary elements are excluded from current use.

Section: Greedy temporal dithering outperforms open loop methods

Regarding the number of single-electrode stimuli used in image reconstruction, it would be better to place the numbers used in the context of what is possible in the perceptual time window. It would recommend using the value of 333 instead of 500, as this corresponds to the number of 0.15 pulses that could be fit into a 50 ms window. The value of 3000 roughly corresponds to what might be achieved with spatial multiplexing. The value of 10,000 corresponds to the upper limit that is achievable through this algorithm.

I think it would be beneficial to make it clearer that the results in Figure 3 are simulated. It would also strengthen the study to perform validation in ex vivo retina to apply the greedy temporal dithering stimuli to the retina and reconstruct the image from the responses. If there is a good reason not to do this, this should be explained.

It would improve the study if a reconstruction algorithm that provides an image with a better match to the perception of phosphenes by retinal implant users was used. If this cannot be done, it should be discussed as a limitation of the study.

It would be helpful to clarify some details of the implementation of the open-loop strategy including:

• How the area that was "near" the electrode was selected when calculating the intensity of the visual stimulus.

• How the temporal sequence of the electrodes was chosen.

Section: Greedy temporal dithering is nearly optimal given the interface constraints

A realistic number of stimulation pulses should be used in performing this comparison e.g. < 400 for the pure temporal dithering or < 3000 for the spatially multiplexed, temporal dithering.

It would be helpful to clarify some details of the implementation of the open-loop strategy including:

• The meaning and purpose of the term V^T.w in the objective function.

• Whether w>=0 was required after the integer requirement was relaxed in the optimization.

Section: Spatial multiplexing for fitting multiple stimuli in a visual integration window

As described in my public review, the description of independence is not correct. I have suggested an alternative description that I believe accords with what was actually implemented.

It was surprising that the results of the validation experiments on ex vivo retina with the spatially multiplexed, temporally dithered algorithm were not reported more thoroughly. It is important to provide figures showing the image reconstruction that was achieved and the statistics for the reconstruction error.

Reviewer #3:

In this study, Shah and colleagues propose an interesting solution to the non-linear interactions caused by simultaneously stimulating multiple electrodes within a retinal implant. Through high-resolution recordings of ON and OFF parasol retinal ganglion cells, the authors demonstrate that a greedy dithering and spatially multiplexed algorithm, which can also work in the presence of saccadic eye movements, is able to faithfully reconstruct images represented by total numbers of spikes in a given time window across multiple retinal ganglion cells. Essentially, Shah and colleagues propose and demonstrate a method to only stimulate single or groups of 8 electrodes at a time from a pre-established dictionary, but then interleave stimulation of multiple electrodes or groups rapidly across the dictionary to additively build an image. Through their very rigorous and elegant ex vivo recordings in 180 ON and OFF parasol cells across four primate retina preparations, the authors compellingly demonstrate that (i) their greedy algorithm performs better than an open loop algorithm, similar to an optimal algorithm considering the interface constraints, and close but not equal to an ideal control using only a single-electrode dictionary; (ii) that groups of electrodes can be simultaneously activated with a high-resolution neural interface without any retinal interactions provided that they are at least 160 μm apart; (iii) that the algorithm performs just as well even with only 50% of the electrodes on the interface and (iv) that the algorithm can work in the presence of saccadic eye movements and performs better when both saccadic and fixational eye movements are made as opposed to saccadic movements alone.

The experimental recordings and performance of the algorithm in various conditions are the biggest strengths of this study and the authors certainly demonstrate that their algorithm can reproduce spiking numbers across an array of cells that resemble closely spiking numbers evoked by visual stimuli for these conditions. In other words, the authors' primary claim that the neural code for visual images in the retina (in the form of spiking numbers) can be faithfully reproduced with electrical stimulation using such an algorithm, is well supported by evidence.

A major weakness in the study however is the reliance of this algorithm on several significant assumptions about neural coding in the retina, neural coding in the visual brain, and interactions between electrodes even with non-simultaneous stimulation. Some of these assumptions have already been highly challenged in several studies in the visual neuroscience field and in studies involving the perception of phosphenes with interleaved stimulation of single electrodes. Therefore, in light of what is currently known about visual encoding and artificial vision, the study whilst showcasing an elegant computational tool perhaps provides only little hope that such an algorithm will actually work in practice to recreate the perception of images with electrical stimulation but instead does lay a foundation for further work to be done with the assessment of future algorithms. The main assumptions that the authors rely on include:

1) That neural coding in the retina is simply based on a number of spikes evoked by populations of cells ignoring any temporal patterns of responses. A plethora of studies has indicated that relative spike timing between groups of retinal ganglion cells for example can encode complex visual features but the greedy algorithm does not aim to mimic these spike timing features.

2) That perception within the brain is solely based on a number of spikes within a slow temporal integration window (the authors cite a 1995 reference for this). Since 1995 though, this has also been challenged, therefore extending the authors' claims of reproducing spike numbers in the retina to reproducing perception in the brain would be contentious.

3) That neural interactions with non-simultaneous interleaved electrical stimulation are absent. There is in silico, electrophysiological and perceptual evidence with retinal implants that interleaving of electrodes still results in neural interactions and that perception with interleaved stimulation with multiple electrodes does not result in a linear summed perception of phosphenes evoked by single electrodes i.e. dictionary elements. Therefore, the algorithm would only work if such interactions are minimal or absent, for example with larger than 0.1 ms intervals between stimulations or more than 160 μm electrode separation. Note, interactions with interleaving also exist with cochlear implants as the current spread is large.

4) That even if the above 3 assumptions were applied and true, the algorithm can faithfully extrapolate to reconstruct moving images at 24 per second. This seems unlikely as presumably the total time required to linearly reconstruct a single static image would extend to many tens or even hundreds of ms given the number of times each dictionary element needs to be accessed to enable reproduction of similar spiking numbers between visual and electrical stimulation, runs in the thousands.

In spite of major reliance on these assumptions, the authors do demonstrate a very useful tool in the form of the greedy algorithm for situations perhaps other than the visual system, where perception with artificial stimulation may be more predictable and interactions with non-simultaneous stimulation may be simpler.

Recommendations for the authors:

It may be possible to address at least some of the limitations in particular (1) and (4) mentioned in the public review. For limitation (1), the authors could try and experiment with their algorithm and reanalyse data to examine if and how well spike timing features (perhaps relative first spike latencies between RGCs or other temporal patterns of spikes) are reproducible. For limitation (4) the authors could at least perform calculations of time taken by the algorithm in each of the situations and targets presented, to examine if these times are realistic.

For limitations (2) and (3), the authors at a minimum should address these clearly in their discussion and the potential implications of the failure of these assumptions on their algorithm performance.

Other things that the authors should consider is including some example raw data from their retinas before and after artifact subtraction in response to both visual targets and their greedy algorithm as a figure.
