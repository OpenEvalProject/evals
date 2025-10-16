# Peer review - Round 1

Editors:
- Stephanie Palmer, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.43533.026](https://doi.org/10.7554/eLife.43533.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The impact of bilateral ongoing activity on evoked responses in mouse cortex" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Spontaneous neural activity is ubiquitous, but its impact on perception and evoked neural activity is not well understood. The manuscript investigates bilaterally symmetrical cortical activation observed in mice during an awake resting state condition and during a visual discrimination task. The authors extend previous work by a number of labs defining bilaterally symmetrical activity dynamics in the mouse brain. Strikingly, these bilateral dynamics are preserved under conditions of spontaneous activity or even anesthesia states. The authors examine the interactions of this ongoing activity with task-evoked activity. They find that although ongoing activity is of greater amplitude than task-dependent signals, it does not interfere with the ability to perform the task. In addition, other significant findings are reported, such as the lack of a relationship between task-dependent and ongoing activity, and a linear interaction between the spontaneous activity and the evoked activity, with no impact on behavioral performance. The results are very surprising, as most studies have suggested that the ongoing activity will, at least to some degree, affect behavior and evoked responses (e.g. Mcginley et al., Neuron 2015). Mesoscopic imaging of these spontaneous neural activity patterns and its impact on a behavior is an important and novel advance for the field. The paper is well-written and it is relatively clear in its presentation and accessible to a wide range of readers.

Essential revisions:

1) Mesoscopic calcium/voltage imaging is becoming a very important tool in systems neuroscience, but it would be good to show some more details on the data processing pipeline, given the importance and impact of the results shown in this manuscript.

The pre-processing step in the data analysis presented in the paper needs to be more clearly described and discussed. There are concerns that the pre-processing, combined with subsequent band-pass filtering could amplify relatively small parts of the original signal. Could this artificially hide some non-linear interaction between the spontaneous and evoked activity? Does the linear relationship between the evoked and spontaneous activity persist in the raw data?

To address these concerns, particularly that the noise removal steps might remove most of the signal in the 0.5 – 7.0 Hz range, it is suggested that the authors:

– Show analyses both of the raw and "denoised" data, including some example traces before and after pre-processing and bandpass filtering, as well as the power spectra of these signals.

– Perform their denoising SVD in the space-frequency domain (rather than in the temporal domain) (see Prechtl et al., 1997 PNAS), and use the resulting components with substantial power in the 0.5-7 Hz band.

2) The manuscript needs to better define the behavioral state of the animal. Are there particular bilateral limb, whisker, or facial movements during sensory-motor bilateral activity? Videos of the animal body, if available, might help make this point a bit more clear to the reader.

3) The term "ongoing activity" should be more clearly defined.

4) Points made in Figure 3A such as ongoing activity dominating stimulus-dependent activity should be stated quantitatively. The current draft only states when "acquiring a large number of trials could ongoing fluctuations be averaged out". Please state what a "large number of trials" is and exactly what the impact can be. Presumably, this effect is dependent on where ongoing spontaneous activity occurs and what particular spatial temporal characteristics it contains. One could imagine ongoing activity could have discreet motifs, as described in Mohajerani et al., 2013, which should also be referenced.

5) The authors elegantly show that bilateral activity adds linearly to stimulus trial evoked activity. While the authors have clearly defined this, it needs to also be stated that this conclusion only holds for a visual stimulus. In the experiments, sequences of activity were chosen where mice were attending to visual stimuli and not doing other tasks such a forelimb or whisker-dependent task. It is possible that most of the ongoing activity has origins outside the visual system, making it unlikely that ongoing activity would interfere with visual processing. In contrast, if the task were a whisker or forelimb-dependent one, and the mouse was also moving these body parts, very different results could be obtained. Please mention this caveat in the Abstract and also discuss it more in the manuscript.

5b) The authors should contrast their findings on ongoing visual-like activity and task success rate and response additivity with activity that features different sensory systems (perhaps forelimb and whisker). One way to do this is by using a template-matching or similar scheme as in, e.g. Mohajerani et al., 2013, to find the visual-system-like versus whisker-like ongoing activity and see whether these have any specific impact on a visual task. It would be good to see a quantification of the general composition of the ongoing activity: how much is whisker- versus visual-like, etc. These would be additional analyses, but require no new data collection.

To add to the Discussion section:

6) In other recent work, it has been shown that a form of ongoing activity derived from optogenetic stimulation can bias behavioral activity. Why does optogenetic stimulation have an impact, but not the forms of spontaneous ongoing activity monitored here? e.g. O'Connor et al., 2014 and Sreenivasan et al., 2016

7) Can one conclude that the ipsilateral hemisphere really is independent during the visual task? Perhaps, instead, it gets inhibited, potentially dampening its utility for reporting the impact of ongoing activity on evoked activity?
