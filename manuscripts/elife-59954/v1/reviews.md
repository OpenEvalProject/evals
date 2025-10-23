# Peer review - Round 1

Editors:
- Franziska Schneider-Warme, University of Freiburg Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59954.sa1](https://doi.org/10.7554/eLife.59954.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

At present there is limited understanding on how optogenetic depolarization of cardiomyocyte membrane potential can terminate cardiac arrhythmias, especially when using sub-threshold light intensities. The current paper presents a 2D computational model describing spiral wave dynamics in cardiac tissue, showing that optically induced spiral wave drift can lead to drift-induced collision with the boundary in favor of termination. It thus provides mechanistic insight into optogenetic defibrillation suggesting novel experimental strategies for terminating arrhythmias by illumination.

Decision letter after peer review:

Thank you for submitting your article "Drift and termination of spiral waves in optogenetically-modified cardiac tissue at sub-threshold illumination" for consideration by eLife. Your article has been reviewed by two peer reviewers, including Franziska Schneider-Warme as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Didier Stainier as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

In the presented manuscript, Hussaini and coworkers study the effects of sub-threshold optogenetic depolarization on the dynamics of spiral (voltage) waves in murine ventricular tissue. To this end, they use a 2D computational model that enables them to test how different light intensities and spatial illumination patterns influence the spatio-temporal dynamics of the respective spiral wave, and whether they enable driving the core towards the boundary for spiral wave termination. The authors analyze three strategies for modulation of spiral wave drift: (1) light gradient across the entire simulation domain; (2) single-intensity illumination of half the domain; and, (3) a "multi-step adjusted pattern" protocol, where the stimulated region is gradually shrunk from half to one 20th of the domain.

While computationally predicted changes in CV and dominant frequency were qualitatively confirmed by "wet" experiments using ChR2-expressing cultured myocytes and Langendorff-perfused mouse hearts, all other experiments are pure in silico calculations so far lacking wet experimental testing.

The presented work is methodologically sound and explores an interesting new application of cardiac optogenetics, which may be of interest to readers of eLife. However, these exciting data are difficult to interpret due to major issues with clarity of language and presentation of data in the Results section. We have the following suggestions to improve the manuscript.

Essential revisions:

1) In the current state, the manuscript has well written passages with detailed explanations of the observed data, however, other passages are difficult to understand, either because of sloppy language, or because the data is insufficiently explained and put into context. Please revise the entire manuscript in order to improve presentation of results and clarity. Please find a detailed list of suggestions below:

a) Please explain how you define "efficiency" of spiral wave termination and "improvement of efficiency" e.g. in the sixth paragraph of the Results. What are the determining parameters and how did you optimize them? In line, what does "further improvement in optimization" in the Introduction refer to? Please be more precise.

b) Introduction: What does the "above mentioned concept of low-energy control" refer to? Could you please explain this in more detail?

c) "we use two-dimensional (2D) simulation domains containing optogenetically-modified adult mouse ventricular cardiomyocytes". No, this is imprecise language that will confuse many readers. The simulation domains do not contain myocytes, but they do represent myocytes in a reasonably realistic way.

d) Figure 1G: It is difficult to see anything on this image, neither cells nor other contrasts. Could you please replace the image or increase the contrast?

e) Results, third paragraph: Badly written paragraph. 5.86 mm^2 contradicts scale bar in image. "Beyond normal" – please be more precise.

f) The figures describing the main findings (Figures 2-4) are extremely information rich, but Figure 2B/C/E/F (and similar panels in Figures 3-4) are quite difficult to interpret. Which lines correspond to which time points (especially the lower purple/blue traces – are those from the first cycles of reentrant activity at the beginning of the simulation?) The reader has no means of assessing the specific times or understanding how they were chosen. The authors refer to these as quiescent periods, but this should be clarified. Is it one trace per rotation of the spiral wave? Please use a color scheme that can be easily distinguished by color-blind readers as well. Color scales like viridis [used in Figure 1—figure supplement 1] are generally more forgiving in this regard compared to Matlab jet [used in the figures discussed above].)

g) For all spatial representations of wave dynamics (e.g. Figure 2A/D) could you please include a scale bar?

h) "demonstrates a temporal drift" – please rephrase.

i) Please be more precise: e.g. "may or may not end up in stationarity" – what is the threshold? How can this be explained? "by increasing light intensity" – by which factor? (please also consider to revise in other places).

j) Please further explain Figure 4E/F. Please explain why (whether) the adjusted pattern is superior to the gradient pattern. Where do the orange lines come from and what exactly was supposed to be communicated here.

k) Discussion, last sentence of fourth paragraph: Incomplete sentence. Please also correct typos e.g. "optogenetics", "Langendorff".

l) Please consistently include space between numbers and units (missing in some sections).

m) "restricted to cardiac tissue"; strictly speaking: cardiomyocytes.

2) Could you please explain the observed differences between wet experimental findings and simulations, and discuss possible reasons for qualitative discrepancies (Figure 1)? Moreover, while the computational work in Figures 2-4 is quite convincing, the impact of the study would be greatly enhanced by addition of data from monolayers or intact hearts confirming these findings. Have you performed any wet experimental work confirming these results? If so, could you please include this supporting data? If no such data is available at present, please discuss possible future experiments to assess your in silico results.

3) Why did you use a 2.5 cm x 0.25 cm tissue geometry (stripe) in Figure 1A-D, especially when comparing the data to data obtained in isolated mouse hearts?

4) It seems to be a general finding that changes in V and dV/dx decline over time? Can you explain this finding? What are the underlying mechanisms (e.g. ChR inactivation, compensatory ionic currents?)? Do these values reach equilibrium (stationary state) and if so, at what time point is it reached?

5) The authors discuss their findings from the 2D models in the context of the decrease in light intensity when applying light by epicardial illumination in 3D (Discussion). While this is an interesting hypothesis, the reviewers disagree that the light-induced voltage gradient is approximately linear in small hearts. The estimated thickness of the mouse LV free wall during diastole is ~1 mm (see Saito et al., 2017), which is presumably even thinner in the RV; the approximate space constant for exponential decay of blue light in cardiac tissue is ~0.6 mm. It is also debatable whether the stimuli (long-durations at 0.4 mW/mm^2) used for mouse preparations in the Bruegmann et al., 2016 study induced transmural gradients with both supra- and sub-threshold regions. In fact, results from human heart simulations in Figure 5D of the same paper show that the effect of light attenuation at a depth of ~1mm vs. the illuminated epicardium is relatively negligible, although there are differences from the mouse experimental prep. Please further discuss your hypothesis by taking into account the dimensions of the mouse ventricle and previously applied light intensities.

6) Videos 2-4 are excellent and helped tremendously in the interpretation of Figures 2-4. Kudos to the authors on this! For Video 1, please explain why the light turning off seems to cause the same artefact as the light turning on. Is this correctly interpreted? In the same video, would it be possible to colorize the data so that the wave front is easier to track?

7) The technique used to induce spiral waves (described in the Materials and methods and highlighted in Figure 1—figure supplement 1): Is this a novel development for this study or has it been described previously? In the explanation the authors state that the sections are initialized with "four different values of cell membrane voltage". It would make more sense if ALL model state variables (esp. gating variables for the sodium channel) were initialized to the values corresponding to that part of the action potential. Otherwise, the spiral wave would most likely not occur because the cells in region four would not be refractory. Please explain further and correct, if needed.

8) Light intensities in wet experiments: Please describe how they were measured. How did you ensure homogenous illumination?

9) "spatial non-uniformity in the refractory period of cells that constitute the domain." This is an interesting finding; could the refractory period (x) be plotted?
