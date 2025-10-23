# Peer review - Round 1

Editors:
- Alexander Shackman, https://ror.org/047s2c258 University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69686.sa0](https://doi.org/10.7554/eLife.69686.sa0)

Vinberg et al. provide a conceptual replication on individual differences in conditioned skin conductance response during fear acquisition training and BOLD fMRI in a large sample (N = 285) of healthy individuals (mono- and dizygotic twins). The authors report results that are in line with previous work and new results from a whole-brain analysis and suggest unique and shared contributions of individual brain regions.


---

# Peer review - Round 1

Editors:
- Alexander Shackman, https://ror.org/047s2c258 University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69686.sa1](https://doi.org/10.7554/eLife.69686.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Whole Brain Correlates of Individual Differences in Skin Conductance Responses during Human Fear Conditioning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Drs. Shackman (Reviewing Editor) and Büchel (Senior Editor).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions

• Authors need to better integrate genetic relatedness into their report.

o The study sample is relatively large (N = 285) – yet the sample is special in that participants were genetically related and as siblings (twins, mono- and dizygotic twins) shared environmental influences. This become only apparent in the method section (and discussion?) but needs to be mentioned upfront in the abstract, intro and included in the discussion as this may have an impact on the results. From the methods section it remained unclear how many pairs of di- and monozyotic twins were included in the study and more information on the sample (age range for instance) would be desirable.

• Polish the manuscript. There are grammatical errors. Wording and clarity could be improved. If the manuscript is meant for neuroscientists and psychologists in general (not only human fear conditioning experts), the reader probably needs some more background on some of the topics dealt with.

• The authors need to be more precise and nuanced in their description of prior work (see below)

• Introduction

o Provide a less superficial review of the current state of the science. Replication attempts are most useful when it is clearly outlined which effect is aimed to be replicated, a thorough and precise status quo of the literature is provided and in case of conceptual replications which procedural and analytical specifications differ from the previous, to-be-replicated work. It would be helpful for the reader if the exact results of previous work are, the employed procedures and analyses of previous work were described and discussed in relation to the present work in more detail.

o Authors need to better clarify the innovation/novelty of the aims and approach

o Provide a stronger motivation for the amygdala focus

– One of the Reviewers noted that, as it is currently written, I found the emphasis on the amygdala problematic. One of the goals of the manuscript is "to replicate previous findings of an association between individual differences in amygdala response and SCR using an ROI approach". Why is this a goal? Isn't the goal to understand the brain correlates of differences in human conditioning. Maybe the ROI result can be added as an additional result, but it probably should not be part of the goals, at least without much stronger justification in the Introduction.

– Another Reviewer noted that, Finding out about an SCR-amygdala BOLD correlation is one of the motives of this study. I was left unsure why mass-univariate amygala activity should correlate with the CS+/CS- difference. According to Fullana et al. (2016), there is no evidence of group-level amygdala activity in the CS+/CS- contrast. On the other hand, patterns of neural responses in the amygdala distinguish CS+/CS- (Bach et al. 2010 J Neurosci, Visser et al. 2011 J Neurosci, Staib and Bach 2018 NIMG). CS+-on neurons are sparse in the amygdala (Reijmers et al. 2007 Science) and is an equal number of CS+ on and CS+ off neurons in the central amygdala (Tovote et al. 2015 Nat Rev Neurosci and original papers referenced therein). On the balance of things, the motivation for looking at amygdala activity in the first place is weak. This needs to be better motivated in light of the available evidence

• Approach

o Authors need to clarify the approach and provide some crucial missing details that have the potential to markedly influence the results and conclusions

– Enrollment criteria

• Some inclusion/exclusion criteria are not well defined (e.g., "current alcohol or drug-related problems") or unclear (e.g., why should someone receiving psychological treatment be excluded? were only psychotropic medications -and not other medications- excluded? )

– SCR/EDA

• The peak-scoring windows for the SCR analysis are unclear, and potentially quite problematic. This, together with the comparably large effect size for the CS+/CS- difference in SCR, suggests a potential risk that the authors may have inadvertently looked at outcome-driven (US- or omission-driven) SCR, rather than conditioned SCR. This would call into question the brain-behavior associations

o The authors seem to use a 6 s-SOA delay fear conditioning paradigm. SCR scoring was done with ledalab, using the "maximum phasic driver amplitude 1-4 seconds after CS presentation for each participant". The potential problem is the peak detection window. First, can the authors clarify whether the peak window is 1-4 s after CS onset or after CS offset? Second, do they analyse only non-reinforced trials or also reinforced trials?

o What Ledalab calls the "driver" is a peripheral neural impulse at some unspecified place in the peripheral autonomic system. As can be seen in figure 5a in Benedek and Kaernbach (2010) where SCR were elicited by external events, this "driver" peaks around 2 s after an external event. So, if the US (or US omission) elicits an SCR, then the estimated "driver" will peak 2 s after CS offset and would be included in a 1-4 s window after CS offset. If, on the other hand, there was a gradual increase in SCR > 2 s into the CS, then the driver would peak > 4 s after CS onset and would not be included in a 1-4 s window after CS onset.

o In sum, the authors need to better work out and explain their peak scoring windows. They should also compare reinforced and non-reinforced CS+ trials, to rule out any bias in their analysis. Given that Ledalab yields no better results than standard peak scoring, and sometimes worse results (Bach 2014 Biological Psychology), they may want to consider using a standard peak-scoring analysis or similar strategy. (I note that the standard procedures implemented in PsPM – Bach et al. 2020 Beh Res Therapy – are not optimized for this 6-s SOA, even though there is an option that makes the models suitable for this case as well.)

• In general, the authors need to provide more details on the SCR data acquisition, processing, and analyses (e.g. the versions of the software used and specific settings/parameters e.g., sampling rate, all filters, downsampling if any, derivative scores, quality assurance/control procedures, etc.).

• The pre-processing (filtering) is not sufficiently justified. Authors may want to consider the results by Privratsky et al. 2020 (https://pubmed.ncbi.nlm.nih.gov/33075428/) to guide their choice of filters

• The authors need to elaborate on the advantages of using Z-transformed SCR in one set of analyses and square root transformed raw values in other sets of analyses? The reader would profit from a bit more detail to what extent Z-transformed values lead to confounding CS+ and CS- values with response magnitude (as indicated in section 4.3.3).

• The authors may want to consult Staib, Castegnetti and Bach 2015 for an investigation of the individual-level z-scoring approach used here.

• Insufficient rationale for analysis: "…if neural correlates to differential SCR were driven more by CS+ or CS-" – What is the motivation for these analyses?

– fMRI

• Similar comments apply (e.g. preprocessing steps in spm, software versions, etc).

• Can the authors provide a more information how exactly the eigenvariates were extracted as there are a number of different ways to do so (different tools, first-level, second level). I also suggest to add a little bit more information/explanation/ discussion what exactly is captured by the eigenvariate that was extracted. Given the level of details provided in the manuscript, I could not completely follow the procedure (i.e., are not 100% sure what was done) and hence interpretation.

• Please clarify whether the CS+ with US were included in the fMRI analyses (or only the CS+ without US)

o Insufficient rationale for some analyses

– Putting together whole-brain and ROI-based data in a regression analysis seems not "fair" (e.g. subject to different biases) to assess the contribution of different brain activations to SCRs

o Additional Analyses – SCR and fMRI: Ideally, data from habituation should be presented/analyzed to make sure that there are no differences between the CS+ and CS- before conditioning.

• Discussion

o At points, the discussion is difficult to follow. I think it needs some cutting and pruning and to be more concise. Some terms are not well defined (e.g, what is "autonomic regulation"?), what are "increases in anxiety"? also, the results from functional connectivity and fMRI studies are combined

o Did the authors record any other outcome measures than SCRs and BOLD fMRI? As the authors only report individual difference analyses with SCRs, the question remains whether results can really be interpreted the way the authors do in the discussion (arousal/salience). It would be very interesting to see comparable analyses with ratings of fear or contingency awareness. If these are not available, I suggest to discuss this point in a bit more detail.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Whole Brain Correlates of Individual Differences in Skin Conductance Responses during Discriminative Fear Conditioning to Social Cues" for further consideration by eLife. Your revised article has been evaluated by Drs. Shackman (Reviewing Editor) and Büchel (Senior Editor) and 2 expert reviewers.

Based on a consultation with the reviewers, there is consensus that, while the manuscript has been improved, there are some important remaining issues that need to be addressed.

To summarize:

(1) The Reviewers identified substantial inconsistencies between the point-by-point response and the revised manuscript, making it difficult to judge the revision.

(2) Table 2 is not evident.

(3) Introduction. The Reviewers emphasized the importance of providing a more thorough review of the existing literature and clarifying the specific aims and their rationale. Again, it will be important to adequately address this in both the response letter and the revised manuscript (and to ensure that the two documents are consistent).

(4) The Reviewers raised some concerns with the electrodermal activity (EDA) approach that need to be addressed. Key details are missing. Adequate rationale for the approach should be provided. It may be useful to re-analyze the data using a more optimal approach.

(5) The Reviewers emphasized the need for greater precision in terminology, more accurate descriptions of prior work (e.g. by Fullana and colleagues), and more sober discussion of the results.

(6) The Reviewers underscored the importance of clearly referencing supplementary material (e.g. Appendix) in the main manuscript, to ensure that readers can easily find the referenced information.

(7) The Reviewers highlighted the need to carefully proofread and copy-edit the revision before re-submission to correct any typographic errors.

Reviewer #1:

The authors have been responsive to my comments and made substantial changes to their manuscript. Nonetheless, it was quite challenging to review this revision as the changes were not fully transparent. In many places, the quotes included in the point-by-point cover letter did not match the revised text, some new text was not highlighted as new text, deleted text was not shown as deleted text at all (which made it extra difficult for me as a reviewer) and I was unable to identify Table 2 that was newly inserted according to the letter. Despite these issues, the results the authors provide are in principle interesting and the large sample should be noted (even though this was a very specific twin sample) even though effects must be considered small.

Abstract

- "Reproduce" is not the correct term. Replicability is "re-performing the experiment and collecting new data," whereas reproducibility is "re-performing the same analysis with the same code using a different analyst" (Patil et al., 2016). Clearly, the authors did not reproduce any results here. What the authors did here was a generalizability test I assume (also known as conceptual replication).

- Differences between this investigation and previous work need to be carved out more clearly in the introduction and discussion (see also next comment).

- Also please specify if N refers to individuals or pairs of twins.

Introduction

- Prior Work. Provide a less superficial review of the current state of the science. Replication attempts are most useful when it is clearly outlined which effect is aimed to be replicated, a thorough and precise status quo of the literature is provided, and in the case of conceptual replications which procedural and analytical specifications differ from the previous, to-be-replicated work. It would be helpful for the reader if the exact results of previous work are, the employed procedures and analyses of previous work were described and discussed in relation to the present work in more detail.

- Aims. Authors need to clarify the innovation/novelty of the aims and approach. There are inconsistencies between the letter and the manuscript.

- Amygdala Focus. Provide a stronger motivation for the amygdala focus.

"One of the Reviewers noted that, as it is currently written, I found the emphasis on the amygdala problematic. One of the goals of the ms is "to replicate previous findings of an association between individual differences in amygdala response and SCR using an ROI approach. Why is this a goal? Isn't the goal to understand the brain correlates of differences in human conditioning. Maybe the ROI result can be added as an additional result, but it probably should not be part of the goals, at least without much stronger justification in the Introduction. We agree that is problematic, and incorrect, to describe the motivation for focusing on the amygdala as being to 'replicate previous findings'. Our focus on the amygdala is grounded in empirical work in rodents showing that the amygdala is necessary for fear conditioning and theories of the importance of the amygdala for both fear conditioning and SCR modulation in humans. Post hoc, we found evidence for greater responses to CS+ than CS- in the amygdala in our whole-brain voxel-based analysis of fMRI data, suggesting that the amygdala might be involved in the acquisition of conditioned fear in our sample. This reflects the finding of another larger (n > 100) neuroimaging study of fear conditioning that reports z-values in the amygdala larger than 5 (Sjouwerman et al., 2020). Therefore, we think a special focus on the amygdala is motivated, and useful, for understanding the regulation of SCR during fear conditioning. However, as the aim was not to replicate the previous findings in the amygdala, we have changed the wording in the last paragraph of the introduction to: 'Also, because the amygdala has been theorized to be important for both fear conditioning and SCR modulation in humans, the association between amygdala response and SCR was assessed using an ROI approach.'"

Comment: If replication was in fact a secondary aim, this needs to be elaborated more in the manuscript. While the authors go into detail in the letter, they only inserted a single sentence on page 3. Please elaborate (also include heterogeneous findings if relevant) and do not change the aims of your work post hoc. It's fine to clarify the aims in response to Reviewer comments, but the aims should not substantively change.

"Another Reviewer noted that Finding out about an SCR-amygdala BOLD correlation is one of the motives of this study. I was left unsure why mass-univariate amygdala activity should correlate with the CS+/CS- difference. According to Fullana et al. (2016), there is no evidence of group-level amygdala activity in the CS+/CS- contrast. On the other hand, patterns of neural responses in the amygdala distinguish CS+/CS- (Bach et al. 2010 J Neurosci, Visser et al. 2011 J Neurosci, Staib and Bach 2018 NIMG). CS+-on neurons are sparse in the amygdala (Reijmers et al. 2007 Science) and is an equal number of CS+ on and CS+ off neurons in the central amygdala (Tovote et al. 2015 Nat Rev Neurosci and original papers referenced therein). On the balance of things, the motivation for looking at amygdala activity in the first place is weak. This needs to be better motivated in light of the available evidence. The motivation to specifically look at the amygdala in relation to SCR comes from the previous work in rodents on threat conditioning as well as neuroimaging studies that have correlated SCR with amygdala responses and shown a positive correlation (see e.g. Labar, Gatenby, Gore, LeDoux and Phelps, 1998; Phelps, Delgado, Nearing and LeDoux et al. 2004; Dunsmoor, Prince, Murty, Kragel and Labar, 2011; Petrovic, Kalisch, Pessiglione, Singer and Dolan, 2008; MacNamara et al., 2015; Marin et al., 2019). We agree that the accumulated evidence for increased amygdala response to CS+ vs CS- is weak as reported by Fullana et al. (2016). However, this does not mean that the amygdala is unimportant in threat conditioning because CS+ on and CS+ off neurons in the amygdala may obscure the signal, as suggested by the reviewer. There could also be multiple other causes for the lack of amygdala findings in the meta-analysis, including varied methodological aspects across studies. Therefore, individual differences in amygdala responses could still be important for understanding SCR. Also, a comparison of amygdala responses to CS+ and CS- in our sample showed that responses were greater in CS+ trials. In the revised version, we acknowledge the lack of strong support for amygdala involvement in neuroimaging studies of conditioning in the introduction. We write: '…However, the involvement of the amygdala in human fear conditioning can be questioned from the results of a meta-analysis of fMRI studies of fear conditioning (Fullana et al., 2016). There are several possible explanations to the lack of aggregated evidence for elevated amygdala responses to the fear cue relative to the control cue. For example, the null result could be an effect of conditioned fear being expressed as a distributed activation pattern across subparts of the amygdala rather than as an increased average amygdala response (Bach et al. 2010 J Neurosci; Reijmers et al. 2007 Science). Even though the evidence for increased amygdala response to CS+ during acquisition remains a topic for discussion, the number of studies that have found a positive correlation between differential SCR and amygdala responses during the acquisition of conditioned fear is substantial (see e.g. Labar, Gatenby, Gore, LeDoux and Phelps, 1998; Phelps, Delgado, Nearing and LeDoux et al. 2004; Dunsmoor, Prince, Murty, Kragel and Labar, 2011; Petrovic, Kalisch, Pessiglione, Singer and Dolan, 2008; MacNamara et al., 2015; Marin et al., 2019), which warrants further investigation of amygdala involvement in SCR regulation in a large sample."

Comment: Note that the text provided here in the letter does not match the text in the manuscript. Please homogenize, and provide adequate detail in the manuscript.

Approach

"SCR/EDA 8 • The peak-scoring windows for the SCR analysis are unclear, and potentially quite problematic. This, together with the comparably large effect size for the CS+/CS- difference in SCR, suggests a potential risk that the authors may have inadvertently looked at outcome-driven (US- or omission-driven) SCR, rather than conditioned SCR. This would call into question the brain-behavior associations. The peak SCR was scored 1 to 4 seconds after the onset of the CS. The CS was presented for 6 seconds, and CS+ presentations co-terminated with a brief electric shock (US). Therefore, the US was presented 2s after the peak SCR was scored, which was enough time to ensure that the US could not have influenced SCRs to the CS+ and the CS-. In the revised version, we also performed a correlation between SCR and fMRI responses when only including the non-reinforced CS+ trials. Results were almost identical to the main analysis including reinforced trials (see Appendix 7)"

Comment: If the authors indeed employed a TTP (Trough To Peak) approach, the 1-4s post-CS refer to the onset of the SCR, not the peak. This approach is uncommon and potentially problematic as they may miss the true-peak which may occur later than 4s post-CS (see e.g. Boucsein 2012, Psychophysiolog). This needs clarification.

"The authors seem to use a 6 s-SOA delay fear conditioning paradigm. SCR scoring was done with ledalab, using the "maximum phasic driver amplitude 1-4 seconds after CS presentation for each participant". The potential problem is the peak detection window. First, can the authors clarify whether the peak window is 1-4 s after CS onset or after CS offset? The time window is after CS onset, not offset. We have clarified this in the methods section under SCR: 'SCR was analyzed using standard peak score (through-to-peak) 1-4 seconds after CS onset for each participant' (p. 11, row 2-3)"

Comment: More information is required. What kind of settings were chosen in Ledalab? What did they use "CDA. Phasicmax" or "TTP. Ampsum" for instance (or yet another option)? The information provided is too little to understand what the authors did.

"Second, do they analyse only non-reinforced trials or also reinforced trials? Both non-reinforced and reinforced trials were analyzed together as SCR was scored prior to US delivery. To ensure that SCR correlation with fMRI responses was equivalent for non-reinforced trials as for all trials, we analyzed these 8 trials separately, as stated earlier. Results were very similar as for all trials. We refer to the new Table 2 in our revised manuscript for statistics."

Comment: I was unable to locate Table 2. Please provide Table 2 or correct the table reference.

"What Ledalab calls the "driver" is a peripheral neural impulse at some unspecified place in the peripheral autonomic system. As can be seen in figure 5a in Benedek and Kaernbach (2010) where SCR was elicited by external events, this "driver" peaks around 2 s after an external event. So, if the US (or US omission) elicits an SCR, then the estimated "driver" will peak 2 s after CS offset and would be included in a 1-4 s window after CS offset. If, on the other hand, there was a gradual increase in SCR > 2 s into the CS, then the driver would peak > 4 s after CS onset and would not be included in a 1-4 s window after CS onset. o In sum, the authors need to better work out and explain their peak scoring windows. They should also compare reinforced and non-reinforced CS+ trials, to rule out any bias in their analysis. Given that Ledalab yields no better results than standard peak scoring, and sometimes worse results (Bach 2014 Biological Psychology), they may want to consider using a standard peak-scoring analysis or similar strategy. (I note that the standard procedures implemented in PsPM – Bach et al. 2020 Beh Res Therapy – are not optimized for this 6-s SOA, even though there is an option that makes the models suitable for this case as well.) We thank the reviewers for this insightful comment. We have described the methodology in a more precise language. After revisiting our analysis, we noted that we had used a standard peak to through method with a time window of 1-4s post-CS onset. See our comment above to Q9."

Comment: While I appreciate the revisions, this is still not clear in the revised manuscript. Please provide a coherent and adequately complete description.

"Insufficient rationale for analysis: "…if neural correlates to differential SCR were driven more by CS+ or CS-" – What is the motivation for these analyses?

Individual differences in SCR difference scores could be associated both with individual differences in SCR to the CS+ and the CS-. Therefore, we wanted to check that SCR to the CS+, and not the CS-, was the reason for the observed correlation between SCR difference scores and fMRI contrast values. We have added this rationale in the results (p 6, row 23)"

Comment: I was unable to locate the rationale on page 6, row 23.

"At points, the authors are insufficiently precise and nuanced in their description of prior work o For instance, please indicate the direction of published findings, rather than just reporting that there was "an association" or "altered responding". We have made changes throughout the manuscript to indicate the direction of associations between SCR and fMRI responses. We have avoided terms like "an association" or "altered responding" to more precisely indicate the directions of findings."

Comment: I was unable to locate the respective changes made (as they were not referenced here and the edits in the manuscript were not fully transparent) and found the reporting oftentimes still too superficial.

"The authors used 4 different trial sequences. Can they provide information on which CS+ trial was the first reinforced trial in these different sequences? The reason I am asking this is that if the first 5 CS+ presentations in sequence#1 were not reinforced but already the first one was reinforced in sequence #2 this would likely lead to differences in learning speed and ultimately average CS discrimination which may impact on the results. Are individual differences in discrimination related to trial sequences? In all sequences, the first CS+ presentation following the 4 CS+ habituation trials was always reinforced. The sequences differed in whether the CS- or CS+ started the acquisition phase. If the reinforced CS+ is always the first trial in the acquisition phase, the CS- trial following the shock will be elevated due to sensitization. This was why the presentation order was counterbalanced. Although it is possible that trial sequences may be related to discrimination, if this is the case, we still show that the individual variation in SCR correlates with fMRI responses irrespective of trial

order."

Comment: Please add this useful information to the manuscript.

"Please clarify in the text whether the amygdala was significantly activated in the whole-brain CS+ vs CS- contrast, as this will be useful for other investigators and future meta-analyses. We now write in the Results section: "We found no differences in neural responses to the CS+ compared to the CS- during habituation. During acquisition, the pattern of activation to the CS+ relative to the CS- was very similar to the pattern reported in the meta-analysis by Fullana et al. (2016) and included large parts of the striatum, the insula, midline areas of the cingulum, lateral temporal cortex, parietal cortex and the supplementary motor areas. Of note, the whole-brain analysis also revealed greater activation to the CS+ than to the CS- in the bilateral amygdala."

Comment: I was confused about this section (page 3 line 45 to end of page) as the authors compare their results to those of Fullana who looked at the CS+/CS- contrast in fMRI but not at a correlation with SCRs. I think this is also done in other sections of the manuscript. It needs to be made clear in the manuscript that Fullana did not investigate brain-behavior associations (i.e. neural correlates of differential SCRs and how the results relate to each other).

"Discussion 41 o Authors note that individual differences in SCRs are stable and provide 3 references for this. They may want to double-check if these references really show demonstrate the stability of individual differences in CS discrimination. If I am not mistaken, neither Fredriksson (1993) nor Zeidan (2012) report stability measures for CS discrimination per se (but only for CS+ and CS- individually). This is a good point. We now refer to Fredrikson (1993) and Zeidan (2012) in terms that they have shown that SCR during fear conditioning is relatively reproducible. We do not refer to CS differences here. (First sentence in the discussion, p. 7, row 5)"

Comment: Technically, what was studied by Fredrikssion and Zeidan was reliability, not reproducibility (see above for a definition of what reproducibility refers to). I suggest being more precise here. Also, I do not think it becomes clear from the revision that the findings by Zeidan, Torrents-Rodas and Fredriksson do not refer to CS discrimination (or do they?). On the contrary, from the wording the authors have chosen, I would infer that this is about CS discrimination. As this work is mainly about CS discrimination this is important. I refer the authors to other work that also investigated fMRI test-retest reliability and/or test-retest reliability for CS discrimination and once more would appreciate (again) more precision in reporting.

Published

Ridderbusch, I. C., Wroblewski, A., Yang, Y., Richter, J., Hollandt, M., Hamm, A. O.,.…

Straube, B. (2021). Neural adaptation of cingulate and insular activity during delayed fear extinction: A replicable pattern across assessment sites and repeated measurements.

NeuroImage, 237, 118157. https://doi.org/10.1016/j.neuroimage.2021.118157

Pre-prints

Samuel E Cooper, Joseph E Dunsmoor, Kathleen Koval, Emma Pino, Shari Steinman, Test-Retest Reliability of Human Threat Conditioning and Generalization , PsyArXiv, https://psyarxiv.com/84uqz/

Maren Klingelhöfer-Jens, Mana R. Ehlers, Manuel Kuhn, Vincent Keyaniyan, Tina B. Lonsdorf. Robust group- but limited individual-level (longitudinal) reliability and insights into cross-phases response prediction of conditioned fear doi: https://doi.org/10.1101/2022.03.15.484434
