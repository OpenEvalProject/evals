# Peer review - Round 1

Editors:
- Volker Dötsch, https://ror.org/04cvxnb49 Goethe University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85216.sa0](https://doi.org/10.7554/eLife.85216.sa0)

This is an important study of the mechanism of how binding of the fatty acid myristic acid (MYR) inhibits the activity of the kinase c-Abl, a critical regulator of many cellular processes. While the general aspects of this regulation are known from structure determination and biochemical studies, the exact molecular mechanism and the nature of the allosteric inhibition were not known. The authors use MD simulation to close this gap and provide a compelling mechanistic description of the inhibitory mechanism.


---

# Peer review - Round 1

Editors:
- Volker Dötsch, https://ror.org/04cvxnb49 Goethe University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85216.sa1](https://doi.org/10.7554/eLife.85216.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Myristoyl's dual role in allosterically regulating and localizing Abl kinase" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Volker Dötsch as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Roberto Covino (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. As you will see, there is general support for the data presented, but some questions remain.

Essential revisions:

1) The overall simulation times seem to be rather short (several repeats, but only 500 ns) for such a large system with large conformational changes. There might be statistical convergence issues, especially because at least some of the starting structures were generated from available experimental structures after some modifications/modelling, and they might thus be out of equilibrium and need some time to fully relax during the MD simulations.

2) There do not seem to be convergence tests concerning the length of the simulations, which are usually considered to be standard analyses and a requirement for publication (Appendix Figure 5 shows the effect of different thermostats and capping of the peptide chain, but no tests concerning simulation time). This could be critical in the present case, where the authors acknowledge themselves (e.g., on p. 4) that there are only subtle differences between the different simulation systems and the variations within a given system are larger than the relevant (putative) differences between systems (Figure 1 C, D, E).

3) Issues with statistical convergence are expected not only for the standard MD simulations but also for the umbrella sampling simulations, as 50 ns sampling per window is nowadays not considered state of the art and is likely insufficient for quantitative binding free energy calculation, especially for membranes (see, e.g., DOI 10.1021/ct200316w).

4) Concerning the metadynamics simulations, these are usually done to obtain a free energy landscape. Why was this not attempted here? In the present case, the authors seemed to have used metadynamics only for generating starting structures, with different degrees of helicity of the α_I part, for subsequent standard MD simulations.

5) It would be superb if the authors could propose precise predictions that could inspire future experiments. Now that they present a residue-resolution allosteric pathway, can they suggest point mutations that would interrupt it? In addition, the evolutionary conservation of the residues identified to constitute the allosteric networks should be analysed.

6) The almost total absence of structural renders is surprising. Given the thorough discussion of structural details in the introduction, some renders would surely aid the reader.

Reviewer #2 (Recommendations for the authors):

– I was surprised about the almost total absence of structural renders. Given the thorough discussion of structural details in the introduction, some renders would surely aid the reader. I must admit that initially, I got a bit lost. Structural renders would help a lot also to appreciate the authors' mechanistic hypotheses.

– line 88 all systems contained ATP – this comes out of the blue, some explanation could be useful.

– Figure 1B. Please explain in the caption the inset and the color code. In general, the caption could give a more detailed explanation of all the symbols and colors used.

– Figure 5. Please make clearer in the caption what the long loop connecting Myr to the protein complex is.

– Regarding the free energy calculations, these are of course the most challenging ones from a technical point of view. The risk of these calculations is that there might be some hysteresis, that would impact the quantitative accuracy of the Δ Gs. Ideally, the protocol developed by Domanski and Best could help make these results more stable.
