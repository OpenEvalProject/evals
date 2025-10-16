# Peer review - Round 1

Editors:
- Jessica Dubois, https://ror.org/05f82e368 Inserm Unité NeuroDiderot, Université Paris Cité France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80878.sa0](https://doi.org/10.7554/eLife.80878.sa0)

Presenting important findings, this study describes the development of the functional brain connectome in human fetuses and neonates through the application of a novel deep learning approach: adult trained variational autoencoder. The methodology, analyses, and evidence provided are convincing and pave the way for future studies on non-linear models of brain network maturation. This work is of potential neuroscientific and methodological interest to researchers studying functional resting-state networks and brain development, as well as to deep learning scientists.


---

# Peer review - Round 1

Editors:
- Jessica Dubois, https://ror.org/05f82e368 Inserm Unité NeuroDiderot, Université Paris Cité France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80878.sa1](https://doi.org/10.7554/eLife.80878.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Towards A More Informative Representation of the Fetal-Neonatal Brain Connectome using Variational Autoencoder" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Floris de Lange as the Senior Editor. The following individual involved in the review of your submission have agreed to reveal their identity: Yong He (Reviewer #1); Andrea Gondova (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

As detailed in their individual reviews, all three reviewers acknowledged the potential insights from this study and provided several valuable comments on it. Among them, we identified essential revisions that should be carefully considered so that the study can be suitable for publication in eLife.

1. Importantly, the current manuscript indicates that this approach captures non-linear patterns of development in fetuses, neonates, and infants, but there appears to be no analysis or results to support this claim. Without this aspect, the study lacks multidisciplinary interest. Furthermore, the biological and developmental significance of the brain states and networks revealed by the VAE approach with respect to functional systems needs to be better explored and compared to other methods. Besides, the current approach did not include subcortical structures that are known to play a key role in the development of functional networks (e.g. transient developmental layers like the subplate, the thalami), which requires further analysis or discussion.

2. The potential of the whole approach to describe the emergence and development of functional connectivity needs to be tempered as the use of a VAE model trained on adult data is based on the strong assumption that connectome features are rather similar/stable across ages. Therefore, it cannot reveal structures/networks that would be strongly different (e.g. present at early stages but not in the adult brain). The smoothing effects inherent in VAE also make the method relatively insensitive to the fine granularity of developing networks. In addition, volume registration may be less effective than surface alignment given the intense growth and increased folding over this age range.

3. The performance of the reconstruction might be driven by several factors other than functional information and maturation, most of which are also age-dependent: brain size and folding (in relation to registration issue), head motion (especially within the womb), acquisition settings (in fetuses vs. neonates), scan duration, processing pipeline, etc. In addition, differences in preprocessing between the two datasets (dHCP vs. DBI) could explain part of the differences in reconstruction, prediction, and mapping findings. It is important to disentangle the effects of potential confounding factors from the developmental mechanisms to consolidate the current findings and interpretation.

Reviewer #1 (Recommendations for the authors):

There are some vague expressions and potential methodological biases throughout the manuscript, which should be further addressed prior to publication.

1. The authors emphasized representing the non-linear maturation of brain functional maps from fetal to neonatal stage by their methods throughout the manuscript. But they failed to interpret the contribution of the proposed approach for capturing this non-linear development. Their model is pre-trained by adult data. The non-linear effect of variational autoencoder refers to the non-linear combination of representing fMRI signals between brain vertexes at the individual level. The age prediction is performed using the SVM model. None of these is directly related to non-linear development. Which result and analysis support this hypothesis?

2. Some potential biases in the comparison with linear ICA methods in age prediction analysis should be further evaluated. First, the number of latent variables and the number of ICA components should be kept the same during the comparison. Second, the effect of individual functional mapping on the baby brain should be taken into account.

3. The advantages of the VAE approach in generating brain functional networks at the system level are not exhibited. Do their methods find more meaningful functional systems than previous studies? This should be well evaluated.

Reviewer #2 (Recommendations for the authors):

The paper is a very interesting application of the VAE method to the early brain. This represents an important amount of work that went into the analysis and presentation of the results. The work is easy to navigate and clearly written (some small problems are detailed below), although the supplementary information cited within the text was not made available. The figures are of good quality and clear to interpret.

• Both data sets have a fairly large range of PMA at scan (in DBI for foetuses from 20w GA). Fast and large-scale changes are taking place within the developing brain in this period which might affect the data processing pipeline at all stages. Please include more details if any quality checks were performed. E.g.:

– Any rsfMRI QC for dHCP data;

– For dHCP, babies were included independently of their radiological scores -> this might have a significant impact on the reconstructed functional data;

– How good was the projection to cortical space? (Authors use 40w template, there is a large temporal distance for some babies – there might be errors distributed non-randomly and based on ages);

– Geometric reformatting – errors with inflation, 3D->2D?, if, are those distributed randomly (unlikely);

– During dHCP data description authors say 'The additional step of voxel-wise detrending, bandpass filtering and voxel-vise normalization' after volume-to-surface mapping. Were these steps applied to DBI set as well?

– Overall, more detail on the processing pipeline(s) would be useful with details on possible differences between datasets and focus on limitations that stem from it on the interpretation of results.

• It would be useful to perform additional data analysis between the two datasets before there are forwarded to the VAE – is there a significant difference between datasets that are due to the pre-processing? Could these explain differences in reconstruction, predictive, and mapping differences?

• It would be very useful to focus on the performance of the VAE compared to adults given the method was developed and validated in adults and most of the novelty comes from its re-application to infants. Please, detail how the reconstruction compares in DBI, dHCP vs adults. It would be good to think about other interpretations for this difference on top of the neurodevelopmental stage (approximated by PMA at scan)- brain size, projection to the template, geometric reformatting to 192x192 array.

• Correlation of reconstruction error with PMA at scan (Figure 3).

– Figure 3B: It would be good to incorporate more detail on the 3 outlier points in DBI dataset – why does it fail so much – do these kids happen to have low quality recording? Or maybe injury that makes the model fail? Understanding why it fails might give informative cues on what the model is actually trying to represent.

– Also, the 3 outlier points in DBI dataset are in the 'normal' cloud in dHCP dataset, please discuss why the reconstruction might be so different between DBI and dHCP datasets

– Please show reconstruction with age for the foetal data. Discuss more why this negative correlation – it can be smoothing, differences in processing, but also movement etc. – in any case, these points make us expect the relationship to be weaker but not to be strong and in the reverse direction, comment more on the foetal processing pipeline

– You are taking head motion into account between sessions – however there might be a relationship between motion and age => it would be good to re-run the same analysis as in reconstruction vs age but with motion

– It would be interesting to see the same comparison for the ICA – e.g. what are the correlations for the second best method IC300? Is that capturing more age/individual signature/noise? If the difference is significant would be a supporting argument for improvement using VAE.

• In the age prediction methods, please indicate final feature set sizes after feature selection to give an idea of what proportion of the latent space might be representing age information, what is the interpretation for the features not associated with age? (if individual signature, could you look into the predictive power of the latent vector to identify the individual in the future?)

• Regarding comments on summing the significantly correlated features (again specify how many) 'to make model more robust against different recording specifications' and then L203: 'age prediction in the dHCP dataset was better than in the DBI dataset, this is likely due to the shorter scan duration' => this makes if for an unfair comparison, in the summing – the latent space is collapsed into one feature which will necessarily remove information, additionally, the reconstruction of the DBI data (specifically foetuses) showed strange relationship with age. Moreover, the processing was different (with its own difficulties for foetuses). There are more limitations other than shorter scan durations involved, please discuss these

• Please detail how the prediction fares on neonates vs foetuses in light of reconstruction with age relationships being very different

• L278 makes it sound the evaluation was made at the age group level separately, this is not the case but would be useful. Overall, it would be beneficial to first restrict the analysis to a narrow age range, for example, the term-equivalent age with the homogeneous data acquisition settings and processing steps to validate the application to dissociate whether the results really do capture the variation within the functional connectome rather than all the other potential confounders.

• L250: does it make sense the author found precursor of the default mode network in DBI and not in dHCP given the DBI subjects are generally younger than dHCP and thus further from the cited young adults rsfMRI studies?

• L254-256: shorter data length is only one of the potential interpretations, another alternative (among others) might be that the maps are not reliable and mostly representing the noise in the data. In the discussion it would be good to go deeper into differences between the networks between the datasets and age groups and whether these make sense in light of the expectations. Can we expect to find the same FBNs across the lifespan? Are the ones identified early on less complex/ordered, or involving primary networks rather than associative ones?

• L263: 'least pattern similarity was observed between preterm neonates and fetuses in the DBI dataset'. This is interesting – is there difference between PMA at scan between these two groups? In light of this observation, does it make sense to include preterm subjects in the age prediction models – and other interpretations (rather than keeping them separate)? Similarly, does it make sense to include fetuses given differences in acquisition settings and post-processing? This brings back the earlier suggestions to initially keep the whole analysis to a narrow range of heterogeneous data to validate the method && increase the confidence that the extracted maps are 'real' rather than artefact of processing.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Towards A More Informative Representation of the Fetal-Neonatal Brain Connectome using Variational Autoencoder" for further consideration by eLife. Your revised article has been evaluated by Floris de Lange (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

We all acknowledge that your revisions have significantly improved the methodological scope of the study, but the methodology described is not new and the neurodevelopmental insights still seem insufficient given the scope of eLife. The potential for a future study is mentioned, but it is such beginnings of evidence that we would like to read in this manuscript. This being said, we would like to offer you a new revision if you believe you'll be able to put more emphasis on some neurodevelopmental findings. Here is a suggestion of analysis that would seem relevant to us.

As we expect that distinct functional networks might evolve differently with development, you might consider different groups of neonates according to age (not fetuses for which results are less clear), highlight between-groups differences in the estimated weights of latent features derived within the autoencoder, and provide a characterization of the latent features showing the highest contribution differences in relation to age (it would be helpful to somehow relate these features to functional networks that can be visualized in terms of brain spatial topography). In our opinion, such analysis would provide some insights on the functional features and networks that show dramatic changes during this developmental period, although such features are derived from the adult brain.

If you are not convinced by this suggestion, please propose another analysis that you think would be more relevant to show some insights on the developing functional connectivity from your methodology.

It would also be very welcome to emphasize that a future study should provide a new training procedure in babies and integrate sub-cortical structures, in order to highlight features potentially present in the developing brain but not in the adult brain.

Finally, we would like to stress that multiple rounds of revisions are not usual in eLife, thus we hope that you will be able to provide a new manuscript fitting with our expectations. Otherwise, we would advise you to submit your work to another journal with more focus on methods.

Reviewer #2 (Recommendations for the authors):

We would like to commend authors for the amount of additional work performed in response to the initial round of reviews. Despite the incorporation of additional analyses and methodological details, the manuscript remained clear and informative, with the same high quality of presentation, analysis, and figures. Additionally, we were pleased to hear about the plans for future work in this interesting area (e.g. further evaluation latent representations' content and their usefulness for the individual identification).

Few additional comments and reflections incited by the revised manuscript and authors' replies are detailed below with hope they might be helpful for their future work.

1. Adult to neonate: how to interpret the resulting networks?

On Page 5 of the response to comments file, the authors bring up an important point regarding the adult lense through which the community tends to analyse early connectomes. As mentioned by the authors, this issue is shared by the majority of papers within this space and we believe it would be useful to discuss this topic explicitly in regards to the limitations it creates for the interpretation of results. With such a point of view, do the authors envisage the latent representations derived from the infant data to be 'real' features of the functional connectome at a given time point ('in-themselves') or rather 'dissimilarities/distances' to the adult network ('in-relation-to' the training data)?

In both of these cases, the latent representations will be practically useful, and outcompete non-linear models, with a high potential for improving the age, individual, and possibly atypical development prediction. However, the interpretation shift – VAE deriving features relevant to age prediction (supported by improved age prediction) to features relevant to brain development (suggested on Page 16 of the response to comments) – might be difficult to make until the deeper understanding of the content of derived latent representations is reached. Comparing the 30 networks derived from the models finetuned to different age ranges (as suggested by the authors) could be very interesting to shed more light on the developmental dynamism and this question. Until then, more caution might be warranted in the current setting when incorporating concepts like 'longitudinal' investigations (L81) or 'neonatal brain dynamics (L109).

On a slightly unrelated note, the authors then argue that 'utilizing adult rs-fcMRI at the level of the analytical model is more desirable than at the interpretation level, as there may be information from rs-fcMRI in adults that can more objectively guide the way we understand representations of neonatal rs-fcMRI'. Is this really the case? Our intuition would be that the bias introduced in one step of a pipeline is likely to be propagated in the consecutive analyses. Thus, it is difficult to see why introduction of the adult reference earlier in the research pipeline, at the level of the model, would be more desirable rather than for example on the contrary more obscuring?

[Additionally, we wonder if it would be useful to have an age prediction baseline which does not use the functional inputs at all? Would comparing the age prediction performance using basic parameters (for example head size, GA at birth to predict PMA at scan) to a model trained on VAE inputs give some additional information about the VAE representational ability vs the cohort composition effects?].

2. Radiological score and reconstruction performance

We are hesitant regarding the presentation of the lower reconstruction performance in neonates with the radiological score=5 (Page 16 of the response to comments file, and then within the manuscript L452). The radiology score of 5 describes an 'incidental finding with possible / likely significance for both clinical and imaging analysis'. Thus, it is expected (and reassuring) that the authors observed reconstruction differences between score groups as changes to the typical brain might additionally disrupt the functional networks independently of the developmental stage of the infant, i.e. make them more unlike the adults. However, these subjects will also probably suffer from a potential decreased quality of the image processing/analysis, for example due to lesions, which could confound these results. Thus, while we think it would be very interesting to further investigate the latent representations of the infants in regards to the brain injury (for example prediction model that classifies infants into subgroups based on the radiological score within the infant group of similar age), it might be difficult to understand how to dissociate the effects of age, injury, and processing quality on reconstruction and predictive performance in this group without additional discussion and quality checks (for example does the data and registration quality differ between different radiology score groups?). It might be more straightforward to focus on the observation of significant results in 'typical' groups (radiological score-1 and/or 2) as a support for potential of VAE to provide a surrogate measure of the distance of infant-to-adult activity pattern and clarify further the reasoning/caveats regarding the results in the score=5 group.

3. Foetal results

Moreover, we remain hesitant regarding the interpretation of foetal results and therefore the use of 'foetal-neonatal' outlook throughout the manuscript.

As mentioned on the L197: 'Once brain size [in foetuses] was accounted for, the negative correlation between age and reconstruction performance was reduced'. This suggests that some, but not all of this unexpected behaviour was accounted for by the head size and the ensuing ballooning effect. If we assume that the young foetuses should not be more similar to the adult cohort than the older ones in terms of the reconstruction performance, is it correct to expect additional problems remaining within the reconstruction of the foetal data?

Additionally, the statement on L40 that '[VAE led to] improved prenatal-neonatal brain maturational patterns and more accurate and stable age prediction compared to linear models' is not entirely accurate given the results presented on L280 which reports that it was cortical parcels that showed the best performance in the foetal group.

Thus, it might be difficult to conclude on L361 that 'This finding may suggest that neurodevelopment of preterm neonates and age-matched in-utero fetuses likely differ given the early extrauterine exposure in infants born prematurely, above and beyond the difference in acquisition settings and preprocessing steps between dHCP and DBI datasets.' Although we agree with the statement in itself, because of the remaining above-mentioned issues it might be difficult to use current findings as a support.

Given the remaining questions regarding the reliability of the foetal results, it is possible that this population (due to very different acquisition requirements, processing problems, large developmental distance) might benefit even more than the other groups from a foetal-specific model/pipeline (whose creation was suggested by the authors). Until then, more caution might be helpful when promoting the foetal aspects of the study.

Reviewer #3 (Recommendations for the authors):

The authors have provided very comprehensive responses to the comments and have largely addressed things appropriately by changing the wording in the manuscript itself.

Although they do a good and compelling job showing that the VAE method is seemingly outperforming other methods (in this case ICA), I have to confess I still struggle somewhat with the insight that can be drawn from this work – apart from the "potential" of the method to study early brain development. Most prominently, the "non-linear" aspects of the method are heavily emphasised in the manuscript – which for characterising brain development would of course be a major benefit which would be unique to this method. However, as it stands, the authors concede that developmental trajectories have not been explored and it could be done in later work. Rather than suggesting there is "potential for this" however, I suspect a reader would want evidence that this method can definitely provide this kind of novel insight to conclude whether it is truly characterising biological effects and/or is worthwhile?

This issue about demonstrating whether this method is truly a specific tool that can provide new insights about brain development are also relevant for 2 other unresolved issues – which would be key to differentiate if this is just a paper showing that a method can be used on fetal/neonatal data or if it is a method that is specifically worthwhile using on these populations. These are again are conceded by the authors but again readers I suspect, may want answered. However, I fully appreciate that these cannot be easily resolved. These issues revolve around the use of the adult training data which means: that (i) the subcortical structures cannot be included – these structures one might argue are even more important in fetuses than the cortex? and (ii) the distinction between "model generation (VAE) and interpretation (ICA)" becomes important. The authors here argue that generation is more desirable than interpretation – although I would personally argue the other way, as interpretation means that anything can be identified but can then be explored (as opposed to generation, where it would not be identified in the first place?). Age effects using ICA networks for example can be easily studied using a method like dual regression. It would be nice to see what would happen if a neonatal data set for example was used for training – but failing that I think it would benefit the reader if this specific issue is explicitly discussed in the same way as in their response?
