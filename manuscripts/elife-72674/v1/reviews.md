# Peer review - Round 1

Editors:
- Antonis Rokas, Vanderbilt University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72674.sa1](https://doi.org/10.7554/eLife.72674.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Approaching the search of novel viruses while in an endogenized stage, rather than as free virions, the study by Hackl et al., reveals a large diversity of complete and fragmented virophage genomes – termed EMALEs – scattered throughout the genomes of four strains of the marine protist Cafeteria. Given that the activation of the integrated virophage mavirus during infection by the giant virus, CroV, has been shown to have a protective effect on the Cafeteria population, this study provides a tantalizing window into the traces of virophage-giant virus¬-protist interactions in the marine environment. Given the enormous diversity of virophages and giant viruses that have been found in metagenomes with no known hosts, this study is a step towards deciphering the biology of these viruses.

Decision letter after peer review:

Thank you for submitting your article "Virophages and retrotransposons colonize the genomes of a heterotrophic flagellate" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and George Perry as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Frank Aylward (Reviewer #1); Chantal Abergel (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers made several suggestions and comments that, if addressed, would significantly strengthen your manuscript and clarify its presentation, so i recommend that you consider them and revise accordingly. In particular, please address the following comment:

1) All reviewers were curious/raised questions about the evolutionary analyses used to identify EMALE and NGARO endogenization and loss and so some clarification from the authors about the specific points raised in their analytical process would be beneficial to the article.

Reviewer #1 (Recommendations for the authors):

Small note on nomenclature. In a few situations the authors use the terms EMALEs and virophage interchangeably, which can be a bit confusing because it is not clear if they are referring to the same thing or if there is some implied difference here (i.e. line 102). This is especially true in the Results section, where it would be clearer to just use EMALE for everything since that term was defined specifically.

For the 7 Ngaro elements in EMALE genes (line 326) it would be useful to have a full breakdown of the predicted function of these genes here. And is this section a discussion of all Ngaro elements or only those found within the 33 high quality EMALEs? That was unclear to me.

It would be useful to note the Pfam domain of the Ngaro elements the first time they are mentioned in the text (or if Pfam is not preferred for some reason some alternative protein family, such as an NCVOG or Interpro ID). This would help to more precisely define these elements for readers. It is also unclear in the Methods how the Ngaro elements were identified- I understand this probably involved manual curation to some extent, but it would be useful to know what features the authors looked for when performing these analyses (best BLASTp hits, Pfam domain hits, etc).

Are homologs of the Ngaro genes found in giant virus genomes? This could be advantageous to giant viruses due to their potential to inactivate virophage. It would be interesting if giant viruses promoted Ngaro gene proliferation. Proteins for a collection of NCLDV and their Pfam annotations are publicly available on the Giant Virus Database (https://faylward.github.io/GVDB/), so it may be easy enough to check what the distribution of these elements across the diversity of NCLDV looks like. If the authors chose to do a quick survey of Ngaro elements in other NCLDV it would increase the breadth and impact of the study, but this is not strictly necessary.

The authors provide an interesting discussion on why a previous study found many fewer endogenous virophage (Blanc et al., PNAS 2015). I reviewed the methods of this study and found them to be quite robust, so it is rather surprising that more endogenous virophage were not found. Hackl et al., rightfully point out that assembly issues may mask the presence of these elements. Another important point is that many fewer reference virophage were available in 2015, so homology based methods were more limited at this time.

The skew towards EMALE integration in intergenic regions is interesting. Given the accumulation of junk DNA in many eukaryotic genomes I would actually predict that many degraded EMALEs would not be removed through purifying selection, and that they would accumulate (though given the high effective population size of these marine hosts it is possible). Is it possible that this bias is due to the difficulty in identifying degraded EMALEs? Perhaps there are more degraded EMALEs in the genome but they are just harder to detect? (see comment below).

Perhaps I missed it but I could not find information on how the EMALEs were initially identified and delineated in the Methods. The results state that "To identify endogenous virophages, we combined sequence similarity searches against known virophage genomes with genomic screening for GC-content anomalies. The two approaches yielded redundant results and virophage elements were clearly discernible from eukaryotic genome regions based on their low (30-50%) GC-content (Figure 1A)". To me this seems quite general and it is not clear what tools were used- for example, I am assuming that sequence similarity searches were done at the amino acid level, and if so was this done with the genes already predicted from the previous Sci Data paper? This is an important detail since gene prediction algorithms often miss NCLDV and virophage genes. In the Scientific Data publication the gene prediction was done with "the BRAKER pipeline which utilizes BLAST Augustus and GeneMark-ES. Augustus and GeneMark-ES gene models were trained with publicly available transcriptomic data of C. roenbergensis E4-10P as extrinsic evidence". If EMALE genes are extensively pseudogenized or not expressed would this pipeline still predict them? More details on EMALE detection and some commentary on the possible limitations of degraded EMALE prediction would be useful.

EVEs necessarily exist on a spectrum from intact to degraded, and the reality is that the most degraded elements may consist of only a single pseudogene and may not be confidently detected using any method. I often think of this, since eukaryotic genomes are full of junk DNA with ambiguous origins- one hypothesis is that much of it derives from endogenous viruses that subsequently degrade beyond all recognition. Some additional discussion of this be useful for interpreting the consequences of retrotransposition, since one would expect that these would actually inactivate quite a few EMALEs and effectively turn them into junk DNA.

Reviewer #2 (Recommendations for the authors):

I was only wondering why the authors did not perform an experiment to assess the reactivation of the type 4 EMALEs upon CroV infection as it would nicely demonstrate they are functional MGEs. This would also address the need for another giant virus for EMALEs presenting different promoters.

To me it is not mandatory but would nicely complement the present findings.

The reading of this manuscript also raised one question. Since some groups only possess rve integrase and some present an additional Tyr recombinase, I was wondering if one could be meant for integration into the host genome while the second could be for integration into the giant virus genome, as it is the case for Sputnik which only have the Tyr recombinase and only integrates into the giant virus genome.

I also have a naïve question concerning the pseudogenized EMALEs without Ngaros retrotransposon. The authors addressed this question on the role of Ngaros in EMALE pseudogenization but focused on complete versus absent and did not look for remnants of possible Ngaro. Could pseudogenization in the ones without Ngaros be the result of ancient integrations that disappeared, just leaving for instance the A, B signatures in these EMALEs?

I noticed that in Figure 1 legend B is difficult to read and legends for C and D panels are missing.

In Figure S7, I was wondering what was corresponding to the gap between c023 and c119 for E4-10which appears to be covered by GC content analysis. Same in panel B for RCC970, between c188 and c258 for which a possible explanation is provided, yet the GC content seems to cover this gap.

Reviewer #3 (Recommendations for the authors):

This is a very thorough analysis and raises many avenues for future work.

I found myself speculating on how the biology of the system is working in terms of the gain-and-loss of EMALEs, with one idea for an analysis that could be done. I am not proposing this as additional work, but I am curious if the authors had already looked into something along this vein. Presumably complete EMALEs are relatively recent acquisitions while fragmented EMALEs have been inactivated by random processes (point mutations followed by larger insertion-deletions) and are therefore more ancient. Have you looked at making phylogenies for the core morphology module genes in the EMALE fragments to see if they represent more basal types?

Below are some points where some additional details would provide clarification.

– Were there other GC-low regions that did not correspond to EMALEs? It is curious that the genome seems so uniformly GC high.

– Do lone ngaro elements seem to be integrated in GC-low regions?

L410 "either of the three fractions" What are the three fractions? Do the authors mean "host", "EMALE" and "NGARO"?

Why were only PacBio reads used to quantify the percentage of EMALE/NGARO and not also the Illumina data? Was it due to GC bias?

L415 "samtools v1.9(47)" Missing space before the citation.

Figure 1

The size of (B) is a bit small so it is a bit hard to decipher with the symbols.

The description of (B) could do with a better description that states the lines represent contigs in decreasing size ordered from left to right and top to bottom.

The legend is missing descriptions for parts (C and D).

Figure 2

A description in the legend of what the terms in the plot "complete" "FALSE" and "TRUE" refer to is needed.

Figure 3.

Perhaps instead of the dashed line separating the region of homology between types 1 and 2, another line at the 5' end would better show it as a block of homology.

What program was used to produce the genomic maps?
