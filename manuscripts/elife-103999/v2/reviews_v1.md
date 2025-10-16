# Peer review - Round 1

Editors:
- Ariel Amir, https://ror.org/0316ej306 Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.103999.sa0](https://doi.org/10.7554/eLife.103999.sa0)

This valuable paper explores the question of when complex ecosystems will be dominated by a few species. The authors present compelling, general arguments for a phase transition from what they call a dominance phase (few species dominate biomass) to an egalitarian phase (no species dominates the biomass).


---

# Peer review - Round 1

Editors:
- Ariel Amir, https://ror.org/0316ej306 Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.103999.sa1](https://doi.org/10.7554/eLife.103999.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Dominance to egalitarian transition in diverse communities" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Sergio Rasmann as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

As you can see below, while both reviewers appreciated the work and its contribution to the field, they raise several technical comments as well as ones pertaining to the presentation. The work will be strengthened if these are addressed in a revision.

Reviewer #1 (Recommendations for the authors):

In this manuscript, the authors investigate the effects of environmental noise on the dynamics of species in hyper-diverse communities. They assume that the community is "time-averaged neutral", namely follows a neutral model (inter- and intra-species interactions are the same), but subject to different and statistically-independent environmental noises. They calculate the species abundance distribution (SAD) and find that the highly-abundant (dominant) species consist of either a finite fraction of the species, or only a small subset of species (growing sub-linearly with the total number of species). The results are compared with SADs from field data.

The manuscript makes two additional contributions:

(1) The discussion leading to these results takes the authors to recent popular concepts in the field such as "diffusive trapping" and "stickiness". In this context, they point out a problem with a recent paper that has received much attention.

(2) They incorporate demographic noise, which I personally find to be the most original part of the work. Comparing the SADs with data, they argue that this term is important even in situations where one would expect a large number of individuals of each species.

The manuscript makes important contributions that merit publication in eLife, is well-structured and overall well-written. However, I found that there are issues in its present form that could be improved. This includes certain aspects of the presentation, and the comparison with other phenomena, in particular abundance fluctuations solely due to the interactions between species, to which the authors dedicate much of the Discussion section.

My particular comments are as follows:

1. Regarding the presentation. I felt that Sec. IIIC that applies the theory to data, is written in a confusing way. It says: "Figure 3 shows that the formula we presented … Equation (4) … describes the species abundance distribution for the gut microbiome quite well." But what was actually done with the data is not clear. I assume that Equation. (4) was fit to the data. But then the discussion goes on to compare with the result with demographic noise, which is given only later in the text (Equation. (6)). All this, without clearly pointing out which panel in Figure 3 is compared with which expression, and what parameters are being fit. Also, it would be helpful to include a table with the values of all parameter values obtained by the fit.

2. In this context, it should be mentioned that the ability to fit the SADs to the expressions is certainly an important first step, but it is not a strongly selective criterion between theories. It is well-known that many theories can fit the same SADs. I feel that this point should at least be mentioned in the text (perhaps in the Discussion).

3. A large part of the Discussion is dedicated to comparison of the model in question with chaotic dynamics due to the interactions between the species. There are several issues with this Discussion:

(a) In line 217, right below Equation. (6), the authors make a distinction between αij\begin{document}$\alpha_{ij}$\end{document} that are "O(1) in the strong coupling scenario, and O(1/S) in the weak coupling scenario". This distinction is unclear and seems arbitrary. First of all, it is not clear what is meant by these scalings; one has to explain how the distribution of the values P(αij\begin{document}$\alpha_{ij}$\end{document}) changes with S, and at least distinguish between the changes to the mean and the standard deviation of the distribution. Secondly, these two scalings (whatever moments they refer to) seem arbitrary; the transition to chaos happens when the distribution width std(α)∼1/S1/2\begin{document}$\text{std}(\alpha)\sim1/S^{1/2}$\end{document} which is neither of the above mentioned. Finally, these terms are not used in a consistent way, and the term "high niche overlap" is used later (referring to the strong coupling, perhaps?)

(b) Line 219 says that "weakly interacting species" lead to a truncated Gaussian distribution. The truncated Gaussian is only obtained at a fixed point phase (and only for interaction distributions that have a finite variance). In the chaotic phase, for any scaling which allows for chaos, wide distributions are obtained.

(c) Regarding sentence starting on line 220: "Remarkably, even in the strongly interacting case, … , each species can be treated separately …". This has been shown numerically to give reasonable results, but I'm not sure that it is known to be an exact dynamical description in the "strong interacting case" as the authors define it.

(d) Line 224: "linear growth rate is weak and negative." This is true for any dynamics that yield chaos, as long as the fluctuation of the interaction sum-term in Equation. (6), are comparable in size to the other terms in the parenthesis in that equation.

(e) Line 243: "After all, it is well known that distinguishing between high-dimensional chaos and mere noise is virtually impossible." While this is true for standard chaos, it is not the case here, exactly because of the phenomena relating to the "heteroclinic" structure of the equations, that leads to phenomena such as "stickiness" that the authors refer to earlier. Some fingerprints are: (1) the internal timescale of the chaotic dynamics that need not at all be related to the timescales of environmental driving, and may be large for small migration. (2) SADs of chaotic dynamics, as a result of the previous point. (3) Changing the number of species one might cross the transition to chaos, and either see stable equilibria or fluctuations, in contrast with changes due to environmental changes.

4. Finally, let me go back and say that I liked the inclusion of demographic noise in the model, and it is interesting that it plays a role in some of the data sets, even when population sizes would naively appear to be quite large (well above tens of individuals, where effects of demographic noise are usually important). If possible, I would have liked to see some discussion of this point. When is demographic noise expected to matter in this model, and what does it mean for the communities in question?

Reviewer #2 (Recommendations for the authors):

In their paper "Dominance to egalitarian transition in diverse communities", Kessler and Shnerb explore the question of if/when diverse ecosystems will be in a dominance phase (few species dominate biomass) or an egalitarian phase (no species dominates the biomass). To do this, the authors build on their previous work exploring time-averaged neutral models. The major technical advance of the work is to carefully use the Stratonovich formalism to show that, even though on average the growth rate is zero, given noise one will get an extra fluctuation-dependent contribution to the growth rate. This careful treatment shows that in this class of models, there exists a phase transition between these phases depending on noise and immigration rates.

The technical calculations are straight forward and seem to correct (these are mostly in the appendix). The major finding of the paper is a transition from what they call an egalitarian regime (\β>2 in Equation 4) to a dominant regime (\β <2) in the SAD distribution. The authors then fit various SAD curves for four experimental systems in Figure 3.

Overall, I found the paper quite compelling and thoughtful. I thought the problem was well motivated and the arguments were well made.

I do have some questions and comments that I think could make the paper a little stronger.

1. I would like much more discussion and motivation about the difference between σe~\begin{document}$\tilde{\sigma_e}$\end{document} (defined on top of page 3 below Equation 2) and the phenomenological parameter \σ_e in Equation 3. I am not sure what is exactly being assumed here and why the different notation?σe\begin{document}$$\displaystyle {\sigma_e}$$\end{document}

2. The authors use a very particular definition of egalitarian and dominance based on the number of species needed to explain half the biomass and how it scales with the size of the ecosystem S? As a statistical physicist, I am wondering if alternative definitions of these quantities such as the Inverse participation Ratio (IPR) also show similar scaling?

3. The authors make a cryptic statement about seeing only the tails of the ocean prokaryotic data. I would like much more discussion of this.

4. Also, given the very close values of the empirical fits of \β to the critical \β_c=2, it would be very useful to have some sense of error bars? For example, is \β=2.03 really over the transition? I would like some bootstrapped error bars for these fit parameters.

5. It would be nice to see some simulations for systems that are not strictly neutral and how well these can be approximated by the time-dependent neutral model. How large does the LV interaction matrix (A in Equation. 7) have to be before the arguments here break down for a simulated community?

I think my primary substantial concern is about error bars on the fits. This is quite important for drawing conclusions about the real communities.
