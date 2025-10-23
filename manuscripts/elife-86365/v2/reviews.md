# Peer review - Round 1

Editors:
- Marcel Stimberg, https://ror.org/000zhpw23 Institut de la Vision France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86365.sa0](https://doi.org/10.7554/eLife.86365.sa0)

The paper introduces a new, important framework for neural modelling that promises to offer efficient simulation and analysis tools for a wide range of biologically-realistic neural networks. It provides convincing support for the ease of use, flexibility, and performance of the framework, and features a solid comparison to existing solutions in terms of accuracy. The work is of potential interest to a wide range of computational neuroscientists and researchers working on biologically inspired machine learning applications.


---

# Peer review - Round 1

Editors:
- Marcel Stimberg, https://ror.org/000zhpw23 Institut de la Vision France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86365.sa1](https://doi.org/10.7554/eLife.86365.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "BrainPy: a flexible, integrative, efficient, and extensible framework for general-purpose brain dynamics programming" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Panayiota Poirazi as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Improve the benchmarks and examples. The examples demonstrating the versatility of the simulator lack details (e.g. number of neurons, training method where applicable, etc.). Similarly, the benchmarking procedures are not sufficiently described, and it is not clear whether the results across simulators are comparable. In particular: What are the integration methods, simulation time steps, and floating point precision that were used, and are they identical across simulators? What time is measured exactly (total time including model construction time, synapse creation time, compilation time, or only simulation run time)? What acceleration modes offered by other simulators (multi-threading, MPI, etc.) were used? Were all efforts taken to optimize the code used for other simulators, or is it based on code provided by the developers of those tools? Finally, please scale networks in a way that keeps network activity roughly constant.

2) Verify/demonstrate the accuracy of the simulator. Please provide evidence that the chosen approach does not trade improved performance against reduced accuracy – or if it does, discuss the trade-off.

3) Improve the discussion of limitations and weaknesses of the presented tool, and beware "persuasive communication devices" (https://elifesciences.org/articles/88654). Some of the comparisons to existing state-of-the-art tools do not do justice to their capabilities/advantages.

4) Clarify the target audience of the tool. Is BrainPy primarily intended for computational neuroscientists or machine learning research, or is it particularly aimed at neuro-AI practitioners bridging the two domains? For "pure machine learning", would the authors consider their tool giving an advantage over using a dedicated tool like PyTorch? For computational neuroscience research, the tool does seem to lack essential local plasticity rules (e.g. Hebbian plasticity or STDP – the latter is mentioned in Appendix 8 but refers to a non-existing class in the package).

Reviewer #1 (Recommendations for the authors):

General remarks:

– The package contains automatic unit/integration tests, but from a cursory look, they (many? most?) only test for the absence of basic errors (i.e. the code does not fail to run), not for the correctness of the result. Some classes (e.g. GapJunction) never seem to be tested at all.

– Personally, I'd remove the supplementary document, it contains information that could rather go into the documentation, since it risks being outdated quickly.

Specific remarks:

– In the abstract, the sentence "Brain dynamics modeling is an indispensable tool for […] modeling the dynamics of the neural circuits" sounds rather redundant/tautological.

– l.36: "An example …" introduces two examples (TensorFlow and PyTorch).

– References to sections seem to be broken (e.g. l. 119, l. 136).

– L.163, "as standalone modules" is not very clear.

– L.177: I'm not sure the authors really mean "recursive" here, shouldn't it be "hierarchical"? Also, l. 181: not sure what the authors exactly mean here, in most simulators, you can e.g. simulate a neuron individually but also include it in a network and simulate as part of the network.

– Figure 2A: maybe add to the figure/caption that BrainPy is imported as bp? What does sh refer to?

– Figure 2D: super should refer to System and not Circuit, I think.

– Figure 3E: Typo in title ("Rater" → "Raster").

– L.199: not sure one can say that the figure "demonstrates" that one can simulate models in parallel.

– L.304: this needs to be qualified a bit, I think, since it is also the idea behind code generation used by several other simulators.

– Figure 7A: missing y-axis label.

– Figure 7C: having the ratio in the same plot is an odd choice, I'd at least use a second y-axis to make this clearer.

– Figure 7D: the y-axis label should not mention Ratio (not plotted here).

– L.311/Figure 8C: this (and the results) seems a problem with the code written by the authors for Brian2, maybe contact the Brian2 developers?

– Figure 8C: I'd recommend changing the colors to match the previously used colors to avoid confusion.

– L. 376: in what way can "standard debugging tools" debug issues with JAX/XAL?

– Appendix 1, last paragraph: "Moreover, descriptive languages…" – I do not quite understand this. With descriptive languages, users do not have to use low-level language. Or does this refer to the effort of the tool developers?

– Appendix 8, l. 1141: apart from the "a piece of cake" expression that I'd rather replace, I did not find any STDP class in BrainPy.

Reviewer #2 (Recommendations for the authors):

There are a couple of significant points to mention here:

You state on p12: "We also implemented this decision-making model with Brian2 on the CPU (although it was stated that Brian2 could target on GPU via code generation with GeNN (Stimberg et al., 2020), we could not run this model on a GPU with Brian2 successfully) and observed that the running speed of Brian2 was significantly slower than that of BrainPy.". In order to make this a fair test, I would expect more effort in getting the model to run, choose another standard model to run with both platforms, or at least provide a substantial explanation for why you were unable to. The editor is in fact the lead author of Brian2 and would very likely be able to help you get support from the GeNN team.

I was also unable to create a Docker image on an ARM-based Mac since jaxlib is unavailable for the combination of linux on ARM processors. Until this (reasonably common) combination becomes an official target for compiled binaries, it would be good to provide instructions on how to compile it from source or otherwise work around this missing dependency. Similarly, I was unable to install brainpylib.

Reviewer #3 (Recommendations for the authors):

More care should be given to the reproducibility of the benchmarks. When using a benchmark like COBA (Figures 6, 7, and 8), the numerical method should be the same, or changes should be stated and explained. The authors should state how many runs they used for each experiment to obtain the presented timings. From the codes in the repository, we assume that they are always analyzing a single run. We would recommend performing simulation multiple times to catch the deviations in-between runs.

The authors use a fixed connection probability of 2% in all scaled benchmarks and to compensate for the increasing number of connections, the authors rescale the weights. However, this approach leads to the following consequence: with an increasing number of connections the activity in the population shrinks. For the settings used in the benchmarks, it would be averaged across 5 runs each: 20.83 +/- 0.87 Hz (4,000 neurons); 10.89 +/- 0.34 Hz (8,000 neurons); 5.25 +/- 0.11 Hz (16,000 neurons); 3.61 +/- 0.04 Hz (24,000 neurons); 2.83 +/- 0.02 Hz (32,000 neurons); 2.38 +/- 0.03 Hz (40,000 neurons).

To retain the average firing rate, one would rescale the probability instead of the weights, e.g., p = 80. / N, where N is the number of neurons while the weight values remain the same in all configurations. Such an approach was used by Stimberg et al. (2020), which has been already cited by the authors. Such an approach retains the firing frequencies at a comparable level, e.g.: 21.91 +/- 1.32 Hz (4,000 neurons); 21.59 +/- 0.71 Hz (8,000 neurons); 21.15 +/- 0.07 Hz (16,000 neurons); 21.33 +/- 0.16 Hz (24,000 neurons); 21.56 +/- 0.19 Hz (32,000 neurons); 21.59 +/- 0.39 Hz (40,000 neurons).

For the COBAHH benchmark, it is first not clear whether the base firing rate of 37 Hz is not too high. Secondly, as the authors used here also the weight rescale, we can see the same drop in activity with increasing network sizes: 37.08 +/- 0.88 Hz (4,000 neurons); 17.57 +/- 0.43 Hz (8,000 neurons); 3.61 +/- 0.01 Hz (16,000 neurons); 3.11 +/- 0.02 Hz (24,000 neurons); 2.83 +/- 0.03 Hz (32,000 neurons); 2.73 +/- 0.05 Hz (40,000 neurons); 2.53 +/- 0.03 Hz (60,000 neurons); 2.55 +/- 0.05 Hz (80,000 neurons); 2.65 +/- 0.04 Hz (120,000 neurons).

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "BrainPy, a flexible, integrative, efficient, and extensible framework for general-purpose brain dynamics programming" for further consideration by eLife. Your revised article has been evaluated by Panayiota Poirazi (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

– The benchmarks, accuracy evaluations and their descriptions have been greatly improved, but they still have shortcomings that at least merit discussion: while the accuracy evaluations in Appendix 11 convincingly argue for no major discrepancies between the simulations, they are not enough to unambiguously state that single precision leads to "a significant speedup without the sacrifice of the simulation accuracy". From my personal experience, simulating a large COBAHH network with single precision will inevitably lead to division by 0 for a few neurons, if not using equations that use special functions such as exprel (scipy, brian2), or vtrap (NEURON) to avoid this issue. This will usually not show in the average firing rate or a raster plot, but having neurons that are no longer active with a membrane potential of NaN should certainly be considered a loss of accuracy. I am aware that a more in-depth analysis of the accuracy (as e.g. in van Albada et al. 2018; doi: 10.3389/fnins.2018.00291) is out of scope, but I think a more careful evaluation of the accuracy is warranted. It should also be noted that the raster plots for NEST and NEURON do look quite different from the other results in Appendix 11 figures 3 and 4 – probably due to different initial conditions? Finally, the authors state that "Notably, BrainPy offers support for utilizing single-precision floating-point (x32) arithmetic", but this feature is present in several of the other simulators that were benchmarked as well and has been prominently mentioned in the papers introducing the GPU simulators discussed in the manuscript (GeNN, Brian2GeNN, Brian2CUDA).

– The manuscript (understandably) puts forwards the features of the simulator, but sometimes is not sufficiently making the link to existing literature on the topic and/or implementations in existing simulators. Apart from the single-precision feature mentioned above, this is in particular the case for the sparse and event-driven synaptic connectivity. Implementing such connectivity has been at the heart of simulator development for a long time, in particular in the context of GPU acceleration (for some early examples, see Plesser et al. 2007 http://link.springer.com/chapter/10.1007/978-3-540-74466-5_71; Fidjeland et al. 2009 https://doi.org/10.1109/ASAP.2009.24; Brette and Goodman 2011 https://doi.org/10.1162/NECO_a_00123). Similarly, "just-in-time connectivity" has been implemented before (e.g. Knight and Nowotny 2021 https://doi.org/10.1038/s43588-020-00022-7). Please also note that the review in Appendix 1 should probably mention NMODL for the NEURON simulator (which I would not describe as having "a library of standard models written in C or CUDA").

– The manuscript text is still somewhat hard to follow at times due to jargon that is not common usage (which also relates to the previous point). For example, eLife readers are not necessarily familiar with technical terms around just-in-time compilation (e.g. "lowering" code onto CPU/GPU, "fusing" operators), and will therefore have a hard time understanding where the speed benefit of JIT compilation comes from. Terms such as "time delays" and "length delays" (Appendix 4) are also non-standard and need explanation (as a side note: the mechanism for delaying spikes is never explained). Finally, readers might confuse the "event-driven operators" mentioned in the manuscript with event-driven simulation (as opposed to clock-driven; see e.g. Ros et al. 2006 10.1162/neco.2006.18.12.2959). I'd suggest the authors carefully reconsider non-standard terms and clearly define them if no commonly used term exist or if a large part of the readership might not be familiar with them. Other examples of such terms/concepts are "bfloat16" (l. 359), "data parallelism" vs. "model parallelism" (l. 479), or even "TPU" (from the abstract on).
