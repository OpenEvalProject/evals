# Neural population dynamics in human motor cortex during movements in people with ALS

## Authors

- Chethan Pandarinath<sup>1</sup> ([ORCID: 0000-0003-1241-1432](https://orcid.org/0000-0003-1241-1432))
- Vikash Gilja<sup>1</sup>
- Christine H Blabe<sup>1</sup>
- Paul Nuyujukian<sup>1</sup> ([ORCID: 0000-0001-7778-5473](https://orcid.org/0000-0001-7778-5473))
- Anish A Sarma<sup>4</sup> ([ORCID: 0000-0003-1261-0589](https://orcid.org/0000-0003-1261-0589))
- Brittany L Sorice<sup>6</sup>
- Emad N Eskandar<sup>8</sup>
- Leigh R Hochberg<sup>5</sup> ([ORCID: 0000-0003-0261-2273](https://orcid.org/0000-0003-0261-2273))
- Jaimie M Henderson<sup>1</sup> ([ORCID: 0000-0002-3276-2267](https://orcid.org/0000-0002-3276-2267))
- Krishna V Shenoy<sup>2</sup> ([ORCID: 0000-0003-1534-9240](https://orcid.org/0000-0003-1534-9240)) †

### Affiliations

1. Department of Neurosurgery Stanford University Stanford United States
2. Department of Electrical Engineering Stanford University Stanford United States
3. Stanford Neurosciences Institute Stanford University Stanford United States
4. School of Engineering Brown University Providence United States
5. Center for Neurorestoration and Neurotechnology, Rehabilitation R and D Service, Department of VA Medical Center Providence United States
6. Neurology Massachusetts General Hospital Boston United States
7. Institute for Brain Science Brown University Providence United States
8. Department of Neurosurgery Harvard Medical School Boston United States
9. Department of Neurosurgery Massachusetts General Hospital Boston United States
10. Neurology Harvard Medical School Boston United States
11. Department of Neurobiology Stanford University Stanford United States
12. Department of Bioengineering Stanford University Stanford United States
13. Neurosciences Program Stanford University Stanford United States

† Corresponding author

## Abstract

10.7554/eLife.07436.001 The prevailing view of motor cortex holds that motor cortical neural activity represents muscle or movement parameters. However, recent studies in non-human primates have shown that neural activity does not simply represent muscle or movement parameters; instead, its temporal structure is well-described by a dynamical system where activity during movement evolves lawfully from an initial pre-movement state. In this study, we analyze neuronal ensemble activity in motor cortex in two clinical trial participants diagnosed with Amyotrophic Lateral Sclerosis (ALS). We find that activity in human motor cortex has similar dynamical structure to that of non-human primates, indicating that human motor cortex contains a similar underlying dynamical system for movement generation. Clinical trial registration: NCT00912041. DOI: http://dx.doi.org/10.7554/eLife.07436.001

## Introduction

Neurons in motor cortex exhibit complex firing patterns during movement (Fetz, 1992; Churchland and Shenoy, 2007; Churchland et al., 2010). Though motor cortex has been extensively studied over the past century (Lemon, 2008), the complexity of these patterns remains poorly understood. Early work demonstrated that neural firing correlates with external variables such as movement direction (Georgopoulos et al., 1982), and an ongoing debate centers on whether the firing patterns represent muscle or movement parameters (e.g., joint position, intended velocity, reach endpoint, muscle forces, and so on; reviewed in Kalaska, 2009). A recent approach has been to ask, instead, whether these patterns of activity reflect an internal dynamical system across the population (Fetz, 1992; Todorov and Jordan, 2002; Churchland and Shenoy, 2007; Scott, 2008; Churchland et al., 2010, 2012; Graziano, 2011; Shenoy et al., 2013; Kaufman et al., 2014). In this view, the system's initial state is set by preparatory activity, and consistent rules govern how firing rates evolve over time across movement conditions, regardless of movement direction or other externally changing variables.

This dynamical view is supported by recent studies in rhesus macaques (

![Figure 1.](https://cdn.elifesciences.org/articles/07436/elife-07436-fig1-v1.jpg)

**Figure 1.:** (A) Projections of the neural population response onto the first jPCA plane for a monkey during an arm-reaching task (monkey N, 108 conditions; adapted from Churchland et al., 2012). Each trace plots the first 200 ms of activity during the movement epoch for a given condition. Traces are colored based on the preparatory state projection onto jPC1. a.u., arbitrary units. (B) Projections for participant T6 during an 8-target center-out task controlled by index finger movements on a computer touchpad. Each trace plots the 250 ms of activity during the movement epoch (‘Materials and methods’) for a given condition. (C) Same as (B), for participant T7. Video 1 shows the evolution of the neural state over time for each participant.DOI: http://dx.doi.org/10.7554/eLife.07436.003

In humans, studies in research participants with tetraplegia have demonstrated that motor cortical action potential (AP) responses contain information about intended movement kinematics (Truccolo et al., 2008). Here, we investigated whether these AP responses also contain rotational dynamical structure at the ensemble level.

## Results

We analyzed multi-neuron AP activity from 2 people with tetraplegia enrolled in the BrainGate2 pilot clinical trial. This ongoing, multi-site, pilot clinical trial is performed under an FDA Investigational Device Exemption and has been approved by local institutional review boards at all study sites. The study participants (T6, T7) had differing degrees of motor impairment due to Amyotrophic Lateral Sclerosis (ALS). T6 retained the ability to make several dexterous movements (especially of the fingers and wrist), while T7 retained limited finger movements.

Neural signals were recorded using 4 mm × 4 mm, 96-channel silicon microelectrode arrays, which were implanted in the hand area of dominant M1. APs were recorded as participants performed visual target acquisition tasks. Participants attempted to move a cursor from the center of a computer screen to one of eight peripheral targets, with the cursor's position controlled by index finger movements on a computer touchpad (see ‘Materials and methods’).

We first tested whether an underlying dynamical structure existed in the neural activity. If present, a population-level analysis should reveal orderly rotational structure that is consistent across conditions (i.e., independent of the direction of movement). To search for rotational patterns in the neural population state, we used a three-step procedure: first, for each condition (i.e., for a given target), we averaged the activity on each electrode across all trials. Next, we performed principal components analysis (PCA) on the high-dimensional population data. We restricted the data to the top 6 PCs, that is, we only preserved the six response patterns most strongly present in the data. Finally, for this reduced-dimensional data set, we applied the jPCA method (Churchland et al., 2012), which searches the data for 2-dimensional planes that capture the strongest rotational tendencies. Restricting the jPCA analysis to the dimensionality-reduced data (6-D) ensured that any rotational structure revealed by the analysis was present in the most prominent response patterns in the data.

For both participants, the population activity exhibited strong rotational dynamics (Figure 1B,C). Each trace shows the population activity in the top jPC plane for a single condition. 250 ms of data are shown, beginning with the rapid change in neural activity that precedes movement onset (the evolution of the neural state over time for each participant is shown in Video 1). Rotations proceeded in the same direction across conditions, following from the initial pre-movement state. The top jPCA plane captured 61% (T6) and 27% (T7) of the variance of the high-dimensional neural data (for comparison, the macaque study reported 28% for the top plane on average).10.7554/eLife.07436.004Video 1.Neural population responses show rotational activity.Video shows the evolution of the neural state over time in the first jPCA plane for participants T6 and T7. Low-dimensional projections were calculated as in Figure 1. Each colored trace represents one of 8 conditions. All times are relative to target onset (0 ms).DOI: http://dx.doi.org/10.7554/eLife.07436.004

One potential concern is that the jPCA method might be powerful enough to find rotatory patterns in state space for any set of responses that contains complex, multiphasic patterns. To test for this possibility, we performed three control analyses, following

![Figure 2.](https://cdn.elifesciences.org/articles/07436/elife-07436-fig2-v1.jpg)

**Figure 2.:** For each data set, neural responses were shuffled in a manner that preserved the complexity of individual response patterns on each electrode, but disrupted the structure of the data across electrodes. For each channel, the pattern of activity during the movement epoch was inverted for half the conditions (chosen at random). The inversion was performed around the initial time point, so that continuity with pre-movement activity was preserved. Performing jPCA on the shuffled responses did not reveal consistent rotational structure. (A, top) Projection of the population responses onto the first jPCA plane for a single shuffled trial (participant T6). (bottom) Fraction of variance of the change in neural state (6-D) explained by rotational activity for the original data set (brown) vs the shuffled data sets (blue). Error bar represents the standard deviation across 300 shuffle trials. (B) Same as (A), for participant T7. Two additional shuffle control analyses are presented in Figure 2—figure supplement 1 and Figure 2—figure supplement 2.DOI: http://dx.doi.org/10.7554/eLife.07436.005

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/07436/elife-07436-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** This shuffle control was similar to the first, but the patterns of activity during the movement epoch were inverted for all conditions. (A) Projections of the neural population state for each data set after shuffling are shown. (B) The fraction of variance captured by the rotational model before and after shuffling. This manipulation would not be expected to remove all rotational structure, as the structure should merely be sign-inverted. However, this manipulation should remove any consistent relationship between the pre-movement activity and the phase of subsequent oscillations. Thus, this control is expected to disrupt the relationship between the rotational phase and its initial state.DOI: http://dx.doi.org/10.7554/eLife.07436.006

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/07436/elife-07436-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** In this shuffle control, activity during the movement epoch from one condition was randomly reassigned onto the pre-movement activity from another. The firing rate at the beginning of the movement epoch was appended to the firing rate at the end of the pre-movement period, to preserve continuity. For a given shuffle trial, the same reassignment was performed for all neurons. (A) Projections of the neural population state for each data set after a single shuffle trial. (B) The fraction of variance captured by the rotational model for the original data sets and 300 shuffle trials is shown (each shuffle trial tests a different random set of pairings of pre-movement and movement epoch activity). Error bars represent the standard deviation across shuffle trials. As with the second shuffle control, this manipulation is not expected to remove all rotational structure. While the relationship between rotational phase and the initial state is disrupted (as each condition's movement epoch activity is assigned to another condition's pre-movement activity), there is some likelihood that a given condition will be assigned an initial state similar to its own, allowing some rotational structure to be preserved by this manipulation.DOI: http://dx.doi.org/10.7554/eLife.07436.007

To quantify the consistency of the rotatory activity, we measured the angle from the neural state in the jPCA plane,

![Figure 3.](https://cdn.elifesciences.org/articles/07436/elife-07436-fig3-v1.jpg)

**Figure 3.:** Traces represent histograms of the angle, q, between the neural state, x, and its derivative, , for each time step. The angle was measured as illustrated schematically (inset) after projecting the data into the first jPCA plane. Purely rotatory activity results in angles near pi/2, while pure scaling/expansion results in angles near 0 or pi. Y-axis denotes scale for participant data (colored traces). For comparison, histograms for the example shuffle control data (x˙Figure 2) and monkey composite data are shown in gray and black, respectively. These traces are normalized to match the participant data range (monkey data reproduced from Churchland et al., 2012).DOI: http://dx.doi.org/10.7554/eLife.07436.008

## Discussion

These results demonstrate prominent rotations of the neural population state in human motor cortex during movements. As with macaques, rotations were consistent across conditions and followed naturally from an initial pre-movement state. As mentioned above, and in contrast to the macaque study, both participants in this study had a diagnosis of ALS with resultant motor impairment. Participant T7's movements in particular were very limited and occurred with a long latency following target onset (detailed in ‘Materials and methods’). Both participants likely had substantial changes in motor cortex due to their disease progression; therefore, these results do not conclusively show that dynamical activity is present in healthy human motor cortex. However, given the finding that dynamical activity is prominent in motor cortex in people with abnormal motor function, and given the similarity of this activity to that of healthy non-human primates, the results strongly suggest the presence of dynamical activity in human motor cortex in general and may also hint at which aspects of motor cortical function are preserved despite the progression of a severe motor neuron disease.

Given the findings of dynamical activity during overt movements, a potentially exciting open question is whether motor cortex exhibits dynamical activity during purely imagined movements. Recent studies (Feldman et al., Society for Neuroscience, 2011, 2012; Pandarinath et al., Society for Neuroscience, 2013) have demonstrated that motor cortex is active during both overt and imagined movements. If the functional role of rotational dynamics is to serve as an oscillatory basis set for generating muscle activation patterns (e.g. electromyogram activity) (Churchland et al., 2012; Sussillo et al., 2015), then one might expect these dynamics to be absent during imagined movements, when the subject is specifically trying to avoid generating motor output. However, if activity during imagined movements serves as a mechanism for the ‘covert rehearsal’ of activity during overt movements, then dynamics might still be present (but might be, for example, orthogonal to patterns of activity that drive motor output). Future studies will attempt to directly address this question.

The current study’s findings also suggest a promising avenue to improve the performance of Brain–Machine Interfaces (BMIs) for persons with tetraplegia, as previous work with macaques (Kao et al., 2015) demonstrated that incorporating neural population dynamics into BMI control algorithms may lead to performance improvements. Finally, as with macaques, the presence of these rotations calls into question the prevailing model of motor cortical activity (i.e., that motor cortical firing patterns represent muscle or movement parameters) in favor of a dynamical systems perspective in humans as well.

## Materials and methods

Permission for these studies was granted by the US Food and Drug Administration (Investigational Device Exemption) and Institutional Review Boards of Stanford University (protocol # 20804), Partners Healthcare/Massachusetts General Hospital (2011P001036), Providence VA Medical Center (2011-009), and Brown University (0809992560). The two participants in this study, T6 and T7, were enrolled in a pilot clinical trial of the BrainGate Neural Interface System (http://www.clinicaltrials.gov/ct2/show/NCT00912041). Informed consent, including consent to publish, was obtained from the participants prior to their enrollment in the study.

## Participants

Participant T6 is a right-handed woman, 51 year old at the time of this study, with tetraplegia due to ALS. On December 7, 2012, a 96-channel intracortical silicon microelectrode array (1.0-mm electrode length, Blackrock Microsystems, Salt Lake City, UT) was implanted in the hand area of dominant motor cortex as previously described (Hochberg et al., 2006; Simeral et al., 2011). T6 retained dexterous movements of the fingers and wrist. Data reported in this study are from T6's trial days 95–213.

Participant T7 is a right-handed man, 54 year old at the time of this study, with tetraplegia due to ALS. T7 had two 96-channel intracortical silicon microelectrode arrays (1.5-mm electrode length, Blackrock Microsystems, Salt Lake City, UT) implanted in the hand area of dominant motor cortex on July 30, 2013. Data reported are from T7's trial days 231 and 245. At that time, T7 retained very limited, but consistent, index finger movements. Subsequent to these days, further motor impairment precluded tasks that relied on finger movements.

## Task design

Neural data were recorded during ‘center-out’ target acquisition tasks. The data were originally collected for neural prosthetic decoder calibration, as part of research testing algorithms for closed-loop neural cursor control (Gilja et al., Society for Neuroscience, 2013). In the ‘center-out’ task, participants controlled the position of a cursor on a computer screen by making physical movements with their fingers on a wireless touchpad (Magic Trackpad; Apple, Cupertino, CA). The cursor began in the center of the screen, and targets would appear in one of 8 locations on the periphery. Participants then acquired the targets by moving the cursor over the target and holding it over the target for 500 ms. In contrast to the prior macaque study (Churchland et al., 2012), the target acquisition task used in this work did not include a delay period. Therefore, participants were free to move as soon as the target appeared. Participant T6 was not limited in her ability to span the workspace of the touchpad. Participant T7's limited movements spanned a small region on the touchpad, approximately 1/8″–1/4″ wide.

## Recordings and data analysis

Data were aggregated over multiple sessions (T6: 8 sessions, T7: 2 sessions). Trial counts varied between sessions and across participants (T6: 75–220 trials per session, T7: 128 and 78 trials per session). The primary data analyzed were multi-neuron APs, which were taken as time points when a given channel's voltage exceeded a fixed threshold. Choice of threshold was dependent on the array (T6: −60 μV, T7, Lateral array: −80 μV, Medial array: −95 μV). Analyses were restricted to electrodes known to have significant modulation during attempted movements (T6: 39 electrodes, T7: 78 electrodes). Firing rates per electrode were then averaged across trials and filtered with a Gaussian kernel with standard deviation of 25 ms (T6) or 30 ms (T7).

## Analysis of rotational structure in the population response

jPCA analyses were performed as described previously (Churchland et al., 2012). Analyses were restricted to a 250-ms time period beginning with the rapid changes in neural activity that occur preceding movement onset. This period began approximately 180 ms and 300 ms after target onset for T6 and T7, respectively, corresponding to a difference in reaction times between participants. Overt movement was detectable at approximately 230 ms and 600 ms after target onset for T6 and T7, respectively. The delayed movements in T7 relative to T6 likely reflect a difference in disease progression between the two participants.

Pre-processing steps (‘soft’ normalization, mean-centering, and initial dimensionality reduction using PCA) were performed following Churchland et al., 2012. The initial dimensionality reduction step restricted the data to the top 6 PCs.

jPCA is a method for finding projections that capture rotational structure in a data set. (The method is described in detail in Churchland et al., 2012; here, we summarize its key features.) The method is based on comparing the neural state at a given point in time with its derivative. The initial dimensionality-reduction step (performed on the trial-averaged firing rates) reduces the data to the matrix Xred, which has dimensions d × ct (where d is the number of PCs kept, c is the number of conditions, and t is the number of time points). We computed X˙red, of size d × c (t−1), by taking the difference in state between adjacent time points (the final time point of Xred was subsequently removed to equalize the sizes of Xred and X˙red). We then fit the neural state transition matrices, M and Mskew:X˙red=MXred,

andX˙red=MskewXred,where M is unconstrained (fit via linear regression), and Mskew is constrained to be a skew-symmetric matrix (i.e., Mskew=−MskewT, which has purely imaginary eigenvalues), and thus, captures only rotational dynamics. The first jPCA plane is then constructed from the eigenvectors of Mskew associated with the largest eigenvalues. For a given jPCA plane, the basis vectors jPC1 and jPC2 are selected such that the pre-movement activity (the initial state) is maximally spread along jPC1, and that the net rotation in the plane is anticlockwise.

To measure the fraction of variance of the changes in neural state (i.e., the dimensionality-reduced data) that could be explained by rotational activity (Figure 3, bottom panels), the data were modeled as a linear dynamical system, where Mskew perfectly captured the dynamics between time t and t−1, that is, only purely rotational dynamics were allowed. Fraction of state variance explained for real and shuffled data was estimated using the top 6 PCs.

## Shuffle control analyses

One potential concern is that the jPCA method might be powerful enough to find rotatory patterns in state-space for any set of responses that contains complex, multiphasic patterns. The likelihood of finding such spurious rotatory patterns, which are common across conditions, increases as the number of conditions decreases. Thus, this is a larger concern in the current work (8 conditions per participant) than previous work with macaques (27–108 conditions per monkey) (Churchland et al., 2012).

To test for this possibility, we performed the three control analyses performed in Churchland et al., 2012 (described in their Supplementary Figures 2 and 3). Each of the three ‘shuffle’ controls preserves the diversity and complexity of responses, but perturbs the structure of the responses at the population level. Specifically, the dynamical model assumes that neural activity during the movement epoch follows in an orderly fashion from its pre-movement state. To test this assumption, the three shuffle control analyses disrupt the relationship between the pre-movement activity and the movement epoch for each channel. If these shuffled data sets still showed prominent rotatory activity, it would indicate that rotations might be found by the jPCA method even when not truly present.
