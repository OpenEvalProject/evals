# Peer review - Round 1

Editors:
- Timothy Verstynen, Carnegie Mellon University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40766.027](https://doi.org/10.7554/eLife.40766.027)

In the interests of transparency, eLife includes the editorial decision letter, peer reviews, and accompanying author responses.

[Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that minor issues remain unresolved.]

Thank you for submitting your article "An afferent white matter pathway from the pulvinar to the amygdala facilitates fear recognition" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Timothy Verstynen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have also agreed to reveal their identity: Jean Vettel (Reviewer #2); Marco Tamietto (Reviewer #3).

The Reviewing Editor has highlighted the concerns that require revision and/or responses, and we have included the separate reviews below for your consideration. If you have any questions, please do not hesitate to contact us.

As you can see from the reviews below, all three reviewers were very positive about this work and supportive of it being published. The analysis was smart, rigorous, and clearly theoretically motivated. The links to previous work were strong and yet the results were also clearly novel, making the work both incremental and novel (not an easy feat to pull off).

Separate reviews (please respond to each point):

Reviewer #1:

This article by McFayden and colleagues reports a beautiful set of multimodal analyses, using the HCP sample, to explore the existence of a subcortical route to the amygdala from the colliculus, via the pulvinar nucleus of the thalamus. Using dMRI, the authors identify plausible white matter pathways that connect 1) the amygdala to the pulvinar, and 2) the pulvinar to the superior colliculus. They then show that, behaviorally, the degree of estimated white matter connectivity between the amygdala and pulvinar predicted individual differences in recognition of fearful faces in the Penn Recognition Test. Using the dMRI structural connectivity information, they then use DCM on fMRI data from the Faces task to evaluate a set of models for information flow along both cortical and subcortical pathways. The winning model, which substantially out performs the other models, includes both a direct and indirect route to the pulvinar that relays information to the amygdala. Finally, the authors show that the degree of effective network connectivity from the DCM analysis correlated with the degree of structural connectivity analysis.

All in all, I thought this was a phenomenal study. First and foremost, I thought this was a very strong theoretically motivated paper. In an era of exploratory data analysis on structural and functional imaging data, it is refreshing to see such a tightly motivated theoretical paper. The multimodal analysis was well executed and the results were clear.

I do have some suggestions for improving the paper.

1) The authors are essentially making a mediation argument without directly stating it: i.e., white matter connectivity mediates a link between effective functional connectivity of the network and behavioral performance in the Penn Recognition Task. But the analysis ends without evaluating a formal mediation statistical analyses (e.g., Preacher and Hayes, 2008). Showing that white matter connectivity statistically mediates an indirect pathway between effective network connectivity and behavior would provide a powerful direct test of the links the authors are alluding to in the paper.

2) Since all of the results here are cross-sectional, the authors fail to account for a critical confound measure that can impact both dMRI and fMRI associations: head motion. The authors report that they include "head motion" as a regressor in the fMRI analyses, but do not describe what terms were used (see Bright et al,. 2017, Cleaning up the fMRI time series: Mitigating noise with advanced acquisition and correction strategies. NeuroImage, 154, 1-3.). In addition, no such control was applied to the associations with the dMRI connectivity (see Baum et al., 2018). The impact of in-scanner head motion on structural connectivity derived from diffusion MRI. Neuroimage, 173, 275-286.). This should be controlled for before making inferences about the between-subject associations.

3) The spatial resolution of the analysis, particularly the tractography analysis, seems underwhelming. For example, in Figure 1 it looks as if the authors are using a full thalamus ROI (although in Figure 6, it appears that they are using a selective pulvinar ROI). Are we sure these tracts are ending in the pulvinar? Also, where in the amygdala are the fibers terminating (and does this match previous neuroanatomy studies)?

4) Along the same lines as my previous point, there isn't much match to previous known neuroanatomy of white matter pathways. Do the paths of the PUL-AMG and SC-PUL connections follow specific white matter fascicles? If so, which fascicles and do the trajectories make sense based on anatomical tracing studies?

5) I am a little confused as to why the authors restricted the DCM analyses to the subset of 237 subjects that had significant within-subject first level GLM maps. In the Materials and methods, the authors report that the use of the subsample doesn't impact the results (third paragraph of subsection “Dynamic causal modelling”). Why was the sub-sampling done? What does it buy you?

6) The structural connectivity and behavior correlations (Figure 2) are all significant with the local tractography dMRI results. However, the effective connectivity and structural connectivity correlation (Figure 6) is significant with the global tractography results. The inconsistency in white matter connectivity measures in the associations is puzzling and somewhat worrisome that some of these correlations may be spurious.

7) In the DCM analysis, it seems that the null hypothesis is that there is not a meaningful subcortical route (either input-to-pulvinar or input-to-superior colliculus) that indirectly conveys information to the amygdala. But it doesn't appear that such a model was tested. Not that I expect this to be particularly problematic given how robust the model selection results are (Figure 4B). It just seems that this model is the most straight forward.

8) This paper uses pretty standard associative tests for the key results. However, given the large sample size, it should be possible to use cross-validation to assess whether variability along one dimension (e.g., structural connectivity) predicts another dimension (e.g., Penn Recognition Test scores). Hold out set prediction accuracy is more informative than simple association tests and should be used as often as possible.

Minor Comments:

– Introduction section, third paragraph: Given how many studies use the HCP data set, this isn't necessarily an "unprecedentedly large" sample.

– Introduction section and elsewhere: The authors repeatedly use the term "neural activity". But they are measuring hemodynamic activity.

– Subsection “Greater fibre density predicts better fearful face perception” and elsewhere: Please show all the statistical results, not just those that emerged as passing the significance threshold. The information on the effect sizes of all analyses are very meaningful, even if the results don't pass the null hypothesis test.

– Subsection “A forwards-only subcortical route is engaged during face processing” vs subsection “Greater fibre density relates to stronger effective connectivity”: Why are you using different outlier tests for different analyses? You should be consistent in your outlier test method.

Reviewer #2:

In the paper submitted by McFadyen and colleagues, the research examines the existence of a direct subcortical pathway for detection of fear from visual input. This question is strongly motivated from (1) animal models that have inspired a search for a human homolog, (2) lesion data from humans who can see affective stimuli without an intact V1, and (3) a rich review of research that has identified suggestive evidence of portions of the subcortical pathway but nothing cohesive to rule out alternatives.

The core strength of the work arose from exploiting the HCP dataset as a resource developed to enable a first pass big data approach, and then combining this large sample with a multimodal technical approach to examine structure (two methods), behavior (out of scanner task), and function (functional localizer and then directed connectivity modeled with 120 models). A noteworthy decision was the data-driven selection of functional regions from the face-shape task. The analytic flow is clearly communicated, results well illustrated and described, and the core interpretations largely justified.

The short list of suggestions for improvement include:

1) The description of the parameters for the DCM modeling is much too sparse to really understand or intuit the core features of the data variability and how it would have influenced performance of the 120 models. Suggest expanding details in the “Dynamic causal modelling “subsection of the main and then add more in the supplement.

2) Related, the text describing the above-threshold participants for the model was confusing (main subsection “Dynamic causal modelling”). The lines list the lowest number of above-threshold participants as 69 and 58 and then 4 and 3, yet the text states that all 237 participants had above-threshold in all ROIs. Why wouldn't 237 + [69 or 58 or 4 or 3] be the lowest number? The intuition of what is being communicated here about the HCP sample must be incorrect on my end, but alternative guesses have not panned out either.

3) Great job checking the difference between the 237 and 385 participants for all of the features listed in subsection “Dynamic causal modelling”, but can some simple stats be added to describe the quantitative element of this. Reveal anything trending?

4) Across all of the tests in the paper, was there any family-wise error applied to cover the sheer volume of comparisons?

5) It would be interesting to know whether the structural connections among the functional regions from the shape task (FG and IOG) could also account for differential performance on the face task. While this is not critical for the specific focus of this paper on subcortical fear pathway, it could augment our understanding about whether the subcortical fear pathway provides a unique avenue for fear response or if it more redundant with the canonical regions involved in face processing.

Minor Comments:

1) The description of the behavioral task could be easier to discern by just stating, "To this end, we examined behavioral data from an out-of-scanner task, the Penn Emotion Recognition Task, that assessed a different component of face processing than the in-scanner task."

2) Throughout the paper, there are a few instances of missing spaces between words and a parentheses and a missing period in subsection “Regions of Interest”.

3) The Results section employs suggestive language (“likely present” –) while the Discussion is very strongly worded (“unequivocally supports” –; “study settles” –). Any chance for softening since all findings are at the limit of our current methods, so softening and adding some text about methodological considerations would strengthen the paper's ability to impact future work.

Additional data files and statistical comments:

Additional document was clear and all is stated to be on GitHub.

Reviewer #3:

The paper by McFadyen and colleagues deals with an extremely relevant and hotly debated topic in neuroscience; namely, the anatomical existence, functional significance and behavioral impact of a subcortical direct pathway to human amygdala for fear perception.

Although there were previous empirical data and theoretical accounts in humans and non-human models supporting this contention, the present study presents several important advancements that, IMHO, deserve attention and publication in eLife.

Briefly, the present study marks a seminal departure from previous investigations that adopted a unimodal approach to focus either on anatomical or functional aspects only, and typically used small samples. Here data from HCP about more than 600 subjects are analyzed with state-of-the-art neuroimaging techniques. Evidence of anatomical existence of fiber tracts connecting SC, PULV and AMG are gathered using in-vivo tractography using both global tractography as well as more traditional ROI-based streamline probabilistic analysis. Noteworthy, results not only indicate that such connections can be reconstructed in a large sample, but also that the part of the PUVL involved is the inferior-lateral (i.e., visual) part of the PULV, as previously found in small samples of human and non-human primates. Next, the behavioral relevance of this pathway is demonstrated, correlating fiber density in these tracts with fear recognition. Then, the functional role and directionality is evaluated with DCM on fMRI data. Results show that the best model incorporates both cortical AND subcortical pathway to the AMG, and that the directionality of the latter is feedforward from SC and PULV to AMG. Finally, greater fiber density is related positively to effective connectivity in this subcortical pathway, therefore supporting further the link between its anatomical and functional properties.

I only have very minor comments ("minimal", I would say), to a paper already excellent.

Minor Comments:

I have only very minimal comments and suggestions that I would like the authors to take into consideration.

First, it is interesting to note that across the different analyses there is a common trend about lateralization on this subcortical pathway in the right hemisphere. Originally, laterality in fMRI response in the amygdala and subcortical structures to masked facial expressions was reported in Morris et al., 1998 Nature and interpreted as supporting the role of the right hemisphere in non-conscious emotion perception. Anatomically, a similar trend in DTI data was reported in Tamietto et al., 2012 that, however, did not reach standard statistical threshold. I would invite the authors to comment a bit more on this laterality effectin relation to previous works and neuropsychological evidence.

Second, there is recent and converting evidence in patients with V1 damage and "affective blindsight" that this subcortical pathway seems tuned to process low-spatial frequency information (e.g., for a recent paper Burra et al., 2018). Evidence in healthy participants seems more controversial, with some findings supporting a similar specialization for low spatial frequencies (e.g., Méndez-Bertolo et al., 2016, Carretié et al., 2017 JoCN), and other data, eminently from the same authors purporting a more "generalized" role (McFadyen et al., 2017). Possibly, some further speculation and more explicit reference to this topic would be of interest in the light of the new data.

Third, one strong hypothesis verified in non-human models is that the subcortical route to the AMG is composed by a functionally integrated disynaptic pathway whereby the superficial layers of the SC project to infero-later PULV and the same neurons in the PULV then send efferents to the lateral AMG (a summary of evidence about different subcortical or non-canonical pathway to the amygdala in humans and non human animals can be found in Diano et al., 2017 Front Psychol). In an attempt to provide indirect evidence in humans, some previous tractography studies, after tracing fiber connection between SC and PULV, and between PULV and AMG, also tried to verify whether a subsample of these reconstructed fibers could be considered as belonging to the same streamlines. If I am not missing something, the present analyses do not investigate this aspect. It would be nice to have this info if possible. I acknowledge the paper is already methodologically rich, so I am not explicitly asking additional analysis, even though this should not be particularly long to perform. However, mentioning to this aspect for future development would be appropriate.

There is a factual error in the Introduction section where authors say about Tamietto et al., 2012 paper that "The white matter structure of the subcortical route was estimated for the patient and for six healthy, age-matched controls". In fact, the healthy controls analyzed were 10, not 6.
