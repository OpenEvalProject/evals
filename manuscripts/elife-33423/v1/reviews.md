# Peer review - Round 1

Editors:
- Michael Doebeli, University of British Columbia Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33423.020](https://doi.org/10.7554/eLife.33423.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Current CRISPR gene drive systems are likely to be highly invasive in wild populations" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Diethard Tautz as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: James Bull (Reviewer #2); Bernard Dujon (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Your paper shows that although resistance prevents drive systems from spreading to fixation in large populations, even very ineffective systems are highly invasive. Based on this it is argued that standard gene drive systems should not be developed nor field-tested in regions harboring the host organism.

The main concern of the reviewers is that the rather forceful message of the paper is not really substantiated in the sense that it is unclear why a high peak frequency of gene drive systems is necessarily a bad thing. For example, transposable elements have recently risen to high frequency in wild Drosophila populations, and while investigating the mechanism of this rise (and its potential prevention) are very interesting topics, it is unclear that this rise is a bad thing for these Drosophila populations. In other words, a rapid spread does not necessarily imply doom. I think this should be acknowledged in some form by the authors, and the message should be tuned accordingly.

The reviewers also raised a number of technical points, e.g. about the effects of a cost of resistance. These concerns should be carefully addressed.

Reviewer #1:

This is an interesting paper on the dynamics of the CRISPR gene drive system. Contrary to prevalent opinion, the authors conclude that invading gene drive systems may have a lasting impact even if they do not go to fixation. In particular, substantial "peak drive" occurs under many conditions. Based on this the authors caution against being careless with such systems, particularly when it comes to introduction of gene drive systems into wild populations.

The theoretical analysis is comprehensive and appears to be sound. The conclusions regarding the danger of gene drive may be a bit too sweeping.

Specific comments:

- The authors start out by pointing out the need for stochastic models of populations with finite size. However, in Figure 9 they effectively show that deterministic models make the same predictions as their stochastic models (if I understand this figure correctly). So why do we need stochastic models after all? This should be better explained, since it is part of the main rationale for the analysis presented in the paper.

- The model assumes that death is random, but births occur according to fitness. What if birth is random, and death is proportional to fitness? (There are some models in which this makes a difference…)

- It seems that in the model, invasion is always initialized with homozygotes? Can this assumption be relaxed?

- I don't really understand this statement, "Invasion is very unlikely when the drive is not initially favoured by selection." I thought the drive allele is never favoured by selection, as measured by the fitness values.

- Why show mean and median in Figure 1E,F.

- I don't really understand Figure 2E: it shows that the probability of invasion into one local population depends on migration rate, but that probably should not depend on migration at all, because as I understand it, the figure presumably refers to invasion of the drive in the local population into which the drive is initially released.

- Choosing populations proportional to the "square of total fitness" seems odd. Shouldn't it be the sum of squares of individual fitness values, or something like that?

Reviewer #2:

Conceptually, I view this paper as having two parts. The first is an analysis of gene drive models to study the spread of drives and consequent evolution of resistance to the drives. The second part is a value judgement on the deployment of drives. The latter occupies little space in the paper, but is extreme and certain to attract attention ("Contrary to the National Academies report on gene drive, our results suggest that standard drive systems should not be developed nor field-tested in regions harboring the host organism" is the last sentence of the Abstract). For convenience, I will refer to these as Part I and II, even though the paper is not structured that way.

Part I is possibly the most comprehensive analysis to date of drive and resistance evolution under alternative population structure scenarios. The overall message is that drives are highly invasive, albeit only temporary, despite resistance evolution. The quantitative details are not intuitive, but I would say the qualitative conclusion is obvious. Most of the models here assume a drive fitness cost of 10%, and what is not obvious is now far a drive allele would rise before being shut down by resistance evolution – the resistance evolution is assured by the fitness cost of the drive. So one cannot immediately guess how abundant a drive allele will get before being suppressed, and indeed, that answer also depends heavily on the rate of mutations to resistance. But if we reduce that cost to 1% (or even 0, values which I think are not addressed, but I did not really check), then resistance evolution is much less of an issue, and the drive allele will get very high before it goes away. (My intuition says that the drive allele never goes away if it has no fitness cost.)

So anyone broadly familiar with the process will a priori appreciate that low-cost drives get to very high frequencies in the population. And if they get to high frequencies, they will be able to invade new populations and overcome all sorts of barriers – will easily escape many hoped-for containments. I don't mean to trivialize the effort here, but if the point of this work is to propose a halt to gene drive releases on the grounds that gene drives are invasive, I'm not sure the analyses here are necessary. (In contrast, if the point was to identify realms of parameter values in which the authors thought releases were safe, then such analyses would be needed.)

One interesting outcome of this study is the demonstration that resistance will evolve quickly and suppress further spread of the drive allele even with a relatively low drive fitness cost. This result may have relevance to proposed uses of gene drives to extinguish populations.

The results are used to bolster an opinion, expressed at the end of the paper and in the Abstract (as noted above) that gene drives should not be released where there is any possibility of escape. While I might accept some justification for this opinion, it goes far beyond the work presented in the paper. Whether a drive should or should not be released depends on many social factors, including the possible good that might come from the release. It is a decision for societies, and the role of science is to inform those decisions on the possible consequences. I thus think that such an apparently bold statement puts the authors in (what I consider to be) the indefensible position of appearing so arrogant as to claim the right to impose their value judgement on the entire world – when many scientists think that gene drives could ultimately save tens of millions of lives a year. Furthermore, the paper does not actually identify any biologically serious consequence to a drive release – the drive in these models merely spreads and modifies the genome throughout the population (which some people would object to, but which may have almost no fitness consequence).

So I would suggest (= my 'opinion') that the opinion expressed be tempered accordingly and perhaps tied more closely to the findings here: "Our results suggest that drives are highly invasive under many scenarios. If there are negative consequences of drive escape, then.…". But it could certainly be interesting to watch the reaction if the paper maintains its strong, unqualified statement. If nothing else, the authors might at least label their advice as an opinion.

Reviewer #3:

This is a short, dense and interesting article in which the authors quantitatively predict allele frequencies in a variety of theoretical populations submitted to artificial gene drive. The article limits its investigation to sexual populations of diploid individuals and to alteration-type drives. The general conclusion is that the drives have high probabilities of being invasive in wild populations, even highly structured ones, unless the gene flow between subpopulations is very low. This is true even if the homing efficiency is low. Based on their quantitative simulations, the authors conclude that presently available drive systems should not be field-tested, contrary to recent conclusions of the National academies of Sciences, Engineering and Medicine. This issue is serious enough to merit publication of this article.

I found the article well documented on the CRISPR gene drive systems and the recently published laboratory assays. Their analysis presented in Appendix is very useful.

My only concern about this work is that all computations were made with the hypothesis that resistant mutations were neutral. This may be true for the experimental models reported but cannot be considered as universal. A fitness cost of the resistant mutations would immediately alter the results in Figure 1D and in Figure 2, for example, and I would urge the authors to take this parameter in consideration.

Incidentally, in the first natural gene-drive ever reported, the group I intron of yeast mitochondrial DNA discovered nearly 40 years ago, resistant mutations to the homing-endonuclease had a major cost because they fall into the peptidyl-transferase center of rRNA. The only choice left to yeast was between being sensitive to intron invasion or being severely unfit.
