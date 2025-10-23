# Peer review - Round 1

Editors:
- Dario Riccardo Valenzano, https://ror.org/039a53269 Leibniz Institute on Aging Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83152.sa0](https://doi.org/10.7554/eLife.83152.sa0)

In this work, Roche et al. study a 13-year long time series of microbiome samples from wild baboons from Kenya. This data allows disentangling ecological dynamics within and across individuals in a way that has never been done before. The authors show that the ecological relationships among baboon gut bacteria, measured through a correlation based on covariation, are largely universal (similar within and across host individuals) and that the most universally covarying taxa are almost always positively associated with each other. This work is foundational in its compelling effort to generate a rigorous method to evaluate co-abundance dynamics in longitudinal microbiome data. The approach taken will likely inspire developments that will sharpen the capacity to extract co-varying microbial features, taking into account seasonality, diet, age, relatedness, and more.


---

# Peer review - Round 1

Editors:
- Dario Riccardo Valenzano, https://ror.org/039a53269 Leibniz Institute on Aging Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83152.sa1](https://doi.org/10.7554/eLife.83152.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Universal gut microbial relationships in the gut microbiome of wild baboons" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Dario Riccardo Valenzano as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Wendy Garrett as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Aura Raulo (Reviewer #2); Oren Kolodny (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Is the covariation data zero-inflated?

2. Did the authors find or analyze the age-dependency in microbial dynamics, i.e. whether baboon age is characterized by specific microbial associations that are not equally maintained across all age groups? More extensively: are there taxonomic covariations that are (i) lost or (ii) acquired during aging?

3. The pairwise species correlations can be explained in (at least) two ways: the species have positive relations in some way (e.g. one is providing something necessary for the other), or the two simply like to be in the same kind of habitat. The "same kind of habitat" may refer to both a similar broad environment of the host (including diet, soil type, etc) OR a similar within-host environment, i.e. host physiology, gut pH, immune status, etc. I would suggest having a discussion of these alternative explanations (and perhaps others) early on, and reference to this discussion in later interpretations of findings, throughout the results and Discussion sections.

4. A graphical summary that would explain the consensus model for the temporal dynamics of microbial pair associations would help clarify the take-home message to a broader audience.

Reviewer #1 (Recommendations for the authors):

I very much liked this work and I congratulate the authors for their contribution to the field of microbiome ecology.

I would suggest better clarifying the novelty compared to previous analyses performed by the authors on this dataset.

It was not clear to me whether the authors found or analyzed the age-dependency in microbial dynamics, i.e. whether baboon age is characterized by specific microbial associations that are not equally maintained across all age groups. More extensively: are there taxonomic covariations that are (i) lost or (ii) acquired during aging?

A graphical summary that would explain the consensus model for the temporal dynamics of microbial pair associations would help clarify the take-home message to a broader audience.

I would like to kindly ask the authors to explain their chosen criteria for authorship. In particular, the authors should clarify whether the contribution of any of the scientific collaborators in Kenya could be worthy of inclusion in the authors' list. To date, the support that goes into field work by local scientists and trainees is not sufficiently acknowledged by foreign researchers, and a more inclusive and less exploitative authorship system can make a difference in developing countries, promoting long-term scientific excellence.

Reviewer #2 (Recommendations for the authors):

• Regarding my worries over the effect of 0-0 links on the positive correlation assessment, if your covariation data is zero-inflated, I suggest you would consider whether a correlation measure based on SparCC-method (See: ), such as SpiecEASI (ref) might be a more robust way of estimating covariation through sparse inverse covariance. If your covariation data is magically not zero-inflated, I would suggest either making it into a bigger thing in the text or considering using the SparCC methods anyway, as they would allow you to have more of the rare taxa in the data. Alternatively, you could just show how much of your positive and negative correlation patterns respectively were influenced by whether or not you consider double zeros or any zeros in the data. You could do this either with separate models or within one zero-inflated hurdle model. If you can show that the pattern prevails even when you only compare non-zero abundances, that would make your correlation method that much more convincing.

• 10 permutations to address the significance of the correlations sounds la quite a low number to me. Would you have the computing power to do 100? I do not really understand how you get to p <0.05 with just 10 permutations.

• You could add a sentence to the abstract to elaborate on why we would expect ecological relationships to be individualized in the first place. I was a bit confused reading the abstract about why is this a matter worth such detailed exploration, but your introduction really convinced me. If you could add something from lines 82-91 into the abstract, it would perhaps make it more intriguing

• You show that population-level signatures contributed almost twice the weight as host-level signatures on correlation patterns. I think this is convincing. But I do think there seems to still be surprisingly much individual variation in ecological associations. I would have expected them to be even more universal, to be honest. I think it would be interesting to add also a discussion on why some taxa are strongly but inconsistently correlated – do these taxa have something special about them? Are they more generalist? Or do they have more positive links (can depend on many others rather than fully dependent on one other taxon)?

• Your universality score takes continuous correlation strength within individual and proportion of hosts with a majority sign as input. I like it, but wonder if you could capture even more of the variation in your data by also using a continuous measure of cross-sectional correlation consistency? Like additive correlation strength in the majority sign relative to additive correlation strength in the non-majority sign. Just a thought though.

• Lines 143-146, you could emphasize that if taxa covariation is driven by selection imposed by the host/environmental, then we would expect phylogenetically or phenotypically similar taxa to be positively covarying. If, on the other hand, covariation patterns were more driven by ecological interactions between taxa, we might expect positive covariation to be not more common in phylogenetically close taxa or less common based on competitive exclusion. Or is there some evidence that phylogenetically close taxa cross-feed more with each other or such?

• Lines 254-255, you write "Note, that the correlation strength for a given pair of ASVs was only weakly predicted by bacterial abundance " – Does this mean it was mostly driven by co-occurrence or that the covariation in abundances was sensitive to overall abundance? I guess the latter. More clarity would be good.

• Line 406, you write " Universality in Amboseli is not solely explained by seasonality or synchrony " – I think this is a bit manipulative title. There is quite a bit of evidence there for seasonality and synchrony and other evidence for environmental of host physiology-related selection driving covariation patterns (such as the fact that positive covariation is more common in phylogenetically close pairs). I feel like someone else could have formulated these results by downplaying the ecological relationships notion and emphasizing the selective effects notion. There is a bit of a tone here like you would prefer the ecological network effect over the environmentally driven covariation. I suggest rewording this to be a bit more neutral, such as "Universality is partially explained by seasonality and synchrony". And also mention that there may be other selective effects (like those related to individual variation in host physiology?) that you did not test but might feed into the selective effects driving covariation.

• Lines 465-467: I am not entirely convinced that the lack of similar patterns in the Johnson data set is likely explained by the different sampling frequencies. Was there much less temporal variation in the Johnson data set? To back up the statement that higher sampling frequency would be the reason the Johnson data set has dissimilar covariation between taxa compared to yours, perhaps you could show that the temporal variation in this data set was different from the baboon one and show that these covariation patterns were sensitive to timescale by subsampling either data to create mock data sets with different sampling frequency and see how this would change the inference of ecological associations. In general, I would tone down the generalizability to humans -conclusions a bit since only one of your data sets showed this, and it is in infants, who have an ecologically more unstable microbiome than adult humans.

• Lines 540-554. Can you clarify why exactly should environmental variation decrease the universality of ecological associations? I would imagine that environmental variation can expand the space of microbial covariation and if universality is driven by covariation due to environmental selection, then this should be maximal when there is broader space for environmental variation to exist. You mentioned in the intro that "genotype by environment interactions, and priority effects-can lead microbiome taxa to fill different ecological roles in different hosts", could you explain a bit more somewhere how this translate to more environmental variation leading to less clear covariation between taxa?

• Lines 575-576 What about individual variation in host physiology?

• Line 633 How much was the sparsity reduced?

• Line 643 Seems very cool but I cannot fully critically evaluate the statistical robustness of this modeling framework

Reviewer #3 (Recommendations for the authors):

• Good abstract, presentation, and introduction.

• Figure 2: perhaps mark in panel A what the threshold for significant positive/negative correlations was.

• Positive correlation – as you note in several places – can be explained in (at least) two ways: the species have positive relations in some way (e.g. one is providing something necessary for the other), or the two simply like to be in the same kind of habitat, so when it is good for one it's also good for the other. You are aware of this, as both possibilities are mentioned in several places, but it seems that sometimes you choose to offer one and sometimes the other, with no clear reason (e.g. you propose that correlations at the phylum level are due to environmental preferences – lines 217-219 – but this explanation is in contrast to the strong emphasis on microbe-microbe interactions that is found throughout).

• I would suggest having a discussion of these alternative explanations (and perhaps others) early on, and reference to this discussion in later interpretations of findings, throughout the results and Discussion sections.

(you are clearly aware of this, e.g. in line 407; I suggest discussing this topic in the introduction and referring to it throughout. This would help readers who aren't aware of the extensive research/discussion/debate about these questions in microbial ecology, landscape ecology, and elsewhere).

• A brief mention/clarification (at least) of causality vs. correlation would be a good idea in this context. Even if clear correlations are found between taxa, this doesn't imply causation, of course. Perhaps discuss in future directions the importance of intervention/manipulation studies to test for causation.

• There's quite a large literature in ecology, particularly microbial ecology, that deals with the link between pairwise interactions between bacteria within a larger consortium of species, and whether inferences can be made from pairwise interactions to more complex scenarios; consider referring to some of this literature and perhaps offering a discussion of your results in light of the insights proposed there. Some such studies (I'm not from the field, there may be better ones) are:

https://www.nature.com/articles/nature22898

https://onlinelibrary.wiley.com/doi/full/10.1111/ele.13211

https://www.nature.com/articles/s41559-017-0109

Also, have a look at one or two possibly relevant studies by Andrew Letten.

• A possible interpretation of the finding that correlations, when exist, tend to be positive: if the driver of significant correlations is the environment, and not positive species' interactions, then this observation might be expected: pairs of species that share environmental preferences will be positively correlated, and pairs of species that prefer different environments would be uncorrelated (and not negatively correlated).

In other words: there is only one way in which environmental preferences can be similar, but many ways in which two environmental preferences can differ (and also an environment is similar to itself in all dimensions, but there are many dimensions in which two environments can differ). "All happy families are alike, but every unhappy family is unhappy in its own way (Leo Tolstoy, Anna Karenina, 1878)".

In a sense, this observation should thus perhaps be viewed as support of the hypothesis that the driver of the positive correlations you find is shared environmental preferences and not species-species interactions. I think. Consider.

• 545-555: If true, the positive correlations are due to shared preferences of environment, it perhaps makes sense that the children dataset, in which children differ quite a bit (more than pairs of baboons), shows a strong signal: the fact that children are different should create high diversity in the overall dataset, and when two children happen to be similar in the conditions they create in their guts – this (and the respective positive correlations between pairs of species that like these specific conditions) would stand out particularly significantly above all this noise. Maybe. This requires some deeper thought, so consider. ((this may be analogous to assessing heritability of traits – heritability seems to decrease – sometimes to the point of being non-significant/below detection level – in a homogenic population, and heritability estimates are higher when the population is diverse))

• 572 – 576 (starting with "We surmise that most") – I would be more cautious about this statement.

I tend to think that the driver of the correlation universality in your data is shared environmental preferences, and – apart from the point I made above – I think this is also particularly likely in light of the phylogenetic signal that you found (it makes sense that phylogenetically related species have similar environmental preferences, stemming from homology; this seems to me more parsimonious compared to the possibility that related species tend to be more supportive of one another for some reason, even though I can come up with some handwaving explanations that could support this if I really had to).

The "environment" in question is the one in the gut. Thus, controlling for diet or seasonal drivers is good, but far from ruling out that there are shared environments that are driving the signal; for that, you'd need to control for the extent to which pairs of host individuals tended to have more similar pH, hormonal status, immune activation (and its profile) and so on.

• 589: There seems to be a problem with this sentence. Look at the "the fact that…" – seems like something is missing.

• Methods: I'd elaborate a bit further about the sequencing, e.g. whether you rarefied samples or accounted for uneven read counts in another way, and which 16s regions were amplified (and/or what their length was – amplifying just V3, for example, would lead to a very different ASV resolution from amplifying V3+V4).
