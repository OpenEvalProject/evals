# Peer review - Round 1

Editors:
- Pierre Sens, https://ror.org/02feahw73 Institut Curie, CNRS UMR168 France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78787.sa0](https://doi.org/10.7554/eLife.78787.sa0)

This article reports fundamental findings regarding spatiotemporal control of myosin-based force generation during Drosophila germband extension and is of considerable interest to our understanding of tissue morphogenesis during early development. Using quantitative imaging, mathematical modeling, and mutant analysis, the authors provide compelling evidence that myosin polarity patterns are not governed by pair-rule gene expression, but that a geometric cue promotes myosin II accumulation of vertically oriented junctions. The results challenge current views of how gene expression patterns control myosin II anisotropies and provide new testable hypotheses on the role and importance of tissue geometry.


---

# Peer review - Round 1

Editors:
- Pierre Sens, https://ror.org/02feahw73 Institut Curie, CNRS UMR168 France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78787.sa1](https://doi.org/10.7554/eLife.78787.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Geometric control of Myosin-II orientation during axis elongation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Ed Munro (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. All referees agree that this is a strong study reporting important findings regarding the dynamics of a developing Drosophila embryo, supported by rigorous quantitative analysis and modeling. There is a consensus amongst the referee to ask for additional data regarding the myosin lifetime in mutants, which would strongly support your predictions. The referees also made a number of comments and suggestions that will help improve the paper.

Essential revisions:

1) Explain more clearly in the main text how the data are used to compute the myosin lifetime (Reviewer 1, 1) and Reviewer 3, 1.b))

2) Report data on myosin lifetime for mutant (in particular Fat2-RNAi) embryos (Reviewer 1, 2) and Reviewer 3, 5))

3) Explain in the main text why more complex models can be ruled out (Reviewer 1, 5) and Reviewer 3, 2)).

4) Reformulate or temper some claims, in particular regarding changing change "PRGs" to "Runt" and "TLRs" to "Tartan" throughout the paper (Reviewer 1, 3)) and Lagrangian dynamics into something like "passive advection" (Reviewer 2).

5) Consider the possibility of using a symbolic regression technique to disprove a relationship more complex than the linear one you tested between PRG and myosin (reviewer 2).

6) Check for myosin enrichment in junctions that become aligned with the DV axis (Reviewer 3, 4).

Please also consider the other comments made by the reviewers, below.

Reviewer #1 (Recommendations for the authors):

1. Using mathematical modeling, the authors propose a myosin lifetime of 5 minutes. The experimentally measured myosin turnover rate in this study is just over 3 minutes. The authors should provide more information about the myosin lifetime parameter and comment on possible reasons for the approximately 1.5-fold difference between the myosin lifetime predicted by modeling and the time to full recovery measured using FRAP.

2. The authors should clarify the predictions of their model for eve mutant, twist mutant, and Fat2-RNAi embryos and perform FRAP experiments to experimentally test these predictions. The authors should apply their model to Fat2-RNAi, which provides the most direct test of their model that embryo geometry provides the static source that aligns myosin anisotropy with the DV axis. At face value, it is not clear how the results in Figure 4, which show largely normal myosin dynamics in a substantially geometrically altered embryo, argue for an instructive role of tissue geometry. The authors should include a more complete analysis of Fat2-RNAi embryos, including applying their model to Fat2-RNAi, analyzing myosin dynamics in the ventrolateral region of Fat2-RNAi embryos by FRAP, and quantifying the change in embryo DV width to document the effects on embryo geometry.

3. The authors extrapolate from their data on Runt to all pair-rule genes (PRGs) and from their data on Tartan to Toll-like receptors (TLRs). These assumptions are not well supported, as it cannot be assumed that all PRGs behave similarly, and Tartan is not only not a TLR, but it also has a different phenotype and function that (unlike TLRs) is restricted to compartment boundaries. As a result, there is no reason to assume that conclusions about Tartan will pertain to TLRs. The authors should change "PRGs" to "Runt" and "TLRs" to "Tartan" throughout the paper.

4. Claims that the myosin pattern is static, made in the Abstract and in parts of the main text, are not fully consistent with the authors' data. Figure 3b shows that the myosin pattern significantly shifts before realigning with the DV axis, and Figure 2k' shows that myosin is aligned with Runt stripe 6 until t=20 minutes, even though the Runt stripe shifts substantially relative to the DV axis. Myosin anisotropy that is out of alignment with the DV axis is also apparent from the images of posterior regions in Figure 2i' and 2j.

5. The last sentence of the Results states that "these results suggest that instead of instructing anisotropic myosin recruitment, PRGs influence the myosin anisotropy by regulating retention of myosin to junctions" is not well supported by the authors' data. Numerous studies, including by the authors, show that eve mutants have less cortical myosin and that myosin turnover is inversely correlated with myosin levels at the cortex. The authors' data are equally consistent with the alternative interpretation that PRGs instruct anisotropic myosin recruitment, with myosin dynamics later modulated by a myosin positive feedback mechanism. The authors should explicitly acknowledge alternative interpretations that are consistent with their data.

6. In the Materials and methods, Fly stocks, and genetics section, "hemizygous control embryos lacked halo" should be changed to "heterozygous control embryos did not show the halo phenotype". The authors should describe the Fat2 RNAi method used. References describing the generation of all antibodies should be cited, and the peptide sequence used to make the Tartan antibody should be described.

7. The location of dorsal and ventral regions should be indicated in all figures, as it is not clear if all embryos are similarly oriented. In Figure 2f and 2g, the correlation coefficients are labeled with the same value. In Figure 2a, measured is misspelled.

Reviewer #2 (Recommendations for the authors):

Overall, I think this is a very good paper, and subject to a couple of revisions would recommend it for publication.

Suggestions:

As I understand it, your experimental measurements include both the full velocity field and the various director fields. Given that a big element of this paper is demonstrating the validity (or lack thereof) of a Lagrangian description of the dynamics, I think it would strengthen the paper to include some direct analysis of the upper convected derivative of both the PRGs and myosin director fields. For instance, a comparison of the magnitude of this quantity for PRGs and myosin at t=7 and t=22 would be helpful in understanding the differences in dynamics between the two.

Since this is a case of tensor transport over a curved surface, there should be some discussion of the possible role of parallel transport. The region of interest in the WT Drosophila embryo is essentially a cylinder you can probably rule out via a quick back-of-the-envelope calculation, but I imagine that there might be a non-negligible effect on the Fat2 mutant, subject to what the flow lines look like in the high vorticity regions.

The language regarding Lagrangian dynamics should be tightened up a bit. Formally, Lagrangian should be used in reference to the Lagrangian frame of reference or coordinate system of the fluid. In my experience, the phrase "Lagrangian pattern," as in the last sentence of the first paragraph, is not really well defined and is being used here to describe what should just be called passive advection. Likewise, it does not make much sense to say that PRGs and TLRs are in a flowing frame of reference, as stated in the last paragraph of the introduction. Any phenomena can be in any frame of reference you want – it would be more correct to say PRGs and TLRs are easy to describe in that particular frame. At these points and in a couple of other places where Lagrangian flows are discussed, the language should be made more precise.

The analysis relating to Equation 1 is fine in itself, but the conclusions drawn from it are not especially convincing, as it is easy to imagine that a nonlinear relationship exists between myosin and PRGs. I think it would be easy to improve this result by applying a good symbolic regression technique to your existing data to see if that likewise fails to generate a clear function for myosin.

In section SE, m is used for two different quantities: to symbolize the local myosin alignment tensor in (13) but also for the angular distribution throughout subsection SE1. Maybe substitute the first m with Q or another symbol.

It is a slight overclaim to say you can independently modulate model parameters in vivo. Myosin kinetics, geometry, and vorticity are not independent, and none of your experiments actually let you alter one while fixing all the rest.

Sometimes the authors write "germband" and other times "germ band" – there is not really a correct spelling but one should be selected and used consistently in the paper.

Figure 3h is a little confusing at first glance. We are meant to compare h, h', and h', but the bar colors mean different things across the panels and there are vortex streamlines in the back of h' even though some of the data on that plot represents irrotational flow.

Reviewer #3 (Recommendations for the authors):

(1) The comparisons of model predictions and experimental observations are presented in a way that I found (and I expect other readers will find) confusing. It would be useful to clarify in the main text (with links to SI as appropriate):

(a) What data are the authors fitting to obtain estimates of myosin lifetime?

I could not find any description of this, either in the main text or the SI. This would be especially important for the analysis of eve mutant embryos where they are drawing a strong conclusion that the myosin lifetime is reduced in these mutants.

(b) What additional predictions of the model are they then comparing to additional data?

For example, the direct comparison of observed and simulated distributions of MRJ orientations shown in Figure 3h is very clear and compelling. It would be helpful to show similar comparisons for Figures 3b and 3i to back up what currently seems like vague and qualitative statements in the main text.

(2) Several questions arose as I was reading the main text. I later discovered that these are addressed in the SI. Because I suspect other readers will have similar questions – I suggest the authors address these questions briefly in the main text and refer to the more detailed discussion given in the SI. These include:

(a) To what extent do local reorientation of MRJ's, e.g due to anisotropic junction shortening, T1 transitions, cell divisions, etc affect the orientation distribution of MRJs during GBE?

(b) In principle, a model based on modulation of myosin detachment by a static geometric cue could also explain the steady state alignment of MRJ's with the DV axis. Can the author's observations exclude this alternative possibility?

(3) The data in Figure 4 showing the analysis of different mutants is also presented in a somewhat confusing way. The opening sentences of the section make it sound like the authors are using existing knowledge of certain mutants to systematically and independently manipulate specific parameters in the model. But it seems like what they are really showing (for twist and eve) is that mutant phenotypes could be explained as tuning variants of the simple model (with different vorticities and myosin detachment times).

By contrast, for fat-2, they are not testing the static source model at all – instead, they are extending an earlier conclusion about the insufficiency of PR and TLR expression patterns that do explain myosin II anisotropies.

(4) A key prediction of the static source model is that myosin II would begin to accumulate on junctions that rotate into alignment with the DV axis in regions of high vorticity (i.e. stripe 6). Would it be possible to test this with their existing data by tracking (perhaps even by hand) a subset of junctions that become so aligned?

(5) The model fits to eve mutant data suggest that there is a reduction in the myosin II detachment rate. It would be awesome, if feasible, to test this directly with FRAP experiments.
