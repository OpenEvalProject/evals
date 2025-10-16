# Peer review - Round 1

Editors:
- Amy Wesolowski, https://ror.org/00za53h95 Johns Hopkins Bloomberg School of Public Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77634.sa0](https://doi.org/10.7554/eLife.77634.sa0)

The authors provide an analysis of how various factors (biological, epidemiological, and treatment) impact the establishment and spread of drug-resistant Plasmodium falciparum using a combination of transmission modeling and model emulation. This comprehensive approach to investigating the complex dynamics underlying drug resistance explicitly considers several factors, highlighting their roles in the increasingly important public health question relating to spread of drug-resistant Plasmodium falciparum.


---

# Peer review - Round 1

Editors:
- Amy Wesolowski, https://ror.org/00za53h95 Johns Hopkins Bloomberg School of Public Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77634.sa1](https://doi.org/10.7554/eLife.77634.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The influence of biological, epidemiological, and treatment factors on the establishment and spread of drug-resistant Plasmodium falciparum" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Bavesh Kana as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The primary essential revisions for the paper are outlined by the two reviewers, but focus on the clarifying and streamlining results (figures, results presented, naming conventions, etc.) as well as considering some additional aspects of resistance (sequential evolution of resistance, lack of monotherapies actually being used in practice, and recombination). While addressing all of these points as thoroughly as the authors have presented their current results may be outside of the scope of this paper, they should at least be addressed in some manner to help put the research in context and make the overall conclusions more relevant to other researchers and policy makers.

Reviewer #1 (Recommendations for the authors):

1. My main suggestion would be to re-think the visual representation of the results. I found Figure 3 to be particularly challenging to parse. I understand the motivation to have the generalized x-axis but it was very difficult for me to understand what was going on and look back and forth with the legend. I suggest thinking through again which results from Figure 3 are most critical to show (are both seasonal and non-seasonal panels needed, when they are so similar?). In addition, some results from Figure 3-supp 1 (low treatment access) were discussed in the text and I felt it would make more sense to promote those to the main text figure. Treatment rate is a very important variable to consider.

2. For Figure 4 (probability of establishment), is it possible to indicate confidence bounds? It seems there is still some stochasticity in the wiggliness of the curves and confidence bounds would help us interpret the differences between curves.

Reviewer #2 (Recommendations for the authors):

1. To increase the future impact of your work, consider a triple combination therapy drug profile.

2. I was surprised not to find explicit mention of other complicated agent-based models of malaria in paragraph beginning line 64. Presumably, some of the factors considered jointly in this study have been considered jointly before in these agent-based models. Does the EMOD malaria model have PK/PD components, for example? I would have imagined it does.

3. I wonder if Drug A and B could have more informative names that would aid interpretation of e.g., half-life results? I'm reminded of leaky versus all-or-nothing vaccines in the vaccine modelling literature. Perhaps partner-like and artemisinin-like would suffice.

4. For the drug B mono and combination therapies, did you include Cmax/EC50, adherence and degree of resistance against drug B altogether? Does that not cause a multicollinearity problem in the variance decomposition? It seems more natural to me to include either Cmax/EC50 alone, or adherence and degree of resistance against drug B together. Also, why is Cmax/EC50 referred to as capturing the killing rate (line 246)? This is a unitless ratio. It makes more sense to me to call this a killing effect, as is done in Table 1 and on line 257.

5. In the discussion, consider expanding upon the possible effects of recombination on the observed results (see Public review).

6. Consider adding some more details about the emulator to increase the methodological impact of your work. For example, can you explain why you choose an HGP? Did you try other methods? Can you quantify how efficient it is? You mention 3500 to 11,500 simulations were used to train the emulator; how many simulations would have been required without the emulator? I personally don't understand what the "two random datasets with a sample size of 100,000, with 150,000 bootstrap replicates" are (lines 718-719). Were these datasets used to generate the line plots (Figures 2b and 3 etc.)?

7. Could two genotypes have the same selection coefficient in the same setting but for different reasons? If so, might they have different probabilities of establishment, that would not be identifiable from the selection coefficient alone?
