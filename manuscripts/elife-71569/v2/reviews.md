# Peer review - Round 1

Editors:
- Detlef Weigel, https://ror.org/0243gzr89 Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71569.sa0](https://doi.org/10.7554/eLife.71569.sa0)

The authors introduce non-negative matrix factorization to analyze shallow WGS sequencing data to detect cell-free DNA fragments diagnostic of cancer. This is an area of active research and the authors add a potentially very useful unsupervised approach to analyze such data.


---

# Peer review - Round 1

Editors:
- Detlef Weigel, https://ror.org/0243gzr89 Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71569.sa1](https://doi.org/10.7554/eLife.71569.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Discovering fragment length signatures of circulating tumor DNA using Non-negative Matrix Factorization" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Y M Dennis Lo as the Senior/Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Alain Thierry (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. More information on the source of cancer patient plasma, characteristics of the patients, especially in respect to treatments at time of blood sampling, should be included. A flow chart summarising the overall results might be useful.

2. The authors can consider citing some of the older work analyzing cfDNA fragment size distribution using PCR-based approaches.

3. The authors showed exactly the same illustrative fragment size profile in Figure 1 (normal and tumor signature) as those presented earlier by Sanchez et al. (JCI insight, 2021). Consequently, they should at least mention in a few sentences the observations made by Jiang et al. and by Sanchez et al. (JCI insight, 2021) in order to validate their assumption.

4. As one could argue that the signatures of cfDNA fragment length had been discovered through various previously published work, in light of the previous concerns, term 'discovery' is perhaps inappropriate. Hence, we would suggest replacing the word 'discovery' by another term such as 'detection' or 'assessment'.

5. In the introduction, it would be better to describe a bit more details about tumor DNA length characteristics that were reported previously, so that readers would have a more comprehensive understanding of what is already known in the prior art and why the analysis of tumor-specific length profile in this study is important.

6. The authors should compare whether an NMF component would give a better correlation with tumor DNA estimated by ichorCNA, compared with the short DNA proportion (i.e.% of plasma DNA < 150 bp) in the overall size profile.

7. It seems somewhat intriguing that the classification power between cases and controls improved as the number of components used in the NMF process. However, the authors did not see an improvement in the correlation between tumor DNA fraction and the weight of one component reflecting the tumor contribution. These observations should be discussed and clarified in a revised manuscript.

8. The AUC was calculated using repeated 10-fold cross-validation. It would be better to show the boxplot of AUC values for a given number of NMF components (Figure 3c).

9. It will be informative to estimate the minimum number of samples is required for performing an accurate NMF analysis.

10. The authors claim their model is directly measuring ctDNA load. Since an untargeted (unsupervised) model to assess the tumor fraction for monitoring purposes would be of great value, it would be interesting to see if changing levels of ctDNA can be captured by changing weights of the putative cancer Signature 1. Since their mCRPC cohort included patients with follow-up samples (at therapy start and progression) it is not clear why this has not been tested.

11. It should be mentioned that ichorCNA can only provide informative results at ctDNA fraction of 3% and higher. At higher tumor fractions the fragment signature signal might be relatively strong, explaining the good correlation, but what about samples with lower fractions? Please indicate the tumor fractions (median, min, max) assessed with ichorCNA and based on the VAFs of the identified mutations for all patients.

12. The authors claim that using NMF they were able to verify that the fragment length profile of the signature correlating with ctDNA levels does indeed match the length distribution of fragments containing mutations. However, although they included PBMCs in their mutation analysis the authors did not correct for clonal hematopoiesis (CH). Recent studies showed that up to 20% of identified mutation are related to CH and that such mutations are also found in driver genes for solid tumors. Since there might be a size difference of mutated fragment originating from the tumor or PBMCs, respectively, this statement is overrated. In case their sequencing approach was not sensitive enough to detected CH-related variants this should at least be mentioned.

13. In Figure 2c, the shift towards smaller fragment is only seen for the dinucelosomes peak but not for the mononucleosomal fragments. How do the authors explain this (if not by contamination of CH-related variants)?

14. The authors demonstrated that NMF was more robust when less data was available than the ichorCNA algorithm, but they lacked to provide convincing data that NMF as a quantitative measure is more sensitive with respect to tumor fraction. To this end, in silico dilution experiments where they computationally mixed healthy fragments and high ctDNA fraction sample(s) to a ctDNA fraction of their choice (with repetitions to achieve a more robust es-timation) should be performed.

15. If there are no CNA or tumor fraction >3%, ichorCNA can literally not be used to determine ctDNA fraction, so the feasibility of the dilution approach to benchmark ichorCNA is not clear to the reviewer (in particular for early-stage cases, in which most samples have tumor fractions >1%). Moreover, low depth can be overcome by additional sequencing whereas the tumor fraction cannot be enriched by more reads.

16. Using NMF the authors demonstrate that there are 2 major contributors to fragment length distribution and the addition of further signatures does not add anything. However, this statement is conflicting with results of the linear SVM classification case/control approach (Figure 3c). A plateau of classification accuracy is reached when using around 30 signatures, which suggests this would be a good trade-off for number of signatures to reach high accuracy (AUC).

17. Figure 3d: Interestingly, open chromatin is associated with a higher fraction of dinucleosomal fragments. How do the authors explain this? Figure 3: the reviewer is not sure what the authors want to show here with Pearson's correlation coefficient, this does not look like a linear relationship.

18. The paragraph on "epigenetic fragment length" could be better presented. I would re-phrase "epigenetic state". Both the DELFI ratio and the fragment length signature are surrogates for the chromatin state (open or closed). First the author talks about bin-wise extraction of two signatures. Why is it, that reducing bin size gives better classification results? ~50 kb bins seem to be best to predict ATACseq results. Is there literature that describes open/closed chromatin in this way? Then they correlate the weights from that with ATACseq results. And finally, they use their bin-wise signature extraction results/weights as input for cancer/control classification. Could be split in two parts for clarity: one that talks about correlation with ATACseq results and one that discusses classification results.

19. cfDNA fragment length profiles are particularly prone to pre-analytical (extraction, library prep) and analytical (clustering efficiency of various sequencings machines) factors. How do preanalyitcal/analytical factors affect the classification? The authors mention in the discussion that changes in the size profiles from their mCRPC cohort and the DELFI samples vary, which might be attributed due to such factors. Yet such confounding event will impact the robustness of such approaches and may prevent a widespread implementation of fragmentomics. This should be further discussed.

20. How can the authors exclude that the above-mentioned differences are attributed to higher/lower ctDNA fractions in the metastatic CRPC and the early stage DELFI samples? Even in Figure 2a it seems that samples with higher tumor fraction have more dinucleosomal fragments. Separate fragmentation profile plots for each stage should be shown; it would be interesting whether such profiles show any differences for stage I and stage II patients.

21. The authors could have checked in the DELFI cohort whether there is a (physiologic fragment length variation) between the seven cancers types? Would there always be the same two signatures coming up if the only consider one tumor type? Based on Supplementary Figure 4 this seems not to be case. In addition, there is a huge overlap of healthy individuals and cancer patients for signature 1? Please also present Supplementary Figure 4 with Signature 2. Can we really assume that this signature is the one related to cancer?

22. Abbreviations should be defined at the beginning for better readability.

23. Resolution of figures need to be improved. Comprehensive legends should also be included for Supplementary figures.

24. Matching colors for better readability are recommended.

25. Specify average read pairs for cfDNA samples and corresponding PBMCs.

26. Excel Supplementary file: Supplementary table 2 should be mentioned in the manuscript.

27. ctDNA (%) on the x-axis in Figures 2 is calculated from targeted mutation analysis, right? How was est.ctDNA % in the Supplementary figures 2&3 calculated?

28. What is the original h matrix in NMF in Figure 2f? There is a normal h matrix described as weight matrix, but I haven't seen the definition of what with "original" h matrix is meant.

29. Assumptions for linear correlation using Pearson are not mentioned, I don't know whether they are met at all. Looking at the figure it does not seem like they are met. Normality of the variables should at least be checked.

30. How is NMF performing on previously unseen data? This part is missing. The authors could have checked for overfitting in this way for example calculating the reconstruction error on a test dataset.

31. It is not clear whether cross validation was used only for the classification task or also to evaluate the NMF decomposition. Are those signatures representative?

32. It would be nice to see the position of the excluded bins based on +- 2* IQR. They already excluded the ENCODE blacklist regions. Other outliers may be real biological signal especially in some type of cancer where copy number alteration play an important role.

Reviewer #1 (Recommendations for the authors):

Renaud et al. aims at developing a new computational method based on NMF relying on the difference in the fragment size profiles of cfDNA extracted from plasma of healthy individuals and metastatic castration-resistant prostate cancer patients. The manuscript is clear and the drawings very helpful. While data are convincing, the reviewer has a few major concerns that should be necessarily addressed:

Major concerns:1. The authors generally poorly refer to the source of cancer patient plasma. Limitations of the work, especially method performance, is slightly described in particular about cancer stages, or other cancers. In addition, characteristics of the patients are missing, especially in respect to treatments at time of blood sampling. Lastly, a flow chart is missing, enabling to evaluate successful rates.

2. Citation of critical reports or issues are missing when introducing this work and placing it into the development of methods for pan cancer screening. Below are concerns that need to addressed:

– The authors are citing reports on cancer vs healthy cfDNA fragment size distribution published after 2016 years. Most of the pre-omics era studies on distinguishing cancer to healthy individuals by fragment size distribution were based on the q-PCR analysis, while this is not mentioned. The first observation was made by Mouliere et al. (PlosOne, 2011) who studied by fractional size distribution with nested Q-PCR systems "the size distribution profile of ctDNA fragments in plasma" and indicated that "the size distribution profile of ctDNA fragments can be used to discriminate between healthy and cancer patients". This team later showed that mutant fragments are shorter than wild type counterparts (Mouliere et al.; Transl.Oncol, 2013), Lo's group later confirmed this observation by showing strong but somewhat different differences in regards to size ranges Jiang et al. (PNAS, 2015) or more recently in Sun Kun et al. (Genome Res, 2019).

– Renaud et al. work as well than those cited in the manuscript such as Cristiano et al., relies on Mouliere et al. (PlosOne, 2011) first observation. Note, Cristiano et al. cited this report as well as Sanchez et al. (npgGenomic Medicine, 2018), Jiang et al., and Underhill (Plos Gen. 2015). Finally, Sanchez et al. (JCI insight, 2021) refined Mouliere et al. (2011) observation by using sWGS from double and single stranded DNA library preparations. The authors should necessarily add these citations.

– The authors showed exactly the same illustrative fragment size profile in Figure 1 (normal and tumor signature) as those presented earlier by Sanchez et al. (JCI insight, 2021). Consequently, they should at least mention in a few sentences the observations made by Jiang et al. and by Sanchez et al. (JCI insight, 2021) in order to validate their assumption.

3. In light of the previous concerns, the title should be corrected, as the term discovery is improper in regards to the study. The signatures were previously made; the method used here, solely allowed to combine fragment length markers in an optimal setting while developing a technology. This is already important since this method appears very performant, and the reviewer is impressed. Discovery should be replaced by another term such as detection or assessment.

Reviewer #2 (Recommendations for the authors):

Specific comments for authors to address:

1) In the introduction, it would be better to describe a bit more details about tumor DNA length characteristics that were reported previously such as https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1006162, https://www.pnas.org/content/112/11/E1317, https://www.pnas.org/content/115/46/E10925, https://stm.sciencemag.org/content/10/466/eaat4921.abstract, therefore the readers would have a more comprehensive understanding of what is already known in the prior art and why the analysis of tumor-specific length profile in this study is important.

2) The authors should compare whether an NMF component would give a better correlation with tumor DNA estimated by ichorCNA, compared with the short DNA proportion (i.e.% of plasma DNA < 150 bp) in the overall size profile.

3) It seems a bit confused to the reviewer that the classification power between cases and controls improved as the number of components used in the NMF process. But the authors did not see the improvement in the correlation between tumor DNA fraction and the weight of one component reflecting the tumor contribution. Such observation should be discussed and clarified.

4) The AUC was calculated using repeated 10-fold cross-validation. It would be better to show the boxplot of AUC values for a given number of NMF components (Figure 3c).

5) It will be informative to estimate the minimum number of samples is required for performing an accurate NMF analysis.

Reviewer #3 (Recommendations for the authors):

1) The authors claim their model is directly measuring ctDNA load. Since an untargeted (unsu-pervised) model to assess the tumor fraction for monitoring purposes would be of great value, it would be interesting to see if changing levels of ctDNA can be captured by changing weights of the putative cancer Signature 1. Since their mCRPC cohort included patients with follow-up samples (at therapy start and progression) it is not clear why this has not been tested.

2) It should be mentioned that ichorCNA can only provide informative results at ctDNA frac-tion of 3% and higher. At higher tumor fractions the fragment signature signal might be rel-atively strong, explaining the good correlation, but what about samples with lower frac-tions? Please indicate the tumor fractions (median, min, max) assessed with ichorCNA and based on the VAFs of the identified mutations for all patients.

3) The authors claim that using NMF they were able to verify that the fragment length profile of the signature correlating with ctDNA levels does indeed match the length distribution of fragments containing mutations. However, although they included PBMCs in their mutation analysis the authors did not correct for clonal hematopoiesis. Recent studies showed that up to 20% of identified mutation are related to CH and that such mutations are also found in driver genes for solid tumors. Since there might be a size difference of mutated fragment originating from the tumor or PBMCs, respectively, this statement is overrated. In case their sequencing approach was not sensitive enough to detected CH-related variants this should at least be mentioned.

4) In Figure 2c, the shift towards smaller fragment is only seen for the dinucelosomes peak but not for the mononucleosomal fragments. How do the authors explain this (if not by contamination of CH-related variants)?

5) The authors demonstrate that NMF was more robust when less data is available than the ichorCNA algorithm, but they lacked to provide convincing data that NMF as a quantitative measure is more sensitive with respect to tumor fraction. To this end, in silico dilution ex-periments where they computationally mix healthy fragments and high ctDNA fraction sample(s) to a ctDNA fraction of their choice (with repetitions to achieve a more robust es-timation) should be performed.

6) Also, if there are no CNA or tumor fraction >3%, ichorCNA can literally not be used to de-termine ctDNA fraction, so the feasibility of the dilution approach to benchmark ichorCNA is not clear to me (in particular for early stage cases, in which most samples have tumor fractions >1%). Moreover, low depth can be overcome by additional sequencing whereas the tumor fraction cannot be enriched by more reads.

7) Using NMF the authors demonstrate that there are 2 major contributors to fragment length distribution and the addition of further signatures does not add anything. However, this statement is conflicting with results of the linear SVM classification case/control ap-proach (Figure 3c). A plateau of classification accuracy is reached when using around 30 signatures, which suggests this would be a good trade-off for number of signatures to reach high accuracy (AUC).

8) Figure 3d: Interestingly, open chromatin is associated with a higher fraction of dinucleosomal fragments. How do the authors explain this? Figure 3: I am not sure what the authors want to show here with Pearson's correlation coefficient, this does not look like a linear relationship.

9) The paragraph on "epigenetic fragment length" could be better presented. I would rephrase "epigenetic state". Both the DELFI ratio and the fragment length signature are surrogates for the chromatin state (open or closed). First the author talks about bin-wise ex-traction of two signatures. Why is it, that reducing bin size gives better classification results? ~50 kb bins seem to be best to predict ATACseq results. Is there literature that de-scribes open/closed chromatin in this way? Then they correlate the weights from that with ATACseq results. And finally, they use their bin-wise signature extraction results/weights as input for cancer/control classification. Could be split in two parts for clarity: one that talks about correlation with ATACseq results and one that discusses classification results

10) cfDNA fragment length profiles are particularly prone to pre-analytical (extraction, library prep) and analytical (clustering efficiency of various sequencings machines) factors. How do preanalyitcal/analytical factors affect the classification? The authors mention in the discussion that changes in the size profiles from their mCRPC cohort and the DELFI samples vary, which might be attributed due to such factors. Yet such confounding event will impact the robustness of such approaches and may prevent a widespread implementation of frag-mentomics. This should be further discussed.

11) How can the authors exclude that the above-mentioned differences are attributed to high-er/lower ctDNA fractions in the metastatic CRPC and the early stage DELFI samples? Even in Figure 2a it seems that samples with higher tumor fraction have more dinucelosomal frag-ments. Separate fragmentation profile plots for each stage should be shown; it would be interesting whether such profiles show any differences for stage I and stage II patients.

12) The authors could have checked in the DELFI cohort whether there is a (physiologic fragment length variation) between the seven cancer types? Would there always be the same two signatures coming up if the only consider one tumor type? Based on Supplementary Figure 4 this seems not to be case. In addition, there is a huge overlap of healthy individuals and cancer patients for signature 1? Please also present Supplementary Figure 4 with Signature 2. Can we really assume that this signature is the one related to cancer?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Unsupervised discovery of fragment length signatures of circulating tumor DNA using Non-negative Matrix Factorization" for further consideration by eLife. Your revised article has been evaluated by Detlef Weigel (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

Essential revisions:

1. The authors partially answered to the concerns but did not add a flow chart to ease reading. In addition, they did not precise the pre-analytics such as delay between blood draw and plasma isolation, storage, centrifugation steps and speeds,… This would validate quantitative data accuracy and may influence fragment size.

2. Please replace "discovery" with "detection" in the title.

3. The authors should describe in more detail how they concluded that the NMF model can be reliably estimated (as well on which criteria) using as few as 20 samples.

4. The authors should indicate whether they have used a spiking strategy to evaluate whether their model is directly measuring ctDNA load, or whether they use another ctDNA techniques to compare. Otherwise, their evaluation is not complete, and this should be indicated in the limitations of the study in the discussion.

5. The authors answered to this concern by showing adequate data but omitting to discuss them. This is of importance since this cutoff appears as a critical limitation of the model.

6. Explanations from authors are reasonable. However, this discrepancy as well as these explanations should be inserted in the text.

7. The authors weakly addressed this concern. In particular, one of the major criticism of the Cristiano work is the selection of the healthy individuals: Are they age matched? Are they fully healthy? Are their plasma absolutely examined as those of cancer individuals? Any difference about pre-analytics or analytics between cancer types? Please discuss. Finally, please be cautious about fragment size cancer signature specificity.
