# Peer review - Round 1

Editors:
- David Kleinfeld, University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55964.sa1](https://doi.org/10.7554/eLife.55964.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Murphy and co-workers have advanced the field of high throughput imaging coupled with behavior to a new level of automation – demonstrating around 2,000 self-initiated imaging sessions per day per mouse for all mice in a colony- that incorporates an online SQL database to segue with the ambitions of a multitude of community-wide efforts in data sharing. This work significantly extends the 2013 pioneering effort of the Brody and Tank collaboration, as well as prior work by the Benucci, Goldberg and Murphy laboratories, among others, to create effective, efficient, and open source tools for longitudinal studies of the neuronal basis of behavior.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Automated task training and longitudinal monitoring of mouse mesoscale cortical circuits using home cages" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: James Ackman (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

All three reviewers of your "Tools and Resources" article, as well as the Reviewing Editor, are serious players in the field of cortical dynamics and imaging from awake animals. They and I recognize the continued impact of your work on automated behavior and imaging with modestly priced equipment to promote high throughput experiments and enable adventurous queries. Yet the content in the current paper, which includes technical advances and demonstration imaging data, is judged to be too incremental to warrant publication. The claims will gain in impact if the increase in throughput is used to solve a narrow but nontrivial scientific issue, or make a novel kind of observation, as opposed to making a solely demonstration measurement.

We kept in mind the criteria for the Tools and Resources category in reaching this decision. This category highlights tools or resources that are especially important for their respective fields and have the potential to accelerate discovery. Tools and Resources articles do not have to report major new biological insights or mechanisms, but it must be clear that they will enable such advances to take place. The concensus was that, while there are many laudable aspects to your approach, the current approach is not a sufficiently large advance over the previous approach to warrant publication in eLife.

We would welcome a new research article that involves an application of this new tool. The Reviewing Editor provided some suggestions, but of course, we recognize that you are already engaged in a vigorous research program that might encompass these or serve as an alternative. I pass them along for your consideration.

1) An expanded imaging study during the Go/NoGo task, i.e., the use of many mice to establish cortical patterns instead of the one mouse as shown in Figures 8 and 9.

2) Activation of the orofacial regions (forepaw, jaw, tongue, vibrissa) in motor and sensory cortices are certainly of interest.

3) An imaging study from multi-animals study that looks at potential gender differences, with reasonable statistical bounds and controls, could fulfil this role.

4) Other extensions, e.g., plasticity of cortical responses during learning, may be more feasible.

Reviewer #1:

In this "Tools and Resources" article, the authors report on an improved methodology for doing widefield imaging in the home cage. The opportunity to measure behavior and neural activity is important, and the authors highlight reasons such as reduced stress for the animal, and removal of experimenter-to-experimenter variability. Further, the chance for automated fixation in conjunction with widefield imaging is exciting, as widefield imaging is turning out to be an informative and high-throughput way to measure neural activity during behavior.

The method proposed here is an improvement over a previous automated head-fixing apparatus that the authors reported a few years ago. Here, the mice are willing to have daily fixation durations that are much longer. In about half of the mice, the observed 28+/-17 headfixations/day (18+/-13 mins/day).

The paper has a lot of strengths. It includes data from 44 mice and a total of >29K task related videos. The authors also created a relational database to allow analysis pipelining. This information, along with a lot of other useful information, such as the drawings for the head straightener that prevents the mouse from going in sideways, are all provided. There are also a lot of nice touches in the system, such as the text messaging system that alerts the experimenter if animals are in the tube too long; this is thoughtful from the point of view of animal welfare.

There were also a number of observations based on this large-scale approach that were interesting. These include the linked behaviors between mice (Figure 4A, B) and the fact that mice had higher success rates while headfixed although they preferred to be head free (Figure 5C). The fact that performance was similar over the 24-hour cycle was also interesting.

Finally, to deal with hemodynamic contamination of the widefield data, the authors captured 440 nm light in addition to the GCaMP signal. They then subtracted one from the other. The authors acknowledged the really beautiful alternative methods for this developed by the Hillman lab, but justified their use of a simpler method based on some constraints of the device, which I thought was fine. Other papers in the literature have entirely omitted hemodynamic correction so I appreciated the efforts to do this.

First, I was concerned that the authors didn't make sufficiently clear how this work is an advance on the Aoki, Benucci et al. approach that was published in 2017. The text states that, "While an advance for training, this work did not longitudinally gather brain imaging data in an autonomous manner, nor were the systems of a footprint or cost appropriate for running at scale." But in the Aoki paper, 2-photon data was collected for 21 days (Figure 5D). The measurements were not taken in the home cage; if the authors feel that is a critical difference, they should state why. I also wasn't sure how to compare the cost difference with that approach and the one presented here. The Aoki apparatus does appear to be commercially available (http://ohara-time.co.jp/wordpress/wp-content/uploads/SelfHead-restraintOperantTestSystem_Pamphlet2017.pdf), but I wasn't sure of its price or the total price of the setup in the current paper so it was hard to compare.

Second, the authors included no female mice in their study. There seems to be no reason that a cage of all female mice might be tested as well. Inclusion of both sexes in a study is now required by many funding agencies, and is good scientific practice because it ensures that scientific conclusions are not made that only apply to one sex and not the other.

Third, I wasn't sure whether the total fixation time of the mice provided sufficient time for measurement of behavior and neural activity. It seemed that the total fixation time wasn't very long – on order of about 18±5 minutes/day (subsection “Improvements to the cage hardware”) for the good performers. It would be helpful to see the distribution of total daily head-fix times for all mice, as well as the distribution of within-day times, at least for some of the good mice. It would also be helpful to see the distribution of total daily completed trials. The Bollu paper (which admittedly isn't a totally fair comparison) reported >2000 trials/day and the Aoki paper reported ~1000 trials/day. The reason I bring this up is that widefield measurements can be very noisy and so high trial counts are extremely helpful. This is especially true given that, as the authors point out, the signals reflect movements, the timing and magnitude of which vary a lot from trial-to-trial. If the approach in this paper is to be useful for sensory or cognitive tasks, large trial counts are needed.

A related point, I couldn't quite understand the sentence comparing good and bad performers (see the aforementioned subsection). It stated that bad performers had less than 20 min of head-fixed time while good performers had while "good performers averaged 15.8+-19.9 h." I think h can't mean hours since the animals didn't headfix 16 hours/day. But it can't mean minutes either, because that would imply that the good performers were fixating less than the poor performers.

Finally, I found that the behavioral/widefield data included at the end (Figure 8 and the section titled, "Task training error analysis examples") was not very useful. The problem is that it is hard to conclude very much from such a small sample size. There is only 1 animal shown in Figure 8 and so the comparison between go and no-go trials (Figure 8B vs. Figure 8C) is not that informative. Further, the data didn't really add that much to the paper. The reason is that this paper is meant to be a tool and a resource. It does that well. The scientific observations in Figure 8 weren't really in the service of that goal. It might be better to include that (potentially interesting) data in a different paper with a larger cohort of subjects and a lot more analyses.

Reviewer #2:

Achieving high-throughput behavioral training and subsequent automated task administration with physiology is a significant aim for the field of systems neuroscience. The Murphy lab and others have made notable contributions to this aim, which are described in the Introduction to this manuscript. The Murphy group, specifically, has previously reported automated methods for home cage behavioral training and for head-fixation with mesoscopic calcium imaging (in the absence of a specific behavioral paradigm). Here, they describe improvements on their previous head-fixation and imaging method and integration with behavioral training and task performance.

Small improvements in the design of the head-fixation system and refinement of their training protocol yield longer and more frequent head-fixations. Using their updated system, they successfully train 21/44 mice to undergo head-fixation to obtain water rewards. While head-fixed, the mice are trained to perform a detection task with varying degrees of success. Further, 10 mice progressed to a go/no-go task, but only 5 of those mice were able to perform the task (as assessed by a relatively lenient d' criterion), and there is no detailed presentation of this behavioral data in the manuscript. The mesoscopic imaging data presented reflects examples from a few selected mice without any analysis of results across mice, and the major benefits of the system (longitudinal mesoscopic imaging across training) are completely unexplored.

The challenge with this manuscript is that it does not present a compelling methodological result, nor does it describe a compelling experimental finding (it's neither fish nor fowl). The methodology is very promising and the authors should be applauded for the impressive level of detail with which they describe the construction of their system, however the methodology as presented appears to be an incremental improvement on the Murphy lab's previously published results (Murphy et al., 2016), and it's very difficult to tell how much of an improvement it actually represents. The first sentence of the Abstract notes a '4X improved automated methodology', but 4X of what? On the other hand, if the manuscript were focused on an experimental finding or data set, it falls short because of the rather incomplete data (one mouse in many experimental groups, little group level or longitudinal analysis), and further the somewhat opaque manner in which data are presented make it difficult to assess the results and compare to previous work by this group and others.

1) The criterions employed, if any, to move mice between training stages are not described, hampering the reproducibility of the study.

2) It is unclear how the length of individual head-fixations is determined. Can mice exit trials at any time? Further, there are no behavioral measures (other than repeated, "clustered" head-fixation) that indicate whether mice are comfortable in the head-fixation system. A lack of comfort could underlie the poor performance of many of the mice in the detection task.

3) The study pools data from several iterations of the home cage system with different conditions across the cages. Further, cage 3 experienced an unexplained outage. This makes the presentation of data in Figure 3 confusing and difficult to interpret. Clarity would be greatly improved by reporting results for a group of cages with consistent and optimal conditions. At the very least, data should be separated clearly by mouse to make it easier to assess changes in performance. Further, the 23 mice that perform well in training should be presented separately from those that did not progress. Additionally, given that the training periods were of variable length, it is not possible to assess the data (as currently presented) relative to the different training milestones.

4) The inclusion of data from non-head-fixed trials detracts from the manuscript. Given that the system is designed for imaging during behavior (which necessitates head-fixation), only data for head-fixed trials should be presented. There is no comparison of behavioral or imaging data collected with automated (infrequent, short-bout) head-fixation and extended manual head-fixation for comparison.

5) Group-level and longitudinal analysis of behavioral data from the detection task (which should have sufficient N), would strengthen the manuscript. The inclusion of limited go/no-go behavioral data detracts from the manuscript, as it does not appear that the current training regimen has been optimized for performance of this task.

6) In section 1, the authors claim that use of a Raspberry Pi camera module is not inferior, but they do not present any data to support this claim.

7) The mesoscopic imaging presented is sufficient to demonstrate that imaging can be performed in their home cage system. However, that was already established by their previously published manuscript (Murphy et al., 2016). At the very least, group level or longitudinal analysis should be performed to facilitate comparison with results published by other groups with conventional imaging paradigms.

Reviewer #3:

The authors improved upon a home cage system they reported on previously in Murphy et al., 2016. Docking system was improved for greater mouse participation, with a more effective training period. Additional monitoring of animal's behavioral state was added. Functional data is provided for a go/no-go licking task.

All materials are provided, along with schematics and acquisition code, and are a benefit to the greater research community. Automated longitudinal population studies are important for furthering our understanding of the neural basis of behavior.

1) Much of this work has already been published (Murphy et al., 2016). Details provided here are improvements upon the original methods, rather than new findings or techniques.

2) Home cage system is described to be optimized for capturing long-term functional changes in cortex, yet the data showed no functional changes after training. Described results did not elucidate benefits of using this system.
