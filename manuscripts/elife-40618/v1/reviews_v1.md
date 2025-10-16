# Peer review - Round 1

Editors:
- Richard A Neher, University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40618.022](https://doi.org/10.7554/eLife.40618.022)

In the interests of transparency, eLife includes the editorial decision letter, peer reviews, and accompanying author responses.

[Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that minor issues remain unresolved.]

Thank you for submitting your article "Precision measurement of cis-regulatory energetics in living cells" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Richard A Neher as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Naama Barkai as the Senior Editor. The following individual involved in review of your submission has also agreed to reveal their identity: Ulrich Gerland (Reviewer #3). Reviewer #2 remains anonymous.

The Reviewing Editor has highlighted the concerns that require revision and/or responses, and we have included the separate reviews below for your consideration. If you have any questions, please do not hesitate to contact us.

Forcier et al. present a method to quantitatively estimate parameters of transcriptional regulation in vivo. The method is based on a phenomenological model of regulation that accounts for DNA binding of transcription factors and the RNA polymerase as well as interactions between them. The parameters of these models are estimated by comparing transcription for a range of promoter sequences in the presence and absence of the regulator. All reviewers agreed that the authors have devised an innovative and original way to quantify crucial parameters determining the fundamentals of bacterial gene regulation. However, the reviews and the ensuing discussion brought up a number of concerns that the authors should address.

1) How do the inferred parameters depend on growth rates and physiological state of the cells? Given that substantial contributions to the inferred free energies are entropic, changing concentrations of the interacting partners will affect the estimated energies. Comparing parameter inferences at different growth conditions would illuminate the nature of the measured free energies and make the precision of the measurements more interpretable. Repeating the measurements in different growth media would be one way to explore this effect.

2) The outlier classification and removal seem rather arbitrary. While many biophysical aspects change when promoter sequences are exchanged and these factors are difficult to include in a quantitative model, a more thorough discussion of why outliers might arise and how they can be distinguished from data that putatively conforms with the model is necessary.

3) What alternative scenarios might explain the failure of the model when CRP sits at -40.5 (see reviews below). How do you meaningfully distinguish a 'failure to collapse' from 'more outliers'?

Separate reviews (please respond to each point):

Reviewer #1:

Forcier et al. present a method to quantitatively estimate parameters of transcriptional regulation in vivo. The method is based on a phenomenological model of regulation that accounts for DNA binding of transcription factors (TF) and the RNA polymerase (RNAP) as well as interactions between TF-RNAP and potential accelerated initiation by TF-RNAP interactions. The parameters of these models are estimated by comparing transcription in the presence and absence of the TF for a variety of the promoter sequences. If a particular scheme of regulation is valid, the two sets of transcription rates are expected to follow a path in the 2d plane and parameters can be estimated from the shape of this path. Failure to collapse indicates a model misspecification.

The nature of the method cancels out/avoids many pitfalls and inaccuracies that arise when fitting more complex explicit models to transcription data. The resulting consistent in vivo measurements are an important step at understanding the energetics of the simplest and most fundamental regulatory systems.

Overall, I feel this is a solid piece of work with consistent results obtained by a clever and original method. The authors discuss ways in which this method could be scaled up to high throughput assays, but this part of the manuscript remains very vague.

The bulk of the DNA-TF binding free energy is claimed to be of entropic nature favoring the unbound state, while RNAP-TF interaction energies are estimated to be much larger than previously thought. To make the manuscript stronger, I would like to see the experiments being performed at different concentrations of the TF (CRP), i.e. vary F via [TF] and not only P.

Minor Comments:

Figure 1C and D: Some of the regimes and their relation to the figure are confusing. All seems correct, but some approximations and definitions are not what I initially thought they were.

a) Why not combine regimes 1 and 2 into t_- = t_bg + Pt_sat and t_+ = t_bg + Pt_sat/(1+F).b) Regime 3: if you don't realize that the figure is meant on a logscale (it is marked, I know, but took me a while to realize). Might be better to mark the diagonal lines as t_-=t_+ and t_- = t_+*(1+F) or similar.

Subsection “Strategy for measuring TF-RNAP interactions in vivo”, second paragraph: cooperatively -> cooperativity

Reviewer #2:

The authors carefully quantify binding of the TF crp by changing the affinity of the RNAP binding sites. Experimental measurements of transcription rates are used to infer binding by parameterizing a biophysical model.

The premise of the paper is very interesting and creative. Because of this, I think it is worth investing more energy in making sure the method is made clear – although I am not sure how to do so. The manuscript was also very substantial, and at times difficult to get through. With some clarifications, I think it is worth publishing.

Major comments:

The model and theory.

With the caveat that I do not have strong theoretical expertise:

The use of "manifold" seems to complicate the matter in the context of this paper. As I understand it, the authors are fitting points to a (nonlinear, geometrically complex) model, and looking for deviations from the various regimes of the model. I expect that both t+ and t- are always monotonically increasing functions of P (as they are modelled). A manifold approach would be required if (for example) t+ increased and then decreased as a function of P, but such a case does not appear in the paper, and is not trivial to conceive. Perhaps the authors could explain when/why a manifold approach is necessary.

The classification of points as "outliers" is arbitrary (e.g. Figure 4C for the site at -66.5). A more objective approach could be taken. For example, changes to fitting method could mitigate this. The current loss function minimizes least squares on the log values. I think this is equivalent to assuming error is log normal and minimizing. Could this assumption be relaxed to assume log normal error for most points plus a fraction of points ("outliers") that are drawn from a uniform distribution with some reasonable limits?

Bootstrap: is this necessary? Can the authors infer some confidence interval using the loss function? The most important implication is that the bootstrap procedure may overestimate the precision of their measurements.

Experiments.

I am not sure whether 250uM cAMP is enough to guarantee full occupation of crp in glucose?

Could the authors provide some data for a small number of RNAP binding variants?

It also might be informative to have cAMP induction/repression curves for a few RNAP binding variants.

I'm surprised the authors opted for Miller assays over GFP cytometry (and microscopy). They mention single cell data from another paper, but do not provide any, nor any live cell data. There is information that could be gleaned from single cell data that is relevant. For example, the variance in txn among cells could corroborate the mean txn rate they observe and use to infer binding constants. GFP assays would also provide a corroborative measure of mean expression for the Miller assays.

Can the authors discuss briefly the question of the validity of using plasmid-based assays (in fact I think these are better than chromosomal-based assays for this experiment).

Subsection “Surprises in class II regulation”: The authors frame their result as "When measuring an expression manifold at this position, however, we obtained a scatter of 2D points that did not collapse to any discernible 1D expression manifold (Figure 7D)." I am not convinced. This is a bolder statement than the rest of the paper and requires a bit more evidence to assert. Another interpretation is that for reasons not established, there was more noise (or more outliers) in this experiment than in others.

Minor Comments:

Subsection “Precision measurement of in vivo CRP-DNA binding”: dyadic is an obscure term

Reviewer #3:

General assessment:

The authors devise a scheme to systematically determine the effective in vivo interactions between RNA polymerase, transcription factors, and their respective DNA binding sites. The scheme is based on quantitative gene expression measurements from a large number of promoter constructs, which are interpreted using models for competitive and/or cooperative protein-DNA binding. The authors illustrate the power of this approach with a study of cis-regulatory transcription control by the transcription factor CRP in E. coli.

The general question attacked by this study is clearly important: How can we characterize the in vivo interactions between DNA-bound proteins that determine transcription rates? The authors make significant progress on this question with their proof-of-principle study of CRP-mediated transcription control, since the underlying approach can readily be transferred and extended to other cases of cis-regulatory transcription control.

Comments and questions to the authors:

1) The authors stress the importance of having in vivo rather than in vitro interaction parameters, and the precision with which they determine these interactions. It is indeed nice to see how well the data collapses, and the quality of the fits is convincing. However, given these encouraging results, I find it important to assess the limitations of both the concept and the precision more broadly. In particular, are the in vivo interaction parameters fixed numbers for a given E. coli strain, or do they depend on the state of the cells? All of the experiments were done with the same growth rate and conditions. The effective strength of CRP binding to its consensus DNA site was found to be -2.1 kcal/mol with 0.1 kcal/mol precision under these conditions, but does this parameter change when the cells are put under conditions of e.g. slow growth? The same question applies to the CRP-RNAP interaction. If these parameters do change with the state of the cell, how do the changes compare to the 0.1 kcal/mol precision? This question is crucial to appreciate the significance of the numbers obtained – will they need to be remeasured under every condition or can they be measured just once and then applied to a broad range of conditions?

2) The analysis of CRP regulation from the -40.5 bp site provides an interesting example of a case where the model fails. However, at this point more insight might be gained by considering alternative biophysical models. For instance, could it be that β now depends on the -10 sequence of the promoter? Or could CRP bound in this position generate a situation of "frustrated binding" for RNAP, i.e., it can simultaneously contact the -10 and the -35 region of the promoter when CRP is absent, whereas in the presence of CRP it could only make either the -10 contact or the contact with CRP/-35, and would choose the better one? Perhaps these scenarios are also ruled out by the absence of data collapse – can the authors specify which types of scenarios are ruled out and which are still possible?

3) I think the authors should discuss more clearly which difficulties will need to be overcome when their approach is extended to regulation via more than one TF-binding site. In particular, it seems that determining pairwise interactions may not be enough, since the interaction strength between proteins A and B can depend on whether protein C is bound or not (i.e., 3-body interactions). This can significantly complicate the analysis. How will the approach be generalized – 3-dimensional plots with data collapse onto 2D surfaces? Personally, I think the best hope is that bottom-up approaches like this one will be complemented with top-down approaches like the one described in Hillenbrand et al., eLife (2016).

Minor Comments:

– Abstract: in my mind, RNAP is not a TF

– Results section, third paragraph: the conversion from kT to kcal/mol is wrong

– “Our result indicates that, in living cells, this Gibbs free energy is almost entirely canceled by the entropic cost of removing a CRP molecule from the cytoplasmic environment”: can the authors provide a back-of-the envelope estimate to interpret this conclusion – is this approximate cancellation reasonable/expected?

– Second paragraph of subsection “Strategy for measuring TF-RNAP interactions in vivo”: "cooperatively factor" α -> cooperativity α?
