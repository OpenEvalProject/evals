# Peer review - Round 1

Editors:
- Kim Orth, HHMI/University of Texas Southwestern Medical Center United States

Reviewers:
- James Slauch, University of Illinois United States
- Babak Momeni, Boston College United States

## Review text

DOI: [10.7554/eLife.40032.035](https://doi.org/10.7554/eLife.40032.035)

In the interests of transparency, eLife includes the editorial decision letter, peer reviews, and accompanying author responses.

[Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that all the issues have been addressed.]

Thank you for submitting your article "Listeria monocytogenes cell-to-cell spread in epithelia is heterogeneous and dominated by rare pioneer bacteria" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: James Slauch (Reviewer #2); Babak Momeni (Reviewer #3). Reviewer #1 remains anonymous.

The Reviewing Editor has highlighted the concerns that require revision and/or responses, and we have included the separate reviews below for your consideration. If you have any questions, please do not hesitate to contact us.

Overall, this submission was well received by all three reviewers. The reviewers highlight that your work provides important insight into the infection process. All three reviewers feel that more explanation is needed to more clearly understand not only your experiments but also the conclusions that are drawn from them. We highly recommend that you address these issues brought up by all the reviewers when submitting your revised manuscript. This will allow the readers to fully understand and appreciate your scientific study on the concept of rare "pioneer" bacteria that are important for spread during an infection, in this case for Listeria.

Thank you for taking part in this form of peer review. We look forward to your revised manuscript.

Separate reviews (please respond to each point):

Reviewer #1:

I don't have any major concerns.

Minor Comments:

This is a very nice manuscript that details an interesting phenomenon that is likely to have impact on a number of both intracellular and extracellular pathogens. I only have a few minor comments.

1) The authors should note that the idea of a pioneer leading a charge that ends up in a different tissue site is a variation of their model, that leads to bottlenecking. In Listeria, this spreading of a few founder bacteria from the intestine into deeper tissue sites was first shown by Waldor and coworkers (Zhang (PMID: 28559314).

2) Figure 3D is really the heart of the paper and shows that the simulations have predictive value. Unfortunately, the measurement parameters of circularity have to be defined better within the manuscript for the nonmathematicians because this turns out to be the single most important measurement parameter in the manuscript. The concept is intuitive, but better definitions within the body of the results are necessary to explain what deviation from circularity means.

3) Subsection “Simulations predict that heterogeneous spread increases the chance of a persistent Listeria monocytogenes infection in the intestinal epithelium”: I don't like the term death to the animal, since during growth in tissue, death may occur at much lower loads of bacteria than what the authors predict for death. Uncontrolled tissue growth is more appropriate. Their definition of death is a blackening out of the movie images.

4) Figure 5D is quite important, but there is no definition of what the colors mean. I think that Red: Bacterial clearance; Green: host animal death; Blue: stable steady state, with blue stable when the Df/Ds ratio is stable

Reviewer #2:

Ortega et al. combine modeling and experimentation to promote the concept that rare "pioneer" bacteria, which spread beyond the neighboring host cells, are important in the biology of Listeria. This is an interesting and very well written paper that provides important insight into the infection process. It builds on quantitative knowledge gained over many years to inform their models. I have only minor comments on presentation.

Although generally clear, throughout the paper and in the figure legends, the authors should strive to acknowledge which parameters are based on assumptions and/or simplifications, and which are based on experimental data.

Minor Comments:

1) Figure 1C. Y axis. Average fluorescence intensity of what?

2) Subsection “Allowing simulated bacteria to interconvert between pioneer and non-pioneer behavior recapitulates the non-circular phenotype of experimental foci” and Figure 3D. As stated, the circularity of the simulations is dependent on time, but it is not clear how this time relates to the experimental results being used as the benchmark. Please comment.

3) Figure 5D. You need to label the lines. After I stared at it a little while, I realized that the "outcomes" colors are indicated under 5C, but it was not immediately obvious.

4) Subsection “Allowing simulated bacteria to interconvert between pioneer and non-pioneer behavior recapitulates the non-circular phenotype of experimental foci” and Figure 5C. You carefully discuss the fact that clearance versus death is dependent on the rate of host cell extrusion, but it is not clear what times you used for extrusion relative to replication, for example. Minutes, hours, days…?

5) I also wonder if you considered having extrusion dependent on the number of bacteria in the host cell instead of time.

6) Some people might read primarily the discussion. Redefine or just spell out "MSD" in paragraph five of the Discussion section.

Additional data files and statistical comments:

Seems more than thorough.

Reviewer #3:

The authors use modeling to infer the mechanism of cell-to-cell spread of L. monocytogenes in epithelial cells. They start by observing that despite expecting each infection to be clonal, the spread appears anisotropic. They then create simple models of random walk (continuum and agent-based) and note that their model predictions do not match experimental observations. Based on insights on known mechanisms of spread, they propose a different model in which a small fraction of progeny spread over longer distances, and examine whether such a model describes the observations properly.

The manuscript has a logical flow, is easy to follow, and has a nice combination of theoretical modeling and supporting experiments. It is generally well-written and contains useful and interesting information. I find the premise interesting and important, but I feel some of the results could benefit from additional explanation to clarify the rationale for some of the assumptions made in the model.

Main concerns:

1) One concern regards the construction of the model. The observed parameter that the authors have used to fit the parameters is "circularity", and their model they introduce two additional degrees of freedom (Dfast/Dslow and P), both of which affect circularity. When fitting the parameters of their model, they assume Dfast/Dslow = 100, and sweep over values of P (in Figure 3D) to find a P value for which their simulations match the experimental data. Since circularity is the only parameter they are using for fitting, it leaves the question open if with other values of these parameters the same outcome can be achieved (say, Dfast/Dslow = 10 and P = 1e-4). I suspect the authors have already examined this when constraining their model parameters, but I think it helps to explicitly mention their process of eliminating the alternative possibilities in their manuscript.

2) When examining the GRR mutant, the authors have mentioned that "This mutant… is less persistent than wild-type bacteria and it is therefore likely to enter protrusions at a lower frequency than wild-type bacteria and to form protrusions that are less straight". First, the authors should clarify what they mean by "less persistent", and why persistence matters.

Second, if I understand correctly, the reference they cite mentions that cell-to-cell spread is less efficient with GRR mutant and the trajectory of protrusions is less straight. I expected the authors to quantitatively assess the hypothesis that the spread of GRR mutant still follows their model (with different P and Dfast/Dslow parameters that they estimate). In my opinion, this is a missed opportunity in the current paper. The experiments are already done by the authors and there are some estimates of the difference between WT and GRR mutants in the reference they have cited. Thus, the only remaining part is making quantitative predictions based on the model about how the spread is expected to be and comparing those predictions with experimental data. If the results match, that would re-enforce the model, and if they don't, perhaps they can speculate what other factors might be involved.

3) In the last section of the Results: "Simulations predict that heterogeneous spread increases the chance of a persistent Listeria monocytogenes infection in the intestinal epithelium", in my opinion, there are aspects that need to be clarified. What is the significance of a stable steady state infection per infection site/villus? Based on the discussions in the paper, one can consider the overall infection as a metapopulation of several sites/villi. In this context, a steady-state infection would be important in the overall infection, not at each site/villus, since unstable sites/villi can still persist at the metapopulation level. This is because infections that spread too quickly are still primarily contained within that site (conceptually similar to coexistence with spatial refuge in a prey-predator ecological model) and the ones that are cleared can still infect other sites (dispersal-clearance balance, conceptually similar to mutation-selection balance in evolutionary theory). Without a more thorough investigation, it is not obvious to me why the special case of stable steady state would be the best strategy for maintaining an infection compared to these alternatives. I suggest de-emphasizing stable steady state infection at each site as the "evolutionarily preferred" solution for persistent infection.

Minor comments:

1) In determining the circularity, the authors mention that they use the smallest circle that contains all the points. How do you find this circle? Maybe I am overthinking it, but to me this is not trivial.

2) The choice of P = 0.01 is justified in Figure 3D, but it's not clear to me how the choice of Dfast/Dslow = 100 was made. Would you please elaborate?

3) Is the "effective" diffusion coefficient in Figure 5C the same as Dslow? I think it is and it helps to mention it explicitly.

4) I think it would have helped to include the spread for another microbe that does not have extracellular protrusions (no pioneer cells, as a point of reference), as a negative control. Would you observe a homogeneous plaque shape in these cases? If not, what are the parameters involved, and do they contribute to the heterogeneous spread observed for L. monocytogenes? I suggest this only as an optional addition, if such a system already exists.
