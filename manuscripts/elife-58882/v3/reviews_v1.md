# Peer review - Round 1

Editors:
- Ryohei Yasuda, Max Planck Florida Institute for Neuroscience United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58882.sa1](https://doi.org/10.7554/eLife.58882.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this revised manuscript, the authors demonstrated an extended field-of-view (eFOV), thin (<500μm) microendoscopes by adding aberration correcting microlenses fabricated by TPL. The performance of the microlens corrected eFOV endoscopes was evaluated with simulations on synthetic calcium data and in vivo activity imaging. In addition, the eFOV microendoscopes were used to investigate VPM activity correlated with locomotion, whisker movement, and pupil diameter. Cell-specific encoding in VPM during these behaviors is further scrutinized with statistical and machine learning methods. The presentation of the methods and the results are clear. The methods are useful and practical for increasing the FOV of ultrathin microendoscopes, removing one of the current limitations of small GRIN lens applications. The authors significantly improved the manuscript based on the reviewer's comments.

Decision letter after peer review:

Thank you for submitting your article "Extended field-of-view ultrathin microendoscopes for high-resolution two-photon imaging with minimal invasiveness" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Andrew King as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Darcy S Peterka (Reviewer #2); Kaspar Podgorski (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Your manuscript describes the development and use of microfabricated corrector lenses for improving GRIN lens imaging. These correction lenses increase the usable field-of-view (FOV) of a given GRIN lens, and improves the resolution. The approach was validated in a variety of samples. While the reviewers agree that the work will be potentially high impact, they feel that revisions with additional analyses would significantly improve the paper.

Reviewer #1:

In this manuscript, the authors demonstrated an extended field-of-view (eFOV), thin (<500μm) microendoscopes by adding aberration correcting microlenses fabricated bt TPL. Performance of the microlens corrected eFOV endoscopes was demonstrated with simulations on synthetic calcium data and in vivo activity imaging. In addition, the eFOV microendoscopes were used to investigate VPM activity correlated with locomotion, whisker movement, and pupil diameter. Cell-specific encoding in VPM during these behaviors are further scrutinized with statistical and machine learning methods. The presentation of the methods and the results are clear. The methods are useful and reasonably practical for increasing the FOV of ultrathin microendoscopes, which is a major limitation for small GRIN lenses. Overall, I recommend publication of the paper in eLife. Listed below are a number of concerns that we hope the authors can address in their revision to further improve the manuscript.

1) For the design and fabrication of the eFOV-microendoscope:

a) The authors presented four types of GRIN lenses (Type I-IV). Four different models of the GRIN lens are shown in subsection “Corrective lens manufacturing and microendoscope assembly”. It will probably help if the authors can explicitly indicate the Types with the model number.

b) It is claimed that the experimental result is similar to ray-trace simulation as shown in Figure 2. However, there is no comparison to support the claim. The high-order coefficient in the gradient profile in GRIN lens is usually not included in the optical model used for ray-trace. High-order aberration will thus not be reflected in the simulation. It would be important to know the difference between the simulation result and the experimental result. For example, the authors can add experimental data in Figure 2 or add simulation data in Figure 3.

c) For all the experiments, is it performed with the 2-photon polymerized lens with resin or with lens replica using a molded UV-curable adhesive? Is the aberration correction performance different from these two fabrication methods? Which material is the ray-tracing simulation based on?

d) What is the yield of the lens fabricated? How is the cured UV-curable adhesive detached from the PDMS mold? During imaging sessions, was there any damage on the lens?

e) How does the correction microlens affect the focal length of the GRIN lens. In other words, what is the allowable change in working distance before and after the correction?

f) There appears to be a much larger field curvature with the corrected GRIN lens. It would be helpful to discuss the impact of this on functional imaging.

g) Instead of AO with an active element (e.g., SLM), one could also put a fixed lens with the desired curvature in the place of the SLM. Compared to the microlens approach, one needs to modify the excitation path somewhat, but the lens can be fabricated using standard techniques and may be more accessible to most research labs. It might be informative to the readers to comment on this alternative approach.

2) For the data taken with the eFOV-microendoscope, there is ~2x improvement in FOV for type III lens (Figure 3G). However, in Figure 3—figure supplement 5C, the images before and after correction for type III lens is almost the same.

3) For the data simulation and analysis:

a) Analysis was shown to correlate whisking, locomotion and cell-specific encoding. Figure 6C and 6D show that locomotion is usually correlated with a higher ΔF/F. Could this be a result of the motion artifact during locomotion from the head-constraint mouse?

b) To simulate synthetic calcium data, different models (Gaussian Mixture, lognormal, etc.) are used to obtain the pixel intensity value as described in subsection “Generation of fluorescence time series”. It is mentioned that the model is obtained by fitting the experimental data. What criteria (e.g. comparing likelihood) is used to choose those specific models? What other distribution is tested to choose the best-fit model?

c) As mentioned in subsection “Analysis of field distortion and calibration of the pixel size”, the author used a gaussian profile to define axial resolution. It is probably better to fit with a Lorentzian function I(z)=〖(1/(1+〖(z/zR)〗^2 ))〗^2 for 2-photon excitation, where zR is the Rayleigh range of the gaussian focus. Not sure how large the difference will be between these two fits.

d) Figure 4D. It is not clear to me why the ROI number is smaller for the corrected lens than the uncorrected when the peak SNR value is small (e.g., less than 10). Can the authors add some explanations?

e) The authors claim that "pairwise correlation increased as a function of the radial distance of the pair in uncorrected probes compared to corrected ones." Figure 4M does not seem to show noticeable increase as a function of the radial distance for the uncorrected lens (left panel). Rather, it seems to show a noticeable decrease as a function of the radial distance for the corrected lens (right panel). Therefore, the statement does not seem to be supported by Figure 4M. This is confusing, and some explanation is needed.

4) There is a typo in the first sentence of subsection “Fabrication of eFOV-microendoscopes”. I believe it is (Figure 3—figure supplement 1C) instead of (Figure 1C).

Reviewer #2:

In this paper, the authors describe the creation and use of microfabricated corrector lenses for improving GRIN lens imaging. GRIN lenses are one of a few technologies (and the only one that is "mature") that allow for high resolution optical imaging in brains at depths beyond ~1.5 mm. These correction lenses a) increase the usable field-of-view (FOV) of a given GRIN lens, and b) improve the fidelity of signals extracted from regions-of-interest (ROIs), by decreasing the point spread function (PSF) volume. Both are important for high fidelity recording of neuronal populations. The paper is well written, and I find their demonstrations compelling. I think the work is of broad interest, and suitable for publication in eLife, after addressing a few concerns and questions.

My comments below are mainly critical, but I note that I think the paper overall is very good, and thorough, and I have high enthusiasm.

Given that the surface profiles begin their optimization from an analytical expression, It would be nice if the authors could comment on the likely maximal possible correction possible – that is on a GRIN lens with a GRIN relay of significant pitch, do they think microlenses would be similarly manufacturable or effective?

In the simulated imaging data, especially the figure, and SNR conclusions drawn from that, I think it is important to more clearly identify the results as "simulations". The authors do label and describe the data as such, however, because of the look of the figure, and in the Discussion, it is very easy to misinterpret as measured experimental data, rather than an in silico sim – perhaps panel shading on a-h would help?

Regarding the simulations, it was not clear what the "imaging" rate was set to be. I am curious why processes where not included in the in silico simulation. I would expect the corrected FOVs to have even better performance than uncorrected, if processes were included, and it would have been nice to explore. Further, I am not quite sure why the authors did not use a standard method to extract the putative ROIs, and compare that with their ground truth – it seems they considered the flaws of standard practice, and biased their sampling of ROIs directly – but I would think using a standard pipeline instead would have been more informative.

Along with this, in the real experiments, different methods were used to pick the ROIs – I am wondering if the authors could comment on the rational for the choices? I say this also, because while one would prefer to record more faithful signals directly, it isn't clear to me that some of the additional "mixing" that would occur between the ROIs would not be removed through source factorization.

The slow imaging rate also leads to higher correlations. Did the authors also collect signals at high frame rates? The basic optical properties would not change at higher rates, but 2-3 Hz is far from typical functional imaging rates. The gains in SNR may be more material at these higher frame rates too. Was it simply a microscope limitation that prohibited faster imaging?

For Figure 7, It is not clear to me why there should be a bias toward information away from the center assuming (semi) random placement of the GRIN- do the authors think that this is real, or simply a measurement artifact – the center of the FOV is nominally furthest from completely healthy tissue, so the slightly lower information reflects network damage? That would also affect the magnitude (but likely not the fundamental interpretation) of the spatial distribution of cells in the modules.

Reviewer #3:

In this paper, the authors describe a novel approach for improving two-photon imaging through thin GRIN-lens endoscopes by using a nanofabricated corrective lens. They validate the approach with in vitro measurements and simulations, and apply the technique to imaging a variety of samples, most notably somatosensory thalamus in awake, behaving mice.

The technique seems easy to apply and could advance the state of the art in several labs. Although I haven't done such experiments myself, I know from other groups that experiments are often sorely limited by their field of view. This paper presents an exciting solution to this problem.

I am enthusiastic about the work, but point out the following issues:

1) With uncorrected GRIN endoscopes, 3D imaging is possible. Do the corrective lenses affect the axial range that can be scanned this way, and if they do, how does this impact the total of neurons that can be recorded with a corrected vs uncorrected endoscope? Zemax simulations would be sufficient to address this.

2) I think the paper could do a better job of motivating the need for thinner endoscopes, particularly in the Introduction. Figure 5 leaves me wondering whether connections would really be disrupted by a larger endoscope. Figure 3—figure supplement 7 makes it clear that larger endoscopes and cannulae require removing a lot of structures, but the paper leaves it to the reader to imagine the consequences. Have there been published accounts of failure rates for different endoscope sizes? Perhaps your own experiences, or studies of e.g. amygdala or hypothalamus?

3) The methods used to segment/analyze calcium imaging data (subsection “Segmentation of simulated time series”) come off as somewhat straw-man. There are a variety of activity-based tools that can separate mixed signals from overlapping cells (PCA/ICA, NMF, CNMF, etc.), and these have been popular for (1P) endoscopic imaging. I wonder if such methods narrow the gap between uncorrected and corrected SNRs and correlations. The statements at the end of paragraph five of the Discussion seem a bit strong if this possibility has not been explored.

4) How chromatic are these corrections? The authors propose simultaneous functional imaging and optogenetic perturbations with these corrective lenses, but this would require the correction be useful across a large wavelength range (perhaps ~900nm and ~1040nm), which needs more evidence. Chromatic issues can easily affect 2P imaging even over the bandwidth of a femtosecond laser.
