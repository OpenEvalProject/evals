# Peer review - Round 1

Editors:
- Adèle L Marston, University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88656.4.sa0](https://doi.org/10.7554/eLife.88656.4.sa0)

This important study makes use of AlphaFold2 to predict the models of tens of cohesin subcomplexes from different species. The models, which are in most cases consistent with published cohesin variants with compromised in vitro and in vivo cohesin activity, provide convincing evidence that leads to testable hypotheses of cohesin dynamics and regulation. More broadly, this study serves as an example of how to use AlphaFold2 to build models of protein complexes that involve the docking of flexible regions to globular domains.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88656.4.sa1](https://doi.org/10.7554/eLife.88656.4.sa1)

There are a number of outstanding questions concerning how cohesin turnover on DNA is controlled by various accessory factors and how such turnover is controlled by post-translational modification. In this paper, Nasmyth et al. perform a series of AlphaFold structure predictions that aim to address several of these outstanding questions. Their structure predictions suggest that the release factor WAPL forms a ternary complex with PDS5 and SA/SCC3. This ternary complex appears to be able to bind the N-terminal end of SCC1, suggesting how formation of such a complex could stabilize an open state of the cohesin ring. Additional calculations suggest how the Eco/ESCO acetyltransferases and Sororin engage the SMC3 head domain presumably to protect against WAPL-mediated release.

This work thus demonstrates the power of AF prediction methods and how they can lead to a number of interesting and testable hypotheses that can transform our understanding of cohesin regulation. These findings require orthogonal experimental validation, but authors argue convincingly that such validation should not be a pre-requisite to publication.

In their revised version, the authors did not systematically include model confidence scores, and it therefore remains difficult for the reader to evaluate the reliability of the models obtained. The authors correctly point out that such metrics are available on figshare. It is therefore possible to obtain such information. The caveat is that it remains to the user to identify and extract the relevant information. While they claim that they have labeled N- and C-termini in their figures, no such labeling can be seen in the revised version. Addition of such labels, at least for some of the figures, would help the user to navigate the models.

The authors have now updated figure legends to indicate which protein is referred to by the chain labels shown in PAE plots.

It is exciting to see AF-multimer predictions being applied to cohesin. As some of the reported interactions are not universally conserved and some involve relatively small interfaces the possibility arises that these interfaces show poor or borderline confidence scores. As some of these interfaces map to mutants that have previously been obtained by hypothesis-free genetic screens and mutational analyses, they appear nevertheless valid. Thus, an important point to make is that even interfaces that show modest confidence scores may turn out to be valid while others may be not.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88656.4.sa2](https://doi.org/10.7554/eLife.88656.4.sa2)

The ATPase protein machine cohesin shapes the genome by loop extrusion and holds sister chromatids together by topological entrapment. When executing these functions, cohesin is tightly regulated by multiple cofactors, such as Scc2/Nipbl, Pds5, Wapl, and Eco1/Esco1/2, and it undergoes dynamic conformational changes with ATP binding and hydrolysis. The mechanisms by which cohesin extrudes DNA loops and medicates siter-chromatid cohesion are still not understood. A major reason for the lack of understanding of cohesin dynamics and regulation is the failure to capture the structures of intact cohesin in different nucleotide-bound states and in complex with various regulators. So far only the ATP state cohesin bound to NIPBL and DNA have been experimentally determined.

In this manuscript, Nasmyth et al. made use of the powerful protein structure prediction tool, AlphaFold2 (AF), to predict the models of tens of cohesin subcomplexes from different species. The results provide important insight into how the Smc3-Scc1 DNA exiting gate is opened, how Pds5 and Wapl maintain the opened gate, how Pds5 and Scc3/SA recruit different cofactors, how Eco1 and Sororin antagonize Wapl, and how Scc2/Nipbl interacts with Scc3/SA. The models are for the most part consistent with published mutations in these proteins that affect cohesin's functions in vitro and in vivo and raise testable hypotheses of cohesin dynamics and regulation. This study also serves as an example of how to use AF to build models of protein complexes that involve the docking of flexible regions to globular domains.
