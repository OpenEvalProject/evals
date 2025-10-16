# Peer review - Round 1

Editors:
- Magnus Nordborg, Austrian Academy of Sciences Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67577.sa1](https://doi.org/10.7554/eLife.67577.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper shows convincing evidence of correlated seasonal changes in allele frequency over large geographical scales.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Broad geographic sampling reveals predictable, pervasive, and strong seasonal adaptation in Drosophila" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Magnus Nordborg as the Reviewing Editor and Reviewer #3, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jeffrey Ross-Ibarra (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife at this stage.

This decision is not based on the quality of the study, or of the importance of the work, but rather on problems with the analysis, which we think will require months to rectify". Therefore, our decision should be seen as "reject, but encourage to resubmit".

As is evident from the individual reviews below, there is no doubt that this is an important and interesting study. However, while we are generally inclined to believe most of your results, the quality of the analysis leaves much to be desired. It needs to be simplified, and the many ad hoc assumptions justified or dropped.

There are also serious concerns about sampling (reviewer #1) and about whether the proposed model would actually work.

We hope these comments are helpful.

Reviewer #1:

In this manuscript the authors present an analysis of seasonal allele frequency change in multiple population samples of D. melanogaster that have been sampled in spring and fall from a number of collection sites within North America and Europe. Briefly, the authors search for seasonality of allele frequencies using simple linear models and then look for coordinated changes among populations. The authors report decent overlap among "seasonal" snps, overlap with sites found to be clinal, as well as a number of ancillary results.

In general I think the dataset is quite interesting and the study to be timely. While that is so there are a number of technical issues throughout the paper and it suffers in numerous places from what I think are inappropriate statistical assumptions. While this is so I'm sympathetic to what the authors are attempting to do-it is hard to do correctly.

1) I have a number of concerns about the sampling design of this study:

a. First and foremost there is no consistency to the sampling date between years or localities. For instance the Fall samples from Linvilla, PA were collected either in October or November. Indeed a quick search for average temps reveals that at their collection site the average daily temperature differs by ~ 10 degrees F between those two dates. Thus I'm concerned that "season" is not a properly replicated factor across the design and instead there could be significant batch effects.

b. I'm concerned about the possibility of contamination from accidental collection of D. simulans that should vary systematically between the seasons (we know that the abundance of sim vs mel in local collections changes dramatically throughout the season. While the authors are rightly trying to account for this by competitive mapping more assurances should be given that this is working. I would like to see a simple simulation demonstrating the power of the competitive mapping proceedure-a straightforward way to do this would be to make synthetic pools of reads from melanogaster and simulans, while varying the percentage of simulans in the pool, and then take those simulated pools through the authors' mapping procedure. In addition, the authors should provide the percentage of reads that mapped to the sim assembly for each sample in Suppl Table 1. Once they have those they should test for an effect of season on that percentage.

c. I notice from the methods that collections varied with respect to baits used (banana or yeast), versus aspiration versus netting. The authors should provide the associated details on the Suppl Table as well check for batch effects again. It would be a shame if collection strategy were a hidden confounder.

d. Finally a question: the authors examine the genital arch of collected males to try to exclude simulans from the pools that way?

2) The heavy filtering of SNPs here will lead to some interesting ascertainment biases. Not only are they filtering out rare and private SNPs but the authors are requiring that the SNPs are found in EVERY population. We should expect this to be quite a biased set of SNPs, likely in the direction of enriching for balanced polymorphisms. While this is what the authors want to find I guess, it means that any statements regarding the percentage of SNPs that are under seasonally varying selection (and thus temporally balanced) will be significant overestimates. The authors at the very least will need to add significant caveats to their interpretations, but I would encourage them to consider redoing the analysis on an unfiltered set of SNPs as well, even if that means that the authors have to restrict portions of the analysis to within populations.

3) Line 742-I'm concerned that the authors are using too simple a regression here. They are assuming that allele frequency in fall is independent of allele frequency of spring within a population, which of course it is not. At the very least I think the authors' should be doing a repeated measures regression, but I wonder if there are even better ways to do this statistical testing, perhaps using a method of regression appropriate for autocorrelated timeseries observations.

4) Line 821-this model is not appropriate as observations of allele frequencies among populations are correlated via shared population history. The authors need to account for that covariance structure in this regression. See for instance Coop et al. 2010

5) Line 841-among population comparisons of the "rank p-value Fisher's method" test (can the authors come up with a better name?) are concerning as the authors are using number of reads as the data. If there are differences in read depth between samples, and there are, won't this test will have different power among different populations?

6) Lines 309-314. This analysis is unconvincing and the result quite weak. I note that the authors in this one tiny section are now presenting Pearson's R instead of R2. The coefficient of determination is very low for each sample here. Thus I feel that the authors are over interpreting what they have done.

7) The "Flipped model" strikes me as troubling philosophically. The authors' report a negative relation, so to make it line up with observations from other populations they are flipping the season labels? The authors need to do quite a bit of work to justify this as anything other than p-hacking, and the authors in my opinion should remove analysis of the "flipped" set from the paper.

Reviewer #2:

Overall this is a very nice study that convincingly shows an impact of seasonality on allele frequencies across many Drosophila populations, suggesting temporally-variable balancing selection may impact a large proportion of the Drosophila genome.

Are the estimates of the number of SNPs and strength of selection consistent with the observed patterns and decay of Fst? That is, how well does Fst and the decay of Fst in your simulations match the observed data?

Given these same parameters it might be fun (but admittedly speculative) to estimate what proportion of sites in the genome are affected by "seasonal draft".

What does the estimate of the strength of selection and number of sites affected tell us about load? Are local Drosophila population sizes sufficient that this is plausible without leading to extinction?

Of course the flipped model does provide more convincing evidence of some sort of seasonal effect, but I think I need a bit more convincing that the flipped model is justified other than the fact that it makes everything fit the preconceived model better.

How important is identication of individual causal loci (Line 653)? If the trait really is highly polygenic and there is limited concordance in loci among populations, how likely is this to be succesful? This doesn't seem to me the natural conclusion from the work presented. It seems to me that careful quant gen studies of phenotypes, selection gradients, and how Vg or Va change among populations and over time might be of more interest.

I'm generally not a fan of GO analyses but recognize that many readers will ask for such tests; I thought the paragraph presenting these results was appropriately cautious.

The definitions of spring and fall confused me somewhat. Are they based on per-location information on sampling abundance of Drosophila? It seems like there must be good weather station data for most of these locations; could a definition based on known thermal tolerances of Drosophila could be used?

What proportion of the ~1M SNPs filtered because they were not found across all populations show evidence of seasonal allele frequency change? It seems like population-specific variation is an interesting area that was left unexplored? Does this also explain some of the difference between Bergland 2014 and the present study?

Reviewer #3:

This manuscript addresses a classical question with unique data set. I was looking forward to reading it, but was disappointed by the statistical analysis, which I found both baffling and inappropriate.

I think the core of the problem is clearly and explicitly specified models and questions. Instead, you use a series of ad hoc tests that quickly made me lose faith in your conclusions.

It starts at the beginning (l. 186), where you perform a "test" of allele frequency change without specifying what you are testing, and why. After flipping between the 3-4 copies of the file I needed to have open to simultaneously look at text, figures, supplementary figures, and methods (which are not well written, see, e.g., the meaningless equation on l. 742), I think you are simply testing whether the spring frequencies at each SNP in each population differ significantly between spring and autumn under a very naive model, which you reject genome-wide (Figure 2A). But rather than tossing out this model and going back to the drawing board, you base all the remaining analyses on complicated intersections of p-values (which are inherently irrelevant in this paper, since you are not trying to identify individual loci).

This seems very odd. The main question of the paper is whether allele frequencies change consistently across populations, and the natural way to test this is using some kind of permutation scheme using the allele frequencies differences. You have naturally paired data, which probably can be treated as independent replicated (although this requires an argument about migration).

Having established this, why not fit the whole data set into a generalized mixed linear model, without a priori assumptions about the distribution of the random changes in allele frequencies (which must reflect both estimation error and random drift), and with explicit terms for selection (as a function of local climate) and (possibly) migration.

This would be so much easier to interpret than the ad hoc analyses you carry out, and would also avoid possible biases due to arbitrary p-value cut-offs for SNPs.

Using such an approach, it should be possible to estimate what fraction of the genome changes in a non-random fashion. Less sure about the strength selection, as I think this only has meaning within an accurate demographic model (which you do not have).

To sum up, I don't think you are doing your data justice here.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your work entitled "Broad geographic sampling reveals predictable, pervasive, and strong seasonal adaptation in Drosophila" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Magnus Nordborg as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that our decision remains the same as after the first round: you are welcome to resubmit, but dramatic changes are (still) necessary. We are sorry if we didn't manage to explain this the first time around.

Although we remain convinced that your study may contain an important and interesting result – strong selection related to season/climate on a wide geographic scale – your analyses largely obscure this. A much simpler (and shorter!) paper that focused on convincingly demonstrating this fact would be much better.

Other major problems include the "flipped" analysis, which is not only post-hoc, but serves to illustrate that you should use climate data directly since the seasons obviously aren't really seasons, and the selection simulations which are based on models that are too simplistic.

Finally, arguing that the "haphazard" sampling is a strength, is, well, not convincing.

Our recommendation remains the same: given that the sampling is haphazard, simplify both claims and analysis in order to make the former rock solid. As you know, a recent pre-print by Buffalo and Coop argues that there is no signal in your first paper: here is your chance to prove that you were right after all.

Reviewer #1:

This version is much better than the previous one, but I still find the analysis confused and confusing. I will comment further below, but before getting to this, I should state clearly that I know how difficult this is. We are currently struggling with analogous data from Arabidopsis, and it clear that we lack an established framework for thinking about them. This is not textbook stuff.

A related, high-level comment is how ridiculously primitive we are from the point of view of basic ecology. We have no idea how selection is working, either in time or space, much less what the main selective pressures are. You write in your introduction that you "elected to solve these two related problems by (i) working as a consortium of Drosophila biologists (DrosRTEC or the Drosophila Real Time Evolution Consortium) and (ii) sampling in a somewhat haphazard manner." The first point is good, but the second is nonsense. The solution is surely not the kind of haphazard sampling described in this paper, but rather dense and non-random sampling in both time and space. (This is needed for Arabidopsis as well, btw)

When I first read this, I didn't even realize that all your samples were not collected in a single year. This raises the issue of why you don't take this into account. In our multi-year Arabidopsis field experiments, we find that there is often greater variability between years than between sites located near 1000 km from each other in a north to south direction (moving from deciduous forest to taiga).

First, what is the temporal correlation? The effect of space is clear from you PCA, but does time explain anything? How far do these flies move?

Second, you don't use climate data except to carry out your post hoc "flipping" of fall/spring labels. Did you try using climate data to explain what you see instead of a priori notions of spring and fall that you yourself dismiss as inadequate? We found that PCAs of multi-dimensional climate data was more strongly correlated with fitness than geographic proxies.

Another major unknown is the demographics of fruit flies. Your analyses assume (explicitly when you simulate selection) that each sampling location is a population (that dreaded population genetics abstraction that we all know doesn't really exist). You convincingly demonstrate that what you see cannot be due migration of randomly differentiated flies (because there is some kind concordance in changes globally), but this does not preclude that most of the allele frequencies be due to migration of selectively differentiated flies. Perhaps what happens is that there is selective die-off each winter, leading to cold-hardy survivors being overrepresented each spring – until they are swamped by southern migrants with vastly greater population sizes? Still selection, still adaptation, but with rather different predictions for the dynamics of allele frequencies. Talk about how fast populations adapt is less meaningful when we don't know what a population is. Returning to my initial point, to understand adaptation, we must understand the spatial and temporal scales over which allele frequencies chance. You don't have the sampling density to do this.

Glass half full: if you really see consistent changes despite all this, there must be some BIG signals out there…

I am convinced that you do see such changes, but my main comment remains that I think you could learn more from these data if you took several steps back and thought carefully about alternative models, and the simplest possible way to test. I suggested using the paired structure (you still need to show that pairs can be treated as independent, btw), but I think you can take it further than you have in estimating effects at individual SNPs. But it is not my job as reviewer to tell you how I would approach this, but rather to check whether I think your claims hold.

Point-by-point then, I am convinced by your permutations that there are large coordinated changes, but you still need to discuss the possible role of spatial and temporal correlations between pairs. Also think this point could be made better by going directly to estimates of allele frequency change, or beta from regression rather than involving p-values.

I find the whole "predictability" analysis convoluted and unconvincing. An attempt to shoehorn observations into an a priori framework. The leave-one-out analysis also requires some discussion of whether these points are independent, and I think it would not be necessary if you directly estimated consistent effects using permutation.

The comparison with clinal data is interesting, but again suffers from too strong priors of what is going on. You have climate data – why not simply check whether there are variables that explain both spatial and temporal shifts?

I find your analysis of the strength of selection across the genome unconvincing for the reasons outlined above: you have absolutely no idea of the demographic model, and treating each population as a close system (i.e. generating fall by sampling from spring) is simply not warranted.

The analysis of which SNPs are under selection is not convincing. The complete lack of correspondence between the original and the "flipped" model strongly suggests that the peaks are not to be trusted. Here is where jack-knifing and bootstrapping might be useful: to assess the robustness of your p-value estimates. My guess is that while your data is strong enough to show that there is selection in aggregate, getting down to individual loci is not possible. This also militates against relying of high-significance filters rather than the whole distribution of effect sizes.

Reviewer #2:

I have read the revised submission and the responses to review carefully. I still have major issues with the analysis done in this manuscript.

1) The authors still provide textbook case of p-hacking through their "flipped" analysis. Their justification-that the leave-one-out analysis tipped them off to a flipped effect-is not a justification at all. This entire section of the paper needs to be removed.

2) The binomial GLM that the authors are doing is inappropriate, as I pointed out in the initial submission. The "paired-fashion" of sampling helps nothing-the authors are simply testing against the null of their being no-difference in frequency between seasons assuming a binomial error model. The binomial error model here is inappropriate because spring and fall are not independent draws from the same parameterized distribution-allele frequency change is expected to occur do to drift. The authors are not accounting for this and it is a major flaw. I would suggest at the very least that the authors using a Nicholson et al. type framework for accounting properly for allele frequency change between seasons.

3) The justification that the authors give about "haphazard sampling" is risible. Adding noise does not add "inferential power" as the authors claim on line 174

4) The issue of biased ascertainment of SNPs has not been dealt with. The authors simply give their same estimates of genome-wide numbers of SNPs affected by seasonal selection and then follow it with a caveat. All such genome-wide estimates should be removed-you can't estimate them given your ascertainment conditions. Moreover you say on line 235 "Whether this SNP selection process generates bias in our estimates […] remains to be determined." This is unacceptable- your ascertainment definitely creates bias- this language brushes that under the rug.

5) The code for the permutation routines and the control SNP matching needs to be shared.

6) Lines 293-295 The authors are reporting that permution suggests the p-value of enrichment > 0.1. This suggests chance and nothing else is responsible for the observed effect despite the authors' conclusion of "robust evidence that parallele seasonal adaptation is a general feature…"

7) Line 309-no enrichment test has been described.

8) Line 330-Citing Gould here is silly. Pick a more appropriate citation.

9) Supplemental Figure 7-in the Bayesenv analysis that I asked for the "All" curve looks very different and goes against the conclusion that the authors are making. No explanation is given.

10) The ABC analysis, now described, is not using proper population genetic simulations of allele frequency change per generation due to drift + selection. As written there is only one generation of drift. This needs to be changed to take this analysis even moderately seriously. Moreover the code for these simulations needs to be shared.

11) Line 1020-In the corcordance regression the authors are doing a binned regression-this is never appropriate and the authors need to redo this analysis without binning.

Reviewer #3:

Overall this is an improved manuscript. Easier to read and follow, and better explained. There are several points I think that should still be addressed.

I am still not a fan of the flipped model. I agree that some of the evidence (predicting into the validation set, etc.) does indeed argue it's a better fit, but it still feels like ad-hoc subjective tweaking of the data until it fits well. I would prefer it to be removed from the paper -- I think show the original model and point out that some population show the reverse pattern and that matches with temperature. Perhaps even include the flipped model in the supplement. I would find that more convincing than the flipped model I think. In either case, the paragraph starting on line 445 should go, as even the authors admit this doesn't really show anything meaningful. The flipped model should also be removed from figures 2A and 2B as again it will by definition show a more convincing signal here.

As an alternative to the flipped model or presenting the data with the course labels of spring and fall, why not actually model the temperature data available? It would seem an objective a priori approach that should allow for differences in the flipped populations (i.e. presumably the difference in temperature the 3 weeks prior between Fall and Spring behaves differently for the flipped populations). Perhaps use mean temperature in the 3 weeks prior and/or the slope of the change of temperature over that time? I'm sure there are more creative/intelligent options, but I don't quite understand why the authors can't use this data instead of grossly categorizing things as spring or fall. I didn't see a good reason for not doing so in the response?

I find the authors treatment of enrichment odd. In some places it is presented as convincing evidence, and in others (line 563) it is disregarded because of absolute numbers. The logic on line 563 is fine of course, but I would like to see enrichment treated the same way throughout. On line 477 it is convincing as a log odds score, and in the paragraph starting on line 318 a modest percentage enrichment is considered good evidence.

I'd like to see a bit more exploration of the clustering. Figure 5D (visually) and the 100kb window analysis seem to suggest that clustering is on a relatively large scale, yet the analysis presented on 629 for % genome and s only investigates 5kb windows. If I'm understanding the ABC correctly it should be pretty fast to run, and it seems like running it on 50, 100, or even 500kb scale might be of interest. (To my eye some of the figures in S10 start to suggest a flattening of the ridge when done at 5kb scale). Certainly the data do appear to argue for a polygenic architecture, but whether this is ~50 windows or 5% of the genome I think isn't well differentiated.

Line 800: I agree with this logic about temperature and why some populations behave differently. I would have liked to see this prediction about temperature earlier in the introduction. Naively my first impression was that Fall populations would be adapted to cooler conditions and Spring to warmer. I see now why that is wrong, but I think stating up front that Fall populations are expected to reflect adaptation to warm summers would help some readers.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Broad geographic sampling reveals predictable, pervasive, and strong seasonal adaptation in Drosophila" for further consideration by eLife. Your revised article has been evaluated by Patricia Wittkopp as the Senior Editor and Magnus Nordborg as the Reviewing Editor.

Almost there! As you will see from the comments below, we got a fresh 3rd reviewer, who picked up on something we agree should be addressed, namely the likely role of inversions. We have two suggestions for how to proceed. Either: a) go through the manuscript and make sure you emphasize that much of the signal may be driven by inversions, and that it is impossible to know how polygenic this really is, or; b) provide additional analyses (e.g., of the X chromosome), to demonstrate that there is a signal independent of inversions.

Reviewer #1:

The authors were trying to confirm preliminary results suggesting that environmental changes accompanying seasonal change drive genome-wide allele frequency changes in Drosophila. This would give new insight into how selection works, and what factors might maintain genetic variation – at least in short-lived organisms. Although the detailed mechanisms are obscure, the authors use parallel changes over large geographic distances to argue convincingly that some form of seasonal selection must be taking place.

This is the third time I see this manuscript, so I will say no more than that it is greatly improved. I'm happy with it.

Reviewer #2:

This is a much improved, clearer version of the manuscript. The analyses are simpler and better explained, and the results I think come out clearer as a result.

Reviewer #3:

The strongest seasonal signal comes from inversions. If inversions are responding to seasonal selection, it is not surprising that the authors find parallel SNP changes across populations as the same inversions are shared globally. Unless the authors refocus the manuscript on parallel selection on inversions, their analyses need to be modified: almost all analyses use the full SNP set, but to study real parallel selection responses on the SNP level, the authors need to restrict their analysis on SNPs, which are not affected by inversions. To this end, it is important to keep in mind that inversions may suppress recombination also outside of the inversion, which makes it a bit challenging to determine the autosomal fraction that is not affected by inversions. A much better strategy would be to analyze the X-chromosome, which is the only major chromosome free of inversions. Unfortunately, the authors excluded this chromosome from their analyses.

Anyway, inspection of Figure 2D shows that the signal for seasonal SNPs is erased for regions outside of the inversions. Furthermore, a significant concordance pattern between seasonal and clinal SNPs outside of the inversion is restricted to 2L and 3R, the chromosomes with the strongest inversion effects. This could be interpreted as an effect of inversions on the genomic regions flanking the inversion.

How do the authors interpret a (presumably significant) underrepresentation of concordance SNPs on 3L?

Apart from my doubts about the significance of the seasonal selection signal, I would like to come back to the novel aspect of the manuscript-sharing seasonal SNPs across populations. The authors highlight, probably correctly, that seasonal adaptation is polygenic. This raises the question of whether parallel selection signatures are expected in differentiated populations. In my opinion two lines of reasoning speak against it: 1) probably more variants are segregating in the populations than required for seasonal adaptation (redundancy) 2) the frequencies of the seasonal SNPs most likely differ between the populations. Hence, SNPs closer to 50% are expected to respond more to the same selection pressure than SNPs with more extreme allele frequencies. This will lead to different power to detect the same selection response in differentiated populations.

Analyze the X-chromosome.

Remove the second season from the locations where two spring-fall pairs were included-only this makes the comparison unbiased.

Evaluate whether the spring-fall permutations remove the statistical issues of the GLM and Fisher's exact tests mentioned by the previous reviewers. Clarify that the matched controls were done on a sample basis, rather than across samples.

Clarify that the effective coverage was calculated per SNP.

The authors cite theoretical work, which suggests that seasonal SNPs may be maintained for highly restricted conditions (changing dominance)-do they find empirical support that these conditions are met in their data?

The significance of the manuscript to a broader audience could be increased by:

– A statement that the seasonal selection response is restricted to inversions-but I doubt that this is the message the authors would like to portray.

– A general discussion about the expectations of parallel selection signatures on the SNP level across populations and why the authors expect to see it (or find it against the expectations).
