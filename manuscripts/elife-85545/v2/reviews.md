# Peer review - Round 1

Editors:
- Timothy W Nilsen, https://ror.org/051fd9666 Case Western Reserve University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85545.sa0](https://doi.org/10.7554/eLife.85545.sa0)

This fundamental study represents a real tour de force, demonstrating the impact of mutation on the mRNA decapping machinery. Accumulation of mRNAs in dcp2 mutants, is dependent both on the classical 5' to 3' pathway of mRNA decay and on the NMD pathway- highlighting the 'non-nonsense' roles of the NMD pathway and how little we really know about the complete set of pathways of mRNA degradation.


---

# Peer review - Round 1

Editors:
- Timothy W Nilsen, https://ror.org/051fd9666 Case Western Reserve University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85545.sa1](https://doi.org/10.7554/eLife.85545.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Decapping factor Dcp2 controls mRNA abundance and translation to adjust metabolism and filamentation to nutrient availability" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Timothy Nilsen as the Reviewing Editor and James Manley as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Mark Peter Ashe (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

As you will see, all the reviewers were quite positive about the work as was the reviewing editor. Specifically, they thought that the demonstration of Dcp2's extensive roles in gene expression was quite interesting. No additional experiments are required, but each reviewer has made a number of comments regarding the text. Please address these issues as thoroughly as possible before submitting a revised version.

Reviewer #1 (Recommendations for the authors):

Vijjamarri et al. describe a multi-omics approach to determining the gene expression consequences of deleting the DCP2 gene in the yeast Saccharomyces cerevisiae. This gene encodes the catalytic subunit of yeast's mRNA decapping enzyme. Throughout the literature it has generally been understood that dcp2∆ strains fail to decap mRNAs and that this defect promotes the stabilization of mRNAs ordinarily subjected to the major 5' to 3' mRNA decay pathway. Previous evidence supporting this conclusion includes data demonstrating that, in dcp2∆ cells, several specific mRNAs maintain their 5' caps, increase their steady-state levels, and extend their half-lives. In this manuscript, the authors seek to beat a dead horse with more sophisticated transcriptome-wide methods, ultimately proving the original point, but also uncovering substantially interesting new results.

The initial experiments (Figure 1) first examined the authors' (and others') prior RNA-Seq datasets to determine the number of transcripts that either increase or decrease in abundance in dcp2∆ cells, ultimately identifying 1376 mRNAs that increase in abundance (so-called "derepressed mRNAs") and 1281 mRNAs that decrease in abundance (so-called "repressed mRNAs"). The respective changes were then validated by qRT-PCR for 10 out of 11 mRNAs tested. To be certain that the RNA-Seq results reflected a loss of mRNA decapping activity, they also evaluated RNA-Seq data from cells expressing catalytically dead Dcp2, an experiment that yielded results almost identical to those obtained with dcp2∆ cells.

Next, the authors sought to determine the role of Dhh1, a decapping activator, in Dcp2-mediated regulation by examining RNA-Seq results for dhh1∆ and dcp2∆dhh1∆ cells. These experiments showed that 752 of the 1376 mRNAs that increased in abundance in dcp2∆ cells could do so when only DHH1 was deleted (albeit to a lesser extent), with 607 mRNAs relatively unaffected by that deletion. These experiments, too, were consistent with previously published results indicating that only a subset of yeast mRNAs were targeted for decapping by Dhh1. Comparable analyses of strains deleted for UPF1, PAT1, PAT1/DHH1, or EDC3/SCD6 yielded results indicating that all of these strains, except for upf1∆ cells, stabilized significant fractions of the Dhh1-dependent mRNAs. upf1∆ cells, however, only appeared to stabilize mRNAs that were Dhh1-independent, results that were also consistent with published data on NMD substrates.

Subsequent experiments employed CAGE analysis and Rpb1 ChIP-seq to further evaluate the basis for increased or decreased levels of the populations of mRNAs identified in the RNA-Seq studies. CAGE analysis was employed to determine whether inferred cap status (capped vs decapped) was correct, and whether there existed subtle differences in cap status of distinct populations of mRNAs. The ChIP-seq experiments were used as an alternative means to testing whether increases or decreases in specific mRNAs reflected changes in transcription of their genes vs. mRNA stabilization. These experiments largely confirmed that mRNAs which accumulated in dcp2∆ cells (and other mutants affecting mRNA decapping) were capped (albeit to different extents) and that RNA polymerase loading differences could not, for the most part, account for the observed changes in mRNA levels.

An additional set of experiments evaluated ribosomal profiling data to assess translational efficiency (TE) of the mRNAs in the expanding subsets of mRNAs that changed in abundance as a consequence of mutations in genes regulating or catalyzing mRNA decapping. These analyses identified 541 mRNAs with TEs that increased in dcp2∆ cells (median increase: 1.65-fold), as well as 659 mRNAs whose TEs decreased in the same cells (median decrease: 0.59-fold). Much of the rest of the paper sought to explain these changes in TE. Agreement between the ribosomal profiling data and TMT/MS-MS analyses indicated that the TE differences reflected actual changes in the synthesis rates of the respective proteins. Subsequent analyses indicated that the translationally-repressed mRNAs generally had lower than average TE in WT cells whereas those that were translationally activated tended to have higher than average TE in WT. The authors' mass spec analyses also indicated that ribosomal protein levels decreased ~25% in dcp2∆ cells, suggesting that the TE differences in dcp2∆ cells might reflect competition caused by limiting ribosomes (or other translational factors) between mRNAs that normally were efficiently vs. inefficiently translated inherently. Numerous other experiments indicated that this indirect model for translational regulation in dcp2∆ cells was likely correct and also identified fine tuning of the expression of genes regulating respiration, alternative carbon and nitrogen sources, mitochondrial function, and filamentation.

During my first reading I was overwhelmed by the length of this manuscript (almost 140 pages!). It was by far the longest paper I had ever reviewed and I was feeling pity for its future readers. That feeling vanished as I reread the paper and absorbed the extent to which the authors had chased down so many details for the phenomena they were tracking, ultimately coming up with a thorough and convincing story, and making it clear to me that cutting this "whole" story up into distinct chapters would be a waste of both the authors' and future readers' time. Hence, I'm supportive of publishing this substantive manuscript in eLife, but here are a few revisions that might make it even better:

1. I'm not fond of the use of the terms "repressed" and "derepressed" to describe mRNAs that respectively decrease or increase in abundance in dcp2∆ cells. I understand that the terms comprise technically correct genetic nomenclature, but we know from prior work that there's no need to opt for vagueness here, i.e., these are mRNAs that go down or up in abundance. Please modify the text to make the observation more precise and describe the repressed class as mRNAs whose abundance decreases and the derepressed class as mRNAs whose abundance increases.

2. The CAGE analysis was quite informative, but the reliability of its measurements of "percent capped" is suspect. This comment follows from the data of Figure 3D, where steady-state levels of capped mRNAs appear to be ~40% of all mRNAs. This figure is at least half of what has been seen in other publications so the authors have an obligation to validate their CAGE analyses with measurements of the extent of capping in individual mRNAs. I recommend the use of cap IPs, but other methods could also work. Also, it's necessary to provide the capped/total data for the dcp2∆ cell samples.

3. On p. 13, the authors note that an "in-depth analysis" of pat1∆, pat1∆dhh1∆, and edc3∆/scd6∆ strains is to be published elsewhere. Is that really necessary? In light of the enormous amount of useful information already in this manuscript why the hesitancy to add a little more?

4. The authors' "old school" models in Figure 8 —figure supplement 1 appear to ignore the recent results and the model for multiple decapping complexes published recently by He et al. (eLife 2022 and FEBS Letters 2022). Do the authors think that their data conflicts with that of He et al? If so, the significant disagreements should be noted.

5. Is it possible that the reduced TE observed for a class of mRNAs in dhh1∆ cells that the authors explain as samples having enhanced decapping may also be targeted specifically by other decapping activators such as Edc3, Scd6, or Pat1? This data may already exist in the set designated for publication elsewhere.

6. Please explain the likely reason for the differences in absolute vs. relative differences in RNA polymerase binding to mRNAs. It's understood that the two datasets differ by the use or not of spike-in controls. However, since there are such large differences in the two datasets it would be helpful to have validation for some of the transcripts in the spike-in datasets that show large changes in abundance.

7. Some figure legends note that outliers have been omitted. Please provide an n for each case of outlier omission.

8. In Figure 3D columns 4 and 5 the authors compare Dhh1 dependent and independent decapping levels for the up_dcp2 mRNAs. Since iESR substrates are 24% of the Dhh1 dependent group they should be removed from the respective datasets to get a clearer picture of what's actually happening.

9. The authors continually refer to one of their datasets (GSE220578) as "unpublished." One cannot examine it in GEO (it's private) so we need to know whether additional authors should be added to this paper. Further, if that dataset is included in this manuscript can we please stop using the term "unpublished."

10. Abstract, line 30: nothing about Lsm2 was addressed in this manuscript.

11. P. 4, line 81: there's nothing about an autoinhibitory region in Fromm et al., 2012. The second reference that's needed is Paquette et al., 2018, ie, the same reference listed on line 78.

12. P. 4, line 63: calling Dcp2 a "bi-lobed enzyme" is probably much too simplistic. The rest of that sentence does a fine job of summarizing Dcp2's structure so I recommend deleting the "bi-lobed" thought.

13. P. 13, line 265: please correct spelling of "trasnscripts;" p. 15, line 299 ("versusvs."); p. 23, line 474, Figure 4F should be 3F; and p. 27, line 556, "do not" should be "does not".

Reviewer #2 (Recommendations for the authors):

This manuscript details a whole range of proteomic, transcriptomic, and ribosome profiling studies comparing mutants in the decapping enzyme, Dcp2 with a parental yeast strain. Furthermore, a careful, logical and scholarly assessment of the implications of the 'omics data are presented. The manuscript gives unprecedented detail at the transcription, mRNA stability and mRNA translation levels concerning the implications of a deficiency in mRNA decapping. The data show widespread mRNA accumulation due to reduced mRNA degradation and consequent alterations in the fine balance of translation regulation. Two areas that are not covered in great detail are the implications of higher level of P-bodies in the mRNA decay mutants and the potential role of the cytosolic exosome in mRNA degradation. However, no paper can cover everything and this manuscript already considers so many angles!

The authors don't mention that mRNA decay mutants such as dcp2delta have constitutive very high levels of P-bodies (Teixeira et al. 2007. PMID: 17429074). This means much of the material that is measured could be present in different contexts within the cell between the mutant and wild type. For instance, do the authors generally spin their whole cell lysates before they conduct their 'omics experiments – if so at least some of this material could have been lost. In my view the connections with P-bodies and biological condensates should be discussed, and any limitations in the study given the presence of these condensates covered.

The idea that increased expression of mRNA and ribosomes in yeast could alter the translational profile in mutants of the mRNA decay pathway has been put forward before in the pre-'omics era. In the paper, the mRNA decay mutants were resistant to the effects of glucose and amino acid starvation. This paper (Holmes et al. 2004. PMID: 15024087) is cited in the manuscript, but not in this context. In my view the authors should cite and discuss this mass action model given the similarities to their hypothesis.

Have the authors cross-compared their datasets with datasets from the Tollervey group looking at exosome substrates?

More specific points

Line 46- eIF4F does not really exist in this context in yeast – i.e. eIF4A is only quite weakly associated and does not generally accompany eIF4G and eIF4E at anywhere near a stoichiometric level- it might be better to get away from mentioning eIf4F

Line 55- the authors state that the exosome pathway is a minor pathway of mRNA decay – while this narrative exists in the literature – I am not clear what the evidence is and, if it exists, it should be cited here. Otherwise, while Delan-Forino et al., 2017. PMID 28355211, don't directly assess the relative contribution of different mRNA decay pathways, they do show that substantial numbers of cytoplasmic mRNAs interact with the exosome.

Line 148- 'suggesting that either Dhh1 or Pat1 is sufficient for repression of translation initiation in glucose starvation'. While Dhh1 and Pat1 may be sufficient to allow repression of translation- the mechanism of repression more likely involves targeting of eIF4A and/or Ded1 (PMID: 33053322, PMID: 21795399, PMID: 34946015). So the impact of the mRNA decay mutants is more likely indirect -see comments above.

Line 214- 'all but one mRNA' – I may have missed it but what is this mRNA?

Line 245- this conclusion implies that the increases in mRNA levels observed are due to a direct impact of DCP2 deletion on mRNA degradation. At this stage in the manuscript, the authors haven't addressed potential transcriptional effects and so the conclusion needs to be more accurately worded.

Line 250- maybe change 'Edcs' to 'Edc1-3'.

Line 483, the authors state most studies have focused on mRNA decay – they need some citations here if they word it in this manner.

Line 495 'These results suggest that Dcp2 broadly controls gene expression at the translational level in addition to regulating mRNA stability'. Given that the authors will later conclude that the impact of the mutant on translation is due to indirect effects on mRNA and ribosome levels – this conclusion is too strongly worded for me.

Line 496 'in an effort to establish' sounds like the result was already known before the experiment. 'In order to evaluate whether' – or something like this would sound better.

Line 519 – relating to Figure 4D- do the authors have controls they could add to this – an mRNA where RPF levels are reduced or are maintained in the mutant relative to the parent strain?

Line 536- YLR361C-A?

Line 569 – is this sulfometuron or sulfometuron methyl?

On Figure 6E, there appears to be an error on the y-axis of the plo.t

Overall though an excellent paper.

Reviewer #3 (Recommendations for the authors):

The manuscript by Vijjamarri et al., is focused on the role of the Dcp2 decapping enzyme in S. cerevisiae. Using a Dcp2 disrupted strain (dcps∆) they address the downstream consequences of the absence of the primary fungal decapping enzyme Dcp2. Although the lack of Dcp2 decapping is expected to result in the accumulation of mRNAs that would have otherwise been degraded and lead to indirect downstream consequences on gene expression and cellular physiology, these outcomes have not been addressed. Here the authors undertake a very thorough analysis. One important and surprising contribution is the association of Dcp2 to decreased translation efficiency. Rather than an expected mechanism of reduced stability contributing to reduced translation, the authors show that this is an indirect effect of Dcp2 by modulating ribosomal protein mRNA stability that in turn leads to a reduction of ribosomal protein levels and competition for limiting ribosomes for translation. A network of mRNAs that are regulated by Dcp2 that are involved in modulating the repression of aerobic growth in glucose-rich media were also uncovered. These discoveries further unravel the indirect contribution of Dcp2 decapping during respiratory growth under non-glucose carbon sources. This is an extremely thorough evaluation of Dcp2 function in yeast and will be an important contribution to the field.

1. Can the authors further elaborate on why they think they do not see (or minimally see) the contribution of codon optimality to Dhh1 directed mRNA decay contrary to current publications.

2. In Figure 5E, the terms "strong" and "weak" mRNA nomenclature should be further clarified or changed.

3. The authors should consider altering Figure 8 to present the functional contribution of Dcp2 rather than the outcome of dcp2 disruption. It seems more informative (to me at least) to state what Dcp2 does rather than what it's not doing when it is absent (as currently depicted in Figure 8).

4. Figure 5C: A brief explanation of C/T should be provided in the text or figure legend to avoid having to search through the M&M section to figure it out.

5. Define TE in the abstract.

6. Lastly, I found the manuscript to be extremely long (more than double the recommended manuscript length for eLife). Although I don't recommend it for this manuscript, I would strongly suggest the authors consider splitting such a manuscript into at least two papers in the future. It is hard to envision most readers retaining everything that is presented in the manuscript by the time they are finished reading it and it simply dilutes the impact.
