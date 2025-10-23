# Author response - Round 1

Authors:
- Darpan Medhi
- Alastair SH Goldman
- Michael Lichten ([ORCID: 0000-0001-9707-2956](https://orcid.org/0000-0001-9707-2956))

## Response text

DOI: [10.7554/eLife.19669.020](https://doi.org/10.7554/eLife.19669.020)

[…]

Essential revisions:

In order to fully validate the interpretations, some additional experiments are needed using the tools that the authors have used in the present experiments. In addition, the authors should not over interpret the data which is based on the comparison of two loci (HIS4 and URA3) with a correlation with HOP1 occupancy. There are a large number of possible differences between these loci aside from the ones the authors focus on, and it remains possible that the direction of the correlation seen with these two loci remains purely coincidental. Pch2 mutant fits the expectation but absence of Pch2 has likely several other consequences. The Abstract and conclusions should be modified accordingly. Use of SEM should me revised.

Please see below for additional work and manuscript changes that address these concerns. We have rewritten the Abstract to modify its overall emphasis, and have also added text to the Discussion that explicitly addresses the above concern about coincidence:

“The observation that some COs at HIS4 are SSN-dependent, even though most are MutLγ-dependent (Figure 3), indicates that this division is not absolute. […] It remains possible that the association seen at HIS4 and URA3, rather than being directly causative, reflects another underlying aspect of meiotic chromosome structure or function, and that other differences betweenthese two loci cause the observed differences in resolvase usage.”

It should be noted that an emerging consensus is that Pch2’s primary activity involves remodeling HORA-domain proteins (see Rosenberg and Corbett, JCB 2015 for discussion). This makes it likely that the varied meiotic phenotypes of pch2 mutants are all a consequence of altered Hop1 distributions, but of course altering Hop1 occupancy will affect many different meiotic processes; thus, the text above, in particular the last two sentences.

1) In order to evaluate the generality of their findings (see general comment above), the authors could compare published ChIP-seq data of Hop1 with available genome wide recombination maps from resolvase mutants.

This is a great idea. Unfortunately, currently there are not sufficient tetrad data to make a locus-by-locus comparison. The only available SSN mutant data are for a mms4 meiotic depletion strain (Oke et al., PLOS Genetics 2014), with a total of 596 crossovers in 7 tetrads analyzed, or a scored crossover density of about 1/17kb. Nishant K.T. and collaborators have (unpublished) crossover data for 19 mlh3 tetrads from an S288c-YJM789 hybrid strain that they have made available to us, but even at this higher crossover number (1224, 1CO/8 kb), there are not enough to confidently score differences between wild-type and mlh3 on a locus-by-locus basis. We are currently exploring strategies to divide the genome into bins with different Hop1 enrichment levels and examine relative Mlh3-dependence of crossovers in each bin, but this is a complex problem that is going to require considerable work before we even know if the current mlh3 dataset is of sufficient size.

2) One important experiment missing in this paper is to demonstrate the requirement for ssn in pch2 mutant and thus to analyze intermediates, COs and NCOs in pch2 mms4 yen1 slx1 mutant.

We did these experiments and they are presented in Figure 4 and Figure 4—figure supplements 1 and 2; corresponding text has also been changed (subsection “Altered Hop1 occupancy in pch2 mutants is associated with altered MutLγ−dependence of VDE-initiated Cos”, last paragraph).

3) Since there are only two replicate datasets for several analyses, error bars should show range rather than SEM for the time-course plots. Bar graphs should be replaced with univariate scatter plots, but if the authors wish to retain the bar graphs, then error bars should show range, not SEM. This paper in PLoS Biology provides an excellent discussion of pitfalls for bar graphs and suggests other strategies for data display: http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128

Error bars were changed to range in all but Figure 3C, D and Figure 4C, D, where error bars were removed (see below). Figure legends were appropriately changed.

We did not convert bar graphs to scatter plots, as they do not report primary data. Primary data are presented as line graphs and also in Supplementary file 2. The bar graphs are used to summarize features of the data, with the goal of visually communicating conclusions.

Weissgerber et al., cited in the reviewers’ comments, object to bar (and line) graphs because they do not “allow readers to critically evaluate continuous data”. In our paper, data are clearly presented in other figure panels and in a data supplement, so the interested reader has plenty of opportunity for evaluation. Weissgerber et al. dislike bar graphs because they conceal differences in distributions (including outliers), in sample size, and in relationships between dependent variables. In our data, there are no differences in sample size (2, in each case), in distribution relative to the mean (can’t be, with 2 values), and variables are independent. Therefore, the issues that motivate Weissgerber et al. are not relevant to our paper.

In the case of Figures 3 and 4, panels C and D, it is not possible to convert error bars to “range”. This is because the values are the mean of 8 and 9 hr samples in two independent experiments with the indicated mutant (all 4 values averaged), divided by a similar mean for the indicated wild-type strain. Since the values are the ratio of two means, range is not applicable. In addition, values are a mix of dependent (8 and 9 hr samples from the same time course) and independent values (everything else), so formally it is not legitimate to calculate standard deviations. Instead, we removed error bars and representations of significance from these panels, and figure legends have been appropriately adjusted. We believe that these bar graphs still have value (see below), in that they enhance comprehensibility. We would prefer to retain them, but will remove them if requested. If error bars are deemed necessary, then we can calculate standard deviations for these ratios (we agree that S.E.M. was not correct), keeping in mind that such a calculation is not strictly legitimate.

(The following contains Michael Lichten’s views, not necessarily those of the other authors, and is included here by way of discussion with the editor, editorial staff, and reviewers. Please feel free to delete it from the public review record or include it, as you see fit.)

Despite current trends to the contrary, there is a definite value to summary plots and statistics, if they enhance clarity and comprehensibility but are not the only form in which data are presented, and if they are not used to hide data features that are relevant to the analysis. Univariate scatter plots (a.k.a. “confetti plots”), currently so popular, actually can make data less comprehensible and more obscure, especially when sample sizes are so large that individual points cannot be distinguished. It is hoped that the suggestions of Weissgerber et al., which are certainly well taken, will not be blindly imposed on every paper that is submitted to eLife, but rather will be used in situations where they are appropriate.

4) The authors should explicitly indicate that in most meiosis VDE cuts both sister chromatids and that the consequences of this on pathway choices are unknown.

The following text was added:

“Thus, in most cells, both sister chromatids are cut by VDE (Gimble and Thorner, 1992; Neale et al., 2002). In contrast, Spo11-DSBs infrequently occur at the same place on both sister chromatids (Zhang et al., 2011). While the consequences of this difference remain to be determined, we note that inserts at both HIS4 and URA3 are cleaved by VDE with equal frequency (Figure 2A). Thus, any effects due simultaneous sister chromatid-cutting should be equal at the two loci.”

5) In the subsection “Local chromosome structure influences meiotic CO formation”, second paragraph: There is little or no mention of prior studies of context-dependence for crossover-noncrossover likelihood (Mancera et al. 2008; Serrentino et al. 2013; deBoer et al. 2015) or interhomolog vs. intersister partner choice (Hyppa & Smith 2010; Fowler et al. 2014). The Serrentino paper is mentioned briefly in passing in the preceding paragraph, but I doubt a reader would realize from this mention that paper had documented differences in crossover vs. noncrossover outcome between different loci. There are also studies documenting the different recombination behavior for DSBs within pericentromeric regions (Chen et al. 2008; Vincenten et al. 2015). These prior studies should be discussed in comparison to the context dependence documented here. (This is also relevant to the statement in the subsection “Concluding remarks”, at the end of the first paragraph.)

We agree that previous findings were given short shrift, and included more of this information in the paper. However:

1) Mancera et al. say that CO/NCO ratios differ at different loci, but this is likely a consequence of small sample size and uneven distribution of polymorphic markers.

2) Serentino et al. showed that three DSB sites with lower Zip3 occupancy/DSB ratios had fewer COs (measured by genetic distance, cM) than a DSB site with higher Zip3 occupancy. Please note that, because NCOs were not scored, this could be because of changes in CO/NCO or in IH/IS ratios. Their calculations used ssDNA data from Buhler et al. as a proxy for DSB levels; when the calculation is made using Pan et al.’s more recent Spo11-oligo data, the differences between loci become much less marked, and Zip3 occupancy correlates fairly well with Spo11 oligo levels (ML, unpublished).

Rather than include an extensive discussion of these issues, we wrote the following:

“Serrentino et al. (2013) showed that enrichment for the budding yeast ZMM protein, Zip3, at DSB sites is correlated with interhomolog CO levels. […] Locus-specific differences in CO/NCO ratios also have been observed in mouse meiosis (de Boer et al., 2015), locus-specific differences in partner choice have been reported in S. pombe (Hyppa and G. R. Smith, 2010), and crossover suppression by centromeres is observed in many species (Talbert and Henikoff, 2010).”
