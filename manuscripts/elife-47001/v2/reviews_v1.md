# Peer review - Round 1

Editors:
- Ross K Maddox, University of Rochester United States

Reviewers:
- Ross K Maddox, University of Rochester United States
- Sarah Baum Miller
- Adam Bosen

## Review text

DOI: [10.7554/eLife.47001.016](https://doi.org/10.7554/eLife.47001.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Shared neural underpinnings of multisensory integration and trial-by-trial perceptual recalibration" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ross K Maddox as the guest Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Barbara Shinn-Cunningham as the Senior Editor. The following individuals involved in review of your submission have also agreed to reveal their identity: Sarah Baum Miller (Reviewer #2) and Adam Bosen (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript by Park and Kayser investigates two complementary aspects of multisensory perception: the integration of audiovisual information within a trial, as well as the impact of a multisensory event on subsequent trials. They use single trial analysis of MEG data while human participants completed a spatial localization task which probes both processes. The experimental design follows that of Wozny and Shams, 2011, which is a good method of dissociating the ventriloquism effect from the ventriloquism aftereffect. This study represents a much needed addition to the field and leverages the spatial and temporal resolution of MEG. All three reviewers viewed the manuscript positively. However, the following reviewer concerns and questions should be addressed in the revised version.

Also note that the title should provide a clear indication of the biological system under investigation. Please revise your title with this advice in mind.

Essential revisions:

The first concern relates to the time course of eye movements during the experiment. Each trial starts with a fixation period, but the Materials and methods do not specify if participants were instructed to maintain fixation during target presentation and/or localization. Eye position can bias auditory localization (Razavi et al., 2007) and the ventriloquism aftereffect is coded in a mixed eye-head reference frame (Kopco et al., 2009), so eye movements during the experiment could substantially influence the behavioral results. We would like to see a more detailed description of how eye movements were controlled or could have influenced the behavioral results. Additionally, the absence of a significant electrophysiological coding of visual location on previous trials (Figure 2A, third panel), could be a result of a shifting visual reference frame caused by eye movements. Because auditory stimuli were presented via insert tubes, the auditory stimuli would not be altered by head movements, which could explain why auditory but not visual representations were evident.

The classification is not explained clearly. In subsection “Neural en- and decoding analysis” you state that "each location was considered as a binary variable," with both left locations (-17, -8.5) collapsed, and the same done for the right locations. Was this done only for the classification outcome, or were the classification features also binarized? If they were, would this be an issue in trials where there was a VE shift but it did not cross into the other hemifield? If it was not the case, please make clear exactly what was binarized and what remained continuous.

Both the VE and VAE models (Equation 4 and 5) appear to be the same model. If this is not the case, then perhaps this could be clarified for the reader. We assume VAE would include βLDAAn * LDAAn as in Equation 3. Please address this.

The ROC for each of the linear discriminants appears to just barely go above the chance line (Figure 2), so it seems the neural correlates of VE/VAE are very subtle. Is the small effect size more reflective of the nature of MEG signals or the nature of VE/VAE?

There seems to be a LH dominant response for βLDAAn-1 in the VAE and VE neural representations. Do you have any sense as to why these would be LH dominant processes, and could you comment on this? One could have (perhaps naively) assumed that any hemispheric biases would be more RH dominant in a spatial localization context.

In the MEG results, the neural locations observed to be associated with the ventriloquism effect and ventriloquism aftereffect are broadly in agreement with our expectations.

The use of generic HRTFs to simulate auditory source location, rather than presenting auditory targets from free-field speakers, requires some assumptions about how participants perceive auditory targets simulated with those HRTFs. However, given the need to electromagnetically isolate the MEG equipment and the fact that stimuli are only presented in azimuth indicates that the use of HRTFs is justified and should not alter the results substantially. If anything, the general HRTF would produce an "in the head" feeling, which may decrease the probability of fusing the auditory and visual stimuli. Given that some participants showed very little VE or VAE (Figure 2, panels B and D, individuals with means near zero), this may have occurred, but some individuals show little of either effect even with free field stimuli, so it seems that the use of generic HRTFs did not alter the expected behavioral trends. Please add justification for your use of non-individualized HRTFs and discuss any effects this may have had on your findings.
