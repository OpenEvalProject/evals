# Peer review - Round 1

Editors:
- Jeremy Luban, University of Massachusetts Medical School United States

Reviewers:
- Gregory J Towers, University College London United Kingdom

## Review text

DOI: [10.7554/eLife.41431.025](https://doi.org/10.7554/eLife.41431.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Functional proteomic atlas of HIV infection in primary human CD4+ T cells" for consideration by eLife. Your article has been reviewed Wenhui Li as the Senior Editor, a Reviewing Editor, and three reviewers. The following individual involved in review of your submission has agreed to reveal his identity: Gregory J Towers (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

While there was discussion among the reviewers regarding the biological significance of your findings, all 3 were impressed with the magnitude of your data set using primary CD4+ T cells. They felt that it was technically innovative, that the mass spec data had depth and stringency, and that you have provided an easy-to-access resource for the community. We have therefore agreed in principle to go forward, potentially publishing your manuscript as a Tool and Resources paper rather than a Research Advance (https://submit.elifesciences.org/html/eLife_author_instructions.html#types).

"Tools and Resources articles do not have to report major new biological insights or mechanisms, but it must be clear that they will enable such advances to take place. Specifically, these contributions will be assessed in terms of their potential to facilitate experiments that address problems that to date have been very challenging or even intractable." (https://lens.elifesciences.org/07083/)

Please go through the specific comments of the reviewers below and send us a revised manuscript with itemized responses to each comment, and formatting with a eye towards publishing your manuscript as a Tool and Resource paper.

Reviewer #1:

Naamati and coworkers use a quantitative temporal proteomics approach to survey protein-level changes in primary CD4+ cells infected with HIV-1 plus/minus various accessory genes. This is the largest data set in using primary CD4+ T cells to-date and over half of the 600+ changes were dependent on Vpr and Vif/Nef/Vpu. This is a technically sound study and a potential resource for the community studying HIV/host interactions.

However, my main concern is novelty and overlap with prior and parallel work. For instance, an eLife paper a couple of years ago focused on Vif by the same group, a PLOS One paper focused on infected cell purification by the same group, and a sister paper (Greenwood, 2018) that describes the Vpr downregulated proteome. The authors indicate 40-60% Venn overlap with proteomic studies in CEM cells, and focus on novel cellular factors (ARID5A, PTPN22, DPH7, and FMR1) but the functional significance of these interactions is unclear.

Reviewer #2:

Naamati et al., present a strategy for isolating HIV-infected primary cells for mass spec analysis based on infecting cells with modified virus bearing a genetically-encoded surface protein with a strong affinity to streptavidin. This virus ("HIV-AFMACS") allows for one-step enrichment of infected cells using magnetic beads. The authors go on to show the utility of this strategy by measuring changes in cellular protein levels upon infection of primary cells with this construct at 24 and 48 hours post-infection, and by comparing changes in protein expression using WT and ΔVif viruses. The authors complete a thorough comparison of the resulting data in the context of previous studies in the literature. They also validate the changes in expression of two proteins that were specific to primary cells (as opposed to CEM-T4s) and two proteins that are potential new Vif substrates using immunoblot.

The paper is clearly written and presented, and its strengths include, in particular, (1) the technical innovation, (2) the emphasis on primary cells, and (3) the depth and stringency of the mass spec data obtained. Especially notable is the interactive spreadsheet that provides an easy-to-access and expansive resource.

Weaknesses of the study are, at a fundamental level, relatively minor. However, they are worth pondering in the context of the anticipated target audience.

First, it can be argued that there is not much new biological insight gleaned here, especially compared to the depth of the stories in these authors' other recent (Vif- and Vpu-focused) and concurrent (Vpr-focused) proteomics studies using CEMs. The major advance seems to be the technical achievement and comparison of primary T cells to cell lines, and while this is both compelling and innovative, there is rather limited validation of new or interesting hits and no characterization of why they (in particular the highlighted factors DPH7 and FMR1) are affected by HIV or the roles they might play in viral or cellular biology.

Second, it is unfortunate that ΔEnv viruses were chosen for the analysis considering the large impact Env-CD4/CoR binding can have on primary T cell responses, likely highly relevant to accurately modeling acute infection dynamics (e.g., see Wojcechowskyj et al., 2013). To their credit, the authors discuss the VSV-G issue (albeit briefly), saying that because of VSV-G they biased their focus to be on late stage accessory gene contributions (Discussion section). However, it seems reasonable that their viruses could have been pseudotyped with wild-type Envelope proteins instead of VSV-G. Indeed, again in the context of acute infection, it would have been even more compelling to compare R5 vs. X4 or TF to non-TF glycoproteins. Further discussion of this issue would be warranted.

Third, the authors did not include an evaluation of whether the expression of SBP-LNGFR and its display on the cell surface causes any changes in expression of cellular proteins, as an important negative control. Unless I missed it, the only cells that are expressing this protein are also infected with HIV, therefore it is not possible to fully distinguish which proteins are changing expression due to HIV infection or SBP-LNGFR expression alone. While the authors do discuss how their technique is superior to antibodies that might cross-link surface receptors, they should also explain the limitations of AFMACS-selection more thoroughly and whether or not the potential effects of LNGFR overexpression and bead binding can truly be disregarded.

Reviewer #3:

In this study Naamati and colleagues measure the proteomic changes experienced by T cells after HIV infection. The study is compelling, appropriately controlled and the results are of significant interest to the community. I have some minor suggestions to improve clarity.

1) The authors make a lot of the MOI being low. Do they know that this is true? Permissivity is typically different between donors/experiments but typically one cannot infect all the cells, especially for primary T cells, even by spinoculation with VSV-G. In the case that only 40% of the cells are permissive an MOI of 50 would only infect 40% of the cells. In order to determine actual MOI one has to titrate the virus back to make sure that eg halving the dose halves the number of infected cells. In the experiments presented, do the authors know that reducing dose reduces infectivity or is their MOI of 0.5 really just an indication that only half of the cells are permissive. Did they test whether lower dose give predictably lower numbers of infected cells? This is important because it also speaks to whether the only difference between the infected and uninfected cells is chance, ie there is not enough virus to infect all the cells, or are the uninfected cells non permissive. In this case, gene expression differences between uninfected and infected cells may be as much to do with the cells being different as it is to do with viral gene expression. I think the experiments are OK and this has been taken into account but a more explicit discussion of this point and whether diluting the virus reduces infectivity as expected is important.

2) A key goal of this study is to provide a resource for examining which proteins are manipulated by HIV infection. With this in mind, could the authors annotate the data in Figure 3C with more detail. Each outlier circle could be numbered and a table of gene names provided. I appreciate that the authors are presenting all of their data and are not hiding anything. But I feel the outliers are what people really want to know about and these could be labeled here. In fact, any opportunity to label the volcano plots would enormously improve the accessibility and thus the likelihood that the field will chase these hits up mechanistically.

3) It’s not immediately obvious what "pos" and "neg" mean in Figure 2A. For clarity, label "HIV+" and "HIV-" instead and change the text in subsection “Time-dependent proteomic remodelling during HIV infection of primary T cells” to "whole cell lystates from both HIV positive and HIV negative populations using.….

4) Provide key for blue and red lines in Figure 2C-E on Figure and in legend.

5) Subsection “Design and construction of the HIV-AFMACS reporter virus” submit the sequence of the construct to GenBank and provide accession number which is more useful than having the seq in a Figure.

6) Subsection “Proteins and pathways regulated by HIV in primary T cells from multiple donors”, its useful to label the x for the constructs that didn't work. Knowing what didn't work is useful, particularly for those that were completely dead vs a bit defective. Figure 1—figure supplement 1B.

7) Can the authors comment on the impact of T cell activation of HIV permissivity. It’s not totally clear why T cells have to be activated to make them permissive for HIV infection. SAMHD1 has a lot to do with it and the authors make this point. In these experiments T cell receptor is crosslinked with anti-CD3, anti-CD28 dyna beads. This presumably doesn't happen in vivo, yet T cells are permissive. I imagine the authors have thought about this and I would be interested to hear their thoughts, perhaps in the Discussion section. Is there value in their data comparing unactivated and activated cells to consider what's driving permissivity? How do their data compare with any published literature on in vivo activated T cells, indeed is there any data on this? I'm interested to hear what they think and whether they think their data can be used to illuminate the changes that occur on TCR cross linking that drive permissivity. Would a figure considering this point be valuable?
