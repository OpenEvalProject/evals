# Peer review - Round 1

Editors:
- Sarah E Cobey, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80329.sa0](https://doi.org/10.7554/eLife.80329.sa0)

Many approaches to predict which animals species might be at risk of infection by SARS-CoV-2 focus on features of the ACE2 host cell receptor to which the virus binds. This important study shows that such methods are not uncovering a true biological signal. Instead, Mollentze and colleagues show that ACE2 sequences are effectively only a proxy for generic species relationships, and species phylogeny alone can provide equivalent predictive power.


---

# Peer review - Round 1

Editors:
- Sarah E Cobey, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80329.sa1](https://doi.org/10.7554/eLife.80329.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Variation in the ACE2 receptor has limited utility for SARS-CoV-2 host prediction" for consideration by eLife. I apologize for the delay in the review process.

Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Miles Davenport as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tyler Starr (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

We have decided there are no truly essential revisions. However, the reviewers have suggested ways to strengthen the writing and analysis. Please consider them carefully. We deem the requested clarifications important enough to merit a revision or reply.

Reviewer #1 (Recommendations for the authors):

1. I found the logical flow a bit indirect. As the authors point out in the introduction, ACE2 binding is necessary but not sufficient in conferring susceptibility. However, the focus they then ascribe to ACE2-based data and ACE2-based predictions weakens the forcefulness with which they introduce this idea that determinants beyond ACE2 binding are going to be important in a full evaluation of animal susceptibilities. For example, the plurality of points in their collated dataset on "susceptibility" derives from (although acknowledges and de-prioritizes the significance of) heterologous ACE2 expression in cell culture viral entry assays, thereby missing all downstream determinants of susceptibility. Furthermore, more and more elaborate models based on ACE2 alone are built (e.g. amino acid classifications, site-wise determinants, ACE2 distance). My interpretation is that this is an attempt to "do the best that can be done" with ACE2 sequence alone so as not to create a straw-man argument for the ACE2 sequence features to then compare to phylogeny alone. This is why I present this as a logical flow issue, and perhaps not a scientific issue. Some ideas to improve this flow could be to spend more of the Introduction emphasizing the importance the field typically puts on ACE2 sequence alone and not as forcefully explain why this is unlikely to be a sufficient proxy (can leave this description until results or discussion), leaving the punchiness of the conclusion that it is indeed not that powerful as a less obvious outcome than is currently presented after the Introduction.

2. Toward the question of the sufficiency of ACE2 binding data alone for predicting susceptibility: when evaluating the hierarchy of evidence used in the final collated dataset (where animal-based studies trump heterologous ACE2 cell culture experiments), were there any cases where an ACE2 receptor is known to be sufficient to enable cell entry but the animal itself is not experimentally susceptible? Highlighting any observations of this seems the most direct evidence to the point that ACE2 sequence alone is insufficient to predict susceptibility.

3. I wonder whether a more pseudo-mechanistic two-step model could be considered or proposed in the Discussion – a first step based on ACE2 sequence (the "first step" necessary for susceptibility), and the second based on broader determinants of susceptibility (which would be best captured by phylogeny given complexity of unknown unknowns). The reason this may be helpful is that ACE2 binding can be "flipped" on or off with individual amino acid mutations and therefore more quickly deviate from phylogenetic trends (e.g. due to virus-host arms races in Rhinolophus bats, PMID 32699095, but see point 6 below). The broader determinants of susceptibility involve many complex components from cell biology to physiology, and so of course can not be tractably ascribed to a single gene sequence, but also may be better captured by a phylogenetic scale anyway. Such a two-tiered model could also better accommodate the multi-tiered data that is collapsed into a single training paradigm in the current study – for example, the simpler heterologous ACE2 entry assays could be incorporated only for the "first step" of model evaluation, while the whole-animal susceptibility data could serve as a target for the second step / integrated two-step model. This model would lose the utility of the phylogenetic model as illustrated in Figure 5, in that ACE2 sequence would need to be known, but could better incorporate multi-modal data to improve predictive accuracy.

4. Many species of bats show dramatic ACE2 polymorphism centered on positions contacted by sarbecoviruses, and this variation is known to influence binding of certain sarbecoviruses (e.g., PMID 32699095). How did you account for ACE2 polymorphism in analyses -- did you just resolve each species to a single ACE2 sequence? And how do you incorporate into the model possibilities that certain ACE2 alleles within a single species are permissive to entry by some sarbecoviruses while others are not?

5. Related to the above point (and a concern that I had about species like R. pearsonii which are seemingly not susceptible to ACE2-utilizing sarbecoviruses, but then I saw Figure 2 – supplement 2): given that the dynamics of long-term host:virus coevolution that exist in Rhinolophus bats are so different from the dynamics of susceptibility that are germane to questions of reverse zoonotic and intermediate/amplifying potential of other species – might it be wise to exclude Rhinolophus species from the analyses as they may require different forms of "signal" for prediction of susceptibility compared to the rest of mammals?

Reviewer #2 (Recommendations for the authors):

Pg 2 L11-12 – has anyone looked at the correlation between susceptibility in cell culture vs in vivo (for any virus)? Might be complex as often comparing across tissue types as well as species. Some support from https://doi.org/10.1371/journal.ppat.1004475 but not sure if there are other studies such as this looking directly at susceptibility?

Pg 3 – L23-30 – re the assumption that infection with SARS-CoV suggests susceptibility also to SARS-CoV-2 and vice versa – this seems reasonable, although may expect some instances of virus by species interactions meaning this is not the case.. Looking at the supp data it looks like in the 6 species tested with both SARS-1 and -2 they can be infected by both (ie 6/6) – is that correct? If so maybe alter the text to say this specifically, and offer some more general support for your approach with (eg their own recent paper in PNAS or https://onlinelibrary.wiley.com/doi/10.1111/tbed.14361)

Pg 4 L3-10 felt some more detail was needed here on ACE2 data to help the reader follow the approach

The authors use the described modelling approach to predict what species are susceptible to sarbecovirus infection, aggregated by taxonomic order (Figure 5, Figure Supplement 2). From the figure it is apparent that the observed data set contains primarily mammalian samples where as the predicted dataset contains a considerably higher proportion of avian samples. Given that the narrative around reverse zoonosis is largely focused on mammals, it would be helpful to have more of a discussion around the role of avian species both in these analyses and in the transmission of sarbecoviruses.

Data and scripts are available via a doi.

Reviewer #3 (Recommendations for the authors):

You write

"Second, since no model has been trained or validated using observed data on infection (the outcome of interest)"

Then later:

"Understanding the value of ACE2-based host range predictions for guiding surveillance therefore requires developing models based on the outcome of interest – susceptibility – and quantifying the accuracy of their predictions."

And later again:

"We treated these different sources of information hierarchically, considering the best available evidence for compatibility or incompatibility in each host species (natural infection > experimental infection > cell culture > heterologous ACE2 cell culture experiments)."

I'd recommend changing "infection" to susceptibility in the first-quoted passage. To me (maybe just me?) "infection" makes me think infection of a live animal, even though I know that cells in culture can be infected too.
