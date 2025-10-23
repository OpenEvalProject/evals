# Peer review - Round 1

Editors:
- Wenying Shou, Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52813.sa1](https://doi.org/10.7554/eLife.52813.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Hallinen et al. combine modeling and experiments to show that the density-dependent effects of antibiotic degradation by resistant cells and the pH influence on antibiotic survival can result in complex and counter-intuitive dynamics.

Decision letter after peer review:

Thank you for submitting your article "Delayed antibiotic exposure induces population collapse in enterococcal communities with drug-resistant subpopulations" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Wenying Shou as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Lingchong You (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

All three reviewers are positive about your work, although we feel that stating the limitations of your study is important. We are also confused about Figure 4C.

I attach modified full reviews to help with your revision.

Reviewer #1:

Hallinen et al. showed that the density-dependent effects of antibiotic degradation by resistant cells and the pH influence on antibiotic survival can result in complex and counter intuitive dynamics. Overall, I find the work quite interesting (although I am not intimately familiar with the field).

Major comments:

How mechanistic a model is a continuum. A phenomenological model was presented in this study. Have you ever tried constructing a more mechanistic model which would account for important aspects such as enzyme degradation of antibiotics and the pH effects? You can then use this model to explain reverse inoculum effect and possibly other experimental results. In the Discussion section, you delineated why a mechanistic model was not constructed, but I am not convinced, especially since you did not measure all parameters in your phenomenological model anyways. If you have tried to construct a more mechanistic model but it did not work, I think that it is still worth including such efforts in the Discussion section as well as speculations on why it might have failed. If you have not tried constructing a mechanistic model, you can cite examples where mechanistic modeling has been shown to be challenging (e.g. Hart et al., 2019).

Figure 4C middle panel: The red curve did not really go extinct, unlike the model prediction in Figure 3 or Figure 4A. Need to explain this.

Reviewer #2:

In this work, the authors investigate the population-level implications of two density-dependent effects that are known to influence bacterial resistance to β-lactam antibiotics (mediated by β-lactamase production). The first, the inoculum effect (IE), suggests that higher densities of resistant cells can decay more drug and therefore reduce its efficacy, while the second, the reverse inoculum effect (RIE), suggests that higher bacterial densities modulate the environment in ways that increase the sensitivity of populations to the drug. They probe this question using both mathematical modeling and bioreactor experiments with a mixed population of sensitive and resistant strains responding to ampicillin treatment. The authors observe both effects in their system and suggest that these competing effects can lead to complex dynamics, especially regions of bistability which implies that under different drug concentrations different initial densities will be favored. The authors attribute the reverse inoculum effect to pH effects, removing it with buffered media. Finally, they exploit this density dependence for populations where the inoculum effect is small (few resistant cells) by delaying treatment until the population density is high enough that the reverse inoculum effect dominates, and show that this delay can allow for population extinction where immediate treatment cannot.

I enjoyed reading the fascinating study, which underscores the rich population dynamics resulting from the interplay between bacterial populations and antibiotics. In particular, what's really interesting is how the composition of a mixture can dictate qualitatively opposite outcomes. The authors elegantly integrate analysis by a coarse-grained model and quantitative experiments throughout the study. The observed dynamics have implications for the effective design of antibiotic dosing when combating bacterial pathogens.

Reviewer #3:

The manuscript by Hallinen et al. is a well-crafted story involving an integration between computer-controlled bioreactors and simple mathematical models that reveals density-dependent feedback loops that address nonintuitive community-level behaviors upon antibiotic treatment. In particular it deals with β-lactam treatment of the pathogen E. faecalis when communities include a drug-resistant subpopulation that expresses a β-lactamase. The authors do a careful job of addressing the effects of treatment on resistant and sensitive populations as a function of density (either alone or in combination), and as a result are able to reveal some behaviors that highlight potentially important variables for driving resistant populations extinct.

A key aspect of their system is the reverse inoculum effect of β-lactams in which there is increased growth at lower densities, arising from changes in local pH. The authors do a good of breaking down the system into its component parts, demonstrating the rIE for their system and using this to motivate their mathematical model, which predicts a region of inverted bistability in which there is a big increase in drug efficacy in the high-density populations and a population collapse.

The work is well done and the paper is well written. I have a few comments/questions:

In Figure 4C (middle), the red population does undergo a large collapse, as stated in the paper in subsection “Small E. faecalis populations survive and large populations collapse when drug influx is slightly supercritical and resistant subpopulations are small”, but then it recovers. Why is this? Is there further resistance selection leading to other mutations (perhaps changes to the level of expression of the β-lactamase?)

One thing that pops out from their manuscript is that the conclusions are almost too clear once you know that there is both an inoculum effect and a reverse inoculum effect; nonetheless, it is good to see that the experiments can indeed achieve the predicted inverted bistability.

They take advantage of the inverted bistability to show that there are beneficial effects of delayed drug treatment. This is an interesting idea, but also very context dependent – you have to know a lot about drug concentration, relative populations of resistant/sensitive pools, initial density. It seems like this knowledge is important, but really hard to apply in a practical way. [This needs to be explicitly discussed in Discussion section.]

One thing the authors could do to address the point above is to do an experiment in a biofilm, where if they can see a similar inverted bistability, that would go a long way toward suggesting that this knowledge can be broadly useful. [Since this would be too substantial of a request, you could include this in the subsection “Future directions”.]
