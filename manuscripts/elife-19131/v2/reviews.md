# Peer review - Round 1

Editors:
- Dominique C Bergmann, Stanford University/HHMI , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19131.051](https://doi.org/10.7554/eLife.19131.051)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Fluctuations of the transcription factor ATML1 generate the pattern of giant cells in the Arabidopsis sepal" for consideration by eLife. Your article has been favorably evaluated by Christian Hardtke as the Senior Editor and four reviewers, one of whom is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Steven Maere (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. Overall, the experimentalists thought the work was well done, but there were several additional controls and tests of the model that were needed to make this a truly solid story. The modeling was evaluated by another expert who again finds the work generally strong but offered some cautions in interpretations. All felt that the authors should be commended for the very clear writing and explanation of complex data in an accessible way.

Summary:

During development, patterns emerge in tissues and organs. The underlying basis for these patterns is a topic of broad interest in the community. Using the Arabidopsis sepal, an organ with a stereotyped size and shape and an epidermis consisting of several cell types, the authors use live cell imaging and modeling to investigate how the pattern of giant cells (GC) arises. The authors provide evidence that stochastic gene expression, a widespread phenomenon that arises from the nature of gene expression as it responds to intrinsic and extrinsic sources of variation, enables equivalent cells to adopt fates different from some of their neighbors, dependent upon cell-autonomous accumulation of a particular key regulator. In this manuscript the authors present a case for ATML1 being such a factor, whose activity in promoting GC fate is determined by stochastic levels that exceed a threshold.

Essential revisions:

1) Better test of the need for ATML1 in G2

High ATML1 levels are moderately predictive of GC identity (.74 or a.5-random to 1.0 absolutely predictive scale). This is OK, but it makes it all the more important to add in something that suggests the ATML1 level is a major component driving (and not simply reflecting) the fate.

Two possible ways to address this are: (1) The best way to do this would be to increase levels of ATML1 only during G2 and only during G1 and test whether these manipulations fit their model. I don't know all the tools available-in other systems there are G1, S and G2/M specific promoters and there are degradation elements linked to the cell cycle. Could these be employed? (2) If the first test is technically impossible, then another part of their model is that there is a feedback of ATML1 on its own expression. The ATML1 site from their ATML1 or PDF1 promoters could be removed to see whether this makes an important contribution.

2) Provide more convincing evidence that correlation of expression patterns (bursts in G2) aren't more general feature of TFs in these cells.

Reviewers were concerned by the use of pSEC24A::H2B-GFP abundance as a control for whether the relative broad variation in pATML1::mCitrine-ATML1 abundance in the developing sepal is a general phenomenon. H2B is quite different from ATML1 in that it is incorporated in the nucleosomes and likely much more abundant compared to regular transcription factors. Also a different fluorescent probe is used. To prove that varying expression of ATML1 in the sepal epidermis is not a common feature among transcription factors, it would be better to use an unrelated mCitrine-TF fusion as control.

3) Some model interpretations are a bit overstretched and should be reconsidered.

For instance, the assertion in the fifth paragraph of the subsection “A model with stochastic fluctuations of ATML1 reproduces giant cell patterning”, that the model correctly recapitulates G2-mediated giant cell fate specification and that the lower AUC values recovered in 2C stages than in 4C in the model indicate 'that high ATML1 levels during the G2 phase of the cell cycle are important for giant cell fate commitment' is not really justified (or at least does not add anything to the experimental observations to this effect). Since a hard threshold for the 'Target' gene to start endoreduplication is hard-coded specifically in the G2 phase of the model, no other outcome could have been expected. Instead, I think the major contribution of the model is that it shows that stochasticity in ATML1 expression alone, associated with a hard threshold on ATML1 levels to induce giant cell formation, is not sufficient to explain the observations, and that it predicts instead that a hard G2-associated threshold on another stochastically influenced downstream factor, causing the ATML1 threshold to become soft, is needed to explain the imperfect relationship between high ATML1 expression in G2 and the induction of giant cell formation. It seems that additionally this downstream factor needs to have a higher degradation rate so that the 'Target' follows the dynamics of ATML1 (which makes sense, although the alternative was not tested), and that the auto-induction rate of ATML1 should not be too strong. These are in my view the real predictions of the model, the fact that e.g. overexpression of ATML1 in the model would lead to an ectopic giant cell phenotype can already be deduced from the model form without running simulations.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Fluctuations of the transcription factor ATML1 generate the pattern of giant cells in the Arabidopsis sepal" for further consideration at eLife. Your revised article has been favorably evaluated by Christian Hardtke as the Senior Editor, and a Reviewing Editor.

The manuscript has been significantly improved in many places, but there is still one issue to address.

Because you cannot supply ATML1 at a specific phase in the cell cycle, nor delete promoter elements, but instead rely on following endogenous ATML1 transcripts after induction to infer a feedback loop, this last experiment must be very carefully done and interpreted.

A concern is whether the technical set up (and point at which ATML1 is monitored) has the capacity to report a "strong" feedback and indeed, what level of transcriptional up-regulation would be considered strong feedback. How can the experiment be calibrated? You will either need to cite evidence from similar experiments (same induction system and timing and tissue for monitoring) that put the 1.7 fold increase in context, or do this type of control experiment yourselves.
