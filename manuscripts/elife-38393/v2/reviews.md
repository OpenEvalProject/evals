# Peer review - Round 1

Editors:
- Hugo J Bellen, Baylor College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38393.016](https://doi.org/10.7554/eLife.38393.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Spatiotemporally controlled genetic perturbation for efficient large-scale studies of cell non-autonomous effects" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Hugo Bellen as the Reviewing Editor, and Didier Stainier as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Chris Doe (Reviewer #1); Marc Freeman (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript describes a genetic toolkit that can be used to generate a specific phenotype in a targeted patch of cells (which I will call the screening phenotype) while concurrently performing gene knock-down/misexpression in the adjacent cells to detect non-cell autonomous modification of the screening phenotype. The screening phenotype transgene is kept inactive until spatial and temporal cues lead to 'flip out' of stop codons, thereby allowing expression of the transgene and initiation of the screening phenotype.

Chai et al. describe this novel method for temporal and spatial control of genetic perturbation using two flip-out cassettes that can be regulated by different transgenes. The method only uses the FLP FRT system and leaves other genetic tools such as other binary expression systems free to use for further genetic manipulation of samples. The authors included a miRNA targeting GAL4 in their construct to silence GAL4 in the expression domain. This allows cell autonomous and non-cell autonomous effects to be separated. Moreover, all the components to induce the expression of the construct can be included in a single parental stock, enabling crossing a single stock to effectors such as RNAi libraries to conduct F1 screens. The authors generate multiple versions of this construct to knock down tumor suppressors and GAL4. They generated enhancer FLPase stocks that can be used for neuronal expression and optimized stop cassettes, flippase constructs and knock down constructs separately. Overall this is a sophisticated method that can address niche questions quite nicely. I believe the method will be very useful for the laboratories that aim to address such questions. This elegant system provides a new tool for Drosophila researchers interested in performing screens for non-cell autonomous functions. The idea and execution of this system are quite impressive, yet we have some concerns about the general utility of the system described below.

Essential revisions:

1) Using the system 'off the shelf' is a stated goal of the authors, and an admirable one. But the system is designed to create just one, very specific screening phenotype: neuroblast tumor formation. This is because the screening transgene has miR against prospero or brat only. Generating other screening phenotypes would require significant molecular genetics to adapt the system to create different phenotypes. As it stands, this tool is only useful for research into non-cell autonomous modifiers of neuroblast-derived tumors.

2) Using the system 'off the shelf' would also be limited to a single Gal4 line, named enhancer2-gal4, as described in Figure 1B. Subsequent figures show crosses to different Gal4 lines, but I don't understand how that works if the gal4 is part of the parental screening fly as shown in the schematic in Figure 1.

3) I have some concern about 'leaky' expression of the screening phenotype, due to unwanted FLP/mFLP5 recombination. The number of events per lineage is calculated, but since there are 100 neuroblasts and 1000 or more INPs in the brain, a low frequency per lineage may translate into an unacceptable level of events per brain. Could the authors give the tumor frequency per brain for each genotype?

4) Figure 2A should have a key for the colored boxes: what do each represent?

Also, in Figure 2 there is small number of green cells that can be seen in both FOFO1 and FOFO2 non heat shocked samples. These do not seem to cause a problem since tumors only form when pros or brat are removed in progenitors. For other applications this leakiness (which most likely results from heat shock promoters leakiness) can be problematic. This should be discussed and quantified.

5) The authors aim to obtain reproducibility of tumor induction but never really compare the tumors in different animals. Is the increase in number of NSC similar between samples induced the same way? How does it change when heat shock regime is changed? These should be quantified.

6) The temporal control of expression is inherently dependent on the expression dynamics of enhancers. Judging from Figure 4—figure supplement 1, almost all the enhancers that the authors use unlock the construct in a larger set of cells that end up expressing the enhancer at third instar (comparing enhancer-GAL4 Tub>Stop>GAL4, UAS-FLP mediated GFP expression to direct enhancer-GAL4 mediated expression). Therefore both the temporal control and special control is limited. The wording in the text should be toned down when it comes to spatial and temporal control of expression and caveats should be more clearly stated.

7) The heat shocks are conducted so early for tumorigenesis and conducting two heat shocks completely ablates the temporal control aspect in the experiments. Is this tumor induction method better/more robust than a single flip out regulated by enhancer specific Flp? A head to head comparison should be included.

8) The authors should deposit their plasmids in Addgene or BDGRC and explain how to expand applications for different applications by customizing their tools. They should also deposit their transgenic flies in the BDSC. They nowhere mention that they are planning or willing to do this. These reagents and stocks should be deposited before the paper is accepted or at the time the paper is going to press.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Spatiotemporally controlled genetic perturbation for efficient large-scale studies of cell non-autonomous effects" for further consideration at eLife. Your revised article has been favorably evaluated by three reviewers, Didier Stainier as the Senior Editor, and Hugo Bellen as the Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

One of the reviewers wrote the following:

The Abstract and end of the Introduction still makes it look like this method can be used "off the shelf" when in fact any different application from their example requires genome engineering to replace their example microRNAs with different microRNAs or misexpression ORFs. So I would like to see the Abstract changed from "Altogether, our design opens up efficient genome-wide screens on any deleterious phenotype." to "Altogether, our design opens up efficient genome-wide screens on any deleterious phenotype, once genome engineering is used to place the desired miRNA or ORF into our genotype."

We agree that this change should be implemented.

Also, we want to ensure that all the reagents will be available from the BDSC without MTA at publication time.
