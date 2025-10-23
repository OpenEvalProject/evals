# Peer review - Round 1

Editors:
- Tony Hunter, Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63299.sa1](https://doi.org/10.7554/eLife.63299.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

These studies reveal that sumoylation of HDA-1, a type 1 histone deacetylase (HDAC), plays a key role in establishing transcriptional silencing of piRNA-regulated genes in C. elegans. Genetic analysis provides strong evidence that the SUMO pathway is involved in piRNA silencing, and further mechanistic analysis demonstrates this involves sumoylation of two lysines in the tail of HDA-1. HDA-1 sumoylation promotes its association with the NuRD chromatin modifier complex, which enhances local H3K9ac deacetylation, resulting in negative regulation of hundreds of target genes that is instrumental in the inherited RNAi pathway.

Decision letter after peer review:

Thank you for submitting your article "HDAC1 SUMOylation promotes Argonaute directed transcriptional silencing in C. elegans" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Tony Hunter as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kevin Struhl as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Federico Pelisch (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this paper, your studies showed that sumoylation of HDA-1, a type 1 HDAC, at two C-terminal Lys residues plays a role in establishing transcriptional silencing of piRNA-regulated genes in C. elegans through enhanced NuRD complex interaction and histone H3 deacetylation. The reviewers all found the link between HDA-1 sumoylation and silencing to be interesting, but raised a number of issues that need to be addressed. In particular, more mechanistic insights into

Essential revisions:

1. The evidence that sumoylation of HDA-1 increases its silencing function is reasonably strong, but no direct evidence is provided that HDA-1 sumoylation at K444 and K459 increases its deacetylase activity, as is proposed. For this purpose, biochemical assays comparing unmodified HDA-1 (desumoylated WT or KKRR mutant HDA-1) with sumoylated HDA-1 (or SUMO-fused HDA-1) to measure changes in deacetylatase activity are required. In this connection, there are also no mechanistic insights into how the presence of a SUMO moiety at either K444 or K459 site in the C-terminal tail would increase HDA-1 catalytic activity. Finally, your evidence for sumoylation is based on K to R mutations of these two Lys, and direct mass spec evidence that the K444 and K459 sites are in fact sumoylated in vivo would be desirable, although not essential.

2. Although the evidence that sumoylated HDA-1 interacts with the NuRD complex is reasonable, it remains unclear how sumoylation of HDA-1 increases its recognition by the NuRD complex. To determine whether the HDA-1 SUMO moieties are directly involved in the interaction, testing for SIMs (and/or UIMs) in MEP-1, or another subunit of the NuRD complex subunit is needed, followed by verification of the importance of these residues in vivo or through in vitro interaction assays.

3. Evidence is provided that HDA-1 sumoylation decreases total H3K9ac histone acetylation in vivo, but the use of ChIP-seq to test if HDA-1 and NuRD complex recruitment, and local histone H3 acetylation are affected at known target genes in the KKRR mutant and HDA-1 degron strains versus the wild type strain, with correlated RNA-seq data in the same lines, would significantly strengthen the conclusion that HDA-1 sumoylation is required for piRNA regulation. The addition of ChIP-seq data for HDA-1 and HDA-1-KKRR genome-wide distribution profiles would further strengthen the authors' claims, but is not essential.

4. A possible role of the GEI-17 E3 SUMO ligase in the regulation of HDA-1 and piRNA-regulated gene silencing was excluded through the use of a gei-17 mutant. However, while neither gei-17 nor pie-1 Individually affected piRNA reporter expression in P0, the authors need to test a double mutant to confirm a lack of synergy.

5. Based on the data presented only a small fraction of the HDA-1 population was sumoylated, and the authors need discuss how sumoylation of such a small fraction of the HDA-1 protein population would be able to exert the functional effects on HDA-1 activity they observed.

6. The authors could do a more comprehensive job of reviewing the relevant literature on the role of sumoylation in Piwi-mediated silencing in other organisms, e.g. Ninova et al. Mol Cell 77:556, 2020.

Additional points are raised in the individual reviews below and could be considered, if the authors believe that addressing them would strengthen the manuscript.

Reviewer #1:

The evidence that sumoylation of HDA-1, a type 1 HDAC, plays a key role in establishing transcriptional silencing of piRNA-regulated genes in C. elegans is quite convincing. The genetic analysis demonstrating that the SUMO pathway is involved in piRNA silencing is strong, and the mutational evidence that this involves sumoylation of two Lys in the tail of HDA-1 is reasonable. Likewise, the finding that HDA-1 sumoylation promotes association with NuRD complex components and association of MEP-1, an HDA-1 interactor, with chromatin regulators is convincing. In addition, the evidence that HDA-1 sumoylation increases H3K9ac deacetylation in vivo, leading to negative regulation of hundreds of target genes, and plays a role in the inherited RNAi pathway is solid.

While the overall conclusion provides an interesting advance in understanding mechanisms of piRNA-mediated gene silencing in C. elegans, the paper is lacking any biochemical analysis of the effects of sumoylation on HDA-1 activity and its association with other transcriptional regulators.

1. The authors mapped two sumoylation sites close to the C terminus of HDA-1, K444 and K459, based on extremely weak homology with two established sumoylation sites in human HDAC1 that are reported to be important for transcriptional repression (N.B. the authors should indicate here that David et al. reported that K444/476R HDAC1 had reduced transcriptional repression activity in reporter assays.). While the two human sites conform to the sumoylation site consensus, ψKXE, neither K444 nor K459 in HDA-1 fits this consensus (possibly one could argue that K444 is in an inverted motif). The fact that the KKRR mutant HDA-1 is no longer sumoylated is consistent with these two Lys being sumoylated, but it would be reassuring to have direct MS evidence that K444 and K459 are indeed sumoylated, which could be achieved using a SUMO Thr91Arg mutant that generates a GlyGly stub upon trypsin digestion, among other methods.

2. It remains unclear how sumoylated HDA-1 is recognized by MEP-1 for assembly into the NuRD complex. Does MEP-1, or another NuRD subunit, have a SIM that could facilitate direct interaction of MEP-1 and sumoylated HDA-1?

3. As the authors discuss, it is surprising that the HDA-1(KKRR)::SUMO protein, which in effect is a constitutively sumoylated form of HDA-1 that will interact constitutively with MEP-1/NuRD, does not have more deleterious effects on the organism, since according to the data in Figure 2B, the stoichiometry of endogenous HDA-1 sumoylation was extremely low. Of course, low sumoylation stoichiometry, which is a general issue with sumoylation studies, means that only a very small fraction of the HDA-1 endogenous population will be able to engage with the silencing complexes at any one time. This point is also worth discussion.

4. Page 5: Here, and elsewhere, the authors claim that sumoylation of the two C-terminal Lys activates HDA-1 histone deacetylase activity, but provide no direct evidence for this statement. There are no HDAC assays, and it is unclear how C-terminal SUMO residues distant from the catalytic domain would alter its enzymatic activity, unless there is a SIM motif in HDA-1 that might allow for intramolecular interaction with SUMO residues at the tail leading to a conformation change. Did the authors check for a SIM motif in HDA-1? The fact that adding SUMO to the C-terminus rather than one or both of the two Lys would also have to be taken into account in determining bow sumoylation might "activate" HDA-1. To demonstrate that sumoylation activated HAD-1 in vitro deacetylation assays would need to be carried out comparing the activities of unmodified and sumoylated HDA-1. Instead of enzymatic activation, it is possible that the PIE-1 interaction and HDA-1 sumoylation results in relocalization of HDA-1 within the nucleus to facilitate more efficient H3K9ac deacetylation.

Reviewer #2:

In their manuscript, Kim et al. describe a role for HDAC1 (HDA-1) sumoylation in Argonaute-directed transcriptional silencing. The authors suggest that sumoylation of HDA-1 is important for proper assembly of the NuRD deacetylase complex. The role of SUMO modification in heterochromatin has been extensively documented and it is a very interesting topic. The current manuscript provides a very interesting set of results on this topic. I have list of comments, suggestions, questions, and concerns, which are listed below, especially related to the first half of the results:

1. A general question would be how can HDA-1 sumoylation, which is barely detectable, account for such a big 'positive' effect on complex assembly? HDA-1 SUMO modification seems around 10% after enriching for SUMO-modified proteins, which means that stoichiometry will be way lower than this. While this is common for SUMO-modified proteins, it does make it difficult to associate with a 'simple' model.

2. In Figure 1, a schematic of the sensor used throughout the study would benefit the reader.

3. In Figure 1, have the authors checked if the 10xHis::tagged smo-1 has the same effect as the 3xflag::smo-1 (i.e. is it also a partial loss of function allele)?

4. In Figure 1 it would be nice to see the global SUMO conjugation levels in the different conditions, particularly in the smo-1(RNAi), 3xflag::smo-1, and ubc-9(G56R).

5. Also Figure 1, was gei-17 depletion/deletion checked in any way (i.e. WB)? Did the authors consider other SUMO E3 ligase, such as the mms-21 orthologue?

6. While I am not a big fan of fusing SUMO to proteins, in this case it seems like a very reasonable thing to do, considering the modification sites are located very close to the C-terminal end of the protein. Did the authors check an N-terminal fusion?

7. In Figure 2B, it becomes very clear that the level of SUMO modification of HDA-1 is extremely small, barely detectable after an enrichment method. I also wonder why the gels were cropped so tightly, especially considering that in Figure 3 there is an additional band corresponding to ubiquitylated, sumoylated HDA-1. in vitro modification assays would be helpful. HDA-1 alongside a known and characterised SUMO substrate would indicate how good a substrate HDA-1 is.

8. In Figure 2D, is the difference between HDA-1(KKRR)::SUMO and HDA-1::SUMO significant?

9. In Figure 3A-C, it would be useful to control whether the GFP::HDA-1 fusion behaves as the untagged one in the sensor assay (wt vs. KKRR).

10. I have a few questions regarding Figure 3D:

i. Considering the extremely low level of HDA-1 sumoylation, did the authors detect SUMO and ub conjugated HAD-1 (not the SUMO usion)?

ii. Is ub conjugated to SUMO or to HDA-1?

iii. Does MEP-1 contain any obvious SIMs and or UIMs?

iv. To make a stronger case for the SUMO-dependent interaction model, in vitro interaction assays with recombinant proteins would be extremely useful.

11. In the discussion, the authors compare the lack of requirement for GEI-17 in their manuscript with the requirement for Su(var)2-10 in flies. It is very important to back this claim that the authors control GEI-17 depletion (as pointed out in 5).

Overall, I think this manuscript provides a very interesting set of results and I believe that, with the addition of some simple biochemical experiments, the quality and impact of the overall work would be much greater.

Reviewer #3:

This manuscript by Kim et al. describes a role of SUMOylation in Argonaute-directed transcriptional silencing in C. elegans. The Authors found that SUMOylation of the histone deacetylase HDA-1 promotes its interaction with both the Argonatue target recognition complex as well as the chromatin remodeling NuRD complex. This enables initiation of target silencing. Impaired SUMOylation of HDA-1 leads to loss of interactions with several protein complexes, reduced silencing of piRNA targets, and reduced brood size. While the findings and claims are interesting, some of the novelty is overemphasized and some of the claims are not fully supported by the data.

1. The importance of HDA-1 SUMOylation for transcriptional repression. The title "HDAC1 SUMOylation promotes Argonaute directed transcriptional silencing in C. elegans" implies a central role of SUMOylation in piRNA-mediated transcriptional silencing. The Argonaute HRDE-1/WAGO-9 targets countless transposons as shown previously and also in this manuscript (Figure S3), and so do the HDA-1 degron and Ubc9 mutant, indicating that histone deacetylation and protein SUMOylation are essential processes in TE silencing. However, the HDA-1 SUMOylation mutant (KKRR) only slightly affects 6 TE families (Figure S3), indicating that SUMOylation of HDA-1 might not be a key mediator of this process. Furthermore, the authors write that "Our findings suggest how SUMOylation of HDAC1 promotes the recruitment and assembly of an Argonaute-guided chromatin remodeling complex to orchestrate de novo gene silencing in the C. elegans germline.", but then they also state that "Comparison with mRNA sequencing data from auxin-treated degron::hda-1 animals revealed an even more extensive overlap with Piwi pathway mutants (Figure S2B), indicating that HDA-1 also promotes target silencing independently of HDA-1 SUMOylation." Based on their results and their own interpretations, I find that the importance of HDA-1 SUMOylation in piRNA-dependent transcriptional silencing is overemphasized.

Additionally, the model (Figure 7) implies that for initiation of silencing WAGO recruits HDA-1 to targets. This should be tested by analyzing HDA-1 distribution over WAGO targets in WT and upon loss of WAGO.

2. The mechanistic role of HDA-1 SUMOylation.

On page 17 (amongst other places) the authors claim that "The SUMOylation of HDA-1 promotes its activity, while also promoting physical interactions with other components of a germline nucleosome-remodeling histone deacetylase (NuRD) complex, as well as the nuclear Argonaute HRDE-1/WAGO-9 and the heterochromatin protein HPL-2 (HP1)".

• Regarding activity: Loss of deacetylation/silencing in the SUMO mutant might be due to loss of enzymatic activity, but it might also be due to defects in recruitment/complex formation. There is no data that proves altered enzymatic activity. In fact, Figure 6 indicates SUMO-dependent interaction of WAGO-9 with HDA-1, implying that recruitment is affected. To distinguish between activity and recruitment, at the very least, the authors would need to show that HDA-1 localization to its genomic targets is unaltered upon mutating its SUMOylation site (ChIP-seq of wt and KKRR mutant), while H3K9ac is increased (K9ac ChIP-seq in wt and KKRR mutant) in the mutant. This, in combination with HDA-1 localization in wt and WAGO-9 loss would imply whether complex formation to recruit HDA-1 or HDA-1 enzymatic activity is mostly affected by SUMOylation.

• Regarding physical interactions: Figure 3D shows that if we fuse a SUMO residue to HDA-1, it will interact with MEP-1, while SUMOylation deficient HDA-1 mutant doesn't interact. However, for the WT HDA-1 control, we only see unSUMOylated protein interacting with MEP-1. Furthermore, in the MEP-1 IPs of samples that should contain SUMO-fused HDA-1, the authors detect a lot of "cleaved", unSUMOylated HDA-1. Unless cleavage happened after IP, during elution (unlikely, and there is "cleaved" HDA-1 in the inputs), these findings argue that the interaction with MEP-1 is not mediated by HDA-1 SUMOylation. An interaction between MEP-1 and unmodified HDA-1 is also shown in the accompanying manuscript, which appears to be dependent on Pie-1 SUMOylation. Thus, SUMOylation of HDA-1 alone seems unlikely to be the major factor necessary for silencing complex assembly. (as a side question: Does the protease inhibitor cocktail used inhibit de-SUMOylation enzymes? I am concerned that deSUMOylating enzymes might compromise some result interpretations.)

• Regarding functional relevance of HDA-1 acetylation: On pages 12/13 authors claim that because "HDA-1(KKRR) animals and mep-1-depleted worms revealed dramatically higher levels of H3K9Ac compared to wild-type" and "HDA-1, LET-418/Mi-2, and MEP-1 bind heterochromatic", "SUMOylation of HDA-1 appears to drive formation or maintenance of germline heterochromatin regions of the genome." These correlations do not prove function. The authors have performed H3K9me2 (although not H3K9-ac) ChIP-seq in WT, KKRR mutant and HDA-1 degron worms, yet do not analyze globally whether acetylation is lost on genes that are affected (change in RNA-seq vs. change in K9me2 or acetyl). To support the claim that SUMOylation of HDA-1 drives deacetylation and heterochromatin formation, it would be important to show changes in H3K9Ac levels (or other acetyl marks) and potentially NuRD component occupancy between control and HDA-1 SUMOylation-deficient animals at specific targets (i.e. genes derepressed upon loss of SUMOylation identified in RNA-seq, and the reporter locus).

3. The authors claim (p17) that "initiation of transcriptional silencing requires SUMOylation of conserved C-terminal lysine residues in the type-1 histone deacetylase HDA-1". I do not see any supporting data that has separately looked at formation/initiation and maintenance of silencing (a technically challenging experiment).

4. The authors repeatedly claim that gei-17 does not play a role in piRNA target silencing, based on loss of gei-17 not affecting the piRNA reporter (Figure 1B). At the same time, they claim that pie-1 plays a role, even though it likewise does not affect the piRNA reporter (it affects the reporter only in F3; data on gei-17 effect in F3 is not present). In the accompanying paper, the authors show that while gei-17 loss by itself causes only moderate effect on extra intestine cells, combined with Pie-1 loss the effect is more severe than when Pie-1 loss is combined with Ubc9 or smo loss. This to me indicates an important role of gei-17 in inhibiting differentiation of germline stem cells to somatic tissues, but these effects are likely synergistic and thus masked by Pie-1. Individually neither Gei-17 nor Pie-1 show an effect on piRNA reporter in P0, but to confirm lack of synergy, their effects of should be tested together. Although possible, the present data is insufficient to rule of gei-17 involvement.
