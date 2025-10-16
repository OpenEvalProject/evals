# Peer review - Round 1

Editors:
- Martin Vinck, Ernst Strüngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66429.sa1](https://doi.org/10.7554/eLife.66429.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

It is commonly thought that rodents are functionally blind when their surroundings are illuminated with light of longer wavelengths, which humans perceive as red. Nikbakht and Diamond challenge this assumption, and show that rats can accurately discriminate different objects that are illuminated only by red light. This result has important implications for the design of experiments and housing of rodents, and demonstrates that rodents can perform perceptual tasks despite the weak activation of retinal photoreceptors.

Decision letter after peer review:

Thank you for submitting your article "Conserved visual capacity of rats under red light" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Nick Steinmetz (Reviewer #3); Katrin Franke (Reviewer #5).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. Overall the reviewers were very positive about this study. They identified a number of Discussion points and further analyses to improve the paper.

Essential revisions:

1) We recommend that the authors comment on at least three applications that they haven't mentioned, which are additional points of impact of the study:

i) Studies of visual development and plasticity in rodents often use "dark-rearing" or days/weeks of darkness as a way to test the visual system under conditions of no stimulation; however, red light is used in husbandry tasks during these times, and any visual experience during those times could severely confound the interpretation of such studies (to pick one recent example, Kowalewski.… Kuhlman Current Biology 2020).

ii) Red light sources are often used in optogenetic perturbation experiments and might be assumed to be invisible to the subject, an assumption clearly invalid. In fact there was a paper with a similar finding to the authors (and to Niklaus et al) in this context – Danskin… Waters Plos One 2015.

iii) Quite some studies nowadays do eye or whisker monitoring and some conclusions of neural activity in the dark could very well be affected by these conclusions. Another point is place field monitoring in the dark – an experiment that has been quite fundamental for the hippocampal field.

2) The photon absorption rate depends on the sensitivity curve of the visual pigment expressed by the photoreceptor and on the light intensity. As stated by the authors in the Discussion, it has been shown that mammalian photoreceptors can be activated by infrared light if the intensity is strong enough – both by single photon and two photon events. As a result of this dependence on intensity, it is critical that the authors carefully measure and report the light intensity used in their experiments and ideally relate this to the expected photoreceptor activation, e.g. as photo-isomerizations per second. In addition, we suggest to discuss the rationale behind using this intensity range in their experiments. Together, this will help other researchers to interpret these interesting behavioral results and adjust their experimental setup accordingly.

The authors did not attempt to present a matching white light that would activate the rods or the cones in the same manner and investigate adaptation. This should be discussed and considered. Furthermore analysis on the extent to which the cones and the rods would be driven in the red light range would be very helpful.

The way in which the LED data is presented and analyzed should be improved. In particular, the authors seem to show fits and they are shown on a linear scale. The authors should show the raw spectrometer values and show these on a logarithmic scale in proper physical units in order to assess how much energy the LED generates in the normal vision range. With respect to intensity calibration of light sources, we suggest to include additional information in the manuscript. The authors mention in the Methods that they use a calibrated spectrometer for intensity measurements. Does this also account for different sensitivity of the spectrometer across different wavelengths? How do you transform spectrometer output to irradiances shown in Figure 1—figure supplement 2? And what is the unit of irradiance in this figure? Did the authors calibrate the different LEDs such that they result in the same irradiance during experiments? We suggest to include all these points into the Methods section. Also, please use absolute and not normalized spectra to compare intensities across LEDs – see Figure 1D. In addition, we believe it is important to (i) state the absolute intensities used in the experiments in the Results section, (ii) relate these intensities to expected photoreceptor activation and also intensities used in common experimental designs, and (iii) discuss the rationale behind using these intensities during experiments. This will help the reader to interpret the results. For example, did the authors pick these intensities because they are regularly used to dark adapt rats during experiments? Did the authors also test other intensities?

If there would be any concern left here after these analysis, one solution could be to use monochromatic lasers for the experiment.

We further suggest to add a simple control experiment to exclude any light contamination in the experimental setup. For that, the authors should position the spectrometer head at the position of the rat's head during behavioral experiments and record both background light levels and spectra of all LEDs. While this is unlikely to interfere with the experiments, it is a fast test that could be added as a supplementary figure.

3) The paper needs to be improved in terms of considering the mechanisms:

i) The discussion on this needs to be improved and extended. These findings likely have a fairly straightforward explanation.

ii) It goes beyond the scope of the paper to investigate whether this depends on cones, rods or even two-photon effects (note that this is unlikely to explain the data given the wavelength results that they describe, this may have been a bit misplaced). The most straightforward explanation is that the small drive of the cones and rods, combined with adaptation mechanisms, is sufficient to perform the task at hand. This seems testable by using very low-intensity green light (hitting the M-cones and the rods) that elicits a similar drive. This would show there is nothing special about red here, it just means that rats can do this kind of task under very low-level lighting conditions.

iii) Another very simple experiment that could have been considered is to prevent adaptation, so first prevent adaptation by using green or white light at normal intensity and then put the animal in the red condition – this should prevent the animal from doing the task. The authors write that "Rats were dark-adapted in a light free environment for 20-30 minutes prior to each session". Was this a necessary step?

4) The normalized irradiance plot in 1D does not extend below 350nm though it is stated that rats have cones with peak sensitivity ~360nm. So, is it possible that the 630-730nm wavelength LEDs also give off a small amount of 300-350nm UV light, and this is used by the rats for discrimination? How can this be ruled out? Many long-pass optical filters also pass some light of much shorter wavelengths than the cutoff - to pick one example, see the spectrum for the DMLP650 on this page (https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=3313). I don't know whether the LEDs in this study obtain their wavelength selectivity from anything at all related to the mechanisms of filtering in DMLP650 or similar - I'm not an expert - but it seems like it must be ruled out.

5) What accounts for the difference in findings relative to Jacobs et al 1991? I think this paper is the most classic/foundational, and it included a behavioral test of visual function, but concluded no behavioral sensitivity beyond 600 nm. I think the authors ought to indicate what they think accounts for the discrepancy in conclusions between that work and the present. Difference in species? Difference in behavioral task design? Difference in light source? Difference in range of wavelengths tested? Different analytical methods used to draw conclusions?

6) In the introduction, it is stated that Rocha et al 2016 found no ERG response above 620nm, while in the discussion it is stated that Niklaus et al 2020 found ERG responses to 650nm. Are the authors claiming that Rocha et al 2016 are simply wrong? If so, it would seem more appropriate to raise that study and call it into question in the discussion rather than the introduction - as is, that study is presented as accepted fact and is never revisited or questioned, which I found very confusing.

Reviewer #1:

This paper challenges a long-standing dogma in the rodent field, namely that rodents don't see in red light. The paper performs careful behavioral analyses to show that rats can indeed see (discriminate orientations) under red light condition. Even though the paper does not explain why this happens, the findings are likely of great interest to rodent vision scientists, and rodent researchers using infrared for e.g. housing and monitoring of the animal (eye, location). I have some concerns w.r.t. the purity of the LEDs. The discussion of the paper in terms of mechanisms should be strongly enhanced. I was surprised that the authors did not attempt to present a matching white light that would activate the rods or the M-cone in the same manner and investigate adaptation. Furthermore I expect more analysis on the extent to which the M cones and the rods would be driven in the red light range.

– The way in which the LED data is presented and analyzed should be improved. In particular, the authors seem to show fits and they are shown on a linear scale. The authors should show the raw spectrometer values and show these on a logarithmic scale in proper physical units in order to assess how much energy the LED generates in the normal vision range.

– Related to this, it would be straightforward to calculate how much the rods and cones are driven by the remaining white light and compare this to the extent to which they are driven by the red light.

– If there would be any concern left here after this analysis, I would recommend using monochromatic lasers for the experiment.

– The paper does little in terms of dissecting mechanisms:

1) The discussion on this needs to be improved and extended massively. I don't think these findings are mysterious but likely have a fairly straightforward explanation.

2) I think it goes beyond the scope of the paper to investigate whether this depends on cones, rods or even two-photon effects (note that this is unlikely to explain the data given the wavelength results that they describe, I felt this was a bit misplaced). it would be straightforward to obtain some minimum mechanistic insight. The most straightforward explanation is that the small drive of the cones and rods, combined with adaptation mechanisms, is sufficient to perform the task at hand. This seems testable by using very low-intensity green light (hitting the M-cones and the rods) that elicits a similar drive. This would show there's nothing special about red here, it just means that rats can do this kind of task under very low-level lighting conditions.

3) Another very simple experiment that could be added is to prevent adaptation, so first prevent adaptation by using green or white light at normal intensity and then put the animal in the red condition – this should prevent the animal from doing the task. The authors write that "Rats were dark-adapted in a lightfree environment for 20-30 minutes prior to each session". I guess, this was a necessary step.

– It would be useful to discuss a bit more practical implications. Quite some studies nowadays do eye or whiskerre monitoring and some conclusions of neural activity in the dark could very well be affected by these conclusions. I'm also thinking of place field monitoring in the dark – an experiment that has been quite fundamental for the hippocampal field.

Reviewer #3:

I think the authors actually undersell the full impact of this work, as it bears on at least two applications that they haven't mentioned:

1) Studies of visual development and plasticity in rodents often use "dark-rearing" or days/weeks of darkness as a way to test the visual system under conditions of no stimulation; however, red light is used in husbandry tasks during these times, and any visual experience during those times could severely confound the interpretation of such studies (to pick one recent example, Kowalewski.… Kuhlman Current Biology 2020);

2) Red light sources are often used in optogenetic perturbation experiments and might be assumed to be invisible to the subject, an assumption clearly invalid. In fact there was a paper with a similar finding to the authors (and to Niklaus et al) in this context – Danskin… Waters Plos One 2015.

Reviewer #4:

This study demonstrates that Long-Evans rats accurately discriminate the orientation of visual gratings illuminated by red light and far red light (wavelengths between 626 and 729), despite lacking a cone type with a peak absorbance at long wavelengths (>620). This important study follows recent work demonstrating that there are significant retinal responses to the same wavelengths of light in both rat and mouse species commonly used in behavioral and neural circuit function studies. The demonstration that rats retain clear form vision and can demonstrates accurate visually evoked behavior under "red-light conditions has important implications for studies of rodent visual perception which may have previously assumed "blindness" when the environment is illuminated by long wavelengths of light. Likewise, housing/rearing recommendations for rodents and possibly "dark" rearing studies not completed without any light, may be impacted by this study if experimenters used red light conditions to provide intermittent care for animals and assumed it was similar to no light or night-time conditions.

The major claims are well supported by the presented psychometric functions of the study subjects. The Authors also provide sufficient evidence that they accurately measured the intensity and wavelength span of their light sources and can therefore eliminate differences in light intensity, or overlap from neighboring wavelengths, as alternative explanations for their robust behavioral data.

This study will set a new standard and raise awareness of the need to stop considering "red-light" conditions as the same as no light or infrared conditions.

I'm at a loss to think of anything to improve the study substantively. It's a clear and tight study. The stimuli appear accurately measured and controlled- the behavior is beautiful (as much as behavior can be) and the specific study design was perfect for the question. It is clear these rats can see the stimuli and there doesn't appear to be any other explanation other than the ability of the rats to see in those narrow bands of red light.

Reviewer #5:

In the study "Conserved visual capacity of rats under red light", Nader Nikbakht and Mathew Diamond quantify the behavioral visual performance of rats under red and far-red light illumination. Due to the lack of a red-sensitive photoreceptor type present in e.g. humans and other primate species, rodents are often considered functionally blind under red light and vision researchers are regularly using this property in their experimental design. Here, the authors demonstrate that rats preserve their visual capacity in an orientation discrimination task under red light illumination up to ~650 nm, with reduced performance at ~730 nm and no visual capacity for wavelengths of 850 and 930 nm. These results resonate well with another recent study reporting robust photoreceptor responses upon red light application in rats (Niklaus et al., 2020). Together, this challenges the view that red light is invisible to rodents and suggests to reconsider common experimental practices.

In general, this study is well-written, the data is clearly presented and the conclusion that rats maintain their visual capacity under red light is supported by the data. The study addresses an important question in animal research and I believe that the results will be of great interest to the vision research community – especially because rodents have become a prominent model species in vision research over the last decade.

However, I have the following comments:

1. The photon absorption rate depends on the sensitivity curve of the visual pigment expressed by the photoreceptor and on the light intensity. As stated by the authors in the Discussion, it has been shown that mammalian photoreceptors can be activated by infrared light if the intensity is strong enough – both by single photon and two photon events. As a result of this dependence on intensity, it is critical that the authors carefully measure and report the light intensity used in their experiments and ideally relate this to the expected photoreceptor activation, e.g. as photoisomerizations per second. In addition, I suggest to discuss the rationale behind using this intensity range in their experiments. Together, this will help other researchers to interpret these interesting behavioral results and adjust their experimental setup accordingly.

2. With respect to intensity calibration of light sources, I suggest to include additional information in the manuscript. The authors mention in the Methods that they use a calibrated spectrometer for intensity measurements. Does this also account for different sensitivity of the spectrometer across different wavelengths? How do you transform spectrometer output to irradiances shown in Figure 1—figure supplement 2? And what is the unit of irradiance in this figure? Did the authors calibrate the different LEDs such that they result in the same irradiance during experiments? I suggest to include all these points into the Methods section. Also, please use absolute and not normalized spectra to compare intensities across LEDs – see Figure 1D.

3. In addition, I believe it is important to (i) state the absolute intensities used in the experiments in the Results section, (ii) relate these intensities to expected photoreceptor activation and also intensities used in common experimental designs, and (iii) discuss the rationale behind using these intensities during experiments. This will help the reader to interpret the results. For example, did the authors pick these intensities because they are regularly used to dark adapt rats during experiments? Did the authors also test other intensities?

4. Finally, I suggest to add a simple control experiment to exclude any light contamination in the experimental setup. For that, the authors should position the spectrometer head at the position of the rat's head during behavioral experiments and record both background light levels and spectra of all LEDs. While this is unlikely to interfere with the experiments, it is a fast test that could be added as a supplementary figure.
