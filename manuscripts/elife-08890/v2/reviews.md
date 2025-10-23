# Peer review - Round 1

Editors:
- Nahum Sonenberg, McGill University , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08890.028](https://doi.org/10.7554/eLife.08890.028)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Many lncRNAs, 5'UTRs, and pseudogenes are translated and some are likely to express functional proteins" for peer review at eLife. Your submission has been evaluated by James Manley (Senior editor), a Reviewing editor, and two reviewers.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Although the reviewers agree that you have addressed important aspects of the use of ribosome profiling to identify the full spectrum of the translatome, the major deficiency of this work is the validation of the data. Many reports have already documented ribosome footprinting of unexpected RNA species, but the next advance must be the demonstration that productive translation has indeed taken place. You state: "Future work including the affinity purification of 80S ribosomes and mass-spectrometry of small peptides will provide more accurate determination of the translational status of individual transcripts." However, ribosome affinity purification has been already applied (Ingolia et al., 2014; Zhou P et al., PNAS 2013) to show that the majority of noncoding RNAs, including most long intergenic noncoding RNAs, are ribosome-bound to the same extent as coding transcripts. You must by now have validation data to add to the paper.

Ribosome profiling is a powerful technology that can be applied to identify ribosome protected positions in a genome wide unbiased fashion. You revisit one of the less explored aspects of this technique, namely to what extent ribosome profiling data can be used to identify true translation events in e.g. 5' UTRs and long non-coding RNAs. The core issue is that it is unknown to which extent non-ribosome related factors, scanning ribosomes etc. can also result in "ribosome-protected" fragments and to what extent such fragments can occur in a random fashion. You weigh in on this with a new, complementary approach to defining true translation in ribosome profiling data. You develop two tests, for codon periodicity and uniform coverage (as opposed to a single, high-abundance fragment). These approaches are different than the scoring metrics previously used by the Giraldez and Guttman groups, and this new approach is well validated here. You show that lncRNA translation tends to occur on transcripts with cytoplasmic (as opposed to nuclear) localization, which is a clear prediction of any model of lncRNA translation but has not previously been tested. You also develop several lines of evidence supporting protein-level conservation constraining a subset of translated lncRNA regions. Forty-one of these are conserved in mice, and represent candidate genes encoding tiny proteins. You argue for the translation of many pseudogenes, including continued selection on the protein-coding potential of these sequences.

The major comments that the reviewers made follow. The first, regarding validation, will require additional data, while it may be possible to address the others through modifications to the text.

1) What the field is in strong need of is a study where suggested translation events are validated at a large scale with an alternative approach than ribosome profiling. This could be mass spectrometry (there are some new approaches that identify and quantify ongoing protein synthesis events) and/or association with polysomes. Such a validation would allow for benchmarking the analysis approaches that are proposed. We believe that a reasonable number of validated targets would be 7-8, for example, from the forty-one that are conserved in mice, and represent candidate genes encoding tiny proteins.

2) Gerashchenko and Gladyshev,(2014 NAR) described a strong bias in ribosome profiling studies because of the use of cycloheximide, in particular affecting uORFs (but likely also long non-coding RNAs). It is surprising that the protocol used by the authors is not discussed in this context and it does seem possible that artifacts such as those described could indeed be a factor in the present study as well. It is unclear how the analysis approach described would deal with such artifacts.

3) Pseudogenes retain substantial nucleotide-level identity with their protein-coding ancestors. Short ribosome footprints are particularly prone to mis-mapping, and the authors don't provide details on their handling of multi-mapping reads &c. They should exclude the possibility that apparent translation of pseudogenes is a result of ribosome footprints on conventional protein-coding ancestors.

4) Can the authors comment on why transcripts with ORFs of >100 (and in some cases >200) amino acids are nonetheless classified as lncRNAs?

5) The uORF-mediated regulation of ATF4 in particular is well-studied by the Harding lab among others, and the authors should cite this literature in discussing these uORFs.

6) The authors say that, "By definition, noncoding RNAs should not be translated into protein" (in the Introduction) and "By definition, non-coding RNAs are not translated into protein" (in the Discussion). In fact, this is begging the question to some extent – there may be RNAs, e.g., that function as microRNA sponges in the cytosol but have a translated uORF whose translation is important only to avoid other translation that would interfere with this non-coding function (e.g. Ulitsky & Bartel).

7) It is surprising that about 35% of all reads do not originate from the expected periodic position (Figure 1B). This suggests that there is substantial randomness in the methodology, which would be expected to contribute to the stochastic characteristics of the data.

8) The approach presented relies on the 3 nt periodicity and random distribution (measured by entropy) of the reads across the ORF. From Figure 2A it appears that it is mainly the 3 nt periodicity that is driving the classification. Thus, one critical issue is to what extent such patterns can occur by chance under the multiple testing situations that are assessed. It is also unclear why we should assume that this situation cannot be the result of factors other than ribosomes or simply occur by chance when the authors states that "It is inconceivable that uniform 3nt period…".

9) The conservation analyses are in general relatively modest and it is hard to interpret whether this is a result of that there is a large fraction of false positive translation events and that the true ones are indeed conserved or whether there is an abundance of "unusual" translation events that are not conserved. Indeed many "peptides" are very short which would suggest a larger risk for false positive 3nt periodicity and uniform distribution of reads, especially for lowly expressed genes (it is not clear if there is bias for detecting more genes with low rpf counts as truly translated).

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Many lncRNAs, 5'UTRs, and pseudogenes are translated and some are likely to express functional proteins" for further consideration at eLife. Your revised article has been favorably evaluated by James Manley (Senior editor), and the Reviewing editor and two reviewers of the original paper. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below. Please note especially that the reviewers commented on the use of the words "inconceivable" and "invariable," which are not appropriate and can be misleading.

Reviewer #1:

The revised manuscript addresses most of my major concerns from the original submission. In particular, it does seem that mis-mapping cannot explain potential pseudo-gene translation, and I am satisfied that the sequencing data largely reflect 80S ribosome occupancy.

I have two substantial concerns with the interpretation of the data:

1) The authors say that cytosolic lncRNAs are translated "invariably" in three places including in the Abstract. This word is too strong even for the set of lncRNAs present in this sample, and more broadly, the only invariable thing in biology is the presence of surprising exceptions.

2) The authors don't seem to consider transcript isoform variation in their interpretation of uORFs and dORFs. In yeast, translated uORFs sometimes occur on small, independent transcripts (Arribere & Gilbert 2013, Pelechano & Steinmetz 2013) and so the lack of uORF-mediated repression may reflect the fact that the uORF is not translated from the same transcript as the CDS. Likewise, the highly translated dORFs may reflect translation of extensively 5'-truncated RNAs.

Reviewer #2:

Regarding the comment on "it is inconceivable the uniform 3-nt periodicity over an extended distance can result in anything other than bona fide translation". This was mainly a concern regarding scientific style. For very few findings in science, if any, should alternative explanations be inconceivable. As discussed, 3-nt periodicity is very strong evidence for translation but as suggested by the authors it could also occur via other events and thus is not inconceivable at the single ORF level. This may not only include biological aspects but also the stochastic nature of data which will suggest 3-nt periodicity with some false positive rate. The stochastic nature of the data was the main concern of this reviewer.

1) The authors seem to agree that all the reads are not expected to be derived from RNA fragments that are protected by ribosomes. The issue that I have is that there is no background model for how this relatively large proportion of the reads would stochastically result in 3nt periodicity.

In this context it would seem important to compare RiboORF to the method as described here http://biorxiv.org/content/early/2015/11/13/031625 (in press in Nature Methods) which uses an alternative approach to use the 3nt pattern.

2) Yes I was referring to the multiple-testing that is the result of testing many possible ORFs. I did not see a false positive assessment which took into consideration what is discussed under point 1. The false positive calculations seem to be for the classifier only (Figure 2A).
