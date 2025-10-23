# Peer review - Round 1

Editors:
- María Mercedes Zambrano, CorpoGen Colombia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70021.sa0](https://doi.org/10.7554/eLife.70021.sa0)

This work will interest researchers who want to explore the functional potential of metagenomes. The authors present an original approach, MetaGPA, for performing enrichment analysis on cohorts of metagenomes and use it to identify a novel enzyme that can modify cytosines in DNA from natural bacteriophage populations.


---

# Peer review - Round 1

Editors:
- María Mercedes Zambrano, CorpoGen Colombia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70021.sa1](https://doi.org/10.7554/eLife.70021.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A Genome-Phenome Association study in native microbiomes identifies a mechanism for cytosine modification in DNA and RNA" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Reviewing Editor Maria Zambrano and Michael Marletta as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this letter to help you prepare a revised submission.

Essential revisions:

The work to obtain functional information from metagenomes is both novel and promising but various issued need to be addressed to support the claim of reproducibility and broader applicability. In particular, the manuscript must provide a more detailed methodology, substantially improve the characterization of their MetaGPA approach, particularly the bioinformatics, and clearly state the limitations of this method and its capacity to be used as a general tool for other searches and metagenome functional analysis.

1) Please take into account previous work, describe how these relate to the presented work and clearly indicate the motivation for MetaGPA in the introduction. The relationship between the author's program and previous attempts at GWAS-like analyses in microorganisms are not thoroughly described in the Introduction. For example, the authors do not mention TreeWAS or other similar approaches.

2) The Methods section contains information that presumably relates to the pipeline, but there is no explicit mention of MetaGPA. There are also seemingly pipeline-related methods that are not part of the codebase. The beginning section of the Results is insufficient to explain the MetaGPA method. A reproducible example is a must.

3) An attempt was made to run the code to confirm reproducibility. The GitHub link contains no information on installation or examples of how to run the code on test or new data. The code itself contains hard-coded file paths that would make it difficult, if not infeasible, to run on another person's machine. There are also dependancies that are unstated. The code must be substantially better documented to be of utility outside this study.

4) The reasons for the use of Tet2 and BGT to modify 5mC and 5hmC are unclear. The newly discovered 5-carbamoyloxymethylcytosine is unlikely to be deaminated by A3A

and hence what is the need for Tet2 and BGT? In fact, other than 5-methylcytosine, larger modifications of cytosine would not be substrates for APOBEC3A (PMID: 28472485). The investigators could treat all the DNA with A3A, divide it into two halves, and then use the USER kit to destroy DNA that contains uracils in one-half of the samples. The DNA that survives should contain a cytosine modification that protected it against A3A. Comparison of sequences of the two populations would show that only a small fraction of DNA has survived A3A+User treatment. If the ability of A3A to deaminate 5mC is a major concern, the authors do not articulate it. However, this can be easily remedied by replacing A3A with APOBEC3B-CTD or APOBEC3G-CTD neither of which is good at deaminating 5mC.

5) The USER kit contains E. coli Exonuclease VIII. This is problematic because this enzyme will excise oxidized pyrimidines in DNA. Thus, the DNA of any organism that routinely modifies its pyrimidines in such a way that it becomes susceptible to ExoVIII, would be eliminated from the case DNA regardless of whether it contains uracils. An AP endonuclease or simple treatment with NaOH and heat would be preferable here.

6) This methodology is designed to work for cytosine modifiers that near 100% efficient and are not sequence-specific. I do not see how this methodology could isolate genes for sequence-specific cytosine modifiers. If an enzyme strongly prefers a certain sequence motif, say 5'-TpC, then all the cytosines in the VpC sequence context (V is not T) would remain unmodified. These would be deaminated by A3A and virtually all the DNA from that organism would be destroyed by the User kit. The methodology may also have difficulty isolating genes for enzymes that modify only a fraction of the cytosine bases, say 25%. Such DNA would also be destroyed during the A3A+User treatment. Such limitations of the methodology should be carefully examined.

7) How does MetaGPA handle phylogenetic resampling (i.e., dealing with the fact that genomes are related)? This is particularly important for microorganisms. It would have been preferable to see the author's method benchmarked in a similar way, if not compared against, previous approaches to similar problems.

8) The manuscript jumps quickly into the main finding of cytosine modification. What are other applications of this technique? How could one incorporate a negative control to quantify FP rates or incorporate other controls?

9) I am somewhat confused by the discussion about the putative thymidylate synthase homologs. The authors point out that several TS homologs contain a change that is equivalent to a N177D change in E. coli TS. They further note that such a change in the E. coli enzyme results in a change of substrate from dUMP to dCMP. Does this mean that these phage genes code for dCMP methyltransferases, not thymidylate synthases? If so, they may be novel enzymes, as E. coli does not contain a dCMP methyltransferase and unlike TS, the normal methyl donor for cytosine methylation is S-adenosylmethionine. The methyl donor for TS is tetrahydrofolate. It would be useful to characterize these variant TS enzymes for substrate specificity and cofactor requirements.

10) It is unclear how the investigators arrived at the substrate and co-factor requirements of the newly discovered enzyme. The classic example of a carbamoyltransferase is ornithine carbamoyltransferase which tranfers the carbamoyl moiety to a nitrogen not to an oxygen. It also appears (https://www.brenda-enzymes.org/enzyme.php?ecno=2.1.3.3) that ornithine carbamoyltransferase does not require ATP as a co-factor. With that in mind, the putative new carbamoyltransferase could have modified the N4 of cytosine without the need for ATP. Did the investigators explore this possibility? Overall, a clearer rationale needs to be provided for how the requirements for the enzyme were established.

11) Interestingly, E. coli bacteriophage Mu carries N6-carbamoylmethyladenine. Is the enzyme that performs this reaction in any way related to the newly discovered enzyme?

12) The only justification for using phage DNA as the source of new enzymes provided by the authors is "phages are known to carry a large diversity of modifications". Another obvious reason for using phage DNA is that few phage genes contain introns. However, this convenience comes with the likely drawback that many DNA modification enzymes in cellular genomes are being missed from their screen. The authors should carefully address this issue.

13) Figure 3b is unclear. What are the units of the color (scale) bars? What am I supposed to take away from this panel? What is red and what is blue (beyond the minimal description in the figure legend)?

Reviewer #2 (Recommendations for the authors):

1. Page 2- Change "who is out there?" to "what is out there?".

2. Page 6- "unmodified cytosines are deaminated to uracils using the DNA cytidine

deaminase Apolipoprotein B mRNA editing enzyme catalytic polypeptide-like 3A

(APOBEC3A) (Carpenter et al., 2012)"- This is misleading on two counts. Among the APOBEC3 subfamily of cytosine deaminases, APOBEC3A is most efficient at deaminating 5mC, in addition to C. Furthermore, the ability of APOBEC3A to cause cytosine deamination was first demonstrated in HBV genome (PMID: 19169351) and the purification of the enzyme and its biochemical characterized was first reported by a different research group than cited in the manuscript (PMID: 22798497).

3. Page 11- "DNA ligase (PF14743.7, PF01068.22), and Cytidine deaminase (PF00383.24) are other domains that have been found in DNA modifying enzymes (Subramanya et al., 1996) (Bhattacharya et al., 1994)"- Did you mean DNA-cytosine deaminase? A cytidine deaminase would convert the ribonucleoside cytidine to uridine.

4. Page 18, last paragraph- The comparison of T4 genome with the contig in which carbamoyltransferase gene is found is confusing. Why is the occurrence of dCMP hydroxymethylase and β-glucosyltransferase in T4 genome "resembles" the occurrence thymidylate synthase and carbamoyltransferase in the contig? Phages have very compact genomes and tend to aggregate genes with related functions. Furthermore, dCMP hydroxymethylase is presumably an oxidase and not a transferase. If this is what led to the prediction of the reaction of the newly discovered carbamoyltransferase, it was a really inspired guess- I say that in all sincerity.
