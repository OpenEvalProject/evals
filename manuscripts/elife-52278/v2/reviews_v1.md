# Peer review - Round 1

Editors:
- Claude Desplan, New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52278.sa1](https://doi.org/10.7554/eLife.52278.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your paper uses the olfactory circuit of Drosophila to test developmental plasticity and robustness in a stochastic sparse wiring circuit between olfactory projection neurons and Kenyon cells in the mushroom body. This sparse wiring encodes olfactory perception. Your simple, well designed and elegant experiments revealed that there is significant presynaptic developmental plasticity explaining the robustness of sparse wiring. By manipulating cell divisions of either Kenyon cells or projection neurons to increase or decrease their population size and measuring "claws" (their connections), you realized that the number of post-synaptic sites of Kenyon cells is invariant while the number of presynaptic sites of projection neurons changes accordingly.

Decision letter after peer review:

Thank you for submitting your article "Presynaptic developmental plasticity allows robust sparse wiring of the Drosophila mushroom body" for consideration by eLife. Your article has been reviewed by Catherine Dulac as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Bassem A Hassan (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The three reviewers agree about the importance of the work and find the problem and the way it is addressed to be highly significant: The principle of developmental plasticity in presynaptic neurons in this circuit is fascinating and the way you manipulate it is very good!

However, as you will see from the comments, two of the three reviewers have some serious issues with the counting of buttons that are presented in Figure 7. They agree that this is not a trivial task (although others have done so very well, see Leiss, 2009) but they are not convinced by the experimental data that you show and they found it difficult to verify the accuracy of the counting, which is critical to the paper.

Therefore, we would like you to provide more information on how you did the counting and to show precise images with markers indicating what is counted as a bouton, and what is not. In particular, you need to elaborate about how you avoided counting errors across optical sections. Furthermore, the n number is too low to allow statistics and might need to be improved.

Reviewer #1:

The authors examine the rules for wiring the input connections in the mushroom body, what sets the degree of synaptic convergence of PN inputs onto KCs. They address this by manipulating cell divisions of either KC or PN progenitors to increase or decrease population size. Based on measurements of KC claws and calyx cross-section, the number of KC post-synaptic sites appears invariant across conditions, while the number of PN presynapses changes.

There are some important technical points that are not adequately described and may not be adequate to justify the conclusions. Figure 7 is based on a seriously insufficient data set. Without resolving these issues, I am not confident in their results:

1) They quantify the size of the calyx as the maximum cross-sectional area. They should quantify calyx volume instead. There could be large change in calyx volume without changes in max cross-sectional area.

The Materials and methods section description of this should also be clarified. It says: '…identified its [calyx's] largest extent in z, outline it in FIJI…'. Do they mean they found the confocal plane with the widest cross section and calculated the area there? They should use brain-based coordinates (i.e. dorso-ventral/A-P) rather than Z since I don't know how they're scanning the brain. Also, it sounds like they simply measure a diameter and assume the calyx is a circle. If so, that is too crude a measure. They should make a more precise measurement of the 3D boundary of the calyx and calculate volume.

2) It's unclear how they actually counted PN boutons/cell bodies/claws. Again, the Materials and methods section description should be more accurate. It says ' counted every other slice' and 'counted every third slice' How do we know whether there is or isn't overlap between slices? We'd need to know the axial resolution, as well as the distance between slices but these are not reported. As written, it sounds like they made an arbitrary decision to skip counting some slices. It's impossible to tell if they could be double counting or missing many counts.

In Figure 1E the number of PN boutons a little less than 500, which is low compared to published results, Leiss et al., 2009 counted between 780 and 1600 depending on markers used, and Turner et al., 2008 estimated 1165 based on PN labeling. Also, the numbers in Figure 1E don't match their statement of '1000/calyx' on in the Materials and methods section. Can the authors please clarify?

Figure 2B shows examples of how they count the number of KC neuroblasts using the 58F02 driver. However, there are sometimes clusters of green cells that are apparently not counted e.g. left panel shows one big cluster and two smaller ones, second from left shows one cluster at 6'oclock and one at 9o'clock but this is assessed to be only one KC Nb. This needs more explanation. Is the driver not completely KC specific? How did they know that a cluster is made of up KCs and not other cells, especially with the 9 o'clock cluster.

3) The authors must take more measurements of KC odor responses in ablated animals, n=3 is not sufficient for any conclusions. In fact, there are no statistical tests in Figure 7 to support any conclusion.

What does the df/f value shown in e.g. Figure 7C represent? Is it peak df/f during the odor, or area under the curve or what?

It would be far better to show some example plots of df/f versus time (as a simple line plot rather than heatmap). This is a better way for the reader to evaluate the data, in particular to assess movement artefacts. Presenting essentially a single point, as in Figure 7C, can mask experimental issues.

The authors also use an arbitrary threshold to define a response: 20% df/f. This is not particularly well-justified and not standard in the field. In any case, there's no need for a response threshold to analyze these data. A better analysis would be to measure df/f values across the entire set of KCs and plot those distributions for ablated and sham animals. Viewing those two distributions is far more informative than a% response, which apparently ranges from 5-40% by the current criterion, so it's not a very robust measurement anyway. (In fact, in Figure 7D I see a number around 0.5, very high!)

The authors should be more forthcoming in their description of these results. Subsection “Developmental plasticity preserves sparse odor coding despite perturbations to cell populations” says 'variation is similar to previous reports' but the Materials and methods section says that more responses were observed in this study than previous, both referring to Honegger, 2011. The authors should be straightforward about the differences between the observations in both Main Text and Materials and methods section. The analysis suggested above should be adequate support for their claims (with enough n), since they are comparing sham and ablated.

Related to overall quality of these experiments: in Figure 7C are there instances of negative df/f values in the responses? It is hard to tell with the colormap the authors use, but I see it ranges down to -0.5. If so, that should be commented on, since inhibition is rarely seen with GCaMP. The concern is that movement artefacts are likely to give negative df/f values, so that should be ruled out.

Additionally, the high level of responsiveness the authors observe relative to previous work could also be due to movement artefacts giving artificially large df/f values. The authors should analyze some non-odor period of their calcium signals to see if similar response frequencies are observed. And do the same for inhibitory responses (if those are in fact negative values).

Reviewer #2:

The manuscript "Presynaptic developmental plasticity allows robust sparse wiring of the Drosophila mushroom body" by Elkahlah et al., uses various alteration in the ratios of neurons that contribute to the calyx of the Drosophila mushroom body to address how the convergence of combinatorial inputs is established during development. The idea put forth by the authors is that the convergence ratio is set by post-synaptic Kenyon cells-such that Kenyon cells produce relatively invariant numbers of claws, whereas the number of pre-synaptic specializations on Projection Neurons can vary bi-directionally.

I very much like the question and approach described in this manuscript. I especially like that the authors took their analysis all the way to circuit function. However, much of the primary anatomical data is not always convincing. And there are experimental oversights that are either problematic or it is not fully explained why they are not problematic.

Figure 1. The authors variably reduce the number of Kenyon Cell neuroblasts and Projection Neuron neuroblasts using chemical ablation approaches. They show this leads to reduction of Kenyon Cell number and reductions in projection neuron bouton numbers.

Can the authors show projection neuron boutons at higher resolution? I have no idea how they counted the boutons from these images. Much of their argument hinges on their ability to count these structures, so showing this in a convincing way in Figure 1 is important.

Figure 2. In the same manipulation as Figure 1, the authors score for additional phenotypes-In panel F, how do these images allow one to count boutons? The images are too low-resolution to tell, could they be displayed bigger, or without the overlay? I can't tell how the drawings are the right correspond to the images that are shown. Similarly, but more dramatically, for the claws in Figure 2F, especially the bottom panel, I cannot understand how the raw image data gives the authors the schematic that they show at the right. I want to believe their quantified data, but seeing these types of raw data make me question!

Figure 3. The authors knock down Mud to expand the Kenyon Cell neuroblast pool. Figure 3C

-Are the neurons properly specified? Are there molecular markers that could be used confirm neuronal identity? (Similar comments are true for PN data in Figure 4).

-Why is it of no concern to the authors that OK107 drives mud-RNAi in mature neurons?

-Subsection “Olfactory projection neurons increase bouton repertoire as Kenyon cell number increases” of the text says that the MZ19+ boutons are doubled and cites Figure 3C-D. There is no expansion show in Figure 3C-D. What is Figure 3E What are AA and B above the panel on the right? (Similar annotations show elsewhere were confusing).

In Figure 3F, I can't see the claws. These images are not high-enough resolution.

Figure 4. The authors knock down Mud to expand the Projection Neuron neuroblast pool. I cannot understand how the authors counted projection neuron neuroblast number. In Figure 4C, it looks like there is an increased density of boutons?

Figure 5. On the y-axis of 5C and 5G what does "+" mean? Does it mean "both" or "expressing"?

In Figure 5F, what is the residual green?

Do the authors not think it is important to know when they kill cells with DTA?

Reviewer #3:

Elkahlah and colleagues use the PN-MB olfactory circuit in flies to test the limits of developmental plasticity and robustness in a stochastic sparse wiring circuit, where the sparsity of wiring is thought to be critical for encoding.

I truly enjoyed reading this manuscript. The authors perform a number of simple, well designed and elegant experiments to address the question. They find that there is significant presynaptic developmental plasticity explaining the robustness of sparse wiring. I particularly love the approach of testing an idea through clever manipulation of neuronal numbers showing that one does not necessarily need a "molecular mechanism" to understand a basic principle of how the brain is wired.

I have no major comments and think that the paper can be published essentially as it is.
