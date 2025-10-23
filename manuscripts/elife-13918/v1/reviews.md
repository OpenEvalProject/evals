# Peer review - Round 1

Editors:
- Jeremy Nathans, Johns Hopkins University School of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.13918.027](https://doi.org/10.7554/eLife.13918.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your manuscript "A robust activity marking (RAM) system for exploring neuronal activity" as a Tools and Resources article to eLife. Three experts reviewed your manuscript, and the evaluation was overseen by Jeremy Nathans as the Reviewing Editor and a Senior Editor. Their assessments, together with my own, form the basis of this letter. As you will see, all of the reviewers were impressed with the importance and novelty of your work.

I am including the three reviews (lightly edited) at the end of this letter, as there are a variety of specific and useful suggestions in them. One point, in particular, that we noted is the limited overlap of PRAM with Fos or Npas4. This needs to be explained.

As you will see, all of the reviewers were impressed with the importance and novelty of your work.

Reviewer #1:

Manuscript 13918 by Sørensen et al. describes a new method to identify active neurons in vivo and to conditionally express transgenes. The method appears robust and adaptable to many uses. In my opinion the work presents an important advance and is suitable for publication in eLife.

The manuscript begins with a generalizable method to identify candidate cis elements and focuses on binding sites for Npas4 and AP-1. They go on to demonstrate the robust inducibility and low basal in depolarized cultured neurons and then in vivo in response to context fear conditioning and kainic acid induced seizure. This looks to be superior to previous methods and so represents an important advance. I was surprised that there is a relatively small difference in Figure 4 between A-A and A-B. This may make people worry that it is not really identifying behaviorally linked networks. I wonder why the authors did not look at CA1 neurons in a place field paradigm where the percentage of active neurons and network specificity is well established. Might the threshold activity required to induce the system be relatively high compared to Arc for example. If so, this should be mentioned in the manuscript. The strategy to confer Cre dependence presented in Figure 5 is very nice. Did you ever see expression in parvalbumin neurons? Comment?

I would have liked to see a panel in Figure 2D looking at dentate 48 hrs after removal of Dox but without kainic acid.

Figure 4 could benefit from a schematic showing the injection site.

Data in Figure 3—figure supplement 3 is very nice showing optogenetic control and might be substituted for panels E-G.

The statistical analysis and data provided appear appropriate.

Reviewer #2:

Sørensen and colleagues have built a synthetic promoter (PRAM) toolkit that reports neuronal activation. Such a promoter can, in principle, be utilized in different ways to mark and manipulate a target neuronal population. The authors provide two such examples: incorporating PRAM with a destabilized tTA in a tet-off system into a single AAV vector that can be used in vertebrate brains and using PRAM to drive reporter expression in a Gal4 and Flp dependent manner in D. melanogaster. I think this system is likely to be widely used, and I am supportive of publication in eLife. In general the experiments are elegantly designed and executed, but I have a few concerns relating to the sensitivity and specificity of labeling of active neurons.

1) The authors make strong claims about the superior sensitivity of their system compared to previous approaches. These may well be true, but it would nice to know how sensitive their system is in terms of detecting changes in neuronal activation. For example, what is the minimal percent increase in firing from baseline that is reliably reported by PRAM ? A measure of sensitivity would also provide estimates of how much noisy fluctuations in firing will elicit PRAM driven transcriptional activity. At the very least this should be discussed. The authors could also potentially test this in their primary neuronal cultures (Figure 1), ideally with channelrhodopsin mediated control of firing. Alternatively, rather than just testing PRAM activity with 35mM KCl for 6 hours, a time course (say 2 and 4 hours) and a dose response to KCl would be informative. In these studies, it would be valuable to perform immunolabeling for c-Fos in parallel to compare this new approach to one that is familiar to most neuroscientists.

2) Some controls appear to be missing for the in vivo studies relating to kainic acid induced seizures (Figure 2) and contextual or tone conditioning (Figures 3, 5). How many neurons express the reporter 24 hours following:saline rather than kainic acid injection;placement in the contextual testing chamber without being shocked;hearing the tone in the testing chamber without being shocked?

These controls will reveal how likely the neurons under consideration express reporter without the experimental manipulation being tested.

3) I really appreciate the authors' extending their validation of reporter induction to multiple brain regions and Glu and Gabaergic neurons. However, the number of reporter+ neurons is comparable between home cage and contextual conditioning paradigms (Figure 5—figure supplement 1A-C), so it's unclear whether reporter expression in Gabaergic Sst+ neurons (panel d) represents reporter induction in response to conditioning or basal expression seen in control home cage conditions.

As far as I can tell, there is no control for the aggressive social interaction test of reporter induction in the prefrontal cortex (Figure 5—figure supplement 1G-H). What is the level of basal reporter expression in the home cage in prefrontal cortex? A comparison between the control and aggression conditions would reveal whether there is reporter induction in the Gabaergic neurons in this region.

1) Please provide a schematic of the experimental setup for the in vivo CRAM studies in Figure 5.

2) Clarify what "% overlap" means as the y-axis label in Figure 4G, H.

3) The first paragraph of the subsection “Application of the RAM System to Other Species” needs to be corrected; AAV-RAM was tested in rats and PRAM was tested in flies.

4) In the second paragraph of the subsection “Application of the RAM System to Other Species”: cite study showing PFC projection to dorsal striatum.

5) Correct discrepancy between Methods and Supplementary Figure legend: was the social interaction/aggression test done for 5 or 10 min?

6) The authors will be depositing the basic AAV-RAM vector with Addgene. I also encourage them to deposit the CRAM version of the vector and other plasmids described here, including the ones for flies (but see below).

7) Frankly, the fly data seem a bit rushed. For example, do we even know whether luciferase expression is even restricted to the nervous system? I would suggest that the authors hold on to the fly data and submit it as a more complete, separate story.

Reviewer #3:

This manuscript by Sørensen et al. reports extensive characterization of a new tool for marking and manipulating neurons based on immediate early gene expression. This tool has the potential to be an important new addition to the arsenal for defining and manipulating cell populations based on neuron activity changes. They developed the RAM promoter, which gives improved signal to noise over past IEG systems and also is compact enough to fit easily inside an AAV vector. This promoter can be used to drive fluorescent proteins and optogenetic neuronal actuators. They go on to demonstrate the application of this tool in mice in a seizure model, contextual fear conditioning, auditory conditioning as well as other models in rat and fly. In addition, a Cre-dependent variant on the tool is described.

The tool depends on the tetOff tTA system, and doxycycline is administered to reduce background expression after viral expression and prior to the experiment. However, there is some ambiguity here because in the rat model, the dox was excluded and low background was apparently maintained. The use of dox appears to be important for the use of this tool, but the necessity of this component needs to be more explicitly expanded upon so that a future user is well-positioned to understand its importance. In addition, further explanation is required for the modest colocalization of Fos (note Fos, not c-Fos, is the MGI protein abbreviation) with mKate2 in Figure 4 for the A-A conditions (only about 20%). Although this colocalization is significantly greater than the context A-B, there is no explanation why the colocalization is not higher. Because the expectation is that expression off of this promoter reflects IEG expression in neurons, this discrepancy is especially concerning as it is an essential aspect for application of this tool. Further examination or explanation of this issue is required.
