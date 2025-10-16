# Peer review - Round 1

Editors:
- Tali Kimchi, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59161.sa1](https://doi.org/10.7554/eLife.59161.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors developed a new software ("VocalMat") to automatically detect and classify mouse ultrasonic vocalizations into distinct categories. The software is based on tools of image processing and neural network classification of spectrograms, that is useful to analyze large dataset of pup and adult USVs in various mouse models and experimental designs. All the datasets collected and the software source codes are freely accessible.

Decision letter after peer review:

Thank you for submitting your article "Analysis of ultrasonic vocalizations from mice using computer vision and machine learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Andrew King as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This manuscript presents new tool to detect and classify mice ultrasonic vocalizations (USVs). The tool ( VocalMat) applies neural network technology for categorization of the various USVs to predetermined categories of pup calls. The paper in the form submitted seems to fit more as a methodology paper. Indeed, the authors state that the goal of their work is to: "create a tool with high accuracy for USV detection that allows for the flexible use of any classification method."

The paper is well written and presents a useful tool to identify and classify USVs of mice. However, the reviewers think that the authors did not provide enough supporting evidence to claim that their method is significantly superior to other tools in the literature that attempted USV classification. For example Vogel et al. (2019) [https://doi.org/10.1038/s41598-019-44221-3], reported very similar (85%) accuracy using more mainstream ML approaches than attempted in this study with CNNs.

Moreover, some of the reviewers were not convinced that the comparison to other tools was conducted in an unbiased and completely fair manner and that the approach described in this paper really represents a significant advantage over other tools. For example, two reviewers claim that the authors used DeepSqueak on their dataset without properly training it for this type of data, while their tool is specifically trained for it. Also, the reviewers expect to see a confusion matrix to assess model performance and establish whether the model does indeed replicate accurately classes (or how skewed it is with dominating classes).

Overall, all the reviewers agree that they would like to see a more rigorous attempt to validate the findings presented (ideally also on an external database) and proper (unbiased) comparison with other similar software, to justify the claim that VocalMat performance in classification of USVs is indeed superior and novel to the methods already in use.

If the authors wish to have the manuscript considered as a research paper and not in the form of methods paper they should change the focus of the paper and provide more data showing a novel biological application of their pup calls classification findings. If not, we will be happy to consider a suitably revised version of the manuscript for the Tools and Resources section of eLife.

For your convenience the detailed comments of the 3 reviewers are included below.

Reviewer #1:

In the manuscript entitled "Analysis of ultrasonic vocalizations from mice using computer vision and machine learning", Fonseca at al. present a novel computational tool for analysis of mice ultrasonic vocalizations (USVs). This tool aims to (1) detect USV candidates from audio clips; (2) separate the USVs from the noise; (3) apply neural network technology for categorization of the various USVs to predetermined categories; They use this tool to analyze a large dataset of pup calls and validate their tool as well as compare it with other computational tools published in the last decade. Finally, they show how they can use diffusion maps and manifold alignment to distinguish between calls of distinct groups of pups.

This tool is nice, but rather limited in its abilities and do not represent a conceptual or technical breakthrough. As for limitations, the tool presented here is designed, trained and validated for a specific type of murine calls (pup calls) and a predefined set of 11 categories, which may not cover all possible categories. As for technical advancement, the software combines criteria-based detection with neural network classification, similarly to previously published tools mentioned by the authors. Moreover, although the authors claim superiority of their software over published tools, I wasn't convinced that this comparison was conducted in an unbiased and completely fair manner and that their tool really represents a significant advantage on other tools. For example, they used DeepSqueak on their dataset without properly training it for this type of data, while their tool is specifically trained for it. Moreover, the success rates the authors report for other tools here are significantly lower than those reported by the relevant publications, and do not fit comparisons made by others. Also, I wasn't convinced that the software presented here will be working just as well as the authors claim on a distinct set of data coming from another lab and recorded in distinct conditions. My attempt to activate the software failed due to an error.

Reviewer #2:

Nice study overall, well-articulated and easy to follow. I also highly commend the authors for making all data + source code available.

1. The goal of the study could be encompassing a wider aim. The authors state: "Our goal was to create a tool with high accuracy for USV detection that allows for the flexible use of any classification method." The task of USV detection is relatively simple (no surprise the authors get 98% accuracy), it is the accurate classification of the USV types that is of particular importance. I would suggest the authors rephrase to emphasize that aspect.

2. "The output of the vocal classification provides the additional benefit of a probability distribution of vocal classes, allowing for the use of nonlinear dimensionality reduction techniques to analyze the vocal repertoire". Probably this needs some rephrasing into something like 'the output of the classifier enables the exploration of the probabilistic class membership'. More importantly though, that is not a pre-requisite for any dimensionality reduction techniques (linear or not). Dimensionality reduction could be directly applied to the extracted features, it is not dependent upon the classifier outputs.

3. "A linear regression analysis between manually validated data from different audio files and the true positives of the CNN revealed an almost-perfect linearity.…" I would expect to see a simple confusion matrix here assessing whether each of the USVs was correctly detected, rather than quantifying the number of USVs within each phonation (in which case indeed the methodology attempted by the authors would be appropriate). I think it is far more useful to assess on a case by case basis the USVs, and potentially determine whether e.g. one or more of the raw files was challenging for any reason. The authors could provide multiple confusion matrices 11x11 e.g. as a Supplementary Excel file.

4. "In order to evaluate the performance of VocalMat in detecting USVs compared to other published tools, we analyzed the same test dataset…" The authors' tool has an unfair advantage in this case, in that their algorithm was trained on the data collected under identical conditions like the test data. Moreover, the test data contains USVs from the same mouse.

5. "In summary, VocalMat is a new tool to detect and classify mouse USVs with superior sensitivity and accuracy while keeping all the relevant spectral features…" It is not clear if the authors mean superior to other studies in the literature that attempted USV classification. For example Vogel et al. (2019) [https://doi.org/10.1038/s41598-019-44221-3], reported very similar (85%) accuracy using more mainstream ML approaches than attempted in this study with CNNs.

6. If I understand correctly the methodology the authors used uses a single split of the data into training and testing, and data from a mouse could end up in both; thus the authors do not necessarily prove that their methods generalize well in new datasets. I would welcome the use of e.g. leave-one-mouse out assessment, and also the use of an additional external dataset collected under perhaps slightly different lab conditions (different lab) to see how well findings generalize. CNNs are extremely sensitive, and theoretical work has shown that adding imperceptible (visually) noise in images results in complete different results.

Reviewer #3:

The technical details should be better explained, with formulas and / or algorithm descriptions in one piece (not separated in main part and methods).

– Could you do a sensitivity analysis on their model for different number of observations?

– What is the efficiency of the method?

– Some state-of the art comparisons are missing: Did you compare it to the Automatic Mouse Ultrasound Detector? To DeepSqueak for classification? (This was only used for detection right?)

– What are the number of mice and number of records per mouse? How did you get them to vocalize?

– You have only used recordings of pups (5-15 d old). Do the results apply to adult mice?

– You used recordings of 5 strains of lab mice. Did you test or control for strain differences?

– There are many classifications that have been proposed, and so what was the basis for your syllable type classification? Can you please explain / motivate that more? Can mice discriminate these syllable types?

– How do you deal with the general machine learning problem that no insights are provided into the features that the model uses to classify syllable types ?

Is this method useful for recordings with a noisy background? Is there any reason to suspect that it might not work?

page1

The comments on the Abstract

"…detected more than >98% of the USVs" – What is the ground truth?

page 2

"…high accuracy for USV detection that" – What is the ground truth? Please mention here.

"…allows for the flexible use of any classification method." – What does that mean? /

"…USVs, outperforming previous tools" – Where is this shown? Where is the comparison on the same dataset?

…a highly accurate software to detect and.." – Mention that this is a supervised approach.

"…spectrogram is then analyzed in terms of its time-frequency plane,.." – What do you mean? The spectogram is already in the TF plan.

"…harmonic components (Figure 1D)" – To support reproducible research and open science, please provide the algorithm to the reader. In an open science approach provide the scripts (and data) to reproduce the tables and figures, where possible.

page 3

"…we manually inspected the spectrograms and labeled.." – Who is "we"? Experts on USVs? The authors? Did you listen to the resampled USVs? What is the inter-human detection rate? So what is the difference between experts? How did you select the test data?

"…the manual counting (4,441..)" – So a lot of FPs, right? Please report all the FPS and Fns.

"… artifacts of the segmentation process" – Where does this come from?

page 5

"…) to the sum over.." – Why the sum?

"…) to the sum over.." whole paragraph – Please represent your results in a figure or table! This is very tough to read and digest.…..

"Therefore, based on these results, we used the calculated inflection.." – Do I understand it right, that you criticize previous work because they required users to manually determine thresholds, but do the same for different parts of your model? For example with the inflection point.

"..In the test dataset," – How does the 14,5% FP rate compare to the one stated above?

"..In the test dataset," – which 7 USVS? out of 13 missing USVs?

"…compared the score for the label "noise"" – the linear regression between what?

"…suggesting high accuracy of VocalMat" – So about 4% of USVs are labeled as noise, right?

"…The rate of detected noise labeled as USV (false positive) was 5.60" – 42 out of 750 FPs, are falsely labeled as USVs, this probably should be mentioned in the abstract.

"Finally, the rate of USVs not detected (missed rate) was 0.28 Â{plus minus} 0.09% (mean Â{plus minus} SEM; median = 0.23; 95% CI [0.05, 0.51])." delete all this – "USVs not detected.." should not be discussed here. It is not related to classification problem and it is already discussed in section 2.2.

"identify approximately 1 in 75" – "identify approximately 1 in 71" – TNR and FPR are complementary so reporting one is enough. And 1 of 18 noises remains in the data.

"Characteristics of mislabeled USV candidates by VocalMat" – this paragraph does not give additional information, in my oppinion.

page 6

"(Table S1)." – Please add "in the appendix"

whole paragraph – Again a very ugly layout.. Why not put tables here, for example.

Why did you not try other pre-trained networks of DSQ for detection?

Your training data is highly imbalanced in classes U, C3, C and step down. Please discuss!

page 7

first paragraph – Again: Please do a graph or table!

"we manually inspected the spectrogram of the sample.." – Why? Do the same on the existing data set?

"We compared all four experimental conditions against each other and visually.." – Please compare to a SVM clustering.

" Since we did not train DeepSqueak with our.." – True, but your model also requires adaptation, so please argue why this is still a fair comparison.

"..when compared to DeepSqueak." – What about false positives?

"Detection of harmonic components" – Why did you report the detection rate for harmonics separately?

"..method to analyze the vocal repertoire of mice." – Which classes are grouped in a same class?

"The difference between the two groups was that in the treatment group,.." – Why did you not compare classification results? But used used diffusion maps instead?.

page 9

"…study that reported the sensitivity to.." – What about specificity?

"..This characteristic provides the possibility for unique.." – How feasible is it to use classifier for other vocal types?

page 10

"..a euclidean space.." – "..an Euclidean space.." – Is the caption of Figure 5 further explained in text?

page 11

(1) – give a reference, please! Which implementation did you use?

"Normalization and contrast enhancement" – Where significant parts cut out in the TF plane?

(3) – Add a reference, please.

"adjusted image" – What is considered one image? This means what regions was used to find Lin and Hic?

"We used a high pass filter (45 kHz) to eliminate sources of noise in the audible.." – Is not 45 kHz a very high threshold?

"..contrast adjustment.." – What is the adjusted image exactely?

".. If the value of the current pixel i" – What is t?

page 12

"..it was empirically chosen as t = 0.2 for our application. " – This contradicts the claim in the introduction, no?

"segments" – The super-windows?

rest of the paragraph – Please provide details how exactly?

"Local Median Filter" – Please define what a segment is!

First two sentence – What do you mean? Unclear! Where does the segmentation noise come from?

" of the pixels in a window that contains.." – Unclear, please provide details!

".file (now referred to as \Upsilon)." – What is this? Where is the starting point?Is it the whole segment? The frequency curve? A binary spectrogram?

"local parametric equations" – Why? Please motivate!

(9) What do you mean by that? What is the structure of \Upsilon'?

"..it was empirically chosen as t = 0.2 for our application. " – Why and how?

"The inflection point is then determined as the point with maximum.." – How is the maximum curvature calculated? This is again a manual set value, right?

Is tau calculated for each audio file separately? Why or why not?

page 13

"Our training dataset consisted of.." – This makes the classification task easier, right? Is this fair?

page 14

Table 1 – Please explain!

Table2 – This is clear, no?

"set (90%) and a validation.." – How? randomly?

" Diffusion maps for output visualization " – What do you mean here?

.."USVs as a distribution of probabilities.." – Really? This is explained in the following, right?

"..clustering of USVs.." – Explain (or put it later after definitions!) Visualization or clustering?

"Euclidean manifold" – Of which dimension? What do you mean? R11 is also Euliclidean!

"bandwith" – of what?

"..of the same label." – How? Maximum intra-cluster distance?

page 15

".."Euclidean space.." – What is this space? R2?

"s idea of moving from node to node" – How? Provide details?

(14) What is ei? ej? Please define!

"d through SVD decomposition" – "d through a SVD decomposition"

"Ms = D1/" – "Ms : = D1/" (to make clear this is a defintion.)

"..sake of notation, consider:" – "sake of notation, consider (for a unitary \Omega)"

(16), (17), (18) – This is not new, so give a reference, please.

"manifolds, we considered this a transfer learning problem" – Explain, please!

"Ls" and "Ld" – please give formal definitions.

Notation has to be clarified, keep fixed and precisely defined

page 16

(19) – In this setting n and d are constant, right? Please discuss!

"…n topology preservation (µ > 1)." – Please either use more or less details. Either put a reference and don't explain, or explain in more details.

"… Nf=∑i=1Ddi" – Why? Motivate!"common space F" – Which space? Is this defined?

"f the samples in order to predict the other half" – Here? Like above?

So the separation is not 90:10?

Is "n" defined?

page 17

"…and Prism 8.0 were used to…" – References, please!

"edited" – In how far? Please explain in full details, how you changed each figure!

"Data were first subjected" – Which data?

"Shapiro-Wilk" – Please add a reference!

"When homogeneity was a" – Was this assumed here or not? Please stat that preciesly.

"critical data collection and insights" – Why those lab members not co-authors?

page 18

"shows an interval of 10 ms." – Nice clarification, but formulate in text as precise formula, please

page 20

Can you please give a summary table of comparison with other approaches?

page 21

[4] [5] – format all references in the same way, please! E.g first names!
