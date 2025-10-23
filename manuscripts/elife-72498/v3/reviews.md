# Peer review - Round 1

Editors:
- Chunling Yi, https://ror.org/05vzafd60 Georgetown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72498.sa0](https://doi.org/10.7554/eLife.72498.sa0)

This article examines the role of p53 in cell division by using a combination of live-cell imaging, cell tracking, and simulations. Overall, the results are extensively and transparently documented and are of interest to cell biologists studying cell division, cell death, and p53.


---

# Peer review - Round 1

Editors:
- Chunling Yi, https://ror.org/05vzafd60 Georgetown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72498.sa1](https://doi.org/10.7554/eLife.72498.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Empirical single-cell tracking and cell-fate simulation reveal dual roles of p53 in tumor suppression" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jeroen S van Zon (Reviewer #1); Brian E Chen (Reviewer #2); Colarusso Pina (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The manuscript needs major rewriting to make it more comprehensible to a general audience. Please rewrite the manuscript according to the specific recommendations from the three peer reviewers.

2) Please provide better explanation of the simulation algorithm and the assumptions behind it in plain language.

3) Please revise the figures according to the specific recommendations from the reviewers.

4) Please better discuss the general impact of this study in the Discussion section.

Reviewer #1 (Recommendations for the authors):

1) Limited lineage analysis.

In general, the combination of cell tracking and manual annotation of events in general is powerful and I think the analysis of cell fusion in Figure 6 is a nice example of this power. However, I think it is under utilised in the paper. Figures 2 and 4 could have been constructed without cell tracking and lineage analysis, but only by analysing total cell number (Figure 2) or by counting events without lineage information (Figure 4). In Figure 3, lineage structures are analysed (but in a way I don't understand, see further below) but apart from changes with increasing MNNG it doesn't provide much insight: it seems that cell proliferation/death is decreased/increased with stress (as expected) leading to fewer large lineages, with no compelling difference between p53 siRNA or control. There is a sentence ('For example, suppression … generate 10-12 progeny (Figure 3b)’) that suggests there is a difference, but I can't see it in the figure.

It also seems that for a single condition, not all lineages have the same number of progeny (e.g 1-3 vs 13-15). Why is it that for the same imaging time lineages have such different offspring? Is it because some cells die? Is it impacted by limits to cell tracking, e.g. if a cell moves out of the field of view it gives rise to a short lineage because the offspring cannot be followed? In the latter case, that would rather represent a technical limitation rather than biological insight.

2) Insight in simulation lacking.

The section 'Cell-fate simulation algorithm' gives information on highest-level procedure of simulating, but it lacks any discussion of assumptions: does each cell choose 'fate' (MD, CD, CF, etc.) independently, or are correlation between sisters, cousins, etc. taken into account? How is experimental data used to constrain parameters of the simulation? The explanation in the supplementary information was not understandable for me. The presentation of the simulation algorithm in Figure S7a-h seems too detailed (e.g. dealing with the choice to load a file or not at the top of Figure S7b), while some of the diagrams (e.g. Figure S7F) are so complex that it appears to me as if a coherent underlying model is lacking. At the very least, it made it impossible for me to check the validity of the underlying assumptions.

3) In silico data generation.

in Figure 5, in silico data is generated based on experimental data, to asses the role of cell death. However, the explanation raises questions. It says that for any cell that dies its lineage was replaced by that of its sibling. But this only works if lineages without any cell death are always symmetric between siblings. Is this indeed the case? Or can you find cases where one sister generates 4 daughter but the other only 2? In that case, it is not clear what the in silico data represent. This is not discussed anywhere

4) Space in simulations.

In the simulations in Figure 9-11, space is taken into account, but I could not find how this is incorporated in the simulations. Also, it is not clear why space is relevant to begin with. It seems the cells are not directly interacting, e.g. by signalling, so could these results not have been obtained by simulations without space? Or is there competition for space? And if cells fuse, do they fuse with a neighbor? This should be explicitly discussed in the paper.

5) Writing and terms unclear.

In many places, explanations are not clear (see below for examples). The authors use a lot of acronyms, which I partly understand, but some sentences become very hard to understand (e.g. p.33 'we asked how progeny of MD that undergo BD survive by performing a simulation in Std mode'). Captions are strangely formatted and seem to sometimes miss panels (e.g. (b) lacking in caption Figure 3, (c) + (d) lacking in Figure 8).

Reviewer #2 (Recommendations for the authors):

Overall the study is very well done. There are several areas that can be better clarified.

The sentence, "However, the function of maintaining low levels of p53 in unstressed cells remains unclear." Is not a great introduction to the rationale of the paper; in that maintaining low levels is not what is being investigated, nor the function of the low levels, nor really the differences between low and high levels.

It is not clear throughout the text what "cell-lineage datasets" means. This could mean many things to many different readers. A sentence as to how the authors will define it is very important. Datasets can mean anything.

Similarly, the quantification of lineage is also ambiguous. How is this defined/quantified? This is never stated in the Methods, and again can mean different things.

The entire section on "Minimum number of cell-lineage datasets required to build a cell-lineage database" is unclear. Is this a random subsampling analysis that is being performed? Are these from experimental triplicates in Supplementary Figure 3, or just a randomly subsampling, as is implied in the statement, "The analysis was repeated three times (green, orange, and red lines) to show variations at a tracking time," so only the analysis was repeated three times, but not the experiments? What is the relationship between all of the datasets starting at 100 cells in the y-axis, but having different numbers of cell lineages?

Quantification of the cell lineage categories was unclear. What does "7-9 progeny" mean? The "number of cells/lineage" (text within the figure) vs "number of progeny/lineage" (main text) doesn't make sense. This is further confused by the Figure 3 legend stating "Values shown in (a) are number of lineages". So if the bar graph is read, then 136 cell lineages had around 350 cells, and 127 cell lineages had 900 cells. This is extremely confusing.

Why are cell densities in control and p53 RNAi in Figure 2 always the same, if MD, CD, and CF are all highly induced after RNAi knockdown?

The normalization factor, "/300 lineages" is not clear. This makes it difficult to compare the rates of the MD, CD, and CF between experiments across the paper. For the numbers "0.0475, 0.125, and 0.0775 events per 10 min/300 lineages" to mean anything substantial to any reader, it should be in a metric that is meaningful.

It is not clear what the numbers in Figure 6a mean. Here, again it is difficult to compare what a low frequency of occurrence of "3.5 to 3.8% of progeny", or "0.7 progeny of MD/100 cell lineage of p53si cells vs. 0.05 progeny of MD/100 cell lineages of Control cells" means when they are normalized to /100 cell lineage.

In the extensive simulations sections, it is not clear that many of them are necessary as main figures (e.g., Figure 8-11). For example, is a simulation necessary to show that extremely high levels in vitro of 7uM MNNG severely sickens the cells? "we estimated that 63.1% and 36.9% of cell growth inhibition … were due to the direct effect of MNNG and damage response, respectively" is very precise for a simulation, but is confounded by biology: off target effects of RNAi, imprecise knockdown of p53 (as the western blot shows), etc.

Overexpression of p53 protein causes senescence, and the paper shows very nicely that p53 is involved in both cell proliferation and cell death. However, it is not clear what the implications are from this and why this is important.

On pg. 35 the use of the word suppressed/suppression and in the rest of the paper implies an active cellular mechanism. Here, it is simply that they are outgrowing or reproducing faster to represent a larger proportion of the population. In the methods on the algorithm, there is nothing that has the two populations interacting, and the two arrays can be "physically" separate in a visualized image and still see the same results. Thus, to state that "p53-silenced cells started to expand their population over that of the p53-expressing cells, " and "allowed the expansion of the p53-silenced cells," and "the cell population was replaced with p53-silenced cells," are all implying physical interactions that are all not really occurring and just two population rates that are simulated and then normalized to 100%. Other statements like, "However, the suppression became less prominent … and p53-silenced cells started to expand their population over that of the p53-expressing cells" are problematic and imply an active biological simulation of physically and chemically interacting cells that is not the case.

There is substantial use of jargon and unnecessary abbreviations in the paper. This is not a minor point and severely affects comprehension and readability. In silico experiments are all simulated by computer. Why the need to keep track of p53Si-Sil(-CD)-Sim? Of BD, CD, MD, and CF; the terms BD, CD, and MD are not related, CD means cell death, CF is also not related to CD, but rather the opposite of BD. On pg. 22, the abbreviations are completely unnecessary, and the information of the abbreviations to be memorized by the reader do not come up until much later in the paper. Event is abbreviated Evt, why is this necessary to get rid of 2 letters, "en"? The abbreviation Evt is never again used until the Methods, thus it is only a methodological importance. I understand as a programmer Event and event type are coded as separate variables containing different data, but for the reader this is irrelevant and superfluous. Similarly, "Among the five simulation modes, Standard mode (Std) …" all of these abbreviations Std, Ind, MX, SS, MCS, in a search function of the PDF, are used only 2-3 times in the main text of the paper.

Reviewer #3 (Recommendations for the authors):

Recommendations for improvement

The paper illustrates the advantages and pitfalls of interdisciplinary work, here cell biology and computational approaches. A more pedagogical approach would have made the paper's rationale clearer because some of the approaches, including the DIC image tracking and the cell simulation modelling are not part of the standard biologist's toolkit.

The paper would be greatly strengthened if the authors could summarize the tracking and simulations through pseudocode or a plain language description of the algorithm used for simulation. That way, the average biologist with or without computational expertise would have a sense of the underlying algorithmic thinking, which is separate from the technical details of the computational implementation. Taking the time to explain the algorithm accessibly yet rigorously, allows a reader new to cell lineage tracking and/or simulations to come away with a better sense of the power of these approaches in cell biology.

The paper also needs more transitions to guide the reader. Unless a reader has a background in this area, it can be hard to keep track of the different testing conditions and visualization of results as they represent a formidable number of combinations. At times reading the paper felt like trying to parse a logical puzzle rather than reading experimental results. In addition, the data sets are rich and varied, additional guidance is required in explaining results as in providing transition sentences that explicitly state the reasoning with a bit more detail.

In terms of the biological question, a statement about the novelty and impact of this work would be useful as it is not clear that the model is indeed testing the effect of homeostatic p53 levels. Tumour cells without p53 are able to avoid cell death and proliferate. It is unclear how having less of a wild-type protein in a cell represents a homeostatic model, distinct from having mutated forms within a cell. Also presenting a general result about homeostatic p53 using one cell line, also derived from a tumour, is questionable.

Additional comments for authors:

1. How is the DIC segmentation and object tracking implemented? Is the code developed by the group and is it available on Github or another public repository? Or is it available commercially? It would be good to document the version of the code. Also Cell Profiler apparently can segment DIC cells, so it would be good to know if the approach used by the authors is novel and/or available through open source, collaboration, purchase etc.

On page 69, this is hard to decipher:

Cell density map created by assigning value 1 to a pixel within the 20-pixel diameter area from the position of a cell (blue); if an area overlapped with other areas, the pixel was assigned the sum of the number of overlapped areas (light green).

Can the authors clarify here as this may also help explain communicate the DIC segmentation/tracking approach better?

2. Although the Figures, including Supplemental Figure 7, describe the simulation steps, a high-level description, such as pseudo-code, is missing. That is, a guide that helps the reader understand the logic and implementation of the simulation and help with the interpretation of the detailed steps given in Supplemental Figure 7.

For example, my interpretation of the algorithm is below. It is highly likely my interpretation in incorrect, yet this gives an indication of how and why pseudo-code would be useful and may point out the parts of the explanation that need more detail.

– All these simulations are based on the empirical tracking data. [Note I am not sure how the authors extrapolated past the time length of the experiment, which means I am missing something important]

– Data sets inputted into the simulation include the location, cell division (BP or MP), cell fusion, or cell death, as well as technical notes that affected the tracking.

– Algorithm starts by loading in cell lineages obtained from experiments randomly and automated tracking/manual correction data.

– Simulations progress by filling in the cell areas based on the cell lineage diagrams, and cells and events are encoded for ready visualization when needed.

– Cells were considered to be the same size throughout[?].

– I am not sure how the lineages are extrapolated past the 4000 min experimental time.

– Also I would explain the reason the simulation is so useful. Here is an example where it may seem so obvious to the authors it needs no mention. Yet sometimes it is better to be explicit. It can seem you are talking down but it is helpful!

With this simulation approach, we test whether the simulation matches the experimental results, and also uncouple the combined effect of cell division, cell death and cell fusion on cell proliferation, which would be difficult to do in an experiment with live cells.

3. Tumour cells without p53 can avoid cell death and proliferate. It is unclear how having less of a wild-type protein in a cell is different from having mutated forms within the cells.

– That is, how does the function differ here compared to a mutation in p53?

– How does reduction in p53 followed by inducing cell damage test the need for basal p53 as a unique pathway in cancer progression?

– In addition, more justification of the choice of A549 cells chosen as the model is required, in light of the statement in the Introduction: Here, we investigated the effects of low levels of p53 on the behavior of cells using empirical single-cell tracking.

What is their endogenous expression of p53 in A549 compared to other p53 proficient cells? How do these levels compare to normal cells, such as those derived from primary culture?

– How does inducing DNA damage test the function of low levels of p53 in unstressed cells? Wouldn't a better model be to compare different cell lines with different endogenous levels of p53 and see how they respond? Or this could be used as a second method to back up the conclusions when you damage silenced cells, it seems that the model is not delineated precisely for studying low levels of p53 on cells. Rather the test is studying the effects of DNA damage on p53 null cells which has been done many times? It would be good to hear more about the rationale here, as it is not clear from reading the paper's arguments.

Detailed questions:

4. Why were the cells monitored at such a high density? Was this choice governed by the biological question and/image analysis algorithm limitations, or some other reason(s)? (to follow the fate of individual cells by monitoring live cells, because the culture eventually became over-confluent).

5. Why were the concentrations of CO2 different in the incubator and experiment? Is it due to maintenance of pH, and if so, it would be good to mention this as not everyone monitors pH when carrying out long-term imaging?

6. The authors mention maintaining the integrity of the cell population in multiple sections, including the summary. How is integrity defined? Is it metabolic, genomic, structural?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Empirical single-cell tracking and cell-fate simulation reveal dual roles of p53 in tumor suppression" for further consideration by eLife. Your revised article has been evaluated by Aleksandra Walczak (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Main issues:

– l. 316-318. The authors suggest that P53 RNAi cells proliferate faster, but have more cell death. Can this not be quantified directly from the data, rather than in the indirect manner pursued here? For instance, one could measure the probability that a cell will divide again, if it doesn't undergo cell death. The prediction would be that this probability is higher for P53 RNAi cells compared to Control.

– l. 391-396: This section is still unclear to me. Why not follow the same approach as shown in Figure 7c for time to MD? Is it because there is a correlation in cell cycle time between generations, i.e. a rapidly-dividing mother has rapidly dividing offspring? This should be explained more clearly.

– l. 418-421. I now understand conceptually what the others do, but from the text and Figure 8 I don't understand how this works in practice. Do the authors linearly interpolate between two Operation data sets? If so, then write that down explicitly. Some things in the text here still make no sense to me. "A start event of 10 and 1", what does this refer to, what sort of event? "The chance of a cell population exposed" A chance of what? Is there some probabilistic process that underlies this?

– l. 489-494. I am not sure I properly understand the origin of shorter doubling time. Is the problem that the cell cycle time is not drawn from a measured distribution (as in Figure 7b) and therefore misses rare but very long cell cycle times?

– l. 523-526. This seems a rather counterintuitive effect: removing the P53 stress response leads to higher cell proliferation when higher stress is applied. I do think it should be emphasized more that this is counterintuitive and perhaps also a possible explanation for this effect should be given.

– l 532-535. It is not clear what the simulations can add here. Is it not possible to use experimental data to measure this directly? After all, the simulations are driven by experimental data, so in principle, there cannot really be anything new from the simulations in that regard.

– l 535. "we assumed" I don't understand what the assumption is based on. Measurements in this paper? Existing biological knowledge?

– l. 550-551. The low frequency of multipolar division is put into the simulations directly from the experimental measurements. So why is this simulation result, which makes exactly the same conclusion, surprising or interesting?

– l. 552. "growth of virtual cells" It is not explained in the main text how the spatial cell dynamics is implemented in the simulations. It is also not explained why space is even important and what novel insights it will bring to incorporate it.

– l. 555-559. It is not clear why showing spatial expansion of MD progeny is important. Couldn't the same insights be gained from purely looking at images? This just means that you get clones of cells that are MD cell progeny, why is it important where they sit in space?

– l. 578. What novel insight does this section bring? The stress-shift experiments show the same conclusion of P53 RNAi outcompeting Control cells as Figure 10. Also, what does the inclusion of space bring to Figure 13a? Would the results in Figure 13b-h be different if space was not included? If not, then I would remove the spatial analysis.

– l. 636. "cancer tissue mass". I don't understand why this result is compared to cancer: most cells are Control (=wild-type?) cells with few P53- cells interspersed, and most of the growth is due to proliferation of Control cells, not P53- cells.

Reviewer #3:

Comment 1:

The experimental data and single-cell lineage analysis are important contributions to the field. Although the authors have included more detailed explanations, the additional insights offered by single cell tracking need to be described more clearly and emphasized throughout the text.

For example, when the authors move from reporting on the population level counting to the single cell tracking results (lines 197 -198), the authors should guide the reader by providing a transition between both approaches. Currently, the authors launch right from the population counting results to validation of single cell tracking without building up the need for single cell tracking.

To quote: We then compared the results obtained by cell counting with those obtained by computer-assisted single-cell tracking analysis to verify whether this analysis indeed yields results consistent with the classical counting method.

Before comparing the results, a transition highlighting the need for single-cell analysis is missing as well as the need for comparing both methods is needed. Suggestion: "Thus far, we have described how the different treatments affect cell numbers at the population level. We then analyzed the data sets using single cell tracking. This powerful approach can reveal how the events occurring at the individual cellular level contribute to what is observed at the population level."

Only then move on to the comparative results such as by stating: To test the accuracy and self-consistency between our standard cell counting and single cell tracking, we compared the results obtained with each approach.

Similarly, when the results obtained from single cell tracking add new information, additional context should be provided for the reader. This paper is cognitively challenging to read and interpret, and more explanation is needed to help the reader navigate and appreciate the significance of the results.

Comment 2:

Similar clear emphasis is needed when describing the simulation approaches and their significance. To illustrate: In the section introducing the cell-fate simulation algorithm (lines 363-372), confluency is mentioned as are "limitations of empirical approaches." Rather than stating confluency and the vague term "limitations," the justification needs to be clear from the start. My suggestion is move the explanation found later in the text to this introductory section.

For example, lines 440-442 state: "cell-fate simulation using Operation data allows the creation of various simulation options and provides flexibility for designing virtual experiments that would be difficult to perform empirically."

Rather than letting the reader wait for this statement, I recommend leading in with a similar statement (and dropping the technical reference to Operation data). Suggestion:" Cell-fate simulations are powerful and flexible tools help us model conditions that are not readily accessible by direct imaging, such as mixed cultures and mixed dosages. "

Other comments:

3. Ensure that cell growth is used when referring to cell size not to cell division within the text. The term "grow" is used colloquially in the lab but here should be reserved for area/volume not cell division. For example, see how "growth" is used in Line 125. Here it is confusing as the passage is describing cell area decreasing and then grow is used to mean cell proliferation.

4. What random number generator was used?

5. Figure 1—figure supplement 3. Y axis in last graph has the label "Variation" but the units are missing.

6. When discussing Figure 5, explain how the results

highlight the need for single-cell tracking studies and how this approach complements and enriches the population level studies. Suggestion: "The cell numbers over time are roughly equivalent for both the scr siRNA and the p53 siRNA treated cells, as shown in Figures 2c and 2i. The single cell tracking data, however, reveal differences that are not directly accessible through standard cell counting. Figure 4 reveals that although the overall cell death is higher in the p53 siRNA cells, it is compensated by increased multipolar cell division. Further, the simulations can help unravel the relative rates of multi-polar cell division compared to cell death. As shown in Figure 5, we see that the relative proliferation curves can be simulated in the presence or absence of cell death. By analyzing the individual cellular fates under well-defined conditions, we can then simulate scenarios that are not accessible through our direct imaging, such as analyzing how a population of mixed cells and/or heterogenous treatments will evolve over time. "

7. Line 226. Quote: To this end, we sorted each cell lineage into groups (Figure 3a).

The division into groups introduces a layer of complexity and seems arbitrary considering the small number of possible bins. Why is reporting the binned data through groups better than reporting the numerical value?

8. Lines 282-286. Quote: …the number of cell death events in Control cells determined by counting was higher than that determined by single-cell tracking analysis. This was because the area of single-cell tracking was slightly outside the area where cell death frequently occurred (Figure 4—figure supplement 1c). However, given that such events do not occur with the same probability throughout the field of view, some variation may occur with both the counting and single-cell tracking approaches.

Was this because cells that die move more than cells that do not or is it something specific about the cell imaging chamber with death occurring near the edges more than the centre?

9. I am confused by the reference to the "accuracy of a detecting a low frequency event." Quote: In general, the accuracy of detecting a low-frequency event is lower than that for frequently occurring events, e.g. bipolar cell division…

Are the authors referring to the probability of the event being captured by the imaging system rather than the detection of the event by their software and/or visual scorer? Or do they have evidence that the detection by the software and/or visual scorer is lower for these events compared to bipolar cell division?

10. The authors state in line 260 "We therefore determined if single-cell tracking could detect multipolar cell division, cell death, and cell fusion with adequate accuracy for statistical analysis. To this end, we determined the number of multipolar cell division and cell death events visually by manual counting in videos, and compared the results with those obtained using single-cell tracking analysis (Figure 4). Notably, cell fusion was not included in the counting analysis because it was difficult to detect without single-cell tracking."

Yet when review Figure 4, I am having trouble deciphering how the authors concluded that the single-cell tracking was accurate as the results are not directly compared to visual scoring. Please clarify.

11. Lines 316-318: These results suggest that p53 silencing promoted the reproductive ability of p53 RNAi cells, but this was counteracted by the induction of cell death, resulting in the formation of p53 RNAi cell populations that were smaller than Control cell populations (Figure 2i).

I see a small dip in the p53 RNAi curve compared to the Control curve in Figure 2i, but otherwise they look similar. Please clarify.

12. Line 318 Analysis also shows that the effect of silencing the low levels of p53 cannot be detected without access to the spatiotemporal information on individual cells provided by single-cell tracking.

Although this statement is likely, the counter-example can not be ruled out. Just to list possible alternative approaches that could reveal similarly nuanced effects of silencing p53. One can imagine a scenario where the number of live and dead cells are measured over time, without any single cell tracking. Or it may be possible to model the number of cells over time using an analytical expression that embeds cell division (bipolar, multipolar) as an exponential and cell death (say as a linear function of time). Suggestion-qualify statement: "This analysis also demonstrates single cell tracking provides more nuanced and detailed information about the effects of silencing p53. Here the single cell analysis revealed clear differences in the rates of cell proliferation and cell death among the scr siRNA and p53 siRNA conditions, differences would be obscured and/or missed if limiting the analysis to cell counts at the population level."

13. Line 331: Following cell fusion, Control and p53 RNAi cells demonstrated 79.4% and 93.2% multipolar cell divisions.

Please define the % values-how are they calculated? Also the numbers are listed on the bar graphs in Figure 6- the relative percentages of listed over the bar graphs is confusing in light of the numbers being relative to another 100, the 100 cell lineages. Also it would be helpful to see the spread of the data points illustrated by the bar graph.

14. Staring on line 385, the authors state: The algorithm then reflected this distribution to choose the End event.

– How is the weighted random assignment implemented? Specify the method or methods and justify why the choice is appropriate.

– Similarly, for LT and other random assignments, is the implementation always the same as for the Event assignment?

– Is the additional +/- 10% in ET imposed for BP events based on experimental data obtained here and/or reported elsewhere or there some other reason for constraining the ET for BP events in this way? Further, could this constraint have led to the observation summarized in lines 489-494: On the other hand, the simulation tended to yield an average cell doubling time about 2 h shorter than that determined by single-cell tracking analysis. Given that the algorithm assigned a cell doubling time to each cell by generating a random number with Operation data-Time (Figure 7), a long cell doubling time, e.g. 3,000 min, which occurred less frequently, may be less likely to be assigned, resulting in the generation of a simulated cell population

– When CF occurs, do these events also reflect the frequency of sibling vs non-sibling under the different conditions studied?

15. I have trouble understanding why calculating Recovery is important to the simulation and why it is listed before the other steps. Line 894 states: Recovery data was used to simulate the rate of recovery a cell population from the treatment of MNNG. When cells were treated with MNNG, the majority of cells may be killed. However, small number of cells gained reproductive ability, which could be found at the end of imaging.

I am confused here as I don't see evidence of the majority of cells being killed in the population expansion data and don't understand why they need to be tracked.

Lines 903-907: For example, if any of the progeny derived from a progenitor underwent bipolar cell division at last within 20% of the single-cell tracking period, e.g. 320 to 400 min when tracking was performed for 400 min, this cell lineage was counted as one upon the calculation of the percentage. Thus, if 10 such cell lineages were found out of a total of 300, the recovery percent was 3.3%.

I don't understand this statement-what does percentage refer to? Why is only BP considered and not MP, for example? Any why is calculating this value important to the simulations as illustrated in Figure 7, supplement 1c, Step 3?

16. Line 918-920: To generate a simulation array for the Operation data-Event, the percentage of each event relative to the total number of cell divisions (total of bipolar cell division and multipolar cell division) was calculated.

As shown in Figure In Figure 7, supplement 1 c, in the "Event" sequence I don't understand why calculating the "% event of total cell division" is possible before the simulation arrays are created?

17. Lines 931-933: the array was empty, the average time that bipolar cell division occurred was calculated and −25% to +25% of the time selected by random 933 number was assigned as LT, and bipolar cell division was then assigned to the cell.

Is this based on experimental data and/or another reason?

18. I appreciate the care and effort that went into detailing the algorithmic approach used for the simulations. The logical flow now is much clearer and moves away from being a "black box" to now being reproducible.

Recommendations and questions:

– Figure 7 supplement 2. Recommend placing this before supplement 1 as it presents the overall logic.

– In Figure 8, supplement 1a, (page 94). Change "Uze" to "Use" in Step 6.

– In Figure 7, supplement 1b (page 95), Step 3 defines the nBD but the description is confusing. Clarify the "last time point of cell tracking" – is this simply the LT associated with the event? Also what is the offset and what is its purpose?

– In Figure 7, supplement 2, there is a typo in "Select an e-vv-ent type"

19. Consider revising sub-headings to guide the reader. Revise to express purpose, result, significance etc. These could serve as signposts throughout the paper would improve the paper's accessibility.

20. In future work, consider graphical representations that are not limited to colour as in "burgundy" plot as 8-11% of the male sex is R/G colour blind. Consider using different plots styles as well as colour. I am not asking the figures to be revised for this publication, but ask that the authors consider visually accessible graphics / figure in future publications.

21. Similarly, consider box plots rather than bar graphs for future work.
