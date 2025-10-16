# Peer review - Round 1

Editors:
- Björn Herrmann, Baycrest Hospital Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.100605.3.sa0](https://doi.org/10.7554/eLife.100605.3.sa0)

Examination of (a)periodic brain activity has gained particular interest in the last few years in the neuroscience fields relating to cognition, disorders, and brain states. Using large EEG/MEG datasets from younger and older adults, the current study provides compelling evidence that age-related differences in aperiodic EEG/MEG signals can be driven by cardiac rather than brain activity. Their findings have important implications for all future research that aims to assess aperiodic neural activity, suggesting control for the influence of cardiac signals is essential.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100605.3.sa1](https://doi.org/10.7554/eLife.100605.3.sa1)

Summary:

The present study addresses whether physiological signals influence aperiodic brain activity with a focus on age-related changes. The authors report age effects on aperiodic cardiac activity derived from ECG in low and high-frequency ranges in roughly 2300 participants from four different sites. Slopes of the ECGs were associated with common heart variability measures, which, according to the authors, shows that ECG, even at higher frequencies, conveys meaningful information. Using temporal response functions on concurrent ECG and M/EEG time series, the authors demonstrate that cardiac activity is instantaneously reflected in neural recordings, even after applying ICA analysis to remove cardiac activity. This was more strongly the case for EEG than MEG data. Finally, spectral parameterization was done in large-scale resting-state MEG and ECG data in individuals between 18 and 88 years, and age effects were tested. A steepening of spectral slopes with age was observed, particularly for ECG and, to a lesser extent, in cleaned MEG data in most frequency ranges and sensors investigated. The authors conclude that commonly observed age effects on neural aperiodic activity can mainly be explained by cardiac activity.

Strengths:

Compared to previous investigations, the authors demonstrate effects of aging on the spectral slope in the currently largest MEG dataset with equal age distribution available. Their efforts of replicating observed effects in another large MEG dataset and considering potential confounding by ocular activity, head movements, or preprocessing methods are commendable and highly valuable to the community. This study also employs a wide range of fitting ranges and two commonly used algorithms for spectral parameterization of neural and cardiac activity, hence providing a comprehensive overview of the impact of methodological choices. The authors discuss their findings in-depth and give recommendations for the separation of physiological and neural sources of aperiodic activity.

Weaknesses:

While the study's aim is well-motivated and analyses rigorously conducted, it remains vague what is reflected in the ECG at higher frequency ranges that contributed to the confounding of the age effects in the neural data. However, the authors address this issue in their discussion.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100605.3.sa2](https://doi.org/10.7554/eLife.100605.3.sa2)

As remains obvious from my previous reviews, I still consider this to be an important paper and that is final and publishable in its current state.

In that previous review, I revealed my identity to help reassure the authors that I was doing my best to remain unbiased because I work in this area and some of the authors' results directly impact my prior research. I was genuinely excited to see the earlier preprint version of this paper when it first appeared. I get a lot of joy out of trying to - collectively, as a field - really understand the nature of our data, and I continue to commend the authors here for pushing at the sources of aperiodic activity!

In their manuscript, Schmidt and colleagues provide a very compelling, convincing, thorough, and measured set of analyses. Previously I recommended that the push even further, and they added the current Figure 5 analysis of event-related changes in the ECG during working memory. In my opinion this result practically warrants a separate paper its own!

The literature analysis is very clever, and expanded upon from any other prior version I've seen.

In my previous review, the broadest, most high-level comment I wanted to make was that authors are correct. We (in my lab) have tried to be measured in our approach to talking about aperiodic analyses - including adopting measuring ECG when possible now - because there are so many sources of aperiodic activity: neural, ECG, respiration, skin conductance, muscle activity, electrode impedances, room noise, electronics noise, etc. The authors discuss this all very clearly, and I commend them on that. We, as a field, should move more toward a model where we can account for all of those sources of noise together. (This was less of an action item, and more of an inclusion of a comment for the record.)

I also very much appreciate the authors' excellent commentary regarding the physiological effects that pharmacological challenges such as propofol and ketamine also have on non-neural (autonomic) functions such as ECG. Previously I also asked them to discuss the possibility that, while their manuscript focuses on aperiodic activity, it is possible that the wealth of literature regarding age-related changes in "oscillatory" activity might be driven partly by age-related changes in neural (or non-neural, ECG-related) changes in aperiodic activity. They have included a nice discussion on this, and I'm excited about the possibilities for cognitive neuroscience as we move more in this direction.

Finally, I previously asked for recommendations on how to proceed. The authors convinced me that we should care about how the ECG might impact our field potential measures, but how do I, as a relative novice, proceed. They now include three strong recommendations at the end of their manuscript that I find to be very helpful.

As was obvious from previous review, I consider this to be an important and impactful cautionary report, that is incredibly well supported by multiple thorough analyses. The authors have done an excellent job responding to all my previous comments and concerns and, in my estimation, those of the previous reviewers as well.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100605.3.sa3](https://doi.org/10.7554/eLife.100605.3.sa3)

Summary:

Schmidt et al., aimed to provide an extremely comprehensive demonstration of the influence cardiac electromagnetic fields have on the relationship between age and the aperiodic slope measured from electroencephalographic (EEG) and magnetoencephalographic (MEG) data.

Strengths:

Schmidt et al., used a multiverse approach to show that the cardiac influence on this relationship is considerable, by testing a wide range of different analysis parameters (including extensive testing of different frequency ranges assessed to determine the aperiodic fit), algorithms (including different artifact reduction approaches and different aperiodic fitting algorithms), and multiple large datasets to provide conclusions that are robust to the vast majority of potential experimental variations.

The study showed that across these different analytical variations, the cardiac contribution to aperiodic activity measured using EEG and MEG is considerable, and likely influences the relationship between aperiodic activity and age to a greater extent than the influence of neural activity.

Their findings have significant implications for all future research that aims to assess aperiodic neural activity, suggesting control for the influence of cardiac fields is essential.

Weaknesses:

The authors have addressed the weaknesses of their study in their manuscript. Most alternative explanations for their results have been explored to ensure their conclusions are robust and are not explained by unexplored confounds. Minor potential weaknesses are:

(1) The number of electrodes used in the EEG analyses was on the lower side, and as such, the results do not confirm that the influence of ECG on the 1/f activity in the EEG is high even for higher density EEG montages where ICA may provide better performance at removing cardiac components (as noted by the authors). Having noted this potential weakness, I doubt the effects of cardiac activity can be completely mitigated with current methods, even in higher-density EEG montages.

(2) Head movements were used as a proxy for muscle activity. However, this may imperfectly address the potential influence of muscle activity on the slope in the EEG activity. As such, remaining muscle artifacts may have affected some of the results, particularly those that included high frequency ranges in the aperiodic estimate. Perhaps if muscle activity were left in the EEG data, it could have disrupted the ability to detect a relationship between age and 1/f slope in a way that didn't disrupt the same relationship in the cardiac data. However, I doubt this would reverse the overall conclusions given the number of converging results, including in lower frequency bands. The authors also note this potential weakness and suggest how future research might address it.
