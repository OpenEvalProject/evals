# Peer review - Round 1

Editors:
- Floris P de Lange, Donders Institute for Brain, Cognition and Behaviour Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37241.012](https://doi.org/10.7554/eLife.37241.012)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Stimulus vignetting and orientation selectivity in human visual cortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Floris P de Lange as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by David Van Essen as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Kendrick N Kay (Reviewer #2); Nikolaus Kriegeskorte (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript uses computational modeling and experimental measurements to make a compelling case that stimulus edge effects (or 'vignetting') may be a substantial source of apparent orientation tuning as measured using standard-resolution fMRI. The work is technically solid and carefully presented, and the topic will be of significant interest to the fMRI community (given the widespread use of multivoxel pattern analysis).

Essential revisions:

I have provided a summary of essential revisions. You will find more details, as well as additional points that need to be addressed, in the original reviews (appended below).

1) Tone down claims of novelty:

-The paper claims to introduce a novel idea that requires reinterpretation of a large literature. The claim of novelty is unjustified. Vignetting was discovered by Carlson et al., 2014 and in Wardle et al., 2017, Carlson's group showed that it may be one, but not the only contributing factor enabling orientation decoding. Carlson et al. deserve clearer credit throughout. See reviewer #2 point 1, and reviewer #3.

2) Provide a more nuanced coverage of the literature. E.g., the conjecture that the orientation preferences in fMRI measurements arise primarily from random spatial irregularities in the fine-scale columnar architecture doesn't seem 'leading' anymore in 2018, and more nuanced positions have been articulated since. See reviewer #1 point 1 and reviewer #3.

3) Discuss the broader implications of the study: the authors claim that the study has wide implications for many studies that used decoding of oriented gratings. But it is left unspecified what those implications are. Could the authors be more specific? For example, how should we reinterpret Kamitani and Tong, 2005 or Haynes and Rees, 2005? What wrong conclusions have been drawn, if we accept the notion that stimulus vignetting is the source of orientation decoding?

The significance of the present work might be further emphasized by relating it more broadly to the general approach of MVPA (i.e. using linear classifiers to decode activity). I believe the larger lesson, highlighted by the present work, is that even seemingly simple properties are in fact hard to isolate experimentally and that powerful approaches like classification can pick up on aspects of the data that might not be what the experimenter intended. See reviewer #1 point 4, reviewer #2 point 2.

4) Address/discuss whether decoding is still possible in the absence of vignetting effects, or is solely dependent on vignetting. See reviewer #1 point 2, 3; reviewer #3.

Reviewer #1:

The authors test the hypothesis that the orientation selectivity of responses in visual cortex, measured at a macroscopic scale, is caused by 'vignetting', i.e. second order changes in luminance caused by the aperture within which an oriented grating is presented. Using a computational model of neural responses in V1, they demonstrate the impact of vignetting on the model response, and confirm predictions made by the model in human fMRI measurements.

I find this a compelling manuscript, with a clear question that is of interest to many researchers. The results are expertly analyzed and clear cut, showing that stimulus vignetting may indeed be a major contributor to the orientation selectivity measured with fMRI. I have some comments related to the coverage of the literature, and a query about the implications of the study for the field.

1) Introduction section: "A leading conjecture is that the orientation preferences in fMRI measurements arise primarily from random spatial irregularities in the fine-scale columnar architecture (Boynton, 2005; Haynes and Rees, 2005; Kamitani and Tong, 2005)."

This conjecture was perhaps leading in 2005, but I don't think this is an accurate description of the state of affairs 13 years later, and it therefore seems a bit of a straw man. For example, a more nuanced view articulated by Swisher et al., 2010 from the Tong lab states that orientation information "can be found at spatial scales ranging from the size of individual columns to about a centimeter". I suggest the authors paint a more balanced picture in the introduction.

2) Subsection “Coarse-scale bias and stimulus vignetting: fMRI experiments”: "From this, we conclude that stimulus vignetting is a primary source of the coarse scale bias."

Why “a primary source”, rather than “a source”, or 'an important source'? It seems bold to conclude this based on a correlation of ~0.2-0.26 between the model and the data?

3) In the same section: "Decoding accuracy for the shifted between-modulator analysis was only slightly lower than within-modulator decoding accuracy".

Could the authors test whether this difference is statistically significant?

If the difference is significant, this could, as the authors point out, be due to the inner and outer radial edges. However, it could potentially also be caused by the fact that there is a small amount of orientation information present in the fMRI activity patterns that is not due to stimulus vignetting. The authors may also want to include this possibility in the text – even though they may find it unlikely.

4) Discussion section: "Our results provide a framework for reinterpreting a wide-range of findings on orientation selectivity, measured with both fMRI in human subjects and in single units."

This statement suggests that the study has wide implications for many studies that used decoding of oriented gratings. But it is left unspecified what those implications are. Could the authors be more specific here? For example, how should we reinterpret Kamitani and Tong, 2005 or Haynes and Rees, 2005? What wrong conclusions have been drawn, if we accept the notion that stimulus vignetting is the source of orientation decoding?

Reviewer #2:

The manuscript by Roth et al. uses computational modeling and experimental measurements to make a compelling case that stimulus edge effects (or 'vignetting') may be a substantial source of apparent orientation tuning as measured using standard-resolution fMRI. The work is technically solid and carefully presented, and the topic will be of significant interest to the fMRI community (given the widespread use of multivoxel pattern analysis). I have some comments, mainly conceptual/framing in nature, which should be relatively easy to address.

1) Wording and framing.

- There are a few places where I think the conclusions and claims should be toned down. For example, "vast number of previous studies" (Introduction section) and "wide-range of findings in the visual system". I assume the authors are referring to past studies that have used orientation stimuli in fMRI, and not the neurophysiology literature on orientation tuning in single neurons. While it is theoretically possible that vignetting effects may be influencing single-neuron response properties (since Gabor and grating patches are widely used as stimuli), it is not yet clear whether single-neuron studies need to be re-interpreted.

- The work of Carlson, 2014 involves modeling work that is similar to what is done in the current manuscript. Of course, the major advance of the present work is the demonstration of empirical findings, but this previous work might deserve more acknowledgment.

- Ultimately, a lot of the controversy regarding fMRI orientation decoding comes down to numbers, and it would be helpful to clarify what is meant by "coarse" and "fine". I assume the authors mean something to the effect that "coarse" is > 1 mm and "fine" is < 0.5 mm (or something like that).

2) Some big-picture perspective.

- The significance of the present work might be further emphasized by relating it more broadly to the general approach of MVPA (i.e. using linear classifiers to decode activity). I believe the larger lesson, highlighted by the present work, is that even seemingly simple properties are in fact hard to isolate experimentally and that powerful approaches like classification can pick up on aspects of the data that might not be what the experimenter intended. One way that we have conceptualized this (Naselaris, TICS, 2015) is that the orientation of a grating stimulus is not the only stimulus feature that can give rise to variance in data, and that classification can reflect a number of different stimulus features, such as those related to vignette effects, unless one does work to rule them out, e.g. by considering explicit computational models.

3) Acknowledgment of the limitations of the model.

- I think the main contribution of the current paper is the experimental results. The modeling analyses do provide value in that they demonstrate a concrete (and reasonably plausible) explanation of what could be driving the observed orientation-tuning results. However, as the authors recognize in the Discussion, there are many stimulus properties beyond what is characterized in the model that are known to affect V1 responses (e.g. surround suppression, contour integration, 2nd-order contrast effects, etc.), and which might also contribute to the orientation effects. Thus, the text could be clarified to acknowledge the limitations of the model and indicate what role the modeling results play in this specific paper. It seems that the role of the modeling results is to show concretely that imbalances in filter energy across orientations exist at stimulus edges and that this is one possible reason for finding orientation tuning in standard-resolution fMRI. (Note that I am not suggesting that the present paper needs to perform detailed model comparisons (in which different models are pitted to quantitatively account for individual voxel responses to a variety of stimulus conditions); that would be outside of the scope of this paper.)

4) Clarification of the modeled effect.

- It would be helpful to isolate and clarify the nature of the effect shown in Figure 2. One potential explanation is that for a linear filter stimulated with an optimal oriented grating, the filter shows a bigger response when the grating has a vignette edge orthogonal to the orientation compared to when the grating has a vignette edge parallel to the orientation. Is this the case in the model?

Reviewer #3:

Vignetting: interactions between grating and aperture edges might explain coarse-scale orientation-preference maps in V1 [I6 R8].

The orientation of a visual grating can be decoded from fMRI response patterns in primary visual cortex (Kamitani and Tong, 2005, Haynes and Rees, 2005). This was surprising, because fMRI voxels in these studies are 2-3 mm wide in each dimension and thus average over many columns of neurons responding to different orientations. Since then, many studies have sought to clarify why fMRI orientation decoding works so well.

The first explanation given was that even though much of the contrast of the neuronal orientation signals might cancel out in the averaging within each voxel, any given voxel might retain a slight bias toward certain orientations if it didn't sample all the columns exactly equally (e.g. Boynto,n 2005, Kamitani and Tong, 2005). By integrating the evidence across many slightly biased voxels with a linear decoder, it should then be possible to guess, better than chance, the orientation of the stimulus.

Another account (Op de Beeck, 2010, Freeman et al., 2011) proposed that decoding may rely exclusively on coarse-scale spatial patterns of activity. In particular, Freeman Brouwer, Heeger and Merriam, 2011 argued that orientations that are radial (aligned with a line that passes through the fixation point) are over-represented in the neural population. If this were the case, then a grating would elicit a coarse-scale response pattern across its representation in V1, in which the neurons representing edges pointing (approximately) at fixation are more strongly active. There is indeed evidence from multiple studies for a nonuniform representation of orientations in V1 (Furmanski and Engel, 2000, Sasaki et al., 2006, Serences et al., 2009, Mannion et al., 2010), perhaps reflecting the nonuniform probability distribution of orientation in natural visual experience. The over-representation of radial orientations might help explain the decodability of gratings. However, opposite-sense spirals (whose orientations are balanced about the radial orientation) are also decodable (Mannion et al., 2009, Alink et al., 2013). This might be due to a simultaneous over-representation of vertical orientations (Freeman et al., 2013, but see Alink et al., 2013).

There's evidence in favor of a contribution to orientation decoding of both coarse-scale (Freeman et al., 2011, Freeman et al., 2013) and fine-scale components of the fMRI patterns (e.g. Shmuel et al., 2010, Alink et al., 2013, Pratte et al., 2016, Alink et al., 2017).

Note that both coarse-scale and fine-scale pattern accounts suggest that voxels have biases in favor of certain orientations. An entirely novel line of argument altogether was introduced to the debate by Carlson, 2014.

Carlson, 2014 argued, on the basis of simulation results, that even if every voxel sampled a set of filters uniformly representing all orientations (i.e. without any bias), the resulting fMRI patterns could still reflect the orientation of a grating confined to a circular annulus (as standardly used in the literature). The reason lies in "the interaction between the stimulus region and the empty background" (Carlson, 2014), an effect of the relative orientations of the grating and the edge of the aperture (the annulus within which the grating is visible). Carlson's simulations showed that the average response of a uniform set of Gabor orientation filter is larger where the aperture edge is orthogonal to the grating. He also showed that the effect does not depend on whether the aperture edge is hard or soft (fading contrast). Because the voxels in this account have no bias in favour of particular orientations, Carlson aptly named his account an "unbiased" perspective.

The aperture edge adds edge energy. The effect is strongest when the edge is orthogonal to the carrier grating orientation. We can understand this in terms of the Fourier spectrum. Whereas a sine grating has a concentrated representation in the 2D Fourier amplitude spectrum, the energy is more spread out when an aperture limits the extent of the grating, with the effect depending on the relative orientations of grating and edge.

For an intuition on how this kind of thing can happen, consider a particularly simple scenario, where a coarse rectangular grating is limited by a sharp aperture whose edge is orthogonal to the grating. V1 cells with small receptive fields will respond to the edge itself as well as to the grating. When edge and grating are orthogonal, the widest range of orientation-selective V1 cells is driven. However, the effect is present also for sinusoidal gratings and soft apertures, where contrast fades gradually, e.g. according to a raised half-cosine.

An elegant new study by Roth, Heeger, and Merriam, 2018 now follows up on the idea of Carlson, 2014 with fMRI at 3T and 7T. Roth et al. refer to the interaction between the edge and the content of the aperture as "vignetting" and used apertures composed of either multiple annuli or multiple radial rays. These finer-grained apertures spread the vignetting effect all throughout the stimulated portion of the visual field and so are well suited to demonstrate the effect on decodability.

Roth et al. performed simulations, following Carlson, 2014 and assuming that every voxel uniformly samples all orientations. They confirm Carlson's account and show that the grating stimuli the group used earlier in Freeman et al., 2011 is expected to produce the stronger response to radial parts of the grating, where the aperture edge is orthogonal to the grating. Freeman et al., 2011 used a relatively narrow annulus (inner edge: 4.5°, outer edge: 9.5° eccentricity from fixation), where no part of the grating is far from the edge. This causes the vignetting effect to create the appearance of a radial bias that is strongest at the edges but present even in the central part of the annular aperture. Roth et al.'s present findings suggest that the group's earlier result might reflect vignetting, rather than (or in addition to) a radial bias of the V1 neurons.

Roth et al. use simulations also to show that their new stimuli, in which the aperture consists of multiple annuli or multiple radial rays, predict coarse-scale patterns across V1. They then demonstrate in single subjects measured with fMRI at 3T and 7T that V1 responds with the globally modulated patterns predicted by the account of Carlson, 2014.

The study is beautifully designed and expertly executed. Results compellingly demonstrate that, as proposed by Carlson, 2014, vignetting can account for the coarse-scale biases reported in Freeman et al., 2011. The paper also contains a careful discussion that places the phenomenon in a broader context. Vignetting describes a family of effects related to aperture edges and their interaction with the contents of the aperture. The interaction could be as simple as the aperture edge adding edge energy of a different orientation and thus changing orientation selective response. It could also involve extra-receptive-field effects such as non-isotropic surround suppression.

Another question is whether the vignetting effects Roth et al. demonstrate fully explain orientation decoding. The original study by Kamitani and Tong, 2005 used a wider annular aperture reaching further into the central region, where receptive fields are smaller (inner edge: 1.5° outer edge: 10° eccentricity from fixation). The interior parts of the stimulus may therefore not be affected by vignetting. Moreover, Wardle, Ritchie, Seymour, and Carlson, 2017 showed that vignetting is not necessary for orientation decoding.

Strengths

-Well-motivated and elegant stimulus design.

-3T and 7T fMRI data from a total of 14 subjects.

-Compelling results demonstrating that vignetting can cause coarse-scale patterns that enable orientation decoding,

Weaknesses

-The paper claims to introduce a novel idea that requires reinterpretation of a large literature. The claim of novelty is unjustified. Vignetting was discovered by Carlson et al., 2014 and in Wardle et al., 2017, Carlson's group showed that it may be one, but not the only contributing factor enabling orientation decoding. Carlson et al. deserve clearer credit throughout.

-The paper doesn't attempt to address whether decoding is still possible in the absence of vignetting effects, i.e. far from the aperture boundary.

Comments and suggestions

While the experiments and analyses are excellent and the paper well written, the current version is compromised by some exaggerated claims, suggesting greater novelty and consequence than is appropriate. This should be corrected.

Abstract: "Here, we show that a large body of research that purported to measure orientation tuning may have in fact been inadvertently measuring sensitivity to second-order changes in luminance, a phenomenon we term 'vignetting'."

Abstract: "Our results demonstrate that stimulus vignetting can wholly determine the orientation selectivity of responses in visual cortex measured at a macroscopic scale, and suggest a reinterpretation of a well-established literature on orientation processing in visual cortex."

Introduction: "Our results provide a framework for reinterpreting a wide-rangeof findings in the visual system."

Too strong of a claim of novelty. The effect beautifully termed "vignetting" here was discovered by Carlson, 2014, and that study deserves the credit for triggering a reevaluation of the literature, which began three years ago. The present study does place vignetting in a broader context, discussing a variety of mechanisms by which aperture edges might influence responses, but the basic idea, including that the key factor is the interaction between the edge and the grating orientation and that the edge need not be hard, are all introduced in Carlson, 2014. The present study very elegantly demonstrates the phenomenon with fMRI, but the effect has also previously been studied with fMRI by Wardle et al., 2017, so the fMRI component doesn't justify this claim, either. Finally, while results compellingly show that vignetting was a strong contributor in Freeman et al., 2011, they don't show that it is the only contributing factor for orientation decoding. In particular, Wardle et al., 2017 suggests that vignetting in fact is not necessary for orientation decoding.

Introduction: "We and others, using fMRI, discovered a coarse-scale orientation bias in human V1; each voxel exhibits an orientation preference that depends on the region of space that it represents (Furmanski and Engel, 2000; Sasaki et al., 2006; Mannion et al., 2010; Freeman et al., 2011; Freeman et al., 2013; Larsson et al., 2017). We observed a radial bias in the peripheral representation of V1: voxels that responded to peripheral locations near the vertical meridian tended to respond most strongly to vertical orientations; voxels along the peripheral horizontal meridian responded most strongly to horizontal orientations; likewise for oblique orientations. This phenomenon had gone mostly unnoticed previously. We discovered this striking phenomenon with fMRI because fMRI covers the entire retinotopic map in visual cortex, making it an ideal method for characterizing such coarse-scale representations."

A bit too much chest thumping. The radial-bias phenomenon was discovered by Sasaki et al., 2006. Moreover, the present study negates the interpretation in Freeman et al., 2011. Freeman et al., 2011 interpreted their results as indicating an over-representation of radial orientations in cortical neurons. According to the present study, the results were in fact an artifact of vignetting and whether neuronal biases played any role is questionable. Note that Freeman et al. used a narrower and more eccentric annulus than other studies (e.g. Kamitani and Tong, 2005), so may have been more susceptible to the vignetting artifact. The authors suggest that a large literature be reinterpreted, but apparently not their own study for which they specifically and compellingly show how vignetting probably affected it.

"A leading conjecture is that the orientation preferences in fMRI measurements arise primarily from random spatial irregularities in the fine-scale columnar architecture (Boynton, 2005; Haynes and Rees, 2005; Kamitani and Tong, 2005). […] On the other hand, we have argued that the coarse-scale orientation bias is the predominant orientation-selective signal measured with fMRI, and that multivariate decoding analysis methods are successful because of it (Freeman et al., 2011; Freeman et al., 2013). This conjecture [that coarse-scale orientation bias is the predominant signal] remains controversial because the notion that fMRI is sensitive to fine-scale neural activity is highly attractive, even though it has been proven difficult to validate empirically (Alink et al., 2013; Pratte et al., 2016; Alink et al., 2017)."

This passage is a bit biased. First, the present results question the interpretation of Freeman et al., 2011. While the authors' new interpretation (following Carlson, 2014) also suggests a coarse-scale contribution, it fundamentally changes the account. Moreover, the conjecture that coarse-scale effects play a role is not controversial. What is controversial is the claim that only coarse-scale effects contribute to fMRI orientation decoding. This extreme view is controversial not because it is attractive to think that fMRI can exploit fine-grained pattern information, but because the cited studies (Alink et al., 2013, Pratte et al., 2016, Alink et al., 2017, and additional studies, including Shmuel et al., 2010) present evidence in favor of a contribution from fine-grained patterns. The way these studies are cited would suggest to an uninformed reader that they provide evidence against a contribution from fine-grained patterns. More evenhanded language is in order here.

"the model we use is highly simplified; for example, it does not take intoaccount changes in spatial frequency tuning at greater eccentricities. Yet, despite the multiple sources of noise and the simplified assumptions of the model, the correspondence between the model's prediction and the empirical measurements are highly statistically significant. From this, we conclude that stimulus vignetting is a primary source of the course scale bias."

This argument is not compelling. A terrible model may explain a portion of the explainable variance that is minuscule, yet highly statistically significant. In the absence of inferential comparisons among multiple models and model checking (or a noise ceiling), better to avoid such claims.

Discussion: "One study (Alink et al., 2017) used inner and outer circular annuli, but added additional angular edges, the result of which should be a combination of radial and tangential biases. Indeed, this study reported that voxels had a mixed pattern of selectivity, with a considerable number of voxels reliably preferring tangential gratings, and other voxels reliably favoring radial orientations."

This reasoning makes sense. The additional edges between the patches (though perhaps not well described as vignetting) complicate the interpretation of the results of Alink et al., 2011. It would be good to check the strength of the effect by simulation. Happy to share the stimuli if someone wanted to look into this.
