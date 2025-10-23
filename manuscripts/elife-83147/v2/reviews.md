# Peer review - Round 1

Editors:
- Leslie S Satin, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83147.sa0](https://doi.org/10.7554/eLife.83147.sa0)

The paper uses both computational and laboratory approaches to test the hypothesis that connectivity in β cells within the islet is due to metabolic rather than gap junctional coupling efficacy. This will be an important advance for understanding the role of heterogeneous β cell populations in driving synchronized oscillations by islets and by extension the oscillatory insulin secretion observed in vivo. There will be implications of the work for understanding the mechanisms of type 2 diabetics and β cell function in general.


---

# Peer review - Round 1

Editors:
- Leslie S Satin, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83147.sa1](https://doi.org/10.7554/eLife.83147.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Β-cell Metabolic Activity Rather than Gap Junction Structure Dictates Subpopulations in the Islet Functional Network" for consideration by eLife. Your article has been reviewed by 5 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: David J Hodson (Reviewer #1); Andraz Stozer (Reviewer #2); Victoria Salem (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The modeling, based on the Cha et al. model is clearly of fast oscillations but the data shown include both fast and slow oscillations. The model will therefore need to be revised to simulate the slow data more closely either using the Cha model in a different mode, or a different model.

2) There are questions about some of the analyses and plots only showing a small number of data points, which must be addressed and also the choice of R-value as discussed.

3) There was a general concern about the small-worldness of the data and this must be dealt with.

4) It is recommended that some of the key conclusions made by the authors be more tempered as some of the reviewers commented that perhaps some key conclusions were overstated based on the data and analysis.

5). It would help if the authors more clearly indicated which findings were truly novel and which were confirmation of observations made previously by their lab and others.

6). The manuscript is quite long and rather dense and thorough editing must be done to improve its readability (especially by non-experts); this would help the paper.

Reviewer #1 (Recommendations for the authors):

I have the following constructive suggestions to further improve the studies:

– "In diabetes the islet shows disrupted [Ca2+] synchronization (representing a disrupted functional network) and diminished gap junction coupling (representing a disrupted structural network)." A schematic would be helpful here to visually explain the functional and structural networks that are the focus of the studies.

– The resolution of the FRAP studies is impressive, with single-cell definition. Nonetheless, FRAP only looks at cationic dye transfer, does not report conductance, and is unlikely to be as sensitive as patch clamp measures. Conversely, patch clamp is inherently biased, is spatially limited, and likely selects for certain cell subpopulations (i.e. cells that do not form seals or respond to voltage ramps are disposed of). Caveats are needed here, since there is probably no perfect measure of GJ conductance across a cell population, which is the basis for the modelling here.

– "Prior work suggested that cells with highly synchronized Ca2+ oscillations possess both elevated metabolic activity (in agreement with our observations, Figure 2) and high levels of gap junction conductance (unlike what we observe experimentally, Figure 2)". Johnston et al. showed that Gjd2 knockdown disrupted synchronization, functional connectivity, and hub number, implying a role of GJ communication in hub function. However, this knockdown was not hub-specific so any inferences about hub GJ coupling are indiirect.

– "However, as the functional network becomes sparser, the uncertainty in the random network-based approach increases (Supp. 4d, seen more clearly in Supp. 6d)." Maybe I am not following here, but would a sparser functional network not be expected to decrease power-law slope/fit and hence the definition of small-worldness? Some more explanation would be helpful.

– "Semi-quantitative immunofluorescence previously demonstrated elevated glucokinase protein in β-cell hubs, suggesting elevated metabolic activity." The authors also looked at TMRE accumulation in hubs, showing more hyper-polarized mitochondria indicative of increased OXPHOS (hence fitting with the NAD(P)H).

– It is well established that gap junction coupling is decreased in animal models of diabetes, as well as aged/high BMI human islets. However, are functional and structural networks mutually exclusive? That is, do changes in cell states drive changes in GJ coupling or vice versa? Or is there no relationship between these parameters?

– Electrical coupling is assumed to be a static phenomenon within the islet. However, connexins are dynamic proteins, their gating can be influenced by cAMP/PKC signals (shown by this group), and expression levels differ across β cells. How would the authors predict such heterogeneity to influence their model? How might this be built into analyses going forward?

– A comment on the translation of the results to human islets would be appreciated since there are known differences in coordination (more regional) and cell interactions compared to rodents.

– "Finally, the islet also contains α-cells, δ-cells, and other cell types which can influence β-cell dynamics via paracrine mechanisms". It would be worth citing recent studies from the Chen and Tang groups (DOI s41467-022-31373-6).

– The authors note some study limitations. It would be worthwhile also discuss limitations with the models of GJ disruption. For example, GJD2 KO is global and occurs early in development, so any effects may be confounded by β cell de-differentiation/immaturity (and metabolic changes therein). I understand that conditional Cx36 models have been historically unavailable, but conditional-ready KOMP mice could be informative in the future.

Reviewer #2 (Recommendations for the authors):

Introduction

– I suggest a reference for the epidemiological data, i.e., for the number of people affected by diabetes. The IDF Diabetes Atlas is a valuable resource and typically accompanied by citable publications, such as PMID: 34879977

The first part of the Results: Cellular metabolism, but not elevated gap junction coupling, is observed in highly synchronized cells in a simulated β-cell network, the corresponding Figures, and Methods

– Rth was chosen at the value of Rth = 0.9995 – this is a rather high value compared with values typically chosen for experimental calcium traces (e.g., Stožer PLoS Comput Biol 2013, Front Endocrinol 2022), which indicates that the model did not produce large temporal differences/delays between cells. Could this be improved in the model to more closely mimic the experimental situation where delays between cells are on the order of magnitude that is the same as the order of magnitude of burst/fast oscillation durations? If there are objective reasons that this cannot be done easily with existing models (by for instance destabilizing the model with increasing heterogeneity), I suggest that the authors point out this difference between experiments and model and more explicitly address the nature of this discrepancy.

– From the inset in Figure 1d, it is also not clearly visible what the temporal delay between traces in different cells was. Please, provide a more detailed inset/zoom-in.

– In addition to the mean parameter values, I recommend that the authors also provide the range of values more precisely quantify heterogeneity. Since the statistics in Figure 1 are based on a rather small number of simulated islets (N=5), I suggest that effect sizes be reported as well.

– In the model, only 500 seconds were simulated, and then the so-called fast calcium oscillations present during the second (plateau) phase of the calcium response (and brought about by bursts of electrical activity) were analyzed. In the simulated traces, they seem to be around 15-25 seconds long (Figure 1d). From the Methods section, it is not entirely clear what period of calcium traces obtained by calcium imaging in isolated islets was used for the network analysis. The authors state that "[Ca2+] time courses were analyzed during the second-phase [Ca2+] response when the slow calcium wave was established", but Figure 2 and other parts of the manuscript do not provide enough information to be sure whether the interval used for network analyses included the whole traces beyond approximately 500 seconds (Figure 2b) or only smaller parts of these traces that would correspond in duration to intervals used on simulated traces. I think it is critical that the authors address and resolve this question in detail for the following reasons.

– First, simulated traces reflect only fast oscillations, whereas in experimental traces (See Figure 2b), there are a few slow oscillations that last approximately 300 seconds each, and superimposed on them fast oscillations (approximately 10 seconds long), corresponding to oscillations analyzed on simulated traces. Since there may be fundamental mechanistic differences between fast and slow oscillations, the first being more importantly determined by ion channel properties and electrical coupling and the second more importantly by metabolism, the networks constructed from experimental traces may contain and provide information that is different from the information provided by simulated traces and networks based on them. If the authors included in their analyses on experimental traces only one part of a slow wave (e.g. 200-300 seconds) containing a few fast oscillations (e.g. 10 fast oscillations), then the simulated traces and networks can be compared with experimental traces and networks. If not, i.e., if they included longer periods (e.g. 1000 seconds) containing a few slow oscillations and thus many more fast oscillations (e.g., 50 fast oscillations), then the Pearson correlation between traces may heavily depend on the slow trends defined by slow oscillations (as addressed recently in Zmazek et al. Front Physiol 2021 and Stozer et al. Front Endocrinol 2022), and thus the network metrics convey entangled information on both fast and slow properties. Most importantly, the main conclusion from the experimental part that the rate of metabolism may be more important than other factors in determining functional network properties may be due to the prevailing influence of metabolic oscillations on networks based on experimental recordings. In this case, I suggest two possible solutions. The authors could extend the simulations to produce a mixed pattern of oscillations (which should be possible, given the existing work by Bertram, Sherman, Satin, Nunemaker, and Benninger) and then systematically analyze the impact of the fast and slow components on network properties and the importance of different parameters (kglyc, gKATP, gcoup) and compare the findings with experimental data where they could also separately study the two components. Alternatively, the authors could extract the fast component from the experimental traces (by using an appropriate filter) and limit their analyses and discussion to the fast oscillations only.

– Second, resolving the above point is not only important for this manuscript, but also for resolving the (apparent) differences between studies (and the Rutter-Rorsman dispute).

– Finally, resolving the first above point is also particularly important for extending the findings to Cx36-/- mice where fast and slow oscillations may be affected to a different extent by the absence of gap junctions, with desynchronized fast oscillations and possibly less desynchronized slow oscillations.

The other parts of the manuscript

– My comments and suggestions to other parts of the manuscript depend on how the above fast-slow oscillation issue will be resolved since all of the following Results and corresponding Figures strongly depend on the way how networks are constructed. I will be more than happy to do so in a possible next round of revision.

Reviewer #3 (Recommendations for the authors):

Briggs et al. present a strong set of both computational and experimental approaches to investigate some current controversies in the functional relevance of β cell heterogeneity and pancreatic islet function. They conclude that β cell connectivity is driven by metabolic rather than gap-function-mediated structural coupling. This lays the ground for future studies understanding how metabolic coupling relates to the identity of "hub cells" and to what extent this can be targeted in the treatment of diabetes. Overall this is a very strong paper that is of interest to the readership of a journal like eLife. It is extremely well written. I would suggest that more experimental data for the NADPH and FRAP experiments might build up confidence in the finding that connectivity is defined by metabolic coupling – at present, the datasets are convincing that metabolic coupling is absent in cells that lack calcium connectivity but are not convincing enough in the opposite direction.

Here are my general comments.

The authors state that "Functional networks represent the emergent system behavior". Diabetes ensues from the autoimmune destruction of β cells (T1) or the functional demise (a mix of environmental insult with a genetic predisposition – T2). To what extent can network theory really tell us anything about the pathophysiology of these disease states or aid the development of new treatments? Or is this simply another tool, like GSIS, for assessing islet dysfunction? I think it would be useful to have this sort of oversight mentioned in the discussion, to persuade readers of the real relevance of your work.

"cell hubs can exert a strong influence over islet dynamics21,24,25 53 and are preferentially disrupted in diabetes23" Did the Johnston paper really conclude that diabetes is causally related to the preferential loss of hubs over followers? Or is it more likely that in a dysregulated islet loss of "hubs" becomes more apparent? I personally would have prefaced this paper by summarising the mathematical and experimental evidence for hubs that exhibit small-world properties.

When you say "structural location" what do you mean – you didn't for example look at a position relative to blood vessels, α cells, nerve endings, and δ cell projections. As a general comment, I'm not really comfortable with you equating conductance (ie the physical number of gap junction interfaces between β cells) as synonymous with their structural topography. There are so many unknowns here still – for example the contribution of other endocrine cells, nerves, and "humoral factors". Your computational model essentially randomly assigns heterogeneity in terms of metabolic rates, for example, across the 1000 "β" cells. In fact, this may not reflect the fact that such heterogeneity is indeed based on a cell's position relative to other aspects of the islet microenvironment (not just other β cells).

Results section 1

Briggs et al. start with data extracted from a model. Whilst the thresholds selected are generally well justified and the testing of various thresholds adds robustness, it is, in the end, just a model. It has been well validated by electrophysiologists, but the audience of this paper is wider and I think it is worthwhile reminding us in a couple of sentences of what the major inputs are into this model and how that results in oscillatory behaviour (I know you do this in supplemental anyway). Presumably, this is being run for a certain ambient glucose level ie parameters change between low and high glucose. It's important that you point out there is no accounting for other endocrine cells etc – which I think you do in the

Discussion.

Was such a high R-value necessary to get the requisite power-law type distribution a surprise to you? Were all 1000 cells included in your readouts? Why did you choose the 60% connection cut-off to define hubs? Is this done by others? In your supplementary data as you move (in very tiny increments) across R thresholds the number of connections on your axis changes apparently randomly (the scale goes from 0-200 to 0-800). Why?

The differences in Kglyc between hubs and followers are statistically significant but the difference in absolute terms seems very small – is this relevant?

Results section 2

This is the experimental dataset which is very interesting.

"We extracted the functional network (Figure 2c) and again generated a normalized degree distribution which reflects a scale free-like distribution."

– ok but there is no mention of actual R values here – presumably much less than the modelled ones previously and the cut off for defining hubs on normalised degree of "edginess" is also different from the above (and others?). Conversely, you then introduce the concept of a "low degree" cell without defining that.

Just out of interest, the cross-section shows that some β cells are much more fluorescent than others, presumably reflecting variation in GcAMP expression. Do you think this is an issue for your calcium trace analysis?

In the Methods section please can you explain in a bit more detail how you extracted your NADPH data – over what time period/resolution etc.

"Furthermore, the NAD(P)H response trended lower in cells that were functionally disconnected (Ca2+ 128 oscillations lacking any synchronization), compared to connected cells (Figure 2g)."

Presumably, you only looked at calcium oscillating β cells as inactive ones will obviously likely have no other How did you define an oscillation? Your time course of over 30 minutes looks long. The association between low NADPH signal and low connectivity seems much more robust than that between hubs and high NADPH signal. Would repeat experiments firm this up?

Is the FRAP experiment powered? I don't have a feel for the sensitivity of this method to pick apart quantifiable differences in gap junction connections but the numbers here seem low – only 4 islets.

Results section 3

The next section poses the question what does the islet functional network indicate about its underlying structure or intrinsic properties on an individual cell basis?

The authors appear to have returned to their simulated data here which initially confused me so should be headlined at the outset. Given that the EPists know that GJ coupling cannot explain connectivity across more than a few cells, I think it's important to state in the main text that you enforced spatial limits on your structural connectivity analyses.

Some of the surprising findings e.g.

"The probability that two cells were synchronized in the functional network, given that they shared a gap junction in the structural network, was = 0.39" has been discussed well later (eg where they don't tally with prior experimental measures.

On the whole, I find the ending statement "These results further indicate that metabolic activity, not gap junction connections, is a greater driving factor for cells to show high [Ca2+] synchronization and thus influence the functional network." to be robust.

The next section looks at long-range functional connections which traverse cells, quite dense. I thought the experiment that modelled GJs of higher conductance to be rather extraneous and could have gone into supplemental but I don't feel strongly about this.

I think there needs to be some unpacking of the term kglyc as a measure of "glucose metabolism" – how does the sameness of kglyc translate into closer coordination of calcium oscillations? Is this simply the speed with which glucose sensing and insulin release are being cycled? Is metabolic "coupling" simply a coincidence – is this all simply an epiphenomenon?

Finally, the authors look at experimental data from connexin KOs (het and homs vs WTs). I found this data (even though we have seen this before) to be rather surprising given the previous narrative. In essence, what it shows is that a 50% reduction in GJs has a marked effect, and a total loss results in a near-complete loss of hubs. If connections, and therefore presumably networks that deliver hubs, can exist just based on random metabolic homogeneity in distant β cells alone, why does this happen? Is there any NADPH data from the connexin KO islets? With the loss of gap junctions, I can see why the amplitude of the calcium oscillations in β cells might become smaller, but why do other metrics of the oscillations eg frequency seem to change?

Figures

Figure 1 – Kglyc and g coup need to be defined/explained so the figure stands alone.

Figure 1b – the word seed is confusing/comes out of the blue. Do you actually mean "modelled islet"?

Figure 1 f/g – this may display my incomplete understanding of the different populations you defined and measured, but why was a paired t-test used to compare them and if these readings are truly paired were they really normally distributed?

Figure 2 – the defined cellular ROIs in a is not the same as the ones shown on your map in c – I was expecting them to be!

Again, here we have the notion of Kmax mentioned which needs defining in the legend.

Reviewer #4 (Recommendations for the authors):

1. The paper is very dense and complex, and thus is difficult to follow, and as a consequence will only be understandable to a very specific and likely small group of readers. The methods, the analysis, and the models used, while largely based on prior work require careful reading, and a true understanding of their implications will be mostly lost on most readers. The paper would therefore be improved by reducing its size and complexity and removing excessive verbiage. Some of the more mathematical aspects could be relegated to either previously published papers by the group or placed in the Supplementary Material. It might be worth considering breaking the paper into two different but complementary ones, one emphasizing theory and the other measurements but I realize this would make reading the two simultaneously very difficult.

2. The paper would also be improved by very clearly highlighting what is truly new in the paper and deemphasizing what is a restatement of what has been known already (e.g. discussing how the islet can be considered a small world network, etc).

Reviewer #5 (Recommendations for the authors):

I have a major concern about how cells related by cell metabolism and cells related by gap junctional coupling are treated as independent. There is no mechanism mentioned (?) for metabolism to synchronize islet cells independent of gap junctions. Consequently, I have concerns about the conclusions of the results.

This work seems to suggest a disregard of the necessity of gap junctional connections for islet synchronization, and suggest that functional connectivity – based on statistical correlation of traces – somehow predominate…up until Figure 6 where knocking down gap junctions is acknowledged as important.

I think identifying subpopulations is reasonable, but when a 60% functional connection threshold is what defines "hub" cells and that produces between 50 and 200 cells, "hub" seems to lose its meaning, especially when these "hubs" seems to be all grouped together rather than dispersed as might be expected in a small world network. The small network-ness is questionable. The sensitivity to the correlation threshold suggests a certain lack of robustness. Perhaps I am misunderstanding the number of cells labeled as "hub cells."

The excitability of cells via metabolism, for example, must be communicated through some (often structural) mechanisms. I appreciate that this article is attempting to get at how that division breaks down and I think much of the calculation and simulation is useful, but the language expressing the certainty rather than the more appropriate equivocation is not completely appropriate.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Β-cell Intrinsic Dynamics Rather than Gap Junction Structure Dictates Subpopulations in the Islet Functional Network" for further consideration by eLife.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #2 (Recommendations for the authors):

I much appreciate the effort that the authors put into addressing my main skepticism about the paper, namely the fact that one type of oscillations were analyzed for experimental data and another type for modelled data, by including an additional model for slow oscillations and additional experimental data.

Given the new results, below, I provide my additional comments and suggestions that should not be too difficult for authors to consider and take into account.

110-197 and Figures 1-S3:

First, the difference between hubs and non-hubs in terms of kglyc is around 0.14 vs 0.13, whereas for gcoup it is around 0.75 vs 0.6. In relative terms, the former is an 8 % difference and the latter a 25 % difference. It is true that the former is more significant statistically, but this is due to the fact that the heterogeneity is larger in the distribution of gcoup for hubs! Therefore, to me, it seems that both kglyc and gcoup seem to define the hub cells to a comparable degree. This conclusion seems to also be more compatible with findings for slow oscillations where the relative difference between hubs and non-hubs for gcoup is again around 20-30 %.

I suggest that authors consider this under the corresponding sections of results and discussion, and perhaps to some extent also in Figure 8.

Second, at a threshold for hub cells of a 60 % normalized degree (i.e., the criterion for the separation line between hubs and non-hubs), different percentages of β cells qualify as hubs for different simulated islets, as evident in Figure 1b. More specifically, the cumulative number of cells qualifying as hubs for islets 3 and 5 is much more than the cumulative number of hubs in simulated islets 1 and 2. This differs from the criterion used in other important recent studies, i.e., in Johnston et al. Cell Metab 2016, hubs typically represent 1-10 % of islet cells, in Lei et al. Islets 2018, hubs represent 10 % of cells, and in Stozer et al. Am J Physiol 2021 and in Sterk et al. Biophys J 2023, hubs represent 1/6th of islet cells. I think it would enhance the comparison between the present and previous research if the authors provided the % of hub cells per islet. Additionally, setting the line of separation between hubs and non-hubs at the given threshold (not changing the threshold and thus the distribution of normalized degree) individually for each islet to achieve a fixed percentage of hub cells per islet close to 10 % of the most connected cells, would be a valuable addition to supplemental figure 1 and could perhaps help detect a larger (or smaller) difference between this more extreme group of cells and the majority of non-hub cells, in terms of kglyc, gkatp, and gcoup. Performing this additional analysis at least for the threshold value used in the main Figure 1 could add much value to the manuscript and make the findings even more directly comparable with the aforementioned studies. The same suggestion could also be taken into account for the analyses of modelled slow oscillations and for the experimental analyses of metabolic activity and coupling, where 10 % of the most connected cells could be considered/classified as hubs as well. Such additional analysis should be easily feasible since it considers a fraction of cells that have already been used in the analyses, but their degree of "hubness" is probably more.

Given that the duty cycle (percentage of active time) so strongly correlates with the role of hub cells, it is somewhat surprising that the authors do not mention in the discussion that this same finding has recently been obtained for both mouse and human islets (Šterk et al. Biophys J 2023, Stožer et al. Am J Physiol 2021, Gosak et al. Diabetes 2022).

Third, I do value the effort of authors in replying to my comment regarding the exceedingly high correlation between simulated traces compared with experimental traces. However, besides noise, one very important aspect is the choice of model and the parameters which determine the observed lags between different cells or the wave speed. For instance, Cappon and Pedersen in their Chaos article built on the model used in Benninger Biophys J 2008 to produce lags between cells that are very realistic compared with experimentally observed values, whereas lags in the present study are just a fraction of the duration of a burst (fast Ca oscillation).

At present, I can only speculate about that, but the rather low conditional probability that two cells sharing gap-junctional conditions also show a functional connection could also be a consequence of the exceedingly short time lags between signals in the model employed in this study. More specifically, in the model by Cappon and Pedersen, there are waves travelling across islets and direct neighbors have shorter phase-lags between their signals compared with more distant cells and therefore on average more similar signals, similar to experimental recordings in isolated islets and tissue slices (the velocity being around 100 um/s, the time lag between direct neighbors is around 0.1 s and the time lag between most distant cells is around 1-2 s). This means that the values of R will be higher for direct neighbors and at any given threshold they will be functionally connected with a higher probability than with more distant cells where lags can be an order of magnitude more.

Therefore, I would suggest that in the future (not in this study), authors also repeat some of the analyses with modeled traces that show larger lags. This would probably also enable them to explore the relationship between different modelled/analyzed parameters and the role of pacemakers, i.e., wave initiators and other populations of cells. Perhaps, if authors consider the above suggestion as useful, they could include it in the discussion as a possible drawback of the present model and as a suggestion for future studies.

Reviewer #5 (Recommendations for the authors):

The authors have thoroughly responded to my (and others') reviews. I think their modifications are reasonable and have tempered the language appropriately. The results are somewhat interesting and the techniques employed to measure and analyze the islets including adding an additional model system are extensive. They have addressed my points.

One point: We discussed (Reviewer #5 question/response 5b) the potential outlier at 2.35 of Figure 1f (gkatp data – Β Cell Hubs). That data point no longer exists on the graph (that I can see?). Since they argue convincingly that point should in fact not be treated as an outlier, I expect it is an oversight of it not being there. This should be fixed (or explained) prior to moving forward with publication.
