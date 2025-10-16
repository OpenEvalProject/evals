# Peer review - Round 1

Editors:
- Oliver Hobert, Howard Hughes Medical Institute, Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53986.sa1](https://doi.org/10.7554/eLife.53986.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Slo2 potassium channel function depends on a SCYL1 protein" for consideration by eLife. Your article has been reviewed by Richard Aldrich as the Senior Editor, a Reviewing Editor (Oliver Hobert), and two reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Leonard Kaczmarek (Reviewer #1); Thomas Boulin (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. As you will see in the reviews below, there is general agreement about the general interest and importance of the study. However, a set of important clarifications and experiments need to be conducted to make this paper become acceptable for publication in eLife.

In brief, the requested experiments are:

1) Independent validation of interactions (reviewer #1, comment 2)

2) Engineering the A>G mutation into the genome (reviewer #2)

3) Improved expression pattern analysis (reviewer #2)(the in vivo recombineering technique has by now been shown to be inadequate).

There are also a number of very important clarifications that are required (e.g. reviewer #1, comment 1)

Reviewer #1:

This manuscript presents some very interesting work demonstrating that Slo2 channels in C-elegans interact with SYCL-1 to alter open probability of these channels. The effects of SYCL-1 on the channels is, in turn, influenced by ADR-2, which is required for A-to-I RNA editing of a site in the 3' UTR of the scyl-1 gene. The work is provocative and points the way to future work to unravel how this potential interaction affects the biology of neurons in the nematode and in mammalian systems.

1) My major comment is on the work that extrapolates the nematode findings to the human Slack channel. The latter has previously been shows to differ from the C-elegans channel in several ways. This interaction with the human channel is an important aspect of the presented work. Examination of the data in Figure 11, however, suggest that the gating of the human channel is quite different from the Slo2 channel records shown in Figure 8. Specifically (if the time bars shown in Figure 11A are correct, the overall open probability of the human channel is dominated by the presence of very long closed states (lasting many seconds). Examination of the X-axis scale bars in Figure 11B and C suggest these may have been excluded from the analyses. The conclusions on the effects of SCYL1 on open probability stated in the last paragraph of the Results section may not be completely valid until these are taken into account.

2) The bimolecular fluorescence complementation assay presented does make a case that there may be a physical interaction of SCLY-1 with SLO-2 but is not completely definitive. It would be good to have some other indicator of physical interaction to support this claim. A more conventional coimmunoprecipitation experiments would be a good addition, one that could perhaps be carried out using the co-expression Xenopus oocyte heterologous expression system.

Reviewer #2:

In this study Niu et al., describe a striking and entirely unsuspected regulatory cascade that controls SLO-2/Slo2 potassium channel activity. They report the role of SYCL-1, a novel physical interactor of the SLO-2 potassium channel, and describe how syCl-1 expression is controled by ADAR-dependent RNA editing in the non-coding sequence this gene. After dissecting this mechanism in worms, they proceed to directly demonstrate the conservation of this novel regulatory interaction with the human SLO-2 ortholog. Given the importance of this class of potassium channel in health and disease, identifying this modulatory mechanism is a very important finding in my opinion.

Essentiaol revisions:

- Please clarify the functional relationship between adr-1 and adr-2. Indeed, in the Introduction the authors seem to indicate that ADAR proteins could compete ("altering the accessibility") for certain binding sites. In this model, wouldn't one expect that adr-1(lf) would "free" access to the scyl-1 site, which would be inconsistent with the similarity of adr-1 and adr-2 mutant phenotypes?

Do the authors think that ADR-1 promotes the recruitement of ADR-2 to the scyl-1 3'UTR?

- I was very intrigued by the results described in Figure 10, and specifically Figure 10D/E. The result is not what I had intuitively expected. Since it was performed in an adr-1/2 wild-type background as far as I could determine from the Materials and methods section, I would have thought that ADAR activity would have edited the wild-type sequence and I would have expected to see GFP in both cases.

I would have performed this experiment in an adr-1(lf) background. Have the authors attempted this experiment in this background? How many independent lines were tested with the wp1923 construct? Is expression seen anywhere else in the nervous system (outside de VNC) to make sure that GFP can indeed be expressed from this transgene?

- Following on this previous point, a direct way to demonstrate the functional importance of this editing site would be to generate the following genotype by engineering the A>G mutation by CRISPR/Cas9 gene editing:slo-2(gf); adr-1(0); scyl-1(A>G)

My prediction would be that the mutation in scyl-1 would restore the slo-2 gain-of-function locomotor impairement, by bypassing the adr-1 requirement. To me this experiment would very strongly support this new and exciting functional regulation and I would encourage the authors to perform this rather simple experiment.

- In wormbase, the annotation of the scyl-1 locus shows a rather sizable 3'UTR. I was curious whether the authors have any comments on that point, and whether this is a common feature of ADAR-edited 3'UTRs.

Does the human SCYL1 3'UTR have a similar hair-pin structure, which could suggest a similar regulation mechanism?

- I was a bit surprised about the strategy used to generate the scyl-1 expression pattern. Why was the in vivo recombination approach used? What happens when the 0.5kb promoter-GFP construct is injected alone?

The previous gene is only approx 2kb upstream and there is significant sequence conservation to C. remanei and C. briggsae DNA less than 1kb upstream of the ATG (see UCSC genome browser for example). Did the authors test such a 2kb promoter fragment?

- Figure 6: I'm not convinced that scyl-1::GFP labels vm1 or vm2 muscles based on this image. I could be wrong, but higher magnification images would need to be checked.
