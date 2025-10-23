# Peer review - Round 1

Editors:
- Jeffrey Ross-Ibarra, University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83115.sa0](https://doi.org/10.7554/eLife.83115.sa0)

This work provides a thorough look at changes in expression, methylation, and nucleotide and transposable element diversity among three populations of Arabidopsis lyrata in two different environments. It is a rich dataset, and the authors present a number of nice findings with relevance for our understanding of local adaptation and the process of – and potential constraints to – adaptation to rapid climate change.


---

# Peer review - Round 1

Editors:
- Jeffrey Ross-Ibarra, University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83115.sa1](https://doi.org/10.7554/eLife.83115.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Environmental response in gene expression and DNA methylation reveals factors influencing the adaptive potential of Arabidopsis lyrata" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jeffrey Ross-Ibarra as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor.

Comments to the Authors:

Regrettably, after consultation among the reviewers, we have agreed that the work in its current form cannot be considered further for publication by eLife. As you will see, there was considerable enthusiasm from the reviewers for what you are trying to achieve, but they also agreed that it is currently unclear whether the analyses are robust enough for the far-reaching inferences made. Having said this, we remain very interested in the work, and would reconsider an extensively revised paper, albeit as a new submission. We would of course try to retain the same reviewers, should you decide to come back to us with such a manuscript.

Reviewer #1 (Recommendations for the authors):

I very much liked the author's goal here of going beyond SNP data to evaluate changes in expression, methylation, and TE polymorphism in common garden experiments in order to better understand adaptation.

They really dig into this data and have a number of nice findings.

My main concern is with the overall interpretation of the findings.

The authors claim their TE results show that TEs could be an important source of adaptive variation. While this is certainly true in principle (anything that creates novel genetic variation could be potentially adaptive), I have trouble seeing how the results move us past this? For example, if we interpret the data as showing increased insertion specifically in environmentally responsive genes, and most TEs are deleterious and we see no evidence of TEs generating adaptive change in these data, what have we learned beyond the above? Also, if I'm interpreting correctly, of the 12 DEG-field or DEG-field:population enrichment comparisons with retroelements, enrichment is only found in 3. How does this constitute strong evidence of enrichment?

The authors also claim that evidence of conservation at environmentally responsive genes will constrain adaptation. I have trouble understanding this argument. Does constraint in the past necessarily predict inability to adapt in the future to novel climates? If these are the genes that are most responsive expression-wise, and those expression changes are adaptive, wouldn't these be the genes most likely to see subsequent cis-regulatory change canalize adaptive expression? The total list of DE genes is a few hundred, but if most traits are polygenic, how much would adaptation really be limited even if these genes remain constrained? Finally, what is the interpretation of the strong enrichment of DEG~Field:Pop for number of sweeps? This seems inconsistent with the argument these genes are super conserved and/or constrained for adaptation.

Many of the differences seen in the paper are between German and the Norwegian populations. I would like to see more discussion of how to interpret this, especially in the light of adaptation. We know Germany is poorly adapted to both sites, so what does DE or DM in Germany tell us about adaptation?

Methodological questions:

– How do you deal with multiply mapping reads in evaluating TE expression and methylation?

– Please verify you used a version of RAISd that accounts for variable numbers of bp sequenced in each window.

– To correct bismark, for some genes, WGS SNP data were used, and RNA-seq for others. Do these two sets (WGS genes and RNA-seq genes) show differential methylation?

– There are a number of enrichment analyses done in the paper; are these corrected for multiple testing?

– Figure 6D looks at the % of TEs. Are total numbers of new DNA insertions higher in J3 than J1? That would change the interpretation I think?

– Does Figure 4 look different if you plot the 95% range rather than the CI?

– It might be useful to quantify TE expression and methylation following Anderson (https://pubmed.ncbi.nlm.nih.gov/31506319/).

– I believe newer versions of RIASd can account for variable bp per window. Since you have this number from ANGSD, you can rescale the RAISd mu statistic appropriately if not.

– I might move Figure 3 to supplement. though good to document, I didn't find it super helpful.

Reviewer #2 (Recommendations for the authors):

This manuscript reports on a genomic analysis of an intricate common garden experiment utilizing three populations (two local and one distant) to better understand the evolution or adaptive benefit of gene expression variation. This is a very interesting paper but there was a bit of an assumption about how DMGs and DEGs are cis variants that needs strengthening or supporting. Without this support, it isn't clear if the evolution of cis sequences is informative of what is happening with DMGs if they are largely trans effects as one might see for a FRI/FLC or similar polymorphism causing large transcriptomic effects.

One complication I'm struggling with is the analysis of differentially expressed genes. The analysis directly compares DEGs to DMGs and to genetic variation with an implicit assumption that they are comparable. However, DEGs can be caused by cis or trans events such that the majority of DEGs are caused by a single causal locus. This maybe comes up the strongest when the analysis shifts to looking for footprints of selection at the DEGs (line 225). This seems to assume the DEGs are all caused by cis but it isn't clear what the support is for this claim. Is there evidence that these are mainly cis (e.g. loci with known PAVs, large bimodal effects, etc)? Some support should be provided for an assumption that a DEG is being caused in cis.

In contrast, DMGs are almost always cis as shown by work from the Springer and Schmitz groups. Although there are known loci influencing global methylation levels which does appear to be the case with the German collection having lower methylation across the board as well as a lack of relative plasticity (Figure 2A and 2D) in comparison. How does this lack of plasticity influence the ability to assess the DMG ~ Field and DMG ~ Field:Population terms as the overall methylation in the German collection is non plastic. In the local populations, one could assume the DMGs are local events but when comparing J1/J2 to Ger there is the possibility that DMGs are a blend of cis/trans. Is there evidence similarly supporting DMGs in this comparison as mainly cis?

A similar concern is that in the closely related Arabidopsis thaliana, a large fraction of cis causality for DEGs is actually not promoter polymorphisms but actually PAV or other structural variation within the loci. Is there evidence in this collection that cis causality is mainly SNP based as the analysis on selection is suggesting? This is partly a concern because, at least in A. thaliana, this can lead to these loci having an elevated level of error in short read sequencing leading to a ponderance of rare SNPs (See recent work by Nordborg and colleagues on variation in gene duplication and SNP error rates).

Similarly work by Schmitz and Ecker has shown that DMGs can also be biased towards genes with structural variants. In this studies, DEGs and DMGs seem to not be behaving in coordination so structural variants aren't likely a universal problem but some assessment of their potential in influencing the data would be necessary to understand how pangenome variation may be introducing error.

Reviewer #3 (Recommendations for the authors):

This study was aimed at identifying the adaptive potential of genomes in response to different environments. To accomplish this aim, the authors performed reciprocal transplant experiments with distinct populations of Arabidopsis lyrata. These plants were grown over a year and then tissue was harvested and used for gene expression and DNA methylation profiling genome wide. A strength of this research is the unique samples available to investigate. This allows the evaluation of impact on differential expression/methylation to be attributed to the environment, genotype or both. Many of the conclusions are justified, but analysis of the DNA methylation data is confounded by the way it was defined and analyzed. The weakness in this analysis stems from only investigating the impact of CG methylation. It is well established in plant genomes (including A. lyrata) that there are two distinct categories of methylated regions. One region is defined as GBM (gene body DNA methylation), which is defined by CG-only methylation in a gene body. The second category of methylation is found anywhere in the genome (including genes) and contains CG + non-CG (CHG and CHH) methylation. This study has not properly distinguished these regions and it has likely led to improper conclusions.

With regards to the findings presented on plasticity of DNA methylation, many of the findings are somewhat expected. It has been established that DNA methylation variation is largely driven by genetic variation within plant genomes. The variation in methylation found between different environments on non-gene regions also reflects common observations. There are lots of environments that lead to genome-wide changes in methylation. It's important to note that not all of these changes are causal. In fact, many of them are likely an indirect effect of 3D nuclear genome compaction and access of DNA methyltransferases to target sequences. Notice the changes in methylation are very subtle and they exclusively occur at regions that already possess methylation. It is not like mammalian systems where methylation is completely lost or gained at regions.

The section of TE activation by stress was not fully supported by the data presented. It's an intriguing possibility, but not well supported by the data. This entire section needs to be revisited with additional analyses.

Overall, although this is a unique population the conclusions presented are incremental to the field. The shortcomings presented in the analysis can be easily remedied, although it will be curious to see how they change the conclusions.

The DNA methylation data must be partitioned into CG and CG/CHG/CHH regions in the analysis. Using CG methylation alone mixes two distinct groups together. It is well established that CG/CHG/CHH methylated regions are generally silenced whereas CG only methylated genes are expressed.

More information is required for understanding how DMGs were defined. What is the size distribution of DMGs? What proportion of DMGs are GBM vs those that contain CG/CHG/CHH? The rapidly evolving DMGs mentioned on line 252 are likely those that contain CG/CHGCHH, as worked by Gaut et al. have shown that GBM genes have low rates of nucleotide substitutions.

I'm not convinced by the TE analysis. Are these full length TEs? Or are they TE fragments? How are multiple mapping reads handled in the RNA-seq analysis? Read counts of 5-6 as presented in 6b are not very convincing for "expressed" TEs. I found this to be another weak aspect of the study. What's the evidence these TEs are "stress induced"? It is stated that TEs overlapping genes were removed, but these genotypes were mapped to a reference genome? There will be differences and no genomes have 100% annotation. This is especially true of out-crossing species. Overall, I found the evidence of stress induced activation of TEs not well supported by the data.

Line 405 – there is not assignment of cause and effect from the results of this study. The authors should be careful not to state methylation is affecting expression. It could equally be possible that expression is affecting methylation.

I found the section on rates of evolution of 1kb upstream regions worthwhile, but to extend this make conclusions about cis-regulatory elements is a bit of a stretch. No CREs were identified and there are lots of non-CREs located upstream of genes that could impact these results.

The bisulfite conversion rates need to be presented for each of the 24 samples instead of an average.

The number of reads sequenced per RNA-seq/BS-seq library need to be presented in a supplementary table along with their alignments rates (and bs conversion rates).
