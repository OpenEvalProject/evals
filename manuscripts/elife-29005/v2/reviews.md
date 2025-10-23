# Peer review - Round 1

Editors:
- Alfonso Valencia, Barcelona Supercomputing Center - BSC Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29005.038](https://doi.org/10.7554/eLife.29005.038)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Conserved noncoding transcription and core promoter regulatory code in early Drosophila development" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Didier Stainier as the Senior Editor. One of the three reviewers, James Bentley Brown, has agreed to reveal his identity.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Batut and Gingeras have collected and analyzed transcription start site data across the developmental time course for five Drosophila species. This large resource of transcription start site usage obtained at base resolution with a technology developed a few years ago by the authors (RAMPAGE). The results correspond to a temporal resolution of 1 hour of Drosophila development 5 species: D. melanogaster, D. simulans, D. erecta, D. ananassae and D.

pseudoobscura (120 samples). The analyses are based is a many as 2.7104 Transcription Start Clusters.

An analysis of the TSCs demonstrated that specific sets of core promoter sequence elements are associated with sets of TSCs that are activated at distinct times during development. This finding suggests that core promoter elements contribute to the temporal regulation of gene expression during differentiation.

The authors also reveal the presence of many TSCs that seem likely to be associated with lncRNAs and might be activated at a specific point in development.

Overall, the paper brings interesting resource to the transcription and Drosophila developmental communities that will contribute to the discussion of the role of core promoters in transcription regulation.

Comments and required revision

There are a number of aspects that require clarification. The most critical ones are points 1, 14, 17, 21, 24, 26, and 27. In general, the tone of some of the claims has to be moderated and adjusted to the actual observations.

1) The alignment of developmental profiles is crucial to the science that follows. Tried and true methods have been used to conduct the alignment, and it would also be good to generate a figure somehow visualizing the time-warping distance between the species across the developmental profile. I believe there was something similar to this between worm and fly in Gerstein et al. Nature. 2014 from modENCODE. You could also try improving on the modE graphic by making the connections between species' time-series heatmaps. You could arrange them in accordance with the phylogeny and then just show the pairwise mappings between neighboring species.

2) Figure 1A, meant to be a graphical abstract, is confusing – it seems to relate a developmental profile directly to a specific genomic locus with arrows that point at the transcribed genome… very odd. I recommend refactoring to make it clear what was done. Or even just scrap it – the project description is very clearly written, not sure a graphical abstract is needed.

3) Figure 1B looks strange. Does it make sense to use the figure to show a single pick. In any case the figure requires a better introduction (Same for 1A)

4) Figure 1E is very beautiful, but may be over-smoothed – looks worse than the data actually is. It will be better re-doing the smoothing with a narrower bandwidth.

5) A better explanation of how clade and subclades are defined will help to understand the significance of Figure 2.

6) Expression profiles are overall tightly conserved across species (Figure 2C and Figure 2—figure supplement 4A), but with substantial gene-to-gene variability:" It is not obvious from the figure.

7) The quantification of expression specificity in Figure 2D, is peculiar. Will be helpful to show the error bars, number of cases involved and significance of the differences plotted in the figure.

8) The paragraph "The high similarity of biological replicates, the accuracy of inter-species alignments for well known developmental genes, and the biological features of evolutionary divergence patterns, together confirm our ability to accurately quantify promoter expression and its variation across species. Our observations also highlight the central importance of systems level selective constraints, such as those acting on gene function and developmental stages, in shaping the evolution of gene expression." Contains affirmation that I find difficult to follow in the data shown: accuracy of alignments for developmental genes? Importance of systems-level selective constraints? Evolution of gene expression?

9) Figure 3A The 3462 promoters where divided in housekeeping and developmentally regulated, but the number of developmentally regulated genes is again 3462 (817+2047+598), implying that the H genes are all early, but how many are they?

10) Are the same clusters shown in Figure 3B and 3C? ("their tendency to co-occur 186 within the same promoters, regardless of expression timing, recapitulates the same three main motif groups (Figure 3C).")

11) "Taken together, our observations suggest that core promoter elements play a significant role in restricting windows of opportunity for expression during distinct periods of development." Would not be more accurate to say that the analysis of the distribution of core promoters shows some differences in distribution than the general promoter expression? Or, otherwise, justify where the "restricting windows of opportunity for expression" has been deduced from?

12) Similar problems with the following affirmation "TFBSs are often specific for only a subset of expression clusters within a class (e.g., Dfd or GAGA). This suggests a model in which core promoter structure defines broad developmental periods of expression potential, and precise expression timing is then refined by sequence-specific transcription factors." This seems to be an anecdotal observation transformed in an important conclusion. Can the solid evidence supporting the very important claim on the general role of core promoters be pointed out clearly?

13) Figure 3F., represents the conservation of core promoter motif between two species that substantiates a claim about conservation and validation of the motif prediction ("conserved between species far beyond random expectations (Figure 3F), which validates the overall quality of our motif predictions") Why only two species, what happen with the clades and subclades? By the way, the font size is too small to be read in a print. Same for other figures too.

14) "Indeed, some TFBSs appear to be strongly associated with specific sets of core promoter motifs (Figure 3G). Dref sites, for instance, are preferentially found along DRE and Ohler-1/6/7 core motifs." I cannot see this in the mentioned Figure 3G. DRE is associated to oh1-oh5 mte and tata. I do not know if there is mistake in the text or my interpretation of the figure is wrong, but text and figure should be reconciled. In any case, the evidence presented in the figure seems to be very light to support the claim ("individual TFBSs and core promoter motifs suggests a possible mechanism to mediate this 2-step specification of expression patterns.")

15) In subsection “Global multispecies profiling of developmental promoter activity”: The GO term analysis seems to suggest that differential rates of cell proliferation across the 5 species may drive the signal, which would be consistent with previous modENCODE results. Any chance that you already have data from which you could quantify rates of cell duplication, or even just look at approximate cell counts and then do a simple regression to confirm? No pressure, but would put this one to rest once and for all.

16) The clustering analysis is somewhat reminiscent of promoter structure analysis in zebrafish. Might be good to cite: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4820030/

17) Figure 4B is key. The analysis by profile conservation quantile seems a little be of a strange choice, where the rest of the paper is based on continuous measurements. It will be good to read the justification of the authors on this point.

18) Figure 4C-D. The positive selection panel (4D) is really not very demonstrative, is it? In any case, it needs a better explanation.

19) The results are show tendencies for three promoter elements: Initiator, DPE and TATA elements. Is justify to generalize to others ("This is consistent with the idea that core promoter motifs are indeed key determinants of this specificity")?

20) In subsection “Promoter birth and death are widespread and dynamic”; the statement that Figure 5A shows that the FDR on promoter gain/loss events is less than 0.1% is not clear, from which data does this follow? Please clarify.

21) The second part of the papers deals with the analysis of non-genic promoters. "We found a stark contrast in the degree of functional conservation of the two classes, with novel non genic promoters evolving at a substantially higher rate than genic ones (Figure 5D). There is, however, a very substantial proportion that is deeply conserved, suggesting the possibility of widespread functionality" Given the importance of this observation some quantification will be interesting. Is the 20% of non-genic promoters conserved between D. pse and D. mel, what the authors understand by "deeply conserved". How many of the 3682 non-genic promoters are "deeply" conserved? Is there an analysis of those promoters in comparison with the genic ones? How similar or different are they from the additional 291 promoters of lncRNAs added to the analysis?

22) It follows with the key question of this second part of the paper, namely: "The discrepancy between the classes may be due to a larger proportion of noncoding transcripts being devoid of biological roles and evolving neutrally. Alternatively, it may instead reflect a more pronounced tendency for noncoding transcription to take on lineage-specific roles and thereby be a driver of adaptation, as has been suggested before."

23) The analysis of the expression reveals complex heterogeneous patters that are positively interpreted as representing possible roles of the lncRNAs, obviously following the paragraph above the opposite interpretation is equally plausible. The analysis of conservation across species has to be the central argument in this paper and this is what is proposed: "Of all D. melanogaster lncRNA TSCs, 2,016 can be aligned to the D. pseudoobscura genome assembly and 1,111 are functionally conserved" (what is functionally conserved in this context?). Does this information solve the question? Is 1111 out of 2016 significant? Is the analysis of the 631 or 1529 promoters conserved across species the best solution? Would not be better a pair-wise comparison between the five species? (All what does not detract from the interesting findings regarding the conservation of the properties of the set of 631 conserved promoters of lncRNAs).

24) What is less convincing is the final argument based on the analysis of the lncRNA TSCs that are specific to the melanogaster subgroup based the results shown in Figure 6H, that shows some similarity between with the conservation profiles of protein coding gene promoters. It seems to be a little be exaggerated, based on the data presented, to conclude "Taken together, our observations show that a vast proportion of lncRNAs are indeed under purifying selection for biological functions relevant to embryonic development."

25) The arguments on the role of the lncRNA TSCs, based on conservation of a subset of them, are not sufficiently strong to close the debate on the actual role of the lncRNA, even if they may serve to point to the function of some specific cases in development control. Along this line, the argument in the final paragraph of the Discussion section, that the work unambiguously demonstrates the relevance of lncRNAs to development is also a bit strong. The work is highly suggestive, but careful knockouts or other perturbation experiments would be needed to "unambiguously demonstrate" – and even then proving that it isn't actually some short ORF would be tough. I recommend softening this language a bit to avoid raising the hackles of the lncRNA and/or the smORF communities.

26) In the third paragraph of subsection “schnurri-like RNA: A deeply conserved, developmentally regulated lncRNA gene”; the claim that the expression pattern is similar to shn seems odd. The gene shn is expressed throughout much of development (certainly through stage 16), it is not restricted to a 3 hour period as with this lncRNA. Here are the in situs of shn: http://insitu.fruitfly.org/cgi-bin/ex/report.pl?ftype=1&ftext=FBgn0003396. Do the authors mean just at this developmental period? If so, a comparison to many other expression profiles, e.g. from the BDGP, would be needed to support the association between this lncRNA and shn – is shn really the "most" similar at this period?

27) Further, the statements in the final paragraph of subsection “schnurri-like RNA: A deeply conserved, developmentally regulated lncRNA gene” that the authors have "confirmed it's noncoding nature" is too bold. The data is consistent with a non-coding transcript, but it is far from "confirmed". Absence of evidence is not necessarily evidence of absence. And on the contrary, doesn't it look quite cytoplasmic in the FISH? It encodes several ORFs > 20aa – I recommend softening this statement a bit. It looks non-coding, it's probably non-coding, but it could also encode a short ORF – to go the extra mile on this would require targeted quantitative proteomics. Not necessary for publication of course, but without it, the statement should be softened.

28) The TGF-β link is also quite a leap – it would be good to strengthen this portion of the paper with a bioinformatics analysis of the in situ imaging data against the BDGP database.

29) The observation that specific core promoter elements are associated with TSCs that are activated at specific points during development was made using the subset of TSCs that are functionally active in all species. If the analysis is performed on all TSCs observed in Drosophila melanogaster, are the same trends observed? Or is this observation specific to conserved TSCs?

30) Are the same core promoter element/TFBS trends seen for the non-coding TSCs? In other words, do you see a relationship between the promoter sequence elements for non-coding TSCs and their timing of activation?
