# Peer review - Round 1

Editors:
- Frances K Skinner, Krembil Research Institute, University Health Network Canada

Reviewers:
- Milad Lankarany, The Hospital for Sick Children, University of Toronto Canada
- Oliver Britton

## Review text

DOI: [10.7554/eLife.42722.025](https://doi.org/10.7554/eLife.42722.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Visualization of currents in neural models with similar behavior and different conductance densities" for consideration by eLife. Your article has been reviewed by Gary Westbrook as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Alexandre Guet-McCreight (Skinner lab) (Reviewer#1); Milad Lankarany (Reviewer #2); Oliver Britton (Reviewer #3). The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

All of the reviewers were fully appreciative of the 'tools and resources' approach and thought that the visualization tool would be helpful and useful to the wider community. At the same time, there were areas for improvement. Specifically, (i) expansion of the code to make it usable by others, (ii) more elaboration on the method itself (optimization, objective function) and perhaps less on the details of the 'results' which are clear enough from the figures and given that this is a tools and resources paper, and (iii) several small fixes throughout. We regard these points as essential in the revision, but the full comments are provided below for your guidance as you revise the manuscript.

Essential revisions:

Reviewer #1:

In this manuscript, the authors present several novel methodologies, including (A) an optimization technique that involves the use of thresholds (i.e. Poincaré sections) as objectives, (B) a visualization technique for better plotting ion channel currents in neuron models, (C) a visualization technique for better demonstrating changes in electrophysiology at different levels of perturbations, as well as (D) combining these two visualization techniques. Specifically, the visualization techniques shown in this manuscript demonstrate very novel, intuitive, and yet surprisingly simple ways of viewing and interpreting complex high-dimensional data. Specifically, the currentscape plots are a much-needed addition to the field and facilitate what both computational and experimental researchers can interpret from models. As well, the plots highlighting changes in voltage and ISI distributions over different perturbation levels provide another surprisingly simple but rich way of viewing large amounts of data. Overall, this manuscript merits publication but may benefit from giving more background on its "landscape" optimization method, and several sections in the results can possibly be boiled down to more succinct take-away messages.

– While the Supplementary files on Dryad are an essential component of this publication, it is not straightforward for every reader to run this code to extract the parameters used in these simulations. As such, it might be helpful for readers who are not immediately intending to try out this code, to include these values in a supplementary table. Related to this, a small glossary table of the variable names might also be helpful.

– For a reader that is somewhat naïve on the topic of optimizations, it remains unclear to me how landscape optimizations differ from other types of optimizations (i.e. why is it called a "landscape" optimization?). It might be helpful to describe a bit more how landscape optimizations work relative to other types of optimizations – it sounds as though the "landscape" part simply refers to the type of target/objective function that is being used? On a related note, very few details are given regarding the "custom genetic algorithm" (subsection “Finding parameters: landscape optimization”). Would it be possible to give more details on this, as well as parameters that were used in the optimizations (e.g. mutation, crossover, population size, etc.)?

– Often throughout the paper, results from the plots are described in more detail than is necessary and this tends to derail the focus of the story. Here I am mainly referring to the more-or-less informal descriptions of what the plots look like across different models, channel mechanisms, currents, manipulations, etc. (e.g. subsection “Perturbing the models with gradual decrements of the maximal conductances” or subsection “Changes in waveform as conductances are gradually decreased”). While these observations are very interesting in themselves, the authors often do not give enough explanation (i.e. of why those observations occur) to warrant mentioning them in the first place. In fact, many of those observations are indicative of the rich amount of information obtainable from these plotting methods, but perhaps beyond the scope this paper. Ultimately, since the authors are presenting a novel visualization technique, the plots should really be able to speak more for themselves. In my opinion, the plots do indeed speak for themselves, better in fact than the results descriptions given by the authors.

– It would be nice to apply the plotting technique in Figure 3 and Figure 5 to a set of experimental data for comparison purposes. Based on the descriptions of how these plots are made, I would imagine that this could be possible, though maybe at a lower resolution(?). If so, it might be worth mentioning, especially for experimental readers. Given that there is diversity in how the electrophysiology of the different models change with removal of channel currents and current injection amplitudes, further steps following model optimization might be to see which models can capture the changes (or diversity in changes) seen in electrophysiology. This might further help narrow the list of possible optimization solutions that can viably capture experimental electrophysiologies.

Reviewer #2:

This paper presents a comprehensive study on how a model neuron with different maximal conductances show similar membrane activity. I think this paper is well designed and presented. The problem of having identical observation (experimental data) given different parameter settings of a representative model is important in neuroscience. This paper introduces a visualization method to track the dynamics of ionic currents underlying each set of parameters. I have two major points to enhance the quality of the paper. Shortly, my major points are about the consistency of the results of the paper with respect to (i) objective function (total Error) and (ii) type of stimulus.

Elaborate on the effect of objective function on your results (overall) – specifically, if more detailed objective functions (or the same as yours but with different weights) might better distinguish between bursting models (which might not be inspected visually). And, I think the value of objective function (total error, Equation 4) should be reported. For the 6 selected models of bursts, you should report those values.

My second point is more like a question. What happened to the response of, for example, two models (a and b) given an identical but noisy injected current? Are they still the same?

Reviewer #3:

This is an interesting manuscript that describes several novel visualization techniques for interpreting the large amount of data that are routinely generated by computational models of neurons and other electrically excitable cells. The authors focus on methods to visualize how the balance of all ionic currents in a model, as well as the voltage, change when the conductance of one current is varied. This is a key part of understanding these highly non-linear models, as changes in one current often have unexpected knock on effects on the behavior of many other currents. These techniques are illustrated using six models with similar control behavior but different conductance values.

I particularly like that the techniques the authors describe allow both qualitative (e.g. firing pattern) and quantitative (e.g. peak AP voltage) changes in model output under parameter variation to be visualized within a single plot.

The authors illustrate the use of these techniques by analyzing an eight current single-compartment neuron model. I appreciate the use of a reasonably complex model as an example, rather than a toy model with few currents, as it better illustrates to readers how they might use the techniques in their own research.

My major criticism of the manuscript is that while I commend the authors for providing well organized source code that is sufficient to reproduce all figures, the study has been submitted as a tools and resources paper, and the code as is does not form a tool for other researchers to use, as it is a series of non-reusable scripts.

To allow other researchers to easily use these techniques, I would like to see the visualization code repackaged as a Python module encapsulating the main plotting functions (i.e. currentscapes; voltage probability distribution and ridge plots; ISI distribution plots; and conductance against current plots) with a documented interface. Building such a module in Python is relatively simple. I would encourage the authors to look at the Python visualization module Seaborn (https://seaborn.pydata.org/) if they are not familiar with it, to see a good example of an open source scientific visualization library.

With such a module, the code for a new user to produce, for example, a currentscape plot could be reduced to a few lines of code, e.g.:

> import current_visualization_module

> # Load pre-existing arrays of data from a simulation including currents,

> voltage, time arrays = load(path_to_data)

> current_names = ['INa', 'ICaT', 'IKA',…etc]

> # Perform the plot

> current_visualization.plot_currentscape(arrays, current_names)

Currently, most of the figure plotting code is provided as a set of scripts, but as these scripts are organized into functionally distinct sections (e.g. running the model, currentscape calculations, currentscape plotting), they could easily be converted into reusable functions. The figure plotting scripts could then be rewritten to use these functions, which would provide a gallery of examples for how to use the module. I don't think this revision would need too much extra work as most of the required code is already written and just needs to be encapsulated within a set of functions.

Releasing such a module this would substantially add to the utility and uptake of this work and provide a valuable tool for multiple electrophysiological modelling communities. From a purely selfish viewpoint, I would use it in my own work!
