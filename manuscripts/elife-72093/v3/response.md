# Author response - Round 1

Authors:
- Keith F DeLuca
- Jeanne E Mick
- Amy H Ide
- Wanessa C Lima
- Lori Sherman
- Kristin L Schaller
- Steven M Anderson
- Ning Zhao ([ORCID: 0000-0001-7092-6229](https://orcid.org/0000-0001-7092-6229))
- Timothy J Stasevich
- Dileep Varma
- Jakob Nilsson ([ORCID: 0000-0003-4100-1125](https://orcid.org/0000-0003-4100-1125))
- Jennifer G DeLuca ([ORCID: 0000-0002-3598-1721](https://orcid.org/0000-0002-3598-1721))

## Response text

DOI: [10.7554/eLife.72093.sa2](https://doi.org/10.7554/eLife.72093.sa2)

Essential revisions:

All reviewers found the tools you developed highly valuable, and the experiments well-conducted and clearly described. A few suggestions for improvements were made:

1) A systematic comparison of the recombinant antibodies to the previously available antibody preparations for these particular antibodies would be useful (Figure 1 and 2). Is there any difference in sensitivity or specificity?

We have now carried out comparison immunofluorescence studies using the same concentrations of the original, traditionally-generated antibodies and all of our full-length bivalent recombinant antibodies. The data are now included as supplemental figures to Figures 1, 2, and 3. [We also note that the original Figure 2 has now been split into Figures 2 and 3.] In brief, the quantification reveals that the recombinant antibodies to Hec1, KNL1 pMELT, Mad2-C, and BubR1 were moderately more sensitive than the original antibodies, and the recombinant antibody to CENP-C exhibited similar sensitivity.

2) The Hec1 scFvC and Fab-Alexa 647 fragments also label the spindle, which is not seen with the rMAb. Do you have an explanation for this? Please discuss the differences more explicitly. A double-staining with the full-length antibodies for direct comparison could be useful.

The differences between the spindle hosphor noted by the reviewer are likely due to differences in final cellular concentrations of the antibodies, which are variable based on the delivery system. As has been noted by others in the field, using high concentrations of antibodies to Hec1 lead to increased centrosome and spindle staining. Although we can use a given antibody concentration for each experiment, applying the antibody through different methods (indirect immunofluorescence, bead-loading, genetic expression, etc.) inevitably results in different final intracellular concentrations. In the future, we and other labs could titer the concentration for whichever method is used for antibody delivery.

3) Please include additional controls for the specificity and sensitivity of the recombinant antibodies. For example:

Figure 1E: Please include the RNAi control for the immunostaining.

We have added the requested control for the Hec1 immunostaining/RNAi experiment, which is now included in Figure 1. We additionally added a similar control for the CENP-C antibody using CENPC siRNA-treated cells (included in Figure 2).

Figure 1C: The rMAb-pMELT was used to detect an exogenously expressed KNL1 fragment.

Does the antibody recognize the endogenous protein on an immunoblot?

We found that both the original, traditionally-generated antibody and our recombinant derivative of this antibody do not work well for Western blotting using whole cell extracts. We therefore overexpressed a fragment of KNL1 in the cells prior to generating lysates.

Figure 2G: The 3F3/2 epitope has been proposed to depend on Plk1, and the antibody has been suspected to recognize BubR1. Does the signal change after Plk1 inhibition? Is the signal reduced in BubR1 RNAi? Does the recombinant antibody detect any band(s) on an immunoblot?

We have removed the 3F3/2 antibody from the current study for the following reasons (this is also related to point #7).

For all the antibodies in our study, each performed consistently throughout purification, concentration, freezing/thawing, with the exception of the 3F3/2 antibody. For reasons that are not yet clear, the yields and performance of this antibody were inconsistent. In some cases, the HEK293 Expi293F cell supernatant tested positive for the antibody at kinetochores, and then after either concentration or purification (or freeze/thaw), the antibody was not recoverable or was extremely low in yield. In other cases, the HEK293 Expi293F cell supernatant did not yield viable antibody. We have been systematically attempting to determine why this one antibody is inconsistent, but we have not been able to determine the cause. We are working towards this interesting question with a multi-pronged approach. For example, we are analyzing the sequences of all antibodies to determine if there are notable differences. In addition, we are systematically grafting different domains of the 3F3/2 antibody onto other antibody scaffolds. Given the above issues we have had with this antibody, we have chosen to remove it from the paper. Once we determine the source of the variability, we hope to share this information with the field in a followup study (see point #7). Finally, Dr. Gary Gorbsky has suggested that we remove his name from the author list since we are no longer using the 3F3/2 antibody. We plan to work with Gary in the future on the 3F3/2 antibody optimization.

Figure 4F: A larger field of view, or a quantification that represents more cells than just one, would be yet more convincing.

We have now included additional examples of both live- and fixed cell images of cells expressing the pMELT scFv. These are now included in new Figure 5 —figure supplement 1.

4) For primary antibody dilutions (e.g. lines 613-615), it would be more appropriate to give the final concentration rather than the dilution.

We completely agree with the reviewers and have made this change.

5) The strategy for Fab purification was confusing to the reviewers (lines 333-334). Cleavage by papain is followed by purification of the Fab fragment with Protein A. Protein A is more typically known to bind the Fc region. Does it bind the Fab and allow purification? Or was the Fc region depleted by Protein A?

We apologize for the unclear description. This has been modified in the text to: “The purified rMAbHec1ms antibody was enzymatically digested with papain protease, the digestion reaction was centrifuged through a Protein A spin column, and the antigen binding fragments (Fab), which do not bind the Protein A resin, were collected in the flow through.”

6) Please mention if the expression plasmids generated in this study will be made available to the scientific community and on what terms.

We have included this information in the legend for Table 2, which describes each plasmid (original Table 1).

7) Line 400, problems with yield: It was not entirely clear whether the yield can vary for one reagent, or only varies between reagents. It would be useful to add a table with the yields obtained for the different reagents, which would allow other researchers to know which preparations would need to be scaled-up to obtain the desired amounts of recombinant antibody.

We agree with the reviewer and have now included this information in a Table (new Table 1). We are also working to try to understand why different recombinant antibodies produce varying yields. Once we determine the source of the variability, we hope to share this information with the field in a follow-up study.

8) Line 190: It does not seem entirely accurate to say that closed Mad2 is “competent to assemble into active … MCCs”. Closed Mad2 is found in active MCCs (or bound to Mad1), but empty closed Mad2 is probably not capable of binding full-length Cdc20 and forming the MCC (Piano et al., Science 2021). Prior experiments that seemed to support this idea were done with a Cdc20 peptide.

The original text was replaced with: “the active form of the kinetochore-associated and spindle assembly checkpoint protein Mad2, which recognize the “closed” conformation of Mad2 molecules that are found in Mitotic Checkpoint Complexes or bound to Mad1 (Sedgwick et al., 2016; De Antoni et al., 2005; Mapelli et al., 2007).”

9) Some of the discussion repeats statements that were already made in the Results section. Shortening or deleting these sections (in particular around line 436 – 461 and 473-481) would improve readability.

In the Results section, we have removed or shortened the more “discussion”-type statements.

In contrast, other aspects could be added in the discussion. For example:

– In case scientists would like to apply the described approach to their favorite commercial antibody, do they have to expect legal objections from the company?

We have included a statement in the discussion indicating that researchers who choose to do this should make sure to consider the “Terms and Conditions” statements from the antibody companies, as they vary. Most indicate that antibodies cannot be reverse-engineered or altered for commercial purposes, but such modifications are not typically prohibited in cases of non-commercial research. The statement added is, “…it is important to consider downstream usage of data generated from antibodies purchased from commercial sources, as different companies may have unique sets of Terms and Conditions.”

– A premise of the article is to combat irreproducibility. But giving out the antibody sequences to everyone to express in their labs seems like it will undoubtedly lead to reproducibility issues as well. Antibody production, purification, and QC are not necessarily trivial. There is ample opportunity to swap plasmids and obtain antibodies different from the “label”. These types of issues are often challenging to identify and correct unless careful QC is being performed. The best solution is to have systems to prevent these types of swaps, but that takes a well-thought-out and careful strategy. Do you have suggestions how individual labs could cope with these challenges?

We have added the following sentence to the discussion: “We note that while an advantage of using recombinant antibodies such as those described in this study is increased reproducibility, it is important that, as with any recombinant DNA-based reagents, plasmids are routinely sequenced for quality control.”
