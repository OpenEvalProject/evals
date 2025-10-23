# Peer review - Round 1

Editors:
- Graham Coop, https://ror.org/05rrcem69 University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66697.sa0](https://doi.org/10.7554/eLife.66697.sa0)

This paper is an impressive look at an important problem: understanding the genetic underpinnings of evolution acting on a quantitative trait. The authors analytically study the response to an abrupt shift in phenotypic optimum, in terms of both phenotype and genetic basis (how various alleles/loci contribute to this response). The basic assumptions are classic, but the methods and findings are new (especially the finite population effects) and well supported by clear analytical approximations and extensive simulation checks. The main finding is that the relative contribution of large vs moderate effect alleles changes substantially and predictably over a long-time period after the shift, even though the phenotypic changes are already undetectable over this period.


---

# Peer review - Round 1

Editors:
- Graham Coop, https://ror.org/05rrcem69 University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66697.sa1](https://doi.org/10.7554/eLife.66697.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Polygenic adaptation after a sudden change in environment" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Peter L Ralph (Reviewer #1); Guillaume Martin (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers and I appreciated the impressive steps made in the analysis of this important model. The paper is a difficult read, but that mostly reflects the challenging area and the broad scope of the results. Most of our comments focus on how the clarity could be improved.

1) The reviewers have numerous suggestions on improving the clarity of the model. In particular, I think we all struggled with the parallel tracks throughout the paper.

There is enough new intuition from the Lande-style results that there's an argument for putting more of the technical results about the skewed distribution into the appendix. This would improve the readability of the paper, and I think would likely significantly broaden what the average eLife reader could take away from the paper. More technical readers will likely read the appendix anyway if it is clearly signposted from the main text. That said, I'm not going to force this move on you, and many of the suggested improvements to the manuscript could be made without this big change

2) In our post-review discussion one point that came through clearly is that we all struggled to keep track of which of the simulation frameworks was being used at various points in the paper. Please make sure this is clearer throughout the manuscript.

I apologize for the somewhat slow turn around I think everyone (especially myself) is currently struggling to get things done.

Finally, the Coop lab discussed the preprint paper as part of our journal club, everyone liked it and got a lot out of the paper. We needed some more background on why large effect mutations lead to a skewed distribution under selection. We also felt like the results about skew changing the rate of approach to the optimum could be explained more. One of the lab members came up with the following argument:

"When the phenotypic mean is far below the optimum (1-D^2/V_S < 0), the phenotypic distribution sits on a convex part of the Gaussian fitness function. There, the positive skew of the phenotypic distribution, by shifting variance away from the left tail (where it is inefficiently selected) towards the right tail (where it is efficiently selected), increases the average efficiency of selection and therefore the rate at which the mean moves towards the optimum.

The opposite is true when the phenotypic mean is nearer the optimum though still not very close (1 >> 1-D^2/V_S > 0), because then the phenotypic distribution sits on a concave part of the fitness function.

Finally, when the phenotypic mean is just below the optimum, so that the phenotypic distribution straddles the optimum, positive skew shifts variance away from the left tail (where it is relatively efficiently selected in the "correct" direction) towards the right tail (where it is relatively efficiently selected in the "incorrect" direction), and thus retards selection on the mean."

I am not sure if this argument is fully correct/useful, but I wanted to send it along in case it helped. I do think a little more intuition on this point would be useful.

Reviewer #2 (Recommendations for the authors):

This paper tackles an old but definitely unsolved issue (at least in my opinion, and this opinion is supported by the review of the literature in the intro).

One main limit in existing treatments of this model of gaussian fitness landscape has been either to tackle non equilibrium, or finite populations. The approach here proposes a methodology to fill this gap on both accounts, so I think it is a new and important contribution to theoretical quantitative genetics.

As a theoretician, I appreciated the appendix, which could be made a bit clearer there and then but is overall flowing and easy to follow, especially when it comes to understanding where we are going. I also appreciated the many illustrative figures in the appendix to check various steps in the approximations by simulations, and as a way to explore a wide parameter range. Overall, the accuracy of the approximations in the various figures is very good. These approximations are not rigorously derived as a limit for some parameter being small etc., some approximations are plugged into others (eg the linear or non linear lande and non lande cases), but we get an intuition of the idea behind the approx., and we get quite many simulations to back it up. Of course a rigorous treatment or a dedicated simulation paper might help identify the exact parameter range of validity, but these would be articles of their own. As such the paper is clearly dense enough!

I suggest that the authors clarify/emphasize two main points for the reader in main text

– First that the phenotypic dynamics are overall correctly approximated by the lande model in the parameter range that was analysed. Indeed, the deviations are much smaller than the main trend in Figure 2 for ex. For the main part of observable phenotypic adaptation (ie until t1). What is lande or non lande here is not this phenotypic mean trajectory but rather its consequences in the longer term dynamics (if I got this right). That should be emphasized and maybe cases where the lande model is not accurate to begin with should be shown too in the simulations.

– Second, therefore, the main contribution of the paper is on (i) obtaining the lande equation without the lande assumptions, (maybe, my knowledge of the vast literature is not large enough to knpw if the various derivations differ that much) and (ii) deriving the longer term dynamics after t1 and especially the genetic basis resuts (relative contribution of alleles as a function of their effect size). It would be nice to pull that string a bit further and illustrate a GWAS or QTL prediction between a pop staying in the original state and a pop having evolved in the new environment, either before t1, or after t1. This is to me the main impact that these results will have and it is somewhat not pushed to its final biological conclusion. Or I missed it and then it must be better put forward.

The paper is very long, both main text and the appendix. I found both flowing though, and that we were guided well into this elaborate modelling exercise. I don't know if this length will be a problematic criterion, that is for the editor to judge.

It was not always easy to know which type of simulations were used for each figure and check. The top check being the true individual based simulations of course. Maybe a table (sup info) dedicated to that would help clarify this without having to go back to methods to know which method is what.

In the intro maybe a link to other models mixing diffusion equation and deterministic pheno models would be nice, I am not sure I saw a reference to the stochastic house of cards approx. and its 'offspring' or to the zhang and hill methods I think.
