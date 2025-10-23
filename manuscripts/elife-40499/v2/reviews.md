# Peer review - Round 1

Editors:
- Michael A Marletta, University of California, Berkeley United States

Reviewers:
- Toby Gibson, European Molecular Biology Laboratory Germany

## Review text

DOI: [10.7554/eLife.40499.085](https://doi.org/10.7554/eLife.40499.085)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Quantitative mapping of protein-peptide affinity landscapes using spectrally encoded beads" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Toby Gibson (Reviewer #2).

Our decision has been reached after consultation within the editorial board. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. In particular, there was uniform agreement that the issues raised by reviewer 1 are highly unlikely to be addressed in revision.

Reviewer #1:

In this study, the authors present a new technique to measure the affinity of protein-peptide interaction in parallel. They apply their method to the well-known Calcineurin-PxIxIT interaction, obtain more data on this interaction, and use it to identify high-affinity peptides. They validate some of these peptides in a cell-based assay.

This work is based around the bead-encoded peptide-synthesis and subsequent affinity measurements using the spectral encoding. This all strikes me as technically state-of-the-art and quite elegant. However, from the paper as written, it is a bit difficult to get a true sense of the advantages of the new method over existing ones, and no direct comparison is attempted in the manuscript. For instance, mapping of the affinities of substitutions (as in Figure 4) surely would be possible using SPOT (to a slightly different degree, also using Phage). The shown r2 of 0.68 is pretty good, but not all that much higher than what has been claimed for SPOT (though a little higher than for phage – see e.g., Ivarsson et al., where, of course, a much higher number of peptides is measured). One should also note that this is for the same protein – incidentally, modern computational methods (such as alchemy-based ones, e.g., TI or CGI) achieve these sort of correlations, and usually perform better than rosetta. As high-quality structures are available, they would be applicable in this case, and may perform similar to the new bead-based method.

Similar things hold for the high-affinity variants obtained here (Figure 5 or later). While obtaining low-nanomolar binding peptides is really quite good, this domain is (as the authors themselves state) what phage display really is optimized for. While their new method can incorporate non-canonical amino acids, that is similarly true of novel synthetic library methods as what recently came out of the Pentelute lab.

Finally, while the authors seem to emphasize ability to detect "weak" affinities, I only see convincing data for affinities of up to maybe 50uM, which is all still detectable using techniques such as AP-MS or phage.

I should note that I do not really want to sound too negative. I see a new technique that brings substantial technical innovation that could be very exciting in this field. However, I find it difficult to ascertain its advantages over the variety of existing methods in the manuscript as presented. I would strongly suggest to include more direct comparisons with existing methods (such as SPOT, ProP-PD, hold-up, etc.) as well a more detailed discussion thereof.

A few additional points:

1) The authors state "CN binds PxIxIT peptides with weak affinities.… estimates for known substrates have varied over a wide range.…". These statements are somewhat contradictory in itself and, in any case, the affinities listed in Figure 2A seem to be all in the single digit uM, which is neither a wide range, nor particularly weak (roughly the expected range for domain-motif interactions).

2) Given the relatively length of the current paper, it would be good scholarship to discuss existing methods (including the variety of phage-display approaches, SPOT arrays and the recently developed holdup assay) – currently, this all happens in part of a single paragraph, with some of the methods I point out above not even mentioned.

3) In a similar vein, the citations (or lack thereof) are a bit puzzling. A 12-year old paper (Neduva and Russell) is cited regarding motif-interactions in Y2H/AP-MS, when most of the relevant work was published in the last decade. For Proteomic phage display, only a review paper is cited.

Reviewer #2:

This paper introduces MRBLE-pep, a medium-scale throughput protein-peptide affinity tool and applies it to calcineurin and variants of the PxIxIT docking motif. Using MRBLEs – colour-coded microbeads, each position in the original peptide can be substituted with all other amino acids. Systematic evaluation of binding determinants can then be rapidly determined using small amounts of reagents. Efficient methods for examining SLiM specificities are vey much needed given the abundance of protein:motif interactions in cell regulation and therefore MRBLE could see widespread adoption. Although the PxIxIT motif is well known from several calcineurin substrates, there has been uncertainty regarding the motif specificity determinants as well as the cooperative involvement of the second LxVP docking motif.

Weight matrices (PSSMs/HMMs) are often used to represent SLiMs in sequence searches but assume that each position in the sequence can be treated independently of the others. Regular expressions are also in widespread use but are overdetermined and insufficiently flexible regarding sequence space. The results here can be used to improve bioinformatic PxIxIT detection in candidate substrate proteins. However, the results also emphasise that positions in the PxIxIT motif are not independent and also that flanking residues affect the binding affinity (which has been seen for a number of other linear motifs too). The data from MRBLE-pep could allow a different computational approach whereby candidate motifs in protein sequences could be compared to and ranked by the total landscape affinity data.

No substantive concerns were identified.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Quantitative mapping of protein-peptide affinity landscapes using spectrally encoded beads" for further consideration at eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below in the first review below. Normally, we try to avoid second revisions, but we feel reviewer #1's comments should be addressed and we hope you will be able to do this easily and quickly.

Reviewer #1:

Essentially, the revisions by the authors haven't changed my opinions drastically. I still see this is as an innovative technology that will likely be of interest; however, the paper is still hampered by some shortcomings that I think could be improved pretty easily. In a way I find it a bit frustrating that the authors choose to write a full two pages of rebuttal to a simple point (correlations to measured affinity - compare these R2s between SPOT and MRBLE-pep) when they could have simply provided two numbers. Also, little of these two pages of rebuttal seems to have made it to the text (or was in there to begin with). Why not provide some kind of comparison of correlation to measured affinity to SPOT in the paper? I'm reasonably certain MRBLE-pep would come out on top.

Similarly, the authors add calculations using FoldX (that I didn't ask for). Not sure why they include comparisons of FoldX to Rosetta in the main text/figure (these would be of interest in computational papers and indeed have been done a bit, but I doubt the main readership of this paper will be interested). Also, I find it a bit frustrating that while they added a many new figures, the one figure that I think would have added to the paper (again a simple direct comparison of ddGs derived from MRBLE-pep to ones derived from rosetta OR FoldX vs. measured ddGs, i.e. combining the panels of Figure 4—figure supplement 4 into one panel and comparing it to the appropriate one for MRLBLE-pep). It's fine if the authors don't want to do any TI/FEP calculations (again, this isn't a computational paper), though if they do want to make the point that FoldX/Rosetta don't perform well on solvent exposed residues (not surprising), they should also mention that this is something that TI/FEP would, at least in theory, do better at.

They did add a much more appropriate introduction with discussion of the literature.

Reviewer #2:

The original MRBLE-pep manuscript was rather let down by superficial treatment of other PPI methods and how MARBL-pep compares to them. The resubmitted manuscript is greatly improved in this regard. This is important because SLiM researchers need to be able to understand which methods are suitable for the projects they have in mind. These range from the low throughput "gold standard" ITC up to whole proteome screens of the "disorderome" with phage display to identify novel SLiM candidates. I believe that MARBL-pep will see significant adoption and will help to define many SLiM motif patterns. The data obtained for the chosen target, the Calcineurin-binding PxIxIT motif, will hopefully now be applied in the identification of novel substrates for this medically important phosphatase. I have no further concerns.
