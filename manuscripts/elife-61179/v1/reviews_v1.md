# Peer review - Round 1

Editors:
- Marisa Carrasco, New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61179.sa1](https://doi.org/10.7554/eLife.61179.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

To maintain accurate perception, vision has to adapt in a changing environment. This paper provides convincing behavioral evidence that the visual system can learn to rapidly adjust to an experienced environment. Such learning may help stabilize vision perception and optimize perceptual processes. For instance, it may support enhanced color constancy across spectral environments an individual human encounters with some regularity, and aid many perceptual tasks, for example recognition of objects or materials.

Decision letter after peer review:

Thank you for submitting your article "Visual mode switching learned through experience" for consideration by eLife. Your article has been reviewed by Joshua Gold as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: David Brainard (Reviewer #1); Larry Maloney (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

It is very well established that chromatic adaptation occurs on short time scales (milliseconds to minutes) and reasonably well established that it occurs on longer time scales (hours to weeks). The question asked here is whether the visual system can learn, over a relatively long time scale (days), to accelerate/enhance its short-term adaptation (seconds to tens of minutes). Such learning might support enhanced color constancy across spectral environments an individual encounters with some regularity. The question is theoretically interesting and not much studied experimentally. The experiments appear to have been carefully executed and analyzed. The authors determine that there are two adaptation processes (rapid and gradual) and that the rapid process learns to anticipate. This "learning to adapt" effect allows individuals to adjust more rapidly to a change in visual experience when they have experienced a similar change previously. The effect was long lasting, still present in diminished form a month after completion of the main part of the experiment. They also found evidence for increased color constancy across days.

The experiments document the effect but do not much constrain the nature or site of the underlying mechanisms. In this sense, this study opens the door to future computational and experimental studies that attempt to dissect and explain the phenomenon.

Essential revisions:

1) The key phenomenon to explain is the decreasing onset of the rapid effect after change in illuminant condition. The idea that there are two stages of adaptation one of which can be driven by predictions of the external environment is exciting. The authors advance a probabilistic model of change detection but no details are given. There is a literature on two-stage models of adaptation (e.g., Pugh and Augenstein, 1977) that should be mentioned.

2) The authors portray their main finding sometimes as "increases in the amount of adaptation the visual system produces immediately upon putting on the glasses" or as learning "to shift rapidly to a partially adapted state". Thy do not seem to be equivalent mechanisms. The first refers to neural circuits adapting more rapidly/extensively after experience with the environment. The second suggests a learning effect-where the short timescale (e.g. seconds) adaptation is the same but the learning allows circuits a head start. It would be helpful to lay out these scenarios clearly in the text and use a consistent characterization of the main result.

3) It is interesting that the after-effect does not change with experience. Although subjects adjust more quickly to the glasses (e.g. they've learned the relevant adaptation state, Figure 2 red points), they haven't learned to undo the effect of removing the glasses (Figure 2, green points). The authors should discuss what they think about these findings.

4) We commend the authors for presenting a summary of the individual differences seen in the data, which are large. The origin of these differences is not clear, and together with mixed reports in the few studies of this sort that are reported in the literature mean some caution is required in interpretation of results. The possibility of some subjects "thinking about what they see" and responding on that basis comes to mind. This is a thorny issue that plagues most studies of constancy and is not reason to hold up publication of the present work, but it should be discussed.

5) How sure are you that subjects complied with glasses wearing instructions throughout the day? Could compliance relate to individual differences?

6) Color constancy: It is not clear what the logic is and how the color constancy calculations were done.

To make a perfect constancy prediction, one starts with some analysis of what surface reflectance corresponded to unique yellow in the glasses off condition, based on some assumption about ambient illumination and some constraints on surface reflectance functions. Then one asks what settings would correspond to that surface reflectance function under the changed illumination (here induced by the glasses). A calculation like this may have been done, but it is not provided.

Why is the proposed metric a measure of constancy? The rationale for the metric used (and claims made) is a single reference. Please clarify and help the readers understand better how the index captures constancy.

7) There are clearly a number of different ways to represent these data. Hue angle in the stimulus is fine and direct, and the L/(L+M) used in Figure 4 is also fine. Another alternative is the relative gain of the L and M cones at unique yellow, on the assumption that unique yellow represents L-kM = 0 for some k in each state of adaptation. That then gives k = L/M. Would this gain oriented expression of the data lead to more insight than the L/(L+M) version? It may be worth taking a look as it refers the data back to a hypothesized mechanistic state of the visual system. Would viewing either this or the L/(L+M) representation on an expanded within session time scale, separately for each session, reveal more about the dynamics, especially if (as suggested below in the context of Figure S2) the individual settings made once per minute in the within-session blocks were shown explicitly.

8) One aspect of the design that is likely important is that observers alternated between the two environments several times per day. It may be that frequency of environmental change is an important factor. Another factor is that the environment they were in was moderately complex, an office.

From Figure 1 it looks like the ambient environment for the experiment varied from day to day with changes in outdoor lighting coming in through the windows. Was there any characterization of this? Are the authors at all concerned that this variation may have affected results? Can they give any guidance to future researchers who would like to try to replicate their experiments as closely as possible, in terms of room size, relative amount occupied by windows, what the indoor lights were, ambient illumination level relative to display, etc.

9) Please say a little more about conversion to MB space and displayed stimuli.

a) How were peaks cone fundamentals scaled relative to each other when computing LMS, for subsequent computation of L/L+M and S/L+M. It seems that those two quantities are the Lmb and Smb passed into the computation of LM and S. Not sure S is the best choice of notation for the latter.

b) What photopic luminosity function was used to define nominal isoluminance. Given use of Stockman-Sharpe fundamentals one might infer the new CIE standard that is a weighted sum of those, or you might have used CIE 1931, or Judd-Vos, or.…

b) Please give the actual radius of the hue circle used in the adjustments, as well as the hue angle spacing for coarse and fine adjustments so that it would be possible for someone to produce your stimuli.

c) Was a full hue circle used, or were there endpoints? If end points, how confident are you that subjects didn't use those as a reference and count steps from there, or less explicitly anchor their adjustments to an estimated midpoint of the range provided? Learning of such strategies could masquerade as learning to adapt.

d) What is the luminance of the test patch that is being adjusted? Subsection “Apparatus” says the background luminance was 41.85 cd/m2, but later and in the picture, this is described/shown as black, which is surprising unless the ambient in the room was very high luminance.

10) Figure S2, top panel interpretation. The pattern of results is a little hard to interpret. We'd expect the least adaptation for the first setting, so in general these should be lower on the y-axis than the corresponding points in Figure 2. That does not appear to be the case in many instances. See the first group of glasses on settings, for example. Any comment? Are the first settings just really noisy? It might be clearer if each individual setting were plotted, rather than just providing the comparison of the first to the mean.
