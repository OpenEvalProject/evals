# Peer review - Round 1

Editors:
- Klaus-Armin Nave, https://ror.org/03av75f26 Max Planck Institute for Multidisciplinary Sciences Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90046.3.sa0](https://doi.org/10.7554/eLife.90046.3.sa0)

This study presents valuable findings that add to our understanding of cortical astrocytes, which respond to synaptic activity with calcium release in subcellular domains that can proceed to larger calcium waves. The proposed concept of a spatial "threshold" is based on solid evidence from in vivo and ex vivo imaging data and the use of mutant mice. Details of the specific threshold must be taken with caution and are necessarily incomplete, but may be supported by additional experiments with higher resolution in space and time in the future.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90046.3.sa1](https://doi.org/10.7554/eLife.90046.3.sa1)

Summary

Lines et al investigate the integration of sensory-evoked calcium signals in astrocytes of the primary somatosensory cortex in anesthetized mice. More precisely, their goal is to better characterize the mechanisms that govern the emergence of whole-cell events in astrocytes, here referred to as calcium surges. As a single astrocyte communicates with hundreds of thousands of synapses simultaneously, understanding the spatial and temporal integration of calcium signals in astrocytes and the mechanisms governing these phenomena is of tremendous importance to deepen our understanding of signal processing in the central nervous system. In line with previous reports in the field, the authors find that most signals originate in the arborization of astrocytes, occasionally leading to somatic and whole-cell events. On average, the latter occur following domain activity closer to the soma, suggesting a centripetal propagation of signals leading to somatic events. Moreover, they observe that the distance from the soma to active domains increases with time after somatic events, suggesting a potential centrifugal propagation of signals post-somatic activity. The results suggest that most calcium surges depend on the expression of IP3R2, the main calcium channel in astrocytes, located at the membrane of the endoplasmic reticulum. Finally, they report a correlation between the percentage of active domains in the astrocyte "arbor", the emergence of a somatic event, and the frequency of slow inward currents from neighboring neurons. The main claim of this manuscript is that there would be a spatial threshold inherent to astrocytes of ~23% of domain activation above which a calcium surge is observed. Although the study provides data and concepts that are important for the glia field, the conclusions seem a little too assertive and general with respect to what can be deduced from the data and methods used.

Strengths

The major strength of this study is the experimental approach that allowed the authors to obtain numerous and informative calcium recordings in vivo in the somatosensory cortex in mice in response to sensory stimuli as well as in situ. Notably, they developed an interesting approach to modulate the percentage of active domains in the astrocyte arborization by varying the intensity of peripheral stimulation (its amplitude, frequency, or duration). The question investigated is important as the mechanisms governing signal integration in astrocytes and its effect on neighboring cells are poorly understood.

Weaknesses

The major weakness of the manuscript is the method used to analyze and quantify calcium activity, which mostly relies on the analysis of averaged data and overlooks the variability of the signals measured. As a result, the main claims from the manuscript seem to be incompletely supported by the data.

Although the revised version includes more discussion on the experiments that could be done to extend the results from this study, more discussion would be needed to clarify the limitations on what can be deduced from the proposed experimental and analytical design. Notably, the analysis pipeline seems biased by the assumption of the existence of a spatial threshold dictating the emergence of global calcium events in astrocytes. Although there is a clear linear correlation between the percentage of active somas and the percentage of active domains in the arborization (Figure 2 panel F), concluding on the existence of an inherent threshold of domain activity is not completely supported by the data (see e.g. Figure 2 panel F or Figure 4 panel E). It would probably be more accurate to report that most somatic events occur when the percentage of arbor domains being active is above 21-24% (95% confidence interval of the reported threshold). Thus, some of the conclusions from the manuscript, such as p.14 l.34-35 " spatial threshold of domains that needs to be reached in order to lead to soma activation", seem a bit too assertive as some astrocytes did display soma activation with a much smaller percentage of active domains or on the contrary, no somatic event despite domain activity way above the threshold. Similarly, as Figure 6 demonstrates a strong effect of IP3R2 knock-out on somatic activation but reports a non-zero probability of soma activity in IP3R2 -/- mice (panel F), the conclusion that IP3R2 are necessary to trigger an astrocytic calcium surge seems a bit too strong. Finally, the results reported in Figure 7 demonstrate the existence of a strong correlation between SICs, the percentage of active astrocyte domains on, and somatic activation, so that the conclusion "These results indicate that spatial threshold of the astrocyte calcium surge has a functional impact on gliotransmission" (l.4&-48 page 13) also seems a bit too assertive.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90046.3.sa2](https://doi.org/10.7554/eLife.90046.3.sa2)

Summary:

The study aims to elucidate the spatial dynamics of subcellular astrocytic calcium signaling. Specifically, they elucidate how subdomain activity above a certain spatial threshold (~23% of domains being active) heralds a calcium surge that also affects the astrocytic soma. Moreover, they demonstrate that processes on average are included earlier than the soma and that IP3R2 is necessary for calcium surges to occur. Finally, they associate calcium surges with slow inward currents.

The revised manuscript is improved compared to the first iteration. While some concerns have been addressed, my main critique pertaining to ROI approach/sampled area, statistical analyses and anesthesia are in my view still important caveats of the study that I think should have been even more clearly addressed in the manuscript.

Strengths:

The study addresses an interesting topic that is only partially understood. The study uses multiple methods including in vivo two-photon microscopy, acute brain slices, electrophysiology, pharmacology, and knockout models. The conclusions are strengthened by the same findings in both in vivo anesthetized mice and in brain slices.

Weaknesses:

The method that has been used to quantify astrocytic calcium signals only analyzes what seems to be a small proportion of the total astrocytic domain on the example micrographs, where a structure is visible in the SR101 channel (see for instance Reeves et al. J. Neurosci. 2011, demonstrating to what extent SR101 outlines an astrocyte). This would potentially heavily bias the results: from the example illustrations presented it is clear that the calcium increases in what is putatively the same astrocyte goes well beyond what is outlined with automatically placed small ROIs. The smallest astrocytic processes are an order of magnitude smaller than the resolution of optical imaging and would not be outlined by either SR101 or with the segmentation method judged by the ROIs presented in the figures. Completely ignoring these very large parts of the spatial domain of an astrocyte, in particular when making claims about a spatial threshold, seems inappropriate. Several recent methods published use pixel-by-pixel event-based approaches to define calcium signals. The data should have been analyzed using such a method within a complete astrocyte spatial domain in addition to the analyses presented. Also, the authors do not discuss how two-dimensional sampling of calcium signals from an astrocyte that has processes in three dimensions (see Bindocci et al, Science 2017) may affect the results: if subdomain activation is not homogeneously distributed in the three-dimensional space within the astrocyte territory, the assumptions and findings between a correlation between subdomain activation and somatic activation may be affected.

Authors reply: In order to reduce noise from individual pixels, we chose to segment astrocyte arborizations into domains of several pixels. As pointed out previously, including pixels outside of the SR101-positive territory runs the risk of including a pixel that may be from a neighboring cell or mostly comprised of extracellular space, and we chose the conservative approach to avoid this source of error. We agree that the results have limitations from being acquired in 2D instead of 3D, but it is likely to assume the 3D astrocyte is homogeneously distributed and that the 2D plane is representative of the whole astrocyte. Indeed, no dimensional effects were reported in Bindocci et al, Science 2017. We have included a paragraph in the discussion to address this limitation in our study on P15, L23-27:

"The investigation of the spatial threshold could be improved in the future in a number of ways. One being the use of state-of-the-art imaging in 3D(Bindocci et al., 2017). While the original publication using 3D imaging to study astrocyte physiology does not necessarily imply that there would be different calcium dynamics in one axis over another, the three-dimensional examination of the spatial threshold could refine the findings we present here.

Comments on revisions: It is good that 3D imaging aspects are mentioned as a limitation, and I agree that Bindocci et al. do not necessarily suggest that results in this manuscript would have been different if also the third spatial dimension was included in the analyses. However, the way I see it, the added analyses and text changes throughtout still do not adequately address my concern pertaining to basing a spatial threshold on a fraction of the astrocyte territory.

The study uses a heaviside step function to define a spatial 'threshold' for somata either being included or not in a calcium signal. However, Fig 4E and 5D showing how the method separates the signal provide little understanding for the reader. The most informative figure that could support the main finding of the study, namely a ~23% spatial threshold for astrocyte calcium surges reaching the soma, is Fig. 4G, showing the relationship between the percentage of arborizations active and the soma calcium signal. A similar plot should have been presented in Fig 5 as well. Looking at this distribution, though, it is not clear why ~23% would be a clear threshold to separate soma involvement, one can only speculate how the threshold for a soma event would influence this number. Even if the analyses in Fig. 4H and the fact that the same threshold appears in two experimental paradigms strengthen the case, the results would have been more convincing if several types of statistical modeling describing the continuous distribution of values presented in Fig. 4E (in addition to the heaviside step function) were presented.

Authors reply: We agree with the reviewer and have added to the paper a discussion for our justification on the use of the Heaviside step function, and have included this in the methods section. We chose the Heaviside step function to represent the on/off situation that we observed in the data that suggested a threshold in the biology. We agree with the reviewer that Fig. 4G is informative and demonstrates that under 23% most of the soma fluorescence values are clustered at baseline. We agree that a different statistical model describing the data would be more convincing and confirmed the spatial threshold with the use of a confidence interval in the text and supported the use of percent domains active for this threshold over other properties such as spatial or temporal clustering using a general linear model. P18-19, L34-2:

"Heaviside step function

The Heaviside step function below in equation 4 is used to mathematically model the transition from one state to the next and has been used in simple integrate and fire models (Bueno-Orovio et al., 2008; Gerstner, 2000).(4)H(a):={0,a<aT1,a≥aT

The Heaviside step function 𝐻(𝑎) is zero everywhere before the threshold area (𝑎T) and one everywhere afterwards. From the data shown in Figure 4E where each point (𝑆(𝑎)) is an individual astrocyte response with its percent area (𝑎) domains active and if the soma was active or not denoted by a 1 or 0 respectively. To determine 𝑎T in our data we iteratively subtracted 𝐻(𝑎) from 𝑆(𝑎) for all possible values of 𝑎T to create an error term over 𝑎. The area of the minimum of that error term was denoted the threshold area.

Comments on revisions: Even with the added explanations, I am still not sure that the data show a specific threshold, or that the statistical model enforce a threshold onto the data. The data in Fig. 4G does not in my view clearly show a clear threshold as suggested. The analyses are strengthened with an added statistical modeling, however, the details of the modeling is not presented in the manuscript as far as I can see. As a bare minimum the statistical packages/tools used, the model details and goodness of fit as residual plots must be shown/commented.

The description of methods should have been considerably more thorough throughout. For instance which temperature the acute slice experiments were performed at, and whether slices were prepared in ice-cold solution, are crucial to know as these parameters heavily influence both astrocyte morphology and signaling. Moreover, no monitoring of physiological parameters (oxygen level, CO2, arterial blood gas analyses, temperature etc) of the in vivo anesthetized mice is mentioned. These aspects are critical to control for when working with acute in vivo two-photon microscopy of mice; the physiological parameters rapidly decay within a few hours with anesthesia and following surgery.

Authors reply: We have increased the thoroughness of our methods section. Especially including that body temperature and respiration were indeed monitored throughout anesthesia.

Comments on revisions: Bath temperature for slice experiments, or cutting conditions are still not reported. For the in vivo experiments, it must be commented that this level of physiological monitoring for acute in vivo brain physiology experiments (self breathing, no control of O2/CO2) is barely adequate and could represent a considerable caveat of the study.
