# Peer review - Round 1

Editors:
- Jody C Culham, University of Western Ontario , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.13420.021](https://doi.org/10.7554/eLife.13420.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "A synergy-based control is encoded in human motor cortical areas" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Jody Culham as Reviewing Editor and Timothy Behrens as the Senior Editor. Our decision has been reached after consultation between the reviewers.

The following individuals involved in the review of your submission have agreed to reveal their identity: Joern Diedrichsen and Jason Gallivan (reviewers).

Based on these discussions and the individual reviews below, we regret to inform you that we are rejecting the manuscript. As it stands, the manuscript would require substantial revisions, including new data and analyses, to address reservations raised by the reviewers, particularly Reviewer #1. All three reviewers (like the editors in the initial evaluation) saw potential in the approach but their enthusiasm was tempered by a number of concerns. In post-review discussions, even Reviewers #2 and #3, who were largely positive, agreed that the manuscript should not be published unless the major concerns detailed below are addressed. Normally eLife tries to avoid making authors go through a gauntlet of revisions if a positive final outcome is uncertain. As such, we are rejecting the current manuscript.

That said, we would be willing to consider a new manuscript that unequivocally addresses the concerns raised. In this case, we would aim to recruit the same reviewers. We must emphasize that, as with any new manuscript, there is no guarantee of publication, especially if you do not make the required changes or the new analyses do not support the conclusions. As such, you may decide instead to submit your manuscript to another journal, in which case we hope the reviewers' comments are helpful.

To be considered for publication in eLife, the following changes would be essential (based on the specific reviewer comments detailed below):

1) The authors would need to test their synergy model against a more plausible "muscle model" based on better EMG recordings of more muscles (Reviewer #1, Point #1; though the other two reviewers were in close agreement during post-review discussion). Though the possibility of removing the muscle model from the paper was discussed, the consensus was that this would reduce the impact of the paper.

2) There was a clear consensus among all three reviewers and reviewing editor that the interpretation of principal components and their mapping needs to be unpacked better. One concern is that without any insight as to what the principal components represent, the demonstration that they show a topography is of limited value (Reviewer #2, first point). A second concern is whether the topography really reflects those components or would equally reflect components in other rotated versions of the space (Reviewer #1, Point #3). There may be some potential with the PCA data ameliorate some concerns at the initial review stage and from Reviewer #1 about whether the paper provides a sufficient advance beyond Ejaz et al. (2015). While Ejaz et al. limited their analyses to M1 and S1, the present manuscript shows potentially interesting patterns in other parietal and frontal regions. However, as it stands, the patterns and interpretation so vague that they do not provide any real insight into regional differences.

3) The authors need to clarify their discussion of their PCA-based methods against the RSA based method (as used both in their paper and in Ejaz et al. – see Reviewer #2's comment on RSA and Reviewer #1, Comment #2).

In addition, if the authors choose to resubmit the manuscript in a new form to eLife, the other comments of the reviewers should be addressed. In post review discussion, all reviewers agreed with the suggestion that noise ceilings should be reported.

Reviewer #1:

The study "A synergy-based control is encoded in human motor cortical areas" provides an investigation of the MRI patterns associated with the execution of grasp-like hand shapes. The main finding is that the activity patterns of two left –out postures can be better discriminated when using 5 regressors extracted from kinematic synergies than 5 regressors reflecting the unsigned displacement of individual fingers or 5 regressors picked from features of EMG recording of 5 different hand muscles. The conclusion of the study are largely overlapping with that of an earlier paper from our lab (Ejaz et al., 2015), but the study adds a number of interesting extra aspects to this line of work, including testing the generalisation of the model to new postures and the investigation of the spatial arrangement of these synergies onto the cortical sheet (but see point 3). The current version of the paper, however, has a number of weaknesses that certainly would need addressing.

1) The alternative models (individual fingers and muscle) give the appearance of straw men. The individual finger uses the L1 norm of movement of each finger – so in contrast to the kinematic synergy model, it does not distinguish between finger flexion and finger extension. This decision appears to be somewhat arbitrary. So, it leaves the reader with the question of whether there is something special about taking the absolute value, or about the specific rotation of these 5 factors in representational space. A more convincing line of investigation would be to try to use optimisation to rotated the 5 linear factors in the kinematic space as to get the best possible decoding performance, and then test the closeness of this solution with the one provided by the kinematic synergy model.

Matters are worse with the muscle model. The authors recorded 5 muscles only, despite the fact that in our experience it is feasible to get 14 or more distinct signals from hand muscles from surface electrodes (Ejaz et al., 2015). These may not always reflect individual muscles, but that is hardly important if we only want to obtain a representative picture of the space of muscle activity. The extracted features from the EMG signals appear obscure to me; and ultimately, the ability to distinguish between postures based on this data is very bad, indicating that most of these numbers reflect noise. Given these large a-priori differences in the quality of the models, I think any subsequent difference in how well fMRI activity patterns can be predicted become utterly unconvincing. So I think the authors need to work harder on trying to equate the reliability of their models (for a possible method, see Ejaz et al. (2015), supplementary methods).

2) While I think that some of the techniques used in the paper are interesting and promising, I believe that they are currently not going beyond the RSA analysis presented in Ejaz et al. Unfortunately, in the discussion the authors misconstrue the previous evidence and perpetuate some misunderstandings that are all too common in the synergy field. For example the authors state that "these findings, however, provide no clue regarding the extent to which the brain may control the hand using functional modules" and "their model (hand usage model) was therefore similar to the individual digit model adopted in the present study", showing that they clearly do not appreciate the tight connection between RSA and the methods chosen here.

It is important to point out that the matrix of pairwise distances contains the same information as the covariance matrix between experimental conditions (and can easily be transformed into it). Extracting PCA factors from this covariance matrix provides a distribution of the same statistical quantity, only that it throws away a certain proportion of the information (and by just considering the principle vectors also disregards the relative importance of the factors). Therefore RSA and extraction of principal components from the covariance reflect highly related information – and I do not think that the authors have made any convincing case that anything can be learned from the PCA approach that cannot be learned from looking at the whole space. This boils down to the key question in the synergy field of whether there is something special about the principal vectors (or synergies) themselves, or just about the representational space they describe. With the current evidence, the difference between this paper and Ejaz et al. is purely superficial and methodological, but not conceptual.

Similarly, our hand use model is not equivalent to the individual finger model used in this paper, but is much closer to the kinematic synergy model (we present a single-finger model in the multi-finger experiment, which is much inferior to the natural statistics model). The authors choose to extract synergies by taking 20 postures that serve as ad-hoc samples of the natural statistics of movement. In our paper we chose to use data sets that are representative samples of the natural statistics of movement. Furthermore, we use the whole covariance matrix of the data to compare to the brain activity patterns, not just the first 5 factors.

Indeed, in the analysis of the multi-finger experiment in that paper, we started with very similar methods employed by the authors here, but ultimately decided to present only the RSA methods, as we believe that they show the main point of the similarity of representational space more concisely, than the extraction of some arbitrary number of main factors, which then serve as descriptors of the same space.

3) The mapping of synergies on the cortical sheet is an interesting addition and provides a real potential argument that the kinematic synergies are more that statistical descriptors of representation space, but that the factors themselves have special status. The problem, however, is that currently the one single mapping is not evaluated against many other possible mappings. Thus the authors have not shown that there is something special about the synergies extracted. For this, one would need to a) develop a measure of the "topological orderliness" of the mapping and b) compare the synergy map systematically against an exhaustive set of alternative rotations in the same space (again using optimisation). We actually attempted this analysis on our multi-finger experiment, but preliminary results were not terribly encouraging, as there seem to be rotations of these factors in the same rotational space which gave similarly orderly mappings. If the authors could show in a stringent and convincing fashion that the particular rotation chosen here is more orderly organised than any other possible rotation in the 3-dimensional space (or even conclude after careful evaluation that this is not the case), I think the paper would really increase in quality. Without such analysis Figure 2 remains merely suggestive and anecdotal and the claims not substantiated.

Reviewer #2:

This is excellent work. The study is well thought-out and executed, the paper is clearly written and the analyses are rigorous and appear to have been conducted with care. I suspect that the experimental question asked and results obtained will be of general interest to the sensorimotor research community and the authors do a good job of integrating and motivating their study based on what is currently known.

While I do not have any significant concerns about the work, there are a few points, summarized below, that I think should be considered in a revision.

1) Given the data-driven nature of the analyses used, I found some interpretation of the top 3 principal components, and their relation to the topography noted, lacking. Ultimately the insight provided by PCA in neurophysiology rests on being able to directly link the components to neural activity. While I agree that there is some general map of the components in sensorimotor cortex, their organization has no interpretation. Some interpretation of the components (PCs 1-3) and how they relate to cortex organization might be informative on this front. Otherwise, simply saying PCs are mapped onto cortex is fairly impenetrable for the reader.

2) I found the intermixing of results material into the Discussion section a bit disruptive (e.g., inclusion of Figure 5 and visual control analyses). I think that results material should be described and motivated in the Results section.

3) It was unclear to me why, after measuring from five muscles, and thus obtaining five measures (i.e., the same number of components in the synergy and individual digit models), the data was reduced through PCA and then up-sampled again (through cross-validation methods) to achieve 5 components. This should be fully explained, as no such manipulation was done to the individual digit data.

4) It might be interesting in the supplement to show the results of RSA/MDS for the other models (EMG and individual digit), allowing the reader to make comparisons between all 3 models.

5) I was initially confused in the Discussion why the authors referred to brain areas that were not apparent in the group maps shown in Figure 1 (e.g., ventral premotor cortex). This became apparent, however, after I viewed the actual source data on the MNI-152 brain, as 2-3 subjects show overlap in some of these areas. In any case, the authors should only use the text to refer to what is actually shown in the paper, to avoid such confusion.

6) In the Discussion, I was hoping for some discussion of the bilaterality of the effects observed, which are interesting. I would suggest adding this in a revision.

7) In addition to the visual control used in the paper (i.e., analysis of visual stimulation evoked time points in the RSA mask), I was thinking that an equally good control to show the selectivity of effects to sensorimotor cortex would be to localize much of visual cortex (e.g., based on visual stimulation response vs. rest) and then perform the exact same encoding analyses on those voxels. Visual cortex is well known to be involved in imagery-a key component of the experimental task-and to see how the kinematic models performs in that area would be of interest. If it does fairly well, it would have some significant bearing on what is actually being measured in sensorimotor cortex as well as its underlying organization.

Reviewer #3:

This study investigates whether and to what extent kinematics or muscle synergies are represented in the human motor system during grasping toward virtual objects. To this aim, authors measured hand kinematics and electromiography (EMG) signals and used these information to create a kinematic synergy model, an individual-digit model and a muscle synergy model. By computing correlations between each of these models and brain activity during grasping of virtual objects, they found that the kinematic synergy model explained better the fMRI data than the other models in various motor areas. The authors concluded that the control of hand postures in the brain is based on kinematics synergies.

This study addressed a very interesting question in the motor control field by using the state of the art fMRI analyses and combining various measurements like kinematics, EMG and fMRI data. I find the results and the conclusions of this study highly relevant for the understanding of the motor control system and for the advance of neuroprosthetics.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "A synergy-based control is encoded in human motor cortical areas" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens (Senior editor), Reviewing editor Jody Culham, and by Joern Diedrichsen, one of the original reviewers.

The external reviewer has devoted a considerable amount of time to re-examining the revision and has had detailed conversations with the editors to make the point clear. We are now at the following position: Two of the original reviewers thought the manuscript was strong and we believe all of their concerns have been addressed. We also think the new manuscript is improved and remains of substantial interest but have several remaining concerns (see list below). Out of these concerns there is one point that is really essential and has a major impact on the interpretation of the study. Let us be clear, we think the manuscript is of interest and we intend to publish it, but we do not think that your current analyses support that claim that the synergies reflect actual cortical codes. The figure where you try to make this point (Figure 2) is not subjected to the correct tests to make this point (as you concede in your response to Reviewer 1, point 3 in your response).

eLife tries not to subject authors to endless rounds of revision, but we would like to give you one more opportunity to revise the paper to take into account the new comments. Essentially we are asking you to either (a) to perform a proper analysis which shows that the synergies do a better job of representing the cortical patterns than other rotations of the covariance space, or (b) to be clear in the manuscript that this claim is not supported and that the claim that you can support is that there covariance space as a whole is well-represented.

There is also confusion as to how to interpret the text around this critical analysis, which you describe is "Resistant" to rotations in the covariance space. It is clear that the analysis is not invariant to such rotations as described in point 11 below. When we read the text surrounding this description, we read the exact opposite interpretation from each other. One of us thought you were saying the R2 value was invariant to rotations and therefore resistant. Another thought you were saying that the R2value was NOT invariant, and therefore the overall analysis was resistant. The R2values change with rotations, and it is important that manuscript is clear about this. However, it is also clear that this point is not sufficient to demonstrate that the particular eignenvectors that you arrive at via the PCA are the ones that are encoded topologically in cortex. To make this point, you would need to compare them to other rotations of covariance space as described above, and in the previous review.

For clarity for a broad readership, if indeed you can show that the three principal components are better than other rotations, the Reviewing Editor thought that some of your wording in the reply to reviewers would be helpful to include in the manuscript itself ("However, a remarkable body of literature indicate that the highest-ranked kinematic PCs correspond to strictly coded grasping primitives (Santello et al., 1998; Gentner and Classen, 2006; Ingram et al., 2008; Thakur et al., 2008; Gentner et al., 2010; Overduin et al., 2012), see Santello et al., 2013 for review). […] In our study, we examined the first two PCs, which were highly consistent with the literature, along with a third one representing a movement of flexion and thumb opposition (as to grasp a dish or a platter)."

Reviewer #1:

Upon reading the revision, I think the authors have addressed some points raised in the original critique, whereas in other areas I found the response and the changes to the manuscript not satisfactory. This may be partly due to a strong philosophical difference regarding what synergies are and how to interpret the evidence – where I seem to fundamentally disagree with the authors. But I agree that the paper provides an interesting additional and alternative viewpoint to Ejaz et al. (2015) – so I do not want to stay in the way and would recommend publication after a number of clarifications and corrections have been made.

Overall I still found the methods and analysis presented in the paper still somewhat obscure and relatively hard to follow. In interest of clarity and transparency, I would therefore urge the authors to clarify the remaining points in the manuscript. It is the policy of eLife to not restrict length or supplimentary materials to allow the presentation of self-contained papers, and the authors should really try to be as clear as possible.

1) "Individual-digit model, based on a somatotopic criterion (Kirsch et al. 2014)" remains still as obscure as it was before. I urge you to clarify here in the Introduction. There is no notion of somatotopy in the individual-digit model as far as I can see. Somatotopy implies that it matters that the middle finger is closer to the ring than to the pinkie finger. The Individual-finger model treats all finger movements equally and independently – so it is not "somatotopic".

2) Results section, first paragraph: I found the analysis provided on the additional 4 subjects interesting and thank you for the additional clarification, but would ask you for two things: a) When using temporal averaging of the EMG signal (mean-based EMG analysis), you should use your dimensionality reduction to 5 PCA, as you did for the feature based analysis. This way we can clearly see that your temporal features, and not the dimensionality reduction provide the critical difference between the red and blue curve. Note also that you did not replicate exactly the analysis performed in Ejaz et al. (2011), as you skipped the critical prewhitening step. It is not clear whether this analysis would be sensible here, as your gestures are a ad-hoc sample from the natural statistics, not an equally-spaced sample of possible finger movements b) this analysis should be included as supplementary material and cited from the main text.

3) Supplementary file 15: I think the table should be supplemented by a one-sentence description for each feature that is detailed enough to be able to calculate these features without going onto a wild-goose chase in the cited papers. I urge the authors to start with a clear definition of symbols and then give a concise and unambiguous formula.

4) Section “A challenge to individual digit correction representations? The functional topography of hand synergies”: I find this section on functional topography overstated and do believe it requires a major change in tone. Your data shows that there is "some" topological organization of the first three synergies, not a "strict" one. Furthermore, some somatotopic clustering can also be shown for individual fingers or – most like for other rotations of the synergy vectors, and you have not provided a quantitative comparison with other possible organizations (see point 11).

5) Section “Limitations and methodological considerations”: The limitation section discusses relatively minor points. Two important weakness should be added: a) the point that while some clustered representation was shown in sensory-motor regions, you did not convincingly show that this specific set of synergies is more clustered than other rotation of the same vectors b) that in comparing the different models, the EMG-model had much less ability to discriminate different gestures and that the disadvantage of the muscle model may simply reflect noise levels on your measurement. These are important limitations that should be pointed out.

6) Paragraph two, “Models validation”: Please clarify in the text how the labels of the test set where shuffled. Specifically, if your test set contained 4 repetitions of each of the 20 gestures, did you shuffle the labels of all 80 trials completely randomly, or did you keep the 4 trials for the same gesture together and just give them together a new label (or equivalently shuffle the labels after averaging over the 4 trials)? This difference has important consequences for the variance of your reshuffling statistics.

7) “Every voxel had a score ranging from 0 (if the voxel was never used) to a possible maximum of 380 (if the two left-out patterns could be predicted, for that voxel, in all the 190 iterations).” Please explain this statement better. Do you mean to say the score was the number of times the voxel was included in the 1000 voxels AND got a specific gesture correct?

8) Section “Assessment of the accuracy of the encoding analysis”: Please clearly point out in the text that the weights were randomly shuffled within each column. Please also point out explicitly (I assume that this is true) that the new "PCA"s were now not orthogonal to each other anymore.

9) Now that I think that I understand what the single subject maps are, I think the group-level maps also needs some more explanation. The score for each voxel varied between 0 and 380 (as stated above). For each subject, which value was then considered as "successful"? Why was it called a "probability map"? Probability of what?

10) Section “Cortial mapping of the three group synergies”: I disagree that using R2 as a goodness of fit for each individual synergy makes the results invariant to rotations in synergy space. It does not. Maybe we fundamentally misunderstand each other, so I will make my point more concrete. Say, you have 2 "synergies" of 5 elements X1 and X2 and a 5-element data series Y.

x1=[-2 -1 0 1 2]';x2=[1 0 -2 0 1]';

Y=[-2 -2 1 2 2]';

Then the R2-values of each of the columns of X can be calculated as

R2_1 = Y'*x1*inv(x1'*x1)*x1'*Y/(Y'*Y) = 0.847

R2_2 = Y'*x2*inv(x2'*x2)*x2'*Y/(Y'*Y) = 0.039

Now I rotate

R=[cos(0.9) sin(0.9);-sin(0.9) cos(0.9)];

Z=[x1 x2]*R;z1 = Z(:,1);z2 = Z(:,2);

Now the individual R2-values are changed, and hence a mapwise evaluation criterion would also be changed.

R2_1 = Y'*z1*inv(z1'*z1)*z1'*Y/(Y'*Y) = 0.6351

R2_2 = Y'*z2*inv(z2'*z2)*z2'*Y/(Y'*Y) = 0.4629

I hope that clarifies my point and why I think a) the sentence stating that individual R2 values are rotation invariant should be removed and b) any claims regarding a special organisation on the cortex should be made weaker – for stronger claims you would need to compare the C-metric (which I think would fit this purpose) across many different rotations of the same vectors or ways of picking encoding vectors from the 20-dimensional space.
