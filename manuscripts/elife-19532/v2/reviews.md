# Peer review - Round 1

Editors:
- Peggy Mason, University of Chicago , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19532.039](https://doi.org/10.7554/eLife.19532.039)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Eco-HAB – fully automated and ecologically relevant assessment of social impairments in mouse models of autism" for consideration by eLife. Your article has been favorably evaluated by a Senior Editor and four reviewers, one of whom, Peggy Mason, is a member of our Board of Reviewing Editors. The following individuals involved in the review of your submission have agreed to reveal their identity: Thomas Bourgeron (peer reviewer). Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The principle reasons for the decision were:

1) The reviewers were uncomfortable with the potential COI. The manuscript was viewed as not sufficiently differentiated from an advertisement. If the system design is to be open source, that should be clearly stated. If the system is to be sold commercially, then a clear COI statement must be included.

2) The system needs assessment of reproducibility across cohorts, validation with manual scoring and comparison to other existing systems.

If the authors can adequately address these issues, then eLife would be interested in taking another look.

Reviewer #1:

In general this is a valuable methodological contribution to the study of social interactions of mice. The system is novel and is likely to yield new data such as the VPA data provided as an example here.

Most of my suggestions are minor but a few overall comments are warranted.

The methods should be better integrated into the text to increase readability. Same with the supplementary figures which are beyond onerous. With the exception of code or circuit diagrams, put all figures into the manuscript in the order needed. Do not use supplemental figures.

What is the time limit for mice in the apparatus? 72 hr is used here – is that the limit and what is the limiting factor? How is air exchange handled (I am assuming that the system is closed on the top)?

How scalable is this system in terms of size? Can it be used for guinea pigs? rats?

The sociability measure is well described in the methods but the "Social preference" appears to me overly derived. Raw numbers – time in chamber with (and wo/) the social odor before during and after the odors presence would be better than the normalized factor used.

It is very confusing to use the term Social preference to refer to the mouse going to the mouse in a 3-chamber test and to a social ODOR in the eco-hab. I highly recommend using the term approach to social odor.

Throughout the manuscript, it is problematic that no non-social stimuli are tested – e.g. a non-social odor or an object. This limits the conclusions about the sociability per se of the measures. Nonetheless, the point here is a novel apparatus which could be used to make these direct comparisons even if they have not yet been made.

Reviewer #2:

This manuscript describes a four-chambered system for animal tracking using RFID tags and antennas as opposed to other available methods (video tracking, IR beam-breaks, piezoelectric floor, etc.) One major advantage of RFID tracking is that it allows for the testing of multiple animals in one arena with individual identifying information. The Eco-HAB apparatus described allows animals to explore a sizable space, the symmetry allows for comparison of different stimuli, and tube connectors may increase mouse comfort in the arena. The authors make an important argument about the need for better reproducibility in social testing, and provide data suggesting that social approach in anxiety-prone balb/c mice is different in the standard 3ChA test under high and low stress conditions. While they did not test the eco-HAB under different lighting or animal handling history conditions (making it not a direct comparison to either the 3ChA comparison or cross-lab variability), data from different time points suggests that the eco-HAB system provides consistent results. The authors further provide empirical data showing the utility of this system in assessing social behavioral differences across multiple variables (including mouse strain, VPA treatment, Fmr1 knockout). Finally, they present a neat metric they call "in-cohort sociability" that provides something really different from standard 3ChA testing because it measures social behavior towards known individuals. One might imagine a scenario under which novel animal social cue exploration might decrease but in-cohort sociability would go up, and having both metrics adds a lot to the interest of this setup.

1) This report may blur the boundary between a detailed description of a methodological advance and the advertisement of a commercial device (available for ~$2000 euros). Other eLife tools reports I've seen use commercial resources but not ones they are selling. I defer to the editor to determine suitability.

2) Data validation must be included so that the accuracy of the software and hardware are disclosed. In particular, a nontrivial amount of testing time should be dually scored by human video observers (e.g. at slow speed on visibly marked individuals) and the RFID data collection system. The authors mention that some signals are dropped, and this is a classic issue with RFID reads – fast moving animals can be missed, and partial tag reads can abound. Depending on the structure of the individual ID tags (unique at only the beginning, end, or all), partial tag reads may or may not be assignable to individuals. Comparisons to hand-scoring of video feed will allow the authors to report estimate how much missing data there is (as analyses reported consist of the subset of the reliable data after dropping conflicting signals. In one note they say that <1% of mice are read as far apart enough that they missed two antennas in a row, however this under-reports the frequency of error. There can be error with no discrepancy in the order of signals detected if, and mice can be missed while moving between adjacent chambers or staying for a long period of time in a single chamber where their entry and exit were both misread. A second method of scoring would put time values to this error (amount or% of time misclassified) as opposed to just frequency of signals being dropped from analysis.

3) This system could potentially provide the ability to do a tremendous amount with individual data, if this is supported in the analysis package. If this is supported (i.e. provided the pair-wise social behavior data in the manuscript were generated by the analysis package), the authors should discuss this potential. For example, a sub-group of cohoused mice could be treated and a subgroup could be untreated, and differences could be assessed within a single testing session. The heat maps of mouse pair interactions could be used to identify more and less social individual mice which could be useful for comparisons to other measures (for example individual differences in specific genes, neural markers, etc.). And presuming other small rodents like prairie or meadow voles could be tested in such an apparatus, stable affiliations could be examined between mates or same-sex peers. This represents an exciting advantage of this kind of tracking system that is currently overlooked in this presentation.

Reviewer #2 (Additional data files and statistical comments):

In my comments above I ask for the authors to share validation data with the results of two methods of scoring the same data. I would hope these have already been collected in the course of validating the hardware and software. It is painstaking work to validate 12 mice visually, but it needs to be done at least once for me to have any confidence in the output. I have seen multiple iterations of other similar testing systems have major flaws in the output that were not caught until such validation was performed.

Reviewer #3:

The authors propose a set-up to study social behavior in mice. The setup proposed is of a complexity between very simple standard tests and more complex RFID arenas. This intermediate level of complexity has the advantage of being much cheaper than full-area RFID arenas and the authors argue that the simplified arena is ethologically relevant.

While the authors compare their setup with simpler arenas, they don’t make a comparison with more complex arenas (Kimchi Lab). To know whether this simplified arena captures the necessary elements, it would seem necessary to compare against these full-area setups.

Perhaps one of the more relevant points is about reproducibility, but I see no discussion of the data apparently used to demonstrate it in Figure 5. What does it count as high reproducibility? Why the data would correspond to that standard? What are the bars in the graph?

The authors justify RFID approaches saying then video-based approaches have the problem of how to deal with shadows and corridors. For a fairer discussion, maybe the authors can (a) discuss how bad the problem really is (giving refs to new developments in this line) and (b) also discuss problems with RFID (more invasive than video?) and (c) try to discuss limitations of their proposed setup (cannot find in different lines how afraid to open spaces they are?).

Reviewer #4:

The paper entitled "Eco-HAB – fully automated and ecologically relevant assessment of social impairments in mouse models of autism" describes an innovative set-up to assess mouse social behavior in an automated way, without human intervention. Mouse sociability is assessed within the housing environment, that is, an arrangement of housing boxes connected by corridor tubes. Mice are tracked and localized using RFID technology. The data collected are used to estimate the amount of time each mouse spend within each box, with or without her conspecifics, and also to measure their interest for social odor cues in comparison with non-social odor cues. The authors challenged their system by testing several mouse models of autism. This new system should allow researchers to detect similar social impairments in different mouse models as the classic 3-chambered test. For example, mouse social interest could be analyzed in low-stress conditions. This could also spare time and avoid many confounding factors (such as experimenter biases, housing conditions, habituation to the test apparatus) and while this concept is of high interest for the community (replication is indeed a major issue in the field), I have several comments on this current version of the Eco-HAB.

First, this setting and the analyses conducted on the data are reduced to a very basic "social interaction" level. The social interaction is described as the time spent in which box with whom. This is disappointing given the high potential of the method to generate more precise data (e.g., sub-group formation: is it possible to quantify the number of individuals in the subgroup and how stable in time the subgroups are?). In addition, the supposition that a mouse spends time with another one when they are located in the same case is not clearly shown. The correction of the time spent with another mouse (by subtracting the supposed spontaneous (non-social) exploration to the time spent in the compartment) is not convincing. It would need further analyses and a validation. Indeed, on a few video samples, it might be possible to compare the manual scoring of time spent with another mouse to the amount of time calculated through the method presented. This would allow the authors to check the accuracy of the calculation. The non-social stimuli used in Eco-HAB might also be more elaborated. For instance, the authors use bedding with sent vs. fresh bedding as a test for social vs. non-social stimuli. To align with the 3-chambered test paradigm, for the non-social condition, the authors could use bedding + non-social odor such as lemon or bedding + inanimate object.

Second, the novelty of the system is not clear to me. The authors quoted a previous article by Weissbrod et al. published in Nature Communication entitled "Automated long-term tracking and social behavioral phenotyping of animal colonies within a semi-natural environment". The paper also describes a tracking via RFID and social interaction matrices. It would be important to compare the two systems and explicitly show why Eco-HAB is different or better. The authors should also include a table indicating the accuracy of the video-RFID-tracking system performance in their system (as Table1 in the Weissbrod paper).

Third, I don't think that "low cost custom system" and "reproducibility" is very relevant here. If the authors want to argue for the reproducibility of the results obtained with this system, it would be appropriate to indicate the results from the same measurements using different cohorts. Currently, the data of the different replications appeared to be pooled. In addition, reproducing the setup is relatively complex and expertise in electronics is mandatory to reproduce the system.

In summary, the authors did not convince the reviewer of the usefulness of this current version of Eco-HAB. However, if they present additional measures that can be made with Eco-HAB (and not with previous behavioral tests using RFID), the system could be of interest to increase reproducibility in the field of mouse behavior.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Eco-HAB as a fully automated and ecologically relevant assessment of social impairments in mouse models of autism" for consideration by eLife. Your article has been favorably evaluated by a Senior Editor and two reviewers, one of whom, Peggy Mason (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in the review of your submission has agreed to reveal their identity: Gonzalo de Polavieja (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This is a great revision. The remaining concerns are very specific and are listed below. Please take a look and revise accordingly. We look forward to seeing your revision.

Reviewer #1:

This is an important methodological advance in the field of rodent social behavior and neuroscience. The revised manuscript has addressed many of the concerns raised by the initial review. Of great importance, it is clear that the system is open source and this manuscript is a contribution and not an advertisement. Additional detail concerning reproducibility has been added.

Minor to moderate concerns are:

Please put open source into the Abstract and keywords and possibly also the summary.

Figure 1—figure supplement 2 – the legend is not helpful. What is being graphed on the y axis? It would appear to be crossings but that is not said in the legend. And how were the manual crossings measured – with red light? Most importantly, why is the interpretation that the RFID measurement is superior to the manual scoring? This graph shows a difference, a consistent one. But it is unclear to me which of the two is more accurate. Finally, this does not truly address the 3rd concern of the 4th reviewer which is admittedly a bit vague. But the gist of the concern is: how does the reader know that the two mice are "spending time together" when they both occupy the same box? I think this questions whether two mice in one box could be at opposite ends and facing away from each other and yet be counted as socially affiliating. Clearly a formal possibility. Do the authors have any data relevant to this concern?

The sentence “Even though, in the present form, our system does not allow for the recognition of particular littermate-related behaviors, results show that both Eco-HAB measures-in-cohort sociability and scent-based social approach allow for drawing similar conclusions” is not understandable to me.

The Discussion is short. Some text in the Results should be in the Discussion (e.g. subsection “Eco-HAB – ethologically relevant testing of social behaviors”, last two paragraphs; subsection “Eco-HAB measurement is unbiased by social hierarchy and allows for long-term monitoring of social behavior”, last paragraph). Several of the comments in the response to reviewers would also be useful to include. The manuscript is concise but to a fault. Hold the reader's hand a bit more and help them to understand what you know so well after working on this for years.

Figure 5. The original is in original form I believe and still does not speak to reproducibility as do Figure 5—figure supplements 1-3. The supplemental figures are very useful and should be the main figure. I do not know what Figure 5 shows in its present form. Here is a suggestion. Make different symbols for the two cohorts in each condition (wt vs. fmr1 and via vs. control). Then line them up from highest to lowest. As it is the individuals are ordered along the x axis by mouse number or some other arbitrary/meaningless parameter. This simply does not show replication. If anything it is a messy version of a scatter or box plot of the data showing variability and range.

What are the ovals in Figure 5—figure supplement 3? The dots are averages from the two days of testing?

Reviewer #2:

Most of the concerns I had have been appropriately address in the new version of the manuscript. Now it is clear that software and data are open. It is also more clear the comparison with other methods and how this setup is more reliable than others and that levels of stress are lower than in 3-chamber setups.

The comparison with standard 3-chamber setups is, in summary, quite deep. However, the comparison with open arenas (Weissbrod, 2103) is only verbal. The authors say that in open arenas animals have territorial fights, as recognized in Weissbrod 2013. However, I see no comparison now between the number of fights or stress levels in the present setup vs. Weissbrod 2013. The reader is left to assume that, because the setup is inspired in ethologically relevant behavior, it must obviously be true that there is less aggression. In the most beautiful scenario, we would have the wild, open arena and present setup measurements of aggressive encounters. In the next level at least a comparison between open arenas and this set-up. But, to avoid doing new experiments, I think the minimum would be to re-analize the data to measure aggression. Video data was acquired, so it should most probably be possible to analyze this data for aggression encounters.
