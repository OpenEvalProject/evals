# Peer review - Round 1

Editors:
- Karel Svoboda, Janelia Research Campus, Howard Hughes Medical Institute , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20252.014](https://doi.org/10.7554/eLife.20252.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Structural determinants of granule cell activity in the dentate gyrus of freely-moving rats" for consideration by eLife. Your article has been favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom, Karel Svoboda (Reviewer #1), is a member of our Board of Reviewing Editors, and another one is Matthew F Nolan (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript describes loose-seal cell-attached recordings from hippocampal granule cells (GCs) in awake rats. We know relatively little about these mysterious cells. Previous experiments have explored granule cell activity using tetrode-style recordings or maps of cFos expression. These methods have suggested that GC activity is sparse – in the sense that only a small subset of GCs are active in any one environment – but both methods are imperfect. Extracellular recordings are biased towards active cells and sample neurons with more membrane area more efficiently. Loose-seal recordings are unbiased in the sense that active and inactive neurons are recorded. The authors find ultra-sparse activity in GCs, providing the strongest evidence to data for sparse coding in the dentate gyrus. Loose-seal recordings in addition allow labeling and reconstruction of a subset of recorded neurons. This provides the additional insight that active neurons are larger and spiny. This is a nice and simple structure-function relationship. These findings of specific structure-function relationships within the (mature) dentate granule cell population are novel and very interesting, and would constitute a valuable contribution to the field.

Essential revisions:

All reviewers have reservations about the strength of the statistical analysis used to support the main conclusions and presentation of the data. We suggest that you take the comments below as a guide to reanalyze the data set.

1) Details on the GC recordings and morphological parameters should be provided. We suggest a supplementary table containing all neurons as separate entries with these data: duration of recording; number of spikes recorded; identity of the animal; duration of the recording; distance covered by the animal; aspects of receptive field shape (i.e. place field attributes), morphological parameters; which analysis and figure the neuron contributed to. This table should allow independent analysis of the dataset. The detailed dendritic structures should be deposited at neuromorph.org or another repository.

2) Given multiple comparisons of dendritic structure were made, it is unclear if corrections for multiple comparisons were made. This is related to the hot topic of 'p-value hacking'. Please make sure to take multiple comparisons into account.

3) The study reports numbers of neurons, treating each neuron as an independent observation. Could the apparent relationship between activity and dendrite morphology instead reflect a subset of animals in which granule cells are more active with more complex dendrites? The possibility of non-independence of observations should be accounted for in the statistical analysis.

4) The description of the classifier and its evaluation is not sufficient. What properties of the spike waveform were used for training? What was the exact composition of the training and test datasets? Is it just the 47 neurons in Figure 1D? This is a somewhat small number of samples compared to datasets often used for training classifiers. What was the false positive and false negative rate when testing the classifier? What was the quantitative criterion for shoulder or no shoulder in Figure 1D? Figure 1G indicates that the shoulder is variable and not present in all granule cells. Does this have implications for interpretation of the data and what are these?

5) Figure 4D. The legend indicates that "the distributions" are statistically different. Is this referring to length, distance, or length data as a function of distance as shown in the figure? The conclusion is based on results of a Mann Whitney U which would usually be used to test for a difference in medians. It is not clear how this was applied here.

The analysis of morphology and its presentation needs to be improved. Assuming that the morphologies of the 7 silent and 6 active granule cells analyzed in detail are complete and representative, the main conclusions of the study are fairly straightforward. Therefore, it is important for the authors to devote more of the manuscript to their morphological methods and clarify their procedures in more detail.

6) The authors write "we reconstructed the somato-dendritic compartment of 7 silent and 6 active GCs, which were selected for the morphological analysis due to their high-quality filling and complete dendritic morphology." What were the criteria for assessing the completeness of the dendritic morphology? Was the labeling protocol standardized in some way between silent and active neurons? For instance, is it possible that it was harder to fill silent cells than active ones? What is the fraction of silent cells for which labeling was attempted whose dendritic tree was completely filled, and how does that compare to the fraction for active cells? If there was any difference in the rate of complete filling, could it be possible that there was a bias in the labeling method that could lead to an apparent difference in the level of branching or complexity? Is it possible, for example, that silent cells were harder to fill and more likely to have somewhat less complete dendritic fills, and thus more likely to appear to have less complex trees?

7) The branching and complexity measures that show a difference between active and silent cells are defined in the methods: "The 'branching index' was defined as the number of dendritic endings divided by the number of primary dendrites. The 'complexity index' was computed as in previous work (Pillai et al., 2012) according to the following equation: (sum of branch tip orders + number of branch tips) x (total dendritic length/total number of primary dendrites)." These measures appear to be particularly sensitive to the number of primary dendrites as it appears in the denominator in both cases. Therefore, the authors should include in the table mentioned above, for each of the 13 neurons with complete dendritic trees, the firing rate in the arena, the branching and complexity values, the total dendritic length, the number of dendritic endings, and the number of primary dendrites. The authors write that there was a non-significant 2x difference in the number of primary dendrites "(the number of primary dendrites (active, 1.1+/-0.4; silent, 2.2+/-1.1; p=0.08)", but the branching index also differed by 2x "(branching index; active, 14.6+/-4.6; silent, 7.8+/-4.7; p=0.026)", though this difference was significant. This suggests that the number of dendritic endings is similar for both silent and active cells. Therefore, is it possible that the difference in the number of primary dendrites could be responsible for differences in activity, instead of the difference in spine number that they suggest as the cause? In comparison, the number of spines differed by a factor of 1.4x "(total number of spines; active, 1802+/-353; silent, 1354+/-257; p=0.035)" and they state "The total number of dendritic spines also showed a significant correlation with firing rates (r=0.63; p=0.019; n=13)". What is the correlation between the number of primary dendrites and firing rate and associated significance?

8) The authors write that "The large majority of sampled neurons were silent (see Figure 2F). In order to record from spiking GCs, silent recordings were routinely discarded by further advancing the electrode within the layer." Does this mean that their sample was biased toward more active cells? If so, they should clearly point this out when they state proportions of cells that were active. For instance, they state "Active GCs were thus very sparse, consistent with previous estimates (Jung and McNaughton, 1993; Leutgeb et al., 2007; Neunuebel and Knierim, 2012) and accounted for only ~14% (32 out of 228) of all blindly-sampled neurons within the GC layer." If they biased their search for active cells, then they should remove "blindly-sampled" from this sentence and point out that the 14% value is an overestimate based on their sampling method. In addition, is it possible that any bias in the search toward active cells could influence the morphological results? For instance, is it possible that cells that are active during the search and active during exploration of the arena are not a random sample of the entire set of cells active during exploration? Perhaps these cells have more branching and complex dendritic trees compared to cells that are active during exploration but were not spontaneously active during the cell search procedure? The basic question is whether the sample of 7 silent and 6 active cells analyzed in detail morphologically constituted an unbiased sample of silent cells, and an unbiased sample of active cells, respectively. If the possibility of such a bias cannot be ruled out, yet there is no reason to think there is a bias, the authors could just make a short comment about how they assume their methods have isolated a random sample of silent and active cells.

How long did they wait before discarding silent cells? This defines an upper bound on the possible spike rate of silent cells.

The authors recently showed that they could induce place fields in some granule cells by juxtacellular electrical stimulation (Diamantaki et al. 2016). Does this effect also correlate with dendritic structure? Please discuss.

The paper should be more tightly framed in terms of measurement of sparseness (additional literature should be cited) and structure-function-relationship.

[Editors’ note: a previous version of this study was rejected after a second round of peer review, but the authors submitted for reconsideration. The decision letter after this second round of review is shown below.]

Thank you for submitting your work entitled "Structural correlates of granule cell activity in the dentate gyrus of freely-moving rats" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor (Karel Svoboda) and Eve Marder as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Karel Svoboda (Reviewer #1) and Matthew F Nolan (Reviewer #2).

Our decision has been reached after consultation between the Reviewing Editor and the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

We note that the reviewers remain very positive about the data set and the finding of sparse coding in the dentate gyrus. However, the focus of the manuscript is the link between activity and dendritic structure (the title is 'Structural correlates of granule cell activity in the dentate gyrus of freely-moving rats'). Given this focus all reviewers and the Reviewing Editor remain concerned about the statistical analysis linking activity and dendritic structure. Some commonly used measures of dendritic complexity, such as dendritic length and the number of primary dendrites, showed no significant effect, whereas some less intuitive measures (i.e. 'dendritic complexity') did, but at modest levels of significance. Most of the reported measures are related and thus not independent. There are some indications that the study may be underpowered to make conclusions about dendritic structure. We are not convinced that the results were corrected for multiple comparisons together in an appropriate manner. For these reasons we cannot publish your manuscript in its present form.

However, we would be happy to consider the manuscript again with one of the following major revisions:

1) A more compelling statistical analysis. This could take the form of a rigorous analysis of multiple comparisons. Alternatively, a reanalysis with randomly chosen 50% of the data might also be appropriate.

2) Addition of data that make the conclusions about structure-function relationships stronger.

3) A refocusing on sparse coding in the dentate gyrus.

Reviewer # 1:

The paper is improved in many ways. However, the analysis of dendritic complexity remains suggestive, but not convincing.

Was the study design a priori to test the relationship of spike rate and the specific measure of dendritic complexity? If so, the analysis is appropriate. However, if this was exploratory then the stats are weak. The reasons are as follows.

There is one effect – higher dendritic complexity for higher spike rates. All the positive effects come from the same data and follow from each other; thus there is no independent second measurement. Of course, If one does enough comparisons there is bound to be one that is 'significant' by chance. I don't see a proper analysis of multiple comparisons (this may be hard to do).

Multiple testing and reporting significant results produces a publication bias. In other words, statistically significant findings are reported, increasing the rate of false positives in the literature. This is a prime cause of the poor replication record in psychology, MRI, cancer, and likely systems neuroscience.

Figure 4F seems to have 11 points, not 13. It is hard to believe that the p value is < 0.01

Reviewer #2:

The manuscript is substantially improved. However, I'm not convinced the issues related to multiple comparisons have been adequately addressed (points 2 and 5 in the original review).

The investigation of the relationship between activity and morphology requires comparing many parameters. Of course, by chance some of these comparisons will turn out significant at a p < 0.05 level. At the moment this possibility is not accounted for in the interpretation of the data. The challenge here seems to be to introduce an appropriate correction.

Using the Benjamini & Hochberg method to correct the p-values most of the significant differences appear to go away. An exception appears to be the 'Dendritic Length Order' measure. Even here one should perhaps be a little cautious as additional comparisons were made and correcting for them would reduce the significance level further – it is unclear how many comparisons one should correct for.

Given these potential issues, the question is what to do. I appreciate the challenges in obtaining the data, but in a sense this makes it even more important to be rigorous in interpretation. One option might be to carry out additional experiments to try to replicate the results with the analysis focussed on specific planned comparisons. An alternative could be to clearly label the study as exploratory.

Different multiple comparison issues apply to Figure 4D. I also don't understand how total dendritic length can be similar between the two groups, but the area of the plots in 4D looks quite different.

Additional comments:

The table only includes a subset of the measurements used for the analysis. It would be more helpful if all measurements are included.

It's not clear why the Abstract reports correlations rather than results of comparisons between active and silent neurons.

The recording duration is longer for active than silent cells. Is this an issue?

Reviewer #3:

The authors have adequately addressed my questions and concerns. I have a few remaining comments:

From the table, the numbers that stand out most are the differences in the number of primary dendrites, even though this did not reach significance.

In the Abstract, the authors write "We found that the majority of neurons (163 of 190) were silent during exploration." However, I recommend that the authors remove the numbers since it reads as if it is an unbiased estimate of the fraction of silent neurons, but they confirmed in the response that this is likely to be underestimate due to their search procedure. Instead they could add "vast" in front of "majority" to make their point.

In the Figure 2 legend the authors write "Unlike extracellular recordings, juxtacellular sampling is not biased towards active cells, since silent neurons can also be recorded and their presence confirmed by current injection." This is followed by "Cumulative plot showing the firing rate distribution within the GC layer. Each red circle represents one neuron, sampled juxtacellularly within the GC layer (see Methods for details). Note the large proportion of silent neurons (163 out of 190) compared to active cells." However, as acknowledged by the authors, their sampling of the proportion of active and silent cells is likely to be biased due to their search procedure, where inactive cells were often discarded early during exploration, before the 60-second threshold they used for counting the cells. Because of this, I think this statement and the numbers could confuse the readers into thinking that these numbers are an unbiased estimate, and one that is a better estimate than obtained with other methods. It would be a better estimate if their cell search / counting procedure was unbiased, but apparently it was not. The correct proportion is an important number. The authors should therefore clarify this in the legend as they have done in the main text. For example, they could write in the legend "Note the large proportion of silent neurons (163 out of 190) compared to active cells. Furthermore, this proportion is likely to be an underestimate of the true silent proportion due to the details of the search procedure (see text and methods)."

[Editors’ note: what now follows is the decision letter after the authors submitted for reconsideration.]

Thank you for submitting your article "Sparse activity of identified dentate-gyrus granule cells during spatial exploration" for consideration by eLife. Your article has been favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom, Karel Svoboda (Reviewer #1), is a member of our Board of Reviewing Editors, and another one is Matthew F Nolan (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript describes loose-seal cell-attached recordings from hippocampal granule cells (GCs) in awake rats. We know relatively little about these mysterious cells. Previous experiments have explored granule cell activity using tetrode-style recordings or maps of cFos expression. These methods have suggested that GC activity is sparse – in the sense that only a small subset of GCs are active in any one environment – but both methods are imperfect.

Extracellular recordings are biased towards active cells and sample neurons with more membrane area more efficiently. Loose-seal recordings are unbiased in the sense that active and inactive neurons are recorded. The authors find ultra-sparse activity in GCs, settling and quantifying the issue of sparseness in a definitive manner. Loose-seal recordings in addition allow labeling and reconstruction of a subset of recorded neurons.

This is a revised submission, which is more tightly focused on sparse coding in the dentate gyrus. The analysis of structure-function relationships is now done using a classifier with multiple structural parameters considered jointly. The classifier reveals that structure predicts function.

Essential revisions:

Although the classifier can use structure to predict function, the relationship is subtle and can't clearly be boiled down to simple measures (at least given the limited data set) (see also Figure 4—figure supplement 1). It would be good to make this last point clearer (the relevant statement in the Discussion is not accurate and should be revised).

Describe more clearly what a primary, as in 1st order, dendrite compared to a 2nd order dendrite. This is because (1) it appears from the table that this this would have a large effect on distinguishing active and silent cells, not just in terms of the total 1st order length, but also in terms of the total higher order lengths (since a 5th order branch would be a 4th order branch if the 2nd order branch it came from was instead called a 1st order branch), and (2) the table shows that the 1st order branches are generally short. Therefore, in the Figure 4—figure supplement 1 the authors should include beside each neuron a close-up of the somatic region showing the soma, 1st order branch(es), and start of 2nd order branches, ideally with markers to show where the divisions are.

It would be valuable to the community for the authors to include some of the data from the original manuscript in the source file on morphological parameters, such as the "soma location within the GC layer" and the "laminar location of the cells (suprapyramidal versus infrapyramidal blade)."
