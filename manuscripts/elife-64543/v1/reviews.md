# Peer review - Round 1

Editors:
- Sandeep Krishna, National Centre for Biological Sciences­‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64543.sa0](https://doi.org/10.7554/eLife.64543.sa0)

This paper builds a biophysical model to understand the contribution of the DNA sequence in σ70-RNA polymerase binding activity. The authors provide evidence that taking into account that RNA polymerase can bind in multiple configurations, including non-productive ones, significantly improves predictions. They also confirm and extend previous observations that functional promoter sequences are relatively abundant in random sequences. This work represents an important advance to the field, and will hopefully serve as the stepping stone for better models that include transcription factors and eukaryotic enhancers.


---

# Peer review - Round 1

Editors:
- Sandeep Krishna, National Centre for Biological Sciences­‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64543.sa1](https://doi.org/10.7554/eLife.64543.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Predicting Promoter Function and Evolution from Random Sequence" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Erik van Nimwegen (Reviewer #3); Tal Einav (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

While the reviewers found that the manuscript contains potentially interesting results, as you can see from the reviews appended below, they have many concerns. Most importantly, they are not fully convinced that the model accurately predicts expression levels and would like to see much more analysis of which extensions of the previous thermodynamic models are important for the accuracy of such predictions. They were also concerned that the result that promoters are common among random sequences is not novel and does not warrant the emphasis that the manuscript puts on this result. Therefore, we suggest that in a revised manuscript you:

(i) focus primarily on the claim that the extensions to the previous thermodynamic model are important for explaining the expression levels from random sequences and real promoters, and show in greater detail how each extension is supported by instances in your dataset;

(ii) quantify more explicitly the accuracy of predictions from your model following the suggestions of the reviewers, and specifically quantify the importance of the extensions to previous models for predicting the expression levels in your libraries and in native constitutive promoters;

(iii) test your model on at least one (preferably more) of the additional data sets suggested by Reviewer 4, and provide a clear summary of how your results compare with the data.

Please do also go through the reviews below and try to address all the additional points raised by the reviewers.

Reviewer #2:

This paper builds a biophysical model to understand the contribution of the DNA sequence in σ70-RNA polymerase binding activity. To train their model, which takes into account intra-motif spacing as well as dependencies, they generate large mutant promoter libraries and measure expression from those. The title is a bit too general since the data and model are for a specific constitutive bacteriophage promoter, but nevertheless, the study has novel implications in evolution of gene regulation.

Lagator et al., have modeled the binding of σ70-RNA polymerase (RNAP) to a constitutive promoter to understand the effect of the promoter sequence in regulating gene-expression. This is a biophysical model that extends the standard thermodynamic model of RNAP binding with its cognate -35 and -10 boxes in several ways: the aim is to account for a variable spacer between the two boxes, binding at non-cognate regions, hindering transcription by binding on the negative strand (opposite orientation), occlusive binding (causing the transcript to begin upstream and not contain the RBS), and relaxing the assumption of independence within the energy matrix by modelling pair-wise nucleotide dependencies. They create three mutant libraries originating from strong λ pR and pL promoters as well as a completely random (25% probability of each nucleotide) set of oligonucleotides to train their model parameters. The model shows an impressive predictive power on a held out set and predicts expression patterns of completely random sequences to a remarkable degree.

They further conclude that many non-promoter E. coli regions are only one bp mutation away from giving rise to measurable expression. They validate their predictions on promoters where the standard model predicts a different expression pattern from their model. The data from their experiments will be a valuable addition to the community in case people want to develop new models or test other hypotheses.

A few things are unclear:

1. The thermodynamic model still makes some assumptions which need to be clearly mentioned. The sum suggests there is at the most, a single RNAP molecule (or a binding site at a time) present on each promoter.

2. The authors learn the models by using multinomial logistic regression (MLR), where the response variable is the median observed expression for each bin (which are four/12 in total, depending on the promoter class). This is a little unusual, since the four expression values are not "categories", which is typically the expectation in MLR. In other words there is a definite order (or dependence) within the categories, the first bin having a lower expression than the second, etc. That information is lost/unused in MLR.

3. It is not clear whether there are enough instances of spacer width varying in the mutant pR / pL libraries. If the mutations are single nucleotide changes (not deletions/insertions), would it not be highly unlikely that the library contains instances of the two boxes having different spacing?

It will be best to mention clearly the assumptions in the cummulative model, mathematically. A more detailed explanation of the sum in equation 2 will be useful. See for example, in the Bintu et al., paper cited in the same section. Similarly, the MLR model should be described with an equation.

Figure 1 C shows the learned energy matrix. There are other studies which use the standard model to learn their own matrix for RNAP from large mutant libraries. A comparison between the matrices will be useful, even if the promoters are different. In the same vein, this new model can be applied on those data to see if the expression can be better predicted. This will show the generality of the model.

Does sequence in pR (and pL) contain also the annotated transcription start site (TSS)? Is there any chance that the TSS also gets mutated in their libraries? Since the -10 box is relative to the TSS the distance between the box and TSS is presumably important, which can be defined only with respect to the nucleotide (or a small neighborhood) at the TSS. Does the final energy matrix contain those regions? Figure 1C suggests not.

I would have expected to see the Y axis of Figure 2B to be stratified across 12 bins. But that is not the case, which means I am missing something.

Is it not possible that the energy matrix values (those at the two boxes) change with the spacer? I understand that is not allowed in the current model.

Finally, the contribution of the dinucleotide interactions is not convincing. Perhaps the prediction accuracy on the held out set based on with and without including these terms will help clear that.

Reviewer #3:

Lagator et al., extend previous biophysical models to predict gene expression of constitutively expressing E. coli promoters from their sequence. They provide evidence that taking into account that RNA-polymerase can bind in multiple configurations, including non-productive ones, significantly improves predictions. They also confirm and extend previous observations that functional promoter sequences are relatively abundant in random sequences.

The aim of this study is to develop a realistic biophysical model for predicting the expression of (constitutive) E. coli promoters from their sequence. From my understanding of the presentation, the main new results that the authors claim are:

1. They extend existing biophysical models to a more realistic model that takes into account that the spacers between the -35 and -10 sites are flexible, that one should not just focus on the best site in a region but take into account cumulative binding to all possible sites, and that one should also explicitly model that binding to some sites is not productive (e.g. binding to reverse-complemented sites on the opposite strand).

2. They confirm experimentally that these extensions can indeed have a major impact on expression, for selected promoter sequences.

3. This biophysical model accurately predicts the gene expression level of any sequence.

4. They show that a substantial fraction of short random sequences will act as promoters, i.e. drive significant expression.

5. There is significant evidence for selection against ubiquitous expression, i.e. sigma70 binding sites are depleted both in gene bodies and in intergenic regions.

In my opinion the strongest parts of the paper are points 1 and 2. The extensions of the 'standard' biophysical model are all very sensible and the model is implemented in a mostly reasonable way. None of the ingredients in the model are particularly novel or surprising, but that's not a bad thing. I do wonder why the authors did not include features such as allowing only one of the two 'feet' of the sigma70 to bind (like in the Einav and Phillips PNAS 2019 paper) or non-specific binding (although maybe the clearing rate that the authors introduce plays a role analogous to non-specific binding). It also was not entirely clear to what extent binding at one site precludes binding at other sites in the model. This could be explained better. But apart from this the model is very reasonable. The only part I am sceptical about is the dinucleotide modeling, which is based on a very ad hoc and rather baroque procedure.

I particularly liked the experimental confirmations (Figure 1 – supplement 1) that support that several extensions of the model can indeed have a major impact on expression for selected promoter sequences. In my opinion these results should probably have been the main focus of the paper, maybe together with some more rigorous quantification of what role the various extensions play in predicting the expression levels of the random sequences. If, in addition, the authors had provided evidence that these extensions are also important for expression in native constitutive E. coli promoters, I think this could have been a very nice paper.

However, currently the focus seems to be on two aspects that I am much less convinced about. The authors in several places make the claim (point 3 above), that their model accurately predicts expression levels. I do not feel this claim is properly substantiated. First, to give some context, there is a very large body of work going back to the 1980s that aim to predict promoter sequences in E. coli directly from sequence, and with just a little bit of googling one will uncover plenty of works in the literature that appear to claim to `solve' this problem, e.g. Cassiano and Silva-Rocha mSystems 2020 present a recent benchmarking of a whole host of promoter prediction tools. I understand that these methods do not specifically aim to predict promoter strength but presumably one could use the 'score' that they calculate as a predictor of promoter strength and it is not clear to me how poorly such predictors would perform in comparison with the model presented here. In addition, there are also several previous papers that specifically claim to successfully predict promoter strength from sequence using either biophysical models close to the ones used here (e.g. Brewster et al., PLoS Comp Biol 2012, Einav and Phillips PNAS 2019) or more general machine learning methods, e.g. Mulligan et al., Nucl Acids Res 1984, Weiler and Wecknagel J Theo Biol 1994, DeMey et al., BMC Biotechnology 2007, Meng et al., Quantitative Biology 2017, and the recent Zhao et al., BioRxiv 2020.06.25.170365. Does the model of the authors significantly improve over these approaches? It is not clear to me. Especially the Einav and Phillips method is curtly dismissed in the discussion, but it is not clear to me whether that model, if trained on this data, would really perform much worse than the current model.

I understand it is kind of a pain to do extensive comparison with previous methods but in order to make real progress on understanding what determines the expression levels of constitutive E. coli promoters, then at a minimum I would have expected a very clear quantification of exactly how well the model performs. What one would want to know is: If I feed the model a random sequence, how accurately does it predict its expression level? Or, how well can the model predict the variation in expression levels of constitutive promoters across the E. coli genome? How much accuracy will be lost when various of the extensions are removed, either on native promoters, or on random sequences.

However, we do not really get such an analysis. The authors only present one scatter and Pearson correlations between the predicted log[Pon] and measured log[expression] for various versions of the model. Crucially, I do not think that a correlation of r2 ~ 0.75 on a dataset where expression levels vary over a 1000-fold range can be reasonably described as `accurate prediction'. Just as a back-of-the-envelope, if both data and model have a standard-deviation in log-expression levels of about log[100], then r2 = 0.75 corresponds to the error between model and data having standard-deviation of log[10]. That is, unless I made a mistake in my back-of-the-envelope, the model's predictions would typically be off by 10-fold (and the scatter does seem sort of consistent with this). t is also in line, with the fact that the bins for the P_R data are 10-fold apart in expression level, i.e. the training of the model is done on a dataset in which promoters whose expression levels are within 10-fold of each other are effective treated as equally expressed. I do not think that this level of precision can be called accurate prediction of expression levels. For example, using very similar reporter constructs, the difference in expression of the median and 95th percentile of native E. coli promoters is about 20-fold (i.e. see Wolf et al., Figure 1B), so this model could barely tell these apart.

Another issue is that it is not clear which extensions of the model are the most crucial for the accuracy of the predictions. I was surprised to see (in Figure 2 – source data 1) that, apparently, by far the biggest improvement on the random sequences (36N dataset) comes from including flexible spacers and that cumulative binding and occlusive binding adds rather little. This appears somewhat at odds with the narrative that the authors present in the paper that stresses the importance of cumulative binding.

In short, although I would like to believe that this reasonable biophysical model improves a lot over previous approaches in the literature, I don't think a convincing case has been made that this is really a major advance in accuracy of promoter strength prediction.

Finally, regarding points 4 and 5, I do not understand why the authors place so much emphasis on the observation that functional promoters (i.e. sequences that drive gene expression) are common among random sequences, because this is neither novel nor surprising. It has been long-known that the 'position specific weight matrices' that model sigma70 binding sites have low information content, e.g. Schultzaberger et al., Nucl Acids Res 2007 estimate it to be about 6.5 bits. Given this, one would very roughly expect a site every 100 bp in random sequences. In fact, this was one of the reasons why, in Wolf et al., (eLife 2015), we were confident that we would easily find a large diversity of functional promoters in a library of random sequences. This expectation was confirmed by our measurements as one can see from Figure 1B of Wolf et al. That is, after selecting the 5% of highest expressing cells from the random library, most of them express at a reasonable level. At the time it didn't even occur to us to mention this as a surprising observation. When the paper of Yona et al., (Nat Comm 2018) appeared, we realized that we misjudged this, and that for many people it WAS surprising that functional promoters are common even in relatively short random sequences. However, now that Yona et al., have an entire paper focused on this observation, including showing depletion of sigma70 sites within gene regions, there is no more novelty to this observation.

The observations about the frequency of occurrence of promoters in random sequences could have been more interesting if it had been more meaningfully quantified. That is, any sequence will presumably drive expression at some nonzero rate. An interesting (and meaningful) quantitative question is how likely it is that a random sequence drives expression at rate > x, as a function of x. Maybe the authors' data and model could give a reasonable answer to this question. However, instead the authors simply treat this problem as if there is just a binary question whether a promoter is expressing or non-expressing. Moreover, they define the threshold between expressing and non-expressing in a way that is not biologically meaningful but seems determined by instrument precision. I actually had a hard time understanding how precisely 'measurable expression' was defined. My understanding is that, for the P_R and P_L libraries, it is defined as any expression higher than the 99th percentile of measurements for cells carrying no YFP. But how it is defined for the 36N library (with another reporter) was unclear to me. In any case, it appears that 'measurable expression' is defined in terms of the auto-fluorescence level that the cells have in the FACS machine. Unfortunately, this is not a biologically meaningful cut-off. In fact, a substantial fraction of E. coli promoters express below the detection limit in the FACS (i.e. not significantly above auto-fluorescence).

In summary, I think there are some very good ideas in this paper. I in principle like the biophysical model, and the experimental validations of the model's extensions I thought were very nice and, when extended, could make a compelling paper. Unfortunately, the current focus of the papers appears to be on the frequent occurrence of promoters in random sequences (which is not novel) and claims that the model is a major advance in predicting gene expression from sequence, which I do not feel are substantiated by the results presented.

1. I had real trouble understanding the processing of the 36N dataset. I understand that, because in the 12-bin dataset you sort until you have a certain number of cells in the bin, you need to correct for this when estimating the relative fractions of cells with a given promoter that go to different bins. But I do not understand the approach with the spike-ins. Aren't there, in addition to the spike ins, also an unknown number of reference promoters coming from the sorting?

2. line 81: "even for constitutive promoters, where σ70-RNAP binding solely determines gene expression levels" Has this really been established? There could be effects of differential binding of topoisomerases that undo supercoiling.. or differential weak binding by other TFs.. and so on. I don't think we really know these levels are solely determined by sigma70-RNAP.

3. Figure 1 – supplement 1.

Why is detectability threshold higher in B than in A? I found it generally quite frustrating that it is hard to figure out how exactly this 'measurable expression' threshold, which plays such a crucial role, is defined.

4. 515-516: Finally, we required the distribution of expression bins to be as unambiguous as possible (Figure 2 —figure supplement 1D,E).

Why is this done? The way I understand it, this throws out promoters whose expression levels straddle two bins. I guess you want to throw those out because the fitting of the model to only observations in 4 bins only is more accurate when using only promoters that fall sort of in the middle of those bins, but I find this quite unsatisfactory. Would it not have been possible to fit a log-normal to the relative fractions of counts in the different bins and get continuous expression estimates?

5. 596: "We define 60:20:20% splits of each of our libraries into three disjunct datasets Figure 2 – Source Data 3."

Are these splits random? A notorious problem in cross-validation based fitting is when highly correlated datapoints occur in both training and test data. For example, in this case you could have promoters that are virtually identical, and with equal expression, in both training and test datasets. This could lead to misleadingly high performance on the test dataset. I actually doubt this is happening here, but maybe it is worthwhile checking this.

6. Did you try adding a non-specific binding term to the model? Or the ability for sigma70 to bind through only one of its two feet? If not, why not? Do the authors think sigma70 cannot be bound only at the -10 or -35 sites?

7. I did not like the way multinomial logistic regression was used to fit the model. Expression should go up monotonically with Pon. It makes no sense to treat the bins as unrelated 'classes'.

8. Comparing evolution of promoters de novo under the extended model against the 'standard model' is a straw man in my opinion. The standard model is an approximation to the thermodynamic model that is valid when there is one site that dominates the overall affinity of a promoter. I agree that it is often assumed that this is a good approximation for native promoters that have been shaped by selection. But I do not think there is anybody that thinks this is a good model for how promoters appear in random sequences. Obviously weak promoters can then appear anywhere in the sequence.

9. For Figure 3A, I think it is essential to also predict such a curve for the sequences in each of the libraries and see how well these predicted curves match the observed distributions for these libraries. Otherwise it is hard to judge how meaningful this predicted distribution is.

10. Many intergenic sequences in E. coli will be constrained to have all kinds of TFBSs, precluding sigma70 to occur in those positions. So to check whether there is really depletion of sigma70 sites, comparing with random sequence of the same nucleotide composition is not quite correct in my opinion. First, you should distinguish intergenic regions that are upstream of two operons from those that are upstream of one, and those downstream of two promoters. Those 3 classes of intergenic regions are also known to have different nucleotide composition. The best regions for tests would be downstream regions, and regions that are upstream of an operon that is constitutive.

Reviewer #4:

The manuscript by Lagator et al., examines a general framework to predict the constitutive level of gene expression for bacterial DNA, which constitutes one of the most fundamental processes in biology. Whereas previous work has typically been restricted to a limited sampling around a well-studied promoter (such as the lac operon), the authors push towards a model that can characterize all possible sequences, which they support with libraries containing 10,000 mutants each around two strong promoters (PR and PL) as well as a library containing 10,000 random sequences (36N). This work represents an important advance to the field, and will hopefully serve as the stepping stone for better models that include transcription factors and eukaryotic enhancers.

While the authors provide a clear and compelling story using their impressive data set, the one piece that I felt was missing was a connection with large gene expression data sets from other groups. How robust will their already-trained model be when applied in another context, where the experimental design is somewhat different? This will help other groups understand the potential gain in implementing this model for their own ends, and if any fine-tuning or model adjustments need to be performed, such information would be important to add. To this end, I suggest a few possible data sets below. The authors do not need to analyze all of them (although more is better), and they are welcome to substitute other data sets of their choice:

1) Hossain 2020 [https://doi.org/10.1038/s41587-020-0584-2] analyzed 4,350 bacterial promoters with a broad range of gene expression measurements varying by 820,000-fold. These promoters should be constitutive, although their random DNA sequences might occasionally give rise to transcription factor binding sites (as in the 36N library). The sequences and read counts are available in their Supplementary Data 3.

2) Urtecho 2019 [https://doi.org/10.1021/acs.biochem.7b01069] analyzed the constitutive expression from 10,000 promoters. Their setup ensures that no transcription factors are involved, providing a clean test for the model. You can find their expression data at the GEO Accession Number GSE108535 [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE108535]. The file “GSE108535_sigma70_variant_data.txt.gz” contains the names of promoter variants and the average RNA/DNA expression levels of two biological replicates, while the file “GSE108535_barcode_mapping.txt.gz” contains the name of each promoter variant and its corresponding sequence (where the sequence is specified in the column ‘most_common’). Figure S12 and Table S1 from their supplementary information provide a visual schematic for how to put the pieces together.

3) Johns 2018 [http://doi.org/10.1038/nmeth.4633] analyzed 30,000 promoters mined from prokaryotic genomes, which would be a very interesting avenue to explore. These promoters may involve transcription factors (although their mining strategy might bias them towards constitutive promoters). Their sequences are given in Supplementary Table 1 and their expression measurements for E. coli are provided in Supplementary Table 3.

I suspect the authors are already planning to do this, but it would be very helpful if a program implementing the fully-trained model was provided (along with some examples of its usage), to help the community utilize these results.
