# Peer review - Round 1

Editors:
- George H Perry, Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69032.sa1](https://doi.org/10.7554/eLife.69032.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This study considers how HIV evolutionary dynamics in a multiple drug-treated individual can give rise to the clinical patterns of the accrual of drug resistance mutations, including with understandings of the pharmacokinetics of the drugs in the body to help explain some of the patterns. The subject is of importance both clinically – for the optimal treatment choice for people living with HIV – and scientifically, due to the potential to predict and interpret evolutionary trajectories.

Decision letter after peer review:

Thank you for submitting your article "Understanding patterns of HIV multi-drug resistance through models of temporal and spatial drug heterogeneity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by George Perry as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Danna Gifford (Reviewer #1); Katherine Atkins (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers collectively found your submission to be "an interesting manuscript with provocative ideas," quoting one of the reviewers from our consultation session. I concur. Each of the three individual reviews is thoughtful and excellent; I'm appending these in their entirety to this email as I thought that you would want to see them to consider the detailed comments in full as you prepare a revision.

There was one overarching, consistent issue raised in slightly different forms by all reviewers: the under-realization of the ultimate conclusive potential of the paper – at least in its current attempt to answer a quantitative question with non-quantitative means – without more quantitative / formal statistical / modeling development. We offer you the choice of two options: (A) revise the current manuscript to become a shorter perspective/ hypothesis piece detailing the question and what would be needed to answer it (including addressing the reviewer concerns but leaving out a quantitative analysis), or (B) develop a revision with a more comprehensive quantitative/ modeling analysis along the lines suggested by the reviewers.

We're split (in a healthy, constructive way) in terms of slight preference for the two options. At least one reviewer leans towards option A. I myself probably lean towards option B. But we all agree that we would be supportive of your choice of either option so we happily defer to your decision on the ultimate form that you would like for your (promising!) manuscript.

Reviewer #1 (Recommendations for the authors):

1. I would like to see formal statistical analyses to support these statements:

• Drug resistance evolution occurs at a surprisingly constant rate (Figure 2A).

How has this been assessed? I would like to see a quantitative assessment of this. The figure title also says "…after the first few years of treatment". What's few here, 2, 4, 10? The rate does not appear visually constant to me over the 10 year span, especially for PI and NRTI.

• While some patients failed without any detectable drug resistance (likely due to non-adherence), viral populations in most patients harbored one, two, three or more resistance mutations.

It does look like the 0 class represents a larger proportion of the area in Figure 2B, but is it a significantly larger proportion?

• The singly-resistant viral populations almost all carry a 3TC mutation, suggesting that resistance to 3TC overwhelmingly occurs before resistance to either the other NRTI or the PI.

I'm not sure that all things having a 3TC mutation is a sufficient reason to say that mutation occurred first (though it is necessary). A different mutation may have occurred first, and then been subsequently outcompeted through clonal interference.

2. I would also please request any revised versions include line numbering to assist in preparing the reviewer's report.

Reviewer #2 (Recommendations for the authors):

The manuscript by Feder and colleagues investigates multi-drug resistance in HIV. By analyzing previously published data, they argue that (1) resistance evolves at a constant rate following a transient period of adaptation, (2) resistance evolves via sequences of single mutations, and (3) the order of mutations is largely predictable. The authors argue that these trends cannot be explained by differences in mutation rate and target size, are sometimes at odds with known properties of the corresponding mono-therapies or known properties (e.g. fitness costs) of the known mutants, and are surprising given that the conceptual basis for combination therapies suggests that partially resistant variants should not expand in the population (full 3-drug resistance is required). The authors argue that spatial or temporal heterogeneity in drug concentration could explain these trends.

The paper addresses an important and difficult problem, and it synthesizes a great deal of work from both the clinic and the modeling worlds. The authors make an admirable effort to re-evaluate numerous data sets from a new perspective, and their observations (1-3, above) are important and (in my understanding) under-appreciated findings with potentially important ramifications for understanding how resistance evolves in HIV.

My primary criticism of the paper, as presented, is that the empirical results (1-3) are relatively de-emphasized, and the focus (at least in title and abstract) seems to be on spatial and temporal heterogeneity as an explanation for these results. And while I do find the author's arguments to be plausible – and they nicely outline the qualitative evolutionary features that could arise from spatial and temporal heterogeneity, in part by summarizing previous work from multiple groups – I believe a more quantitative comparison between models and the data would substantially strengthen their conclusions. The paper presents interesting hypotheses and sound qualitative arguments-and this would be ideal for a perspective paper, for example. On the other hand, I think a more detailed analysis of the models would be required to convincingly argue that these heterogeneities are likely, rather than just plausible, explanations for their observations, and to more rigorously determine how features of the heterogeneity lead to particular features of the evolution.

With that said, I recognize that modeling these real-life processes is exceedingly difficult and that the empirical work alone is a nice contribution, and I'm not suggesting that a detailed, realistic model is required. But if the authors prefer to keep the focus on heterogeneities as a likely explanation, I would suggest going in one of two directions (both of which are in line with their expertise and strengths in modeling). One option is to develop a parameterized model based on known properties of the drugs in question (perhaps focusing on just one of the most detailed clinical studies), known mutations rates, etc, and to quantitatively assess the level of heterogeneity needed to (approximately) capture the measured dynamics. It would be interesting to see whether those bounds are consistent with known properties-half life, drug distribution-of the individual drugs and whether, for example, temporal or spatial heterogeneity is the more likely explanation.

Alternatively, I might suggest focusing on a generic toy model-similar to what was likely used to generate the results in Figure 4c – and try to determine qualitative features required for particular features to emerge. In some sense, this approach would be in between what is currently presented (a qualitative model with no equations) and a detailed quantitative model (which may well be impossible given the uncertainties in various parameters). Yet it could provide richer insight into how certain evolutionary outcomes depend on features of the model. In either case, the authors could use these models to make a stronger case for precisely how spatial and temporal heterogeneity (or perhaps a restricted class of such heterogeneity) could lead to the observed phenomena. In particular, it would be interesting to determine the conditions under which the probability of acquiring a mutation rises linearly, or conditions that lead to particular drug ordering (given some set of predefined properties of the mono-therapies themselves). This analysis may substantially limit the structure of the models and would, in my view, enrich the paper a great deal.

I have a few other comments (some naïve) for the authors to consider.

Given that the observed evolutionary dynamics are sometimes unexpected given what's known about the single drug characteristics, what role might interactions between the drugs play? As the authors know, drug interactions have been shown to modulate resistance evolution in other microbial systems (e.g. bacteria). What, if anything, is known about the impacts of drug interactions in HIV? Could this provide an alternative explanation, even in the absence of spatial or temporal heterogeneity?

Similarly, could any of these results be explained by cross resistance / collateral sensitivity. I'm not an expert in viral dynamics, but I know these features have been studied a great deal in bacteria. Is it well established that the mutations found here – which are assumed to be associated with resistance to a single drug – have no collateral effects (i.e. confer increases resistance or sensitivity to more than the target drug)? The authors mention cross-resistance briefly, but it might be worth discussing in a bit more detail.

Reviewer #3 (Recommendations for the authors):

Introduction

1. I enjoyed reading the introduction, but I don't think it did the study credit. I would suggest clarifying some of the core points. Specifically, (i) what is missing from previous models (e.g. calibration to data? calibration to specific types of data? processes that are known to occur? inability to recapitulate known phenomena?). I was left a little in the dark at the end of the introduction as to what the study was assessing and how these were improvements as to what had gone before. For example, mention is made of 'clinical data' and 'heterogeneity of selection pressures' but without context, it is unclear what these refer to. I've provided some more specific suggestions below.

2. The introduction is very nice, but I would perhaps be a bit more specific about the nature of 'time' and 'space' as mentioned in the sentence:

"Second, mathematical models have explored how heterogeneity of drug levels in time (Rong et al., 2007; Braithwaite et al., 2006; Rosenbloom et al., 2012; Cadosch et al., 2012; Bershteyn and Eckhoff, 2013) and space (Kepler and Perelson, 1998; Moreno-Gamez et al., 2015; Sanche et al., 2017) can allow the evolution of resistance,…"

as it reads to me a little vague. E.g. what is 'heterogeneity of drug levels'? are the timescales and the spatial scales that have been evaluated? More information would be helpful please.

3. Would remove the word 'quite' as it is ambiguous (same comments applies elsewhere); and perhaps 'Sophisticated' might be replaced by 'complex' or the clause left out entirely.

4. As above (in 1.) "… there is no common framework to test the effects of spatial and temporal heterogeneity on triple-drug combinations of antiretrovirals." is a little vague to me. Can you pin down what you mean by 'spatial and temporal heterogeneity'

5. "…as revealed by various facets of clinical trial and cohort study data" is also vague. Can you explain what these facets are?

6. "Matching models specifically to mutational patterns in clinical data can help us better understand whether these models can explain multi-drug resistance evolution in the real world." – has this been done ? (i.e. calibrating models to mutational patterns within individuals)

7. "…to match clinical data across multiple dimensions" – again, please clarify what you mean by 'multiple dimensions'.

Figure 1

8. Very nice graphic. Could you indicate the timescales of the studies and/or accrual of mutations in the caption?

Section 2

9. "(2) Viruses do not need to be fully resistant to all drugs in a combination in order to spread" – I find this conclusion a little confusing, presumably you mean emerge to detectable levels within a single individual?

Figure 2

10. I'm not convinced by the description of panel A. This in part may be down to more explanation needed of the data. What does the x-axis represent – time since study commencement or time since beginning of therapy? Did all patients keep receiving the triple Tx continually through the study?

11. You conclude that the probability of acquiring a DRM is approximately constant (because the gradients of each of the lines are approximately constant?). However, because the frequencies of DRMs are plotted across the whole population, it's not clear whether the accrual of each DRM is independent or not. Equally, to me it looks like there is saturation of the frequency of these DRMs as well as some more complex cumulative distribution happening. You don't rule these out, but how would these phenomena change your conclusions?

Figure 3B

12. Could the authors give more evidence for the existence of the idealised Hill curve for the drug response? Specifically, at high doses, why would we expect the replication capacity of the drug resistant mutant to be approaching 0?

13. Leaving aside my reservations about the shape of the graph, I believe this graph only captures part of the story; that is, the replication capacity of the mutant existence. Two other factors come into play if a composite measure of 'Chance of mutant emergence' is considered: (i) the probability that the mutant exists (this is a function of the viral load, which itself is a function of R0 – i.e. high VL when R0>1, low/negligible VL when R0<1) and (ii) the probability of an outbreak for a given R0 and existence of a mutant. Approximately this probability is 1-1/R0, then finally (iii) the relative replication capacity vs wild type. The chance of mutant emergence would then be the product of all three. This is just an idea, and by no means a suggestions for inclusion, but it's been the way I think about emergence of drug resistance and may be useful for these purposes.
