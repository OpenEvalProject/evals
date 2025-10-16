# Peer review - Round 1

Editors:
- Adrien Peyrache, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82952.sa0](https://doi.org/10.7554/eLife.82952.sa0)

This useful study investigates the coordination of neurons coding for head direction in the anterior thalamus and the retrosplenial cortex during environmental manipulations. The evidence supporting the claims of the authors is solid. The paper will be of interest to neuroscientists working on spatial navigation.


---

# Peer review - Round 1

Editors:
- Adrien Peyrache, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82952.sa1](https://doi.org/10.7554/eLife.82952.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Coordinated Head Direction Representations in Mouse Anterodorsal Thalamic Nucleus and Retrosplenial Cortex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While each reviewer has raised a number of specific concerns about the present study, there was an agreement that the following essential revisions needed to be addressed to warrant the publication of the manuscript.

1) The study claims that the 0-lag correlation in decoding error demonstrates a near-synchronous encoding of HD in the AD-RSC network. However, this observation may arise from erroneous decoding and video tracking. Specifically, the decoding seems quite unreliable at times, and concomitant errors in HD tracking and/or decoding would lead to a high 0-lag correlation. This problem can be addressed by measuring correlation at times of reliable decoding only and possibly using decoding techniques depending less on the neuron's tuning curves (i.e. unsupervised techniques).

2) Cue rotation did not necessarily lead to a shift in the internal HD signal. It seems like the animals after some time ignored the position changes of the visual cue. In this context, it doesn't make much sense to qualify the update of the HD reference as "successful". It would perhaps be better to include the first rotations or include only the trials that led to a substantial rotation of the internal HD.

3) There are some concerns about the quality of the spike sorting and criteria used for the identification of HD cells, as example tuning curves seem broader than what has been previously reported. Additional examples and quantification of sorting quality could address this problem.

4) Considering how critical the number of simultaneously recorded neurons is to evaluate the reliability of decoding, the study should include a detailed table of the number of neurons per session, etc.

5) Along the same lines, whether recordings at the same tetrode depth were included as independent samples is unclear. A detailed table of sessions, tetrode position, number of cells, etc. would be very informative.

6) The limitations regarding RSC-to-AD connectivity should be carefully discussed as RSC projecting neurons are likely in layer 6 only and may not have been sampled as well as other layers. Furthermore, only one tracing technique was used, not ruling out the possibility that these viruses have a poor tropism for this specific pathway.

The authors are invited to address as much as possible specific comments from the reviewers, appended below.

Reviewer #1 (Recommendations for the authors):

While I believe there are very strong points to this manuscript as noted above, some concerns about the experimental design have dampened my enthusiasm a bit. I have a series of specific questions.

1. The design of the behavioral protocols is not ideal to draw conclusions on visual landmark updating, as the visual cue was not presented as a reliable landmark for the animal. (It had shifted repeatedly while the animal was in the arena, and therefore probably underwent 'devaluation' (line 428) over time, and 90{degree sign} cue rotations often gave rotations of the neural representation of HD around 0 (cf line 1069)). If I understand correctly, this means that the animals after some time ignored the position changes of the visual cue. In this context, it doesn't make much sense to qualify the update of the HD reference as "successful" (line 261), after cue rotation, when an HD shift of > x{degree sign} is observed. It is a mismatch situation, and the mouse might rely more on self-information, proprioceptive and vestibular, than on the moving visual cue. I suggest changing the wording ("successful"). Beyond that, could it be helpful to include only the first few cue rotation experiments for a given animal? Before it considers the visual cue as unreliable.

There might be an opportunity to investigate more deeply the effects of learning cue reliability (or unreliability) over time.

2. Can you rule out potentially confounding effects of recordings obtained during early or late phases of the repeated exposures to the visual stimuli, that would affect the coherence between the AD and RSC HD representations? Are there more or less HD cells over time, when the animals have more prior experience with the environment?

3. To help the reader to better understand how the experiments were structured, I suggest including an overview table, indicating, per mouse, for each of the 12 mice of this study:

Mouse id;

Tetrode positions in Suppl Figure 1;

Which experimental protocols were run;

How many sessions/trials;

How many units in AD and/or in RSC were recorded;

How many of them were HD or nonHD cells;

Number of possible AD – AD pairs;

Number of possible RSC – RSC pairs;

Number of possible AD – RSC pairs.

4. Often times persistence of directional firing in the dark is used as a criterion for Head direction firing, and it may be useful to distinguish HD cells from visually responsive cells for example. I saw that 3 mice were tested in the dark (Figure 3), does it mean 9 mice were not? (How sure would you be to qualify directionally tuned cells as HD cells, and not visually responsive cells, if a dark condition was missing?)

Furthermore, the criteria for HD cells typically include cue control. Because of the lack of a disorientation period during the cue rotation, this may be difficult to affirm for the protocols used here. Do you think it is still justified to qualify all the directionally tuned neurons as HD cells?

Did you examine if units identified as HD might change and become nonHD (or vice versa) across different recording conditions?

In the dark recordings, do you find that some directionally tuned cells become silent, and might those be cells responding to the visual cue?

5. Please show more examples of tuning curves of HD and nonHD cells in addition to those in Figure 1B. I would find it more convincing and also a helpful resource, for reference, to see the range of different shapes of the tuning curves in AD and in RSC, their width, and peak firing rates.

How many HD cells have more than 1 peak (suppl Figure 2A), in AD and in RSC?

6. All head direction cells were pooled together to produce suppl Figure 2D. In an ideal setting, one would expect the diagonal of preferred peak firing directions to be straight and to show uniform coverage of the 360{degree sign}, at least for ADn. This is not entirely the case. Could some of the HD cells be cells that are tuned to the visual cue? Can you indicate the cue position(s) on the graph, and might they be overrepresented?

7. Decoding: how many neurons were included? A range is given in the Discussion section, line 423, this information should rather be moved to the methods, and the actual number of simultaneously recorded units for each ensemble (Figures2, 3, S6) indicated in the results (or figure legends). How may this number influence the accuracy of the decoding?

8. What is the firing frequency in light and in dark (Figure 3, suppl Figure 6), and is decoding still reliably carried out at low firing frequencies?

9. Figure 2C. It may be misleading to label the Y axis as a 'decoded error' with respect to a visual cue when the visual cue might not function as a visual landmark (see point 1, the mouse might rely more on self-information, proprioceptive and vestibular, than the visual cue). Figure 2C would benefit from showing more time before 0 (baseline).

10. Line 359 states that AD-to-RSC connectivity was divergent, but in Figure 4H it appears that four differently tuned AD neurons, in blue, contact two (same?) RSC neurons (same-shaped tuning curves 1-2, and 3-4). Is this a mistake? Also, can you confirm that the RSC (red) traces all qualified as HD units (it looks quite untuned by the eye)?

11. In addition to the connectivity rates indicated in Figure 4, I would suggest also including the numbers for ADn-ADn and RSC-RSC pairwise connectivity rates, for comparison, and for the sake of completeness.

12. line 274, "highly synchronized" – please indicate the time scale.

13. It is not easy to read the color codes in some instances, including Figure 4G FS vs RS; especially when histograms overlap, also in Figure S2BC and Figure S6A.

14. Figure 4 rabies tracing: There is only one example for each, please indicate n = 1, unless there are more experiments that are not shown (in which case, please show them in the supplementary data). In B, why are the presynaptically labelled cells in RSC red? Shouldn't they be green?

Figure 4G: Is there really similar tuning between connected Ad and RSC HD units (line 451)? Even if the circular mean of the RS peak differences is at -7.44{degree sign} (Figure 4G), very few pairs seem to have such a small difference in preferred head direction.

15. Suppl F1b: Why are there so many tetrode locations in RSC, the text said 11 mice were recorded in RSC. Give AP levels for thalamic sites, to help the reader to situate the lesions.

16. Mouse numbers:

Line 74, 9 mice were simultaneously recorded;

Line 97, 8 mice… which is correct?

Reviewer #2 (Recommendations for the authors):

1. The authors state that 'our results provide direct evidence against the hypothesis that visually guided updates in the HD reference would first appear in the RSC' (page 17 lines 416ff). This is indeed a strong statement, but I am not sure it is entirely supported by the authors' data. I wonder if a temporal offset in cue-rotation responses between AD and RSC HD cells might have gone undetected in the authors' study (see also point 2 below). For example, the visual update drive – in the form of e.g. an excitatory input from RCS that realigns HD cells in the AD- could be difficult to detect, considering the temporal resolution of the authors' experimental design. Hence, it is difficult to prove a 'negative result' here. The authors refer to two possible limitations (page 20 lines 491-492): 'cue devaluation with repeated trials' and 'temporal control of the cue rotation'. Is it conceivable that these limitations might have prevented the observation of a temporal delay between the shifts in HD representations between retrosplenial and AD?

2. It is surprising that the authors recorded in the retrosplenial cortex, but do not comment upon nor describe bidirectional HD cells (Jakob et al., 2017). Since these neurons are regarded as prime candidates for the sensory-HD integration the authors aim to study, I think they should focus their analysis on these firing patterns specifically.

3. The tuning curves of HD cells in the AD nucleus are very broad (e.g. Figure S2E, Figure 1B, E), which seems to be at odds with prior literature, and this is potentially concerning. I wonder if this might be accounted for by the authors' definition of HD cells, and/or by spike sorting quality. The authors should try to quantify and exclude systematic spike sorting issues. As a 'control' they should maybe apply more stringent inclusion criteria, restrict the analysis to 'good' sharply tuned and nicely sorted HD units, and see if their conclusions hold for this refined dataset as well. They should also comment on whether and how (possibly suboptimal?) sorting might have impacted the 'negative result' of the present study, i.e. the fact that against predictions from prior literature, the authors did not find evidence for a visual update drive in the RSC cortex.

4. The authors state that "the RSC is not wired to drive visual reference update" (page 17 line 413). However, connectivity RSC◊ AD has been demonstrated in several prior studies, and this is somewhat not recapitulated by the authors' tracing experiments with rabies viruses (I wonder if this finding needs to be confirmed with more conventional tracers, to exclude suboptimal tropism or synapse-specific effects of the viral transynaptic tracing, e.g. Rogers and Beier J Neurosc Methods 2021). The authors' statement is also supported by functional connectivity data (cross-correlations). The 'apparent sparsity' of connectivity could however be biased by cellular sampling since most thalamic projecting neurons are expected to be found in the deep layers (mostly L6) which seem not to have been systematically sampled with tetrode recordings.

5. The authors state that they have performed 'widespread sampling of RCS locations' (page 18 line 449). This is to some extent true; however, the retrosplenial cortex goes well beyond the recording locations sampled by the authors. I think the authors should reword these statements and acknowledge the possibility that other subfields of the retrosplenial cortex (which were not extensively sampled by the authors) could in principle be responsible for the visual update drive to the thalamus.

Reviewer #3 (Recommendations for the authors):

Decoding errors: Average decoding error in RSC seems very high – 90.83 degrees for fast head turns seems like a chance level and I am not sure if it is still appropriate to talk about successful decoding of HD in that case. Since the quality of decoding is critically dependent on the number and tuning of HD cells recorded in each session, could the authors provide evidence that in each session included in the dataset both ADN and RSC decoders perform significantly better than chance as estimated from spike shuffles?

Examples in Figure 2A show many gaps in the tracked HD of the mouse, which to me indicates the sub-optimal quality of the behavioural tracking. This is especially important for analyses of decoding errors like the one in Figure 2D that shows that internal HD representations in ADN and RSC are coordinated at zero lag (+/- 20ms). The observed zero-lag peak could be instead explained by errors in behavioural tracking dominating the analysis, which would affect both representations simultaneously and show spurious zero-lag positive correlations. However, coordination could also be shown by computing the difference between internal HD decoded from ADN and RSC at different time lags, without reference to the HD tracked behaviourally. Could the authors include this sanity check in the manuscript?

The percentage of HD cells in RSC reported in the literature is generally low (~10%), but those RSC HD cells often show very narrow HD tuning. Yet, judging by the examples, the HD tuning of RSC cells recorded in the study seems worse than expected. Could the authors provide some statistical measure of HD tuning stability for each cell (i.e. correlating the first and second half of the baseline recording) as a sanity check? Canonical HD cells should show very good tuning stability under constant conditions.

Supplementary Figure 2F seems to show an overrepresentation of HD cells with similar preferred directions, especially so in RSC. If this is indeed the case, I am wondering if this apparent HD tuning could be explained by any other behavioural variable that in this session happens to be correlated with HD, as in my experience sometimes happens when a tuning curve shows weak HD tuning. I find that such spurious HD tuning often disappears if only epochs when the animal is moving are included in computing the HD curve, could the authors demonstrate that HD tuning does not change if stationary epochs are excluded?

Could the authors provide the breakdown of overall cell numbers recorded per animal (including nonHD/HD cells), for example as a table?

Are there any differences in HD modulation across layers and sub-regions of RSC?

Figure 1J shows that HD cell receptive fields exhibit both clockwise and counterclockwise rotations, do these correspond to the clockwise or anticlockwise rotations of the cue, or is the realignment not dependent on the direction of cue rotation?

The manuscript often uses a number of trials as their sample size for statistical analyses and the methods state that tetrodes were regularly advanced, but there is no indication of whether multiple trials at the same tetrode position were included in the same statistical comparison (except for recordings '4 days apart' for the HD tuning and synaptic connectivity analyses). Multiple trials with a high likelihood of recording the same cell population should not be counted as separate samples when calculating statistical significance. The authors should clarify whether tetrodes were moved between recording sessions and, if that was not the case, correct their statistical analyses to, e.g. perform statistical tests on average values per recorded population over multiple sessions.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Coordinated Head Direction Representations in Mouse Anterodorsal Thalamic Nucleus and Retrosplenial Cortex" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but reviewer #2 has some remaining issues that need to be addressed (mostly clarification of result interpretation and discussion), as outlined below.

Reviewer #2 (Recommendations for the authors):

In response to my concern #1, the authors state: "We agree that the 20ms temporal resolution prevents the observation of a temporal offset occurring at shorter timescales, for example, that of direct excitatory drive between the two regions". This potential limitation should be specifically acknowledged in the discussion, e.g. by stating that the temporal resolution of the decoding approach (20 ms) might have prevented the resolution of faster (monosynaptic) dynamics, which are approx one order of magnitude faster. Again, I believe that saying "our results provide direct evidence against the hypothesis that visually guided updates in the HD reference would first appear in the RSC" (lines 343ff) is a very strong statement. The authors provide evidence consistent with this hypothesis but do not formally rule out alternative updating mechanisms that might occur on faster timescales, i.e. beyond the authors' temporal resolution. Faster dynamics (<20ms) might have gone undetected in the authors' work. This limitation should at least be acknowledged in the discussion.

The sentence in the abstract "with surprisingly little reciprocal drive in the corticothalamic direction" is not supported by the authors' data, nor by previous anatomical work showing strong RS deep layer-to-ADn connectivity. This is also clear from the authors' tracing data (from retrograde tracings, RS L6 shows up prominently). At some points, the authors make granular vs agranular RS distinctions (e.g. lines 377ff), but this is not done consistently throughout the manuscript, and the above sentence in the abstract generally refers to RS. The authors also refer to "asymmetry" in RS – ADn connectivity; I do not see what the authors mean by 'asymmetry', since the connectivity follows the classical thalamocortical rules (e.g. L6 back to thalamus). As for the functional data, more extensive sampling of RS L6 is needed to support claims about asymmetric connectivity. Hence, such strong claims (as the one in the abstract) should at least be moderated throughout the manuscript.
