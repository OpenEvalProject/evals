# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54080.sa1](https://doi.org/10.7554/eLife.54080.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The study enhances our understanding of cellular effects of protein load.

Decision letter after peer review:

Thank you for submitting your article "Genetic Profiling of Protein Burden and Nuclear Export Overload" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In "Genetic Profiling of Protein Burden and Nuclear Export Overload", Kintaka et al. performed a synthetic genetic array screen to explore the genetic interactions between mutants (DMA and TSA libraries) and protein burden. They used the 2 micron plasmid of Saccharomyces cerevisiae to explore the genetic interactions in response to three different protein burdens/overloads: (i) regular GFP; (ii) triple-GFP (tGFP), a much bigger protein that they found created some aggregates when highly expressed; and (iii) the nuclear export signal-containing tGFP (NES-tGFP). A similar study has already been published in this journal (Farkas et al., 2018), where the genetic interaction between the DMA library and yEVenus burden was explored. The present work, however, is much more extensive: it includes four biological and two experimental repeats, a second mutant library (TSA), different types of burden, and, most importantly, it checks the effect of higher burden levels using a stronger promoter.

Essential revisions:

Fundamental:

Overall, this work increases the knowledge about processes involved in protein stress alleviation. Yet, while the manuscript describes interesting phenomena, it does not provide follow-up findings to explain the main observations and therefore remains descriptive in nature. Here are concrete suggestions to this end.

1) In general, since there is no systematic follow-up on the main findings, it is difficult to appreciate how cells deal with the increased protein burden. In particular, as the authors noted, their findings are significantly different from other studies using similar reporter systems. Additional work is needed in order to substantiate the different pathways.

2) The authors overexpress GFP that does not have any physiological activity in yeast cells and therefore considered non-harmful. Yet, overexpression of tGFP shows genetic interaction with the proteasome. This may imply that tGFP undergoes post-transcriptional modification(s), such as ubiquitylation and this must be taken into consideration when attempting to explain the data. Accordingly, the authors need to examine the ubiquitylation status of their constructs, especially in proteasome where ubiquitin conjugates accumulate. Abolishing GFP ubiquitylation (using a lysineless variant, for example), may mitigate or abolish genetic interactions with proteasome subunits, suggesting a role for ubiquitin during overexpression.

3) tGFP-op levels are !~10 fold lower than GFP-op and yet only tGFP forms aggregates and affects cell viability in proteasome mutants. This is an interesting observation that requires some explanations. How tGFP-op is related to its tendency to aggregate and whether it is related to the proteasome activity should be verified before drawing a conclusion.

4) A main limitation of this work is the use of "tug of war" plasmid to generate the burden. This means that the plasmid copy number, and with it the GFP levels, will change across different mutations. The authors found, for example, that GFP levels are lower in many of the Mediator mutants. The reaction of the mutant cells to the burden should be measured not only by the growth effect but also by the burden level. The latter can be approximated by GPF levels or by the plasmid copy number. The authors report that in -Leu/Ura conditions, there are 30 copies of the plasmid. This statement is correct only for WT, and needs to be measured or estimated for the different mutations. This estimation, again, can be done by measuring the GFP levels of the different mutants. For the GFP set, they indeed used a method to measure the GFP levels. It would have helped to understand the mutants in Figure 3, if the GFP levels had been shown – this could easily be done in a supplementary figure. Fluorescence levels were, however, not done in the tGFP and NES-GFP experiments, or at least they are not being reported. It is important and probably critical to successful publication, that GFP levels be measured and reported, to help interpret the results correctly. At a minimum, this GFP levels should be given for those mutants above the GI threshold.

5) When the authors compared their results with those of Farkas et al., they didn't find any correlation. Neither study, incidentally, quantified GFP levels. Also, the present study used a plasmid with much higher expression levels, which will inevitably have obscured comparability. Farkas and co-workers used yEVenus and they showed that "yEVenus binds weakly, but significantly to certain molecular chaperones…". This binding, that may be unique to yEVenus, could also be part of the reason for the apparent differences in results. Farkas et al. showed that the burden effect was reduced by adding more AA to the media. Checking the AA effect on the GFP burden would have helped to reconcile whether the difference in results is a reflection of a different kind of burden, or whether it is mainly the results of a growth effect that wasn't normalized by GFP levels.

Presentation:

The writing of the manuscript and the interpretation of the data needs considerable expansion. The methods and the results are not described clearly. Please see major comments below.

1) Clarify the definition of genetic interactions.

1a) The term “genetic interactions” should be defined in the Introduction in a way that is specific to how it is used in this study, e.g. "In this study we screened for gene knockouts or knockdowns that had different impacts on growth depending on whether a green fluorescent protein was overexpressed."

1b) Clarify the meaning of positive and negative interactions, specifically whether the mutations are deleterious or beneficial. A positive interaction could either mean that GFPop alleviates a growth defect or enhances a growth advantage. Which one happens more? Probably the former but this needs to be clearer. This should be broken down in the figure, e.g. what fraction of orange dots signify a growth defect being alleviated vs. a growth advantage being enhanced? Can the authors use 4 colors, blue, light blue, orange, light orange? Since the goal here is to understand the biology of the cell and how GFPop changes it, these details seems important.

2) Clarify the protein burden.

2a) It is not a good idea to assume readers are familiar with previous publications using the tow system. Thus, most readers will assume that all mutant strains are expressing the same amount of GFP plus or minus some kind of noise (e.g. plasmid copy number variation due to unequal cell division). Please explain this in more detail in the Results section.

2b) Also, the term protein burden needs to be continuously explained. It is easy to interpret that term as meaning “the growth defect imposed by GFPop”. But it probably refers to the number of GFPop molecules produced. Is that right? Rather than using the term, “protein burden”, sometimes it would be OK to spell out what is meant, e.g. the number of GFPop molecules that burden the cell.

2c) An interesting question that arises is whether, in negative interactions, the expression of GFPop is enhancing the growth defect of the gene knockout/knockdown or the gene knockout is increasing the protein burden, e.g. increasing the level to which the tow system is able to express GFP. The authors have an impressive method of disentangling these two hypotheses, which they explain in Figure 4. But paragraph two of subsection “Investigation of GFP expression levels of mutants” of the paper, where these possibilities are enumerated, are unclear. One has to go back and work out many details including the possible types of positive and negative interactions, and how the tow system worked. A diagram or cartoon should be presented earlier in the paper, perhaps as Figure 1, which explains the logic showing the different possibilities that could be happening inside of cells and how the authors plan to disentangle them. The authors could depict 4 double-mutant cells, for example, one with a high level of GFP but a lower growth rate than either the GFPop strain or the mutant strain. Then they could explain in the legend the hypothesis as to what is happening inside this cell. Maybe a figure is unnecessary. But some more detailed explanation of how this system works and how the authors plan to us it to disentangle the possible things happening inside of cells should come up much earlier in the paper.

3) The growth regime is not clearly explained.

3a) The text in the first part of the Results section is very brief and relies heavily on Figure 1 to explain the experimental set up. Perhaps add a few more sentences to guide the reader. For example, the comment in paragraph two of subsection “Isolation of mutants that have genetic interactions with GFP-op” about “colonies” does not make sense. It should have already been stated that growth is measured in colonies and not in liquid culture. Otherwise the word “colonies” comes from nowhere.

3b) On that note, Figure 1C is confusing because these particular measurements were taken in liquid culture. Why are two different culturing methods used? Since 1C is meant as a control to show how the GFP affects growth when no knockout/knockdown is present, shouldn't this control be performed using the same method as the rest of the experiments?

4) Why were the particular GI threshold levels chosen? Why were the cutoffs chosen, including 0.08 in Figure 1 and 0.2, to define GFPop-positive and negative?

5) Why better correlation across conditions than within conditions? Figure 2A shows that even when taking only GI that exceed the 0.8 threshold, the correlation between replicates is less than 0.5 in the DMA -Ura condition. But Figure 2B shows that when comparing DMA -Ura to DMA -Ura/-Leu the correlation is greater than 0.5. How come the correlation between replicates is less than the correlation between these two different conditions? Is it because by averaging multiple replicates you get a better sense of the true GI value? This should be addressed.

6) Too many abbreviations. There are so many terms in this paper that are used to capture important concepts, e.g. positive interaction, protein burden, TMA, GFPunit_L, GFPunit_H, GFPop_positive, GFPop_negative. The reader loses track of how all of these things are related. The authors should not rely on these abbreviations so much and talk though these relationships, e.g. "Mutants with growth defects that were enhanced by GFP overexpression were also more likely to produce less GFP, indicating that the limit of GFP overproduction in these cells was lower than in other cells." Sentences like these would be so helpful in explaining what is actually going on.

7) Sometimes the Results section read a little bit like a list.

7a) This is a common issue in studies that report GO terms from different groups. Figure 3 is particularly list-like. The balance of the paper should shift away from listing GO categories and towards explaining and interpreting what is happening inside of cells as in paragraph two of subsection “Investigation of GFP expression levels of mutants”, and in Figure 6. For example, the authors were nicely able to do more with the actin and cell bud genes and show that indeed these cells had aberrant morphology. Also Figure 6F where the authors digest all of this information into a hypothesis about what is happening inside of cells was nice. Problematically, that hypothesis is unclear and will only become clear once points 1 and 2 above are addressed.

7b) Also, in 6F the relationship to the proteasome was not as clear as was the perturbation of actin. Could the proteasome relationship be explained more clearly?

Final thoughts: In sum, the authors' goal seems to be to go beyond listing GO categories to talk about how the protein burden affects cell biology. They need to rework the paper a bit in order to achieve this goal.

8) In the NES-tGFP experiment (and only in this experiment), they found strong interaction with the nucleus export machinery. This result isn't surprising per se but it's a good proof of concept, and it can be used as a control – showing that the system is working, which is worth mentioning. So this work could be an important resource to the field enabling a deeper understanding of protein burden origin. It should be emphasized.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Genetic Profiling of Protein Burden and Nuclear Export Overload" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

As you can see, reviewer 2, raised outstanding issues regarding the mechanism. Originally they felt that more experiments are needed. However, in the discussion that followed they agreed to allow the authors to deal with them by adding statements that further studies to reveal the mechanisms are needed. It is up to you to decide whether you would like to add more experiments or language changes.

Here is a part of the discussion that elaborate on the proposed experiments, which could be useful to you:

"One model that I can think of, which is based on recent literature, is that tGFP undergoes ubiquitylation and then a portion of the ubiquitylated protein is sequestered into large aggregates. Proteasomes are been recruited to these aggregate but the kinetics of degradation is altered. This results in overall reduced proteasome capacity, shown through genetic interaction with proteasome subunits. I proposed to the authors to address the connection between overexpression and aggregation.

In my second revision, I suggested two experiments:

1) to IP tGFP from the pellet and show that indeed it is the protein that undergo ubiquitylation. I believe that technically this experiment is essential.

2) To reduce overall ubiquitylation (through the overexpression of mutant R48 ubiquitin) and test if tGFP is still aggregated and if this has an effect on cell growth.

One can think of alternative experiments, but the point is that the basis to the effects the authors observed upon overexpression of tGFP is still unclear to me."

Otherwise, please re-phrase some of the statements regarding the ubiquitylation of tGFP and the possible mechanism of tGFP function. Regarding the former, showing poly-Ub chains in the pellet does not prove that tGFP is indeed as the substrate. Regarding the latter, according to the accumulating data, the mechanism is unlikely to be a general effect of overexpression that leads to the proteasome. A statement about the effect of aggregates on proteasomal degradation could also help clarifying the issue. Possibly the depletion of essential factors like molecular chaperones?

Reviewer #1:

The authors have addressed all of my previous comments, moreover, this is an impressive revision. The authors add new figures and text that clarify their methods and previous findings. The authors also add new analyses, including biochemical analyses of some of their overexpression strains. Finally, the authors add a new figure and synthesize their results into a model which describes the different ways cells might be affected by overexpressed proteins.

The revised paper represents a massive amount of experiments and careful thought about how the cell responds to overexpressed proteins. The paper sheds new light on this question.

Reviewer #2:

The authors nicely addressed my first comment. however, in my opinion, issues 2 and 3 require further clarification:

In respond to my comments regarding the level of expression and PTM of tGFP, the authors tested whether tGFP aggregates were ubiquitinated and concluded that overexpressed tGFP but not GFP forms ubiquitinated aggregates in cells. They hypothesized that tGFP-op causes an overload of the proteasome because tGFP is frequently misfolded, ubiquitinated and degraded by the proteasome. This may be the cause of the negative genetic interactions between tGFP-op and the proteasome mutants.

I suggest that this hypothesis should be further clarified, since aggregation of tGFP is at the center of the manuscript and without having a mechanistic explanation to its function, the significance of some the authors findings is unclear. Generally, the overexpression of misfolded proteins (even large ones) per se does not inhibit the proteasome in yeast cells. Alternatively, the recruitment of proteasomes to protein aggregates may abrogate their function. Since the proteasome harbor several ubiquitin receptors, it is possible that protesomes interact with aggregated proteins through conjugated ubiquitin chains. This could be tested for tGFP by isolating it from aggregates by IP and looking for ubiquitylation. Furthermore, I accept that having lysineless GFP might not be the best approach to tackle the issue. Yet, the authors could test the effect of conditional overexpression of lys48 ubiquitin mutant on aggregate formation, proteasome function and/or cell viability in cells overexpressing GFP or tGFP. This type of experiments should shade some light on the molecular basis for tGFP aggregation and the effect on cell growth.

Reviewer #3:

The revise version of "Genetic Profiling of Protein Burden and NuclearExport Overload", is greatly improved. the logic is easier to follow, and there are more illustrations. The comparison between their and Farkas' results are dipper, and most important to my opinion, they now have the GFP measurements for all the conditions, and those measurements now better integrated into the text and figures.

Their final model about the different ways protein overproduction can affect growth rate is very nice. they display some of the interesting biological questions that rise up from their screening, include the interaction between actin and protein burden, and that over-expression tGFP lead to aggregate and proteasome stress. They also did some follow-ups experiments to both of them, but they didn't reach to a biological understanding about the origin of those interesting observations: way Actin is so important to protein overproduction? and the reason for tGFP aggregates. It would have been nice to get a better understanding to at list one of them but many times interesting questions are as important as answers, and it is very extensive and interesting screen. So, they answered most of the question, and in my opinion the current wark important and good enough for publication.
