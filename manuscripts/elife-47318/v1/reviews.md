# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.47318.sa1](https://doi.org/10.7554/eLife.47318.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Vagne et al. study a minimal model for the self-organisation of the Golgi, showing how the traditional models of "vesicular transport" and "cisternal maturation" arise as limiting cases of rich dynamical behaviour in a model of vesicle budding, maturation, fusion that leads to self-organised Golgi structure and cargo transport.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "A minimal self-organization model of the golgi apparatus" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jane Kondev (Reviewer #3).

You will see that the reviewers had differing views on the paper, with two highly critical and one supportive. Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The consensus among the reviewers is that there is no doubt in the potential utility of the kind of minimal model that you have developed, but there were serious questions about the connection between that model and existing data, about the presentation of the model itself, and the structure of the paper.

Reviewer #1:

The Sens group has been developing mathematical models of the Golgi apparatus since 2011 and this paper represents a continuation of this effort. Here, theoretical roles of vesicle budding, maturation and self-organization are used to describe the Golgi's various activities. While the mathematical computations and simulations are not in question, the paper provides no experiments on the Golgi to support or verify the proposed model, and the study fails to incorporate significant features of the Golgi (including the Golgi's unique lipid composition, its tubular-vesicular character, and its ability to form de novo from ER). The paper reads as an exercise for modeling a minimal, self-organizing system that, while attempting to capture some features of organelles (i.e., fusion, budding and maturation), is far removed from the actual complex system comprising the Golgi apparatus. Because the proposed model does not significantly further our understanding of the Golgi apparatus, I cannot support its publication in eLife. Among the concerns of this study is that the model is built on faulty or unproven assumptions regarding the Golgi apparatus (some of these are listed below). It is also worrisome that several papers providing quantitative experimental data detailing Golgi dynamics are never cited, perhaps because these data cannot easily be explained by their model.

1) In their Introduction, the authors state that proteins passing through the Golgi interact with Golgi enzymes in a pre-determined order dictated by the position of the enzyme in the Golgi stack (i.e., cis first and trans last). There is no evidence for this in the literature. Indeed, Farquhar et al., showed many years ago that some trans-acting enzymes are, in fact, in the cis-most cisternae. We also know that carbohydrate processing by Golgi enzymes occurs in a sequential manner whether or not the enzymes are in the ER (i.e., in BFA-treated cells) or Golgi. In both cases, it's substrate availability that dictates the processing events.

2) The authors claim in their Introduction that there are only two major classes of models for explaining the Golgi's activities (i.e., the vesicle transport and maturation models). However, a third model involving tubular continuities and lipid partitioning has also been proposed by the groups of Luini and Lippincott-Schwartz. This third model can account for key experimentally observed features of the Golgi that neither the vesicle transport or maturation models explain. These features include: the finding that secretory cargo rapidly mixes throughout the Golgi stack upon arrival; that different types of cargo exhibit different export kinetics from the Golgi; and that cargo export from the Golgi follows mass action laws. Sens' model cannot account for any these observed features of the Golgi.

3) The authors claim that each membrane patch in their model undergoes maturation from a cis to medial to trans identity. This may have some type of support in yeast (in which membrane patches budding out from the ER clearly “mature” by exchanging cytosolic components over time), but it has no support in mammalian Golgi systems. There, cargo transport through the Golgi stack has never been visualized due to the extremely compact nature of the stack, whose individual cisterna are separated by <20 nm, well below the diffraction limit of imaging.

4) The authors' model predicts that there will be more cis/medial components associated with Golgi structures having low maturation rates, and more trans components for Golgi with high maturation rates. There is no evidence in the literature supporting this prediction. If anything, when one lowers the temperature to slow movement through the Golgi (which in the Sens' model would slow maturation), molecules tend to accumulate at the trans face of the Golgi, the opposite of their prediction.

5) The authors state that cargo flux through the Golgi in yeast is two orders of magnitude faster than in mammalian Golgi. This is unlikely. Bonfanti's paper examining flux of VSVG through the Golgi by EM, which they cite as supporting evidence, is inappropriate for this calculation at many levels- from using repeated temperature shifts to counting a few immuno-gold particles per Golgi (a super crude quantification) to having to compare different fixed cells at different time points. The authors ignore the quantitative live cell imaging data of Golgi export of VSVG-GFP provided by Hirschberg et al., 1998, which measured VSVG export out of the Golgi in real time, with thousands of data points per cell. There, VSVG was shown to be transported out the Golgi at an enormous rate (~7,000 molecules leaving the Golgi per sec) at peak flux after release from the ER. Importantly, the Hirschberg paper also revealed that the amount of VSVG cargo leaving the Golgi is directly correlated with the amount of cargo in the Golgi, with a single rate constant characterizing VSVG efflux kinetics. Sens' paper does not integrate any of these findings into their analysis.

6) The few predictions made by the author's model are not supported by findings in the literature. For example, the authors' state that their model predicts that deletion of Arf1 will decrease the number of Golgi compartments and increase their size. Experimentally, this has already been tested with brefeldin A (which inactivates Arf1) or with Arf1 mutants. Contrary to the Sens' model prediction, when Arf1 is inactivated in cells, the Golgi disappears, being resorbed quickly into the ER with no increase in any Golgi subcompartment. This occurs through retrograde transport back to the ER, a pathway not incorporated into the Sens' model.

I appreciate the efforts made by the Sens group in using modeling to describe self-organizing systems, but their attempt to describe the Golgi apparatus with this approach is missing key aspects of Golgi organization and dynamics. This has resulted in predictions by the model that are counter to experimental data.

Reviewer #2:

Poorly written, hard to understand.

I was excited to read this paper since the work of one of the authors is known to me and I expected an understandable and well-crafted paper. I was rather crestfallen to find a poorly written paper, and one where I could not figure out what the authors were actually doing.

One major concern is that this paper is not at all easy to read. It is either i) not self-contained, or ii) sloppily put together. The authors refer to a "steady state" but do not at any time show that such a state exists, as far as I can see. There is no plot with the time evolution of any quantities being measured. In fact, they admit that there is no steady state, since the size of the system is not constant. They state that "the maximum number of time-steps is typically set to 106 or 107 in order to reach steady state and accumulate enough statistics on all the measured quantities", but that in and of itself is meaningless if one doesn't correctly specify the conditions underlying the measurement.

The paper as a whole is an odd combination of being verbose AND telegraphic at the same time. Echoing my above comment, I do not feel that I am getting enough information, enough detail, despite the verbosity. An example: it takes a long time to get to the point of how heterogeneous compartments can form; they say "this homotypic fusion mechanism (relying on local interactions) allows vesicular transport between compartments of different identities – a process that may be regarded as heterotypic fusion. It merely requires that the receiving compartment contains some membrane patches of identity similar to that of the emitted vesicle". Why not just give the rule, rather than the metaphysical description? It would take up less space!

Does seemingly everything have to be in the Appendix? One can understand page limits, but this is ridiculous. More explanation of the model in the main text would have been very welcome, because in its present form, the paper is extremely difficult to understand.

The question of system size should appear in the main text. As mentioned above, they cannot really keep it constant, so they just adjust the injection rate so it is more or less constant when they change K. They say that they aim for N ~ 300, but the actual system size (sometimes called size, sometimes mass) in the "steady state" changes significantly with K (see Appendix 1—figure 1B and Appendix 4). Moreover, the fluctuations are very large (since no time evolution plot is ever shown, one suspects that they are not really fluctuations…). Of course, the results would be highly dependent on system size, and one gets no justification for their choice of N ~ 300 until the Appendix.

The plots that are shown in the paper are not very useful. They rather tend to obfuscate. Figure 2A intends to show a power law for the size of the compartments with an exponential cutoff, but by plotting a bar diagram (even though it is a log-log scale), it is very difficult to see how well this works. They should plot actual points and a fit, or a parallel line showing an actual power law. In a similar vein, they overuse density plots that are not really quantitative (even in the Appendices). In Figure 2BC, they could at the very least plot some contour lines (perhaps dotted) for the same values that are plotted with a continuous line for the analytical approximation – from the colour map, it is difficult to judge.

Nomenclature:

It is confusing to keep track for reasons that are fully avoidable. For instance, their parameters are (Ki,Kf,Kb,Km): the rates of injection, fusion, budding and maturation. All of them are normalised by Kf, which sets the time unit. But then they define km = Km/Kf and, instead of maintaining the use of lowercase k for the others, they then define K=Kb/Kf, J=Ki/Kf. As if the other problems with the paper weren't enough, now the reader has to remember what each means.

Main result is obfuscated:

The main result, in my opinion, is the existence of an intermediate "sorted" regime. It would be trivial to have a regime with a large mixed compartment or with small pure ones. The potentially interesting aspect of the model is that it can create pure compartments of at least intermediate size, if the parameters are chosen correctly. This is highly dependent on the way budding is modeled -- only explained in the Appendix, in an unclear way. In short, the budding flux for species i is defined as

Jb,i = Kb \times n \times f(\phii)

where n is the size of the compartment and phii the proportion of vesicles of type i (phii = ni /n). This is already confusing nomenclature, since they use Jb for this flux, when J is also the normalised injection rate. They then say that if the budding rate for species i depends linearly on its concentration, so

Jb,i = Kb n \phii = Kn ni

then you cannot get the intermediate regime. For that you need what they call "non-linear budding". In their words: "In order to reproduce this feature we choose a highly non-linear budding scheme f(phispecies) = 1 if phispecies > 0 and f(phispecies) = 0 otherwise". First of all, they are now using phispecies for what was before phii.

I can only imagine what biological readers might make of this labeled "highly non-linear scheme". It is, after all, just a constant!

phii cannot be negative and if phii = 0, then there are no vesicles to bud. So the budding rate is just a constant, independent of everything and the same for all species in the same compartment.

Problematic statistical analysis:

The statistical analysis is problematic. First of all, because we don't know whether there is a steady state, can one even define averages? But even if there is a steady state, there are things like the figure in Appendix 4. There, they measure the "temporal standard deviation" of the mass and purity. How are they defining this standard deviation, when the individual measurements come from a correlated time series and are, therefore, not independent? Note that there is a very large dependence with K, which could be trivial for this reason (as the correlation time would obviously depend on K).

Conclusion:

I cannot recommend publication of the paper – it is too flawed at present – and importantly, it is not possible to evaluate whether the research presented is even correct. A revised version, should the editors wish to solicit one, at the very least, must show some evidence of a steady state and explain how averages are calculated. The authors should pay special attention and care to make the paper more readable. Much more readable. In particular, the model (the actual model) could be fit in the text and justification/discussion of terms could be left for the Appendix.

Reviewer #3:

This paper explores a simple model for the dynamics of vesicles as they progress through the Golgi apparatus and shows that a number of observed phenomena can be understood based on a small number of biologically, and physically, well-motivated assumptions.

I thoroughly enjoyed reading this paper, even though I am not an expert on the Golgi. I think it's a great example of theory at its best, applied to an interesting biological problem. The authors start with some simple observations that have been reported in the literature, which they turn them into a mathematical model that upon analysis yields some interesting and experimentally testable predictions. I am optimistic that their results will lead to some new experiments.

The key result of the paper is the connection between the directionality of the vesicular transport and the chemical composition of the Golgi compartments, for which there seems to be experimental evidence. The connection is established within a very simple model whose assumptions seem reasonable. The paper also describes the emergence of a number of structural and dynamical properties of the Golgi, from the same small set of assumptions. A particularly interesting feature of the model is how different structures and dynamics can be accommodated within the model by changing one or more parameters (of which there are only four). For example, the model predicts that there is an inverse relationship between the speed of vesicle transport and fidelity of processing, which is consistent with published comparisons between the structure of Golgi in normal and starved yeast.

The paper is very clearly written, and there were only a few places where I was not quite sure about what the authors had in mind.

1) When describing the Budding mechanism, there is reference to a non-linear budding scheme that depends on the compartment size and contamination state. These are described in detail later, but I would recommend that the authors say a few words here to give the reader an intuitive sense of the thing without having to skip ahead.

2) In describing maturation, the chemical transformations are described as going only one way. How is this justified? Is it known that the reverse reactions are very slow? Also, is the maturation rate independent of the composition of the compartment and if so, what is the justification for that?

3) A typical compartment size is defined as the ratio of the second and the first moment of the size distribution. I was struck by the fact that this would give a "typical size" even for an exponential distribution of sizes, which I would not say defines a typical size (at least not from the point of view that the mean and standard deviation of such a distribution are equal). Might be worth a short comment on why this is a good definition of "typical size".

4) In the "Steady-state organization" section there is reference to a cut-off size, which I don't think was defined.

5) In the Discussion there is a conclusion that the spatial information is less crucial than biochemical composition for the organization of the Golgi. I am not sure this is warranted since a comparison between the two cannot be made in a model lacking spatial information.

In general I was left wondering whether simple testable quantitative predictions can be made from the model. I very much liked the qualitative observations that the model neatly explains, but I would be even more excited if there was a prospect for putting it to a much more stringent test provided by quantitative experiments, which the authors might propose for an intrepid experimentalist to do.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "A minimal self-organization model of the golgi apparatus" for consideration by eLife. Your revised article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Suzanne Pfeffer as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Following your submission of a revised manuscript we sought the opinion of the original reviewers and, more recently, that of an additional reviewer (a theorist chosen specifically to be outside the field of Golgi research). As you can appreciate, purely theoretical papers in eLife need to be accessible to the biological readership of the journal and, if on the abstract side, may require extra effort to be suitable for publication. Such is the case here. As detailed below, we fully appreciate the significance of your major conclusions regarding the emergence of two distinct models from a singe underlying dynamics. At the same time, the reviewers request changes in the structure of the paper to improve readability, and that you address some key questions about the role of the actual structure of the Golgi.

Summary:

Vagne et al. study a minimal model for the self-organisation of the Golgi, showing how the traditional models of "vesicular transport" and "cisternal maturation" arise as limiting cases of rich dynamical behaviour in a model of vesicle budding, maturation, fusion that leads to self-organised Golgi structure and cargo transport.

Revisions:

1) Regarding prior work, the reviewers note that as the work of Patterson et al., 2008, provided a detailed quantitative model of the Golgi using one set of parameters, and furthermore assessed and tested those parameters by doing extensive quantitative live cell imaging experiments, it would be appropriate to seek a comparison between your model (with its dimensionless parameters) and those results. This would likely enlarge the scope of potential predictions for direct experimental tests. Workers in the Golgi field would benefit from some suggested experiments expected to skew the pathway in one direction or another, with predicted outcomes on the size of the compartment or the speed of traversal etc. For example, the cisternal progression model predicted that larger cargo export rates would be more sensitive to nocodazole dissolution of microtubules and resulting creation of ministacks, a prediction that turned out to be correct: PMID 25103235.

2) To help the general reader understand the context of this work better, we would like to see an introductory figure illustrating the structure of the Golgi (and perhaps some of the models for transport in the Golgi).

3) The reviewers suggest that putting more of the model equations in the main text would streamline the argument; one way of making things more understandable might be to start by writing down simple mean-field equations (as in the early parts of Appendix 3), before delving into the analysis of the detailed model. The back-and-forth between the main text and the appendices makes for difficult reading.

4) An important concern is that the model shows how Golgi structure and vesicular transport can arise in a self-organised fashion, but it remains unclear to what extent the authors can claim that vesicular transport in actual Golgi is dominated by this transport arising from self-organisation. When reading the paper, we wondered about the contribution of spatial structure or biochemical processes (that might bias which vesicles cargo goes into, or which compartments a vesicle fuses into). It was only pages later, in the Discussion, that one finds a paragraph on the role of spatial structure: even if experiments show that "Golgi functionality is preserved under major perturbation of its spatial structure", how is transport affected? From a quick look at the reference (Dunlop et al., 2017), it seems that transport can be slowed down massively, hinting that spatial structure is just as important as self-organisation. Are there similar experimental results on biochemical effects?

5) One of the main results in the paper is the existence of different regimes of self-organisation, and in particular the existence of an intermediate, sorted regime with large pure compartments. However, the definition of these regimes remains rather qualitative. Perhaps some plots of mean compartment size against mean purity, to complement Figure 2, would put this part of the analysis on a clearer footing.

6) The model shows very clear anterograde transport of cargo in the limit kb>>1, but the retrograde transport in the limit kb<<1 is less clear; in particular, the model appears to show transport from the trans to well-mixed compartments, but not into the cis compartments: rather, there is weak flow from the cis compartments to well-mixed ones, i.e. anterograde flow in part of the system. Is it possible to show that flow cannot be purely retrograde? – This might be an important constraint on the "cisternal maturation" mechanism. (Perhaps part of this issue is addressed in Appendix 6.)
