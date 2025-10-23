# Peer review - Round 1

Editors:
- Luisa Cochella, https://ror.org/00za53h95 Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87865.sa0](https://doi.org/10.7554/eLife.87865.sa0)

In this manuscript, the authors describe the earliest differences in sex-specific splicing in Drosophila embryos or any animal for that matter. Based on solid data, they report the important finding that differences arise already during the first few hours of embryogenesis and that a maternally-deposited pioneer transcription factor contributes to generating these differences. The authors also provide a bioinformatics pipeline to analyze splicing over time.


---

# Peer review - Round 1

Editors:
- Luisa Cochella, https://ror.org/00za53h95 Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87865.sa1](https://doi.org/10.7554/eLife.87865.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Sex-specific transcript diversity is regulated by a maternal pioneer factor in early Drosophila embryos" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

The three reviewers agreed on a number of points, with the main ones being that:

1. the mechanistic conclusions on how CLAMP may affect alternative splicing are not fully substantiated by the data;

2. that the effect of CLAMP loss of function on Sxl is quite minimal – despite the effect at the protein level appearing to be very substantial; this apparent discrepancy raises several concerns about what direct vs. indirect effects of manipulating CLAMP.

The reviewers had several specific points in addition to this, which are attached below.

Reviewer #1 (Recommendations for the authors):

In this manuscript, the authors describe the earliest systematic differences in sex-specific splicing in Drosophila embryos or any animal for that matter. They find that differences arise already during the first few hours of embryogenesis and also identify a maternally-deposited pioneer transcription factor that contributes to generating these differences. The authors also provide a bioinformatics pipeline to analyze splicing over time.

The main strength of this paper is that the authors were able to generate pure populations of male or female embryos (using a recently published genetic system in Drosophila), and they exploited this by generating numerous genome-wide datasets. Their analyses revealed an interesting link between a maternally deposited transcription factor and alternative splicing, in particular, of genes that are differentially spliced between males and females.

A weakness of this paper is that several mechanistic conclusions are drawn from rather correlative experiments. So while the main observations are very interesting, the mechanistic model should be interpreted more cautiously.

This manuscript presents a lot of data exploring the question of regulation of sex-specific splicing by a maternally deposited factor, in early Drosophila embryos. These data show:

– Loss of maternal CLAMP affects alternative splicing of 200-400 transcripts, with a trend to affect a bit more the mutually exclusive exon category.

– This is a small fraction of the total alternative splicing events in embryos at these times, but a larger fraction of the sex-specific alternative splicing (30-60%).

– Loss of maternal CLAMP causes both loss and gain of alternative splicing events.

– ChIP-seq of CLAMP shows two types of distribution over genes: on genes whose level is affected by CLAMP, it is enriched at the ends of the genes; on genes whose alternative splicing is regulated by CLAMP, there is an enrichment over the whole gene body.

– iCLIP of CLAMP shows binding to RNA, predominantly on chromatin (experiment done in cell lines). It binds mostly mRNAs but also other RNAs

– CUT&RUN of the helicase MLE also has a dual type of enrichment over genes. Upon loss of maternal CLAMP, the signal in males looks globally lower, in females less so. But other peaks are also gained, suggesting a re-distribution.

– CLAMP is necessary for sex-specific splicing of Sxl in a manner that correlates with chromatin accessibility over the alternative exon.

The observations presented here are very interesting, but a few critical aspects of the mechanism are over-interpreted. For example, I find it hard to know whether the association with snoRNAs found in iCLIP is meaningful. By the same criteria, we should conclude that CLAMP associates with tRNAs. I think it's more likely that the proximity of spliceosomes to chromatin produces the observed signal. Also, the specific focus on particular peaks of CLAMP and MLE is difficult to interpret without more global views of how these very general proteins redistribute along the genome. Also, the connection between MLE redistribution and alternative splicing is not really explored adequately. I don't think the authors need more data for this paper, but I would suggest more concise and accurate descriptions of the data and more cautious interpretations.

Regarding the last experiments looking at splicing of Sxl, it seems unclear to me why the authors switched from the RNAi tool to ablate the maternal contribution, to a mutant allele which (if I understand correctly) ablates the zygotic contribution. It is also unclear why even though a small fraction of Sxl is mis-spliced in females, the effect on the protein level is so dramatic (!). This suggests that something else is happening in these embryos that lack CLAMP. This actually raises some doubt about what causes all the effects in the earlier part of the paper, but we cannot really compare these experiments given that the authors used very different genetic tools.

Reviewer #2 (Recommendations for the authors):

Ray, Conard et al. describe the role of the CLAMP transcription factor in the regulation of sex-specific alternative splicing in Drosophila embryos, larvae, and tissue culture cells. The results are presented from three main lines of investigation: (1) genomics in early embryos, including sex-specific RNA-seq, which is analyzed with "time2splice" a newly developed pipeline for detection of alternative splicing events; (2) iClip in cultured S2 and Kc cells. (3) Validation of CLAMP's effect on alternative splicing of core sex determination factors Sex Lethal, Transformer, and Doublesex. There is very much data included in this manuscript, and the presentation of the genomics data will require substantial clarification for readers accurately to interpret the results. At the heart of the manuscript is the observation that clamp mutants demonstrate aberrant expression or loss of expression of sex-specific genes, and the argument presented here is that this is largely due to the misregulation of splicing in clamp mutants. While the genomics data suggest that CLAMP is necessary for certain sex-specific alternative splicing events and that CLAMP interacts with splicing factors, CLAMP appears to only have a small effect on the specific examples of sex-dependent alternative splicing (Sxl, Tra, Dsx) presented as validation. The findings also catalog for the first time the splice variants present at the maternal-to-zygotic transition, but the current analysis of these data leaves open the question of whether such alternative splicing events are associated with zygotic transcripts, and whether the magnitude of CLAMP's effect in this process is significant.

– The title of the manuscript touts the regulation of alternative splicing by a maternal pioneer factor, but a substantial proportion of the data is derived from cultured cells or third instar larvae, where the maternal contribution of CLAMP is not substantial. It is also unclear what pioneering per se has to do with the mechanism the authors propose and what little connection they present is not focused on in any validation or mechanistic follow-up work. I recommend changing the title to de-emphasize CLAMP's maternal expression and pioneer activity.

– Throughout the manuscript, but particularly within the description of the RNA-seq results, the number of objects (genes, transcripts, splicing events, peaks, etc…) are rarely stated explicitly in the text, but are instead sometimes part of figures or legends, if they are stated at all. Please edit the manuscript throughout to indicate the number of objects being compared and include percentages of the relevant group when discussing specific categories (e.g., x% of total genes/transcripts are alternatively spliced (n/N). Y% (n) of alternatively spliced genes/transcripts are sex-specific. Of these z% (n) are zygotically expressed.). As written, I was unable to clearly evaluate the biological conclusions for the first half of the manuscript because I had to rely on non-quantitative descriptors provided by the authors to glean magnitudes: for example, "very low levels," (line 260).

– In terms of the magnitude of the effect: piecing together information in Figures 1 and 2, there appears to be 10891 total (genes? transcripts?) in the 0-2 hour female RNA-seq data. Figure 1B implies that 16.27% (1771) of these are alternatively spliced. Can the authors comment on what an expected range of alternative splicing would be for a 'typical somatic cell' of any sort?

– For Figure 2D and associated text, the authors address whether CLAMP-dependent sex-specific alternative splicing is observed mainly in zygotic genes. I have several issues here. Mainly, I am unclear on how this comparison is being made (partly because of the lack of numbers in the text). The numbers of sex-specific AS genes in the legend are different than the numbers in the Venn diagrams. From the minimal explanation of how this was done, the impression is given that if an AS gene was not one of the 841 maternal genes, then it is likely to be zygotic. This does not follow logically, given that most of the 0-2 hour transcripts (~10891?) will by definition be maternal, and that non-membership in this limited list of 841 maternal genes (from which source?) cannot directly imply that the gene is zygotic, since most of the remaining transcripts will be maternal but not included in the limited list of 841. There are near-exhaustive gene lists of purely zygotic genes (DeRenzis/Wieschaus), and maternal-zygotic genes (Chen/Zeitlinger, Kwasnieski/Bartel). This analysis may be enhanced by enumerating the fraction of purely zygotic genes and maternal-zygotic genes. This is an important analysis and should be (1) re-done, and (2) documented extensively (with accurate numbers).

– Corollary to the above point: the 10891 number (Figure 2A): does that refer to unique transcripts (tx) or unique genes (gn)? The enumeration requested in the above point should clearly state that the numbers are tx or gn, and if tx, the total number of gn represented by that value should be cited. Comparisons with published gene lists should be done in the appropriate 'unit' (tx or gn), dictated by the published list.

– The authors should comment on how a maternally supplied transcript could be alternatively spliced in a sex-specific manner. At least some of the sex-specific alternatively spliced genes are identified as being maternal in Figure 2. Are these maternal genes that are also zygotically expressed? Are the maternal isoforms consistent with the female zygotic isoform? Any detection of sex-dependent alternative splicing in solely maternal genes (i.e., not zygotically expressed) could indicate issues with the computational approach for scoring AS events and should be discussed.

– One of the differences between Kc and S2 cells is their sex, but this does not mean that any difference observed between the two cell types is sex-specific. The section beginning at line 335 reads as if 100% of the differences between Kc and S2 cells is interpreted as a sex-specific difference. In any case, I also felt that the results from this section should be confirmed in embryos somehow, perhaps through an RNA IP experiment. snRNAs should be abundant enough that they can be detected in a CLAMP IP, even from early male or female embryos.

– Section beginning line 514: In general, one of the weaknesses of this paper is that it switches between embryos, larvae, and cultured cells, without much critical evaluation of whether such different contexts impact the strength of the conclusions. In this case, I am puzzled why the authors choose to solely rely on MNase-seq in cultured cells to make a point about CLAMP-dependent chromatin accessibility when they have also performed ATAC-seq on CLAMP-knockdown embryos. The observation that loss of CLAMP leads to a greater amount of accessibility at Sxl exon 3 specifically in Kc cells (which is presumed to be because these are female cells but could instead be a cell-type specific effect independent of sex). Such a large effect should be evident in mixed-sex embryo collections from a CLAMP knockdown, and these data should be shown and presented in the Results. Are sex-specific differences in CLAMP binding observed by ChIP-seq at this locus? This data would be essential to show as well.

– The magnitude of the effect of CLAMP loss of function on Sxl splicing, however, does not seem to be very large, given the near absence of Sxl protein in female larvae. Can the authors clarify how they interpret this discrepancy? The same could be said for the MXL results. Is the regulation of splicing only a minor function of CLAMP?

– I have not yet reviewed the supplemental tables for completeness and suitability for use in follow-up studies. This should be revisited during the consultation.

Reviewer #3 (Recommendations for the authors):

In flies, it is well established that sex determination is controlled by gender-specific alternative splicing of the sxl gene. The current study extends the catalog of embryonic alternative splicing events, including numerous new gender-specific splicing events. The primary data set is RNA-seq from pre- and post-zygotic gene activation gender-specific embryo samples collected using the meiotic drive. The study identifies 92 transcripts differentially spliced between genders at 0-2 hours post fertilization, and 138 at 2-4 hours post-fertilization. A small subset (4) of splicing events were validated by alternative methods. In general, these data are convincing, though more validation would strengthen confidence in the data set.

The data are then compared to existing RNA-seq where maternal CLAMP is depleted. CLAMP is a candidate maternally deposited alternative splicing regulator. Between 30-50% of gender-specific splicing events are CLAMP-dependent, while only 2-3% of total splicing events are CLAMP-dependent. The authors suggest these results indicate a specific role for CLAMP in regulating gender-specific alternative splicing. The overall number of CLAMP- and gender-specific alternative splicing events is fairly low (<50) compared to the total number of alternative splicing events detected (>10,000). Having said that, the enrichment is significant by Fisher's Exact Test, and subsequent binding experiments provide additional support for the model.

Next, the authors performed gender-specific ChIP-seq to map positions of CLAMP binding in embryos as a function of the developmental stage. Approximately half of the CLAMP-dependent gender-specific alternative splicing events show CLAMP enrichment on the DNA of alternatively spliced genes. This suggests (but does not prove) that CLAMP could be directly regulating co-transcriptional alternative splicing of gender-specific events. CLAMP also binds to some gender-specific mRNAs revealed by iCLIP data sets from male and female cell lines. This binding is enriched in RNAs that co-fractionate with chromatin, suggesting that DNA and RNA precipitation is coupled. CLAMP also appears to bind to snRNAs and components of the spliceosome, and loss of maternal CLAMP causes redistribution of the MLE complex, especially in male samples.

Finally, the authors show that CLAMP plays a role in regulating sxl alternative splicing, and this role correlates to CLAMP-dependent chromatin formation.

All told, the experiments point to a model where CLAMP regulates alternative splicing for a limited subset of embryonic transcripts, about half of which are gender-specific alternative splicing events, through a mechanism that involves DNA binding, RNA binding, and chromatin conformation. This is a fascinating outcome for a variety of reasons, as the concept of broad parental control over progeny splicing patterns has not been widely explored. It seems clear that the mechanism proposed accounts for a small fraction of the observed embryonic alternative splicing. There is no evidence that the novel alternative splicing events detected are important for embryogenesis or sex determination. Nevertheless, the results do move the field forward and provide testable hypotheses that can be addressed in future studies.

In all cases where data is presented as a percentage, it would be MUCH CLEARER if both the numerator and denominator were presented, along with a p-value. For example, on line 279, it states "43.8% of all CLAMP-dependent sex-specifically spliced genes are bound by CLAMP:" This should be followed with (num/denom, p-value XXX) so it is clear to the reader that this percentage is meaningful and how large (or small) of a list of genes it describes. This should be done throughout the manuscript.

Several key experiments are relegated to supplementary information (for example, the volcano plots in figure S2). Where possible, critical experimental data should be moved into the body of the manuscript and confirmatory analysis placed in the supplement.

Some of the rationale was missing from the text, for example, the chromatin fractionation for the iCLIP data sets. I think I understand why this was done, but it should be presented.

The paper would be stronger with functional studies to assess the biological importance of the CLAMP-dependent sex-specifically spliced genes, although the manuscript is already overloaded with experiments and it strikes me as unreasonable to request more.

The work as presented is difficult for the reader to get through. The paper would benefit from significant rewriting. I found significant overlap between the introduction and Results section, with several concepts and rationale presented in both sections. Also, in one case (concerning sxl) introductory material was first presented in the Results section. The reader would benefit from a more succinct presentation. In fact, the authors might wish to consider splitting the work into more digestible chunks, for example, a description of gender-specific alternative splicing events/stage-specific splicing events along with a more detailed description of the pipeline used to identify them, and a CLAMP paper with more functional characterization of the impact of CLAMP targets on embryogenesis. Ultimately, this decision is up to the authors, but I would ask them to consider it for readability/clarity's sake.

There are some typos that should be corrected (line 344 "most CLAMP RNA binds to hundreds of RNA", line 340 "Although CLAMP do not have a canonical RNA recognition motifs").

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Sex-specific transcript diversity is regulated by a maternal transcription factor in early Drosophila embryos" for further consideration by eLife. Your revised article has been evaluated by Kevin Struhl (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

After careful review and much further discussion, the reviewers agree that the premise is very interesting and the data are original and valuable. However, they also all agree that the paper tries to tell a story (or even multiple stories) that are not fully substantiated by the data. The data are overinterpreted in a number of places and that leads to a main storyline of CLAMP being a critical regulator of splicing that the reviewers (4 in total by now) do not think is substantiated. They do not dispute that there are effects on splicing, but they do not think that the data support the mechanism proposed to explain these, or that these changes are functionally meaningful (relative to other functions of CLAMP).

The editors and reviewers would be willing to evaluate a revised version of this manuscript, but this would require a very significant rewrite to more accurately and clearly present and interpret the data. No new experiments are required (although they can be added). At this point, the reviewers are undecided about whether the current version should be rejected or sent back for revision. To facilitate the decision and to save time, they have suggested that you first send back a revised abstract that indicates how you will address the main criticism. If this revised abstract satisfactorily addresses the main issue, the decision will be "revise" under the assumption that the bulk of the paper is changed in accord with the revised abstract.

Reviewer #1 (Recommendations for the authors):

In this manuscript, the authors describe the earliest systematic differences in sex-specific splicing in Drosophila embryos or any animal for that matter. They find that differences arise already during the first few hours of embryogenesis and also identify a maternally-deposited pioneer transcription factor that contributes to generating these differences. The authors also provide a bioinformatics pipeline to analyze splicing over time.

The main strength of this paper is that the authors were able to generate pure populations of male or female embryos (using a recently published genetic system in Drosophila), and they exploited this by generating numerous genome-wide datasets. Their analyses revealed an interesting link between a maternally deposited transcription factor and alternative splicing, in particular, of genes that are differentially spliced between males and females.

A weakness of this paper is that the argument that CLAMP's effect on splicing is functionally meaningful is not fully substantiated by the data.

Whereas the observations that loss of CLAMP affects the splicing of a set of genes, many of which seem to be involved in sex determination, a number of other observations do not fit with the "master regulator of splicing" role for CLAMP that the authors are pushing.

For example, the authors show that in early embryos, where they detect xxx genes show CLAMP dependent splicing events, only 8-20% of these genes are actually bound by CLAMP. In later embryos they say 60-65% of genes affected by CLAMP are also bound, but CLAMP may be binding to a very large number of expressed zygotic genes at this time. There are no statistics to show that this overlap is meaningful. It is true that the pattern of CLAMP binding is different in different subsets of genes, but there is no concrete information of how many genes were used to generate the plots in Figure 3, making it difficult to evaluate the meaning of these data.

Moreover, the authors compare CLAMP binding to RNA and CLAMP-dependence on splicing for the two cell lines they use (as they only have CLAMP RNA binding data for the cell lines). In these data, 452 genes show CLAMP-dependent changes in splicing, but only 54 are bound by CLAMP and the authors say only 10 genes are direct targets of CLAMP-mediated splicing regulation. The authors conclude that the rest of splicing regulation is due to mis-splicing of other splicing regulators and are thus indirect effects of CLAMP. If such a small fraction of binding sites correlate with splicing changes, how can we interpret other analyses that take into account all CLAMP binding sites?

Similarly, the overlap between CLAMP and MLE binding is minimal, yet the authors conclude that CLAMP "sequesters" MLE and prevents it from binding at specific sequences. But there seems to be a lot of MLE binding that is completely independent of CLAMP in wt, so it's unclear how the authors propose CLAMP is preventing MLE from undesired binding.

An original concern was that even though the relatively minor effects of CLAMP on alternative splicing are an interesting observation, there is no indication of the functional significance of these changes. The authors claimed to have addressed this, but this is not the case. There is still no indication that any of the changes in splicing are functionally significant. I don't mean to say that it is not important to document these changes, but all claims of functionality are not supported by any piece of data. The key regulator of sex determination, sxl, whose splicing is somewhat changed, is affected by the loss of CLAMP in a much stronger way at the protein level than at the alternative splicing level. It is thus not fair to say "We demonstrate the functional significance of CLAMP-dependent alternative splicing by determining that CLAMP-dependent changes in sxl splicing in females induce the formation of the male-specific lethal dosage compensation complex in females that never normally occurs". This could all be due to the extremely reduced level of sxl at the protein level.

Another concern was the question of uncoupling the effects of CLAMP on transcription and splicing. The authors provide some comment that 85% of genes affected at the level of splicing are not regulated at the level of transcription, but there is no data shown or any details as to how this comparison was done.

Overall, the paper has not changed much from the previous version we reviewed. The authors present a very large amount of data. These are not always totally clear and often seem over-interpreted. I still do not think that the strong push for a role of CLAMP as a master regulator of splicing is substantiated.

Reviewer #2 (Recommendations for the authors):

The authors of this manuscript have added significant additional data to support a role for maternal Clamp in the regulation of sex-specific alternative splicing. These data, while correlative, help to convince me that regulation of alternative splicing is a major function of Clamp. Intriguingly, the new data present yet another mechanism of Clamp-dependent gene regulation through 5'UTR association and FMRP-dependent regulation of translation. This surprising finding helps put to rest a concern from the previous version of the manuscript, where the reduction of Sxl protein levels seemed to poorly correlate with the magnitude of the change in splicing observed. As such, it would seem Clamp's major role in Sxl regulation occurs at the level of translation control, as opposed to splicing or transcription initiation. An additional complication that will warrant future investigation.

The manuscript is dense and completely packed full of data and analyses. This strength is also its flaw, as it remains challenging to follow the thread of the story at times as the models and assay systems change. Nevertheless, I feel that it is important that the work should be published without further delay so that others may benefit from the discoveries and data sets described in this work.

I have a few suggestions for the authors about ways to help clarify the presentation.

1. It would be wonderful if the figure legends would include the identity of the assay used to collect the data. For example, the legend for Figure 4E does a great job of this, but Figure 3, the rest of Figure 4, and Figure 5 would benefit from the same level of detail. This saves the reader from jumping back and forth so much between the text, the figure, and the legend while trying to understand the data.

2. The rationale for using specific statistical tests should be presented in the manuscript and/or legend. Perhaps a section in the methods for statistical analysis? For example, Figure 1D relies upon a chi-square test (why not ANOVA?) while Figure 2A relies upon Fisher's exact test. I think I understand why (sample size), but I'm guessing. Figure 2E the p-value range is not clear for the left and center panels.

3. Did the authors mean to use "transcriptions" on the left axis of Figure 2A graph or "transcripts"?

4. The 5'UTR in figure 7C should be labeled.

Reviewer #3 (Recommendations for the authors):

In this manuscript, the authors carry out a detailed examination of sex-specific gene expression and pre-mRNA splicing during early Drosophila embryogenesis. They take good advantage of a meiotic drive system that had been previously implemented in the PI's lab to enable the collection of sufficient amounts of properly sexed embryos to perform various genomic assays. The authors carry out transcriptome (RNA-seq) and chromatin (Cut&Run) profiling experiments in the presence or absence of a maternally provided transcription factor, called CLAMP (chromatin-linked adaptor for MSL proteins). They analyze two different developmental time points (0-2 hrs and 2-4hrs after egg laying) corresponding to pre- and post-ZGA (zygotic gene activation) embryos, respectively.

This is a huge manuscript (80+ pages) with a ton of supplemental figures and data. There is a lot to like here, but in my view, the manuscript needs further revision. Most of my critiques can be addressed without further experimentation. There is a good story here but I feel that the stronger points get diluted by the weaker arguments.

Response to Previous Review

I did not participate in the previous round of review and so have tried to avoid bringing up new points that were not raised in the first round. Rather than diving into the details straightaway, I would say that the main criticism raised by the referees was one of data over-interpretation. Personally, I am not comfortable making deep mechanistic conclusions (e.g. an association with the catalytic step 2 spliceosome) largely on the basis of genome-level analyses. After reading the revised manuscript and the response to the review I still feel that some of the data are being pushed beyond their limits. The authors' model may well be correct, but the narrative in many parts of the manuscript goes from a given finding being what I would say is "consistent with" a certain interpretation, rather than one that actually "suggests" it works that way.

General points

1. CLAMP is a general transcription factor, but it has a well-documented role in the histone locus body (HLB), located at the histone gene complex (HisC). Reduced expression of histones can have major effects on gene expression (on both transcription initiation and downstream RNA processing steps). The potential for pleiotropic effects on transcription (e.g. elongation rates are known to affect splicing) due to reduced histone dosage is not really mentioned.

2. Line 142. Claims of primacy should be removed from the Results section. That sort of thing can be used in an introduction summary or in the discussion of the results. Using it as a conclusion in the Results section ("Therefore, we defined sex-specific splicing events in the early embryo for the first time.") just seems a bit odd.

3. Some aspects of the Results need to be reworked. Probably got mixed up in the revision. As it now stands, the subsection starting on line 150 is redundant and out of sequence. There is a whole list of reasons for doing these experiments in the Intro (lines 78-87), seems like line 150 starts to make the same arguments over again. Furthermore, the information on lines 154-159 really should have been introduced on/near line 128 where the authors first present results of splicing analysis following CLAMP depletion.

4. Line 188. The way that this sentence is written, the authors have already concluded that CLAMP regulates splicing. At this point in the narrative, loss of maternal CLAMP could affect SSS by any number of indirect means. "Regulation" implies something more active. So I'm not sure you can say start off with: "Furthermore, 85% of genes at which clamp regulates SSS…" because it assumes facts that are not in evidence. I apologize if this comment sounds picayune but this sort of logic matters when you are building an argument.

5. The Cut&Run data in Figure 6 are curious. I worry that there is some sort of normalization problem with the dataset. In the peaks that were identified in the male control embryos (panel A), roughly two-thirds of the sites on the autosomes and half the sites on the X chromosome are essentially flat. Does that mean the peak that was called by MACS2 is really more than 1.5 kb wide? Maybe that makes some sort of sense on the X. But on the autosomal sites, it looks like noise. The signal in the flanking regions next to the sharper peaks in the second heatmap column (Male control) looks too high. Well above the background binding levels in all of the other columns. This suggests that maybe there are simply more reads in this sample. I cannot tell without seriously digging into it. Is MLE really coating large chunks of chromatin on the autosomes?

Why is there such an abrupt transition from the set of narrowly defined peaks to a set of wide, shallow ones? If there were some sort of second criterion one could use for peak calls then you might be able to exclude (or include) certain regions. Right now it just looks like autosomal noise.

Again, for the autosomes at least, it might make some sense to try and find a common set of peaks that are found in both the male and female control samples. Then look at the effects of CLAMP depletion on that subset. In addition to a heatmap, one could use DESeq2 to quantify the difference in a metaplot for males vs females (+/- clamp).

Specific ideas for revisions:

Figure 1. Panels A and D. The multiple uses of various shades of gray in panel D versus similar shades of gray in panel A are confusing. This could be improved with color to make it a bit more readable. In panel A, I suggest that the authors use a unique color for each of the "differential" exons (currently they are all in black) examined in the 7 classes. Then shade the corresponding bars in panel D with that same color (one of which could be black). That way you can continue to use gray in panel A for the exons that are not differentially analyzed.

Figure 2E and lines 212-214. Most of the SSS genes in the early female embryo encode transcription and splicing factors? This statement is not at all obvious or even well supported by Figure 2E. There are two dots, one roughly 3 genes and the other 6-7 genes? What is the numerator? What is the denominator? Why should I believe this finding is significant? Why is the adjusted p-value bar all one shade in the two on the left? More stat power in the third GO term panel? I feel like the major points being made in Figure 2A-B get diluted with the additional panels and Venn diagrams. Better to focus the reader on solid conclusions.

Lines 239-274. Three full paragraphs of text are assigned to Supplementary figures. Does that not seem excessive? If the RNA-seq data regarding zygotic CLAMP expression are not going to be presented in the main body figures, why so much text? This leads to Figure 3.

Figure 3. Important points are being made here, but I fear some of the points are getting lost in the blizzard of metaplots. I don't have any good suggestions for how to streamline but it seems if a few key points could be distilled out of Figures3, and from the supplementary tables cited in the three paragraphs above (lines 239-274), that a single main-body figure with most important points would be impactful.

Figure 4. This whole figure should be reworked and most of it sent to the supplement. Panel E should be deleted. The information content in panels C and D is really low. That leaves A and B. What are the points being made in these panels? I don't think that the authors make much out of the motifs in the text. So the main points.

Figure 5 (see general points above). Reanalysis seems to be in order.

Figure 6. This figure may need some reshuffling or even split in two. I think that most of the readers of the paper will be confused by the fact that the males do not show any male-specific splicing in panel B. After reading the nuanced text (lines 519-520) a couple of times, where the authors mention that the embryos have not yet become "fully specified," I realized that this is actually the expected result. Maybe the authors should lead with that. Or be more explicit. In fact, I'm not even sure the pre-ZGA transcripts of Sxl are even translated in the early embryo. But that's a story for another time.

In this part of the manuscript, I don't think the reader is quite ready for panel A, which could be combined with panels D and E to make a new figure. Meanwhile, it might be helpful to bring back two of the panels from the older version of this figure (currently in Figure S11). The gene model in the current panel C (X-axis) is poorly annotated and the Y-axis is unlabelled. I found the panel particularly unhelpful and had to look at Figure S11 to figure out what was going on. I suggest bringing back panels S11A and S11F into the main body somehow. This would show the casual reader that later on in development splicing works the way it is depicted in all the textbooks. Then explain to the reader that early embryos have, by definition, maternally spliced Sxl transcripts. The authors have RNA-seq data that for these time points, why not use them? Analysis of splice-junction reads in the RNA-seq could be added to flesh out an entire figure about Sxl splicing.

A new figure could be used to show the pathway and the splicing of Tra, Dsx, Msl2, etc.

Figure 7. The overall model. I don't know what to say about the current Tfigure other than it's pretty complicated. The biology is complex, so I get it. But am worried that the authors' main points are going to be lost on a readership that will not appreciate all the nuances.
