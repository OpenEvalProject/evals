# Peer review - Round 1

Editors:
- Frank L van de Veerdonk, Radboud University Medical Center Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58227.sa1](https://doi.org/10.7554/eLife.58227.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The concept of using EHR system and machine learning in COVID and finding anosmia as a specific clinical sign without a specific trigger for doctors to ask this sign is a very nice example of this system to help filter out new signatures in new or old diseases. The manuscript shows how to use big data to elucidate relevant clinical clues in practice.

Decision letter after peer review:

Thank you for submitting your article "Augmented Curation of Unstructured Notes from a Massive EHR System Reveals the Signature of Impending COVID-19 Diagnosis" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jos van der Meer as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that it needs revision before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). We are offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The manuscript provides a deep neural networks study over an institution wide EHR platform for the augmented curation of 15.8 million clinical notes from 30,494 patients subjected to COVID-19 PCR testing during the SARS-CoV2 pandemic. The studies focused on potential earlier diagnosis of COVID-19 by identifying specific gastro-intestinal, respiratory, and sensory phenotypes, as well as some of their specific combinations. Overall, the research question is interesting, and would contribute to the understanding of COVID-19 early diagnosis. This part of the manuscript is strong and justifies its publication.

However, the manuscript overall needs some reorganization, as there are sections from the Materials and methods and Discussion that belong in the Results, and the overall details about the data, methodology and discussion need better clarity and expansion.

The data on RNAseq and treatment strategies (Figure 1 and 2) do not belong in the context of this paper.

Essential revisions:

1) The cohort itself is not well-defined and should be better described (see below).

2) Materials and methods section should be written more clearly (see below).

3) Remove RNA seq data and treatment figures and discussion about these topics. It is distractive and does not make the manuscript stronger.

Cohort description:

How many patients had an admission 7 days before getting a swab taken? How many individuals do the authors have a full week of information on prior to the PCR? Why was there a delay in PCR testing of these patients? Who are the 30,000 patients, and why were they admitted to a hospital? Or were they outpatients? The setting and patient population needs to be described. Completely basic information like sex and age are missing. The authors report that they use 15.8 million clinical notes from 30,494 patients, so about 500 notes/patient. Are these from the 7-day period, so more than 70 notes written per day? Or from a longer non-disclosed time-span?

Materials and methods section:

In this study patients are analyzed until date of diagnosis (test), it seems to be an analysis of when in the natural course one chooses to test? As it is formulated in the manuscript, "temporal patterns" first of all indicate, that the population converge towards day of test, so patients "progress towards same phenotype" and it is unclear how this relates to COVID-19 progression? What is the link between the analysis and the references to chloroquine/hydroxychloroquine?

The presentation in Materials and methods, also has many unclear aspects. For example, what was the output from also curating disease and medication? It seems, that only symptoms are presented in the manuscript? How do symptom categories and phenotypes differ? The iteration for optimization of the model seems a little unclear and how were the 18,500 sentences in the test set selected? What was the indication for COVID-testing in these patients? Were they all hospitalized for different conditions? Were all 30,494 under suspect for COVID-19 or were some tested simply because they were hospitalized in the period of the pandemic (i.e. routine/screening test)? And what were the diagnoses of the COVIDneg cases? Where there notes on all patients from index -7 to 0 as mentioned above? What are the demographics of these patients? And were symptoms handled as chronic or temporary conditions? Why was altered or diminished sense of taste and smell (anosmia/dysgeusia) included in Results despite a classification performance of 64.4%? Not sure why there are two F scores. Why calculate F scores on sentences labeled as "not present" – how is recall not undefined in such a calculation? How were the sentences in step 2 and 3 chosen? Why is the sum of the true positive rate and the false positive rate not 100%? Confidence intervals would help the interpretation of the data. It would be great if the authors would provide number of tests or the significance level to help interpret the Benjamini-Hochberg correction.

2) The authors state that the platform utilizes state-of-the-art transformer neural networks. But they used BERT (original version) indeed. Bert is not the state-of-the-art transformer model. XLNet and RoBERTa are the state-of-the-art models. For name entity recognition of clinical note data, there have been some specific BERT-based variations or pre-trained models, such as BioBERT.

The authors did not provide details of the implementation of BERT configuration, like how many layers, heads? How they train BERT, like how many epochs? what is the optimizer setting? Did they use a pre-train (on which corpus) BERT? etc. All these details need to be provided for reduplication. My suggestion is better to provide several examples regarding what the input looks like ,i.e., the unstructured clinical notes, and corresponding structured output, so that readers can understand how powerful the model is.

3) The dataset split (90%/10%) is not usual. "70%/10%/20%" or "60%/10%/30%" are more common for fair evaluation in deep learning (the middle one represents the validation set). Could the authors provide the reason why they split dataset in this way or provide a reference that applied this strategy?

4) In the Results section, the first paragraph is about details of data collection, it would be more appropriate in part of the Materials and methods, and the final paragraph would be more appropriate in the Discussion. In Table 1, the proportion columns would be better to combine with the patients-count columns.

5) In terms of the Discussion, it would be important to emphasize and discuss the main findings. "By contrasting EHR-derived phenotypes of COVID pos (n = 635) versus COVID neg (n = 29,859) patients during the week preceding PCR testing, we identify anosmia/dysgeusia (37.4-fold), myalgia/arthralgia (2.6-fold), diarrhea (2.2-fold), fever/chills (2.1-fold), respiratory difficulty (1.9-fold), and cough (1.8-fold) as significantly amplified in COVID pos patients" This statement in the Abstract should be the key finding, but the authors did not emphasize the statistical method and make discussion properly.

6) The pairwise analysis of phenotypes considered only the combination of 2 phenotypes. How to process the combination of multiple phenotypes?

7) As the NLP-based entity recognition can bring errors, the following statistic analysis could be biased by these errors. The authors should emphasize this point. I would suggest the authors to use the manually curated data from the first 100 patients to perform the same analysis to see if it can generate the same results.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Augmented Curation of Clinical Notes from a Massive EHR System Reveals Symptoms of Impending COVID-19 Diagnosis" for consideration by eLife. Your article has again been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jos van der Meer as the Senior Editor. The reviewers have opted to remain anonymous.

You have definitely made a number of changes that have improved the readability and consistency of the manuscript. Although the paper essentially only presents already known symptoms of the disease (e.g https://doi.org/10.1136/bmj.m1996), it is now clearer that the paper aims to characterize when and how long prior to PCR-diagnosis a symptom is overrepresented.

However, one reviewer comments that there are still many inconsistencies in the manuscript that at best makes it difficult to read but also bring uncertainty about the validity of the results. Materials and methods section paragraphs are still hard to follow to the extent that the study would be hard to reproduce.

Specific comments:

1) Altered smell is as mentioned not a new finding, the authors also report this in relatively small numbers (6.3%) for covid19 patients, it seems unclear how much of an impact this would have clinically. The authors should comment on how this differs from other studies. In the context Tim Spector's work using app may also be relevant.

2) I could not follow the number of symptoms (26 or 27?) and how were these 26 or 27 selected? Who selected these and what was their backgroundsWhy not search for overrepresented symptoms in general and include way more symptoms? Currently only suspected/known symptoms were included. "Examining the other 325 possible pairwise symptom combinations" which were the first 26 for example. In Table 1, why is respiratory failure and dysuria marked in a light grey color?

3) Why is there automated entity recognition of "drugs"? Drug are not otherwise mentioned in the paper? There is still a part about scRNA-sequencing in the results, but no results about RNA-seq presented.

4) Why was the method applied to the 35 million notes? When only notes from 7 days are analyzed in the study… I don't agree with deleting information about the number of notes, it does not solve the problem from the original submission. It would be nice for the reader to be able to evaluate the number of notes or words written about the included patients. Also, how many notes are from day 0? Are notes recorded at day 0 included or not, there seems to be inconsistency here throughout the manuscript. The BERT validation seems to be done on notes including day 0, whereas the actual proportion analyses seem to be excluding day 0 which is the day one must expect to have most notes concerning covid19.

5) Many basic aspects are still unclear. How many data points could one patient contribute with? Could one patient tested multiple times contribute more than once? If a patient was tested negative and then positive, how was this handled?

6) It a considerable limitation that there is no separation between chronic and acute symptoms. If the condition is chronic it wouldn't help at all in the diagnosis, only that this population for some reason is more prone to be covid19 positive.

7) It still remains unclear why patients with obvious covid19 symptoms like "respiratory difficulty" and "fever" were not tested for sars-cov-2 earlier. It is very unlikely with patient delay from this point since the symptoms were recorded in the notes. These cases should be manually evaluated.

The method was trained on "cardiovascular, pulmonary, and metabolic diseases and phenotypes", so not gastro-intestinal? How were symptoms like diarrhea validated?

Still confusing to me that "negative sentiment classification" can have recall. I don't understand this, are there true positives in the negative classification? If so why?
