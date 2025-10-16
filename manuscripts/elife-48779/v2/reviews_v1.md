# Peer review - Round 1

Editors:
- Alexander Borst, Max Planck Institute of Neurobiology Germany

Reviewers:
- Armin Bahl, Harvard University United States

## Review text

DOI: [10.7554/eLife.48779.023](https://doi.org/10.7554/eLife.48779.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "An arbitrary-spectrum spatial visual stimulator for vision research" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Armin Bahl (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

General:

The manuscript "An arbitrary-spectrum spatial visual stimulator for vision research" by Franke and colleagues describes the design of a new type of visual stimulator for vision neuroscience. The basic idea of this study is to use the increasingly popular, commercially available LightCrafter system in combination with a set of precisely tuned and filtered LEDs. Such an arrangement provides optimal experimental control over the color spectrum and temporal properties of the visual stimulus, features that are fundamentally needed for studies of color vision and generally helpful when visual stimulation is combined with fluorescent microscopy. The most attractive feature of this system is that it can be adapted to any spectral channels desired by the experimenter, and it can be tightly controlled to avoid visual stimulation during fluorescence image acquisition.

The authors provide a rigorous and detailed description of their system, including measurements of brightness gamma correction, spatial and temporal resolution, and chromatic aberration. Further, the authors test their visual stimulator under three different configurations and in two example biological applications, one in mouse retina explants and one in in vivo zebrafish larvae, showing that the visual stimulator behaves as expected. While modified LightCrafters have been extensively used in multiple previous studies in different model organisms, a detailed assembly manual for the use in visual research has been missing so far. In particular, the description of a two-projector system, allowing for up 6 arbitrary color channels to be presented, is novel and exciting. The work, therefore, is of general interest to the visual neuroscience community as a whole and should provide significant help for other researchers planning to implement such systems and adapt them to their specific needs. This constitutes a great service to the field.

Specific:

1) Because their system relies on commercially available LightCrafters, the authors should introduce them earlier in their manuscript, already in the Introduction (for example after the fourth paragraph). Here, the authors should also acknowledge and cite other studies (mouse retina, flies, zebrafish,.…) that have modified such systems by replacing LEDs and adding filters to improve spectral specificity. Moreover, when introducing this system, the authors should also mention that UV-optimized LightCrafters exist commercially. Moreover, it is important to note that the LightCrafter sequentially activates the different color LEDs (this is already described later in the manuscript, but it would help to have this in the Introduction. For example, the authors could move the opening sentence of the fourth paragraph of subsection “Separating light stimulation and fluorescence detection” into the Introduction). Finally, it would be nice to know if other studies in systems neuroscience have already used the fiber-coupled version of the LightCrafter.

2) In the description of the stimulator, it does not become clear whether it is at all possible to project stimuli that consist of spatially patterned multi-chromatic light, for example a blue-green square-wave grating. Since the electronics of the LCr control the timing of the LEDs, this arrangement should allow for the described external light engine (when controlled by the LCr electronics) to provide multispectral stimulation. It would be important to point out explicitly how this can be realized with the described system.

3) For readers wishing to rebuild such a system, I suspect that the most challenging part is the printing and soldering of the circuit boards controlling the LEDs. Here, more information about these boards would help. The authors seem to have uploaded their designs as Gerber files to the provided github folder. Could the authors explain (briefly in the text and in more detail in the github readme.md) how to load these files and how to send them to manufacturing? What software did the authors use for the design, what software (open-source) do they recommend to the reader? Additionally, it would be nice to have an actual image of the PCB board drawings in a supplementary figure as well as a table of the needed electrical components.

4) The authors say that the four-channel zebrafish stimulator provides a more general solution. When does the simpler stimulator fail? Would the latter circuit board design also be fine with the two-channel mouse stimulator? Is it correct to conclude that for the four-channel zebrafish stimulator, one would need 2 boards as in Figure 2—figure supplement 5F and 4 boards as in 5G? What external power supply and what voltage do the authors drive their LEDs with in the two circuit board designs, or are all LEDs always powered by the LightCrafter?

5) Please provide a more detailed drawing and explanation of the collimator system and add the missing parts to Table 2. What holds the LEDs firmly in place and are they cooled via fans? What holds the bandpass filters in place, etc.? Are some of the parts 3d-printed? If so, which ones?

6) The authors have characterized the spatial properties of the "through-objective-configuration" but have not done this for the "through-the-collimator" configuration and for the side projection in the zebrafish preparation. I assume they have focused only on the former configuration as passing light patterns through the objective might lead to unexpected distortions while in the latter two configurations, this is less of a problem. Is this true? If so, the authors should say why such quantification has only been done for the through-the-objective configuration. Otherwise, please provide respective measurements.

7) Is the ScanM software for the microscope from Sutter or is it self-written by the group? According to their website, the Sutter MOM microscopes come with a software called MScan. How are these two software packages related, or is this the same? Please provide a link to this software if it is open-source or point to the Sutter website.

8) Do the authors gate the PMTs during the retrace period in order to protect the PMTs? Would this actually be necessary? If yes, is this automatically done by the MOM microscope software? The authors further make a point that scan patterns like spiral scanning or back scanning patterns have little or no retrace period (subsection “Separating light stimulation and fluorescence detection”). The authors should elaborate on how the temporal separation would work without retrace periods?

9) The authors talk about application of their visual stimulator for studying retinal explants and larval zebrafish vision. Could the authors also discuss the use of their system in other models, such as Drosophila? Perhaps the authors could provide Drosophila photoreceptor spectra in the supplement and describe what changes would be needed in the zebrafish system to optimize the design for Drosophila? If feasible, the authors might even provide a more generalized version of the zebrafish calibration ipython notebook?

10) The authors nicely show the concept of the silent substitution protocol in the mouse preparation. Because of the 4 cone types in zebrafish, whose spectra are significantly more overlapping, such experiments are likely more complicated. In Figure 6, how do you make sure that UV is not just activating all cone types? Could the authors discuss that a silent substitution protocol as was done for the mouse retina could increase confidence about their UV specificity?

11) For the zebrafish stimulator system, one major additional advantage is that one can quickly modify the visual stimulus spectrum to separate it maximally from fluorescent probe detection. If one would like to image green probes, one could not use the green LED but all other LEDs. If one would like to image red probes, one could turn off the red LED and leave all other LEDs on. This makes the system more flexible compared to what is commonly used in the field (fixed wavelength, often red, and difficult to change within an experimental session) and interesting for researchers wanting to occasionally image red-shifted calcium indictors in the same microscope where they normally use GCaMP. Furthermore, their system allows one to fully turn off stimulation through software to study the circuit in complete darkness. In contrast, commonly used projector systems show always some residual light even when one sends black to the projector or monitor. Discussing these points would make their system even more interesting to a broad readership.

12) The authors mention that QDSpy generates a "compiled" version of the stimulus (subsection “Visual stimulation software”). What does this mean? Do the authors upload a "movie pattern" to the LightCrafter, which is then displayed in a loop?

13) In Figure 3F, are both peaks and colors s/cones? Where is the m/cone?

14) In Figure 2—figure supplement 2, the b-label should be in the second line of panels. The authors say that the "ringing" comes aliasing-related fluctuations with the 60 Hz projector (subsection “Separating light stimulation and fluorescence detection”) but could it also come from the on/off dynamics of the LED switching? Which circuit board design was used here, the one in Figure 2—figure supplement 5C or the one Figure 2—figure supplement 5F,G? In the latter, would the dynamics look similar? If the authors have measured this already, it would be nice to see this in the supplement, or at least mention it.

15) The authors discuss the possibility to use mechanical choppers as blanking signals (subsection “Potential issues and technical improvements”). Why is the design of the "blanking" circuits more demanding when LED power is higher? Because of on/off dynamics of the LEDs? Are there systems neuroscience papers that the authors can cite that have already used mechanical choppers during fluorescent imaging?

16) Subsection “Visual stimuli for current animal models”: This section on the range of photopigments in different species is interesting, but such detail is not really required in this context. If the authors wished to shorten the Introduction, this is a section that could be abridged a bit.

17) Subsection “Stimulator design” paragraph one: "beamer" is rather colloquial. Perhaps "digital projector"?

18) Subsection “Stimulator design”: ("small footprint"): The actual dimensions (i.e., L x W cm) would be a nice addition to give the reader an immediate idea of the size without poring through the TI literature.

19) Subsection “Stimulator design” paragraph two: ("coupled by a light guide"): It would be nice to have a bit more detail here about how the external LED input is introduced to the LCr. Presumably some internal optics need to be removed from the LCr, and an entry port must be fashioned. How critical is the alignment of the incoming signal?

20) It is not clear, why spectral separation of visual stimulation and fluorescence detection is necessary, if the temporal separation approach works. In general, it seems that spectral separation reduces the claimed versatility of the stimulator. Related to that, Figure 2—figure supplement 3 is very hard to understand. The curves should be labeled better. Second, it seems like for the zebrafish-stimulator the green LED is not transmitted at all by the dichroic mirror.

21) The discussion of the paper should provide an outlook on potential applications that require the design of this stimulator.
