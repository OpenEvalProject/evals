# Peer review - Round 1

Editors:
- Alexander Shackman, University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66968.sa1](https://doi.org/10.7554/eLife.66968.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors assessed multivariate relations between a dimensionality-reduced symptom space and brain-imaging features, using a large database of individuals with psychosis-spectrum disorders (PSD). Demonstrating both high stability and reproducibility of their approaches, this work showed a promise that diagnosis or treatment of PSD can benefit from a proposed data-driven brain-symptom mapping framework.

Decision letter after peer review:

Thank you for submitting your article "Mapping Brain-Behavioral Relationships Along the Psychosis Spectrum" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Drs. Shackman (Reviewing Editor) and Gold (Senior Editor).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

– The reviewers expressed some enthusiasm for the report:

– Unique dataset!

– I really appreciate the authors' efforts to demonstrate the robustness of their findings. Overall, this is really great work.

– This paper has the potential to provide helpful guidance to neuroimaging scientists who aim to discover generalizable associations between multimodal imaging and behavior.

– The strength of this study is that (i) in every analysis, the authors provide high-level evidence of reproducibility, (ii) the study included several control analyses to test alternatives or independent techniques (e.g., ICA, univariate vs. multivariate), and (iii) the report demonstrates relations with independently acquired pharmacological neuroimaging and gene expression maps.

– Overall the study has originality and several important tips and guidance for behavior-brain mapping.

– The report details an interesting and rather comprehensive analysis of the trend of developing data-driven methods for developing brain-symptom dimension biomarkers that bring a biological basis to the symptoms (across PANSS and cognitive features) that relate to psychotic disorders.

– Combined analysis of canonical psychosis symptoms and cognitive deficits across multiple traditional psychosis-related diagnoses offers one of the most comprehensive mappings of impairments experienced within PSD to brain features to date.

– Cross-validation analyses and use of various datasets (diagnostic replication, pharmacological neuroimaging) is extremely impressive, well-motivated, and thorough. In addition, the authors use a large dataset and provide "out of sample" validity.

– Medication status and dosage also accounted for.

– Similarly, the extensive examination of both univariate and multivariate neuro-behavioral solutions from a methodological viewpoint, including the testing of multiple configurations of CCA (i.e. with different parcellation granularities), offers very strong support for the selected symptom-to-neural mapping.

– The plots of the obtained PC axes compared to those of standard clinical symptom aggregate scales provide a really elegant illustration of the differences and demonstrate clearly the value of data-driven symptom reduction over conventional categories.

– The comparison of the obtained neuro-behavioral map for the "Psychosis configuration" symptom dimension to both pharmacological neuroimaging and neural gene expression maps highlights direct possible links with both underlying disorder mechanisms and possible avenues for treatment development and application.

– The authors' explicit investigation of whether PSD and healthy controls share a major portion of neural variance (possibly present across all people) has strong implications for future brain-behavior mapping studies, and provides a starting point for narrowing the neural feature space to just the subset of features showing symptom-relevant variance in PSD.

– Overall, the work could advance our knowledge in the development of biomarkers or subject level identifiers for psychiatric disorders and potentially be elevated to the level of an individual "subject screener". While this is a noble goal, this will require more data and information in the future as a means to do this. This is certainly an important step forward in this regard.

Essential revisions:

Nevertheless, both reviewers (and a third, who was unable to provide a full review in a timely manner) expressed some significant, conceptually overlapping concerns.

– Significance/Innovation – As written, it's unclear that the report represents a significant advance.

– As it stands, while the results are very interesting and presented in a quite compelling way, it is unclear whether this is an advance in modeling beyond what has been done before.

– Significance/Aims – Lack of clarity about the aims and goals, which weakens significance and makes the report more challenging to understand.

- A major concern is the emphasis. Is the paper about the methods, or about understanding the neural underpinnings of PSD?

– I was not clear about the target domain of this paper. If this was to show the reproducibility of datamining findings, I guess one can give some other examples, not fully testing on the PSD. But then if I read in that angle, the authors also hold strong domain opinion and knowledge on the PSD. So it would be much straightforward to read if they clarify their stance a bit more between clinical neuroscience and datamining/reproducibility.

Clarity

– Overall I found the paper very hard to read. There are abbreviations everywhere. The paper is methods heavy (which I am not opposed to and quite like). It is clear that the authors took a lot of care in thinking about the methods that were chosen. That said, I think that the organization would benefit from a more traditional Intro, Methods, Results, and Discussion formatting so that it would be easier to parse the Results. The figures are extremely dense and there are often terms that are coined or used that are not or poorly defined.

– The paper contains heavy descriptions about dimensionality reduction (e.g., PCA, ICA, and CCA) and prediction techniques which, at times, made it challenging to read.

Inadequate motivation for targeting the Xia paper as a point of reference, weakening significance.

– One thing I found conceptually difficult is the explicit comparison to the work in the Xia paper from the Satterthwaite group. Is this a fair comparison? The sample demographics are extremely different (e.g. non-clinical, general population, younger). Can it be suggested that the groups that are clinically defined here are comparable? Is this an appropriate comparison and standard to make? To suggest that the work in that paper is not reproducible seems flawed, when viewed in this light.

– The authors' argument seems to hinge on their methods being better insofar as it increases overall reproducibility (a good thing). However, they use the Xia paper as a strawman – this paper is done in a non-clinical, younger sample. Perhaps, it's not that surprising that they cannot replicate.

Key methodological details and motivations for specific choices are lacking.

– Many researcher degrees of freedom in what is reported (e.g., why is PC3 selected? Because it looks like default network? this is not explicitly stated, and selection criteria are not quantified).

– Why was PCA selected for the analysis rather than ICA? Authors mention that PCA enables the discovery of orthogonal symptom dimensions, but don't elaborate on why this is expected to better capture behavioral variation within PSD compared to non-orthogonal dimensions. Given that symptom and/or cognitive items in conventional assessments are likely to be correlated in one way or another, allowing correlations to be present in the low-rank behavioral solution may better represent the original clinical profiles and drive more accurate brain-behavior mapping. Moreover, as alluded to in the Discussion, employing an oblique rotation in the identification of dimensionality-reduced symptom axes may have actually resulted in a brain-behavior space that is more generalizable to other psychiatric spectra. Why not use something more relevant to symptom/behavior data like a factor analysis?

– The gene expression mapping section lacks some justification for why the 7 genes of interest were specifically chosen from among the numerous serotonin and GABA receptors and interneuron markers (relevant for PSD) available in the AHBA. Brief reference to the believed significance of the chosen genes in psychosis pathology would have helped to contextualize the observed relationship with the neuro-behavioral map.

Need to clearly distinguish 'stability' from 'reproducibility'

– To enhance the clarity of the results, the authors need to be more explicit about what they demonstrated is stability or reproducibility in each result section. As discussed on page 18, during the k-fold or leave-one-site out validation, at each iteration the training data for PCA is largely overlapped between the full sample model and the one excluding the held-out data, which makes the result of dimensionality reduction quite similar. In this case, an extremely high prediction-observation correlation is not totally unexpected, and those tests may not be ideal for generalizability but more fit to the stability test (i.e., whether the result is robust against potential outliers). I know that the authors already used the word 'stable' in many sentences, so my comment is only minor, but some sentences "… symptom-derived PCA solution remained highly robust across all sites.…", ".… This similarity was high for all sites (Figure S6).…" (p2) and others give a nuance as if the authors found a replicated effect from each site independently (i.e., PCA on each side), so generalizable. Please note that I am not questioning the fact that the authors demonstrated reproducibility. They did it based on the 'split-half' independent test. The only thing I point out here is that it would be clearer if the study deals with the stability and reproducibility separately across the result section.

Some key aspects of the results need a much more thorough discussion

– Weakness – A lack of overarching interpretation for PC's other than #3. Although the authors provided all supplementary materials for the relationship between behaviors and other principal components than the 3rd one, the current presentation of the results (only the single component throughout the study) makes the study partially complete. Unless the whole point of the study is a thorough data mining test on neuroimaging, I think that the authors could provide an integrative interpretation or discussion on other behavioral PCs that are relevant to explain the PSD behaviors and brain.

– What the identified univariate neuro-behavioral mapping for PC3 ("psychosis configuration") actually means from an empirical or brain network perspective is not really ever discussed in detail. E.g., in Results, "a high positive PC3 score was associated with both reduced GBC across insular and superior dorsal cingulate cortices, thalamus, and anterior cerebellum and elevated GBC across precuneus, medial prefrontal, inferior parietal, superior temporal cortices and posterior lateral cerebellum." While the meaning and calculation of GBC can be gleaned from the Methods, a direct interpretation of the neuro-behavioral results in terms of the types of symptoms contributing to PC3 and relative hyper-/hypo-connectivity of the DMN compared to e.g. healthy controls could facilitate easier comparisons with the findings of past studies (since GBC does not seem to be a very commonly-used measure in the psychosis fMRI literature). Also important since GBC is a summary measure of the average connectivity of a region, and doesn't provide any specificity in terms of which regions in particular are more or less connected within a functional network (an inherent limitation of this measure which warrants further attention).

– While the inclusion of cognitive measures for PSD individuals is a main (self-)selling point of the paper, there's very limited focus on the "Cognitive functioning" component (PC2) of the PCA solution. Examining Figure S8K, the GBC map for this cognitive component seems almost to be the inverse for that of the "Psychosis configuration" component (PC3) focused on in the rest of the paper. Since PC3 does not seem to have high loadings from any of the cognitive items, but it is known that psychosis spectrum individuals tend to exhibit cognitive deficits which also have strong predictive power for illness trajectory, some discussion of how multiple univariate neuro-behavioral features could feasibly be used in conjunction with one another could have been really interesting.

Reviewer 1:

The paper assessed the relationship between a dimensionality-reduced symptom space and functional brain imaging features based on the large multicentric data of individuals with psychosis-spectrum disorders (PSD).

The strength of this study is that (i) in every analysis, the authors provided high-level evidence of reproducibility in their findings, (ii) the study included several control analyses to test other comparable alternatives or independent techniques (e.g., ICA, univariate vs. multivariate), and (iii) correlating to independently acquired pharmacological neuroimaging and gene expression maps, the study highlighted neurobiological validity of their results.

Overall the study has originality and several important tips and guidance for behavior-brain mapping, although the paper contains heavy descriptions about data mining techniques such as several dimensionality reduction algorithms (e.g., PCA, ICA, and CCA) and prediction models.

Although relatively minors, I also have few points on the weaknesses, including (i) an incomplete description about how to tell the PSD effects from the normal spectrum, (ii) a lack of overarching interpretation for other principal components rather than only the third one, and (iii) somewhat expected results in the stability of PC and relevant indices.

Reviewer 2:

The work by Ji et al., is an interesting and rather comprehensive analysis of the trend of developing data-driven methods for developing brain-symptom dimension biomarkers that bring a biological basis to the symptoms (across PANSS and cognitive features) that relate to psychotic disorders. To this end, the authors performed several interesting multivariate analyses to decompose the symptom/behavioural dimensions and functional connectivity data. To this end, the authors use data from individuals from a transdiagnostic group of individuals recruited by the BSNIP cohort and combine high-level methods in order to integrate both types of modalities. Conceptually there are several strengths to this paper that should be applauded. However, I do think that there are important aspects of this paper that need revision to improve readability and to better compare the methods to what is in the field and provide a balanced view relative to previous work with the same basic concepts that they are building their work around. Overall, I feel as though the work could advance our knowledge in the development of biomarkers or subject level identifiers for psychiatric disorders and potentially be elevated to the level of an individual "subject screener". While this is a noble goal, this will require more data and information in the future as a means to do this. This is certainly an important step forward in this regard.

Strengths:

– Combined analysis of canonical psychosis symptoms and cognitive deficits across multiple traditional psychosis-related diagnoses offers one of the most comprehensive mappings of impairments experienced within PSD to brain features to date.

– Cross-validation analyses and use of various datasets (diagnostic replication, pharmacological neuroimaging) is extremely impressive, well motivated, and thorough. In addition the authors use a large dataset and provide "out of sample" validity.

– Medication status and dosage also accounted for.

– Similarly, the extensive examination of both univariate and multivariate neuro-behavioural solutions from a methodological viewpoint, including the testing of multiple configurations of CCA (i.e. with different parcellation granularities), offers very strong support for the selected symptom-to-neural mapping.

– The plots of the obtained PC axes compared to those of standard clinical symptom aggregate scales provide a really elegant illustration of the differences and demonstrate clearly the value of data-driven symptom reduction over conventional categories

- The comparison of the obtained neuro-behavioural map for the "Psychosis configuration" symptom dimension to both pharmacological neuroimaging and neural gene expression maps highlights direct possible links with both underlying disorder mechanisms and possible avenues for treatment development and application.

- The authors' explicit investigation of whether PSD and healthy controls share a major portion of neural variance (possibly present across all people) has strong implications for future brain-behaviour mapping studies, and provides a starting point for narrowing the neural feature space to just the subset of features showing symptom-relevant variance in PSD

Critiques:

– Overall I found the paper very hard to read. There are abbreviation everywhere for every concept that is introduced. The paper is methods heavy (which I am not opposed to and quite like). It is clear that the authors took a lot of care in thinking about the methods that were chosen. That said, I think that the organization would benefit from a more traditional Intro, Methods, Results, and Discussion formatting so that it would be easier to parse the Results. The figures are extremely dense and there are often terms that are coined or used that are not or poorly defined.

– One thing I found conceptually difficult is the explicit comparison to the work in the Xia paper from the Satterthwaite group. Is this a fair comparison? The sample is extremely different as it is non clinical and comes from the general population. Can it be suggested that the groups that are clinically defined here are comparable? Is this an appropriate comparison and standard to make. To suggest that the work in that paper is not reproducible is flawed in this light.

– Why was PCA selected for the analysis rather than ICA? Authors mention that PCA enables the discovery of orthogonal symptom dimensions, but don't elaborate on why this is expected to better capture behavioural variation within PSD compared to non-orthogonal dimensions. Given that symptom and/or cognitive items in conventional assessments are likely to be correlated in one way or another, allowing correlations to be present in the low-rank behavioural solution may better represent the original clinical profiles and drive more accurate brain-behaviour mapping. Moreover, as alluded to in the Discussion, employing an oblique rotation in the identification of dimensionality-reduced symptom axes may have actually resulted in a brain-behaviour space that is more generalizable to other psychiatric spectra. Why not use something more relevant to symptom/behaviour data like a factor analysis?

– The gene expression mapping section lacks some justification for why the 7 genes of interest were specifically chosen from among the numerous serotonin and GABA receptors and interneuron markers (relevant for PSD) available in the AHBA. Brief reference to the believed significance of the chosen genes in psychosis pathology would have helped to contextualize the observed relationship with the neuro-behavioural map.

– What the identified univariate neuro-behavioural mapping for PC3 ("psychosis configuration") actually means from an empirical or brain network perspective is not really ever discussed in detail. E.g., in Results, "a high positive PC3 score was associated with both reduced GBC across insular and superior dorsal cingulate cortices, thalamus, and anterior cerebellum and elevated GBC across precuneus, medial prefrontal, inferior parietal, superior temporal cortices and posterior lateral cerebellum." While the meaning and calculation of GBC can be gleaned from the Methods, a direct interpretation of the neuro-behavioural results in terms of the types of symptoms contributing to PC3 and relative hyper-/hypo-connectivity of the DMN compared to e.g. healthy controls could facilitate easier comparisons with the findings of past studies (since GBC does not seem to be a very commonly-used measure in the psychosis fMRI literature). Also important since GBC is a summary measure of the average connectivity of a region, and doesn't provide any specificity in terms of which regions in particular are more or less connected within a functional network (an inherent limitation of this measure which warrants further attention).

– Possibly a nitpick, but while the inclusion of cognitive measures for PSD individuals is a main (self-)selling point of the paper, there's very limited focus on the "Cognitive functioning" component (PC2) of the PCA solution. Examining Figure S8K, the GBC map for this cognitive component seems almost to be the inverse for that of the "Psychosis configuration" component (PC3) focused on in the rest of the paper. Since PC3 does not seem to have high loadings from any of the cognitive items, but it is known that psychosis spectrum individuals tend to exhibit cognitive deficits which also have strong predictive power for illness trajectory, some discussion of how multiple univariate neuro-behavioural features could feasibly be used in conjunction with one another could have been really interesting.

Another nitpick, but the Y axes of Figure 8C-E are not consistent, which causes some of the lines of best fit to be a bit misleading (e.g. GABRA1 appears to have a more strongly positive gene-PC relationship than HTR1E, when in reality the opposite is true.)

– The authors explain the apparent low reproducibility of their multivariate PSD neuro-behavioural solution using the argument that many psychiatric neuroimaging datasets are too small for multivariate analyses to be sufficiently powered. Applying an existing multivariate power analysis to their own data as empirical support for this idea would have made it even more compelling. The following paper suggests guidelines for sample sizes required for CCA/PLS as well as a multivariate calculator: Helmer et al., (2020). On stability of Canonical Correlation Analysis and Partial Least Squares with application to brain-behavior associations (p. 2020.08.25.265546). https://doi.org/10.1101/2020.08.25.265546

– Given the relatively even distribution of males and females in the dataset, some examination of sex effects on symptom dimension loadings or neuro-behavioural maps would have been interesting (other demographic characteristics like age and SES are summarized for subjects but also not investigated). I think this is a missed opportunity.
