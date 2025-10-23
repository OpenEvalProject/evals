# Peer review - Round 1

Editors:
- Darius Balciunas, Temple University United States

Reviewers:
- David Grunwald, University of Utah United States

## Review text

DOI: [10.7554/eLife.48081.021](https://doi.org/10.7554/eLife.48081.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Acceptance summary:

Your manuscript represents a very important technical advance in the emerging field of conditional mutagenesis in the zebrafish. The mutagenesis vectors you have developed offer a key advantage over existing tools: the ability to track homozygous wild type, heterozygous mutant or homozygous mutant status of every cell using fluorescent reporters. Together with well-documented amenability of zebrafish embryos and larvae to high-resolution imaging, these tools should enable tremendous advances in genetic analysis of developmental processes. Furthermore, the ability to unequivocally assign mutant, heterozygous or wild type genotypes to every cell in a mosaic tissue should be of high interest to those studying genetic control of post-embryonic processes such as regeneration. The apparent ease with which your vectors can be integrated into the genome (using non-homologous end joining instead of less efficient but more precise homology directed repair) should make the methodology readily accessible to a large number of laboratories.

Decision letter after peer review:

Thank you for submitting your article "One-step efficient generation of dual-function conditional knockout and geno-tagging allele in zebrafish" for consideration by eLife. Your article has been reviewed by Didier Stainier as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: David Grunwald (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript by Zhang and colleagues describes a novel conditional mutagenesis system for the zebrafish. The system uses non-homologous end joining pathway to integrate dual function transgenes into the genome with very high efficiency. The "rescue" component of the integrated transgene contains the cDNA coding for exons downstream of the integration site co-translationally linked to a fluorescent reporter. The "rescue" cassette is flanked by loxP sites for Cre-mediated excision. The second part of the integrated transgene contains transcriptional terminators and splice acceptors for mutagenesis using the gene trap principle. Authors demonstrate efficient transgene integration and Cre-dependent mutagenesis of tbx5a, sox10 and kcdt10 genes.

While several recent papers have described conditional mutagenesis methods for zebrafish, they have not yet been broadly employed by other laboratories. The approach described in this manuscript is made particularly attractive by the ability to pre-screen using fluorescence, resulting in very high apparent transgenesis rates. The ability to use fluorescence to track mutant and wild type alleles built into the PoR-NeG vectors may be of particular interest for mosaic analysis. An additional advantage, shared with another method recently published in eLife (Sugimoto et al., 2017), is that downstream exons of the mutated gene are not expressed, which should help avoid genetic compensation.

In summary, the manuscript by Zhang et al. represents an important step developing a highly sought-after technique of conditional mutagenesis for the zebrafish.

Essential revisions:

1) The described method of conditional mutagenesis is very likely to be refractive to genetic compensation (with the caveat that the mutExon in the PoNe donor may induce NMD and genetic compensation if expressed). This compelling hypothesis can only be tested by mutating a gene known to be subject to genetic compensation. To our knowledge, tbx5a, sox10 and kcdt10 loci selected for mutagenesis are not subject to genetic compensation, making them unsuitable for testing the non-compensation hypothesis. Thus, authors must either provide data demonstrating lack of genetic compensation or text sentences describing genetic compensation to the Discussion section, clearly indicating speculative nature of such statements. Furthermore, the possibility that mutExon in PoNe donor may induce compensation needs to be discussed.

2) Expression of insertionally mutated loci has to be quantified in "on" and "off" states. It can be done by qRT-PCR using primers in exons upstream and downstream of the integration site, as is common for gene traps. The need to analyze expression in the "on" state is justified because the gene is expressed from intron-less cDNA with a non-native 3' UTR. It is important to analyze expression in the "off" state because all the coding sequences are present in the genome and mutagenicity relies on the efficiency of splicing and transcriptional termination modules within the inserted transgene.

3) A thorough breakdown of transgenesis efficiency must be provided, starting with numbers of injected embryos (if available), embryos screened for fluorescence, percentage/numbers of embryos selected for raising and so forth.

4) A better explanation for different components used in different vectors must be provided. Specifically, why was mutExon not retained PoR-NeG vectors, why different transcriptional terminators are used in PoR-NeG vectors integrated into tbx5a and sox10 loci? Stability of constructs and transgenes containing two 8X terminators should be discussed. In simplest terms, which vector would you recommend for other labs to use?

5) Since rescue function is provided by partially intronless cDNA, this approach may not be applicable to genes with multiple alternatively spliced isoforms or genes regulated at the level of RNA splicing. This limitation should be discussed.

6) Higher resolution images of transgenes must be included for all figures, especially Figure 4—figure supplement 1.

Reviewer #1:

The manuscript by Li et al., "One-step efficient generation of dual-function conditional knockout and geno-tagging allele in zebrafish", describes the authors successful attempts in generating dual functional alleles in zebrafish using NHEJ-mediated insertion targeted by Cas9/gRNA. This gene-trap approach uses two functional units in the vectors. The first unit confers cis-complementation of the mutagenic effect and expression of a fluorescent protein. It consists of the native splice acceptor, the remaining downstream coding sequence, and the coding sequence of a fluorescent protein. The unit is flanked by loxP sites to allow Cre-dependent removal. The second unit confers transcriptional termination. In the basic vector, it consists of two or more pA signals (SV40 pA and BGH pA) followed by a mutant native exon with a premature stop codon. In the more advanced version, the second unit consists of a traditional gene-trap that could lead to the expression of a different fluorescent protein. The authors inserted the cassettes at 3 different loci (tbx5a, kctd10 and sox10) and demonstrated germline transmission in 5-50% founders. They showed the conditionality of these alleles and the utility of alleles generated by the advanced cassette in revealing the genotypes of individual cells. The results are of good quality and the writing is fair. Efficient generation of conditional alleles is a sought-after technique in the zebrafish field. The manuscript therefore addresses an unmet need and should be of interest to scientists in the zebrafish community and beyond. However, there are several issues that need to be addressed, both in the experiments and in the writing.

Essential revisions:

1) There is no quantitative evaluation of the effects of the KI alleles on gene expression. The authors only qualitatively assessed the KI alleles by comparing the expression patterns of the fluorescent protein(s) and the major phenotypes of the homozygous mutants. Quantitative evaluation of such alleles in "normal" and "defective" state at the mRNA level is a norm and should be done here. It is important to know how normal is "normal" and how defective is "defective".

2) The cassette design seems random, not systematic. The authors used 3 different designs. They discussed potential benefits of each feature but often without strong experimental evidence. When adding more features to the more advanced cassettes, they also dropped certain presumably important feature without rationale. For example, the authors argument that the mutant exon with premature termination codon in the cassette may be indispensable for effective gene disruption, but there is no direct evidence. They then dropped the mutant exon in the more advanced cassettes. Although the authors argued that 2PA is highly effective as the transcriptional terminator, they replaced it with 8PA in the last cassette. The stability of two tandem 8PA needs to be evaluated.

3) The authors argued that one of the main advantages of the described alleles is that they may bypass transcriptional adaptation elicited by a premature termination codon. Yet they included a premature termination codon in their cassette.

4) All the alleles also retain the backbone sequence of the vector at the insert site. It has been reported that such extraneous sequence can induce DNA methylation and silencing. This needs to be discussed.

5) The resultant "normal" alleles have reduced intron number, which may alter the expression, or eliminate certain alternative spliced forms. This needs to be discussed as potential disadvantage.

6) The necessity of LiCl precipitation of gRNA is confusing. Although the observation is intriguing, but it is only true for the emx1 gRNA. It is unclear whether the lamGolden gRNA also requires LiCl precipitation for activity.

Reviewer #2:

In the present report by Li et al. the authors describe a genetic method to generate conditional knock out alleles in zebrafish based on the Cre/Lox system and CRISPR/CAS9 mediated NHEJ. With this technique the authors generate specific alleles in few target loci (tbx5a, kctd10 and sox10). In each case they developed reporter alleles that were tagged with fluorescent proteins and could be inactivated by Cre mRNA injection.

The use of NHEJ manipulate endogenous loci in zebrafish with high efficiency was previously reported in various papers. In particular a strategy to tag endogenous proteins at the C-terminus in zebrafish was previously reported by Li et al., 2015. The present manuscript is an improvement of the current methods that consists basically in the design of two loxP sites around the artificial tagged exon that is inserted by NHEJ.

The authors claim that their strategy will offer novel advantages including the avoidance of genetic compensation mechanisms and the possibility to generate conditional knock out alleles. Although I agree in principle with these statements these are not shown in the current paper.

In particular the authors should use their method to silence a known locus that is triggering genetic compensation when inactivated with the insertion of classical indel mutations (as described in the recent literature).

In addition, it is important to test their floxed alleles, crossing them with Cre expressing lines in specific tissues (for instance the heart primordium) to show that tissue and temporal control of the recombination event can be achieved.

Without these experiments the paper shows only a very limited advancement in designing clever targeting plasmid but fails to proof the real power of this approach.

Reviewer #3:

Li et al. introduce a new method for creating conditional knockout alleles in the zebrafish. The method generates a wildtype allele translationally linked to a fluorescent protein so that cells expressing the wildtype allele can be identified. Cre activity leads to excision of the wildtype-fluorescent reporter sequences and leads to expression of a different reporter protein so that the loss-of-function allele is tagged. It is a very nice idea and it will be very useful. The method is not perfect in that the wildtype activity is supplied by a cDNA sequence and the claim is that the mutant allele will not trigger transcription compensation, which is not tested and may or may not be true, but this method is a true advance in the field and will be implemented by others. The method deserves to be published.

Overall the manuscript is very well written. Nevertheless, the manuscript has a number of areas that require clarification. At present, a number of the experiments presented in the figures are difficult to interpret. The paper will make a much bigger impact if the reader has an easy time understanding the experiments and the results.

1) The authors do not correctly describe the efficiency rates of generating insertions or the efficiency with which germline insertions are made or recovered. This is a very important point and must be corrected. The authors claim throughout the paper that they have improved the efficiency of insertion or of generating insertions that will be transmissible through the germline. This is not correct. They have created a method that allows for the efficient recovery of germline transmissible modified alleles. They have made a wonderful advance but it is not the same as improving recombination rates. The authors have come up with a wonderful method for pre-selecting embryos that have acquired insertions in somatic tissue, because integration in the correct orientation leads to expression of a fluorescent reporter under control of the targeted gene. A low percentage of injected embryos grow into normal-looking embryos with reporter expression (subsection “High efficient generation of a dual-function KI allele at zebrafish tbx5a locus” claims 10% in one experiment). Then among those animals pre-selected for the presence integration events, a reasonable and varied fraction will transmit the edited allele to the next generation. Therefore, it is simply false for the authors to write "The feasibility of this strategy was demonstrated at tbx5a and kctd1 loci, with germline transmission efficiency as high as 56%." Such a statement would be interpreted by readers as indicating that they had greatly advanced targeting efficiency so that 56% of injected animals will transmit an edited allele. Similarly, in the Discussion, the authors claim: "As high as 50% of the F0 fish could transmit the integrated donor construct to their offspring, which is much higher in germline transmission efficiency than previously reported HR-mediated gene knock-in." Instead, the authors should say they have developed a clever method that makes recovery of conditional alleles very efficient. This method involves first preselecting embryos that have mosaically acquired the conditional allele, and then only screening the preselected transgenic animals for the ability to transmit the alleles through the germline. Under these conditions, up to 56% of the pre-selected founders may transmit edited alleles. The authors should make this clear in the Abstract also.

2) It is difficult to reconstruct and to figure out the actual numbers that describe the recovery of germline transmissible alleles. For example, let's look at the section that begins subsection "Generation and evaluation of geno-tagging alleles at zebrafish tbx5a locus". The authors write: "After injection and screening, integration of this donor and germline transmission of the tbx5a PoR-NeG donor geno-tagging alleles were detected and confirmed in 2 out of 48 adult F0". I can't understand where the number "48" comes from – was this all the F0 adults from an injection? Was it 48 F0 selected on the basis of fluorescent reporter expression? In Table 2, row 3 it appears that 16/124 injected embryos had reporter expression – so where did the 48 come from?

3) The authors create conditional alleles that can be switched from WT red to mutant green. They call these PoR-NeG alleles for Positive Red to Negative Green. They also seem to call these geno-tagged alleles. They sometimes breed these to animals with another type of condition allele that switches from a WT-fluorescent reporter to a mutant-no reporter allele. They call these alleles PoNe, positive to negative. It would make the reading much easier if they always labeled an allele that co-expressed a fluorescent reporter. In other words, when the wildtype allele is marked by expression of tdTomato and the mutant allele is not marked by reporter expression, maybe call it PoR-Ne. In addition, they place these PoNe alleles on backgrounds that express a heart reporter (cmcl2:EGFP). As a result, if the WT allele were clearly marked as PoR-Ne then it would be easy to tell which is the heart marker and which is the tagged gene. In general: please use consistent nomenclature.

4) The figures need some work. The easiest suggestion is that the lettering needs to be larger or at higher resolution – especially for the line drawings – when I expanded it on my screen it became very pixelated. For example, try enlarging Figure 4—figure supplement 1F.

5) Figure 2A and C: I find these very hard to interpret – I think the authors are visualizing fluorescent markers in three embryo siblings generated from a single cross some of which have been injected with Cre mRNA. The patterns of fluorescence reporter expression differ and I believe the results are to be interpreted as being derived from embryos with different genotypes. Would it be possible for the authors to tell us the presumed genotypes of each row before Cre exposure? I feel this would make the interpretation easier for the reader. I don't understand Figure 2C – it looks like each embryo has a green heart but I think the authors want us to focus on differences. These need to be spelled out perhaps in the figure legend? For Panel E please explain in the figure legend this experiment. Explain the cross and what Normal and Defective embryos are. Explain what "before injection" means.

6) Figure 3B: I suspect the markers on the gel are mistakenly labeled. For example, the experimental band of 380 bp is larger than the marker of 500 bp and the experimental band of 820 bp is smaller than the marker of 750 bp. Also, in Panel B, the gel of the 3' junctions: I don't understand how amplification from the donor shown in Panel A with T5F2 and T5R1 would give a band – is there some mistake here?

7) In Figure 3C, I believe the images of dorsal view and ventral view have been reversed. I think the first column and bottom row picture is a ventral view. Please check – I may be wrong. I think the cross that produced the embryos in Panel C needs to be clearly explained and how to interpret the genotypes should be clearly explained. The images are difficult to interpret – what are we supposed to look at in the boxed insets? Explain in the legend please.

8) The images in Figure 3—figure supplement 1 are difficult to interpret. Again I suspect that if the authors told us the predicted genotypes and told us what we are supposed to be seeing in the outlined boxed areas, then it would be clearer.

9) Subsection “Generation and evaluation of dual-function alleles showing CKO with gene labeling effect at zebrafish kctd10 locus”: it the sentence beginning “Interestingly, in the initial design of the kctd10 PoNe donor…” might be easier to read if you re-phrased this sentence something like: "In initial experiments, we used only a donor with a single SV40pA termination signal sequence without the modified exon (mutExon). With such donors we were able to isolate stable integrations at the kctd10 locus and observed the correct expression pattern of tdGFP.”

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "One-step efficient generation of dual-function conditional knockout and geno-tagging allele in zebrafish" for further consideration at eLife. Your revised article has been favorably evaluated by Didier Stainier (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) The revised manuscript is much improved, and additional data demonstrating feasibility of fully conditional knockout using the new cmlc2:CreERT2 line. However, one major issue remains. It is common practice to measure the expression of targeted loci in the "off" state in homozygotes. Data can be displayed in several different ways, exemplified by Figure 2 in Ni et al., 2012 reference and Figure 1D in the Grajevskaja et al., 2018. Figure 1A in Sugimoto et al., 2017 serves as a directly relevant example of from a recently published eLife paper describing a conditional knock-in allele. This is very important. As one can appreciate from error bars in Figure 2—figure supplement 1E, Figure 2—figure supplement 2L, Figure 3—figure supplement 1E and Figure 4—figure supplement 1G, it is impossible to distinguish between 90% and 99% mutagenesis efficiency in heterozygotes (55% vs. 51% of read-through transcript remaining in heterozygotes). In contrast, the difference between 10% and 1% levels of remaining wild-type transcript should be quite straightforward to reliably quantify in homozygotes. Results of such quantitative analysis may have an impact on the choice between your described polyA cassettes (tandem SV40/GBH vs. 8xSV40). Thus, qRT-PCR analyses must be performed on embryos homozygous for Cre-excised alleles.

2) A second issue somewhat detracting from the overall quality of the work is occasionally difficult-to-read English. I would simply recommend that the final submission should be edited with the help of a professional editor.

3) Sequences of primers used for qRT-PCR should be included, along with other primers, in Supplementary file 7.

4) Why is kctd10 deleted from the Abstract?

5) Subsection “High efficient generation of a dual-function KI allele at zebrafish tbx5a locus”: Need to show hEMX1 target site on the vector in Figure 1A, and corresponding sites in vector diagrams in subsequent figures.
