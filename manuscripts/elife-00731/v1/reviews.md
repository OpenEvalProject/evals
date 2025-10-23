# Peer review - Round 1

Editors:
- David Baulcombe, University of Cambridge , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.00731.026](https://doi.org/10.7554/eLife.00731.026)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Herbarium metagenomics reveals the rise and fall of the Phytophthora lineage that triggered the Irish potato famine” for consideration at eLife. Your article has been favorably evaluated by a Senior editor and 4 reviewers, one of whom is a member of our Board of Reviewing Editors.

The following individuals responsible for the peer review of your submission want to reveal their identity: David Baulcombe (Reviewing editor); Paul Birch (peer reviewer); William Fry (peer reviewer).

The reviewers agreed that this is an interesting and important paper. It draws on both the availability of historic samples of P. infestans and the power of next-generation sequencing to re-evaluate the 19th century pandemic that precipitated the Irish Famine. Overall, the conclusion of a single clonal lineage, HERB-1, dominating the late blight population outside of Mexico for at least 50 years, closely related to US-1, but perhaps giving way to variants derived from the latter, is well supported by the data. The derivation of both HERB-1 and US-1 from a common ancestor within a “metapopulation” outside of Mexico, the accepted centre of P. infestans diversity, again seems likely. Of interest is the apparent increase in ploidy levels in 20th century isolates, compared to HERB-1 and US-1, although it should be stressed that this is based entirely on projected allele frequencies (rather than backed up by other means).

In addition, there is part of the analysis that they consider to lack detail and that the conclusions may be reaching too far. These concerns are summarised by one of the reviewers who writes:

1) The authors state: “Given that nineteenth century potato strains [surely they mean cultivars?] in North America and Europe did not yet contain resistance genes to control HERB-1, one would expect HERB-1 to contain a full effector gene complement”, as it has not yet been disrupted “…by the selective forces imposed by resistance gene breeding”. What exactly is meant by a “full effector gene complement”? I guess they intend the focus to be on avirulences recognised by the S. demissum R genes? These would be AVR1, 2, 3a, 3b, and 4 of those shown in Table 2; the others are not pertinent to their line of logic. In Table 2, the coverage of AVR2 is 100% for the isolate 06_3928A, a “Blue_13” genotype representative. Actually, this genotype lacks AVR2, expressing instead AVR2-like, which suggests that the % coverage they show in this table is lacking the detail to reach their conclusion: “consistent with the expectation that the HERB-1 genotype was avirulent on the first potato cultivars that acquired late blight resistance through breeding”. The focus is on AVR3a, and it is interesting that the KI allele alone exists in the HERB-1 lineage. Did they specifically amplify and sequence this gene from all of the herbarium samples? If their conclusions are based entirely on sequence assemblies (from NGS of ancient DNA), then they need to be backed up by additional experiments. AVR4 has been well documented to be “lost” through mutation that leads to truncated proteins. Is AVR4 intact in the historical samples? I am surprised by the apparent absence of Avr3b. This is a gene that is conserved in P. parasitica, for example. Indeed, they show good coverage in mirabilis and ipomeae in Table 2. Did they specifically check this absence by alternative means (i.e., PCR and sequencing)?

2) The reviewers believe that these concerns can be addressed in a straightforward fashion, if you amplify and directly study AVR3a (done), AVR2/2-like and AVR4 sequences across the samples to add weight to conclusions about HERB-1 being avirulent. You could also include Avrblb1, avrBlb2, and AvrVnt1 in this, as controls. The corresponding R genes have not been bred into the cultivated potato, so they represent a contrast in terms of the selection pressures that they refer to in 20th century breeding efforts (i.e., introduction of the demissum R genes).

Please respond to these suggestions, including additional data where appropriate, in a revised manuscript.

An expert reviewer on phylogenetic analysis makes the following substantive point:

3) Before running the BEAST analysis, the modern sequences alone are clock tested. I doubt whether these data contain enough signal to detect substantial rate variation, but it is important to test whether there is enough temporal signal in the data to trust the dating analyses.

To do this, it is common to correlate the sampling date against the root-to-tip distance from the ML tree (or NJ tree). This would give a visual indication of the amount of temporal signal in these data (e.g., Harris et al. Science 2010). Second, (and optionally) it is also common to carry out randomisation tests, rerunning the BEAST dating analyses a few times after randomly permuting the sampling dates (see e.g., Firth et al. MBE 2010).
