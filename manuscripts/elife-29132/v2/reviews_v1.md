# Peer review - Round 1

Editors:
- Andrew J MacPherson, University of Bern Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29132.030](https://doi.org/10.7554/eLife.29132.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Bacterial colonization stimulates a complex physiological response in the immature human intestinal epithelium" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor. One of the reviewers, Emma Slack, has agreed to share her identity.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. There was consensus among the reviewers that your manuscript would be most appropriate, if adequately revised, for our Tools and Resources section.

Summary:

Human intestinal organoids (HIOs) were used to investigate host microbial interactions at the epithelial surface. Using live or dead Escherichia coli they report contact and hypoxia driven responses with antimicrobial peptide production, maturation of the mucus layer and improved paracellular barrier function. The paper represents a technical development of the HIO system, with findings that are aligned with interpretations from previous culture systems.

Essential revisions:

General comments on presentation in the paper

Especially for a paper where the main point is development of an experimental system, the technical validation and reporting of the methods and results in the paper must be completely solid. The reviewers noted missing information on the number of biological and technical repeats, concentrations of stimuli, number of injected bacteria from the figure legends. The Materials and methods section was considered incomplete to allow a researcher from a related field to exactly reproduce every experiment shown – concentrations, solvents and timings – e.g. Figure 7, how much TNF, how much IFNgamma? It was unclear exactly how the false discovery rate was assessed – which algorithm was used? What sample numbers were used in the calculations and how reproducible were the experiments? Specific information about the E. coli strain should be given, and whether it is motile.

The model depends on selective injection of live bacteria into HIOs and evidence is provided in Figure 1 about this. The experimental protocol needs to be far more explicit in the main body of the text: in the Materials and methods under 'HIO culture' it is stated 'HIOs were maintained in ENR media without antibiotics prior to microinjection experiments'; then under 'Microinjection', '…cultures were rinsed with PBS and treated with ENR media containing penicillin and streptomycin…'. Controls that assess the potential influence of carry-over of antibiotics of the readouts reported in Figure 1 are required.

Further issues on Figure 1

A) Figure 1B appears to be compromised by fixation and/or freezing artifacts.

B) In Figure 1C the y axis is labelled 24h δ CFU. Given that the scale becomes fractional, it seems likely that ratios rather than differences are being used.

C) What dose(s) of injections were used for 1D?

D) As a main panel of Figure 1E, showing two agar plates does not add much, especially when the legend does not give details of exactly when are how they were generated. Further, the final sentence of the third paragraph in subsection “HIOs can be stably associated with commensal E. coli” and the results quoted in the following paragraph after day 3 are contradictory. Controls are absolutely necessary to ensure that these findings are not simply due to antibiotic carry-over.

The transcriptomic approach does not capture all basic information about the system. Does the E. coli injection alter the size, morphology and longevity of the HIOs? Does it alter the rate of epithelial cell turnover (which could be easily tested by BrdU labeling, and would be predicted from e.g. Proc Natl Acad Sci U S A. 2011 Mar 15;108 Suppl 1:4570-7)? Does it alter the pattern of epithelial cell maturation, i.e. the fraction of mature paneth cells, goblet cells, enteroendocrine cells etc?

It is accepted that enteroids are 3 dimensional structures, and the study has been productive in the evaluation of stem cell dynamics and other tissue level events. However, organoids are not vascularized with a capillary network that generate O2 gradients in vivo, thus organism level physiological events such as hypoxia are difficult to address and these caveats must be included in the discussion

Using the pathway analysis from the GO and REACTOME databases limits the insight that the reader is given into the changes in gene expression. For example, in Figure 2C 'muscle cell differentiation' is shown as a pathway. It would be possible to report detailed network analyses at least in the supporting material so that the contribution of different transcripts to the overall analysis is clear. This would allow considerable refinement of the time-dependent transcriptional response descriptions in the text.

In Figure 3C it is difficult to appreciate whether the cadherin stain has worked in the PBS panel. How reproducible are these results? What happens with a hypoxic control?

The data analysis shown in Figure 4 was complex and challenging for the reviewers to appreciate in its current form. The subset organisation must be clear and specific.

A) Why is there no PBS control with the NFkB inhibitor? Many cell survival/cell death pathways converge on NFkB signalling and the inhibitor may exert effects already at baseline which would then fall into gene set 1 and gene set 2? From the Venn-diagrams shown in panel A, it appears that genes in set 1 and 2 are mutually exclusive, which would make the lacking control less problematic, but apparently the hypoxia-responsive genes are highly enriched in both (of course these may be different genes in the same pathway? But this would be slightly surprising if a statistical exclusion had been made).

B) For the discussion of the analysis, it appears that an assumption is made that the effect of live E. coli is identical to dead E. coli combined with hypoxia. There is a large body of literature on "vital PAMPs" (e.g. Nature. 2011 May 22;474(7351):385-9), which might suggest there is more to it. Nevertheless, there appears to be an excellent correlation between genes regulated by live and dead E. coli in the plots in Figure 4B. If the hypothesis is correct, then injecting dead E. coli and then immediately transferring the organoids to a hypoxic chamber should produce a gene-expression profile that correlates better that the dead E. coli alone. Noticeably the gradient of the correlation between hypoxia/PBS and live E. coli/PBS seems to be close to zero?

C) Is there some sort of statistical significance cut-off for the genes identified for each set in panel B? The clouds appear to very closely approach a log2-FC of zero, suggesting genes showing very small changes in expression are included? Would it be logical to show the data pre-filtered for p-value? Or show the limits of the region and color-code for p-value?

D) In panel C, is it right that "% genes matched to pathway" is this the percentage of genes from each set (e.g. the full 1940 genes in Set 1) that map to the indicated pathway? Thus 5%, i.e. around 400 genes from set 1 map to "regulation of cytoskeleton organization"? Please clarify. Also, as the plots in B suggest that many genes are included with a very small up- or down-regulation, it would be important to have some handle on not just the significance, but also the average absolute size of the change observed. A second set of graphs, or a supplementary figure with more information would be helpful.

E) In the legend, were pathways with enrichment P-values greater than 0.01 excluded?

In Figure 5B and C, it would be important to include a group microinjected with dead E. coli, immediately followed by hypoxia, to conclude that both factors act together to induce b-defensins. For Figure 5D, does hBD-2 require a reducing agent for activity as hBD1 does (Nature 469, 419-423)? Typically, these pore-forming AMPs to exert a stronger effect on the rapidly growing bacteria than in the stationary phase, and in fact, your maximum growth rate (i.e. maximum curve gradient) is even higher where the BD-2 is added, suggesting that something in the BD-2 may even permit faster E. coli growth in LB. Death over several hours in late stationary phase may be rather due to accumulation of a toxic metabolite. To control for these effects, it will be important to show growth data with heat-inactivation of the BD-2. To focus on killing in the stationary phase a late stationary-phase culture could be treated with differing concentrations of BD-2 over short time-courses (including the inactivated controls), measuring loss of membrane integrity by Sytox-green uptake by flow cytometry or microscopy. As O-antigens can inhibit AMP function, E. coli K-12 could be included in these experiments.

In relation to Figure 6, can induction of mucus production and induction of goblet cell differentiation be delineated? The slow appearance of mucin gene upregulation appears more consistent with a differentiation phenotype than simple gene expression?

The interpretation that 'Epithelial barrier integrity is enhanced following bacterial association' (p13) is rather at odds with the data in Figure 7 B and D where the PBS and E. coli treated permeability is the same. Is the meaning that NFkappaB signaling is required for the compensatory effects of the barrier in E. coli-treated organoids? What is the effect of the inhibitor alone?
