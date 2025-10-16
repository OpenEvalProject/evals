# Peer review - Round 1

Editors:
- George H Perry, https://ror.org/04p491231 Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84759.sa0](https://doi.org/10.7554/eLife.84759.sa0)

This study has important implications for the impact of sexual conflict on population viability under different temperatures. The authors provide compelling evidence that male harm to females in sexual conflict can be reduced as a function of temperature within the optimal reproductive range of a species. The results have implications for the likelihood of the evolutionary rescue of species facing the climate crisis.


---

# Peer review - Round 1

Editors:
- George H Perry, https://ror.org/04p491231 Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84759.sa1](https://doi.org/10.7554/eLife.84759.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Thermal phenotypic plasticity of pre-and post-copulatory male harm buffers sexual conflict in wild Drosophila melanogaster" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and George Perry as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Ivain Martinossi (Reviewer #1); Lennart Winkler (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. A consistent critique from all reviewers concerned the need for improved clarity regarding experimental design, both in terms of the experimental steps themselves and also in how the experiments themselves explicitly relate back to the phenomena being studied. Numerous general and specific comments on this point are provided in the below reviews. Please also consider developing one or more figures to assist readers at a high level (while also not neglecting the need for major improvement in clarity and thoroughness at deeper levels in the text itself).

2. The above comments can be extended to the statistical frameworks applied in the paper, i.e. requiring more clarity, depth, and precision (and correction for multiple tests as appropriate in some cases). In some cases, this will likely require adjustment to the statistical approach used for a given hypothesis test.

3. Consider tempering slightly your conclusion that the effect of sexual conflict can be buffered by temperature in the wild, based on the experiments conducted to date.

Reviewer #1 (Recommendations for the authors):

Partly because the methods are placed at the end in this format, I had a lot of confusing moments going through the results. Certain details need to be explained before the methods section. For example, the fact that the polygamy treatment is also a highly male-biased treatment is very important and should be stated clearly. This will impact the interpretation of the results. It is also very important that you explain better the experimental design before diving into the results, otherwise much confusion follows. To be fair, even going through the methods section I found it quite hard to understand the details of the experimental design, especially the receptivity experiment part. It is a complicated experiment with a lot of aspects to it. It needs to be explained very carefully. Perhaps a diagram could help? In any case, you need to explain better the general architecture of the design before getting into the result section. Here are the facts that I think need to be mentioned before the result section so the results can be understood at all (either end of the introduction or the first paragraph of the Results section):

– There are several experiments in parallel, not just one, all across 3 temperatures.

– In experiment 1, flies are exposed to three temperatures in either monogamy (1:1) or polygamy (1f:3m) conditions. LRS is measured, senescence too, and behavior (courtship and aggression) on day 1 are recorded.

– In experiment 2, flies are also exposed to 3 temperatures. This part is very confusing in the methods l.508-525 and after reading it 5 times and drawing diagrams on my whiteboard I am still very unsure of what happened. As far as I got it, virgin individuals are collected and then paired repeatedly in monogamous assays. Males can either come from a "high sperm competition" pool (they are stored together with other virgin males) or "low competition" (males stored alone). There is also a duration factor which I understand to be how long the males sit in their respective competition and temperature treatments before the mating assays. What is clear is that this experiment leads to mating duration and latency measurements (the fact that this is not part of the "behavior" assays is also confusing while going through the results).

– Experiment 3, with the same male treatments as experiment 2, this time female fecundity and egg survival are measured. (where do we see the data from that experiment? As far as I could tell all the figures and supplementary figures are from experiments 1 and 2).

I apologize for the long review. I think it partly reflects my difficulty going through the results and methods section. Overall, I really liked the study even though I was frustrated at times by how much effort I had to put to understand certain figures or results. I think this can become a great manuscript if the methods and results are given just a bit more structure. I would also like to see some slight changes to the statistical methods and a couple of additional supplementary figures (female fecundity data and egg survival). See my details comments below.

Abstract

In the second mention of the mating system treatments, I would reiterate the term polyandry instead of using just "high male competition". Otherwise, it is not immediately clear that it is a mating system treatment. For example "At 20C, female senescence was accelerated under polyandry (high male competition)" and "At 28C, polyandry mostly resulted in reproductive ageing". As far as I understand these results come from Experiment 1 (following my numbering) so they do not correspond to the "male sperm competition" treatments of Experiments 2 and 3.

Not entirely clear results in the abstract. What does it mean when the authors say that at 28C female reproduction is "modulated"?

Results

This is a very dense result section with a lot of interesting data! I would suggest using post hoc tests to investigate the interaction effects, instead of running separate models per temperature. This way, you get p-values corrected for multiple testing. Regarding male-male aggression, I do not think it is correct to assign a zero for the monogamy treatments and test for interaction. The behavior is simply impossible in that treatment, and what you are really looking at is the main effect of temperature on the behavior in polyandry settings. Presenting it as you do is very confusing both in the text and Figure 4 and, I think, is not correct. To clarify the structure further, I would not use exactly the same colors for Polygamy/monogamy and high/low sperm competition. See detailed comments below. I also suggest clearly separating the results that come from different experiments so the readers know which sections are>

l.101: Maybe "temperature by mating system" instead of "x mating system" would be better when inline.

l.103: I would suggest running a post hoc test to see at which temperature the two mating systems differ or not, for example, Tukey's post hoc, instead of three separate models per temperature. What you do is also okay and I have no doubt that this is what the data is showing given how clear it is in Figure 1. But a post hoc would be nicer than 3 separate models because then you get proper p-values corrected for multiple testing.

You could use the package "emmeans" in R. See code below:

>library(emmeans)

>model<-lm(LRS~treatment*temperature, data=data)

>pairs(emmeans(model, ~temperature|treatment, adjust="Tukey"))

l.106: what is "H"?

l.107-109: I am confused about this part and the figure that goes with it. Where do those estimates come from? How are they calculated/simulated? See further comments below in the Figure section.

l.110: not exactly clear what model is run there. Is it only on time point 1 of Figure SI1? Please be more specific.

l.127-135: It is a bit difficult to interpret the model with its simplified estimate of reproductive senescence in the light of figure SI1 which shows the whole complexity of the data. It would be helpful to also have a figure with the mean (week 1, week 2) and mean (week 3, week 4). Do you justify why leaving out the last time point in the methods section?

l.130-131: It may be clearly significant, but it is not clear from the figure which way the effect is going. Perhaps if you provide a simplified figure with means it would help a bit. Also, same as above if you run post hoc tests you will have correct p-values and it should give you an estimate for the differences. The same comment goes for actuarial senescence.

l.147: aggression rate of…I am going to guess males towards females. Please specify. It could also be male-male (or female-female, at least in my study system…), but there can't be male-male aggression in a monogamy assay since there should be only one male. Same as above, please use post hoc tests to determine how the interaction is playing out.

l.147 again: I am super confused now, given that Figure 4a shows only 1 color (no monogamy values) and the figure legend says that we are looking at male-male aggression. Of course, male-male aggression should only be present in the polygamy treatment, but then what is the "estimated decrease"? is it compared to the zero of the monogamy treatment? And what is the interaction term in the model? Did you specify "zero male-male" aggression events in all the monogamy treatment observations? I don't think this is correct to use the monogamy treatment as a comparison here and to fit an interaction effect. What you are really looking at is the main effect of temperature on male-male aggression in polygamy treatments.

L.157: It would be interesting to also look at the rejection rate relative to the courtship rate. For example, you could see that in monogamy at 24C rejection rate seems to increase while the courtship rate decreases…probably not significant but still, another way to look at it that should be informative. Do females reject more, or do they just reject the same in proportion to courtship intensity?

l.162: I find it rather strange to title that section "ejaculate effects" since no ejaculates are sampled, weighed, or analyzed in any way. I understand that the assumption behind this setup is that there is male harm that can happen through ejaculate toxicity, but it is too much of an interpretation to bring that up here. What you measure is female mating behavior and female life history traits (fecundity, egg survival), the title of the section should reflect that.

l.165: Up to that point and before reading the methods section I was not even aware that there was a parallel experiment running with different treatments! That's not good. I got so lost the first time I encountered that part of the result section!! You need to (i) introduce better the experimental design and (ii) structure better the result section so we know where we are. Just the appearance of that "treatment duration" is confusing. If I understood correctly, it is the time that males are exposed to their respective temperature and competition treatments. If that is the case, why is the data not structured that way in Figure 5? We only see the different temperatures and "sperm competition" treatments, the duration of exposure is absent, which does not help.

L170: The same comment for 5b, why does the figure not represent the data, especially given the significant interaction between temperature and treatment duration?

l.179: I would like to see this data represented in a figure (supplementary is fine), including the treatment duration effect.

l.179: Just to emphasize again how it is absolutely needed to clarify the design and structure of the results: any reader who arrives at that point of the text and reads "for the number of eggs produced by females during the first 3 days…." Will assume that we are still talking about the same females as from the LRS data in the beginning and be utterly confused.

l.192: There is an effect of treatment duration on egg/offspring number and survival, but we do not even know in which direction. Please support with figures or give model estimates.

Discussion

I feel that the results from the different experiments remain too separated in the discussion. It is the opportunity to connect together the different pieces, and there are many in this complex puzzle. Is the behavior data consistent with the trend in the LRS data? The lifespan data? The fecundity data? There are some attempts in the last section but I feel that more can be done. The conclusion feels very generic.

l. 202: please remind the reader "net harm in terms of reduced LRS".

L204-207: after reading the methods, there are still no explanations about how those are calculated.

l.210: I would replace "Thus" with "More specifically".

l. 211: Did cold temperature increase female senescence? This is not what I would expect, and not what I see in Figure 3. Females live longer when it's cooler. The effect of the mating system is stronger at 20C though.

l. 212: modulated? In what way? Again, I think it is a bit of a leap to call that "ejaculate effects". Yes, it is likely part of the mechanism, but no you have not measured any ejaculate traits. I would be okay with a statement like "Male competition status affected female mating behavior and fecundity, likely through ejaculate trait. These effects were in turn affected by temperature".

l. 214: if the reproductive senescence is from the separate experiment on fecundity and egg survival, we still need to see the data somehow to be convinced of that statement.

l.236-241: this is actually the best explanation of the rate-sensitive estimates. It comes a bit late and still is not detailed enough.

l.303: ok but what about 28C? the male aggression is at the highest, courtship rate as high as 24C…yet no detectable male harm.

l.311-322: This info is super helpful and should come earlier to introduce this part of the experimental design.

l. 324: with respect to…

l.330-345: Very interesting. Is it possible that females are simply optimizing their mating rates by controlling the remating latency, instead of it depending entirely on the efficiency of SFPs? There are two sides to sexual conflict after all.

l.366: male harm, yes, but female behavior may also be plastic. For example, why see the female rejection rate as a consequence of the action of male SFP, rather than adaptive female behaviors? With this view, sexual selection is only between males, females are just part of the background… that's missing half of the picture.

l.371: I think you are over-simplifying here. Male harm is defined as a reduction in female LRS. At 20C there is a smaller decrease in LRS than at 24C, so reduced male harm, but a larger impact of polyandry on female survival. However, this reduction in survival need not be male harm, since it does not imply a reduction in fitness. It could be part of the female reproductive strategy.

Methods

l.483: I would remove the quotation marks on toxicity.

l.420: polyandry = biased sex ratio as well. Why? Monogamy vs polyandry could be 1:1 vs 3:3. The treatments are effectively "Monogamy" and "Polyandry with a highly male-biased sex ratio". This likely magnifies the effects of sexual conflict. If you were measuring male fitness, there would be additional problems such as underestimating selection on males. I think the sex-ratio unbalance needs to be mentioned more clearly in the first part of the manuscript. It is not an obscure detail to have only in the method section.

Figures

Figure 2: (a) female? Male reproductive success? Just from the result section and the figures, it is very difficult to understand what this is. Does it come from a simulation? Why do the values on the y-axis look so different from figure 1? If it is female LRS, why does it decrease with the population growth rate? So many questions and the few lines in the methods (l.572-577) do not answer them. Consider writing a supplementary page about how this works. (2b) the name of the y-axis is confusing. The cost is obviously highest at 24C but this is the lowest value on that axis so it is the opposite of a cost. Consider changing the variable to 1-X or changing the name. I would also avoid cutting the y-axis if possible (if you change to 1-X and still call it a cost, there is no need to show the zero so you can have your plot centered on the data without cutting the axis).

Figure 4: I understand the need to keep the figures compact but at first glance, the use of two different axes per figure is a bit of a headache. In the end, it would be alright not to have the "estimated decreases" in the main figures, because it is quite visible from the confidence intervals when the two treatments are different. But it is a matter of taste. Also, in Figure 4a it is a bit surprising to still see the estimated decrease when only one treatment (polyandry) is present. What is it compared to?

Figure 5: Keeping the same color schemes for the two experimental designs (polyandry/monogamy and high/low sperm competition) is confusing.

Reviewer #2 (Recommendations for the authors):

Thank you for the opportunity to read this exciting manuscript.

I found the methods detailed, yet I feel that at some points there is still crucial information missing that would be important to judge the robustness of results or for reproducibility (see detailed comments). Furthermore, while I applaud the authors for the great amount of data they collected and the experiments they combine here, I feel that the reader could benefit from a graphic experimental scheme or so to illustrate the procedures. I believe this might help to ease the digestion of the abundant amount of information necessarily given in the methods.

Detailed comments

– L90f: Could you provide more information regarding the source and year these temperature data were collected from?

– L105ff: Were the different harm levels significantly different from each other, as the abstract seems to suggest? I think here only the difference between monogamy and polygamy was tested within temperatures in a pair-wise manner, right?

– L107: 'Rate-sensitive fitness estimates…' Maybe add a bit more context here for an explanation of this term and why this was tested. (It has not been mentioned in the introduction, I think, so this comes a bit out of the blue.)

– Figure 1: I am confused about the model estimate at 20°C. The effect size is smaller compared to 28{degree sign}C and there seems to be just a difference in the CI between those two. This does not fit the data, I believe.

– Figure 2B: I think having a line at 1.0 for no relative fitness cost and then having a break in the y-axis is a bit misleading.

– L147: Male 'aggression rate'?

– L203: '…is not statistically detectable…' That is only a matter of statistical power, isn't it? Unless there is really zero difference, which seems unlikely given the presented data, I believe.

– Figure 4A: What is the comparison plotted here? 'Decrease' from where? In the other figures, it is the comparison between monogamy and polyandry, right?

– L330: '…this effect was consistent for males treated for 48h and 13 days…' Where is this shown? Wasn't there a 'sperm competition risk level x treatment duration interaction' (L164)?

– Figure 5: Are the data for the two experiments pooled here (i.e. 48h and 13 days)? Are these really comparable as the duration of exposure is so different and also the experimental protocol varies (i.e. emptied the seminal fluid and age difference between focal and competitors)?

– L373f: '…maintaining genetic variation in sexually selected traits in males…' I think this is true, but it has not been mentioned before and could do with a bit of context, I believe.

– L406: Could you specify how the temperature fluctuations were achieved? What type of device/incubator was used? Were these fluctuations random or in predictable/pre-programmed way?

– L413: What was the 'controlled density'?

– L415: Please specify, were all collected individuals in separate vials?

– L448: Please clearly define the 'W' in this formula.

– L460f: I am slightly confused by this sentence: 'However, all flies were 5 days old at the start of the experiment.' Do you mean the experiment in general? Then I am not sure what this sentence is here for. Or, do you mean by the start of each behavioral essay? Then I don't understand how the order could have been randomized. Please clarify.

– L522: What exactly does 'right-censored' mean for your analysis?

– L537: How exactly was this modelled? I am not sure that this is sufficient information to be repeatable.

– L550: Maybe add a citation for the R packages used in the analysis?

– Unfortunately, I was not able to access the data or the code via the provided link. Please make sure these are working. I greatly appreciate the publication of code and data.Reviewer #3 (Recommendations for the authors):

I have a number of recommendations that authors should address before the paper is suitable for publication (in the order in which they arise in the manuscript).

1) The authors should avoid detailing the relative harm index H in the abstract. This index will have no meaning to most readers and requires them to read the details of the methods to understand, which is contrary to the purpose of the abstract.

2) L101: Here and throughout the paper it is unclear what statistical models are being tested and how. For example, here the authors test for a significant interaction between temperature and mating system on LRS, and report a chi-square statistic. In the methods, they state that they test the "compared GLMs with their corresponding null GLMs using likelihood ratio test" (L559), so I am guessing that this is the outcome of the test. What is the null model, however? Is it the model without the interaction and just the main effects? They are not explicit here. Further, tests of the main effects are generally considered unimportant when adjusting for the interaction (although trends in the main effects can nevertheless be interpreted). Did they adjust for the interaction when testing for the main effects? Again, this is unclear from the statistical details. I did not have access to the R script (which is stated as being available on Dryad but appears not to be), so am unsure as to what the tests actually are. It may be more straightforward to report the results of the GLMs with an ANOVA table.

3) The authors subsequently test the effect of the mating system on LRS at each temperature and report the harm index. Since these are posthoc tests, they should apply a Bonferoni correction to the significance levels (which may render the effect of the mating system on LRS at 20°C non-significant.

4) Figure 1. Here and in many of the other figures, the authors report both the means (left y-axis) and the contrasts (right y-axis), the latter being labelled 'estimated decrease in LRS'. These estimated decreases look like they are the parameter estimates from the GLMs, but their value depends on how the data are coded. Here they are the decrease in LRS in the polyandrous versus the monogamous, but they could equally be the increase in LRS in the monogamous versus the polyandrous if the authors had coded their data differently. Thus simply labeling the axis 'estimated decrease in LRS' is not sufficient. I think that these parameter values would be best presented in a table, rather than included in the figure. It would be also preferable if the authors included all the data in the figures, for example using a violin plot, rather than just the means and the 95% Cis, since this provides the reader additional information about the distribution of the data.

5) Figure 2. This is perhaps a lack of familiarity on my part, but I do not know how these figures were generated or what they show. These are presumably the outputs of a model (there are some details provided at L575-577) but much more detail needs to be given here.

6) L136. I appreciate that the authors want to provide the details of the statistical analyses on female survival, but all the parentheses make this paragraph extremely difficult to follow. Perhaps including the results of the analysis as a table would make this much easier to read.

7) L146. Again, this paragraph is complex and difficult to follow. The authors may want to state the main finding of their data, before detailing the statistics that support this finding. As for the analysis of the LRS, the P-values of the main effects are questionable if they have been adjusted for significant interaction (which is what is implied in the use of type III ANOVA, L560). As an alternative the authors could conduct posthoc tests on the effect of temperature or mating system for each mating system or temperature respectively, applying appropriate corrections for a multiplicity of tests, e.g. Bonferroni. As for Figure 1, the parameter values for the main effects in Figure 4 (right y-axis) would be best presented in a supplementary table.

8) I find the evidence that temperature affects ejaculate quality to harm females much less convincing. The authors report data on the effects of the mating system on mating duration and remating latency in females mating with males that have been kept singularly (low sperm competition) or in groups of three (high sperm competition). They should clearly explain the relationship between sperm competition, ejaculate quality, and these two assays, with citations if these methods have been used before. The description of these experiments is particularly difficult to follow, but it appears that they recorded mating duration both for the first mating (with males having just been exposed to different levels of perceived sperm competition) and during rematings. Which of these is shown in Figure 5A? They also conducted mating assays on males that had been maintained at different temperatures for 48h or 13 days (L 502). Data from which of these are used in Figure 5A? Which of these were used for female remating latency? Because the experimental methods are so difficult to follow, it precludes an interpretation of the data and makes it difficult to determine whether the data support the conclusions of the authors.

9) L179: This is another dense paragraph that essentially shows that sperm competition risk does not affect female fecundity and survival. That is, while sperm competition may increase mating duration, or remating latency, these do not appear to result in female harm. This undermines the interpretation that changes in mating duration and remating latency with risk of sperm competition reflect the chemistry of the ejaculate. An alternative explanation is that maintaining males with other males may increase his mating duration, which in turn leads to an increase in remating latency. It is interesting to note that the interaction between temperature and risk of sperm competition on mating duration and remating latency reflects a decline in these dependent factors with temperature when risk is low, but maintenance when risk is high. Chemical analysis of the ejaculate would help clarify the relationship between temperature and sperm competition on post-copulatory female harm.
