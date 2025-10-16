# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Developmental Biology , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.17061.036](https://doi.org/10.7554/eLife.17061.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Arabidopsis FORGETTER1 mediates stress-induced chromatin memory through nucleosome remodeling" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Detlef Weigel as the Senior and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal his identity: Yijun Qi (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Through a mutant screen, you have identified a new gene, FORGETTER1 (FGT1), that is required for maintenance of heat-induced gene expression. You propose that the FGT1 protein globally associates with the promoter regions of actively expressed genes in a heat-dependent fashion, interacting in this process with chromatin remodelers of the SWI/SNF and ISWI families. You conclude that FGT1 mediates stress-dependent chromatin memory by modulating nucleosome occupancy.

The reviewers agreed that such findings should in principle be published at the highest levels. While the reviewers furthermore agreed that the data presented are clear, they also agreed that the conclusions went considerably beyond what the data showed directly. To bring the interpretation more in line with the data, they ask you to tone down your claims, and also to add a series of new data to support their claims:

Essential revisions:

1) Perform a carefully controlled RNA-seq time course experiment (wt, fgt1-1, brm1 etc) over a heat shock to compare fgt1 and swi/snf effects more precisely. Alternatively, test whether SWI/SNF and ISWI is required for FGT1 binding to HS memory genes or vice versa, with FGT1 ChIP in the swi/snf or iswi mutants and SWI/SNF and ISWI ChIP in the fgt1 mutant, and add RNAPII ChIP.

2) Examine whether nucleosome redistribution dynamics during the HS memory phase are affected by swi/snf or iswi mutations.

3) Include as a control analysis of nucleosome occupancy of a gene that is not a target of FGT1 nor persistently expressed (i.e. HSP101).

4) Provide a better control for FGT1-H3 interaction.

We have included the full reviews, which mention separate points for essential revisions, but after discussion, we condensed them to the four points above

Reviewer #1:

In this manuscript, the authors identified FORGETTER1 (FGT1) as a new factor that is required for heat stress (HS) memory. They found that FGT1 primarily binds to the proximal promoter upstream of the TSS as well as the region downstream of the TTS and functions as a co-activator of memory genes. Moreover, they showed that FGT1 interacts with SWI/SNF and ISWI chromatin remodelers that are also required for HS memory. Finally, they showed that FGT1 is required for maintaining low nucleosome occupancy during the memory phase. The authors propose that FGT1 modulates HS memory through modulating nucleosome occupancy dynamics and transcription-competent chromatin. These findings advance our understanding about the molecular mechanism of stress memory and should be of general interest. The data are of high quality and well presented. Meanwhile, I feel the authors should make efforts to provide the missing link between FGT1 and nucleosome dynamics. My requests for additional experiments are listed below.

1) The interaction between FGT1 and SWI/SNF and ISWI was shown by IP Mass-spec and BiFC experiments. As this is one of the key points of this paper, additional approaches should be employed to demonstrate the interaction.

2) The authors should test whether SWI/SNF and ISWI is required for FGT1 binding to HS memory genes or vice versa. This can be done by performing FGT1 ChIP analyses in the swi/snf or iswi mutants and SWI/SNF and ISWI ChIP in the fgt1 mutant.

3) The authors should examine whether nucleosome redistribution dynamics during the HS memory phase are affected by swi/snf or iswi mutations.

4) It would be also interesting to examine which histone marks are affected by fgt1 during HS memory.

Reviewer #2:

Organisms respond to changes in environmental conditions through changes in transcription. Most of these changes are transient and are lost if the environmental stimulus is removed. For example, heat shock leads to transient upregulation of protein folding chaperones. However, in Arabidopsis, heat stress also leads to persistent expression of several genes (HSA32, HSP21, HSP22.0, HPS18.2) for ~3 days and this protects plants from lethal heat stress during this period. This phenomenon is called heat stress memory and requires an HSF-related transcription factor HSFA2 and is correlated with changes in histone H3 lysine 4 methylation.

Here, the authors perform a genetic screen for mutants that fail to express HSA32 three days after heat stress. This screen identified a mutant in a gene called FORGETTER (FGT1), which is homologous to Strawberry Notch in animals. This mutant resulted in 1) normal expression of HSA32 immediately after a mild heat shock, 2) normal survival of a lethal heat stress administered 90 minutes after a mild heat stress, 3) low expression of an HSA32 reporter (compared with wild type) after 2 or 3 days of recovery and 4) poor survival of a lethal heat stress after 3 days of recovery. These results suggest that FGT1 is specifically required for the long-term effects of mild heat stress. The manuscript seeks to understand the phenotype of the fgt1 mutant and to define the molecular role of FGT1 in stress memory. This is a very interesting phenomenon and the system is excellent. The experiments are well designed and the data are clear. However, I do not agree with the authors' interpretation of several experiments and I am not convinced that they support the major conclusions of the paper. As a result, I do not feel that this work is mature enough to recommend publication in eLife.

To validate these observations, the authors measured the mRNA levels of both genes that exhibit persistent expression after heat stress (HSA32, HSP21, HSP22.0 and HSP18.2) and a gene that is induced by heat stress but does not show persistent expression (HSP101) in the fgt1-1 mutant. Surprisingly, despite having used an HSA32 reporter for the screen, the fgt1-1 mutant plants showed normal persistent expression of HSA32 and HSP18.2 and slightly defective persistence of HSP21 and HSP22.0. However, the authors claim that the very slight decrease in HSA32 after 45 and 69h are the source of the phenotype. Because there was no statistical analysis of this difference, it is unclear if it is significant. These differences do not appear to be as strong as the differences observed with the Luciferase reporter (Figure 1A). Quantitation of the luciferase for comparison would have clarified the phenotype. To convince the reader that the mutation is impacting transcription, ChIP against RNAPII would have helped. Furthermore, inclusion of the HSFA2 mutant for comparison would have made the strength of the phenotype easier to assess. It is possible that the mutation has a larger effect on the reporter and that the survival phenotype is the result of an effect on a different subset of genes (i.e., HSP21 and HSP22). If so, then the persistent expression of genes in response to heat stress involves both an FGT1-dependent and an FGT1-independent mechanism.

The authors hypothesize that FGT1 promotes persistent expression of HSP21 and HSP22.0 by remodeling nucleosomes because the protein possesses a PHD finger domain and a Helicase C domain. Consistent with this hypothesis, FGT1 localizes to the nucleus, interacts with both active genes and heat stress-induced genes and physically interacts with the BRM (SWI/SNF) and CHR11/CHR17 (ISWI). Unfortunately, a number of experiments create uncertainty about this conclusion. First, the changes in nucleosome occupancy in the fgt1 mutant do not correlate with binding of FGT1: FGT1 binds strongly to the HSA32 promoter/TSS upon heat stress and this correlates with decreased nucleosome occupancy. The fgt1 mutant shows lower nucleosome occupancy prior to heat stress and this decreases to a comparable level to the wild type in the days following heat stress. Therefore, FGT1 is not required for the decrease in nucleosome occupancy at HSA32. In the cases of HSP18.2 and HSP22, although the fgt1 mutant shows increased nucleosome occupancy, the changes in the wild type strain upon heat stress are difficult to appreciate and, as mentioned above, there is no obvious effect of this mutation on the expression of HSP18.2. It would have been helpful to include a gene that is neither a target of FGT1 nor persistently expressed (i.e. HSP101) as a more relevant control. Likewise, as mentioned above, examining the effect of the HSFA2 mutant in this assay would have been informative. Also, peptide binding experiments show that the PHD finger interacts non-specifically with (non-overlapping) histone peptides. The authors did not include a biologically irrelevant peptide control, but the low affinity and the lack of specificity cast doubt on the claim that "FGT1 binds to the N-terminal region of H3[…]". It seems equally plausible that FGT1 binds to the FLAG peptide. Finally, ChIP seq shows that FGT1 associates with both the transcription start sites and the transcription termination sites of active genes. Given the DExD-like helicase domain, this raises the alternative hypothesis that the protein is involved in post-transcriptional events and might impact the ability of plants to survive through influencing protein levels.

The authors also explored the role of BRM and CHR11/CHR17 in heat stress memory. Mutations in BRM1 and FGT1 produced synthetic flowering and development phenotypes, suggesting non-overlapping roles in these processes. Both mutant plants were somewhat defective in heat stress protection after 3d of recovery. However, these mutant plants also showed significantly lower peak levels of the HS-induction of HSA32, HSP18.1, HSP21 and HSP22. Therefore, the decrease in expression afterward appears proportional to the wildtype, but starting at a significantly lower peak level. If so, then poor survival after 3d of recovery is likely due to lower levels of induced transcription, not less sustained transcription.

Reviewer #3:

How plants adapt to heat stress and remember previous heat shocks is a very interesting area of biology. This paper breaks new ground by discovering a new component, FORGETTER1, which the authors show is necessary for plants to "remember" heat stress correctly at the level of transcriptional regulation. Interestingly, the fgt1-1 mutants have a specific defect in acquired thermotolerance, consistent with the proposed role for this gene in controlling the transcriptional response to temperature. The authors present a rather complete story, since they go from a genetic screen, to mapping and examining the underlying molecular mechanism. It is a bit of an open question as to the actual role of FGT1 in transcriptional memory itself, but that is probably beyond the scope of this study.

Here are a few suggestions that came to my mind on reading the paper, and resolving these might make the study even stronger:

1) For the ChIP-seq of FGT1 it would be nice to see screen shots of actual loci from a browser. Averaged data is rather hard to interpret. Relating to this, different gene lists were used for "active" genes and HS responsive genes for Figure 4B and 4C. Isn't there a more relevant list of genes whose transcription appears to show "memory" of heatshock? Another way of looking at this, what about the transcriptome of fgt1 itself?

2) The model for FGT1 action is interesting. It seems to invoke a specific role for +1 nucleosomes in responding to temperature. It's striking that there is such a strong enrichment for FGT1 at the +1 position as well as the TTS. Of course these are sites where there is global enrichment for H2A.Z-Nucleosomes (Coleman-Derr and Zilberman 2012) and H2A.Z-nucleosomes are evicted in response to temperature (Kumar and Wigge 2010). It is therefore curious that no attempt is made to synthesise what is already known about temperature-dependent gene expression and its regulation by chromatin. At a minimum, one could simply overlay the distribution of FGT1 with that of H2A.Z.
