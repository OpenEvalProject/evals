# Peer review - Round 1

Editors:
- Mihaela D Iordanova, Concordia University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64934.sa1](https://doi.org/10.7554/eLife.64934.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript is a thorough examination of dPAG activity in threat exposure. Some strengths of the paper include relating the open-closed sensory states to threatening states in a live rat study, and the elegant neural analyses that show support for the generalization of neural representation of threat approach and avoidance across procedures.

Decision letter after peer review:

Thank you for submitting your article "Dorsal Periaqueductal gray ensembles represent approach and avoidance states" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Mihaela D Iordanova as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Philip Jean-Richard-dit-Bressel (Reviewer #2); Jonathan Fadok (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The manuscript looks at how dPAG neurons represent threat approach and avoidance using the elevated plus maze and a live rat exposure situation. The data show that the dPAG populations split in terms of avoidance and approach when the mice are exposed to the EPM. These populations correspond to threat approach and avoidance in the live rat procedure. Machine learning algorithms further show support for the generalization of neural representation of threat approach and avoidance across procedures. The paper uses established behavioral methods as well as state-of-the-art neural methods and analyses. It presents a thorough examination of dPAG activity in threat exposure tasks. Although the study of the dPAG in these tasks has been reported in the past (e.g., Deng et al., 2016, DOI: 10.1523/JNEUROSCI.4425-15.2016; Masberrer et al., 2020, DOI: https://doi.org/10.1523/JNEUROSCI.0761-18.2020), which limits the novelty of the present paper, relating the open-closed sensory states to threatening states in the live rat study is a nice development.

Essential revisions:

The existing data mostly supports the main conclusions of the paper and I do not think added experimentation is needed. However, there are some concerns:

1. Concerns about the analyses, interpretation and representation of the data:

a. An argument is made in terms of threat and operationalized as a threat score and dPAG activity. However, this threat score seems to be determined where in the EPM the mouse is and has nothing to do with perception of threat derived from a behavioural response. So, if differential dPAG neurons fire to open vs closed arms in the EPM, then it seems hardly surprising that there would be a correlations between the 'threat score' and neural activity. What is more the threat score is more related to distance from centre as opposed to any actual threat. The latter is inferred. Correlation with head dip may be a better examination.

b. Cells were defined by their bias in firing patterns in open vs closed arms, which was then used to predict animal location. It would be more compelling if cell classification was determined using separate portions of the session than that used for prediction (akin to way training and testing is separated for SVM) to avoid circularity.

c. Emphasis is placed on how activity patterns are shared between incompatible behaviours such as freezing and escape, both of which are reactions to threat. While this might suggest threat-coding, it may also be the case that shared activity are an artifact of the slow kinetics of GCaMP6s coupled with these behaviours occurring in close temporal proximity to each other. Is there any evidence that the same patterns of activity are observed when the potential contribution of other behaviours are factored out? Perhaps GLM could be used to isolate event-related activity kernels.

d. For Figure 2D, define what is meant by strong correlation. What is the threshold?

e. Please include the EPM aggregate activity heatmap for all cells, as is reported for the REA in Figure 3C.

f. Is the overall activity bias near the rat in Figure 3C driven by novel threat preference in previously 'neither' cells, reduced activation of closed cells near the safe wall, or increased activation of open cells near the rat (relative to activity during EPM)?

g. The data in Figure 3-S3A do not appear to match the data Figures 3C and 3F and therefore are not representative.

h. The increased z-score to rat movement by closed-arm cells in Figure 3I-J is inconsistent with the interpretation that these neurons reflect threat proximity, since the threat is moving closer to the mouse and these cells are inhibited in proximity to threat in other scenarios. The data are better explained by the activity representing the mouse's state on the exploratory-defensive continuum.

i. There should be a zoomed-out image of PAG histology showing the spread of the GCaMP expression and the lens placement.

2. Methods. Methods should be written rigorously enough to promote reproducibility. Some specific questions are included below, but the authors should ensure that they provide a thorough account of the methods used.

a. Lack of clarity regarding shuffling and bootstrapping. It is unclear whether the authors are in fact applying bootstrapping (resampling from dataset with replacement) or another analysis method such as permutation tests (randomly relabelling cases). Please clarify and provide more details within Methods.

b. k = 10 seems arbitrary. It would be useful to know the relative strength of k = 2-10+ clusters (e.g. table of mean and minimum silhouette values) to confirm k = 10 is sensible.

c. The behavioural timeline, methods and procedures were confusing. More detail and clarity need to be provided in the Methods. This should account for the differential number of animals in the EPM and REA. Further, it was unclear when habituation took place.

d. Is the threat score binary (+1 or -1) or is it bounded by -1 to +1, with values in between? If that latter, how are values in between calculated? A liner a relationship is assumed between threat and distance travelled, which seems appropriate for the open arm but perhaps more uniformly low throughout the closed arms.

3. Discussion.

a. A discussion of the results and how they fit into the larger body of PAG literature is necessary.

b. The significance of the neither cells being activated in the REA.

c. Any insight the authors may have into the circuit or physiological differences of the two populations.

d. A discussion of the counterintuitive finding that a greater relative ratio of open:closed neurons correlates with less time in the open arm and threat approach.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Dorsal Periaqueductal gray ensembles represent approach and avoidance states" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Mihaela D Iordanova as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Philip Jean-Richard-dit-Bressel (Reviewer #2); Jonathan Fadok (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The reviewers agreed that the paper was greatly improved with the inclusion of necessary additions to methods, improvements to language, and addressing concerns around circular analyses and overlapping behaviour-related activity. The change in the semantics from EPM threat score to EPM location index was welcomed, although whether there is a linear gradient of threat in EPM remains up for debate. Some questions remain over the concerns raised previously. These are specified below.

Essential revisions:

1. Justification regarding the choice of 10 clusters has not been adequately addressed. A good solution would be to show that mean and minimum silhouette values for k = 10 is positive and higher/comparable to the range of other k-means solutions. This can be presented in a supplementary table. This is important because it goes a long way towards showing that the choice in clusters was valid. Currently the justification in the paper is not adequate and does not address why k=10 was chosen, rather is focused on why k=2 was not a good choice.

2. The added point that rat movements did not generally decrease distance to the mouse needs clarification. Did the increased distance between rat and mouse include movement made by the mouse? Given rat movement precipitates mouse escape, the increased distance is potentially due to mouse escape, not the rat moving away? Separately, was there a reason a 2 sec window was chosen? Rat movements towards the mouse followed by retreat (e.g. due to constrained movement) would easily elapse within 2secs, and be registered as movements away despite the mouse likely perceiving/responding to the advance. All relevant details about measuring rat movement should be included in Methods.

3. For variance thresholding, if this was performed per experimental session, were there cells that had high variance in one assay but low variance (and were thus excluded) in another assay? This would inflate the apparent degree of cross-assay coding. Details, i.e., a statement or Venn diagram, explaining how many cells were excluded on basis of EPM alone, REA alone, or both would be pertinent. If the number excluded on basis of only one assay is substantial, the text should acknowledge the impact this likely has on apparent cross-assay coherence.
