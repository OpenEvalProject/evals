# Peer review - Round 1

Editors:
- Olga Boudker, Weill Cornell Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66862.sa1](https://doi.org/10.7554/eLife.66862.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper will be of broad interest, particularly to mechanobiologists and muscle scientists. The authors investigated how muscle contraction might be linked to the mechanical activation of a kinase domain in a large structural protein in a living animal. They developed new imaging methods to relate molecular-level mechanical events to the motion of the whole organism, C. elegans. The work points to a potentially new regulatory mechanism via a mechanically sensitive kinase. The study combines imaging of the moving live animal with FRET measurements to show that twitchin kinase activation is coupled to muscle contraction. The necessary development of an imaging and image analysis platform that combines information on locomotion with fluorescence output is an important advance in itself. The conclusions might represent ground-breaking work into cytoskeletal signaling mechanisms.

Decision letter after peer review:

Thank you for submitting your article "Conformational changes in twitchin kinase in vivo revealed by FRET imaging of freely moving C. elegans" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Olga Boudker as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: James R Sellers (Reviewer #1); Isaac Li (Reviewer #2); Mathias Gautel (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All reviewers agreed that this is a high-quality significant paper that requires primarily editorial revisions. Below I have compiled questions, comments, and suggestions that the reviewers have made.

(1) The authors address the importance of discriminating between the desired intramolecular FRET signal versus any intermolecular FRET, which, given the tight molecular packing of the myofilament lattice, is an important concern to be addressed. Their approach was to introduce the FRET fluorophores into two different positions along the transgenic reporter construct and ultimately, for the test construct, in the gene edited nematodes. However, for force to act across the kinase region, it would have to be bound to two components of the myofilament lattice moving with respect to each other (explaining sufficient conformational changes to account for the FRET changes and induce an open kinase conformation) by its N- versus C-terminal regions. Therefore, a C-terminally integrated FRET may be in a different molecular and mechanical environment than the regions immediately around the kinase domain. Ideally, to assess the level of intermolecular FRET, two constructs with Donor or Acceptor fluorophore only, but in their correct positions for the complete sensor, are co-expressed. Any FRET signal detected and any changes in FRET would then be attributable to intermolecular FRET occurring at the site of the sensor due to spatial proximity of the donor and acceptor fluorophores.

(2) Figure 5 B and C indicate that expression of the transgenic FRET sensor seems higher in GB282 than in GB284, and this appears to correlate with higher FRET signals. Has the FRET signal been corrected for expression levels or donor-acceptor intensity?

(3) Given the major achievement of generating the GB287 (or GB286?) genome-edited nematode line, it is surprising that its characterisation is terse and the results are banished to the supplements. Could FRET videos of this line be shown? Where in the sarcomere does the FRET probe localise?

(4) It seems reasonable to postulate that the relationship "between the fluorescence signal and the curvature dynamics … is causal" – but is it due to active force? Would the FRET signal change persist if the worms were paralysed or anaesthetised, e.g. with BDM or a sodium channel blocker, e.g. tricaine? In other words, is this a geometric (lattice packing) or biomechanical (active forces) effect, as far as this can be separated?

(5) It is intriguing that the largest decrease in FRET occurs in relaxed sarcomeres, implying that the kinase region would be stretched preferentially when the myosin heads are relaxed. Again, could this hypothesis be tested by interfering with the actomyosin cycle, for example with para-nitroblebbistatin? Could the authors propose, with data from point 3, a hypothetical arrangement of twitchin in the myofilament lattice that would satisfy these observations?

(6) The propagating patterns in the kymographs of mCFP and mCit (Figure 5BCFG) are puzzling. The authors contributed it to inherent locomotion artifacts, noise and internal sarcomere rearrangement during motion. While some of these may be true, could these be image processing artifacts? The authors stated in the method section that the fluorescence intensity at a particular body segment is obtained by drawing a perpendicular line to the midline. The pixels that it intersects will provide the fluorescence intensity. This approach does not seem to account for the fluorophore density change due to tissue compaction and expansion, resulting in overcounting intensity in the inner circle and undercounting at the outer circle – similar to the observed intensity patterns Figure 5BCFG. Can the intensities be normalized by the arclength at the different radii from the center of the curvature?

(7) As related to the previous comment, but more generally, image analysis is a critical and sensitive step towards the interpretation of the fluorescence results. The authors should elaborate if and how errors in the image processing might contribute to the emergence of correlation between FRET and curvature. For instance, the CFP and mCit expression levels vary significantly along the body of the worm (Figure 5) and should be time-invariant. If an error in image processing picks up nearby spatial variations as the worm moves, the detected fluorescence will become time-variant and correlate with the worm's motion. Could this happen with the current algorithm? This is a crucial assessment as it is crucial to ensure the observed small FRET changes (+/- 0.015) are due to molecular stretching and not artifacts of image processing.

(8) The shape and meaning of FRET change in the contraction-relaxation cycles (Figure 7) require further interpretation. The data shows that the extrema and phase of the FRET signal correlate to curvature, and thereby, sarcomere stretching. Is it valid to assume the stretching or relaxing of sarcomeres apply tension directly over each twitchin? Is the binding-unbinding transition of NL to TwcK two-state? If so, would this lead to two-state behaviour in the observed FRET? What can the authors comment on the shape of the FRET-curvature response curve?

(9) The reason behind the small observed FRET change (+/-0.015) requires further clarification. Is it because (1) all FRET sensors changed slightly, or (2) a small fraction of FRET sensors changed from high to low FRET. What is the expected FRET change as depicted in Figure 1D?

(10) The manuscript provides strong evidence of FRET correlating to curvature during the muscle contraction cycle. However, the causality is less clear. Does the contraction force cause the FRET change, or can curvature without any active contraction cause FRET change? For instance, if the worm is dead or myosin activity inhibited, will the bending of the worm cause FRET change?

(11) FRET was used as a proxy for kinase function in some of the discussions. Although this may be the case as expected based on crystal structures, it is not demonstrated, i.e. when the mCit-TwcK-mCFP is stretched, it is unknown whether the kinase regains activity. The current controls for TwcK activity (Figure 1C) only demonstrated the lack of kinase activity for TwcK-FP but not mCit-TwcK-mCFP. There could also be many reasons for the lack of activities, e.g.: (1) NL peptide autoinhibition, (2) misfolding of TwcK domain when tagged by fluorescent proteins, (3) steric-hindrance of target peptide binding by the fluorescent proteins. Can the kinase activity in the presence of force be experimentally demonstrated? I recognize that this may be a very challenging experiment, and outside of the scope of the current manuscript, it should be discussed. In any case, FRET is still valid as a proxy for tension through TwcK. However, arguments based on kinase function during FRET change can only be inferred indirectly. These points should be made more explicitly in the article.

(12) Is there any existing estimation on the magnitude of force required to peel the NL domain off from TwcK? I think some estimates of the expected dynamic range of FRET in response to force (order of magnitude estimation) could help interpret the result.

(13) Direct comparison of FRET between mCit-TwcK-mCFP (GB282) and mCFP-Ig-mCit (GB284) requires clarification. First, GB282 seems to be expressing the proteins at a higher level comparing to GB284 (Figure 5). Is this true for all worms? Second, it seems that GB284 generally has a lower FRET comparing to GB282. This is puzzling as the authors assumed the Ig domains do not unfold, and hence GB284 should remain at high FRET compared to GB282. Isn't the unfolding of Ig domains a physiological process in muscle function? What is the evidence that Ig domains in the control construct would not unfold? Would it be a better control to remove proteins between the two FRET FPs if this is uncertain? Is maintaining the exact distance between the two FPs crucial?

(14) What causes the expression level difference along the length of the worm? It seems that each part of the worm can contract similarly (Figure 4A), which indicates the presence of muscles and sarcomeres along the entire body.

(15) The authors have made several arguments regarding intermolecular FRET. The Foster distance for fluorescent proteins is only 4-6 nm. Considering that they sit at a particular location on the long polydomain protein, it would require perfect alignment with nearby twitchins at a very high spatial density for intermolecular FRET to occur, which seems unlikely. Do the authors have evidence that intermolecular FRET is indeed happening?

(16) I think it would be beneficial if the authors can show that dorsal and ventral FRET anticorrelate as a validation of their method and strengthen the paper.

(17) Many of the readers will not be familiar with C. elegans motility and the manuscript would benefit from having a supplemental video of a moving worm, perhaps captured by each of the imaging modalities.

(18) Similarly, there should be some description of what is the period of the undulating waves.

(19) It took me a while to wrap my head around the kymographs in Figure 4 and subsequent figures and it would be helpful to have a bit more discussion of how they are generated and interpreted. I assume that each of the diagonals in the kymographs represent a single contractive event. Can you average 10 or more of these in cases where the direction and period are very similar to get cleaner signals?

(20) Is there any way to instantaneously paralyze the worms and freeze them in their undulating shapes? If so, could this simplify the imaging?

(21) I think that the data shown on the knock-out/knock-in worms is important and I suggest moving it to the main text. Figure 6 could go to the supplement.

(22) Figure 1D seems only to suggest that the NL domain is only stretched instead of unbinding then stretched from the kinase. Figure 1A is a clockwise 90-degree turn, which was not clear from the illustration. The ATP pocket should be marked in both figures.

(23) Figure 2D: The assessment of distance of 5.3 nm is the distance between the N/C termini of the fluorescent proteins, but not the fluorophores. The two fluorophores' distance and orientation would affect the coupling and FRET between them. Can these values be estimated? In addition, are the observed FRET in vivo similar to FRET observed in vitro using recombinant proteins?

(24) Figure 5: The fluorescence intensity is saturated. Is this a display issue, or is the fluorescence data collected saturated? If display issue, I would recommend a non-linear colour legend to display the full dynamic range. If the collection is saturated, then wherever saturation occurs should be excluded for all analyses.

(25) I do not see where Figure 3E is mentioned in the text.

(26) Figure 4D,E. Describe the colors used for the two traces in each panel.

(27) The gene-edited twitchin line is referred to as GB287 in figure legends and text (e.g. page 15), but as GB286 in supplementary figure S4.

(28) Please correct the typo in Figure 3A: EMCCD Fluorescence Imaging

(29) Please clarify what is meant with "computed" when referring to e.g. "computed change in FRET signal" as the reader might assume the data are simulations not experimental.

Reviewer #1 (Recommendations for the authors):

Many of the readers will not be familiar with C. elegans motility and the manuscript would benefit from having a supplemental video of a moving worm, perhaps captured by each of the imaging modalities.

Similarly, there should be some description of what is the period of the undulating waves.

It took me a while to wrap my head around the kymographs in Figure 4 and subsequent figures and it would be helpful to have a bit more discussion of how they are generated and interpreted. I assume that each of the diagonals in the kymographs represent a single contractive event. Can you average 10 or more of these in cases where the direction and period are very similar to get cleaner signals?

Is there any way to instantaneously paralyze the worms and freeze them in their undulating shapes? If so, could this simplify the imaging?

I think that the data shown on the knock-out/knock-in worms is important and I suggest moving it to the main text. Figure 6 could go to the supplement.

I do not see where Figure 3E is mentioned in the text.

Figure 4D,E. Describe the colors used for the two traces in each panel.

Reviewer #2 (Recommendations for the authors):

I enjoyed reading this manuscript and appreciated the transparent discussion of many potential issues. In addition to the issues pointed out in the public review, addressing the following points could further strengthen the manuscript:

1. FRET was used as a proxy for kinase function in some of the discussions. Although this may be the case as expected based on crystal structures, it is not demonstrated, i.e. when the mCit-TwcK-mCFP is stretched, it is unknown whether the kinase regains activity. The current controls for TwcK activity (Figure 1C) only demonstrated the lack of kinase activity for TwcK-FP but not mCit-TwcK-mCFP. There could also be many reasons for the lack of activities, e.g.: (1) NL peptide autoinhibition, (2) misfolding of TwcK domain when tagged by fluorescent proteins, (3) steric-hindrance of target peptide binding by the fluorescent proteins. Can the kinase activity in the presence of force be experimentally demonstrated? I recognize that this may be a very challenging experiment, and outside of the scope of the current manuscript, it should be discussed. In any case, FRET is still valid as a proxy for tension through TwcK. However, arguments based on kinase function during FRET change can only be inferred indirectly. These points should be made more explicitly in the article.

2. Is there any existing estimation on the magnitude of force required to peel the NL domain off from TwcK? I think some estimates of the expected dynamic range of FRET in response to force (order of magnitude estimation) could help interpret the result.

3. Direct comparison of FRET between mCit-TwcK-mCFP (GB282) and mCFP-Ig-mCit (GB284) requires clarification. First, GB282 seems to be expressing the proteins at a higher level comparing to GB284 (Figure 5). Is this true for all worms? Second, it seems that GB284 generally has a lower FRET comparing to GB282. This is puzzling as the authors assumed the Ig domains do not unfold, and hence GB284 should remain at high FRET compared to GB282. Isn't the unfolding of Ig domains a physiological process in muscle function? What is the evidence that Ig domains in the control construct would not unfold? Would it be a better control to remove proteins between the two FRET FPs if this is uncertain? Is maintaining the exact distance between the two FPs crucial?

4. What causes the expression level difference along the length of the worm? It seems that each part of the worm can contract similarly (Figure 4A), which indicates the presence of muscles and sarcomeres along the entire body.

5. The authors have made several arguments regarding intermolecular FRET. The Foster distance for fluorescent proteins is only 4-6 nm. Considering that they sit at a particular location on the long polydomain protein, it would require perfect alignment with nearby twitchins at a very high spatial density for intermolecular FRET to occur, which seems unlikely. Do the authors have evidence that intermolecular FRET is indeed happening?

6. I think it would be beneficial if the authors can show that dorsal and ventral FRET anticorrelate as a validation of their method and strengthen the paper.

7. Figure 1D seems only to suggest that the NL domain is only stretched instead of unbinding then stretched from the kinase. Figure 1A is a clockwise 90-degree turn, which was not clear from the illustration. The ATP pocket should be marked in both figures.

8. Figure 2D: The assessment of distance of 5.3 nm is the distance between the N/C termini of the fluorescent proteins, but not the fluorophores. The two fluorophores' distance and orientation would affect the coupling and FRET between them. Can these values be estimated? In addition, are the observed FRET in vivo similar to FRET observed in vitro using recombinant proteins?

9. Figure 5: The fluorescence intensity is saturated. Is this a display issue, or is the fluorescence data collected saturated? If display issue, I would recommend a non-linear colour legend to display the full dynamic range. If the collection is saturated, then wherever saturation occurs should be excluded for all analyses.

Reviewer #3 (Recommendations for the authors):

1. The authors address the importance of discriminating between the desired intramolecular FRET signal versus any intermolecular FRET, which, given the tight molecular packing of the myofilament lattice, is an important concern to be addressed. Their approach was to introduce the FRET fluorophores into two different positions along the transgenic reporter construct and ultimately, for the test construct, in the gene edited nematodes.

However, for force to act across the kinase region, it would have to be bound to two components of the myofilament lattice moving with respect to each other (explaining sufficient conformational changes to account for the FRET changes and induce an open kinase conformation) by its N- versus C-terminal regions. Therefore, a C-terminally integrated FRET may be in a different molecular and mechanical environment than the regions immediately around the kinase domain.

Ideally, to assess the level of intermolecular FRET, two constructs with Donor or Acceptor fluorophore only, but in their correct positions for the complete sensor, are co-expressed. Any FRET signal detected and any changes in FRET would then be attributable to intermolecular FRET occurring at the site of the sensor due to spatial proximity of the donor and acceptor fluorophores.

2. Figure 5 B and C indicate that expression of the transgenic FRET sensor seems higher in GB282 than in GB284, and this appears to correlate with higher FRET signals. Has the FRET signal been corrected for expression levels or donor-acceptor intensity?

3. Given the major achievement of generating the GB287 (or GB286?) genome-edited nematode line, it is surprising that its characterisation is terse and the results are banished to the supplements. Could FRET videos of this line be shown? Where in the sarcomere does the FRET probe localise?

4. It seems reasonable to postulate that the relationship "between the fluorescence signal and the curvature dynamics … is causal" – but is it due to active force? Would the FRET signal change persist if the worms were paralysed or anaesthetised, e.g. with BDM or a sodium channel blocker, e.g. tricaine? In other words, is this a geometric (lattice packing) or biomechanical (active forces) effect, as far as this can be separated?

5. It is intriguing that the largest decrease in FRET occurs in relaxed sarcomeres, implying that the kinase region would be stretched preferentially when the myosin heads are relaxed. Again, could this hypothesis be tested by interfering with the actomyosin cycle, for example with para-nitroblebbistatin? Could the authors propose, with data from point 3, a hypothetical arrangement of twitchin in the myofilament lattice that would satisfy these observations?
