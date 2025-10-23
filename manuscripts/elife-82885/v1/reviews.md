# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, https://ror.org/01cwqze88 National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82885.sa0](https://doi.org/10.7554/eLife.82885.sa0)

The authors show that an artificial-intelligence method can be used to predict the three-dimensional structure of protein-protein complexes formed between cellular factors that promote the assembly of bacterial outer membrane proteins. The structures are compelling because they explain previously published biochemical data and provide novel insights into the function of these factors.


---

# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, https://ror.org/01cwqze88 National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82885.sa1](https://doi.org/10.7554/eLife.82885.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Deep learning-driven insights into super protein complexes for outer membrane protein biogenesis in bacteria" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, overseen by José Faraldo-Gómez as the Senior Editor. Two of the reviewers have agreed to reveal their identity, namely Nir Ben-Tal (Reviewer #1); Arne Elofsson (Reviewer #3).

As you will see below, the reviewers conclude the manuscript is not suitable for publication for eLife in its current form, but they make specific recommendations to resolve their concerns. I recognize some of these revisions are substantial – nevertheless, I encourage you to take the time required to address these concerns convincingly and then submit a revised version.

Reviewer #2 (Recommendations for the authors):

In this manuscript, Gao et al., combine a very elegant virtual screening method (AF2Complex) based on Α Fold with known crystal structures to predict the structure of super-protein complexes in the E. coli cell envelope that play important roles in the biogenesis of outer membrane proteins (OMPs). The authors do an excellent job of validating their methodology. Their predicted structures both explain a considerable amount of biochemical data that has appeared in the literature (e.g., the crosslinking of PpiD to SecY and SurA to BamA) and provide compelling explanations for unresolved conceptual issues (e.g., how DsbA is recruited to the Sec machinery to form disulfide bonds as proteins are translocated into the periplasm). With one exception (see comment 4 below), the predicted structures also provide potentially important insights into the function of the assembly factors. In essence, this work describes an impressive example of the power of AI that should be of interest not only to investigators who study OMP biogenesis but also to the broader research community. I should also note that the manuscript is clearly and concisely written for a general audience.

Specific comments:

1) Lines 83-86 and Figures 1a, 4a and 6a: The authors selected predicted structures of known biological relevance for further study, but they do not comment on high confidence predictions of supercomplex structures of unknown biological significance. How can they distinguish predicted structures that have potential biological significance from those that simply represent noise/false positives? This is an important issue that requires further explanation, especially because the authors provide false-positive rates on lines 76/77.

2) In the paper by Alvira et al., (ref. 21) the authors argue that E. coli produce a "holotranslocon" in which SecDF and BAM interact across the periplasm. I was surprised that AF2Complex did not detect this interaction with a high confidence score. Does AF2Complex have a significant rate of "false negatives"? The authors should discuss this issue.

3) Lines 181-183 and Figure 4c: As suggested by many different studies, the C-terminal β signal of OmpA must be accessible to bind to the first β strand of BamA at a relatively early stage of assembly. Would the last β strand be accessible if the β barrel is wrapped around SurA? The authors should comment on this issue.

4) Lines 246-249: While the structural model of the BAM-BepA supercomplex shown in Figure 6 is intriguing, the idea that the protease activity of BepA is controlled by the probing of substrate β barrels as they bud from the BamA β barrel does not appear to be consistent with the literature. The authors propose that β barrels that are stalled within BamA permit the opening of the BepA lid and activation of the protease. This suggests that BepA degrades β barrels that are stalled at an early stage of assembly, but not at later stages. The work of Soltes, et al., (ref. 48), however, shows that BepA degrades an LptD mutant that has formed a nearly complete barrel (and that likely protrudes from the BamA barrel) while another protease (YcaL) degrades a second LptD mutant that engages BAM at an earlier stage of assembly. I realize that the stages of OMP assembly are currently rather vague, but the authors should discuss the work of Soltes et al., and state that it imposes a possible caveat on their model.

Reviewer #3 (Recommendations for the authors):

1) What is the advantage of running both monomer and multimer versions of AF2? Does it provide an advantage? In our benchmarks, the multimer is slightly better and roughly doubles the computational cost. Also, did you run 2 multimer versions (version 2.1.0 should not be used it makes bad predictions often)?

2) Why is not the top-hit for surA (oppA) discussed? Or any other of the high-scoring pairs?

3) The authors claim that an iScore of 0.4 is related to a 1.2% FPR. This would mean that yfgM would have roughly 100 interactions. Is this correct? If so, this would need to be discussed (and possibly proven experimentally). Here only discussion with PPID at rank 12 is discussed. Should it not be more likely that the other 11 higher-ranked models interact? Why are these ignored?

4) Would it not be computationally more efficient to use MMseqs2 to make the MSAs?

5) Why is it only tested on 4 proteins? I think it should be computationally possible to run it on many more (in particular as you already have the MSAs). At a minimum, all complexes shown in Figure 7 should be run through the pipeline to ensure these can be modelled.

6) How would the pipeline handle stoichiometry?

7) WHat happens if a set of the high-scoring pairwise interactions are fed into alphafold-multimer (which can handle up ~5000 residues). Can the large complexes be modelled?
