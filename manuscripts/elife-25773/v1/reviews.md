# Peer review - Round 1

Editors:
- Michael Doebeli, University of British Columbia , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25773.016](https://doi.org/10.7554/eLife.25773.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Eco-evolutionary dynamics in quorum-sensing microbial populations can induce heterogeneous production of autoinducers" for consideration by eLife. Your article has been favorably evaluated by Gisela Storz (Senior Editor) and three reviewers, one of whom, is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper presents a theoretical model for the emergence of phenotypic heterogeneity in autoinducer production, which is essential for quorum sensing in bacteria. The paper shows that a feedback between the total concentration of autoinducers and individual costly production of autoinducers is sufficient to generate heterogeneity in individual production.

Essential revisions:

The reviewers found the paper very interesting and well written. However, they raised a number of concerns that preclude publication of the paper in its present form.

Notably, some comments point to a lack of integration of the theoretical results with empirical reality. On the one hand, the paper should make more specific suggestions about how the proposed theory can be tested. On the other hand, and more importantly, the authors should consider incorporating more biological realism into their modelling. Reviewer 3 makes a number of useful suggestions in that regard. For example, this reviewer suggests incorporating heterogeneity in signal perception, an issue that was also commented on by reviewers 1 and 2. Further, it is unclear how decay of the signal concentration in the environment would affect the results. You will see that the reviewers have made a number of other suggestions about how to improve the paper.

If you find that you are able to address the concerns raised in the reviewer comments we would welcome a resubmission of your article. In the revision, please try to address all of the reviewers' comments in a constructive way. In particular, it would be good if you could extend the theoretical analysis to cover the salient comments.

Reviewer #1:

This is an interesting paper showing how the emergence of phenotypic heterogeneity in autoinducer production can, in principle, be understood as an emergent collective behaviour of quorum sensing in microbial ecosystems.

The model presented is simple and elegant, and results are supported by both numerical simulations and analytical derivations. The main result of long transients at heterogeneous states in the stochastic model is surprising, and the mean-field approximation serves the purpose of explaining this result very well.

In principle, the analytical work generates novel and testable predictions for autoinducer heterogeneity in quorum sensing (although the paper might benefit from being more specific in this regard).

1) The phenotypic response defined by the response function R is assumed to be deterministic (as e.g. seen by the Delta function appearing in the autoinducer equation (Acar et al., 2008)). I think it is important to investigate what happens if the response is instead probabilistic, i.e., when the offspring phenotype is drawn probabilistically from some distribution with mean R(<p>) and positive variance.

2) I don't agree with the paper's distinction between "ecological" and "evolutionary" dynamics. The authors call the feedback mechanism for autoinducer production "ecological", and they call differences in growth rates "evolutionary". However, there are no genetic differences between individuals, and hence no evolutionary dynamics occur. Instead, individuals simply have different birth rates, which is a purely ecological difference. Thus, both processes, fitness difference and global feedback, are clearly ecological in this model, and any claim that the former is "evolutionary" is misleading. The coupling is not between "ecological" and "evolutionary" dynamics, but between global production and individual birth rates.

Reviewer #2:

This manuscript shows how phenotypic heterogeneity in autoinducer (AI) production may arise in monostable autoregulation from the interplay between sensing and responding to the environment and fitness differences between producer and non-producer phenotypes. I really enjoyed the manuscript, and feel that this is an important contribution to the study of collective behavior in microbes, mainly because it provides an alternative mechanism to explain AI production phenotypic heterogeneity using "bistable threshold models". The paper is well-written and technically very rigorous. In my view, it would be acceptable for publication in eLife after some minor points are clarified.

According to this model, phenotypic heterogeneity relies on (i) fitness differences between producers and non-producers linked to the metabolic cost associated with AI production, and (ii) AI production, p, is more likely to be inherited from the parental cell than obtained from the mean level of production, <p>, in the environment. I am wondering if, due to this fitness difference between producers and nonproducers the authors could devise any population level experimental procedure (in addition to the single cell experiments briefly discussed in the last paragraph of the Discussion) to check the existence of the proposed feedback. The authors envision this possibility, but I think that the paper would greatly improve by establishing tighter connections between theoretical results and their possible empirical confirmation. In my opinion, this would be an important point to reach the broad readership of eLife, although the theoretical results are of enough significance by their own.

I have some doubts about the probabilistic mechanism by which newborn cells adopt. In my opinion, this is the most important ingredient of the model, because it allows for phenotypic heterogeneity, and I think that it would be good to discuss whether there is empirical support for such election (is the production level a trait maintained during the whole life cycle of the cell?) or whether that is a choice of the authors. In the latter case, it could be interesting to discuss other possible mechanisms and maybe outline the robustness of the results presented here against these alternatives.

I think that the importance of the paper could be highlighted, especially for non-specialist readers, if the Introduction is slightly reorganized. As it is now, one may understand that there are experimental proofs of both bistable and monostable autoinducer synthesis regulation, and that the authors provide a mechanism that could explain phenotypic heterogeneity in the latter case. However, if I understood the Discussion correctly (second paragraph), bistable autoregulation has not been experimentally verified, but there are not empirical studies showing monostable autoregulation either. I think this point should appear earlier in the Introduction, accompanied by more references to existent models that utilize a bistable autoregulation (1,2). My feeling is that if there is not experimental verification of monostable regulation in AI synthesis, then this paper opens a much broader and deeper question because it not only provides a new mechanism by which phenotypic heterogeneity can emerge, but also suggests that AI synthesis regulation could be monostable. In either case, I think that this should be clarified.

1) Goryachev AB, Toh DJ, Wee KB, Lee T, Zhang HB, et al. (2005) Transition to Quorum Sensing in an Agrobacterium Population: A Stochastic Model. PLOS Computational Biology 1(4): e37. doi: 10.1371/journal.pcbi.0010037

2) Dockery, Jack D., and James P. Keener. "A mathematical model for quorum sensing in Pseudomonas aeruginosa." Bulletin of mathematical biology 63.1 (2001): 95.

Reviewer #3:

The present study describes theoretical model to provide a possible explanation for the occurrence of phenotypic heterogeneity in quorum sensing. In general phenotypic heterogeneity is an interesting topic which spans from antibiotics persistence to bacterial competence. Resent study has shown that bacteria exhibit reversible heterogeneity in QS response even in the presence of saturating concentration of QS signal, which indicate that bacteria maintain a stochastic homogenous population as a bet-hedging strategy to counter fluctuating environmental conditions.

1) The model has been thought in the lines of heterogeneous expression of QS synthase gene by epigenetic mechanism, however in QS, sensor plays an important role in the perception and auto regulation of the QS synthase as well as expression of other QS controlled genes. In this model however, the heterogeneity in terms of QS signal perception is not considered which could play an important role in the process.

2) The model is based on the assumption that there appears to be little change in the extracellular signal concentration once it is produced or the intracellular conc. It has now been shown that signal degradation also takes place in some QS system such as in Pseudomonas syringae, in which bacteria secrete QS degrading enzymes (some are secreted and some are intracellular), which can also influence the heterogeneity in the population. However, it appears that in this model it could have been also considered while simulating the fluctuation along with the assumption of non-producers grows faster.

3) It has been shown that in certain environmental condition, the QS nonproducers has a growth advantage as they take benefit of the social task performed by the responders and also save on signal production cost. However, it has also has been shown in case of Pseudomonas that QS- strains has a big disadvantage under certain environmental condition where QS controlled "private goods" are required (Science. 2012 Oct 12;338(6104):264-6.). How will this affect the present model?

4) How the stability of auto inducers in the system will influence the cellular response to fluctuating environment and phase transition to homogeneous response?

5) A factor that could play a role in the QS heterogeneity response is the relative affinity of different QS signal with the receptor. In case the affinity is high, the local concentration of QS signal could be maintained for a prolong period and can affect the distribution. In this model, it is better to include the signal perception component also, as ultimately even for the stochastic expression of signal synthase, the signal perception and henceforth regulation of gene expression also contributes to the overall QS process.

6) What happens when competition experiments are performed with signal blind and signal sensing mutants in this model? Does fluctuating the ratio of these variants also influence the heterogeneous distribution?
