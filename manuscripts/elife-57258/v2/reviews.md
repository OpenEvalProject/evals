# Peer review - Round 1

Editors:
- Rebecca Seal, University of Pittsburgh School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57258.sa1](https://doi.org/10.7554/eLife.57258.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "A machine-vision approach for automated pain measurement at millisecond timescales" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor, one of whom is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Rebecca Seal (Reviewer #1); Andrew Shepherd (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Specifically, while an automated, objective approach to measure evoked mechanical pain behavior in rodents will be a highly significant contribution to the pain field and the authors have presented solid efforts toward this goal, several critical aspects of the PAWS system and its validation that would successfully elevate the approach to a level above the manual one published previously (Abdus-Saboor et al., t) remain underdeveloped or missing. (1) A clear, well-defined and easy to understand method for reporting the response using PAWS is lacking. (2) The point of measuring SJL and 129S1 strains as extremes using PAWS was weakened by the absence of measuring traditional von Frey and also motor function. (3) While the reviewers understand the appeal of the eDREADD approach to identify the role of specific brain circuits in pain, a classic inflammatory pain model to demonstrate the detection of hypersensitivity by PAWS would be more straightforward and have broader utility. (4) Many of the quantitative aspects of foundational measures used to interpret PAWS were lacking, for example, how non-overlapping response is defined in the LDA and statistical analysis for interpretations of significance. Please also see the full Comments from the Reviewers, included below. We do appreciate that you could make revisions that would address some of the reviewers' specific comments, but our determination is that addressing these concerns would be beyond the scope of a revision at eLife.

Reviewer #1:

This work described in the manuscript by Jones, Foster, et al., describes an automated protocol to quantify and interpret (based on 8 components of the paw trajectory: 4 pre and 4 post) the response of mice to noxious and innocuous mechanical stimuli applied to the plantar hind paw using high speed video recordings. The protocol is designed to objectively report whether the mouse interprets the stimuli as non-painful or painful as well as the severity or intensity of the pain. Mouse strains that show extremes in their response to the stimuli (hypo and hyper) and also eDREADD activation of the pain neuronal ensemble within the amygdala were used to validate whether the protocol is able to accurately quantify and interpret a range of stimuli.

Comments:

The development of an easily accessible, automated and objective way to measure evoked mechanical pain in rodents will be extremely valuable for the field, as will delineating affective versus discriminative components (and in the context of chronic pain) and this is a good first step.

1) Authors should discuss variability in PAWs in relation to the variability inherent in the methods used to simulate the paw.

2) PAWS data in Figure 4 are showing significant differences between CS+DB and LP+HP in the scoring but the LD1/LD2 analyses extract differences in the LP and HP for post-peak features. A deeper explanation of how data are to be reported be interpreted would be helpful.

3) Activation of the pain ensemble with the DREADD and CNO evokes a pain like behavior. I would have expected that the LP would have resulted in greater shaking and guarding behavior than the -CNO control. Do the authors have an explanation?

4) Authors should discuss the interpretation for how mice like the CBA strain, which seem hypersensitive in the traditional testing method but are apparently within range by PAWS, compare to the SJL mice, which were not tested by the traditional method but are deemed hypersensitive by PAWS.

5) The 0.7 probability correct shown in Figure 5 and Figure 6 as being sufficient should be interpreted for the reader a bit more than what is provided in subsection “Automated scoring of rapid paw dynamics and lingering pain behaviors”. Related to this: There are no stats for these comparisons.

6) The rationale for mentioning a potential relationship to aggressive behavior in the Discussion section is not well-developed. What about a relationship of PAWS outcomes to the magnitude of a startle reflex?

Reviewer #2:

In this article, Jones et al. describe an automated assessment of tactile sensitivity. They report development and validation of a novel combination of high-speed videography and automated paw tracking. With this resource, they demonstrate that paw withdrawal to innocuous versus noxious stimuli can be separated in six inbred mouse strains. Using this system, they also present evidence that activating an ensemble of basolateral amygdala neurons during noxious stimulation changes paw withdrawal metrics. This approach represents a significant advance in behavioral assessment of tactile sensitivity, with the potential to contribute to much-needed discoveries in this domain.

Major comments:

This manuscript builds upon prior machine vision-based approaches in other animal models. High-speed videography of such withdrawal responses has been attempted before, but the demonstration of the ability to detect chemogenetic activation of pain aversion neurons in the amygdala and the validation across multiple inbred strains are new developments. The importance of this approach stems from its potential to address previously challenging problems, i.e. high-throughput, objective assessment of sensory and affective components of innocuous touch and noxious stimuli. PAWS has the potential to drastically improve the resolution and dimensionality of rodent pain scoring when compared to subjective 'yes/no' withdrawal scoring and threshold calculation, which has been the standard in the field for several decades.

1) Chemogenetic activation of a BLA pain ensemble is a worthwhile experiment, but the rationale for choosing this particular experiment wasn't particularly clear in the manuscript. Many potential experiments could have been proposed that would target some aspect of the pain neuraxis, with the hypothesis that a shift in sensitivity would be detected by the PAWS system. Why did the authors opt for chemogenetic activation of a BLA ensemble? Furthermore, would an equivalent experiment using an inhibitory DREADD have been likely to tell us anything further? Can these experiments tell us anything about the affective component of a response to a noxious stimulus in terms of paw withdrawal responses?

2) It would benefit the readers to state more clearly that analgesic reversal of pain-related changes to paw withdrawal were detected in Abdus-Saboor et al., (2019), wherein a software-assisted, manual scoring system of similar indices was used. Reversal of changes in paw withdrawal-associated behaviors is a robust indicator that they are pain-related.

3) In Figure 6, the authors mention two outlier strains (129S1 and SJL), which exhibit unusually low and high degrees of sensitivity. I applaud the authors for the inclusion of these datasets; it benefits the research community to describe the limitations and caveats of a new assay as early and as comprehensively as possible. However, are these shifts in sensitivity in 129S1 and SJL seen with conventional von Frey hair testing, as reported for the other strains in Figure 1B?

Whether or not von Frey data 'match' the PAWS data for 129S1 and SJL mice, it is likely to be instructive. A match between von Frey and PAWS data would be further validation of the accuracy of the PAWS system, and a discrepancy would raise the possibility that PAWS is extracting information from a multidimensional dataset which cannot be achieved with conventional von Frey assessment.

4) Related to the previous point, it is not clear if prior reports characterizing pain sensitivity in 129S1 versus other strains have also seen relative hyposensitivity. The discussion does mention that such strain differences have been assessed, but no direct comparisons are between these reports and the data in this manuscript are made.

5) In subsection “Statistical modeling with linear discriminant analyses separates touch versus pain across six inbred mouse strains” the authors note that pre-peak paw movements are nocifensive in nature, whereas those behaviors seen post-peak (shaking/guarding) are supraspinal in origin. I agree that this distinction seems plausible, given the timescales involved, but are there data in the literature to support this? Unless this is founded upon findings from prior studies, this comment might be more at home in the Discussion section.

Reviewer #3:

While I appreciate the importance of what the authors are seeking to accomplish in this study, it is not obvious how PAWS (Pain Assessment at Withdrawal Speeds), which scores eight defined behavioral endpoints, can be easily used by researchers in the pain field to quantitatively evaluate the magnitude of pain or to accurately predict the pain state. The authors convincingly show that a painful pinprick evokes a withdrawal response that looks very different from a non-painful response in terms of trajectory and pattern. A more straightforward approach would thus be to develop an algorithm that captures and classifies these trajectory and pattern differences over time. This would likely generate a more accurate and simple classifier relative to what the authors did-breaking these distinct motions into component variables like X and Y velocity, paw height, etc. The authors should seek to capture this visual difference in paw withdrawal trajectories with a single metric, and then show that this metric is scalable based on pain intensity. Without such a measure, the current implementation of PAWS is of limited general use for those who are interested in studying pain in mice. For example, what endpoint(s) is someone in the field supposed to use when studying pain and responses to analgesics? Y-velocity? X-velocity? # paw shakes? Paw height? All of these variables? Two of these variables? Three? Four? It is confusing and not simplified.

The title of the paper implies the machine vision approach is automated; however, this does not appear to be the case. The first step in this process is to manually label the center of the stimulated paw. This is thus more akin to a "semi-automated" approach.

Time of the first withdrawal peak (t*) is a critical variable in their analytic pipeline. However, it is unclear precisely how t* is calculated or defined. In the paper, authors write that t* is the time leading up to the initial paw peak. And in Figure 3A, since this is a 3d graph in 2d, it is unclear where t* is relative to the trajectory data.

From the LDA analyses, the authors state that the low and high pain stimuli separate from the no-pain stimuli (Figure 5A,B). However, I do not see a clear separation between these groups in the figure. Instead there appears to be significant overlap, which raises the question as to how specific the LDA analysis is at discriminating, in a quantitative manner, the magnitude of a pain response.

Figure 1B. The paw withdrawal frequency data has no error bars and the number of mice used to generate these data is not indicated. The authors write that strains differ in some of these assays but provide no statistics to confirm that the differences shown are statistically significant. Moreover, the authors are encouraged to consult and cite work by Jeff Mogil's group who evaluated mechanical sensitivity in different mouse strains many years ago.

Figure 3B and C are difficult to interpret. Provide more details in legend and in the figure itself. Ex. in B, are those lines with two arrow heads? What does the length of the line and angle of the line mean? And in C, how was the shaking vs guarding bout determined? Was this done by a human or did the algorithm make these assessments in an unbiased manner?

Figure 6. Authors state 129 and SJL mice are outliers, but based on data presented in this figure, it is hard to appreciate how exactly they are outliers. In panel B, 129 mice show a similar probability correct relative to all other strains, and SJL error bounds largely overlap the other strains. An outlier is typically defined as being two or more standard deviations from the mean.

Moreover, the atypical withdrawal response may have nothing to do with a pain hyposensitivity phenotype, as the authors assert. Instead, these strains may simply have motor deficits that prevent them from performing more vigorous/elaborate paw withdraw responses.

The use of chemogenetic amygdala stimulation to demonstrate the efficacy of PAWS for detecting hypersensitivity to noxious stimuli seems out of place in this study. A simpler, more straightforward, and more broadly applicable (for pain field) approach would be to inflame hindpaw with complete freunds adjuvant and/or perform a nerve injury surgery. These are commonly used ways of inducing pain hypersensitivity in the field, and hence as a first test, it will be important to show that PAWS can detect this form of hypersensitivity.

Moreover, it will be important to show that PAWS can detect graded changes in pain hypersensitivity, such as in response to a known analgesic.
