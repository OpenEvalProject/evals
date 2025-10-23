# Peer review - Round 1

Editors:
- Neil Burgess, University College London United Kingdom

Reviewers:
- Sara N Burke, University of Florida United States

## Review text

DOI: [10.7554/eLife.44487.030](https://doi.org/10.7554/eLife.44487.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Dynamic control of hippocampal spatial coding resolution by local visual cues" for consideration by eLife. Your article has been reviewed by a Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Sara N Burke (Reviewer #1).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. Although potentially interesting, the results are not strong enough to support publication in eLife. Their novelty compared to previous results is not completely compelling, the interpretation is not entirely clear (e.g. presence of objects compared to enriched optic flow), and most importantly the results seem preliminary/ statistically weak in coming from very small numbers of animals in some analyses.

Reviewer #1:

The manuscript, "Dynamic control of hippocampal mapping resolution by local visual cues" by Bourboulou et al., documents the modulation of spatial coding by virtual 3-dimensional objects with a comprehensive analysis of firing properties of CA1 neurons in conditions with and without virtual objects. I have a few issues with the presentation of these data that would be helpful for the authors to address. First, throughout the Introduction and stated in the abstract the authors contend that, "whether hippocampal spatial coding resolution can be dynamically controlled within and between environments is unknown." This statement is false. In fact, there have been a number of studies showing that spatial coding resolution can be affected by behavioral/experimental parameters such as objects and active versus passive movement. Please see, Lee et al., 2012, Song et al., 2005, Terrazas et al., 2005 and Burke et al., 2011. The authors cite the Burke et al. (2011) paper but make no mention that this study also reported a decrease in place field size in the presence of objects, as well as an increase in the rate of theta phase precession. As it stands in the current presentation, the authors are upselling the novelty of their data.

A second major issue is how the statistics were conducted. It appears that cell number or place field number were the degrees of freedom for most analyses. Because multiple cells are recorded from the same animals, this is a nested design. In other words, multiple observations (cells) from a single subject (mouse) are treated like independent samples. The fact that many of the cells are from a common animal violates the statistical assumption that the observations are indeed independent. I refer the authors to Aarts et al., (2014) for an elegant description and meta-analysis of how such an approach can increase the chance of a Type I error. The data should be re-analyzed to account for the nested design of the experiment. Moreover, the authors do not report how many cells/fields were recorded from each mouse; so different animals could be making disproportionate contributions to the data.

Finally, the authors' use of the Hilbert transform to calculate theta phase is somewhat problematic. Hilbert imposes symmetry on the oscillation and it is known that theta is not symmetrical (Belluscio et al., 2012). This could lead to estimation errors for instantaneous phase that would obscure the quantification. At a minimum, the authors need to show that the shape of the theta oscillation (that is, the degree of asymmetry) did not vary between the object and no object conditions.

Reviewer #2:

In this paper, Bourboulou et al., show that the resolution of the hippocampal map is improved in the presence of 3D objects in the environment. They record hippocampal activity from head fixed mice running on virtual linear tracks with or without objects to show an improvement in spatial resolution and stability as well as improved theta phase precession.

While there are multiple major concerns with this paper, the biggest concern is the small number of experimental subjects per condition (**2**-3). More sessions per subject or more neurons per session cannot compensate for the possibility that the differences they saw could be the idiosyncrasies of individual subjects.

Major concerns:

1) Subsection “Low proportion of landmark vector cells in OT” "Because LV cells tend to systematically discharge near objects, these cells should discharge near the same object (s) in both back and forth trials."

This is not an accepted criterion to call a cell a LV cell. Both Deshmukh and Knierim as well as Geiller et al., papers, quoted by the authors, use the tendency to fire at multiple locations defined with respect to multiple objects to identify LV cells. The criteria in the present study merely identify bidirectional neurons. We know place fields tend to be unidirectional on 1D tracks. There's no reason why there can't be unidirectional LV cells on 1D tracks. Deshmukh and Knierim used 2D arenas, while Geuller et al., had 1D arenas, but unidirectional movement; neither of these studies have any information about bidirectionality of LV cells on 1D tracks.

Geiller et al., do refer to bidirectional predictive cells, "Indeed, it is worth noting that in a study 43 where local cues were laid on a linear track, place cells similar to LV cells were reported in significantly large numbers. These cells had bidirectional place fields that encoded in each direction an equidistant position ahead of a landmark, and were suggested to reflect view-invariant object information.", but are careful not to call these cells LV cells. In fact, the LV cell model by McNaughton et al., (1995), and the Collett et al., (1986) observations that model was supposed to explain would not predict this activity, since the animals (and the LV cells in the model) need to keep track of allocentric direction as well as distance from the landmark.

It is possible that the LV cells exhibit this bidirectional behavior in linear tracks, but there needs to be a comparison of behavior of LV cells in 2D and 1D before this bidirectional behavior gets labelled as LV.

Furthermore, this may not be the only possible representation of LV cell activity. Do the authors notice place fields equidistant from two or more objects in the same cell more often than expected by chance? That is the more classic LV cell behavior reported in Deshmukh and Knierim as well as Geiller et al., papers.

Subsection “Low proportion of landmark vector cells in OT” "In the track with objects, LV represented only 6.79% of all place cells. This corresponds to the proportion of LV cells recorded in area CA1 in the presence of real objects (Deshmukh and Knierim, 2013)."

This is an incorrect characterization of Deshmukh and Knierim results. McNaughton et al., (1995) posted that place cell vectors could be bound to one or more landmarks ("typically one, occasionally two, rarely more than two"). The percentage reported in Deshmukh and Knierim is that of LV cells with vectors bound to two or more landmarks; the paper had no means to characterize LV cells bound to a single land marks (which would be virtually indistinguishable from place cells with single place fields in absence of object manipulation). Thus, the low proportion of LV cells reported is the limitation of the method, not the actual proportion of LV cells, which is expected to be much higher.

Discussion section "the lateral entorhinal cortex where LV cells were first discovered (Deshmukh and Knierim, 2011)".

Deshmukh and Knierim (2011) did not report LV cells in LEC.

2) The papers switches between parametric and nonparametric tests, based on whether the data were normally distributed and had equal variance. While this is acceptable practice for individual tests, it is impossible to compare statistical significance across different comparisons of same quantities in the paper if one uses parametric tests while the other uses nonparametric tests. It will be better to use nonparametric tests throughout. In addition, median and range need to be reported when using nonparametric stats; mean and SEM reported in the paper are inappropriate. Conversely, reporting medians and range is inappropriate when performing parametric statistics (e.g. the box plots in Figure 1E).

3) Subsection “Effects of local visual cues on spatial coding resolution2: "similar rate of reward collections (OT: 1.70} 0.29 rewards/minute, n = 9 recording sessions in 3 mice; OT: 1.15} 0.09 rewards/minute" and "average running speed (OT: 14.1} 2.12 cm/s, n = 9 recording sessions in 3 mice; OT: 16.8} 1.58 cm/s, n = 5 recording sessions in 2 mice"

How is the average running speed for the without object track lower than that for OT (with object track), while the average reward rate is lower for OT? Do the average speed calculations exclude stationary periods? Do the OT mice sit longer at reward? More importantly, do they slow down at objects?

If they do slow down at objects, can this explain better spatial resolution/stability/place field dispersion in neural code near objects? i.e., can this be simply explained by slower speeds or longer time spent, ensuring better sampling of space near objects, and thus more (and less variable if the speeds at other locations vary more than those near objects) firing rate estimates at these locations than locations away from objects?

4) Subsection “Effects of local visual cues on spatial coding resolution” "There was a tendency for place field width (calculated on complete fields) to be lower in the track with objects (OT: 111 51.5} 3.33 cm, **n = 15 place fields**;".

This is a very small number of place fields (15) to be compared quantitatively. This ties in with the issue of small sample size (number of mice) used throughout the paper. Curiously, the authors report a greater number of place fields in the same without object condition elsewhere: subsection “Effects of local visual cues on spatial coding resolution” "Accordingly, spatial information (in bit/spike), a measure independent of place fields' detection (Skaggs et al., 1993) was very low in the track without object (0.06} 0.01 bit/spike, n = 48 place cells)". Place cells are defined as cells with at least 1 place field (subsection “Effects of local visual cues on spatial coding resolution”). Is that because most of these 48 cells don't meet the criterion of "complete place field" for even 1 field? Doesn't this make the definition of a "place cell" a bit too permissive? Clearly 31 of these fields were good enough for end track vs on track comparison (subsection “Virtual 3D objects improve spatial resolution locally”).

5) Subsection “Local visual cues improve hippocampal population coding accuracy” "We used the spike trains from all pyramidal 192 cells recorded (i.e., both the spatially modulated and nonspatially modulated cells) and compared decoded positions with actual positions of the animal in the virtual linear tracks."

Does using only the spatially modulated cells improve decoder accuracy? An explicit comparison of decoding accuracy using a matched number of spatially modulated cells is crucial, in addition to the "active cell" ensemble data presented here.

In continuation of the above point, subsection “Local visual cues improve hippocampal population coding accuracy”: "In both cases, downsampling was performed to equalize the number of cells used for decoding between the two conditions (20 active cells)."

Even after downsampling to 20 cells, most cells are place cells for with object but not place cells for without object condition. Matched number of place cells will complement this analysis.

6) The paper has no data to prove that it is the 3D nature of objects rather than their localized sensory information that is responsible for improvement in spatial representation.

7) Subsection “Recording procedure” "**On the day before recording**, animals were anesthetized (induction: isoflurane 3%; maintenance: Xylazine/Ketamine 10/100 mg/Kg supplemented with Buprenorphine 0.1 mg/Kg) and a craniotomy was drilled above one hippocampus (centered on a location -2 mm posterior and} 2.1 mm lateral from bregma)."

These lines and the rest of the paragraph in the methods give an impression that there was a single acute recording session per animal, the it is clear from the results that there were multiple recording sessions per animal (e.g. subsection “Effects of local visual cues on spatial coding resolution” "n = 5 recording sessions in 2 mice").

Each of these sessions included exposure to with and without object conditions: Subsection “Recording procedure” "All mice (n = 8) experienced first the familiar environment (either OT, OT or EOT) for around 20 back and forth trials. For mice trained in OT or OT (n = 3 and 2, respectively), this first exploration was followed, after 3 minutes of free running with the screens displaying a black background, by exploration of a new environment, identical to the previous one except for the presence of the three 3D objects (objects were added for mice trained in OT and removed for mice trained in OT) for another 20 consecutive back and forth trials." This means that the later sessions (session 2 onwards) had previous exposure to the "novel" condition; was there an effect of increasing familiarity on the neural response?

It is not clear from the description if the probes were fixed in one position on the first day of recording and reused over multiple days, or if they were inserted at different locations on different days. If they were at the same location, the statistics will be affected by the inflated degrees of freedom while recording from the same (or significantly overlapping) set of neurons over multiple days.

8) Discussion section "Nevertheless, End-track fields had a low spatial information content and stability when compared to fields recorded in OT (but similar to On-track fields recorded in the same maze). This argues against increased spatial coding resolution at these locations and further suggests a possible dissociation between overrepresentation and increased spatial coding resolution."

Or, it could simply be explained by the confusion caused by dissociation between the animal's movement and the arena caused by "teleportation" at the ends of the track.

9) Subsection "Effects of virtual objects in a visually enriched environment": This section lacks an essential control with enriched environment without objects.

10) Subsection “Virtual reality environments” "Outside the maze walls, two large 3D columns were positioned on each side (dimensions 8 x 8 x 47 cm; positions 58 and 143 cm from end wall) to provide additional visual cues.

While 58cm column position is close to an object, 143 cm position is not; there appears to be an enhancement in local stability near 143cm. But these columns are 3D, so doesn't detract from the overall analysis – just compounds the interpretation of this specific experiment. Is the reported improvement in neural code really due to an enrichment or merely an increase in number of discrete landmarks available to the animals?

Reviewer #3:

In this paper, the authors record hippocampal neurons as mice explore virtual reality environments that vary in their presence or absence of visual objects. They find that the resolution, defined as the number, spatial stability and scale, or place cells increases in the presence of visual objects. They go on to show that visual objects also enhance temporal coding, with theta phase precession emerging to a larger degree in the object rich compared to object poor environment. These results have interesting implications for our understanding of how hippocampal circuits dynamically change their coding properties based on the visual features available to the animal. In general, the experiments and the analyses in this paper are rigorously performed. The authors convincingly demonstrate a number of coding differences in hippocampal activity between the two environments. However, I do have concerns regarding interpretation, controls and sample size.

1) Interpretation and controls: I'm not certain to what degree the increased place cell resolution is driven by an 'object' per say versus the availability of improved optic flow sources. The use of a visually rich track with objects goes part way to addressing this issue but does not account for the fact that the optic flow from objects may carry more information than the optic flow from the walls, due to the proximity of the objects to the mouse. Moreover, the appropriate control here would be to record in the visually rich environment in the absence of the objects. It is possible that the presence of the objects induces a ceiling effect (perhaps coding cannot be further improved). More convincing to me would be that the visually rich environment without objects did not improve coding to the same degree as the presence of objects.

2) Sample size: Unless I misunderstood something, the number of place cells out of the total number of cells seems surprisingly low (48 and 103 out of 1124), which is concerning. I also have some concern about the number of mice used in the OT track (n = 2); while the overall cell number is large, I worry that this sample size is too small in terms of individual animals. Moreover, the session number is also rather small in some cases.

[Editors’ note: what now follows is the decision letter after the authors submitted an appeal.]

Thank you again for choosing to send your work entitled "Dynamic control of hippocampal spatial coding resolution by local visual cues" for consideration at eLife. Your article and your letter of appeal have been considered by a Senior Editor, a Reviewing Editor, and the original reviewers. We would happy to consider a new submission along the lines of your appeal, but please take note of the specific points below:

- Specifically, the authors would need to include the controls in a revised version, as well as the additional animal. The authors should redo the statistics taking into account the nested design after adding more data as indicated.

- In addition, the authors also need to substantially overhaul the writing of the entire manuscript to reflect the claims they make in the rebuttal/appeal.

For example, they state in the rebuttal, "We classified a cell as a LV cell if it responded either to multiple objects (having place field in the same object zones in back and forth trial) or to a single object (if they in addition code for that object's identity)." The entire LV cells section (subsection “Low proportion of landmark vector cells in OT”) does not mention anything about object identity being used for LV detection. Neither does the LV cells section (subsection “Landmark Vector cells detection”). The results do mention responding to the same object in both direction as a criterion, but that is not object identity, as a neuron firing bidirectionally for all objects will also be classified as LV cell.

- The resubmission will have to also deal with related issues, like the claims about percentages of cells that are landmark vector cells and how they compare with the other papers, definition of LV cells as bidirectional cells without confirming their LV nature in 2D environments etc.
