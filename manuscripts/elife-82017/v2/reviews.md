# Peer review - Round 1

Editors:
- Naama Barkai, https://ror.org/0316ej306 Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82017.sa0](https://doi.org/10.7554/eLife.82017.sa0)

This paper addresses an important question in the field: the cell-to-cell heterogeneity in stress response and the functional relevance to stress adaptation. The experimental approaches are timely and their clustering and correlation analyses suggest some interesting relationships between phenotypic factors and growth adaptation.


---

# Peer review - Round 1

Editors:
- Naama Barkai, https://ror.org/0316ej306 Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82017.sa1](https://doi.org/10.7554/eLife.82017.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Integrating multiple single-­cell phenotypes links stress acclimation to prior life history in yeast" for consideration at eLife. Your initial submission has been assessed by a Senior Editor in consultation with members of the Board of Reviewing Editors. Although the work is of interest, we regret to inform you that the findings at this stage are too preliminary for further consideration at eLife.

As you will see from the reviews below, the reviewers found your manuscript potentially interesting but the story incomplete (see for example reviewer #2 – "My concern is that the story seems incomplete and lacks any firm conclusions regarding causality or mechanisms. The paper relies completely on the correlation analyses, which could serve as a good starting point for a story, if followed with experimental validation (e.g. by perturbations) and mechanistic investigation. However, the authors decided to end the paper there, leaving the story incomplete and inconclusive. Therefore, a significant amount of further work will be needed to warrant publication of the paper in eLife."; this was pretty much the oncensus)

if you can fully address this concern through additional experiments (as well as the other concerns expressed by the reviewers), we will be happy to reconsider the paper.

Reviewer #1 (Recommendations for the authors):

In the present paper Bergen, Hose, McClean, and Gasch study the yeast stress response and recovery in the form of cell growth rates. It is well-known that there is great heterogeneity among the responses of otherwise genetically identical single cells to stress. An interesting question therefore is to what extent is the heterogeneity is just random stochastic noise and to what extent is it "hard-coded" into the cell based on its recent prior history (e.g. expression of various proteins, cell-to-cell variation of protein abundances, prior stress response, etc).

Clearly both – random noise and prior life history – contribute. For example, it is well known that stochastic single molecule events can regulate cell fate (Choi, Cai, Frieda, Xie, Science, 2008), but it is also well-known that if you "prime" cells by exposing them to mild stress, then they respond much better to a subsequent high-intensity stress.

An interesting question then is, what is the relative contribution of random noise and prior life history? And for prior life history, what factors are most predictive?

The setup of this paper is pretty simple. They look at two well-known factors, Msn2 and Dot6, using a single type of stress (0.7M NaCl step function) and they then quantify various aspects, the 3 most important of which are: (1) Msn2 nuclear localization; (2) Dot6 nuclear localization; and (3) cell growth rate.

The key finding is that prior Dot6 activation is more predictive than Msn2, and that a model with more variables can predict more of the variance than for example a single factor.

While the authors test multiple factors, the overall amount of the variance that can be explained is modest – around 35% using the full linear model.

I don't have major technical concerns and the work generally seems to be well done. I think the two main issues are (1) I would like to see some control computational analyses to assess how robust their growth rate quantification is and (2) the size of the dataset is pretty small, just 221 cells. This is a concern especially since they have 11 clusters, some of which have very few cells in them, raising doubt about their conclusion.

For the 1st concern, I'd like the authors to do a mock experiment: grow cells without any stress and then arbitrarily set a boundary and do similar plots to Figure 2 to see how much change in growth rate they see without stress. This will allow us to understand how much of Figure 2 is true signal and how much is just quantification noise. This could either be a new experiment or re-analysis of existing data before the stress. I'd also like to see "moving average growth rate" plots for single cells – how meaningful is a single growth rate number? I'd also like to get more detail on how growth rate was calculated. If I understand correctly, the authors use cell size. This is very reasonable, but it is a challenging quantification: since volume scales with radius to the 3rd power, tiny errors in the estimation of the radius can result in massive changes in the estimation of the volume. What was the pixel size and did they do subpixel analysis?

In general, I'd like to see a comprehensive description of how they quantified cell growth as well as a comprehensive supplementary figure "stress testing" the robustness of their quantification.

This is important since the entire paper rests on the cell growth numbers being accurate.

For my second concern, I'd like the authors to test how robust their various results are to cell numbers. I suggest that they do subsampling, where they leave out 50% of their data/cells, repeat their analysis, and then iterate multiple times to assess if all of their conclusions are robust. For example, I am concerned about whether or not they have enough data to support 11 clusters. This type of subsampling approach should be informative, though I would like to see this approach applied to all of the major conclusions and analyses.

Since both of these concerns can be assessed using either purely more computational analysis and/or just with the addition of a very simple experiment, hopefully they should not be onerous to address.

My conceptual concern is whether or not the present paper is a major conceptual advance. The notions that prior life history affects how cells deal with a stress response as well as the observation of substantial heterogeneity in single cell stress responses, are both well-known in the field and similar observations have been made in yeast and other organisms. So, the major novel contributions seem to be the relative important of Dot6 and Msn2 (Dot6 is more predictive than Msn2, which at least I did not know), and a quantification of how much one can predict from Dot6 and Msn2. This is certainly a nice contribution, and the study seems to be generally performed in a thoughtful manner, but it is perhaps a modest conceptual advance given what is already known.

Reviewer #2 (Recommendations for the authors):

In this manuscript, Bergen et al. combined microfluidics and time-lapse imaging to monitor single-cell phenotypes in response to acute osmotic stress. In particular, they measured translocation dynamics of two transcription factors, Msn2 and Dot6, together with a series of cellular phenotypes, e.g. cell growth, cell size, cell cycle phase, etc. To make sense of these data, they classified single cells into clusters based on their Msn2 and Dot6 dynamics, and performed correlation analyses to quantify relative contributions of measured phenotypic factors (alone or in combination) to post-stress growth rate. They found that post-stress growth rate showed a stronger correlation with an integration of multiple factors (rather than each single factor alone), among which pre-stress growth rate and Dot6 peak height seem playing major roles.

The authors focused on an important question in the field – the cell-to-cell heterogeneity in stress response and the functional relevance to stress adaptation. The experimental approaches are not new but timely. Their clustering and correlation analyses suggest some interesting relationships between phenotypic factors and growth adaptation.

My concern is that the story seems incomplete and lacks any firm conclusions regarding causality or mechanisms. The paper relies completely on the correlation analyses, which could serve as a good starting point for a story, if followed with experimental validation (e.g. by perturbations) and mechanistic investigation. However, the authors decided to end the paper there, leaving the story incomplete and inconclusive. Therefore, a significant amount of further work will be needed to warrant publication of the paper in eLife.

Other concerns:

1. I find the title a bit misleading. "Prior life history" sounds like a cell's previous stress encounter, nutrient condition, or age, etc. However, in the paper, it seems referring specifically to Msn2/Dot6 dynamics and pre-stress growth rate during the 72-min baseline (no stress) period immediately before the stress treatment. Maybe "pre-stress cellular state" is more accurate than "prior life history."

2. Figure S2, it seems pre-stress growth rate and Dot6 acute stress peak height are major contributing factors to post-stress growth rate. Is it possible that these two factors are mechanistically connected? Is there any correlation between these two factors? My concern here is whether these two factors can be simply combined into one factor, pre-stress growth rate or biogenesis capacity whereas Dot6 acute stress peak height simply depends on Dot6 protein expression level, reflective of cellular biogenesis capacity. If this is true, then an alternative interpretation of the correlation results will be that cell-to-cell variation in post-stress growth rate largely arises from variations in pre-stress growth rate or biogenesis capacity, which has long been known as a major source of extrinsic noise. Dot6 peak height and other phenotypic factors simply reflect pre-stress biogenesis capacity. This interpretation can also reconcile the contradiction that Dot6 peak height positively correlates with post-stress growth rate whereas Dot6 is a repressor of ribosomal biogenesis. A careful test of this possibility will be needed.

Reviewer #3 (Recommendations for the authors):

Bergen et al. study how the dynamic subcellular localizations of two stress-responsive transcription factors (Dot6 and Msn2) relate to variability in the growth of yeast cells before, during and after high-salt stress.

Previous studies (e.g., by the O'Shea lab) used microfluidics to look at subcellular dynamics of Msn2 and other transcription factors from a more mechanistic point of view. Other studies (e.g., Li et al. 2018 cited in the manuscript) used higher-throughput time-lapse imaging to look at population heterogeneity in growth, gene expression and stress tolerance. The present study is appealing because it sits somewhere in between. It uses microfluidics to track the two transcription factors but asks how their dynamics relate to growth.

One interesting finding, corroborating the authors' 2017 work, is that Msn2 and Dot6 do not show entirely coordinated activity. The authors identify upwards of 10 clusters of cells distinguished by different dynamic patterns of the two TFs. This finding raises the possibility that this kind of approach can find meaningful subpopulations of cells with different physiological properties.

However, the manuscript does not go far in developing understanding of how these subpopulations are generated. The authors describe Msn2 and Dot6 as both being controlled by both PKA and TOR. But that does not necessarily mean that Msn2 and Dot6 should always respond together -- one simple hypothesis is that the discordance that is seen is a result of differences in the relative contributions of these signaling pathways to Msn2 and Dot6 control. There are also counter-intuitive results that remain to be explained. In particular, the authors report that cluster 11, with below-average Dot6 response before and during stress showed slower growth. Because Dot6 represses growth-promoting genes, one would expect low Dot6 response to produce faster growth. In the end, the biggest predictor of post-stress growth rate was pre-stress growth rate, so the authors' conclusion that prior life history states are predictive (to some extent) of future ones is reasonable. But it remains to be seen why the correlation exists.

The results presented in the manuscript will certainly be of interest to those following this line of research, but the impact more generally is moderate because of the lack of deeper mechanistic insight into how this important signaling network generates heterogeneity in growth responses.

One recommendation to strengthen the presentation of the paper would be to include a figure (and/or movies) showing primary data (time-lapse images of fluorescent signal in cells in the microfluidics device), especially since this is not an off-the-shelf microfluidics platform.

Another recommendation is to flesh out more the comparisons to prior experimental work. For example, a reader new to this line of research would not immediately grasp that Li et al. 2018 followed colony growth for much longer time periods, did not use microfluidics, and used cells enriched for slow growth when examining Msn2 dynamics. These details can affect how a reader interprets the observation that Msn2 response does not correlate strongly with growth in this study. Also, the authors do not discuss any connection between growth heterogeneity and mitochondrial function, which featured heavily in the Fehrmann et al. 2013 and Li et al. 2018 papers that were cited, as well as in Dhar et al. (eLife 8:e38904, 2019) that was not cited.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Modeling single-cell phenotypes links yeast stress acclimation to transcriptional repression and pre-stress cellular states" for further consideration by eLife. Your revised article has been evaluated by Naama Barkai (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

I appreciate that the authors have put in a fair amount of work into the revision and I do believe the paper is strengthened. The authors have responded to my main concerns.

Regarding cell growth calculations, I do remain concerned. They do not do subpixel segmentation, and they only do 2D segmentation as I understand it. Furthermore, they do not quantify growth rate (which I would define as the mass accumulation per unit time). Instead, they take the relative change in the median size, and for much of the paper they then take the logarithm of this number. A lot of these assumptions seem reasonable but arbitrary and as added complications, yeast cells shrink dramatically in size upon osmotic stress and then gradually recover (so changes in cell size reflect both cell growth and osmotic changes) and budding yeast mainly grow at the bud, and the bud is frequently out-of-focus and not quantified.

Accordingly, the main output metric in the entire paper – cell growth rate – and the measured values are associated with very very large uncertainties and caveats. At a minimum, this need to be more explicitly mentioned and caveated in the main text.

Moreover, some of the analysis remains not totally convincing. For example, in Figure 5A there is a mostly random vertical scatter of points, and what seems like a fairly arbitrary straight line is drawn through it. The p-value may be small, but this does not look like a model that very well explains the data.

Overall, I appreciate the great work done by the authors to address the reviewer comments, but I do think both some technical and conceptual concerns remain. That said, it is a challenging question to tackle, and it is not clear a priori how much of the variation we should even expect Msn2 and Dot6 dynamics to explain.
