# Peer review - Round 1

Editors:
- Arup K Chakraborty, Massachusetts Institute of Technology , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.11282.035](https://doi.org/10.7554/eLife.11282.035)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Population genomics of intrapatient HIV-1 evolution" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Diethard Tautz as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

In this paper, you use deep sequencing to track the genotypic evolution of HIV in individuals over multiple years. You observe patterns in the virus's evolution over time, and note a surprising amount of parallelism in the fate of specific mutations in the few patients you study. Although others have conducted similar studies, your study is more comprehensive than past efforts. Another major strength is that you develop a web-based visualization platform that enables both expert and non-expert users to inspect the results in detail. However, the current manuscript does not properly describe past efforts adequately, and this is the primary criticism that will need to be addressed before we can justify publication in eLife.

For example, in the Introduction, you may want to discuss the work described in the following references as part of the background and then make clear what is novel about your studies: Bernardin J Virol 2005; Bar KJ Plos Path 2012; Brockman J Virol 2010; Schneidewind A JVirol 2010. Also, Salazer-Gonzalez 2009, did not examine T cell escape in acute HIV infection; escape was examined Goonetilleke et al. 2009 (published in the same issue of JEM as Salazar-Gonalez) followed by Liu et al. JCI 2013. Key papers from the lab of P Borrow should also be recognized. Iyer S Plos One 2015 (lab of J Mullins) is a recent cross-sectional study in HIV-1 using deep sequencing techniques that is also relevant. Finally, the point made in the Discussion about how your results provide direct justification for past efforts to extract universal fitness landscapes of HIV from cross-sectional data might be considered for inclusion in the introduction as well (e.g., Dahirel, PNAS (2011); Fergusson, Immunity (2013); Mann PLOS CB (2014)).

In addition, it is important that you address the following comments in order to improve the paper:

Specific comments:

1) It is clear from Figure 1B that the major limitation for low-frequency SNPs is low template abundance, rather than sequencing errors. SNP frequencies are not expected to be accurate below 1/N where N is the number of template molecules, and N appears to be about 10 to 50. This would suggest that the SNP frequencies are not very accurate below about 2-10%. This idea seems to be consistent with the results in Figure 9C, which show a very strong correlation between frequencies called from different fragments at moderate frequencies, but little correlation below about 1-5%. Although you do discuss this point to some degree, we think this point should be noted more emphatically. There is a great deal of interest in more accurate techniques for sequencing viruses, but as the results here make clear, there isn't really much benefit in improving sequencing accuracy if the accuracy is already > 1/N.

2) A major finding of the paper is the evidence for parallel evolution in the sense of similar positions accumulating similar divergence among patients, and of strong tendency of reversion to the same consensus identities in all strains. However, it is often unclear if this trend is occurring primarily on the protein level, primarily on the nucleotide level, or both. For instance, in Figures 4 and 6 it is unclear if the trends are for nucleotide or amino-acid mutations – this should be clarified, and ideally results for both nucleotides and amino acids could be shown. Figure 3 might also benefit from showing similar data for both nucleotides and amino acids. In the Discussion you note, "The strong and lasting preference for specific nucleotides needs to be accounted for…". In fact, the cited reference discusses strong and lasting preferences for specific amino acids, not specific nucleotides.

3) How does the consistency of evolution between patients correlate with distance between those patients' founder viruses? A central claim in this study is that: "At a single nucleotide level, the spectrum of mutational possibilities is explored reproducibly." The evidence supporting this claim includes the correlation between the site-specific entropy of patient samples and natural sequences (Figure 4A). However, something that is unclear from this comparison is whether variation is increasing at the same or different sites for different samples within this study. Can you make similar comparisons to Figure 4A across samples within the study? Are the correlations stronger between samples from individuals infected with genetically similar viruses?

4) More discussion is needed on the clinical characteristics of patients (viral load and CD4 count over time). Of note, participants had to be ARV naïve for at least 5 years, and thus some had a low viral load. How might factors leading to low viral load affect evolution? You note that some patients received ART during the study, and were included in an ongoing sub-study. However, it is not clear if the time points after ART initiation were included in the present study. If they were included, are there any interesting differences in evolutionary patterns between patients that received ART and patients that did not?

5) Five of nine subjects in the cohort were identified in either Fiebig V or VI. This staging precludes confident determination of the transmitted/founder viruses in these subjects and therefore the statement that “initial consensus sequence approximates the sequence of the founder virus(es)” is not supported. You may want to revise the terminology to reflect that, in these subjects, you deduced a consensus sequence of an early virus sequence.

Regarding the Fiebig staging and virus loads: These data are very confusingly described and presented. Was Fiebig staging performed during a visit prior to the available plasma samples tested? If so, when? Going through the supplementary file, the VL of the first sample available for sequencing is clearly outside the acute window for several of the patients described as detected in Fiebig II-IV. As above, how can you justify describing the first sequence as the founder? As shown by multiple groups, significant immune selection and recombination occurs within the first months of HIV infection.

6) You provide a convincing demonstration of reversal to global consensus and provide a discussion of the how this observation can be reconciled with the observed intra-patient and global HIV diversity. It might help the reader to have the discussion of the balance of divergence and reversal (presently in the fifth paragraph of the Discussion) sooner, e.g. in the subsection "Extensive reversion toward consensus". The findings in this regard relate to a major ongoing debate in molecular evolution about the extent to which diverged homologs retain strong propensities for specific amino acids. Pollock et al. (PNAS, 109:E1352) and Shah et al. (PNAS, 112:E3226) have argued that pervasive epistasis means that the propensities for specific amino acids means will diverge rapidly among homologs, which will quickly come to favor different amino acids at homologous sites. On the other hand, Ashenberg et al. (PNAS, 110:21071), Risso et al. (Mol Biol Evol, 32:440), and Doud et al. (Mol Biol Evol, doi:10.1093/molbev/msv167) have argued that the propensities for specific amino acids are similar among homologs. How do your results bear on this issue?

7) In the tree in Figure 1, near the yellow for patient 9 there is a black line that doesn't connect to any colored lines in the tree. What does this indicate?

8) It is confusing that there is one Methods section called "diversity and divergence" and another called "divergence and diversity".

9) The y-axis of Figure 5 should be labeled with the appropriate units, or this information should be added to the figure caption.

10) You state: "Figure 6B indicates that diversity accumulates over a time frame of 2-4 years." However, since Figure 6B shows the rate of reversion compared to variability at 5-6 years, it is not clear how this demonstrates that diversity accumulates over a 2-4 year period.

11) A*32 is overrepresented in this group; a much higher frequency than found in the broader Swedish population. Can the authors comment? Are these subjects in any way linked?
