# Peer review - Round 1

Editors:
- Andrew B West, https://ror.org/00py81415 Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70921.sa0](https://doi.org/10.7554/eLife.70921.sa0)

In this work, the authors provide a useful compendium of proteins labeled within dopaminergic cells using a novel approach. Novel viral approaches were developed to rapidly biotinylate proteins in dopaminergic neurons in oriented sections of brain whereby circuits can be spatially parsed for proteomic dissection. In addition to providing a useful new database of proteins for investigators interested in this circuit, the results also provide a more general approach to examining a compartment proteome in neurons and what might be expected in that analysis in an unbiased way not previously envisaged.


---

# Peer review - Round 1

Editors:
- Andrew B West, https://ror.org/00py81415 Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70921.sa1](https://doi.org/10.7554/eLife.70921.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Subcellular proteomics of dopamine neurons in the mouse brain reveals axonal enrichment of proteins encoded by Parkinson's disease-linked genes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Gary Westbrook as the Senior Editor. The reviewers have opted to remain anonymous. The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) All reviewers and the Reviewing editor agreed that additional protein validation is needed, potentially with orthogonal antibody staining approaches. While the synaptosome preps presented are supportive of the BioIDs, and may facilitate candidate selection, the synaptosome preps do not obviate the need for an orthogonal approach. In protein validation, the target could be evaluated in other circuits as well which would help provide insight into how unique the localization in the dopaminergic neurons really is compared to other types of neurons.

2) All reviewers and the Reviewing editor were confused by the steps taken by the authors to normalize the data. Two of the reviewer's thought that it is critical to normalize the abundance of biotinylated proteins from one lysate to the next to the amount of APEX2 enzyme present in the lysate, or provide a justification of why more peroxidase expression would not be expected to label more distinct protein substrates and label protein substrates to a higher level? Normalization methods of all mass spectrometry data should be included briefly in all relevant figure legends, as well as a clear work-flow in the Methods section.

3) Two reviewers thought the comparative analysis of the PD GWAS data with the proteome IDs was imprecise at best, and potentially misleading. Some specific concerns include the conflation of strong recessive, dominant, and risk factor variants with potentially incorrect gene assignments, arbitrary inclusion of some genes and not others, overly relaxed false-discovery rates, and heavy implicit bias. All reviewers and Reviewing Editor agreed that the manuscript would be more focused without these experiments and the related claims about the heritable aspects of PD and PD-associated diseases.

Reviewer #1 (Recommendations for the authors):

The following suggestions for improvement are provided per figure for clarity, although some may be relevant more globally;

Figure 1 is generally showing that the technique works in vivo and is good. One small question is with 1d, where it appears that the V5APEX2 expression is higher in the striatum than in midbrain. Was this consistently seen and might it influence detection sensitivity later in the paper? It would be important to add a reference protein for loading to 1d and quantify relative expression in the two regions.

Figure 2 is the main results figure and again largely makes sense. Here, I would again like to see an evaluation of the amount of V5-APEX2 in each region relative to control, so we can understand the apparent discrepancy between number of proteins detected and % biotinylation between ventral midbrain and striatum. It is notable here that the control is different from figure 1, which was -H2O2, vs no APEX2. It would therefore be important to include validation experiments using immunoblotting and also include the controls from figure 1 to be sure that these are dependent on APEX2 activity.

Figure 3 is generally fine apart from the discrepancy in FDR p values selected for cutoffs. FDR<0.15 is too liberal, especially given that log fold cutoffs appear not to have been applied and that t-tests were used without evaluation of normal distributions that would be difficult from low n of samples. Again some validation of key results is needed.

Figure 4 particularly needs validation of proteins that are expected to be post-synaptic. I am sure that the literature distinctions between pre and post synaptic are less rigid than might be inferred, but some evaluation of accuracy of this separation is needed.

Figure 5 is the figure that has most problems. Figure 5a is a schematic and 5b tells us that there is partial agreement between proteome and scRNA-seq, which is to be expected. But, 5c, has little informational quality for multiple reasons. For GWAS SNPS, the selection of nearest gene to lead SNP is only true in some uncertain proportion of loci so whether INPP5F is the gene at the Chr10 locus that includes BAG3 and RGS10 is impossible to evaluate. For the smaller set of Mendelian loci, whether we should combine PD and atypical and dystonia is hard to evaluate. At the same time, there are multiple loci that are not in this set – LRRK2 and GBA being very obvious. So at best, this dataset says that some PD genes are in dopamine neurons, which is unsurprising, but not all PD genes are dopamine neuronal. The real problem here is in decision of numerator and denominator. For other tools more widely used in GWAS (FUMA, MAGMA etc) the test set is all candidate genes vs all expressed in a given cell type. Here, the authors compare a set they detect in the cells and then look for cell body vs axon enrichment, which is fundamentally less precise or informative. Authors should look for enrichment within each dataset for all Mendelian PD genes or all GWAs hits, which should include all reasonable candidates within LD-defined bounds of each locus. Even if this turns out to be more than chance, the authors must discuss limitations – DJ-1 is found here but very notably not PINK1/parkin. Such patterns might easily be explained by chance ordering of proteins in Str vs VM and should be discussed adequately.

Reviewer #2 (Recommendations for the authors):

1. When doing streptavidin-dependent pulldowns of biotinylated proteins the authors write 'immunoprecipitation'. This is not correct since no antibodies are used. The authors should be technically correct and talk about 'pull-downs' or 'streptavidin-dependent purification of biotinylated proteins.' I realize most readers will understand what they are trying to say, but for such a technically excellent paper I think the authors shouldn't use wrong terminology.

2. In some instances I found the figures to be overly 'busy'. For example, Figure 3d is very busy with a great deal of speculation included about protein function. No studies here actually test biology of the candidates identified by mass spectrometry. The faith (and I label it as such) placed in GO analysis by the authors is not justified. On the other hand, I applaud the authors for attempting to place some of the identified proteins in biological context. What I'd prefer to see is a bit of a disclaimer about the robustness of GO analysis and also include more statements about how this is a discovery approach that will require many follow-up studies to elucidate protein function.

Reviewer #3 (Recommendations for the authors):

The compendium seems rigorous and potentially useful to the field in understanding TH neurons in the SNpc.

1. I do not understand why biotinlyated protein abundance in the different preparations from the different compartments are not normalized to APEX2 abundance in the relative quantifications. Overall, the process of normalization was unclear, including how differing AAV transduction efficiency is factored into calculated biotinylated proteins. Unless i am fundamentally mistaken, APEX2 labeling occurs so quickly that the relative abundance of enzyme will influence not only the number of proteins that the mass spectrometry analysis can identify, but also the relative abundance when comparing one preparation of protein to the next.

2. Along those lines, since there are simply more proteins IDed in the striatum, with a larger 'interactome' afforded by more substrate material, and with higher possible proportional abundance of APEX2 , it makes sense that there are more PD- GWAS genes identified in the striatal lysates. Would the same be true for any compendium of neuronal genes?

3. Along those lines, are the 'novel' post-synaptic and other proteins identified in the striatum something that is unique to SNpc cells, or present in other subsets of neurons. The implication of involvement in PD seems overly speculative without real support.

4. Beyond the proteomic IDs, orthogonal methods of detecting some of the non-expected post-synaptic proteins in the striatum are mandatory for interpreting the validity of the IDs.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Subcellular proteomics of dopamine neurons in the mouse brain reveals axonal enrichment of proteins encoded by Parkinson's disease-linked genes" for further consideration by eLife. Your revised article has been reviewed by 2 peer reviewers and the evaluation has been overseen by Gary Westbrook as the Senior Editor and a Reviewing Editor. The consensus discussion of the reviewers and editors is summarized below. We will look forward to hearing from you with a revised article and a response letter describing the changes made.

Essential revisions:

The manuscript has been greatly improved but all reviewers concur that there are some remaining issues that must be addressed. All reviewers applaud the quality and rigor of revised data and corresponding Figures 1-5. The reviewers and editors agree that the authors have carefully considered concerns and addressed the major questions surrounding methods and rationale for normalization of data as well as validation of key DA axon enriched proteins using orthogonal approaches. Further the flawed statistical analysis of axonal vs. somatodendritic enrichment for PD genes was removed.

However, a lingering remnant of the flawed enrichment dataset in PD is inappropriately held over (e.g., the title of the manuscript which must be revised). The reviewers and editors think that the enrichment strategy (Figure 6) continues to suffer from an imprecise GWAS list of genes that inaccurately infers a particular gene at a locus when the actual gene may not be known with the degree of precision required here. Further, the APEX2 strategy biases towards certain proteins and not others that are known to be important in PD but were excluded. For example, well-known PD-associated genes like LRRK2 and GBA might be excluded because the cytoplasmic APEX2 enzyme does not access many endolysosomal proteins, favoring instead distributed proteins with bias. APEX2 is not distributed in the soma in all compartments evenly, and may exclude important mitochondrial genes. The imprecision and bias in both approaches combined, yields a meaningless dataset that is included in Figure 6 and related Supplementary files. Even without these flaws, without comparator datasets, it is not clear whether there would be similar enrichments in any neuronal context, or what the non-neuronal proteome might be. Thus, Figure 6 and all related text referring to PD and PD enrichment that utilizes PD-linked genes should be removed, including references in the title and Supplementary files. The editors acknowledge that removal of these analyses may have an impact on authorship.

All reviewers felt that Figures 1-5 and related text were exciting and had sufficient impact on their own.
