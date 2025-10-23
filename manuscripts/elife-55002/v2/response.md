# Author response - Round 1

Authors:
- Kazuki Saito
- Rachel Green ([ORCID: 0000-0001-9337-2003](https://orcid.org/0000-0001-9337-2003))
- Allen R Buskirk ([ORCID: 0000-0003-2720-6896](https://orcid.org/0000-0003-2720-6896))

## Response text

DOI: [10.7554/eLife.55002.sa2](https://doi.org/10.7554/eLife.55002.sa2)

[Editors’ note: the authors resubmitted a revised version of the paper for consideration. What follows is the authors’ response to the first round of review.]

Reviewer #1:

This paper describes an innovative approach to probe the importance of Shine-Dalgarno (S-D) sequences in translation initiation in Escherichia coli. […] I also have concerns about the interpretation of Figures 6 and 7 that impact the overall conclusions.

- The presentation of the cold shock data is confusing. The overall conclusion is that S-D-dependence is lost at almost all genes during cold shock. However, a small subset of genes appears to depend strongly on the S-D. The distinction between the effect on the majority of genes and the effect on a small subset should be explained more clearly. The simplest interpretation of these data is that most start codons are highly structured during cold shock, but those that are do not rely on their S-Ds. This model is largely consistent with previous work.

We have removed the figures dealing with cold shock and other stresses. We agree that they are largely consistent with previous work. The confusion raised by the cold shock story appears to have taken away from the main story.

- I disagree with the interpretation of Figure 6. The data show that for the altered ribosomes, annotated start codons are used far more efficiently than the collection of all other ATG sequences within ORFs. However, there are many more ATGs within ORFs than annotated start codons, and even if translation relies heavily on S-D sequences, you would expect that most ATGs within ORFs would not be selected by alternative ribosomes because only a small subset will have appropriate S-D sequences, and many may be weakly expressed. My interpretation of these data is that alternative ribosomes do use annotated start codons, but there is no way to tell how selectively they do this. A more appropriate comparison would be of (i) annotated start codons to (ii) ATGs within ORFs where the ATG is associated with a sequence that is predicted to function as a good S-D for the alternative ribosome.

We have added analyses to the new Figure 4 and Figure 4—figure supplement 1 showing initiation at internal AUG codons predicted to have high affinity for the mutant ASD sequences. These data show that initiation occurs with all four ribosome types regardless of the SD strength or specificity, but that initiation is most efficient when the SD and ASD are complementary.

- Another concern I have with Figure 6 is that presumably some, and perhaps many of the annotated start codons will have good SD matches for the alternative ribosomes. Figure 2C suggests that the number with good matches will be fairly high. Is the ribosome density at annotated start codons simply due to the subset of start codons that have reasonable SD matches to the altered ASD? Another way to think about this is to ask whether the start codons contributing to the signal in Figure 6C are the same start codons that contribute to the signal in Supplementary Figure 5A-B.

We added analyses to the new Figure 3 showing that initiation occurs with all three mutant ribosomes at annotated start sites that have no affinity for the mutant ASD sequences.

- Figure 7E shows the importance of an A-rich sequence in the context of start codons lacking a good S-D. Similar to Figure 6, these data highlight the contribution of non-SD sequences to translation initiation, but they do not provide any information about the relative importance of the different sequence elements.

We have removed claims about the relative importance of different sequence elements.

Reviewer #2:

Critique:

This is an interesting, intriguing and important study. The results are nice and clean and the implications are important for unraveling the fundamental mechanism of translation initiation in bacteria. Although the paper is generally well written, it was hard at times to follow the authors logic and I strongly encourage the authors to try to clarify the message, which often was hard to extract.

1) Here are several examples:

- Abstract: The statement "We reveal a genome-wide correlation between the SD strength and translational efficiency" is followed by "this global correlation is lost and a subset of genes […] becomes [dependent] on SD motifs for translation". This is hard to digest.

- Figure 4C legend ("the strength of the SD motifs determines whether wild-type or ASD mutants are recruited to messages") is supposed to contrast Figure 4F legend ("the unstructured SD motifs can recruit wild type ribosomes more effectively than they recruit ASD mutants"). However, they sound nearly identical and thus, do not accurately communicate the point the authors apparently are trying to make.

- "genes with strong SD motif are translated better by ribosomes with canonical ASD": better in comparison with the ASD-mutant ribosomes or better in comparison with the genes with weak SD?

We removed the section on stress conditions that was hard to follow and taking away from the main point of the manuscript.

2) Aleksashin et al., 2019, have shown that altering ASD in 16S rRNA compromises rRNA maturation. Although the presence of unprocessed sequences at the 5' and 3' end of the ASD-mutant 16S rRNA would not likely change the general conclusions of the paper, hypothetically it could affect the functionality and elongation rate of the mutant ribosomes. I am wondering whether authors have checked how well their mutant 16S rRNAs are processed. Irrespectively, I believe a more detailed discussion of the general functionality of the ribosomes with altered ASD, especially in relation to the elongation rate, would be beneficial.

RNA-seq analyses of rRNA (prior to nuclease treatment) is now shown in Figure 1—figure supplement 1 and discussed early in the Results section (subsection “Selective profiling of ribosomes with mutant ASD sequences”).

3) Subsection “Gene-specific roles of SD motifs under stress”. The readers need a better explanation why the authors switched from ΔlogTE to ΔlogRPKM metrics when they move to the experiments in the stressed cells.

This section was removed.

4) The influence of the competition between wt and mutant 30S subunits for the translation start sites on the conclusions drawn from ribosome profiling should be discussed.

This possibility was added to the Discussion.

Reviewer #3:

1) The author focuses primarily on the importance of the sequence colloquially known as the Shine-Dalgarno in controlling a mRNA's translation initiation rate. The authors write that "Initiation rates vary depending on how well an mRNA recruits 30S subunits to the start codon, and in bacteria, the working model is that this is accomplished primarily by Shine-Dalgarno (SD) motifs." This is incorrect. […] Their current conclusions are already subsumed within the state-of-the-art (i.e., nothing new).

We added a more detailed description of the factors that affect initiation rates to the Introduction, including the points listed above.

2) Any discussion of "which translation rate interaction is most important" or "which translation rate interaction is responsible for X whereas the interaction Y only fine-tunes Z" is not productive and can easily be contradicted by selecting a real counter example. Overall, it is the binding free energy of the 30S ribosome to the mRNA that determines its translation initiation rate. Each of these interactions contributes free energy to this process and the magnitude of the contributed free energies can be roughly equal across a selection of real mRNA examples. There are unstructured mRNAs where there is little penalty for unfolding inhibitory mRNA structures. There are highly structured mRNAs that have consensus SDs sequences. There are mRNAs that have consensus SD sequences far away from the start codon. All of these mRNAs could have the same translation rate. Which interaction is most important? That's not the right question to ask, because it's meaningless.

We have removed language that focuses on the relative contribution of the individual factors that affect translational initiation. We agree that our analyses do not allow us to determine their relative contributions.

3) The manuscript's main topic is the Shine-Dalgarno sequence, but the authors should be made aware that at least the last 9 nucleotides of the 16S rRNA can contact the mRNA and hybridize to it. In E. coli, the anti-Shine Dalgarno sequence is 5'-ACCUCCUUA-3' and the "consensus" Shine-Dalgarno sequence is therefore 5'-TAAGGAGGT-3'. The manuscript text and the authors' calculations should reflect this.

We revised the Introduction to explicitly state that up to 9 bp can form. Drawing on previous work, we refer to the “consensus” as GGAGG because it is the G’s that are overrepresented upstream of start codons (see the data for E. coli in Figure 5—figure supplement 1).

4) The authors are mis-using the ribosome profiling measurements in their analysis. Ribosome profiling measurements do not directly measure translation rates. They measure mRNA-bound ribosome densities. A mRNA's ribosome density will depend on both its translation initiation rate AND its translation elongation rate. Specifically, in steady-state conditions, the ribosome density will be the ratio between these two quantities (initiation rate over elongation rate). In the initial applications of ribosome profiling, researchers assumed that all mRNAs have the same translation elongation rate in order to conclude that ribosome density measurements were proportional to translation initiation rates. This is not true. Coding sequences in mRNAs have very different translation elongation rates, due to differences in synonymous codon usage. Unless each mRNAs' translation elongation rates are predicted or directly measured, ribosome density measurements cannot be used to infer their translation initiation rates. Therefore, when the authors write "In pioneering ribosome profiling studies in bacteria, the paradoxical observation was made that there is little or no correlation between the translational efficiency of a gene and the strength of its SD motif (calculated using thermodynamic algorithms for RNA pairing), as had been anticipated based on the SD model." there is no actual paradox. The ribosome profiling measurements were not used correctly to test how mRNA sequences control translation rate.

We revised the Introduction to explicitly state that up to 9 bp can form. Drawing on previous work, we refer to the “consensus” as GGAGG because it is the G’s that are overrepresented upstream of start codons (see the data for E. coli in Figure 5—figure supplement 1).

5) Getting to the authors' main conclusions, they write that "These data indicate that the ASD mutant ribosomes translate genes with weak SD motifs better than genes with strong SD motifs, exactly the opposite of what wild-type ribosomes are expected to do." This statement is confusing given the real conclusion of the authors, that all other factors being equal a "strong" SD motif does result in higher translation than a "weak" SD motif. It's only because of other confounding factors that the initial analysis did not yield a positive correlation. An incorrect analysis (excluding confounding variables) cannot lead to a correct conclusion.

The sentence, “These data indicate that the ASD mutant ribosomes translate genes with weak SD motifs better than genes with strong SD motifs” describes the observations in Figure 2B, the result of all the other factors except for SD-ASD pairing. We removed the phrase “exactly the opposite of what wild-type ribosomes are expected to do” that seems to have caused the confusion.

6) Figure 2C shows a very interesting and productive result, that the difference in translation efficiency between the wild-type "C" ribosomes and the A-ribosomes correlates to some degree with the hybridization free energy between the mRNA and (a portion of) the anti-SD sequence. This is a productive approach towards eliminating key confounding variables because, in principle, the strengths of the four other interactions that control translation initiation rate should not change when the 16S rRNA aSD sequences are changed. However, it's not apparent in the manuscript text, but the authors are using the modified 16S rRNAs to “eliminate the SD-aSD interaction as a contribution to the mRNA's translation rate”. So when they subtract the contribution from the modified A-ribosome's translation rates from the C-ribosome's translation rate, they are observing more directly the contribution from the SD-aSD interaction. The manuscript text should more clearly explain this experimental design. This is a creative and valid way of using ribosome profiling measurements.

We revised the language at the end of the Introduction and the beginning of the Results section to better explain our experimental design. The fact that we can isolate the effects of SD-ASD interactions from the other factors that set initiation rates explains why we use statistics for single variables and focus primarily on the SD mechanism of initiation.

7) However, the hybridization free energy calculations could be improved. First, as mentioned previously, the wild-type aSD sequence in E. coli is ACCUCCUUA. Second, the hybridization free energy calculation was only performed on the region from 15 to 6 nucleotides upstream of the start codon, but the aSD sequence can hybridize at other locations. Third, the hybridization between the mRNA and aSD can accommodate 1 or 2-nucleotide bulges or internal loops.

The fact that we see a strong correlation between our calculated SD affinities and differences in ribosome occupancy (WT – mutant) argues that the calculations are basically reliable. We see the highest correlation when affinities are calculated using the 10 nt between -15 and -6 from the AUG and we show the data for various windows with different SD distances in Figure 2—figure supplement 2. The calculations are quite robust to changes in parameters: we see little or no differences in SDRO correlations if we use 9 nt of ASD sequence to calculate affinities instead of 7 nt, or if we allow the ASD to pair anywhere between -20 to 0 upstream of AUG, or if we use the RBS calculator to generate the ΔG values.

8) The measurements in cold shock are greatly confounded by the higher expression levels of RNA chaperones that are unfolding mRNA structures “at specific mRNAs” where the RNA chaperones recognize binding motifs. The conclusion here should be that RNA chaperones bind specific mRNAs, unfold their inhibitory mRNA structures, and increase their translation rates during cold shock. This is all independent of the Shine-Dalgarno sequence. This process also does not depend on many other uninteresting factors.

We removed the section on the role of SD motifs under stress because it generated confusion and ornithological references without strengthening the main point of our manuscript.

9) The use of ORF-wide GINI values is odd because it's generally only the region surrounding the start codon that affects its translation initiation rate, and not the structure of the entire ORF (which this coefficient is quantifying). Also, using the SHAPE reactivity around a start codon as a proxy for RNA structure is a bit misleading as ribosomes actively unfold RNA structures during translation initiation. A highly structured mRNA with a consensus SD sequence will have a high SHAPE reactivity (i.e., low RNA structure) because the ribosomes can rapidly bind to the mRNA and unfold the mRNA structure. SHAPE reactivity is measuring the effect of rapid ribosome binding and not the cause of it. Rapid ribosome binding can also be facilitated by slow RNA refolding kinetics, called "Ribosome Drafting" in the literature.

Carol Gross and colleagues showed that ORF-wide GINI values are highly correlated with translational efficiency genome-wide. This is true whether the DMS probing is done in vivo (where ribosomes could affect structure by unwinding the RNA) or to a lesser extent with purified RNA in vitro. Kevin Weeks also showed that RNA structures are correlated in vivo and in vitro using the SHAPE reagent. These data argue that at least to some extent mRNA structure is driving translation rates. This was clarified in the Results section in the discussion of Figure 5E.

10) The data in Figure 6 just says that A-ribosomes can initiate translation rate at other start codons because they now have more negative binding free energies to those start codons, compared to the annotated ones. The authors could perform hybridization calculations using the A-ribosome's aSD sequence to investigate whether these "new start codons" have a nearby "SD" sequence that is complementary to the A-ribosome's aSD. That would be interesting.

The new Figures 3 and 4 now include analyses of sets of initiation sites with various affinities for the WT or mutant ASD sequences showing more clearly that translation occurs at start codons even without strong SD-ASD pairing.

[Editors’ note: what follows is the authors’ response to the second round of review.]

Reviewer #2:

The streamlined paper of Saito et al. reads much better than the original version and delivers a clear and impactful message.

I believe it can be published after authors address two remaining issues:

The authors refer to "the number of elongating ribosomes per mRNA as a proxy of initiation rates". This is incorrect: there would be twice as many ribosomes on an mRNA that is twice as long as another one, even if those two would have the same initiation rate. The correct metrics is not the number of ribosomes per mRNA but the ribosome density (their number normalized by mRNA length). This does not affect conclusions of the paper because authors normalize RiboSeq reads by RNASeq reads. Yet, I would try to avoid this confusion.

The language was changed to “ribosome density” instead of “the number of ribosomes.”

The authors write: "Interestingly, in comparing internal AUG codons that support initiation in our ribosome profiling data to those that do not, we found that A's are enriched both upstream and downstream of initiation sites (Figure 5A).…. This results from endogenous initiation sites… ". However, Figure 5A does not deal with the internal initiation sites, but with the annotated sites lacking SD.

Thanks for catching this mistake; the Discussion was updated to reflect this.
