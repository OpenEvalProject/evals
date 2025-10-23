# Author response - Round 1

Authors:
- Marco A Díaz-Salinas ([ORCID: 0000-0003-2983-0123](https://orcid.org/0000-0003-2983-0123))
- Qi Li
- Monir Ejemel
- Leonid Yurkovetskiy
- Jeremy Luban ([ORCID: 0000-0001-5650-4054](https://orcid.org/0000-0001-5650-4054))
- Kuang Shen
- Yang Wang
- James B Munro ([ORCID: 0000-0001-7634-4633](https://orcid.org/0000-0001-7634-4633))

## Response text

DOI: [10.7554/eLife.75433.sa2](https://doi.org/10.7554/eLife.75433.sa2)

Essential revisions:

1) Please revise your manuscript to describe your model selection process more comprehensively and, most importantly, to include a stronger justification for your use of a two-state model.

We appreciate the importance of the Reviewers’ comment and agree that a discussion of model selection is appropriate. In brief, we used the Akaike information criterion (AIC) to compare maximized likelihoods across a range of models with varying numbers of state and topologies. The simplest model we considered was a two-state model, consisting of one non-zero-FRET state and a 0-FRET state, which accounts for fluorophore photobleaching. We find that addition of a second non-zero FRET state (three states in total) improves model fitness as evidenced by a decrease in the AIC value. Additional states and connections did not further decrease the AIC value for the SDTM D614 or D614G data sets. Therefore, we performed our analyses using a circular model with 3 FRET states in total (0.65, 0.35, and 0 FRET). This analysis is now described in the Materials and methods section (lines 507-516 of the revised document) and presented in Figure 3—supplement 1.

2) Please revise your manuscript to include a stronger justification for the incubation times and temperatures that were used to achieve equilibration/saturation of ligand binding.

The Reviewers raise an important point, which is often overlooked. Spike proteins (S trimers and isolated domains) have been used in multiple studies to characterize the interaction with ACE2 and antibodies. However, these studies have yielded divergent estimates of ligand affinity for the spike proteins, likely stemming from the different protein constructs and reaction conditions used. For the ligands studied here, estimates of KD range from 0.04-8 nM. Overall, we have sought to work in high excess of these KD values. The outlier is 2G12, which binds a glycan epitope with relatively low affinity (343 nM). Therefore, our studies were likely conducted under sub-saturating 2G12 binding. So, our results probably under-estimate the effects of 2G12 on S conformation and ACE2 binding. Regarding equilibration, the rates of dissociation have not been thoroughly reported for the ligands considered here. The available rates are in the range of 10-5 to 10-2 s-1. So, some of our measurements (which followed a 90-min incubation) may not have been conducted under fully equilibrated conditions. These caveats are now noted in the Materials and methods section on lines 479-488.

3) Please revise your manuscript to include a stronger justification for the relatively small number of smFRET trajectories recorded and analyzed in these studies. Related, please clarify the number of trajectories in Figure 3 and Figure 4-Supp 1, as requested b Reviewer #1.

Here again, we thank the reviewers for raising an important question that often goes overlooked in smFRET studies. To the best of our knowledge, there is no consensus on the minimum number of traces needed to justify a conclusion. In the present study we have chosen to determine the adequate number of traces by calculating the sample size necessary to obtain the desired statistical power for a given hypothesis. In this case, our hypothesis is that addition of the specified ligand shifts the occupancy in the RBD-up conformation. As seen in Author response image 1, for the magnitude of the change in RBD-up occupancy that we observed upon addition of ACE2 to SDTM, and the observed variance across the population of traces analyzed, a sample size of 140 traces yields a statistical power of >99%. This indicates that the observed change in the RBD-up occupancy upon addition of ACE2, and the associated p-value, are highly reliable. In the second example shown in Author response image 1, for the effect on RBD-up occupancy seen upon addition of mAb 4A8, which is a comparatively modest effect, our analysis of 294 traces yields a statistical power of approximately 90%. All data sets displayed in Author response image 1 achieve minimally 85% statistical power. Again, this indicates that our results and the associated p-values are highly reliable. We are therefore confident that the number of traces that we have analyzed is sufficient to justify the conclusions of our study. This is now noted in the Materials and methods section on lines 524-526.

Data for MAb362-IgG and MAb362-IgA overlap with REGN10987 and CR3022, respectively.

4) Please revise your manuscript to carefully and comprehensively address the error analysis concerns raised by Reviewer #1.

We appreciate the Reviewers raising this issue, and we fully acknowledge that the treatment of our smFRET data was insufficiently described in the initial submission. To address this concern, we have expanded the statistical analysis of the FRET state occupancy data, and thoroughly described our procedures in the Materials and methods, and in the legend to Figure 3. In brief, we have clarified the origins of the reported error bars. The errors bars in the FRET histogram bin counts reflect standard errors, which were determined from three technical replicates, as Reviewer 1 surmised, but which we had not stated clearly. In the previous submission, the error bars reported with the rate constants had reflected 95% confidence intervals generated by bootstrapping in Matlab. However, to simplify the interpretation of our data, in the revised submission the rate constant error bars now reflect standard errors determined across the three technical replicates. Although the recalculated error bars are indistinguishable from the error bars in the initial submission, the internally consistent procedure makes for a more logical description of our methods. For this reason, we appreciate the rigorous comments from the Reviewer 1. These procedures are now reported in the Materials and methods, in the subsection entitled “smFRET imaging and data analysis”.

Finally, in order to transparently display the breadth in the behavior of the smFRET traces that we have observed, we have now reported the FRET state occupancy data as violin plots from the total population of traces analyzed. This treatment enabled us to calculate mean, median, and quantiles in FRET-state occupancies across the experimental conditions considered. This recalculation in mean occupancies and standard errors reported in Tables 2 and 3 led to adjustments from the initial submission, but the qualitative conclusions still hold. This treatment also enabled us to calculate statistical significance measures (p-values) using ANOVAs. As Reviewer 1 correctly points out, some of the effects that we report are relatively modest in magnitude. We therefore felt it was important to report p-values in this way. This procedure is now described in the Materials and methods, lines 516-524.
