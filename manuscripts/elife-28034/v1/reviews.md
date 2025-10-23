# Peer review - Round 1

Editors:
- Patricia J Wittkopp, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.28034.020](https://doi.org/10.7554/eLife.28034.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Principles of cellular resource allocation revealed by condition-dependent proteome profiling" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript describes a crucial relationship between the ribosome population and growth rate, controlled by nutrient conditions. It seeks, in a model eukaryote, to extend findings made in E. coli and long-standing in the literature, that the rRNA content of a cell is linearly dependent upon growth rate. However, the manuscript seeks to further extend these findings in yeast, by identifying the existence of 'reserve' ribosomal capacity, which the authors argue is used in cases of rapid nutrient upshift. The manuscript discoveries in yeast confirm similar findings made in E. coli, that reserve ribosome capacity exists in E. coli grown at slow growth rates. We are all enthusiastic about the potential of this work to be suitable for eLife, but also have some comments/questions that need to be addressed before moving forward.

Essential revisions:

1) The discovery that 8% of the proteome encodes excess ribosomal proteins, not actively employed in translation, depends on a quantitative scaling, and an interpretation of the author's central growth relationship, namely that;

Growth rate = Γ (translation elongation rate) * [ribosome active]

And by extension, since ribosome(sum) = ribosome(active) + ribosome(inactive);

Ribosome(sum) = mu/γ + ribosome(inactive)

The authors make the assumption that the r0 inactive ribosome fraction is invariant, then the rate of translation is also invariant. However, r0 and the rate of translation are both variables in the central equation governing these experiments, thus unless it is certain that the elongation rate is invariant with changes in growth rate, the assumptions made in fact break down.

Of direct relevance to this point, there is good evidence in the literature that crucially, γ, the translation elongation rate is proportional to growth rate, a relationship governed apparently by a linear function. This discovery is reported in at least two publications, PMID: 372763 and PMID: 1089627, not cited in the paper, but whose findings impact directly on one of the central assumptions of the paper. Indeed, using the discovery that the translation elongation rate scales with growth rate, Bonven and Gullen reach the following conclusion, at odds with the conclusions reached in this manuscript;

Bonven and Gullen, Mol Gen Genet. 1979;170:225-30 "When our Cp estimations are taken into account (Table 1) this pattern can be interpreted to mean that the number of active ribosomes decreases drastically with decreasing growth rate, resulting in an overproduction of ribosomes at low growth rates. The vast amount of idled ribosomes observed might be seen throughout the cell cycle or could be restricted to discrete steps within the cell cycle." [note the Cp that Bonven and Gullov refer to is the peptide chain elongation rate)

Bonven and Gullen adopt the same analytic approach to defining the relationship between ribosome content and growth rate, and also examine the effect of nutrient upshifts on this relationship.

Further, in this manuscript under review, the authors also acknowledge that their monosome estimates, used in part to judge the proportion of inactive ribosomes, may be subject to error, since as they state, "In contrast, monosomes are thought to contain primarily inactive ribosomes, although some of these may represent low-translating genes (Aspden et al., 2014; Heyer and Moore, 2016; Kelen et al., 2009)". This is a material observation when the fraction on idling ribosomes they estimate is relatively small, and subject to experimental measurement variation.

In summary, there are important factors not taken into account in the authors' analysis which may materially change the conclusions they reach. Since these factors include assumptions made directly at odds with other literature reports, addressing these in full is critical to make the manuscript suitable for publication.

2) The reported specific growth rate goes to above 0.6 h-1. I have never seen so high values for S. cerevisiae before, and I doubt these values can be true. Not because this is important for the story as it will probably be a linear mistake in the estimation of this value, and hence all the values reported are too high. The authors refer to their previous paper for calculation of this, but that does not help me much when checking. So this should be addressed and the manuscript should be revised. The problem will be that if these numbers are not corrected there will be a lot of confusion in referring to data from this paper and comparing the data here with data from other studies.

3) The fraction of mRNA transcripts that code for ribosomal proteins as a function of cell growth rate showed the similar quantitative scaling as at the ribosomal fraction at the of the proteome level. Considering a simple steady-state scenario where protein level corresponds to the mRNA level multiplied by the ratio of translation to mRNA degradation, this observation suggest that this ratio is similar for all protein. It would be insightful to address this point and explain whether it is reasonable.

4) In using area under the curve of polysome profiling, it is important to mention that the area is proportional for both the ribosome and the mRNA that it is bound to. This might lead to overestimation of the "nonactive" ribosome. As this is an important experimental validation to the inferred active ribosome fraction, it should be taken into account at least as a margin of error.

5) The authors suggest that cells entering stationary phase transiently decrease their predicted fraction of inactive ribosomes (r0). The authors should explain why the non-linear relations in Figure 4 is the result of changing r0 and not the translation rate.

6) When forcing cells to produce more proteins, the authors examine the change of growth rate for same burden but different media conditions. This relation gives a slope which is similar. One can also consider the change in growth for the same condition but different burdens. In a previous figure the author showed that different strains that grow on xylose (one way to manipulate growth) and different conditions (second way to manipulate growth) falls on the same curve. In that case the change of growth rate has a different slope for different conditions which suggest that the translation rate changes. In other words, the relation between growth rate and r is not unique and does depends on the way growth rate is changed. The authors should address this point. This is also relevant to the results presented in Figure 6. The parameters could be inferred from the slopes within burden and not within condition.

7) The logic behind the relation between growth rate and r (the amount of protein that is produced during doubling is related to the translation rate multiply by the active ribosomes) seems to hold also the double mutant data in Figure 2. It seems that slope is smaller than the condition dependent case but it is not zero. What does this smaller slope mean? What does the bigger interaction mean? This is important in the context of using this observation to support the suggestion that growth rate feedback is less dominant as suggested in Figure 7.
