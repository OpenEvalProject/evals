# Author response - Round 1

Authors:
- Shuai Wu ([ORCID: 0000-0003-1677-0221](https://orcid.org/0000-0003-1677-0221))
- Archit Garg ([ORCID: 0000-0002-5931-2522](https://orcid.org/0000-0002-5931-2522))
- Zachary Mazanek
- Gretchen Belotte
- Jeffery J Zhou
- Christina M Stallings
- Jacob Lueck
- Aubrey Roland
- Michael A Chattergoon ([ORCID: 0000-0002-2220-1116](https://orcid.org/0000-0002-2220-1116))
- Jungsan Sohn ([ORCID: 0000-0002-9570-2544](https://orcid.org/0000-0002-9570-2544))

## Response text

DOI: [10.7554/eLife.81918.sa2](https://doi.org/10.7554/eLife.81918.sa2)

Essential revisions:

1. The authors show that the MBP tag affects the oligomerization of POPs. The POPs used in Figures 2A, 3A, and 4A contain a GFP tag which may change the inhibitory effect of POPs on ASC filament formation. Experiments with untagged POPs are therefore required to validate the results.

We added new results monitoring the oligomerization of mCherry-tagged PYDs, ASCFL, and AIM2FL in the presence of untagged POPs, which remain consistent with our existing results (Figure supplements following Figures 2-4).

2. The authors take the reduction of PYD filamentation as an indication of inhibition, but it is not clear how they ruled out the possibility that POP1 co-assembles into the ASCPYD filaments and inhibits inflammasome formation by repressing the recruitment of Caspase-1 (as POP1 lacks the CARD the effector domain). Thus, some functional assays measuring downstream Caspase-1 activation are required. In addition, the possibility that POP1 and ASC co-assemble could be tested directly with FRET experiments in which one protein is the donor and the other is the acceptor. Without such experiments, the statement in the Discussion "Our investigations here reveal that POPs interfere with the polymerization (nucleation and/or elongation) of various inflammasome filaments without co-assembling, … " does not appear to be justified.

We included data showing that POP1 is least effective in inhibiting the NLRP3/nigericin-mediated release of mature interleukin-18 (Figure 4—figure supplement 2E; i.e., a functional assay requested by the reviewer). Here, we also find that POP2 is most effective, likely by directly suppressing ASC polymerization. Our observation here is also consistent with the report by Ratsimandresy et al. reporting that POP2 is more effective in suppressing ASC/inflammasomes than POP1.

We also generated fluor-labeled recombinant POP1 and confirmed that there are no discernable FRET signals between donor-labeled POP1 and acceptor-labeled ASCPYD, again supporting that POP1 and ASCPYD do not intermix (Figure 2, Figure Supplement 2C).

3. Further computational analysis should be performed to determine if the theory that a combination of favorable and unfavorable interactions is generally applicable. Does this theory account for other PYD/PYD interactions and CARD/CARD interactions? For example, for the AIM2PYD/ASCPYD interface, do they see only a favorable interface or a mixture? How about two unrelated PYDs, such as between AIM2PYD and NLRP3PYD? How about for COPs? How about the homotypic interfaces between the POPs themselves?

We are afraid that the reviewers are asking for future orthogonal studies significantly beyond the scope of the current work. This present manuscript focuses on PYD•POP interactions by studying more than a dozen pairwise interactions using three different methods (in silico, recombinant proteins, in cell imaging). We strongly believe that any additional in silico predictions need to be validated and (re)interpreted in light of biochemical experiments. Thus, investigating different systems such as CARD•CARD and NLRP•ASC interactions with our rigorous approach would require years’ worth of additional work, especially if they have unique patterns (rules) for themselves. Also of note, there are reports on the co-activation of different inflammasome receptors (e.g., Han et al., Sci. Immun., 2021). We do not yet know whether they directly interact with/regulate one another via PYDs or only communicate with ASC. We refrain from suggesting any interactions or lack thereof without biological/biochemical studies (i.e., beyond the scope of the present manuscript).

In our recent work (Matyzewski et al., Nat Com, 2021), we did not see any strong unfavorable energy scores between AIM2 and ASC, and our in silico approaches helped in identifying the directional interaction between AIM2PYD and ASCPYD filaments. Of note, we do not treat Rosetta energy scores as absolute free energy terms (as they are not), we use them as relative-yet-quantitative measures to guide our investigations. Importantly, our conclusion then was strictly based on our subjects at hand, as is here (any potential differences found in investigating NLRP•ASC interactions would not validate or invalidate our working model for AIM2•ASC).

We ran Rosetta interface energy analyses on hypothetical homotypic interactions for each POP. Although we refrain from making any claims without conducting extensive biochemical studies, it appears that POP1 lacks the symmetric landscape for “top” and “bottom” halves seen from PYD filaments, which like reflect the lack of filament formation.

On the other hand, POP2 and POP3 show significantly unfavorable energy scores vs. PYD filaments such as AIM2PYD and ASCPYD. Of note, we do not yet understand how POP2 and POP3 form oligomers. For instance, we do not know whether they oligomerize via different interfaces than those mediate filament assembly in PYDs (Type 1-3). We believe that delineating how POP2 and POP3 form oligomers is beyond the scope of our current manuscript and requires extensive combinations of in silico and biochemical experiments.

We believe our work here opens a door for testing to what extent our findings reported here are applicable to other death-domain (DD) proteins (or other filamentous assemblies).We look forward to such future studies to compare and contrast, improve, and even modify our understanding of how DD proteins interact with one another. To further clarify our stance, we added the following sentence at the end of the Discussion:

“Future investigations using molecular dynamics simulations and extensive mutagenesis will further delineate the complexity of oligomerization mechanisms and target specificities of POPs in more detail. It will be also interesting to see to what extent our findings for POP•PYD interactions can be applied to other DD family proteins such as COPs and CARDs. Overall, our multi-disciplinary approach provides an example of how to use in silico predictions judiciously for investigating multipartite protein-protein interactions.”

In addition, as raised by reviewer 3, the authors do not consider at all in this manuscript that there is a seventh interface described for PYDs besides the hexagonal assembly in the filament. This is the homodimer interface seen, e.g., for NLRP3, in the crystal structure of the PYD and in size exclusion chromatography (Bae and Park, 2011; 3QF2). For completeness, the energy scores should be also calculated for this interface. It might well be that POPs associate in this binding mode as heterodimeric assemblies to monomeric PYDs of NLRs or ALRs to regulate their activities. This would be somehow reminiscent of profilin binding to actin, regulating the pool of free G-actin for filament assembly.

In the report by Bae and Park, a minor population of the NLRP3PYD dimer was observed in the SEC/MALS analysis using very high protein concentrations under an acidic buffer system without any reducing agents (~600-800 µM protein at pH 5.0; Bae and Park, JBC, 2011). Considering the conditions, we are afraid that such dimer formation is unlikely physiologically important. Indeed, we regret that we do not find any biological relevance for NLRP3 dimers in the literature (full-length or PYD), and even Bae and Park did not report any functional relevance of this dimer in their paper. Although this 2011 study revealed the structure of NLRP3PYD monomer, it predates the groundbreaking discovery by Hao Wu, Ed Egelman, and colleagues showing that inflammasomes form filaments (Lu et al., Cell, 2014).

Nevertheless, we generated dimer models of PYDs and POP•PYDs based on the NLRP3PYD dimer crystal structure and conducted Rosetta interface analyses. We regret that we do not see any compelling signs indicating that such hypothetical interactions would play a major role in the target specificity of POPs:

Also importantly, the putative dimer interface is part of the filament interface we have already included in our analyses (Author response image 2; type 3a/1b). We thus respectfully disagree that this is a uniquely important seventh interface.

The colored region is thought to mediate dimerization.

4. To more directly test the mixed-interaction model, the authors should use their Rosetta structural predictions as a guide to introduce mutations into the various POP1/ASC-PYD interfaces to reduce the binding energies of those specific interactions and then test whether the introduction of a single or multiple, weak interactions then allows POP1 to restrict ASC-PYD oligomerization. To further elucidate their mixed interface model, the authors should also address whether the weak interactions need to be on the same 'half' of the interface, e.g., does weakening the 1b and 2b interfaces lead to better disruption of PYD filamentation than a 1b/1a combination mutant?

We considered such mutagenesis approaches early on but decided against them. For example, one can transplant POP2 residues on POP1, and vice versa. However, this would simply make POP1 more like POP2 and vice versa, which, in our view, do not provide significant new insights.

Instead, we are developing a new approach of combining the Monte Carlo simulation with Rosetta to further delineate how POPs and PYDs interact (this project has been inspired by our prior work reported in Matyzewski et al., PNAS, 2018). Briefly, our approach will test the probability of assembling the filament base (and inhibition of) by various PYD-POP pairs with different number of favorable and unfavorable interfaces (we will also give different weights to each interface and introduce in silico mutations). As with the current manuscript and our prior studies, any in silico predictions will be tested using biochemical methods employing recombinant proteins and cellular assays, which will take more than a year to complete. This follow-up study will help in further improving our understanding (model) of how POPs regulate PYDs. Moreover, it could also allow us to generate “designer” POPs that can target a wide variety of PYDs. We look forward to reporting our findings in the future.

We would also like to stress that our manuscript presents a comprehensive approach for investigating the interaction between POPs and PYDs. Moreover, the present manuscript marks only the beginning of our long-term goal of elucidating the “interaction codes” that underpin the specificity and interaction mechanisms of DD proteins.

Reviewer #3 (Recommendations for the authors):

It seems to this reviewer that the authors have written the manuscript in chronological order as they have performed the experiments, which might, however, not be the best way to present their data. I propose to rewrite and reorganize the manuscript, to better make the points. The Discussion is a bit repetitive and seems overwritten. Some shortening, despite adding new ideas and considerations (see below), might be reasonable.

Thanks for the suggestion. We shortened the Discussion.

Additionally, our apologies for the oversight, we improved the resolution of Figure 1—figure supplement 1.

This reviewer does not understand the scientific rationale regarding the PYD sequence identity and similarity of POPS to either NLRs or ALRs as a measure of their potential regulatory/inhibitory function in the respective inflammasome formation.

We do not intend to support or refute the rationale behind this previously proposed notion by Devi et al., Indramohan et al., de Almeida et al., and others (cited throughout the manuscript); however, our observations here indicate it’s indeed more complex.

[Editors’ note: what follows is the authors’ response to the second round of review.]

1. You need to explicitly recognize/discuss/acknowledge that NLRs and ALRs contain additional domains beyond the PYD that can modify the energy landscape to create oligomers, and it is vital to consider this aspect as a caveat to your study which focuses on dissociated PYD interactions.

We added such a disclaimer at the end of the paper.

2. The consensus of the reviewers remains that you need to test your model by employing site-directed mutagenesis. This was a clear requirement in the previous decision letter (point 4), and the reviewers were not convinced by your argument that this is not necessary. One reviewer suggests: "One could easily imagine replacing a favorable interaction with alanine to gently weaken the interaction or with glutamate or other charged residue to break the interface. By taking POP1 and introducing mutations to disrupt one or multiple surfaces the authors could show that these mutants do or do not inhibit filament formation ASC. Alternatively, the authors could introduce mutations into the ASC PYD and determine whether the mutant protein could now act like a POP and block WT ASC filament formation. While I appreciate that doing such a comparison for every POP and PYD in the paper would be excessive, I strongly believe that the authors need to experimentally test their model with at least some site-directed mutants".

We added new mutagenesis data at the end of the Results section. Briefly, we introduced mutations that hamper the self-assembly of AIM2PYD (i.e., unfavorable) and found that resulting mutant proteins can inhibit the polymerization of WT-AIM2PYD.
