# Peer review - Round 1

Editors:
- Caroline Gutjahr, https://ror.org/02kkvpp62 Technical University of Munich Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76968.sa0](https://doi.org/10.7554/eLife.76968.sa0)

The authors present an automated system for phenotyping root system architecture based on bioluminescent roots resulting from a constitutively expressed luciferase transgene (GLO-Roots). They have developed a robotics-assisted phenotyping platform and an automated image analysis pipeline for high throughput analysis. An impressive array of 93 luciferase expressing Arabidopsis thaliana accessions provides a major resource for understanding the genetic basis for root system architecture variation under physiologically relevant conditions. The work will be of great interest to plant biologists and all those studying genetic variation in plants.


---

# Peer review - Round 1

Editors:
- Caroline Gutjahr, https://ror.org/02kkvpp62 Technical University of Munich Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76968.sa1](https://doi.org/10.7554/eLife.76968.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Uncovering natural variation in root system architecture and growth dynamics using a robotics-assisted phenomics platform" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jürgen Kleine-Vehn as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Niklas Schandry (Reviewer #1); Larry York (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

As you see from the reviewers' comments they (and myself) are excited about your manuscript, although it requires some revision and clarifications to become acceptable for eLife. Please find the reviewer comments below. We have discussed the experiment with 6 accessions (mentioned by reviewer #3) and we agree that it should stay in the manuscript but that it also causes some distraction from the main point. We suggest to more strongly focus the text on these results to better integrate them with the next chapter describing results from the full panel. Otherwise, we consider all reviewer comments to be important to improve the manuscript.

Reviewer #1 (Recommendations for the authors):

Comments on GWAS:

– I noticed that sometimes, the data cleaning procedure appears to retain pixels which are not part of the root system (e.g., Ting-1 in GWA-5; Tomegap2 in GWA-1 and GWA-5 or Dra2-1 in GWA3).

– The authors use “depth” to refer to the vertical distance covered by the overall root system, and “length” to refer to the sum of the length of all vectors that represent the root system. In the extreme case of a single main root growing straight down depth would be equal to cumulative length and depth should never be larger than cumulative length, yet there are cases where depth is larger than the total length of the root (Kz9, GWA3 and Kor3 GWA2). The length measurement in several accessions suffers from unconnected vectors, while the overall shape of the root system is probably correct (depth, width, hull). See for example accession Ge-0 GWA3, GWA5 or GWA6, where the root appears to be made up of many very short vectors with gaps. This raises the question if the length variable is suitable for quantitative genetic analysis. I also wonder how this issue affects the accuracy of the vector angles with respect to the true root system.

– Breeding values were computed for the quantitative genetic analysis. It should be clarified whether “breeding value” refers to the estimated model coefficients (p. 8), or to the fitted values (p. 54). All traits were overall using the same formula. It is not really clear why the authors opted for this approach instead of using different models for the different traits. Some traits, such as width (see Figure S5) do not display a linear relationship with time.

Average angle per day appears to extremely dynamic and I am not sure if the breeding values for this trait are meaningful with regards to the original data, raising the question if the fitted values for this trait are a good input for GWAS. Is it possible that the overall observation that p-values of some SNPs decrease over time simply reflects the linear relationship with time specified in the model, as fitted values increase over time?

What is the advantage of using fitted values at different timepoints over using the model coefficients for each accession as the input?

Since the model assumes a linear relationship, which appears to not capture the dynamics of all traits, would it not be reasonable to simply compute the trait mean per day per accession and use these values as input for GWAS, instead of using fitted values?

Reviewer #2 (Recommendations for the authors):

1. While the GLO-Bot system is using potting mix, it will still be very different from soil grown roots. With GLO-roots, the roots are grown in a thin sheet of soil (essentially restricted to 2 dimensions) and the roots will become constrained by the width of the system as well. This will most likely reduce differences between shallow rooting accessions and intermediate accessions. It will be important to discuss the constraints of the system and discuss whether any time point will be closer to a 3D soil growth environment. One way how this might be elucidated would be to look at broad sense heritability at different time points. Such an approach might also indicate an optimal timepoint for the GWAS and the correlations with environmental variables.

2. Page 8: "For each of these traits, we used a generalized linear mixed model in the R package MCMCglmm to account for replicate and block effects noises and estimate the "breeding value" of each accession for a given trait (Wilson et al. 2010; Mrode 2014); (Hadfield 2010) (Supplemental Figure 5). The denoised trait values for each genotype at 0, 48, 96, 144, 192, 240, 288, and 336 hours after the start of imaging (equivalent to 14, 16, 18, 20, 22, 24, and 28 DAS) were used for further analyses."

It remains a bit unclear what the process was (how were the block effects defined, etc.) and what the rationale was to use "breeding value". Also, most readers will not know what a "breeding value" is. Are the "denoised" trait values breeding values? Why do the authors think that the raw trait values are not helpful for further analysis (after all, many of the BSH seems reasonable)?

3. Page 9ff: The candidate gene follow up is very incomplete. For instance, the authors show in their Manhattan plots that some associations are linked to other SNPs in that region. It therefore would be good to also include genes in proximity of the linked SNPs in the table. Also, the SNPs identified with a GWAS are not necessarily the causal SNPs (in particular, this is an issue if not the full genome sequence was used for GWAS). The causal SNPs could be linked or partially linked to the GWAS SNPs (e.g. due to allelic heterogeneity). It would therefore be helpful if for the genes discussed in the text, the genomic region could be shown with haplotypes or just using the 1001 genome project SNPs in accessions with alternative GWAS SNPs.

4. Page 5: Root Angle output is unclear (also in the Suppl. Table). This is important as it is a major trait in the manuscript. Is this the average of all roots? Do all roots need to be detected for that? What are the two points that are used to measure the angles? What is a root segment? How many are considered?

5. Page 6: How many root systems were compared with SmartRoot? Is each point in Figure 2B an entire root system? Is the comparison similarly accurate for very different RSAs? What is the advantage of GloRoot vs Smartroot (i.e. how much time does it take to trace a GLO-bot RSA manually)?

6. The trait data is not deposited with the manuscript or on a public repository. This would be very important to allow the community to build on the work of the authors.

Reviewer #3 (Recommendations for the authors):

The comments below may be helpful to the authors.

Since there weren’t line numbers, I give page numbers below and tried to ‘quote’ key words that should allow the authors to find what my comments pertain to.

1: ‘above ground’ is not hyphenated here but is elsewhere.

1: 'climate variables of the accessions respective origins' or something as to not be confused with growth conditions, etc.

2: 'between' should be among.

2: "Most RSA studies…" – can the most here really be substantiated? If not, "many" may suffice. I am not sure that most are in gel or in Arabidopsis.

3: rhizotrons are often called rhizoboxes. If rhizotron is preferred, perhaps "(or rhizobox)" can be added at first mention to orient some readers.

5: 'detection and translation of subsequent images' – I believe this describes what is commonly called registration so the word may be useful to add here for clarity.

5: 'invert the images' may be expressed as 'invert the colors of the images' to be precise.

5: 'root segment' needs defined.

6: 'series of vectors' – seems like RSML and some would ask if RSML is supported.

6: 'half of which' could be confused for accession or replicate (I know it's replicate) but consider saying "where five replicates" instead.

6: for the 6 accessions, you can add a bit more quantification by using a calculation of heritability or repeatability. You could have also used the additional replication for power analysis to determine the need for replications numbers, for example boot strapping from 2 – 10 reps to see if replicates improve measures or heritability.

7: in the last paragraph, what type of randomization used should be specified (maybe in methods, I don't like this format where some methods are in results but not all, but I know it's because results are first). On page 8 it is mentioned that an R package is used for block. I think this is leading me to conclude the results simply have to methods mixed in.

8: So is it right that a subset of days are used? Why?

8: PCA over time implies time dependent traits are just sized related.

9: ‘fitted values’ could be clarified.

10: ‘published bioclimatic variables’ could include for clarity ‘…from the origin sites of the respective accessions.’

11: ‘progress in machine-learning’ – I remember I think one of the original rationales for this system was to image on both sides for a more complete root system? Was that in the original paper? Is that done here? With regards to bioluminescence – is it still clear that this method is advantageous to RGB imaging or other forms of imaging? For example, the Smith et al. 2020 paper shows many examples of identifying roots from complex backgrounds. The RootPainter software has been used for a rhizobox study:

https://www.biorxiv.org/content/10.1101/2021.08.24.457510v1

Can the possible advantages be discussed, especially if there are specific examples from images that show color imaging alone is not sufficient?

11: sample sizes could be sample numbers I think.

Figure 1 – scale needed in all panels.

48: Not clear why Materials and methods are in supplemental?

51: "Accessions were always planted in the same locations relative to each other so the population was treated identically in each replicate." Strictly speaking – this is a bad choice, somehow you decided to intentionally NOT randomize which goes against statistical training and a strict reviewer may say it compromises the experimental design where all the measurements could be artifacts of position. Is there a good reason to not randomize? It seems odd in what otherwise seems like such careful design.

51: 'four raw images' – root and shoot from each side is four? Maybe make clear.

51: what is the 'correct blank images' – is this process entirely automated? Sounds like a user walks the processing through several fairly automated steps but not quite automated from image to data it seems.
