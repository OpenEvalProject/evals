# Peer review - Round 1

Editors:
- Alexander Westermann, Helmholtz Centre for Infection Research Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62438.sa1](https://doi.org/10.7554/eLife.62438.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study expands our definition of bacterial small RNAs (sRNAs) as it demonstrates functionality of several "nonconventional" sRNAs. The work is expected to boost future studies looking into bacterial sRNAs derived from 5'UTRs or ORFs in E. coli and beyond.

Decision letter after peer review:

Thank you for submitting your article "Regulatory roles of 5' UTR and ORF-internal RNAs detected by 3' end mapping" for consideration by eLife. Your article has been reviewed by four peer reviewers, including Alexander Westermann as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kevin Struhl as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Masatoshi Miyakoshi (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

In the present study, you have comprehensively identified the 3' ends of transcripts in E. coli and demonstrated that many arise from premature transcription termination in either Rho-dependent or intrinsic manner. As a result, you discovered numerous stable RNAs derived from 5'UTRs or CDSs and functionally characterized several of these "unconventional" RNAs as sponges of well-studied Hfq-dependent small RNAs. The reviewers all agreed that this is impressive work, the findings are novel and relevant for researchers within the microbiology and RNA communities and may inspire future studies of non-canonical bacterial sRNAs. Overall, they deem the results convincingly supported by the experimental data, but would like to see a few more experimental and analytical amendments to your work.

Essential revisions:

1) Comparison of global data sets: For cross-comparison, it would be advisable that the current data sets and previously published ones were analyzed consistently. This might increase the overlap between the results of the different studies.

a) Term-seq: The computational method used to process the current Term-seq data is different from the one presented in the original Term-seq paper of Dar and Sorek. The authors should explain why they turned to a different computational pipeline and – for cross-comparison – reanalyze the published data set from Dar and Sorek with their own computational methodology, or analyze their results by Dar and Sorek's computational method.

b) Rho-dependent termination: Since the authors here made the effort to treat the cells with BCM and generate sequencing libraries, it is not clear why they did not simply carry out Term-seq following BCM treatment and compared the identified 3' ends to those determined without BCM. Rather, the authors followed the analysis pipeline of Dar and Sorek who used available data of BCM-treated cells from Peters et al., 2012, and therefore could only evaluate the readthrough in the vicinity of determined 3' ends. Here also, the authors modified the computational method of Dar and Sorek. This needs justification and the parameters used should be explained (e.g. why using a window size of 500 nt and threshold of the Rho score of 2). For cross-comparison of the results, the Dar and Sorek data set and the current data set should be analyzed by the same method.

2) Evaluation of statistical significance: It is not always clear how the reported p-values of the hypergeometric tests were computed, and it is not possible to re-compute them as the value of N was not provided. Please verify that p (x{greater than or equal to} actual result) was computed and provide the details of the computation for all hypergeometric tests included in the manuscript.

3) Experimental validation: Several newly discovered 3' termination sites were tested experimentally. From the reported results it seems that all tested sites were validated by wet-lab experiments. Could the authors explain how the individual examples were selected? Were there any predicted 3' ends that could not be validated experimentally? If so, reporting true vs. false positives would provide another assessment of the reliability of the data.

4) Rho-dependent premature termination (–subsection “Novel sites of regulation are predicted by 3´ ends and Rho termination regions in 5´ UTRs”; Figure 2D, E, F): The results obtained from some of the northern blots seem confusing in light of the corresponding LacZ reporter assays. For example, the galactosidase experiments with cells from OD 0.4~0.6 showed an increase of LacZ activity in the rhoR66S mutant for most reporters, as expected (Figure 2D, E and Figure 2—figure supplement 1B). On the other hand, in several cases the northern blot analysis of total RNA extracted from cells at OD 0.4 revealed the increase of prematurely terminated 5'UTR fragments in the rhoR66S strain (Figure 2F and Figure 2—figure supplement 1C). Wouldn't these 5' fragments be expected to accumulate in the WT – rather than the R66S – strain, if they were generated through Rho-dependent termination? The authors' hypothesis that increased levels of longer transcripts in the absence of Rho could be processed to give rise to these shorter products (see the aforementioned subsection) could be better explained. In parallel, the northern blot membranes should be re-hybridized with probes for some of the sequences downstream of the termination sites to corroborate this assumption.

5) sRNA sponges: The exact effect of RybB on FtsO has not been clarified in the manuscript (subsection “ORF-internal FtsO is an sRNA sponge”). When RybB is abundant, the level of FtsO is reduced (Figure 7B). This may be indicative of coupled degradation upon base-pairing between FtsO and RybB. However, when RybB was induced by ethanol (Figure 7E), the level of FtsO was unchanged (or even increased), probably attributable to transcriptional activation of ftsI. To clarify the reciprocal regulation between RybB and FtsO and the consequences of their interaction, the half-life of each sRNA in the presence or absence of its counterpart sRNA should be quantified. Additionally, the (indirect) effect of FtsO on the RybB target ompC is not very pronounced (Figure 7E). Could the authors please quantify this effect on the protein level (e.g. by western blot, ß-gal assay) to further support the notion that FtsO-mediated sponging of RybB translates into a de-repression of RybB targets?
