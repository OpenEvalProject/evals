# Peer review - Round 1

Editors:
- Kristin Scott, University of California, Berkeley, Berkeley , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22279.021](https://doi.org/10.7554/eLife.22279.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "FlpStop: a tool for conditional gene control in Drosophila" for consideration by eLife. Your article has been favorably evaluated by K VijayRaghavan as the Senior Editor and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript by Fisher et al. presents a new method ("FLP-Stop") that uses FLP-mediated recombination to accomplish post-mitotic disruption of targeted genes in cell types of interest in Drosophila. The authors generate a FRT-stop-FRT cassette with a red reporter that integrates into existing MiMIC sites in the genome to allow FLP-mediated gene disruption (or rescue) and labeling of mutant cells. The manuscript assesses the effectiveness of this approach and performs a number of critical validation experiments.

The manuscript is well-written and generally easy to read. The method is ingenious, and has the potential to be a very useful technique for scientists working in Drosophila – particularly in the neurosciences. One area in which the manuscript could be improved is by providing a more systematic assessment of the efficiency of Flp-mediated conversion and discussion of FlpStop's disadvantages as well as its advantages.

Essential revisions:

1) Why do the three of the seven genes targeted not generate null alleles? This is an important point for expanded discussion and hints at limitations of the approach. Is there anything in the insert location in ChAt that may suggest why disruption did not work? Was the insert incapable of flipping (testable by expression of tdTomato) or simply skipped? A better understanding of why the approach did not work in some cases may allow one to produce better reagents for new genes of interest.

2) Quantitative assessment of the efficiency of Flp for the examples of FlpStop usage discussed in the manuscript would be useful and this data should be included either in the text or in a table. The "flipping" frequency across loci is not well documented and seems variable (Figure 5). The authors report ~80% of red-green cells using cacFLPstop and M1-Gal4, is this number a function of the locus or of the GAL4/FLP combination? What is the frequency for other loci using the same Gal4/FLP combo and for the same locus using different Gal4s? (There is a hint of this answer in the legend of Figure 5—figure supplement 1; this should be addressed head on and quantified). Moreover, Figure 5 panel B seems to show quite a good number of cells that are green but not red and possibly a number of cells that are red but not green (e.g. in the calyx). How is this second population explained? This figure will benefit from higher resolution images and better quantification.

3) The advantages and disadvantages of FlpStop should be thoroughly discussed. With regard to the utility of the FlpStop toolkit to a potential end-user: a clear constraint is its dependence on the MiMIC insertion lines. The authors assert that MiMIC insertions "allow access to the coding introns of approximately 46% of neuronal genes" (subsection “FlpStop enables a diversity of applications”, first paragraph) and that "FlpStop alleles can be created that target any desired genomic locus using CRISPR/Cas9." The first statement seems likely to be a serious overestimate (using the authors methodology, I come up with MIMIC insertions into 23% of "neuronal genes"). While the second assertion is true, it would be more compelling if the manuscript presented and validated a FlpStop construct that was CRISPR/Cas ready if such a reagent has been made. The need for a null allele for all non-X-linked genes should also be addressed. The general possibility of using the FlpStopD insertion itself is not discussed, but has the obvious disadvantage of unveiling second site mutations on the same chromosome. What other general strategies (e.g. deficiencies) exist, and how useful might they be?

4) Subsection “FlpStop can produce conditional null alleles”. This section demonstrates at length that the FlpStop cassettes can do what MiMIC cassettes have already been shown to do – namely disrupt gene expression. While it is necessary to show that FlpStop works, this information would be of greater interest if it compared the efficacy of gene disruption using FlpStop with that of a MiMIC insertion in the disrupting orientation. One design difference between the MiMIC and FlpStop constructs is that the latter has transcriptional terminators, and it would be interesting to know if they are actually useful (i.e. do FlpStopDs reduce transcript levels more than the original MiMICs, when the latter are in a disrupting orientation?)
