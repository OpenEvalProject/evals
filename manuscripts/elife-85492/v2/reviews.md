# Peer review - Round 1

Editors:
- Magnus Nordborg, Gregor Mendel Institute Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85492.sa0](https://doi.org/10.7554/eLife.85492.sa0)

This is a rigorous and critical analysis of the performance of a popular suite of methods for inferring population history, accompanied by improvements. Should be of broad interest to anyone interested in human history.


---

# Peer review - Round 1

Editors:
- Magnus Nordborg, Gregor Mendel Institute Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85492.sa1](https://doi.org/10.7554/eLife.85492.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "On the limits of fitting complex models of population history to genetic data" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, including Magnus Nordborg as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Carsten Wiuf (Reviewer #2); David Balding (Reviewer #3).

Comments to the Authors:

We are sorry to say that, after consultation with editors and reviewers, we have decided that this work cannot be published in eLife in its current form. We all agree that the work is excellent, and the writing is good in a local sense, but the manuscript is also overly long and its current presentation makes not very accessible even to those who are genuinely interested in this area (see also individual comments below). While the manuscript contains interesting and important points about population genomics inference and human history, these are buried in what is best described as a mixture between a lab blog and a user manual for ADMIXTURETOOLS. It is thus unclear what the target audience is.

If you were willing to substantially streamline the presentation, so that it is more in the form of a conventional (computational) biology paper, we would be willing to reconsider a new submission for eLife.

Reviewer #1 (Recommendations for the authors):

Research on human population history has long used models of population splitting with subsequent admixture to make sense of polymorphism data (mostly from humans, but also from commensal species). In this paper, Maier et al use introduce algorithmic improvements that allow them to search the space of such "admixture graphs" more exhaustively and use them to re-evaluate a large number of published results in order to investigate whether the corresponding studies really found the "best" models. They find that they generally did not, and conclude that greater caution is in order when interpreting these kinds of data.

The work is encyclopedic (the single-spaced manuscript is over 50 pages - a monograph, really) and well written. The conclusions are well supported and illustrated by many examples.

The main problem I have with the paper is that reading it feels a bit like entering a cladistics meeting where people debate things like the significance of a particular scale on the middle toe of the Lesser Two-headed Tree Wrangler. While the overall point is clear, the details (and there are many) will be obscure unless you are intimately familiar with the specific examples. This means that the majority of the contents of the paper will/must be skipped by those not directly working on human population history. Which is a pity, as the overall conclusions are generally relevant.

Furthermore, just as would have been the case at a cladistics meeting, this paper is narrowly focused on a particular analysis framework. Technical terms like "f-statistic" are thrown around without introduction. In the few remaining corners of population genetics that do not work on human genetics, there are those who do not think in terms of discrete populations, and who hold heretical notions about isolation-by-distance. The question of whether *any* admixture graph is a good model for the data is not asked here - and it arguably should be given the generality of the title. As the paper makes very clear, there are indeed limits to what we can infer about history from genetic data. However, beyond a vague "here be monsters", the paper offers a general audience little guidance about which of the large numbers of claims in illustrious journals are actually likely to be true.

I think this is an excellent and important paper written for a narrow audience. If you want to reach a larger audience, a very different paper is in order.

I also think you do not address the very broad question in the title – this would again be a different paper.

Reviewer #2 (Recommendations for the authors):

The authors aim to correct inference problems with existing software by changing and implementing new features of Admixtools. The conclusions are supported by the results. The program will likely be much used.

The authors deserve credit for acknowledging that there might be many admixture graphs fitting a given data set equally well and that this fact has not been acknowledged in any/many previous study(ies), incl the authors own :-

Also they deserve credit for a quite substantial re-analysis of already published data.

The novelty and selling point seem to be a new version of Admixturetools (together with re-analysis). However, several of the "new ideas" implemented are already in Admixturetools 7.0.2, so the novelty is quite limited. While I acknowledge computational speed-ups, clever data manipulations, proper testing and so forth are important and important to publish, it does not seem to have the novelty-level required for eLife.

Reviewer #3 (Recommendations for the authors):

The authors briefly describe improvements to the popular ADMIXTOOLS software, now released as ADMIXTOOLS2. These include computational speedups that allow computationally-intensive resampling-based methods such as bootstrap to help assess model fit, even for large datasets, as well as a more extensive automated search over model space (exhaustive search is still infeasible, so constraints based on judgments of plausibility are still required).

Using these improved tools, the authors extensively re-analyse 8 published datasets (human, dog and horse), and find many conclusions of the original authors about demographic history to be not well supported. This is because there exist other plausible models, often many of them, that fit the data better, sometimes significantly so, that does not support the original authors' conclusions based on their preferred model. Often there are also even more alternative models that fit the data worse than the published model, but not significantly worse and so they cannot be excluded.

I'm a statistical methods person not closely familiar with any of the studies re-analysed here, so I don't have deep insights about the revised analyses proposed here. However, the authors seem to me to have conducted a careful and well-justified model fitting exercise with important conclusions and implications for future analyses.

The authors conclude with recommendations for future analyses of genetic data to make inferences about population history. They hope to change the field in a similar way to the step change in standards for statistical significance in association studies that occurred around 2008. The guidelines proposed are no doubt open to improvement over time, but I agree that this study is likely to have a big impact on the field of demographic history inference leading to better-justified conclusions from future analyses. The problem addressed is much more complex than genetic association, and conclusions based on limited exploration of a vast model space will always open to further improvement.

It's a very good paper, I don't have much to say at a general level except that it is very long and perhaps trying to do too much. The introduction of ADMIXTOOLS2 and the general discussion about principles of model fitting both seem inadequate. In contrast, the discussion of the re-analyses of datasets is very thorough. Perhaps two papers would have been better?

In a generally well-written paper I found the first sentence of the abstract confusing "… the only information needed to capture the patterns of allele frequency correlation among populations". Why is "capturing.… correlation" your primary focus? I would restate with an objective that is comprehensible to a general reader.

Abstract L17: "Our results suggest that strong claims.…. be made when all well-fitting and temporally plausible models share common topological features" This doesn't follow from the results, you are asserting it as a principle. The "all.… models" is perhaps a strong requirement when there are many of them.

L42 " finding fitting".

L163 " the time required to process.. trivial compared to the time required to compute.…" I found this confusing because its unclear to me what "process" means here.

L291 " Parameters with extremely wide confidence intervals can thus be immediately shown to be poorly determined." Vacuous statement – the paper is already very long! Delete.

L300 define "worst-residual" (maybe refer here to an explanation in methods).

L303 "… methods relying on AIC or BIC.… were over-aggressive". The merits of resampling based versus likelihood based model comparison is an extremely important topic, it's beyond the scope of the present paper to discuss fully here but you should be able to cite some authorities to support this claim.

L342 "to test the null hypothesis that the true difference in log-likelihood.… is zero" The log-likelihood is a function of the data so is not appropriate in a null hypothesis, which should be a statement about models/parameters and not data.

L375 "… without either fixing one of them or forcing the lengths to be evenly distributed." not strictly true and there must be a better way to say what you mean: we can only estimate 1 parameter, not both.

L514 "Lower scores of the fits obtained.… indicate overfitting to the full data set." This is one of the first of many references to overfitting that I found unsatisfactory as I did not notice a discussion of its implications for your analyses. Overfitting is a broad and ubiquitous phenomenon, why is it important here? I feel you should remove these (not needed to justify your main conclusions) or explain better. Are you diagnosing a mechanism that has led other authors astray? Also the specific wording "overfitting to the full data set" seems odd, is there any other kind of overfitting?

L614 "Near East" Near to what? East of what? Please use standard terminology that is meaningful to a general reader, not this outdated colonial-era relic. Similarly for "Middle East" (L687): that term is widely used but not appropriate in a science paper, use "West Asia" or "Eastern Mediterranean" something more specific. Also "Levantine" – is that a standard term in the dog world? It seems not from a quick search. Replace with some more meaningful to a general reader.

L662 "pseudo-diploid" has not been explained. I looked it up and the meaning I found doesn't make sense here.

L1119 "cannot be right" is not an appropriate way to summarise statistical evidence.

L1505 explain(or replace) "high degeneracy".

L1677 "time and population size as the two sources of genetic drift" they are factors affecting rather than sources.

Reviewer #4: (Recommendations for the authors):

Overview:

The article is composed of a review of the existing method for the admixture graph estimation and the update of the ADMIXTURETOOLS, and the application of the package to real-life examples. The Results section is hard to follow, and it contains substantial parts which would better fit the Introduction section and the User Manual. Figures are in their draft versions.

Plusses:

The existing ADMIXTURETOOLS method was improved by useful features (confidence intervals and identifiability of admixture graph parameters and the searching the space of all admixture graphs), and heuristics significantly sped it up for f-statistics computations.

Minuses:

L139: what are the philosophical differences between two versions of ADMIXTURETOOLS.

L169: the bias should be demonstrated more clearly.

L175: what is the regression approach to estimate f-statistics.

L186: "pseudo-diploid and pseudo-haploid" – these computational details are not properly explained if they are essential.

L190: "unbiased" – analysis of bias based on the number of samples is required.

L194: "inbreed: YES" option – user manual detail. This detail does not mean much for users who have not worked with ADMIXTURETOOLS.

L201: "incorrect algorithm for calculating" – should be explained more. It would be more important than to mention user manual details.

Figure1 should be rearranged in columns; there are a lot of places for it.

Figure1a: low subfigure x-axis should be reorganized.

Figure1b: if the formula for the F4 is exact, then what is the source of mentioned bias, and where is the heuristics.

Figure1c: what is the difference between all F3/4. Is there any conventional definition, and what is the difference between mentioned definitions? This should be organized as a table, nut a subfigure.

Figure1d: Why are formulas for F3 not presented.

Figure2: Dash dots for the y-axis levels should be presented to compare bars.

Figure3: (a,b) – what does it mean? The figure is in the draft stage.

1. No basic explanation for unprepared readers, what are f2/f3/f4, and what is the practical difference between them.

2. The article contains many references to features from the ADMIXTURETOOLS by names, without explanation. Authors should provide the text to a broad audience of eLife, but not for the users of ADMIXTURETOOLS.

Suggestions:

1. I strongly recommend revising the manuscript stricture. For example, the result section is a blend of "literature revie,"&"draft result"&"methods"&"program manual".

2. The text should be significantly reduced, especially when it is hard to read and seems to be in its draft version.

3. Type of the article should be defined more clearer: whether it is a research article? New method? Or a review manuscript of the existing methods.

4. Be more accurate with figures. In the current version, figures are not properly arranged and resemble draft versions.

5. Introduce the abbreviation for "admixture graph" as, for instance, AG.
