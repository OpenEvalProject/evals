# Peer review - Round 1

Editors:
- Sarah E Cobey, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73896.sa0](https://doi.org/10.7554/eLife.73896.sa0)

This study provides important observations about the transmission of SARS-CoV-2 lineages within Canada and the importation of lineages into Canada over the first year of the COVID-19 pandemic. This information is critical for understanding SARS-CoV-2 evolution and epidemiology, including the potential impacts of travel restrictions.


---

# Peer review - Round 1

Editors:
- Sarah E Cobey, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73896.sa1](https://doi.org/10.7554/eLife.73896.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Early introductions of SARS-CoV-2 sublineages into Canada drove the 2020 epidemic" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by David Serwadda as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Bernardo Gutierrez (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All reviewers thought this study represented a potentially valuable contribution. They also all expressed concern about the impact of potentially biased sampling on the conclusions. We recognize that this is a general challenge in the field, and not all papers in it have necessarily faced this level of scrutiny. Because the conclusions of this paper are quantitative, it seems important to quantify the uncertainty (in this case, to model misspecification/sampling bias) accurately.

The reviewers outline nuances in their individual commentaries below, but there are effectively three general issues:

1) It seems particularly important to understand (e.g., as a sensitivity analysis) the impact of not downsampling the samples from Canada.

2) Reviewers also asked whether the case-based scaling of sequences is appropriate. This relates to a more general problem raised by the highly uneven sampling by country and region. Downsampling so that no region is overrepresented with respect to its relative infection load would leave zero samples for analysis, since so many areas are missing sequences entirely. Perhaps again performing some kind of sensitivity analysis or referencing a more thorough investigation of this problem, how does uneven representation impact estimated migration rates?

3) The reviewers were also concerned with the estimate of the total number of introductions.

Effectively, all the reviews are requesting a more careful treatment of potential problems with data collection (it is not random!), both in the analyses and in the text.

Reviewer #1 (Recommendations for the authors):

A few other statistical questions are raised in the recommendations for the authors below.

Statistics/methodology

1. p. 5, l. 3: Clearer logic in the "Subsampling" section would help. What is the justification for subsampling proportional to case number, which is obviously quite biased by surveillance effort, perhaps even more biased than the number of sequences? Why not subsample proportional to countries' population size or excess mortality, adjusted for age? It would be helpful to describe too how much subsampling occurred and that it was necessary for computational reasons. What kinds of biases are still present? For instance, it would be good to point out somewhere the regions/periods that are so poorly sampled (e.g., in many lower income countries) that the inference could be biased to favor endemic transmission, assuming my intuition is correct.

2. p. 8, ll. 6-8: Could you explain the logic of how the total number of introductions was inferred given the estimated rate at which cases were sequenced (and cases detected)? Should the estimated number of introductions scale linearly?

3. p. 12, ll. 6-9 (Figure 4C): Does this model properly adjust for the typical delay between sampling members of a sublineage? Sublineages with more recent tMRCA should have fewer descendants simply because less time has passed. It is not clear the stratification takes care of this. There might also be a decrease in the number of descendants with time if the total number of sublineages is increasing and surveillance does not scale with sublineage richness. The text reads "To elucidate the relative contributions of early and late sublineages,….," but it is unclear exactly what contribution is being measured here.

4. p. 10, ll. 10-11 (Figure 4D): I think we could see an increase in days since importation over time even if more recently imported lineages were generally more common ("dominant"). The maximum possible age of the oldest lineage is increasing with time. The sentence says this "suggests" that early introductions "increasingly dominated" the epidemic. Maybe it would be easier to demonstrate this through specific examples or a measure of persistence time and a proxy of prevalence.

5. p. 18, ll. 6-8: "Sequences from individuals with travel history to Iran or Italy before June 2020 were recategorized as having been sampled in the country of travel." Why was this not done for individuals with travel history from other countries?

Interpretation

1. Abstract: "Rapid implementation of stringent border controls and quarantine could have diminished the Canadian COVID-19 burden by curtailing the spread of early introductions." I question how much stringent border controls, unless defined very severely as prohibiting the introduction of, e.g., more than ten lineages, could have diminished the COVID-19 burden. Once any lineage is established and transmitting in the community, additional introductions have negligible impact on prevalence or the "final size" of an epidemic. Quarantine, by reducing the effective reproductive number, can reduce burden. I worry that lack of precision on the impact of introductions on burden can lead to the sort of knee-jerk travel bans we see with Omicron.

2. p. 3, ll. 7-8: "can illuminate"? Deciphering the rates of imported and domestic transmission is not guaranteed.

3. p. 8, l. 8: A 42% infection detection rate (as cases) struck me as rather high. The cited reference appears to be for something else.

4. p. 10, ll. 1-3: What is the purpose of mentioning the number of global descendants when it is known to be such an underestimate?

5. Figure 4. It would be useful to reference 4A and 4B specifically in the text.

6. p. 15, ll. 4-6: How can we separate the impacts of behavioral changes (NPIs) from seasonality on sublineage size and duration?

7. p. 15, ll. 22-24: Where is the mandatory 14-day quarantine coming from? Given the incubation period and duration of shedding, I know many who think quarantine should be shorter (if testing were not feasible). With sensitive testing, there is no reason to keep people past a week if they are consistently negative. I think it's important not to imply the traditional durations used for quarantine are especially grounded or optimized.

Potential enhancements

It would be interesting to see how the importation rates from different countries correlate with air travel to/from those countries. I realize this is difficult given connecting flights, but perhaps the data exist somewhere.

p. 16, ll. 11-14: Ideally these nonstationary sampling probabilities by province (and really for all countries) would be built directly into the likelihood.

Reviewer #2 (Recommendations for the authors):

1. Line 17-21 argue genomic epidemiology is useful to track and characterize VOI/VOC, but the sequences analyzed in this manuscript are largely pre-VOC so I think it makes sense to re-focus and expand this discussion to include commentary on the importance of evaluating the success of public health interventions, travel restrictions, etc.

2. I think outlining a hypothesis at the end of the intro is useful, but as it is currently written the hypothesis is very long and difficult to understand. Can the authors restate and clarify the hypothesis into a single sentence?

3. As the authors discuss, their results and those of all genomic epidemiological studies are very sensitive to sequence quality, availability, distribution, and sampling paradigms. They reduce the impact of unequal global sequencing efforts by subsampling global sequences proportionally to their monthly case counts, excluding Canadian sequences. I understand the rationale here, but worry that inclusion of all available Canadian sequences (which are not proportional to case count trends as is clear in Figure 1D and 1E) skewed their results. Perhaps one way to assess the robustness of the results would be to repeat the main analyses using a subsampled (proportion to case counts) Canadian dataset and compare results? Relatedly, even case counts could be skewed depending on testing availability and accuracy -- could the authors include a brief commentary on the availability, accessibility, and capacity of testing centers in Canada during the first year of the pandemic?

- it is also clear to see in Figure 1C and 1F that US sequences are overrepresented in this dataset compared to case counts -- do the authors think this is inflating the proportion of US imports? (I agree it is clear most imports came from the US)

- the Alberta and Maritimes outbreaks in spring of 2020 appear very striking (large outbreaks with lots of person-to-person spread and very few descendants) in Figure. However, this interpretation is fraught when you consider Figure 1E and 1D because there are lots of available sequences during this time compared to the total case count vs fall of 2020 where there is actually a higher case burden and very few available sequences. I think many readers will get hung up on this so maybe the authors could address it briefly in the text?

- While the color scheme is lovely, it is difficult to distinguish between some provinces particularly in Figure 2

4. Lines 6-10. I think it is a big leap to estimate the total possible introductions based on sequences representative of 1.1% of total cases.

5. It might be very informative to take a more careful look at rates of viral spread (R0) over time in addition to patterns of viral importation. This could help contextualize the effect of public health interventions on domestic spread. The authors bring up quarantine, contact tracing, testing, and individual behavior change in the discussion -- do the authors think the rate of international imports is the best measure to assess these interventions? I think R0 would be just as informative!

6. I am skeptical the results on reductions in sublineage size, increasing tMRC, and perhaps even sources of domestic transmission will persist if the Canadian sequences are subsampled proportionally to case counts. Can the authors please assess the robustness of these results against a subsampled dataset?

7. I agree with and appreciate the authors' discussion of the importance data sharing, including a limited metadata set to aid in the rapid interpretation and use of sequence data for important public health decisions.

8. Although this is a stylistic preference, I believe a cleaned up version of Figure 7 with the Canada's key public health interventions and COVID-19 outbreaks along with a map of Canada's provinces (already a supplemental) and case counts during the study period would be very useful to include as an early, primary figure.

Reviewer #3 (Recommendations for the authors):

My main concern lies on the explicit naming of sources of importation following the application of an epidemiologically-based approach to downsample the publicly available genome sequences from GISAID. While it is mentioned that ten subsamples were generated, it is not clear to me that the ancestral state reconstruction was evaluated on these ten subsamples and how the results compare between them. The uncertainty of the ASR itself was incorporated for the fixed phylogeny through an ML approach (ape::ace()), but I am missing the analysis of the robustness of the results across different subsamples.

Furthermore, even if these analyses where performed, it is unclear whether a different subsampling approach could lead to the identification of a different profile of source countries, and if so, which subsampling approach would be more accurate. The accuracy of the identified countries of origin (and therefore accuracy of the proposed downsampling approach) would be validated if a complementary data source showed similar patterns: an expected importation index (EII ~ Incidence * no. of travellers to Canada), self-reported travel histories of patients with confirmed COVID-19, etc. If these complementary data sources are unavailable, I would recommend reducing the emphasis on the identification of countries of origin (or constraining it to regions where you're confident that the monthly reported cases are reliable – the USA would be an obvious example of this), or adding a clear discussion on these limitations. I would argue that this goes beyond the already mentioned idea that downsampling does not allow to increase the numbers of sequences from some unsampled times/locations (page 16, lines 5-20), and that it can also reduce the probability of phylogenetically identifying true importations from countries with low case prevalence.

On other topics: I am unsure about the estimation of total number of introductions presented in page 8 (lines 6-10). Do you have any particular reason why you would expect that importations scale linearly with sampling/representation? Given the overall dynamics, wouldn't it be more probable that higher sampling intensities would add unsampled sequences to the larger sublineages in the country (proportional to the size of the lineages) as well as uncovering unsampled importations? The rationale behind these calculations requires some more detailed explanations.

Regarding the domestic transmission, I was wondering if you had access to finer geographical resolution beyond province-level? Provinces are particularly large geographical areas, and providing some insights (rather than a full, high-resolution phylogeographic re-analysis of all the data) into the sampling within provinces could add to the manuscript. This is particularly the case for the analysis of international importations to Quebec and Ontario: where these sublineages first detected in large urban areas or not necessarily? Is the sampling within provinces representative of the cases reported in urban and rural areas? Are there any differential dynamics between larger urban areas and more remote locations?

Finally, it is quite interesting to see that the peak of TMRCAs nicely coincide with the maximum stringency on March 21 (Figure 4A,B) – even more so given that the TMRCA of a sublineage is more likely representing something akin to the first transmission event within said sublineage rather than the importation event per se. It would be interesting if the TMRCAs could be contextualised to show their distribution after accounting for sampling lag (i.e., the time between symptom onset and sample collection). This could be estimated from sequence metadata or approximated from non-genomic epidemiological data, but it would give a better idea of the times during which the infections that lead to these sublineages started.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Genomic epidemiology of the first two waves of SARS-CoV-2 in Canada" for further consideration by eLife. Your revised article has been evaluated by Sara Sawyer (Senior Editor) and a Reviewing Editor.

The manuscript has been dramatically improved---the sensitivity analyses are immensely helpful---but there are some remaining issues that need to be addressed, as outlined below. The reviewing editor is concerned that some of the policy suggestions do not follow the evidence presented.

1. Abstract: "… suggesting travel restrictions and quarantine must be sustained to fully curtail COVID-19 burden." I am guessing most readers will likely interpret "to fully curtail COVID-19 burden" as to get the burden near zero. Is this what the authors intended? It affects the logic. The results here show that travel restrictions were usually associated with at least several importations per week. Mathematically, we know that the burden of COVID-19 does not really depend on the number of importations if R ~ 1 or more---all you need is at least one endemic lineage to maintain the prevalence/burden dictated by R. Maybe the authors are referring to conditions when R<1 and travel restrictions are even greater than what they have been historically, but this is unclear. It is also unclear precisely what the authors mean by "quarantine." Usually, it refers to the isolation of contacts of potential cases (not the cases themselves), and sometimes it refers more generally to lockdowns. Neither policy seems particularly worth calling out here. Why not say "sustained interventions to lower transmission (R<1)"? It seems unjustified for this study to single out quarantine (either def) as the necessary complementary intervention when so many other approaches have been shown more effective. I'm dwelling on the wording because these kinds of conclusions, especially in an abstract, can have an outsized impact on policy.

2. Abstract: "…restrictions that reduce the probability of importations are most effective during periods of low domestic prevalence and low or waning immunity." Waning immunity means R is rising, which, all things equal reduces extinction probabilities and increases the success of invading lineages (e.g., Otto and Whitlock 1997). Without more precision about R and how effectiveness is being defined, it's not clear restrictions should be more impactful under these conditions. I do see the positive correlation between "periods of waning immunity" and possible ban-assisted extinction, but only because immunity is most often waning when there has recently been an epidemic, and the recently boosted immune protection is relatively high. I worry again about the implications of these claims, which are not exactly supported by the research here.

3. Relatedly, the main text describes evaluating the relative contribution of (reducing) importations to (reducing) *burden* (e.g., ll. 190-192, ll. 605-607, 691-701), but this analysis is not really performed here. Such analysis would require careful estimation of R and prevalence and a good enough transmission model to evaluate extinction probabilities and outbreak sizes (in the case of R<1) over time, and it would have to account for clonal interference. Put differently, the fact that imported lineages caused x% of cases does not mean that the case count would've been (100-x)% without those importations. The fact that imported lineages displaced resident lineages does not mean the resident lineages could not have caused comparable infections had the imported lineages been stopped at the border, assuming the imported lineages had no fitness differences. Imperfect travel bans that allow some lineages to invade can at best slightly (at measured rates) change the timing of an epidemic (ll. 704-707), but usually not its size or severity. The authors write, "Although blind travel bans may not be beneficial from a socioeconomic perspective, ultimately governments need to protect citizens and dynamic travel bans are one of the few tools available." This is surprising considering the number of broader tools at our disposal (e.g., rapid testing, vaccination, ventilation/filtration) that can slow importations AND endemic spread, as well as the observed ineffectiveness of travel bans at stopping spread outside of islands and China. The authors IMO have not demonstrated how much bans could delay importation and allow time to "plan", or if investments to reduce transmission generally are more effective. I suggest these claims be carefully reconsidered.

I apologize for the wordiness. I would be happy to bolster these points (maybe with math) if they are unclear. I am concerned that too much is being extrapolated about the possible and actual epidemiological impacts of travel bans from the measured rates of importation.

You may wish to consider some suggestions to improve readability from another reviewer:

4. In line 424, I'm not entirely sure what the authors mean by "the first wave of singletons had a higher amplitude than the second wave". By 'amplitude', do they refer to the range of dates when singletons were identified between both waves? Is this relative to a feature of the importations of sublineages (given that this sentence talks about this comparison between sublineage and singleton dynamics)? Some clarification would be helpful.

5. The Discussion addresses a lot of the reviewer comments thoroughly and systematically, which was very helpful, but could be streamlined for the readers. I think that, for example, the two paragraphs that go from line 711 to line 741 could be reduced to a single paragraph discussing 1. sampling bias in phylogeography, 2. the specific effects of overrepresentation of some locations and how they addressed it with subsampling and the sensitivity analyses, 3. effects of upsampled lineages and under-sampled locations and how this can theoretically be overcome, 4. the broader challenges of scaling up Bayesian phylogenetics (this last point could be a separate paragraph, but unrelated to sampling bias).
