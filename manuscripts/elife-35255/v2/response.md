# Author response - Round 1

Authors:
- James Attwater ([ORCID: 0000-0002-7244-9910](https://orcid.org/0000-0002-7244-9910))
- Aditya Raguram
- Alexey S Morgunov
- Edoardo Gianni
- Philipp Holliger ([ORCID: 0000-0002-3440-9854](https://orcid.org/0000-0002-3440-9854))

## Response text

DOI: [10.7554/eLife.35255.045](https://doi.org/10.7554/eLife.35255.045)

Reviewer #1:

[…] 1) Overall, the manuscript was very difficult to follow. It is up to the authors to make their presentation as simple and direct as possible. Given the availability of supporting information, there is no reason why the authors could not add schemes where appropriate to clarify their presentation, logic, and workflow.

We apologize for the poor presentation and have made several changes to enhance clarity. These include textual changes to reduce ambiguity and lay out our reasoning more thoroughly as well as explanatory schemes of ribozyme activity in Figure 1 and Figure 1—figure supplement 1. Furthermore, we have redesigned Figures 3 and 7, and now provide an additional dataset presenting substrate concentration-dependent error rates in a more straightforward manner in Figure 9—figure supplement 1.

The manuscript structure is complicated by the multiple stages of RNA evolution and characterization involved in the project, and to help navigate the progress of our ribozyme development, we now provide the new Figure 4—figure supplement 1 detailing all the stages of evolution and engineering of the different triplet polymerase ribozymes to provide a “roadmap”.

2) Regarding the dimerization, it is not clear how the authors implicated the 5'-hairpin to begin with, leading to the experiment that showing that a single mutation in that loop inhibits dimerization.

We welcome the opportunity to clarify this. We had originally noticed the ‘cap-’ mutation in the most abundant isolated type 1 clones, and when testing this in different constructs observed that it quenched type 1 enhancement pointing towards the 5’ hairpin region as the critical interaction site. We now refer to this in the manuscript text.

Our knowledge about this dimerization interface is currently limited and we have therefore generally refrained from speculation. However, it seems possible that the ‘cap-’ mutation was enriched in these type 1 sequences to diminish homodimerisation of type 1 that may interfere with heterodimerisation with active triplet polymerase in the selection pool.

3) The assertion that the two RNAs form a 1:1 complex is not quantitatively substantiated from Figure 3B.

We now include quantitative data on the stoichiometry of the complex as observed by gel shift (EMSA) titration in Figure 3B, and activity tests in Figure 3—figure supplement 1. These support a 1:1 stoichiometric complex in the active ribozyme as expected from the final selection pool composition.

4) Considering their success in replicating structured hairpins and achieving primer free synthesis of an 18 nt strand (β+), it would be interesting (though not necessary for publication) to see how much of the Broccoli RNA could be transcribed without the addition of a primer sequence. If this is not possible, the authors could demonstrate the complete replication of a functional RNA of tractable length, like the Hammerhead ribozyme, to illustrate the ability of their trinucleotide RPR to replicate entire sequences of functional RNAs by exclusively using triplets as substrates.

The reviewer highlights an important challenge that such ribozymes must ultimately face – copying without primers both strands of functional RNAs to achieve their complete replication using only short oligonucleotide substrates. With the current triplet polymerase ribozyme, while primer-initiated synthesis is almost general (as we show by synthesizing both + and – strands of the Broccoli RNA aptamer), we cannot currently achieve primer-free synthesis of all sequences. The latter includes Broccoli where yields of full-length RNA are poor using triplets alone. This may reflect inefficient initiation of synthesis or poor upstream inclusion of some 5’ terminal triplets.

Nevertheless, the current triplet polymerase ribozyme can achieve this for some functional sequences, most relevantly from t5 itself. To demonstrate this, we have now included data on the primer-free synthesis and replication of the Υ segment. Specifically, we describe primer-free synthesis using triplets alone of the γ+ strand segment with sufficient yield to use this ribozyme-synthesized RNA as the template for primer-free γ- strand synthesis, demonstrating complete primer-free sequence replication using only triplets. These new data are now included as Figure 7C, replacing the (now in our view redundant) primer-free γ+ syntheses.

5) The fidelity analysis is based on testing 12 of the possible 64 trinucleotides, so one cannot be convinced of the generality of their observations and inferences. The authors need to underscore this in the discussion of fidelity. The authors show that increased concentrations of triplets help fidelity, however in the absence of the 'correct' triplet, it is likely that RPR will incorporate 'mismatch' triplets. The authors should comment on this aspect.

We measured fidelity of triplet incorporation with all64 triplet substrates present but in the context of 12 defined template triplet sequences flanked by conserved CCC incorporation sites. These were chosen to be compositionally balanced, including both GC-rich and AU-rich template triplets, to provide fair estimates of ribozyme fidelity, as well as an effective tool to compare the fidelities of different ribozymes.

This assay was designed to allow us to separate incorporation fidelity (i.e. discrimination among 64 triplets for decoding a defined anti-triplet) from each ribozyme’s extension capabilities by providing a uniform, tractable sequence context.

The important qualification regarding this assay, we feel, is therefore that while it provides an accurate representation of fidelity in a defined sequence context (triplet-triplet junction), it may not provide a comprehensive picture of triplet polymerase fidelity performance in all sequence contexts. We now provide this caveat in the text.

Reviewer #2:

1) In this paper, the authors demonstrate interesting and novel results that provide further evidence for RNA's capacity to act as prebiotic genetic material. The key feature associated with this study involved using trinucleotide triphosphates (triplets) rather than NTPs as substrates for a novel RNA polymerase ribozyme. The use of triplets allowed structured templates to be unfolded and in some cases avoided the need for primers, circumventing an ongoing obstacle to RNA self-replication. This study thus makes some significant steps towards identifying a truly self-replicating prebiotic biopolymer. Literature precedents are well-discussed, and the results are interpreted in a detailed and convincing manner. I would nonetheless encourage the authors to try to make these important results as accessible as possible to readers who are unfamiliar with in vitro evolution.

As discussed above, we have made a significant number of changes to the manuscript in order to present our results more clearly.

These include textual changes to improve clarity and remove ambiguities. We have also made an effort to lay out our experimental progress and reasoning more thoroughly, using explanatory schemes of ribozyme activity in Figure 1 and Figure 1—figure supplement 1, redesigning Figures 3 and 7, and providing an additional more straightforward dataset in Figure 9—figure supplement 1. We hope this will make the manuscript easier to read and more accessible to the general reader.

Specific comments:

2) Subsection “in vitro evolution of triplet polymerase activity”, last paragraph. The use of "in-ice evolution" (a technique developed by the authors) is reported. A sentence could be added describing why this technique is being used / why it is necessary.

We have expanded our description of the mechanisms of in vitro evolution and discuss in more detail the reasoning behind our use of eutectic ice phases and in-ice evolution. As the properties of ice as a medium for RNA-catalyzed RNA synthesis, replication and evolution are discussed at length in the cited references, a fairly brief discussion must suffice. We hope nevertheless that this will now clearly illustrate our rationale in using this technique in our work.

3) For certain experiments (e.g. subsection “Fidelity of triplet-based RNA synthesis”), random triplet pools were used. What kind of triplet pools were used in other sequence-copying experiments? Were they non-random? This needs to be more clearly articulated.

We generally list the triplet substrates used for different experiments but apologise for any ambiguity.

In general for preparative syntheses we have avoided using pools of random triplets, providing instead a set of defined triplets as specified by the template sequence to minimise substrate consumption. We have however verified that random triplet pools can be used for key triplet based RNA synthesis experiments including hairpin invasion (see Figure 5—figure supplement 1) and ribozyme segment synthesis (see Figure 6—figure supplements 4 and 5), as well as in experiments on ribozyme fidelity (see e.g. Figure 8). We now explicitly state the substrate composition in the text and figure legends for all experiments described.

4) "… we found that using modified substrates with a disrupted minor groove hydrogen bond acceptor at the 3rd position…" – What is the modification? This should be stated in the body-text.

We apologize for this omission and have amended this. We now state in the text that uracil was replaced by 2-thio uracil in the triplets.

5) What is the scope of substrates for the t5+1 ribozyme? Triplets reportedly incur a lower entropic cost than NTPs (Discussion, third paragraph), but what would happen when a mixture of the two were used? Would both the NTPs and triplets be incorporated?

This is an interesting suggestion considering that abiotically-generated substrate pools would likely include a mixture of different length substrates including mono- and dinucleotides. We have performed additional experiments to explore this and now include data on their incorporation during segment synthesis in Figure 6—figure supplement 5.

In summary, t5+1 does incorporate both dinucleotide triphosphates and NTPs, but with reduced efficiency. Furthermore, they appear to serve as poor substrates for segment synthesis with triplets incorporated much more efficiently. Increasing amounts of NTP and dinucleotide substrates vs. triplets (up to a total 4:2:1 ratio) do lead to diversification of extension products outside the initial triplet register, but do not notably affect the total amount of ligation performed.

As seen in Figure 6—figure supplement 2, more length-heterogenous substrate pools (including longer oligomers) may offer both advantages and disadvantages, but we feel that a more systematic investigation of diverse substrate pools and their effect on yield and fidelity of RNA-catalyzed RNA replication goes beyond the scope of the current manuscript.
