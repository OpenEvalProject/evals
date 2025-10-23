# Peer review - Round 1

Editors:
- Patricia J Wittkopp, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38822.026](https://doi.org/10.7554/eLife.38822.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: the authors were asked to provide a plan for revisions before the editors issued a final decision. What follows is the editors’ letter requesting such plan.]

Thank you for submitting your article "Disentangling the effects of genetic architecture, mutational bias and selection on evolutionary forecasting" for consideration by eLife. Your article has been reviewed by Patricia Wittkopp as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: James Bull (Reviewer #3).

Overall, we were impressed by the experimental data presented, but had concerns about the predictions and model testing. These concerns included both the clarity of presentation and the substance of the modeling. Different reviewers had different interpretations of some elements of the work because key elements (including Figure 3) were not clearly explained. The mutation model was one element identified as particularly difficult to understand. The lack of statistical tests comparing the predictions to data was also identified as a missing element. Especially in light of the title of the paper; making sure these predictions are made and tested appropriately, is key - we agree that this is where some of the most exciting aspects of the paper lie. Critical points raised during our discussion are provided below. Minimally, we request that you make it clear that you are evaluating two different prediction models and clarify them. Ideally, we'd also like you to make the evolution model explicit and quantitative as well as evaluate each model separately by computing numerical predictions and reporting statistics on the fit with results.

We recognize that the refinement of the modeling work we are requesting may be substantial. Given the list of essential revisions, the editors and reviewers invite you to respond within the next two weeks with an action plan and timetable for the completion of the additional work. We plan to share your responses with the reviewers and then issue a binding recommendation.

This paper reports important experimental work that could easily become a paradigm copied by others. We appreciated the study's span of known biochemical pathways for a phenotype, of documented mutations and mutation counts in those pathways leading to that phenotype, and the attempt to model/quantify the mutation rates in light of some genomic details. The topic is of sufficient interest to publish in eLife.

1) A major strength of the study was that there is an in-depth analysis of different mutational pathways to the WS phenotype. This is a data-intensive part of the paper with lots of detail about gene identity of mutations that were found in WS mutants. However, descriptions of gene functions would be better presented in a table with the in text discussion streamlined more.

2) A much better description of Figure 3 is needed. Not only are the colors not explained, but the meaning of the arrows isn't given either (are they quantitative, qualitative; how do they plug into the model?). I thus cannot easily understand how the figure connects to their models. We ultimately found this information in the supplementary materials, but the reader shouldn't need to look there to understand this key element of the paper. As one reviewer wrote: the manuscript describes Figure 3 as a diagram of a "pathway" or "molecular network" but it does not use ordinary conventions for biochemical or regulatory pathways. It is better described as a graph of mathematical dependencies between reaction rates (red) and gene-product concentrations (blue). Once you know this, you can read out some of the implied reactions like F + E* ==(r6)==> E + F*. In the supplement, see reaction 6, Figure 3—figure supplement 1, "Phosphorylated WspE can phosphorylate WspF". It would be more understandable to just list the reactions, I think.

3) Most importantly, we felt that the modeling elements were presented superficially and were not well-integrated. There are two different prediction models developed and evaluated in the paper: one of mutation rates and one of evolutionary tendencies. Regarding mutational predictability, we have (1) a model for predicting relative mutability for 3 pathways, (2) measured mutation rates for the 3 pathways, and (3) a revised model. But there are no statistics telling us how well the model fits and how much it was improved.

In theoretical population genetics there is a simple "origin-fixation" or SSWM framework for considering the relative chances of different discrete evolutionary changes. Whether or not one wishes to criticize this formalism for being too simplistic, it is the obvious framework for making a prediction when one has measured mutation rates and selection coefficients. It allows precise quantitative statements about the relative contributions of selection and mutational heterogeneity to parallel evolution, as per "What drives parallel evolution?" by Bailey et al., 2017, which uses the theory explained more thoroughly in "Parallel evolution: what does it (not) tell us and why is it (still) interesting?" by Lenormand et al., 2016. The analysis also needs statistical tests, e.g., tests of differences where the authors are making claims about differences.

Regarding the modeling framework, let me explain this concretely. The relevant facts on mutation rate, selection coefficient, and frequency evolved are (subsection “Obtaining an unbiased measure of pathway-specific mutation rates to WS”, Figure 6 and Figure 7):

Wsp: u = 3.7E-9; s ~ x; E = 15

Aws: u = 6.5E-9; s ~ x – 0.2; E = 7

Mws: u = 7.4E-10; s ~ x – 0.05; E = 3

Here x is the selection coefficient of the WspF control used in growth competitions, and I have estimated s by eye from Figure 6.

The authors talk about predictability, but they do not compute a prediction using a model, nor compute the fit between results and predictions. One way to do this is to invoke origin-fixation dynamics, yielding 3 relative predictions of u * Pr_fixation(s), which can be compared to the 3 E values using a chi-squared test (or, better, define expected Wsp and Aws as sums over the 5 and 3 relevant gene targets). Given all the numbers and Kimura's formula for Pr_fixation(s, N), this can be done in a spreadsheet in 15 minutes.

If the authors do not want to commit to the assumptions underlying origin-fixation dynamics, they can just do a multinomial regression on the assumption that E(p) = f(u_p, s_p) where p is the pathway.

In summary, we all agreed that under the origin-fixation framework, having estimates of mutation rates for different phenotypes is important and that these are not easy to obtain in most systems. We are excited about the opportunity to test how well a model based on known information can recapitulate observed mutation rates. It is interesting that it does a relatively poor job unless they incorporate information about mutational hotspots. We think that making this analysis more formal in addition to formally testing your evolutionary predictions using an origin-fixation framework (or similar approach) would both strengthen the paper and be in the spirit of what the title claims the paper does.

[Editors’ note: formal revisions were requested, following approval of the authors’ plan of action.]

Thank you for describing your proposed revisions. This summary has been reviewed and discussed by the reviewers and myself. We all agree that your proposed responses to everything except point 3 is satisfactory. For point 3, the reviewers were disappointed in the response. They all agreed that their recommendation to take advantage of your rich and powerful dataset to model the evolutionary process more formally had been dismissed too quickly.

After considering your response and their comments, it seems to me that you are thinking about "predictability" in the way that David Stern does (i.e., which genes/pathways are most likely to be changed to give rise to a particular phenotypic change given the molecular/developmental functions of all genes in the genome), and they are thinking about predictability in a more population/quantitative genetics sense (i.e., given that you know the relative mutation rates and fitness effects for different genes, you should be able to make predictions using theoretical models about how the trait should evolve, which you can then compare to the observed data). In the reviewers’ opinion, you are focused more on the effects of mutations as they arise and they want to see these combined with other evolutionary forces to make more robust evolutionary predictions.

I do not want to be so heavy handed in the review process as to try force you to make your paper something you didn't intend it to be. However, I also see the potential for modeling with your data that has the reviewers excited. It is rare to have the type of data that you have, and there are well-developed models that could make your data even more impactful.

Ultimately, I will leave it up to you to decide whether or not to go beyond the response you propose and fit a specific evolutionary model and compare it to your observed data with statistical tests. If you choose not to do this, however, it is essential that the title, abstract, and other parts of the paper are modified so that readers do not think this type of analysis is included within the paper.
