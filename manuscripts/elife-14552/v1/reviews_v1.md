# Peer review - Round 1

Editors:
- Elaine Ostrander, National Human Genome Research Institute, National Institutes of Health , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.14552.033](https://doi.org/10.7554/eLife.14552.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Mitochondrial genetic diversity, selection and recombination in a canine transmissible cancer" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Elaine Ostrander as the Reviewing Editor and Mark McCarthy as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a well-written and concise paper that addressed the next natural step in unraveling the mystery of CTVT in the dog. The figures are clear (and attractive). Overall the paper does an outstanding job documenting, through low-coverage sequencing and phylogenetic analysis, the frequent transfer of mitochondrial DNA from the affected host to the canine transmissible venereal tumor (CTVT). Sequencing reveals that acquisition of host mtDNA has occurred at least five times during the worldwide spread of the clonal tumor, and that these five clades acquired their mtDNAs around 1,000 years ago. The sequences further suggest that there has been retention of ORFs, suggesting selection for function in the acquired DNAs. The data for the five clade hypothesis and horizontal transfer is convincing. The paper can be strengthened however in a few ways.

Essential revisions:

The reviewers felt this was a strong and important contribution to an interesting field. They identified several issues, however, that need to be addressed. These include:

1) Two reviewers raised the issue of the Indian-CTVT clade (IV), which implies highly non-clock-like evolutionary rates within the ancestor of the lineage. It is found at the end of fairly long branches and it may not be accurately placed within the phylogeny. One possibility is that this observation may be the result of the ML search that was performed [(Phyml with rudimentary branch swapping – a "combination of NNI and SPR")]. This approach may be insufficient to search treespace with such a large number of OTUs. The reviewers ask that the analysis be repeated with the newest version of RAxML which has more thorough search options. Alternatively, the authors should closely check the sequences or alignment as this could be due to minor alignment errors.

2) Two reviewers also raised the issue of the full-length mitochondrial NUMT that is found in the dog genome. The reviewers state that NuMTs are a major confounder in many species, and it was well-served to be addressed. However, over 150 NuMTs have been discovered in the canine genome. It is unclear how the wgsim recreation of reduced CTVT reads aligned to the canine genome would demonstrate how NuMTs are unlikely to contribute significantly to mtDNA variant calling. During CTVT evolution, particularly in an organism purported to engage in mictochondrial capture, it is likely that novel NuMTs were introduced that diverge from the canine genome. While the authors are likely correct that current mtDNA assemblies have not been compromised by NuMTs, if the NuMT is tandemly arrayed (as they are in many mammalian genomes) it could be highly multicopy and approach the read depth of the true cytoplasmic copies. The authors should check this by estimating read depth of the dog NuMT insertion within the nuclear genome and see if is collapsed and determine the expected depth based on this measurement, rather than assuming one copy. This will certainly raise the caliber of the paper.

3) The time estimate of 11,000 years cited in this work was estimated using a subset of extant canine variation to isolate ~1.9 million somatic mutations, and perform a strict clock approach based on the mutation signature of human medulloblastoma. Subsequent work used a more comprehensive catalog of canine variation resulting in a 50% reduction in total somatic mutations. A reanalysis of the timing of CTVT origin may be warranted and particularly useful for the field.

4) The authors discuss the phenomenon of mitochondrial recombination, but do not discuss the likelihood of heteroplasmy. If mitocapture is a mechanism prevalent in CTVT, it is likely that these tumors are heteroplasmic. Are the authors indicating that mitochondria from the original CTVT founder, or a subsequent host prior to Clade A is no longer present, and has been supplanted completely by now homoplastic horizontal transfer? The issue of tumor clonality / subclonality is not addressed.

5) The authors use an in-house variant caller that is based on paired tumor-normal samples. Since CTVT by its nature does not have a normal sample, why was another caller that did not rely on tumor /simulated normal used? Please explain.

6) Why was ploidy estimated to be 1.5 for CTVT and 2.0 for host? The reference indicates that CTVT is diploid.

7) Importantly, there is no indication of where the mtDNA alignments or variants, and low coverage nuclear data is deposited for future replication. This must be done prior to acceptance of the paper for publication.
