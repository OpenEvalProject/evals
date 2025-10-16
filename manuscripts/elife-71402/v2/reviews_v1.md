# Peer review - Round 1

Editors:
- Eugene V Koonin, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71402.sa0](https://doi.org/10.7554/eLife.71402.sa0)

This work is a substantial contribution to the important and fascinating field of genetic code diversification.


---

# Peer review - Round 1

Editors:
- Eugene V Koonin, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71402.sa1](https://doi.org/10.7554/eLife.71402.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A computational screen for alternative genetic codes in over 250,000 genomes" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Molly Przeworski as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The reviewers are unanimous in their view that the proposed method for inference of alternative genetic codes is valid and will be useful for many researchers involved in analysis of genomic and metagenomic data. As such, this is a strong paper that requires revisions primarily for clarification.

Essential revisions:

1) Clarify the methodology and, in particular, address the following question of Reviewer 2: "How many occurrences of an apparently wrong amino acid are needed in practice to draw an inference?"

2) Clarify the situation with the mitochondrial codes as requested by Reviewer 2.

Reviewer #1 (Recommendations for the authors):

As I described in my comments, I strongly recommend the authors to validate amino acid assignment of CUG codon in S. malanga.

Other Comments:

Line 160: Explain the meaning of the sentence, "Lack of an amino acid inference ("?") contributed to neither.", in more detail.

Line 213-216 and Line 241: It is better to explain why the number of the aligned Pfam consensus columns was so small in these species.

Line 221: In the title of this paragraph, "Computational screen of all bacterial and archaeal genomes finds previously known alternative genetic codes", the authors used "all", but it is not precise. It should be removed.

Line 238-240: Provide the reference(s) for the claim that Mycoplasmatales and Entomoplasmatales translates the opal stop codon UGA as Trp.

Line 247-250: Provide the claim that Gracilibacteria translate UGA as Gly.

Line 282-284: Provide the reference for the argument that "high GC content-driven nonsynonymous substitutions of the AAA and AAG lysine codons to AGA and AGG arginine codons at protein residues that can tolerate either positively-charged amino acid".

Line 287: Citing N. Sueoka (1961) that "…have long been observed to preferentially use more arginine and less lysine.". However, in his original study, Sueoka is simply plotting the possible correlation between the GC contents and the amino acid composition, drawing from a limited 'dataset' at his time. He did not directly observe any preferential usage of Arg over Lys in high-GC bacteria. This sentence should be corrected accordingly, given the citation to Sueoka's paper.

Line 300-303: The authors should be more specific in their analysis of the values of probabiltiy and tRNA sequences on which they base the results they are describing here.

Line 317-318: The values of the probability on which the author's decision were based should be indicated or summarized.

Line 368-376: The values of the probability on which the author's decision were based should be indicated or summarized.

Line 408-414: Do these species in which tRNAUCG is missing have homologs of the modifying enzyme responsible for the formation of inosine?

Line 443: The authors described "two differently charged tRNAs" here. However, they did not demonstrate that.

Figure 2 and line 709-715 (method section): Supply the exact sequences of T7 in vitro transcribed tRNA used as controls in northern blot.

Reviewer #2 (Recommendations for the authors):

The paper proposes a method for large scale genome analysis that is able to detect reassignments in the genetic code. In general, the examples given are convncing. The method detects several variants that are already known and discovers some new ones. This appears to be useful development and a thorough analysis.

The essentials of the method are in lines 112-126. I don't find this 100% clear. If I understand correctly, the DNA sequence of the test sequence is translated with the standard genetic code and then aligned with HMMs of proteins. If the codon follows the standard code, the amino acid will be in agreement with the common amino acid in the alignment column. If the codon has been reassigned, the apparent amino acid will be an unusual one according to the alignment profile. This requires the protein sequence to be less variable than the genetic code. I can see that this would become convincing if the same apparently wrong amino acid appears consistently in alignment columns where a particular amino acid is the most common one. How many occurrences of an apparently wrong amino acid are needed in practice to draw an inference? This paragraph says there are 17000 alignments in Pfam, but it does not say how many are used for the inference.

There is no mention of mitochondrial genetic codes. Does this method work with mitochondrial genomes? Maybe there are too few coding sequences in mitochondria?

The case of Lys and Arg codons discussed in lines 277-291 is interesting. Since Lys and Arg are similar amino acids we expect non-synonymous substitutions to be frequent between Lys and Arg. Therefore it is not surprising that the method might give a false positive prediction of a codon reassignment. In fact it is surprising that more cases like this do not occur. For example AUA is frequently reassigned from lle to Met in mitochondria, and an Ile to Met non-synonymous substitution is also quite possible. Does this not also show up in the analysis?

At the end of the day, computational predictions of codon reassignments will not be fully certain until there is experimental confirmation. But this method seems very useful at suggesting cases that are worth looking at experimentally.
