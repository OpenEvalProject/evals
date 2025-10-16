# Peer review - Round 1

Editors:
- Kang Shen, Howard Hughes Medical Institute, Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64911.sa1](https://doi.org/10.7554/eLife.64911.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The design of the genomic insertion into introns tolerates INDELs and increases accurate targeting in somatic cells. The authors provided evidence that several in situ fusion proteins remain functional.

Decision letter after peer review:

Thank you for submitting your article "High-fidelity, efficient, and reversible labeling of endogenous proteins using CRISPR-based designer exon insertion" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Craig C Mello (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. What is new is the finding that FP insertions are frequently expressed and at least partly functional as evidenced by their ability to localize to the expected intracellular structures. However, no actual functional data is provided in this study so it remains to be seen how frequently the insertion of FP exons is tolerated. It would help the study substantially to have functional information for a few insertions.

The value and utility of this study hinges on whether insertions of this type frequently retain function. The authors speculate that "labeling at an internal site of a gene is feasible as long as the insertion does not disrupt the function of the encoded protein. Many introns reside at the junctions of functional domains because introns have evolved in part to facilitate functional domain exchanges (Kaessmann et al., 2002; Patthy, 1999)." Thus an analysis of how often intron tags are tolerated as homozygotes would be helpful for users who will worry that a potentially "quick and dirty" CRISPIE insertion might not accurately report on the function and localization of their protein of interest.

2. Adoption of this approach by the community will depend on access to reagents and protocols. I applaud the authors for stating that they plan to deposit plasmids at Addgene (lines 349-350). However, they also need to provide a list or table of plasmids that will be deposited, along with a description of the purpose of each plasmid, to allow potential adopters to quickly figure out which constructs are needed. From the schematic provided in Figure 1—figure supplement 3, it appears that at least some of the constructs (b1-b5) must be modified prior to use to insert an sgRNA target that will release the synthetic exon from its plasmid; others (b6-b10) might not require any modification before transfection, but this needs to be clearly stated and explained. Do b6-b10 represent newer versions of the design that can be used without any cloning required? Which construct should a novice user choose when trying this approach for the first time? To answer these and related questions, I would urge the authors to provide a detailed protocol for targeting a new gene of interest – including all cloning steps – as a supplemental text file.

3. The results in figure 2B show that a population of CRISPIEd cells contains alleles with no insertion, correct insertions, and inverted insertions. I really wanted to know the relative abundance of these – especially the frequency of inverted insertions compared to correct, forwards insertions. This could be easily measured using qPCR of genomic DNA, and should be reported for several different targeted loci (and ideally in several different cell lines) to get a sense of how variable the insertions are. This is critical information to enable a reader to evaluate whether the CRISPIE approach will be useful for a particular application.

4. The high incidence of indel mutations at the 5' end of forward inserts (Figure 2D-iv, top row) is surprising, since previous reports have suggested that indels are relatively uncommon when using the NHEJ approach to target exons (Suzuki et al. Nature 2016; Artegiani et al. Nature Cell Biol. 2020). The authors don't provide an explanation for this difference – could it be a specific consequence of targeting introns? Or is it rather due to experimental differences such as choice of cell line, transfected plasmid concentration, etc.? Did the authors observe a similar indel frequency when targeting exons (in the experiment reported in Figure 3)?

5. Please report the data in Figures 3B-C as absolute labeling efficiencies instead of relative efficiencies. Normalizing efficiency to 1 is misleading and obscures the actual frequency of successful labeling.

Reviewer #1 (Recommendations for the authors):

The gene therapy literature has been touting introns as ideal targets for the very same reasons that you are here. So you should acknowledge them.

In line 144 you say "Had the coding sequence been targeted, an inverted label insertion would inevitably cause disruptive mutations. However, under our conditions, only wild-type and forwardly inserted mRNAs were detected (Figure 2B), demonstrating the advantage of CRISPIE." Rather than saying "our conditions" for clarity you should explain that the donor only contains splicing signals for new exon inclusion in one orientation. And so the mRNA is altered only by the forward insertion.

You mention that "to the best of our knowledge, this is the first demonstration of a readily reversible gene editing approach at the DNA level." The concept of reversibility is very well established in genome editing going way back to using loxP sites and Cre drivers. Numerous other CRISPR studies have described the incorporation of new sgRNA target sites for just this reason also. What you mean to say is that it is easier than these other CRISPR methods since you are in an intron where indels from DSBs will be better tolerated.

Reviewer #2 (Recommendations for the authors):

The authors should address the following points in their revision:

– Adoption of this approach by the community will depend on access to reagents and protocols. I applaud the authors for stating that they plan to deposit plasmids at Addgene (lines 349-350). However, they also need to provide a list or table of plasmids that will be deposited, along with a description of the purpose of each plasmid, to allow potential adopters to quickly figure out which constructs are needed. From the schematic provided in Figure 1—figure supplement 3, it appears that at least some of the constructs (b1-b5) must be modified prior to use to insert an sgRNA target that will release the synthetic exon from its plasmid; others (b6-b10) might not require any modification before transfection, but this needs to be clearly stated and explained. Do b6-b10 represent newer versions of the design that can be used without any cloning required? Which construct should a novice user choose when trying this approach for the first time? To answer these and related questions, I would urge the authors to provide a detailed protocol for targeting a new gene of interest – including all cloning steps – as a supplemental text file.

– The results in figure 2B show that a population of CRISPIEd cells contains alleles with no insertion, correct insertions, and inverted insertions. I really wanted to know the relative abundance of these – especially the frequency of inverted insertions compared to correct, forwards insertions. This could be easily measured using qPCR of genomic DNA, and should be reported for several different targeted loci (and ideally in several different cell lines) to get a sense of how variable the insertions are. This is critical information to enable a reader to evaluate whether the CRISPIE approach will be useful for a particular application.

– I was surprised by the high incidence of indel mutations at the 5' end of forward inserts (Figure 2D-iv, top row), since previous reports have suggested that indels are relatively uncommon when using the NHEJ approach to target exons (Suzuki et al. Nature 2016; Artegiani et al. Nature Cell Biol. 2020). The authors don't provide an explanation for this difference – could it be a specific consequence of targeting introns? Or is it rather due to experimental differences such as choice of cell line, transfected plasmid concentration, etc.? Did the authors observe a similar indel frequency when targeting exons (in the experiment reported in Figure 3)?

– Please report the data in Figures 3B-C as absolute labeling efficiencies instead of relative efficiencies. Normalizing efficiency to 1 is misleading and obscures the actual frequency of successful labeling.
