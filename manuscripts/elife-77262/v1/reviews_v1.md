# Peer review - Round 1

Editors:
- Jesse H Goldberg, https://ror.org/05bnh6r87 Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77262.sa0](https://doi.org/10.7554/eLife.77262.sa0)

This fundamental work in songbirds shows that stereotyped neural sequences known to drive the correspondingly stereotyped acoustic structures of adult songs can exist very early in development even when songs are variable and before birds have been provided song models by tutors. The evidence is exceptional and includes imaging activity of populations of premotor neurons in singing birds. This paper provides important insights into the mechanistic foundations of how nature and nurture work together to produce learned motor sequences.


---

# Peer review - Round 1

Editors:
- Jesse H Goldberg, https://ror.org/05bnh6r87 Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77262.sa1](https://doi.org/10.7554/eLife.77262.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Self-organization of songbird neural sequences during social isolation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Yarden Cohen (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) In the abstract and elsewhere, the authors write that 'experience is not necessary for the formation of sequences.' This statement is a bit of a reach – this paper exclusively shows that tutor exposure is not necessary for chain formation. It's conceivable that the experiences of deafening, muting or the absence of singing WOULD block chain formation. It's also possible that cohabitation with females – who call – could play some rudimentary auditory experience that helps establish chains. Please edit the language of the manuscript to make sure the conclusions match specific experimental results. Comb the manuscript for use of the work 'experience' and ensure that tutor-experience is what's written.

2) The adequacy of the sequence detection method (seqNMF) and analyses of its outcomes need further explanation and support. This is especially needed when describing results where sequences are truncated, jittery, or otherwise variable (as some of the results indicate). The presentation of results will be strengthened by:

2.1. A clear presentation of seqNMF's outcomes and fit to data:

2.1.1. Explaining in the main text and methods what is meant by 'sequences' that the algorithm extracts. It is not clear if these are cells activating one after the other or any robust spatiotemporal pattern. seqNMF allows seeking 'event based' or 'part based' factorization. Please describe which was used in this manuscript.

2.1.2. How much of the data variability is explained by sequences?

2.1.3. How specific are neurons' activity to sequences (compared to its activity not in sequences).

2.2. Control analyses (or citation if shown elsewhere) can show that the atypical properties of sequences are not confounded by seqNMF.

2.2.1. For example, measures in Figure 1E-K may be compared to sequences extracted from time-shuffled data. (Similar to the 'sequenciness' approach defined by previous work of the authors[3]).

2.2.2. Alternatively, if at all possible (because data is limited), results could be compared to analyses carried out on held-out data. For example, sequences can be discovered in training set data and used to calculate results as in Figure 1E-K on test set data.

2.3. Is it possible to compare sequences (the W's) found before and after training? The claim that they persist needs quantitative support.

3) The tutoring process and its effects need a clearer presentation.

3.1. The methods are vague about the process of tutoring (specifically, how many days of tutoring each bird received).

3.2. When describing (in text and in figure panels) the effect of tutoring it is most helpful to show: (3.2.1) the tutors template, (3.2.2) parts of the template that were copied by the tutee. Currently, the manuscript shows newly adopted syllables but doesn't demonstrate that these syllables were copied from the tutor. (3.2.3) The imitation score. These elaborations on tutor match can be put in a supplemental figure.

4) In all figures the spectrograms are tiny and it is very difficult to see the link between the identified sequences and the acoustic structure of song. Please revise figures so that the reader does not have to simply depend on somewhat abstracted statistical measures of song locking to absorb the result. Please make spectrograms bigger in the figures.

Also In Figure 1C, the first and second sequences seem to overlap. E.g., for the second sequence (magenta) the units in the upper sequence also participate. I assume that whether the seqNMF algorithm generates these two sequences or merges them is dependent on the parameters? But either way, how do we interpret these sequences: is the conclusion that the same units participate in more than one sequence (in the same order) or that it is the same, but noisy sequence? How often were different there shared sub-sequences between the identified sequences?
