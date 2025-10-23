# Peer review - Round 1

Editors:
- Denise Cai, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73266.sa0](https://doi.org/10.7554/eLife.73266.sa0)

This paper is of interest to neuroscientists working on all-optical interrogation of neural circuits and optogenetics. It provides a new, inexpensive, one-photon approach for high-speed 3D photostimulation with sparse targeting. This new method has been well characterized and demonstrated in both in vitro and in vivo experiments on mouse brain tissue.


---

# Peer review - Round 1

Editors:
- Denise Cai, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73266.sa1](https://doi.org/10.7554/eLife.73266.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Three-dimensional Multi-site Random Access Photostimulation (3D-MAP)" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and John Huguenard as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Luis Alberto Carrillo Reid (Reviewer #3).

The reviewers have discussed their reviews with one another and are unanimous in recommending submitting a revised version of the manuscript. The Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All 3 reviewers were enthusiastic about the manuscript and found your approach of an all optical 1P method for stimulating neurons to be of interest to and impactful for the neuroscience field. In general, the reviewers found the manuscript to be comprehensive and well-written. However, there were several points of clarification/ more detailed explanations the reviewers have requested that will be need to addressed prior to recommending publication in eLife. Please see the detailed points of clarification requested by reviewers below.

Reviewer #1:

The authors nicely quantify the optical point spread function both on a fluorescent slide and, importantly, in brain slices and in vivo, and they do so for blue and red light – wavelengths that are suited for single photon optogenetics. The authors demonstrate the utility of this technique, particularly in cases where neurons expressing a given optogenetic protein are sparsely labeled or, as may be the case for inhibitory neurons, naturally sparse. Notably, as cell type specific promoters in layer 2/3 are more fully characterized, it is likely that naturally sparse excitatory networks will be evident as well.

The authors demonstrate the use of this approach for optogenetic circuit mapping, and for in vivo read-write experiments.

Weaknesses:

In Figure 4E, it seems like excitatory inputs to PV cells are clustered. Is this the correct message from this figure, or do those spots (particularly near dZ=40um) represent single excitatory neurons rather than groups of excitatory neurons?

I didn't understand the approach in Figure 6. CoChR is a blue-light opsin while jRCaMP1a is a red light calcium indicator. Why the need to start imaging the jRCaMP1a responses only after the CoChR stimulation? Is there a great deal of cross talk in the excitation wavelengths?

While the authors are very up front about the fact that this stimulation approach works best for very sparsely labeled neurons, this does limit the potential utility of the application.

Overall, this is a well written paper that presents a full accounting of a new and potentially quite useful 3D stimulation approach. The authors are candid about the shortcomings, which is refreshing. They provide well done quantitative measures and they do so across a range of preparations. They validate their approach with electrophysiological measures. There is little here to dislike.

I have no specific recommendations. I found the paper to be well written and I imagine that it will be of some real interest to the field.

Reviewer #2:

Xue et al., introduced a new high-speed 3D photostimulation method, 3D-MAP, based on single photon light sculpting. Compared with typical single photon approaches, this new technique is improved in 3D spatial resolution, simultaneous targeting numbers and pattern refresh rate, offering a simple and inexpensive alternative to two-photon optogenetics. Although this technique requires a certain level of expression sparsity especially in a scattering sample, its overall 3D stimulating throughput still makes it valuable in various applications.

Xue et al., also demonstrated the application of 3D-MAP in in vivo 3D optogenetic photostimulation and all-optical parallel interrogation of mouse brain with impressive results. The 3D-MAP technique can be potentially used as an add-on module for existing imaging system, such as for single objective light-sheet microscopy. Its application can be expanded to other animal models with a less scattering brain, such as zebrafish, to mitigate spatial crosstalk.

This paper has provided sufficient technical details for readers to understand the 3D-MAP method, with carefully designed and conducted experiments to demonstrate the potential applications in high-throughput interrogation of neural circuits. Yet there are some aspects of the system characterizations and experiment details that need to be further clarified.

Overall, this manuscript described the 3D-MAP technique clearly and demonstrated its application with promising data. I do have a few suggestions that I think would enhance the clarity and strength of this paper.

1. The authors mentioned that they could unselect certain illumination angels of specific stimulated focus to avoid stimulating non-targeted areas. Is it calculated automatically with the current algorithm? When multiple rays for different foci make a cross section in the 3D space, do they get removed or not?

2. The authors compared different foci across the large FOV in Figure 2—figure supplement 1 based on the 25 foci located on an oblique plane (Figure 2D). It would be more reliable if the PSF is averaged from multiple measurements taken from randomly distributed foci across the entire FOV.

3. Is the same 10-pixel radius aperture on the DMD used for all the experiment with mouse brain tissue later? Is the PSF improved in scattering tissue when using a smaller radius?

4. The authors performed the all-optical interrogation experiment in vivo in L2/3 neurons that are 200μm-300μm deep in the intact mouse brain, yet they only measured the optical PSF under the brain slice up to 150μm. Similarly, the PPSF measurement in Figure 3 only shows the results "in the upper 100μm of the brain". Since the resolution in Z degraded dramatically with blue light stimulation, it would be better to add the measurement of thicker brain tissue to mimic the in vivo experiment condition in L2/3. Besides, the all optical 3D PPSF under 200μm (Figure 6E) shows a similar axial FWHM compared with the electrophysiology PPSF in the upper 100μm brain (Figure 3I) as well as the optical PSF in under 100μm brain slice (Figure 2H). This is a bit confusing and could be a bit misleading. Please explain further taking the optical PSF, the nonlinear effect of opsin and calcium indicator sensitivity and the imaging system performance into consideration.

Reviewer #3:

This paper proposes a low-cost approach to perform simultaneous calcium imaging recordings and photostimulation of neuronal ensembles. The study of the causal relation between the activity of identified groups of neurons and their behavioral output is a topic of broad interest for the neuroscience community. Recently it has been shown in different brain areas that the identification and further manipulation of neuronal ensembles related to a behavioral task could be achieved using two-photon microscopy. This paper proposes a one photon tool to eventually facilitate the use of all-optical interrogation of neuronal circuits and behavior. However, the main limitations of the system showed in this paper are the necessity of sparse expression of opsins and the spatial resolution that comprises volumes bigger than the somatic region of individual neurons.

The authors suggest that the proposed 1P system could be used instead of 2P systems but according to the experimental results, this is only valid for a very narrow set of experiments that involve the sparse expression of opsins.

1. To clearly show the ability of the system to perform simultaneous calcium imaging and photostimulation the authors should show raw calcium transients of photostimulated and non-photostimulated neurons at different trials, as well as a plot showing calcium transients of non-stimulated neurons that express the opsin as a function of the distance between photostimulated neurons.

2. The manuscript mentioned the cost of budget and high performance realizations of the 1P system but a clear statement of the disadvantages of a budget system is lacking. It would be helpful to include a paragraph indicating what is missing in a budget 1P system compared to a high performance 1P system.

3. One of the main issues with all-optical interrogation of neural circuits and behavior is the lack of co-expression of opsins and calcium indicators. This is a crucial step since usually the targeted neurons are the ones that have activity in the behavioral task. However, the manuscript mentions that the system proposed is ideal for sparse expression of opsins, but the authors didn't mention the level of co-expression in their experiments. If the level of co-expression in a sparse labeling is low, then the system will not be ideal for the all-optical interrogation of neural circuits and behavior.

4. The main strength of the paper is the demonstration that the system could be used to map the influence of sparse neurons over a large volume onto a postsynaptic target. So, focusing the rationale, results and conclusions on those experiments could be a better strategy until the 1P system is refined to reach similar performance of a 2P system for broad expression of opsins.
