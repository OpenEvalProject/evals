# Peer review - Round 1

Editors:
- Felix Campelo, https://ror.org/03g5ew477 Institute of Photonic Sciences Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76308.sa0](https://doi.org/10.7554/eLife.76308.sa0)

This paper will be of interest to the structural biology community and people working on cryogenic fluorescence microscopy. This paper is a clear step forward in the use of single-molecule localization microscopy at Å resolution, thanks to low-temperature polarized super-resolution imaging and advanced data processing algorithms.


---

# Peer review - Round 1

Editors:
- Felix Campelo, https://ror.org/03g5ew477 Institute of Photonic Sciences Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76308.sa1](https://doi.org/10.7554/eLife.76308.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Deciphering a hexameric protein complex with Å optical resolution" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Volker Dötsch as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Sophie Brasselet (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All three reviewers of this manuscript have pointed out important questions that I'm convinced will help the authors to resubmit a revised paper that is much stronger and clearer. The detailed reviews are enclosed in this email, and I would strongly encourage the authors to address all the questions and comments raised in those reports. That being said, the most important points are listed here (see referee reports for the details):

1) About the non-Gaussian shape of a 3D-oriented dipole PSF: what is its effect on localization precision?

2) Discuss the limitations of the method: requirement for no dipole rotation, orientation discrimination, etc.

3) Discuss a more general/wider applicability of the method: how can this be applied to non-symmetric/unknown complexes. How necessary is it the use of particle symmetry to determine the structures?

4) Discuss the reliability of particle discrimination based on the fluorophore polarization state.

5) Provide a better/fairer comparison of this technique to EM (e.g. number of needed particles, low yield in determination, etc.)

6) Expand on the methods (especially because this is a methods paper), in particular in the image analysis bit.

Reviewer #1 (Recommendations for the authors):

Some points, detailed here, need to be addressed to clarify the findings, their conclusion and the claims.

1. Effect of the 3D orientation of the fluorophores.

1.1 Even though the used NA is low and the incident polarization is in the sample plane, the localization precision required here is extreme and necessarily comes in competition with the inacuracy of PSF-centroid determination when the dipole is oriented in 3D. In particular, PSFs from 3D dipoles are not symetric Gaussians anymore. It is quite surprising that the 3D-orientation bias does not surpass, in some situations, the other bias sources in the reported data. This bias needs to be estimated and introduced in the localization accuracy estimation, together with the other inaccuracy sources (noise, drift).

1.2 Is the presence of the mirror-enhanced substrate modifying the expected brightness from dipoles at different axial positions, as well as the 3D-orientation bias mentioned above?

2. Orientational and time emission dynamics of the fluorophores.

2.1 The orientation of the dipoles is considered fixed at low T. The authors should give the expected number for the rotational diffusion of the fluorophore. We would expect that if some degree of rotational motion is permitted by the linker between the dipole and protein, this could be an issue for the reconstruction of the information, even at low T since more orientations will be probable for the measured dipoles.

2.2 It is not clear how the time dynamics of emission of the fluorophores affects the reliability of the discrimination of the different oriented dipoles in the time traces recorded. Is there any need for fine-tuning this on-off dynamics as well as the recording time of the measurement such as only one dipole emits at a time ? Optimal settings rules should be mentioned.

3. Orientational discrimination of fluorophores.

3.1 The authors mention in line 126 “The maximum number of resolvable polarization states per protein is currently limited to fewer than 5, dictated by the width of the polarization histogram”

How is this number 5 extracted from the width of the histograms, and how does this number depend on the signal level, possible presence of orientational mobility (see above)?

3.2 Would this number increase if the measurement also includes the quantification of the 3D orientation of the dipoles as mentioned below? If the measurement also includes spectral discrimination in addition to polarization discrimination?

3.3 The previous work by the authors (Boning et al.,) involved important signal thresholding, which was determining in the final dipole-distances assessment. How necessary is the signal thresholding here and what how is the choice of this filtering performed?

3.4 The authors mention in line 128 the necessity to exclude cases where the expected number of polarization states is not well resolved. What is the origin of this effect and is this also a limit of the unsupervised statistical learning algorithm used to treat the time traces?

3.5 The authors mention an angular resolution required for resolving 3 vs 6 fluorophores in a structure. How is the experimental angular resolution measured and what are the experimental sources of errors that can affect this resolution?

4. Classification and reconstruction.

4.1 The fluorophores assignment relies on a robust supervised classification procedure and template matching, which decreases the number of unknowns. How would this classification perform if the structure would contain unknown parameters?

4.2 In Figure 3 —figure supplement 2, it is not visible by eye that some of these figures belong to one class rather than another: some of them look very similar (e.g. aligned 3 dots) and belong to different classes.

4.3 Table S1 shows that the yield to reconstruct 3D information is very low (for ClpB, 100-200 particles are used out of more than 23000 particles detected initially). A lot of particles are also excluded from the analysis because a low-confidence score (line 202). What would be needed to increase this yield and increase the confidence score?

5. Methods

5.1 Is the fact that there is an ambiguity on the projection angle retrieval a problem? Since the orientation measured is confined in the [0-90{degree sign}] range, can't the orientation discrimination be problematic if a whole angle sector is missed in the angles determination?

5.2 How is the 100 photon/frame threshold (Figure S3 legend) chosen, what is the rationale behind in terms of estimation precision and accuracy? Isn't intensity thresholding also excluding 3D dipoles orientations?

5.3 The authors mention in line 160 a model to extract the side lengths of the projected triangles, what are the detail and hypotheses of this model?

5.4 The 3D protein orientation is linked to the spatial repartition of the fluorophores, however there is no mention of the possibility to use the 3D z position of the fluorophores to infer such a 3D information. Can't this axial position be exploited?

5.5 There are several recent techniques developed to infer the 3D orientation from emitting dipoles (using PSF engineering and/or polarization splitting, possibly using radial-polarization filtering). The measurement of the 3D orientation of the fluorophores would be of great value to complete the information with an additional angular parameter, which could increase the number of measurable fluorophores. The authors should comment on this, and possibly test this extension of the approach.

5.6 The abstract (line 43) states that the method “promises to provide crucial insight into intrinsic, environmental and dynamic heterogeneities of biomolecular structures.” The present method requires a large amount of data to be collected in the context of a known, fixed protein structure which density is highly controlled. It seems therefore very robust in the limited framework of low-level labelling, immoblilized and low concentration proteins, however it is difficult to envision its application in a native, dynamic configuration where diffusion potentially comes into play. The authors should provide more detail about what would be the ingredients needed to enlarge the application range.

Reviewer #2 (Recommendations for the authors):

In Weissenburger 2017, the authors already presented the reconstruction of four fluorophore sites within streptavidin. Overall, I think the manuscript presents an advance of previous developments by the authors, but the generalizability and applicability to more complex samples remain partly open. This could be discussed in more detail.

1) Fluorophore discrimination depends on the correct assignment of the different polarization states. It would be good to include a representation of the uncertainties in fluorophore assignment and the resulting filtering procedure. For clarity, it would also help to color-code the different fluorophores as identified from the polarization state in the scatter plots. For example in Figure 2A, some spots appear larger or have an irregular shape, which could be associated with the uncertainty (as mentioned above) or the result of overlapping molecules for which a color code could help.

2) I am wondering about how generalizable the described reconstruction approach is or can be with respect to non-symmetric complexes or mixed samples of multiple protein species. To what extent does the reconstruction rely on prior knowledge of the investigated proteins? For example, the simulations used to classify the triangle images in the case of ClpB. What are the boundaries of these simulations (distance, angle, etc)? Is it possible to combine this with existing pattern extraction schemes (i.e. Curd, 2020)? Also, would more classes be helpful in increasing the precision or applicability of the approach? Particle reconstruction typically relies on many more classes unless some of them are redundant due to symmetries.

Reviewer #3 (Recommendations for the authors):

The paper by Mazal, Wieser and Sandoghdar presents a method to image molecular complexes with light microscopy, but still obtain resolutions/localization uncertainties of fluorescent labels that have been limited to cryo EM.

This submission build upon earlier work from the same group (Weisenburger 2017 and Boning 2021). The polarisation detection does not increase the sparsity compared to Weisenburger, but on the detection side they can identify different emitters based on their fixed dipole emission as shown in Boning. They further improve the sparsity, by explicit under labelling which later is compensated by particle registration and averaging. Compared to Boning the submission adds 3D reconstructions of two molecular complexes from 2D under labelled structures. The polarisation and localization method is improved technically, but the concept was already there.

The presented methodology and results are overall very nice.

In the following a few remarks and details that could help to improve the manuscript or that are unclear to me.

– Abstract: many it would good to directly state to how many sites you extend the method (l34).

In how far was the use of a supervised classification and use of particle symmetry really needed? (l93) Typically in cryoEM the use of symmetry is only needed to increase the resolution or in the absence of a large number of particles. What does the method deliver if the symmetry is not implied? That is a strong prior knowledge assumption and hinders discovery of new insights. The supervised classification is similar as model assumptions could be brought into the reconstruction.

In the introduction it would be nice to mention the idea of Hafi et al., Fluorescence nanoscopy by polarization modulation and polarization angle narrowing. Nature Methods, 11:579-584, 2014. and also Hulleman et al., Fluorescence polarization control for on-off switching of single molecules at cryogenic temperatures. Small Methods, page 1700323, 2018. Similar ideas to exploit polarisation of the fixed dipole emitters have been introduced here too.

l112 the polarisation state give the in-plane dipole angle. Would the method benefit from an estimation of the polar angle in addition? around l125 this could increase the number of resolvable polarisation states, but this might not be the limiting factor but the sparsity of the blinking?

l132 After localizations and identifying emitters by their polarisation state, how is the average position computed? Is that done weighted by the photon count?

l162 The remark the only 119 particles are needed for a reconstruction and not many more as in cryo EM is a bit misplaced. The information density in the LM is very low (only the few coordinates of the particles), while the EM map is a full image with millions of pixels that contain information. In addition early LM particle averaging results have used also hundredth of particles only typically. In addition the benefit of increasing the number of particles in LM is diminishing, because the additional particles cannot improve the localization precision but only fill in missing information thereby increasing the SNR. For cryo EM the resolution scale as sqrt(N) with number of particles, for LM this is much worse and eventually zero.

l181 Could you provide the t_on and t_off for the emitters. The 50% underlabelling is based on their ratio?

l203 "better 3 nm" -> better than 3 nm.

l205 yield of 7,46% point and comma not correct. 2 digits behind comma not needed. In addition why was the yield so low? Even if you consider that the polarisation state removes 3/4 of the particles the yield is still low. In cryoEM most particles needs to be removed due to damage resulting from stress close to the air water interface. What could be the reason here?

l 217 The claim to "all possible orientations" is a bit strong. I do not see why the 3 citations, in particular Huijben and Sieben, cannot deal with data in all possible orientations. I would argue that up to now, either the particles in a top-down configuration have been images because the structure was 2D or in the case of the much used NPC because the nuclear envelope is running nearly parallel to the cover slip. Therefore the NPC only have a limited tilt range. In conclusion, the claim to being the first is a big too much, as this is certainly not a methodical advance.

l277 the amount of Trolox 1mM seems quite a lot. Is this needed to suppress triplet states?

l288 What is the physical pixel size of the camera. The model is not stated, but the back projected size is stated as 190 nm with a 100x objective. This information is also not present in the supplement of Boning2021.

l290-298 Image analysis.

This part is vague on the details. Is the code available? I think as the analysis is not standard this needs to be open. The Poisson-weighted Gaussian MLE, what is that? Fitting a Gaussian function with Poisson likelihood? Will not polarisation effects of the restricted dipole play a role already at 0.95NA? (see Stallinga 2010, Optics Express 18:24461 and Engelhardt 2010, NanoLetters 11:209). The drift correction is non-linear, but for the rest it is totally unclear how it works. However, that is quite important as the acquisition time is a bit less than 1h.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Deciphering a hexameric protein complex with Å optical resolution" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Volker Dötsch as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please, consider answering the 3 specific comments from Reviewer #3, which need no new experiments, just clarification in the text and maybe some simple extra data analysis.

Reviewer #2 (Recommendations for the authors):

The authors have done well in responding to my comments, which at least partly came from misreading and/or misunderstanding on my side. The paper remains a difficult read but shows a clear step forward in using low temperature to increase SNR in single-molecule imaging.

Reviewer #3 (Recommendations for the authors):

Overall the authors did a very nice job with the revision. I would support the publication of the manuscript.

point (2) I strongly disagree that classification is needed and an assumption of symmetry. Many published averaging techniques for LM deal exactly with the problem described by the authors "In that sense, the incompletely labelled object inherently behaves as a heterogenous sample with multiple labelling configurations and distances". This is why most of the cryo-EM algorithms fail when applied to strongly under labelled data, they see the different labelling states as different classes. Please have a look at the work of Heydarian et al., (Nat Methods 2018, Nat Com 2021), Sieben et al., (Nat Methods 2018), Salas et al., (PNAS 2017), Shi et al., (PLOS one 2019) and maybe others.

The question at hand is, if the under labelling here is so severe that indeed the above methods cannot deliver a good reconstruction. From my own experience somewhere between 30-50% degree of labelling is needed to obtain a meaningful reconstruction. However, this depends also on the absolute number of sites. Some of the above papers have open access code, it might be worthwhile to try this at least.

The approach to validate their model via the AIC is good. The idea from Curd et al., have been well incorporated as this method typically only can learn something for the nearest neighbour distance, exactly what it has been used for her.

point (5) The average best position of a set of localisations from the same molecule is typically done by photon weighted averaging not median computation? If there are strong outliers which suggest the use of the median, maybe it would be better to remove the outliers first and then compute a weighted average?

point (13) I see that the author fit a 2D Gaussian, at the expense of a bit of blurring due to model mismatch. I would expect that the random dipole orientation do not average about but give rise to a large standard deviation of the localization than strictly needed with a correct model fitting. The localization will be unbiased due to the randomness, but it will result in a bit of extra blurring.
