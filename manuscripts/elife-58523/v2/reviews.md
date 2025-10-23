# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58523.sa1](https://doi.org/10.7554/eLife.58523.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper is a clear account of an odor-guided behavior in which the authors use machine-learning movement analysis to work out how mice combine odor sampling with a set of sniff-locked movement motifs in their decision-making. The authors find that in this task, the mice use odor gradients, but do not use stereo olfaction. The careful characterization of movement motifs during the task will be useful to relate olfactory decision-making with neuronal activity.

Decision letter after peer review:

Thank you for submitting your article "Sniff-synchronized, gradient-guided olfactory search by freely-moving mice" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Catherine Dulac as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analysis is required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This paper is a clear account of an odor-guided behavior in which the authors use machine-learning movement analysis to characterize the behavior in detail. The key findings are sniff-synchronized movement (already known), the ability to classify a number of movement motifs (but not strikingly distinct) and the further analysis of relationships between these movements and sniffing.

All reviewers felt that this detailed analysis of behavior in a non-invasive manner was exciting and has much promise for the field.

Essential revisions:

The reviewers felt that the interpretation of sampling and movement needed a better understanding of the strategy used by the mice.

They suggest that there are several possibilities:

– The animals could be memorizing absolute concentrations.

– The animals could use two samples during the turn, to ascertain gradients.

Further, they felt that the motif analysis might be useful to elucidate how the animal corrects an initial decision.

They feel that the authors need to provide the reader with a detailed and rigorous analysis of the decision strategy. As the discussion on this topic was extensive, I have provided excerpts below to help the authors.

In addition the authors need to do more with the analysis, clarifying:

– Animal differences and lack of stereotypy in movements;

– Nose speed during ITI;

- State transitions and error correction;

- Decision points.

Here I provide excerpts from the extensive discussions on this paper. The intention is to give the authors an understanding of the key points that the reviewers took from the paper, and where they felt that its analysis could be strengthened.

After watching the videos several times, here is my interpretation of the decision strategy: when the trial starts, the mouse faces away from the gradient. It must make a rotation of ~180 degrees to align its body with the direction of the gradient. This stereotyped movement forms an arc of the alpha shape of Figure 3D. While rotating, the mouse could already detect whether the concentration increases or not. Upon the detection of an increase, the mouse infers that the gradient points in that direction, and it initiates a walk toward the corresponding odor port. During that walk/approach, the mouse sniffs a couple of times. If a decrease in concentration is measured during these sniffs/samples, the mouse might still be able to stop and reorient before the decision boundary.

In addition, I don't think that a sequence of samples on the left and the right side must be taken for the mouse to infer the direction of the gradient. All it needs to do is compare the intensity when the head is aligned with the body (before ) with the intensity after a lateral sample (after). If an increase is detected, the head must be pointing toward the gradient. In the videos, I didn't see systematic left-right samples.

…

sampling a landscape with two longitudinal asymmetric gradients would be challenging. This situation would make the sensory experience associated with an alpha turn largely inconclusive. Without making multiple samples on the left and right sides of the midline, a mouse would not be able to obtain a coarse map of the landscape to inform its decision.

But the intensity landscapes reported in Figure S2 indicate that most gradients do not really have two real maxima (or two lobes). Even for the 60:40 condition, the landscape essentially looks like one smooth gradient with a maximum on one side. So the sensory experiences produced by an alpha turn toward the left and the right side might be different – a signal the mouse might learn?

That said, I was puzzled by the fact that the two landscapes corresponding to the 60:40 conditions are quite different when 60 is located on the left or the right side (top versus bottom panels in Figure S2B). So, one might expect that the 60:40 – right would be harder to scan than 60:40 – left. Since the performances of the left and the right conditions were lumped together, it's impossible to tell whether this prediction is correct.

And here is another possible strategy:

An alternative possibility is that animals are not actually making L-R comparisons and just memorizing 'expected' gradients or absolute concentrations (100, 80, 60 etc) – which is actually quite easy for mice to learn!

In that case, indeed the mouse actually already knows which side the reward will be. If during the alpha turn it smells concentrations 100 or 80 or 60, it sticks to that side, otherwise walk to the other side. Indeed in this scenario – there is no need for lateral comparisons – and the knowledge gathered during the alpha turn already tells the animals which side it should go towards.

But this in principle is a different task than the authors intended to set up!

The authors actually do try to rule out the possibility that animals learn absolute concentrations by doing what they refer to as variable |C| sessions (Figure S4 B). i.e. by present the same absolute concentration, but in opposing contexts – one where its the higher of the two concentrations (30:10) versus one where its the lower of the two concentrations (30:90).

But the data presented is not really conclusive –.…

performance in the first 10 trials is quite low – so its very likely that the animals just learn a new rule..

Reviewer #1:

This paper is a clear account of an odor-guided behavior in which the authors use machine-learning movement analysis to characterize the behavior in detail. The key findings are sniff-synchronized movement (already known), the ability to classify a number of movement motifs (but not strikingly distinct) and the further analysis of relationships between these movements and sniffing.

The basic behavioural checks and controls are thoroughly done. It is interesting that there is no stereo component to these decisions.

A key finding is sniff-synchronized movement. This has also been seen in other studies (Kurnikova et al. 2017, Moore et al. 2013, Ranade et al. 2013) as the authors point out. I was looking for a clear statement of how the current work advances this understanding.

Motif analysis.

The motifs don't appear to be particularly crisp, in that they continue to contribute up to 100 motifs. I was looking to see this enumerated, as in % of variance explained (or in this case cross-validated log-likelihood). It turns out it is done in Figure S8C. This should be in the main text.

There is nice but not much explored finding of there being distinct movement patterns between individual mice.

The motif correlation to stage of trial and to sniffing and nose speed is interesting but maybe not surprising. The subsequent analysis shows up a number of patterns here which are suggestive of general synchronization between breathing and other motor rhythms. I wonder if the authors could do a zero-order correlation, of something simple like leg movements which are much more directly quantifiable than these motifs. Or has such work been done?

The main accomplishment, to my reading, is the detailed characterization of sniffing and its relation to movement. The authors are candid about the being mostly a descriptive account of behavior and movement and make a case for this being a prerequisite for subsequent mechanistic and interventional studies.

On the one hand, I appreciate the value of a thorough descriptive account of freely moving behavior. However, it seems to me that the motifs are fuzzy and the core outcome of sniff-locked movement has been reported. I wonder if there is more to be gleaned from this rich dataset, such as an analysis of what differs between mice or whether there is something underlying the lack of stereotypy in the movements of the mice.

Reviewer #2:

In this study, Smear et al. aim to investigate how mice sample the noisy stimulus information from olfactory plumes such as to navigate towards their source. To this end, they developed a 2AFC task for freely moving mice where the same odor emanates from two lateral sources, at independently controllable concentrations. Mice are required to identify the more intense of the two sources and collect water from reward port located on the side with the higher odor concentration. The authors improve on previous attempts at studying this problem by requiring the mice to commit to their decision at a substantial distance from the odor ports. This forces the mice to assess odor concentration from distal cues rather than via serial sampling of the sources themselves. Interestingly, the authors find that stereo olfaction (comparing concentration across two nostrils) is not required to determine source location from distal cues. Using a series of stimulus conditions, the authors convincingly show that in their paradigm, mice rely on olfactory cues and specifically the relative, not absolute, concentration difference between the two sources.

The relevance of stereo olfaction for airborne odor cues has been long debated. In my opinion, the authors results in principle resolve this debate – stereo comparisons allow finer source localisation near the source, while serial sampling may play a larger role farther away from source. One concern however is that this lack of reliance on stereo sampling may result from the specific task design and the constraints it imposes on the behavior (see concerns).

Further, the authors characterise the sampling behaviors of mice during this task by monitoring respiration (thermistor) as well as nose, head and body positions (video tracking). The authors find a striking, active synchronisation of sniffing and nose (and body) movements that gets selectively recruited during putative investigatory phase of the task i.e. when mice are actively exploring the concentration gradient. The authors do exhaustive analysis to show that such synchronisation is not a default state and the coupling is much weaker during other phases within the same trial. While such coupling of movement and intrinsic rhythms has been proposed previously, to my knowledge this is the first careful characterisation of this phenomenon in freely moving mice. Importantly, the authors results not only confirm the existence of such coupling but also clarify that this synchronisation is an active feature of olfactory navigation. Interestingly however, the authors do not find any significant difference in sampling strategies across different stimulus difficulties (see concerns).

Lastly, the authors use machine learning to parse motion trajectories into identifiable behavioral motifs. With their approach, they find that a range of motifs that are stereotyped across mice and occur in non-random sequences during each trial. Further, a trained decoder can successfully decode mouse identity from the sequences in which these motifs in each animal. While these motif based analysis are well done, the data presented do not seem to make any clear predictions about how these motif sequences would change in different task conditions. The authors do not find any obvious relationship between trial types (difficult versus easy stimuli) and motif sequences and the presented analyses do not add much to the main message of the paper. I therefore lack the imagination to accurately assess the relevance of this portion of the study.

Overall, the study is well executed – the data presented are clear with numerous controls at each step. In my opinion, the evidence provided for lack of need for stereo olfaction for distal source assessment and active synchronisation of sniffing and sampling movements are important contributions to the field of olfaction that warrant publication in eLife. However, I have several conceptual concern about the task design and the interpretations of the results that the authors should clarify prior to publication.

1. My primary concern is about the task design. I commend the authors for the careful control of olfactory stimuli and substantial improvements over previously published odor localisation assays by separating the reward port from the odor source and forcing decisions at locations distant from the source. However, the task design chosen does not really require the mice to localize odor sources beyond just indicating whether there is more odor on the right versus left. This is different from natural conditions, where the necessary spatial resolution may be much higher. In fact, finer source localization confers no additional benefit for maximizing reward in this task. Therefore, the sampling strategies exhibited by the subjects here may be different from those employed during natural odor navigation where the motivation is to precisely locate the source of mate, food or predators.

2. Along the same lines, it is surprising that even for the easiest version of the task, the performance hovers around 80%, even though PID characterisations show very clear differences between the two halves of the arena. Furthermore, performance drops with increasing stimulus difficulty but mice do not appear to change their sampling strategies to compensate for the lower reward rate. I am trying to reconcile these two facts. At first pass, given known olfactory acuity of rodents, it seems that trained mice should have no trouble handling the easiest stimuli (reach almost 100% success). One possibility is that the mice are not fully motivated/engaged in the task. An alternate explanation is that mice are fully motivated to reach maximum reward rate, but the task is just too hard and the sampling strategies employed at 100:0 condition are their best, and therefore with increasing stimulus difficulty, they cannot perform any better. Yet, the latter possibility appears very unlikely. Can the authors comment on these two possibilities? The question remains whether mice when pushed to achieve higher performances would employ different sampling strategies.

3. Lastly, looking at Figure 5Ai it appears that overall nose speeds are significantly lower during ITI than during the investigatory bouts within the trial. While the authors rule out that sniffing-movement synchronisation is simply a feature of rapid sniffing, they do not rule out the dependence on running speeds. Perhaps the apparent lack of synchrony in ITI results from poorer ability to resolve decelerations, given lower speeds on average. This is also consistent with reduced, but significant synchrony during premature initiations in the ITI (Figure S7A) where speeds tend to be higher than those shown in Figure 5Ai. This should be easily addressable by repeating the analysis on speed matched datasets.

Reviewer #3:

In this manuscript, Findley and colleagues propose a novel assay to study the behavioral strategy freely moving mice adopt to navigate turbulent odor gradients. This assay is neat and well-thought. It sheds light into the control of active sampling through sniffing and search patterns involving head and body movements. The work is an admirable technical tour de force. The results are built on solid data analysis, which makes use of unsurprised machine learning to avoid subjective biases in the categorization of behavioral states. The manuscript offers a wealth of data that should be a wide interest to the field of olfaction. Finally, the conclusions are presented in a way that is balanced and supported by the well-controlled experimental data. This manuscript combines innovation with rigor to advance our understanding of olfaction in rodents (and beyond).

I have a few suggestions to improve the manuscript. These suggestions do not require any additional experiments.

1. An exciting finding of the manuscript is the description of two behavioral states underlying odor search: investigation and approach. The authors might want to push the analysis of the search strategy one step further by defining whether/how mice can switch from investigation to approach, back to investigation to perform error correction. This process would rule out that animals find the gradient through an initial guess that leads to a full commitment to one side during the approach phase. The data suggests that error correction takes place (Figure 7C and D), but those cases are not analyzed in detail. Can a statistical analysis of the state transitions reveal any principles in the organization of error correction? Does the animal's state indeed switch from approach to investigation during error correction?

2. The occupancy diagram of Figure 3F is fascinating. Together with panel 3D, it suggests that mice undergo fairly stereotyped searches: after poking their nose out of the initiation port, they appear to make a 180 degree rotation (sweep) to face the gradient. The density reaches a maximum at that point (opposite to the position of the initiation port). Is this position (crossing of the alpha shape) dominated by an "investigation" state? Can this position be viewed as a decision point? When/where does the animal tend switch to the "approach" state? More generally, could you map dominate trends in behavioral motifs of Figure 6B onto the stereotyped alpha shape of the occupancy diagram of Figure 3F?

3. Figure 2D: Could you speculate about the reason why trials tend to be longer for the 100:0 conditions compared to the more difficult 60:40? Do mice spend more time in the investigation phase when gradient is stronger? Although this result would be counter-intuitive, it might suggest that mice learn (?) to spend less time on the initial search when less information is available to them.

4. Figure 1D indicates that the average gradient's geometry is not the same when the odor is delivered on the left side (100:0) compared to the right side (0:100). This observation appears to be true for the other odor ratios reported in Figure S2. This asymmetry should affect the gradient that the animal experiences during the investigation phase, which should in turn influence the accuracy of the decisions. Do you expect a 50:50 condition to produce no preference (on average)?

5. Figure 7F: What are you concluding from this panel? Are you sure that the shaded areas represent the standard deviation and not the SEM? If the standard deviation is shown, how do you explain the existence of stereotypical wiggles on a timescale of 50 ms? It would be very useful to represent a variant of Figure 7C where the trials are sorted between correct and incorrect.
