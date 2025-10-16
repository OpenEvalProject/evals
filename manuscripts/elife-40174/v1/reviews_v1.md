# Peer review - Round 1

Editors:
- Asifa Akhtar, Max Planck Institute for Immunobiology and Epigenetics Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40174.045](https://doi.org/10.7554/eLife.40174.045)

In the interests of transparency, eLife includes the editorial decision letter, peer reviews, and accompanying author responses.

[Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that all the issues have been addressed.]

Thank you for submitting your article "Time-resolved mapping of genetic interactions to model rewiring of signaling pathways" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aviv Regev as the Senior Editor. The reviewers have opted to remain anonymous.

The Reviewing Editor has highlighted the concerns that require revision and/or responses, and we have included the separate reviews below for your consideration. If you have any questions, please do not hesitate to contact us.

In this study, Boutros and colleagues study the plasticity of genetic interactions by performing an imaging based RNAi screen using combinatorial knockdowns at multiple timepoints in Drosophila. By studying in particular on the RAS signaling pathway, authors showcase several examples of context dependent crosstalk. All three reviewers are interested in the study and thought that this will be an interesting resource for the community.

However, concerns were raised regarding the clarity of methodology to make it accessible and useful resource for the field. Also, the manuscript currently appears very technically written and therefore reviewers have made several suggestions for sections where optimization is required so that the main message and importance of the study comes out more clearly.

Separate reviews (please respond to each point):

Reviewer #1:

This is an extremely technically and statistically thorough study using quantitative phenotyping in Drosophila cells to look at genetic interactions in sub-genome scale set of genes. WHat marks this out in particular is that the authors are specifically interested in interactions that change over time following chemical perturbations. In broad terms this is a really important question and the thoroughness of both the experimental approach and the rigour of the statistical framework that they devise to examine and compare GIs is outstanding. I am thus happy both with the importance of the science and the technical quality of the work.

My main comments would be that the authors need to flesh out some of their data descriptions so that we know more why these conclusions are important and what they mean biologically as well as what happened. This is most true (for me at least) in the section 'Differential GIs enrich in stress responsive genes…".

1) ksr and rl form a syn sick interaction independent of Ras – what does this mean biologically? How does it change how we think they act?

2) Next paragraph skd and Stat92E – synlet connects them until perturbed. Same question – how does this affect our view of how these pathways work?

3) High numbers of alleviating (nuclear shape) or aggravating (nuclear texture) stable interactions. Is this different to what we expect? Why? What is the null expectation for these results?

4) Exceptionally high time dependence for interactions with housekeeping genes. Why?

GIs are pretty abstract entities. How they are expected to change across time is something I cannot guess so having some idea what we might have expected and what these findings reveal would really help.

I'd also suggest in future that as well as focusing on a well chosen gene set as they do here, they also do similar analyses on a set of random genes so we can see whether the trends they find are specific to the chosen genes or to genes in general. I know that adds greatly to the work (hence not requiring it here) but I think it would be useful.

Minor Comments:

Results section, paragraph twenty; extent

Figure 2 – I'd prefer something other than yellow in A. It's faint on the page.

Reviewer #2:

In this work, Heigwer et al. develop a method to map genetic interactions in a time-resolved manner. They use automated microscopy of Drosophila cells treated with dsRNAs and/or chemical compounds to study "trigenic" interactions.

This is mainly a technology paper, with some quite interesting preliminary observations. The main fleshed out contribution here is the time-resolved analysis and associated tools. The manuscript is clearly (albeit very verbosely and technically) written, and should be published after corrections below.

Major:

– There is excessive technical and numerical detail in the main text, making the work difficult to access. This will limit the ability of general readership to discern the main contributions. I would recommend moving some text to methods section, and more technical figure panels to the supplement, and making a new final model figure that summarizes the main contributions and highlight the rationale of using the time-resolved approach. I would try to answer the question: What did we find because we used this technology that we could not have found using a more standard end-point genetic interaction analysis?

– The outputs that are studied are expected to behave differently over time. Cell number expands exponentially, whereas cytoplasmic phenotypes could be largely additive or have sigmoidal response functions. The type of "interaction" detected will depend on the assumed shape of the downstream input-output curve. This should be discussed, possibly citing relevant papers such as that from the Lehner group in recent eLife. It should also be considered whether the different temporal responses of interactions between components involved in distinct biological processes result from differences in shapes of the input-output curves.

– Feedback will also lead to epistasis, and the authors' approach might be able to detect the mechanisms of feedback, as transcriptional feedback is expected to be slower than phosphorylation- or allostery-based feedback, and translational or transcriptional components might behave differentially when they are required for feedback. Analysis of this aspect would increase the impact of the study and give the readers a sense of "why". Now the paper looks a bit like "we did this because we can".

Minor Comments:

Abstract "end-point assay"

Results paragraph seven; "a control perturbation"

Paragraph two subsection “Differential genetic interactions enrich in stress responsive genes and pathways”; "to such an extent that"

Reviewer #3:

In this manuscript Heigwer and colleagues study how multi-parametric genetic interactions inferred from double knock-down experiments change during time in the presence or absence of a kinase inhibitor. Pair-wise gene deletions or knock-downs have been used for a long time to study how the consequence of the double gene perturbations to a phenotype is different from expectation. More recently, such pairwise combinations have been performed in different environmental conditions or in different genetic backgrounds. In this study the authors asked how such genetic-interactions change during time. Time dependencies in genetic-interactions were previously exploited but not studied, as mentioned by the authors, by Shen and colleagues (Shen et al., 2017). For this purpose they have developed a linear regression model to jointly estimate the impact of the kinase inhibitor and the time dependencies of the genetic-interactions. The authors go to great lengths to set-up the experiments and to show the validity of their data and approach. In fact, about half of the results are devoted to this. They first performed a single gene down-regulation screen in the presence/absence of MEK inhibitor using microscopy and imaging as cellular phenotypes. Based on this they selected a set of candidate genes to perform a 76 by 168 double gene knock-down experiments in 3 time points (+/- MEK inhibitor). They performed a series of benchmarks on the screens to ensure that the data is reproducible.

From the genetic-interactions screens there are some general analysis and findings. From a technical point of view the authors show that modelling the time dependencies as they do can identify a higher number of differential interactions when compared to previous approaches. Biologically, most of the interactions with changes over time were interactions that changed in magnitude over time in a way that was similar in the control and MEK inhibitor (called "stable" by the authors). Those interactions that changed over time differently in the inhibitor versus the control were found to be enriched in signalling genes. One aspect that I found particularly interesting was the possibility to assign a magnitude of time dependence to each differential interaction. Based on this they briefly explored how some phenotypes and some genes were more responsive to changes after perturbation. The authors showed that the correlations of the changes interactions is predictive of functional association. Finally, from the analysis of correlation of differential interactions, they then selected and further investigated the role of Rel as a potential negative regulator of Ras signalling.

Overall, I think this work explores well the changes in genetic-interactions over time after perturbation. The analysis is well performed and extensively benchmarked. I have the impression that the manuscript focuses almost more on the generation of the data than on the new insights. It was also not very easy to follow but that is also due to the complexity of the experiment – non linear effects of pairs of gene knock-downs over time plus and minus drug. Even for researchers used to thinking about genetic interactions the results of these assays should be difficult to conceptualize. In part, this complexity also makes it difficult to extract novel findings on the genetic architecture of the cell.

I have no major concerns regarding the work, only a few minor points on clarification that the authors may consider:

– From my reading of the manuscript the major novel findings of this work relate to the time dependencies on the differential genetic interactions. However, almost half of the Results section relate to the process of obtaining the differential interactions. While I commend the authors for the thorough characterization of the chemical-genetic and genetic-interaction data it would be possible to summarize further the initial results, in particular the initial screen for MEK inhibitor sensitive genes and to a lesser extent the establishment of the genetic interactions. This could give more space to focus on the main novel findings regarding the differential genetic interactions. The section on the differential interactions could in turn be broken down into more sub-sections trying to give more visibility to the main new findings that derive from this data.

– The article gets confusing in the nomenclature of the genetic-interactions. These interactions can be: time (in)dependent, differential, stable, positive, negative, aggravating and alleviating. In particular, calling a time dependent interaction as "stable" is awkward. Perhaps using condition independent or condition insensitive instead of stable would be clearer.

– The differential genetic interaction method is not described in the Materials and methods section. Are all genetic interaction pairs tested for differential interactions ? Can a genetic interaction be called as significantly changing without having a strong effect size in any condition? Looking at the genetic interaction scores of replicates in Figure 2—figure supplement 5, the values range from around -5 to 5 with strong variance around -0.5 to 0.5. However, in several places in the article the interaction values and changes highlighted are often in the ranges of 0 to 0.5. Are these interaction terms calculated in the same way in Figure 2—figure supplement 5? It would appear that the variance in replicates is higher than the apparent precision of the method.

– How are condition independent interactions ("stable") defined ? A cut-off on the condition sensitivity parameter ?

– Given that the differential interactions are being called with a linear model on the time differences with a term for the drug effect, are time invariant but drug dependent genetic interactions well captured by this model ?

Minor Comments:

- Figure 1E – annotate in the figure what are the Ras pathway components and translational regulators groups described in the Results section for clarity.

- Figure 4F – could be move to supplementary materials and corresponding results description shortened.

- Figure 2—figure supplement 2 – figure title is wrong
