# Peer review - Round 1

Editors:
- Michael T Laub, Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65467.sa1](https://doi.org/10.7554/eLife.65467.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This manuscript presents intriguing data to support the notion that B. subtilis cells have tuned a variety of parameters related to SMC loading and translocation to ensure that individual complexes do not collide. This is likely an important but poorly understood aspect of condensins/SMCs, and as such represents a valuable contribution to the field and should be of interest to a broad set of readers.

Decision letter after peer review:

Thank you for submitting your article "Fine-tuning of the Smc flux facilitates chromosome organization in B. subtilis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor, Michael Laub, and Jessica Tyler as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

Although the reviewers were generally enthusiastic, there were some concerns raised. The full set of concerns/issues is appended below and the authors should respond to each item in a revised document. Immediately below is a summary of the 5 major issues – the first two include additional experiments that the reviewers collectively decided would be needed for a revision.

1) The authors need to include a quantification of SMC (and SMC variant) levels, including an assessment by chromatin fractionation of the quantity free in solution versus chromosome-associated. There are also several cases of quantification of Hi-C data that are needed.

2) Additional experiments are needed to help address the relative contributions of SMC-RNAP and SMC-SMC collisions. In particular, the reviewers agreed that the authors should examine the effects of adding rifampicin on WT-SMC and SMC-CC425 with all parS, parS-9 kb, and two parS (e.g. parS-9 kb and parS-304 kb). The results in Figure 4 with higher levels of WT-SMC could also potentially benefit from the addition of a +rif experiment, though this was deemed lower priority.

3) In some cases, conclusions about the actions of SMC in individual cells are being made based on Hi-C data that intrinsically average the behavior of SMC in large populations of cells. This fact should be more carefully taken into account when interpreting and discussing the data presented.

4) In general, the authors should, in light of the comments from the reviewers ensure that the conclusions they draw take into account the full set of possible models that explain their results, not just the favored model. In other words, if alternative models cannot be fully ruled out in some cases, please make that explicit in the text and tone down conclusions accordingly.

5) Finally, although not noted in the reviews, the discussion among the reviewers led to the suggestion that the paper should better discuss the simulations in the pre-print from Wang and Mirny, which is cursorily discussed in the current version of the manuscript at hand.

Reviewer #1 (Recommendations for the authors):

The data generally support the conclusions.

I would like to see inclusion of some chromatin fractionation experiments to directly address the quantity of Condensin in free versus chromosome-associated states – many of the authors conclusions would be strengthened by inclusion of these data.

Reviewer #2 (Recommendations for the authors):

Below I list out a few other suggestions/concerns for the authors to consider:

1. Figure 3B: the insertion of two equally strong parS sites on an otherwise parS-less background showed reduced loop formation/arm alignment. This can be attributed to SMC collision or that the total pool of the SMC loader (ParB) is being shared equally between the two parS sites, leading to fewer SMC available to travel from each site. Can the authors rule out the later possibility? I think this is an important point since the accumulation of SMC in the interval between the 2 parS sites (as seen by a population-averaged method such as ChIP-seq, Figure 3C or so) does not necessarily mean that SMCs collide there.

2. ParB can slide at a short distance but might bridge over a longer distance, should the authors consider the possibility that the very weak Hi-C interactions (orange box, Figure 3B ) is due to the bridging of ParB-DNA from the two distal sites

3. How did the authors distinguish experimentally between SMC loading rate and SMC unloading rate? For example, lines 196-199: "..indicating that the modified SMC coiled coil impede DNA translocation and/or increased the rate of unloading". Why an increase in unloading rate? The proposed increase in unloading rate for the arm-modified SMC-CC425 is very counter-intuitive to me when I looked into the magnified ChIP-seq profiles (Figure 2A). Figure 2A (left panel, WT SMC): parS-9kb does not align with the summit of the highest ChIP-seq peak. That is probably due to SMC unloading/escaping from the loading site parS. However, in Figure 2A (right panel, SMC-CC425), parS-9kb aligns perfectly with the summit of the highest ChIP-seq peak. Naively, that suggests to me that SMC-CC425 has a problem either (i) unloading less from parS (rather than more as proposed) or (ii) SMC-CC425 somehow being held on more tightly by the loader ParB. Could the authors clarify this, please?

4. Is this possible, given available data, to speculate on why there is no major arm-alignment in an all-parS + SMC-CC425 strain (Figure 1B)? Is that because of too many collisions in the main parS cluster that cannot be resolved by a defective SMC-CC425, leading to unproductive loop formation?

Reviewer #3 (Recommendations for the authors):

Improvements on the presentation of previous models and results from the literature:

– Is there direct evidence that bacterial condensins also work by loop extrusion? This is not clear to me and is an important assumption of the authors.

– "Smc-ScpAB complexes start DNA translocation from predefined entry sites". The manuscript cites Gruber and Errington and Sullivan (2009) but did these studies show that SMC-ScpAB translocate on DNA?

– Citations of ParB binding specifically at parS should rather acknowledge the original papers describing this, as it is unimportant whether ParB forms a clamp or not.

– The first to describe condensin-dependent co-alignment of chromosome arms in Bacillus were the papers of Wang et al. (2015) and Marbouty et al. (2015). These should be cited for this instead of: Minnen et al., 2016;Tran et al. 2017; Wang et al., 2017.

– The authors seem to assume in the introduction that Bs SMCs translocates by a two-sided mechanism. But has this been demonstrated?

– Removal of parS/ParB in Bs does have an impact in chromosome conformation and segregation, as shown by Wang et al. (2014). Thus, I would be careful with conclusion that arm-alignment is not required for efficient translocation.

– Wang 2015, and Marbouty 2015 both showed that a single parS site display arm alignment. The authors cite only Wang 2017.
