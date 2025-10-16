# Peer review - Round 1

Editors:
- Randy B Stockbridge, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83464.sa0](https://doi.org/10.7554/eLife.83464.sa0)

The goal of this study is to identify allosteric modulators of an SLC-1 amino acid transporter, ASCT2, which has been implicated in cancer progression. By combining computational and docking methods with functional measurements, this study provides convincing evidence for a conserved allosteric SLC-1 inhibition mechanism. The findings are important to the fields of transporter mechanism and SLC-1 pharmacology.


---

# Peer review - Round 1

Editors:
- Randy B Stockbridge, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83464.sa1](https://doi.org/10.7554/eLife.83464.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Conserved allosteric inhibition mechanism in SLC1 transporters" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Randy B Stockbridge as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Aldrich as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The following revisions are essential to support the central claims of the manuscript regarding the conservation of an allosteric inhibition site in SLC1 transporters:

1. The MD simulations should include detailed convergence analyses to support the conclusions. According the X-ray crystal structure, the UCPH-101 binding pocket is only accessible via the lipid membrane. It seems unlikely that the 100-ns timescales of the simulations is sufficiently long to permit conclusions to be drawn. The minimum length of the MD replicas should be chosen such that complete dissociation of UCPH-101 is observed in all the ASCT2 replicas. The authors should also comment on how independence of the simulation replicas is ensured.

2. A major conclusion of the paper is that ASCT2 and EAAT1 share a conserved allosteric inhibition mechanism. However, the reviewers are not convinced that an allosteric inhibition mechanism has been established for ASCT2. The data for UPC101 suggests a mixed inhibition mechanism (lines 460-465 and Figure 7). The authors should comment on why the mechanism of UPC101 inhibition differs for the two SLC1 subtypes. Likewise, the evidence that #302 acts as an allosteric inhibitor (i.e., that the inhibition constant is independent of substrate concentration) is quite sparse, since inhibition was only tested at two substrate concentrations, and different inhibitor concentrations were used at these two substrate concentrations. An experiment with constant #302 concentration and varying substrate concentration should be performed to establish the allosteric inhibition mechanism.

3. The only evidence that #302 binds to the same binding pocket as UPC101 is from docking studies. The authors should provide data that #302 binds in the same pocket in ASCT-2 as UCPH-101, for example by testing the same point mutations that were used for the UCPH-101 experiments.

4. The manuscript is written in a very technical manner. The reviewers recommend that the authors revise the manuscript for readability, taking into consideration eLife's broad readership. In addition, the studies of UPC101 inhibition of EAAT1 largely confirm previous studies that established the allosteric inhibition mechanism (PMID: 35192345; PMID: 33597752). In the text, the authors should clearly explain how their studies of UPC101/EAAT1 inhibition are significant advances beyond what is already known about the inhibition mechanism, or consider shifting the emphasis of the paper towards the more novel studies involving ASCT2 mutagenesis and inhibition.

Reviewer #2 (Recommendations for the authors):

The manuscript is written in a very technical way and should be edited to improve readership by a broader eLife community.

Throughout, 'trimerization' and 'scaffold' domain are used interchangeably. One term to describe this domain should be selected and used throughout the manuscript.

Line 24: the EAAT1 structure was solved by X-ray crystallography, not cryo-EM.

Line 53: the counter-transport of K+ and co-transport of H+ that also occur with glutamate transport are not mentioned.

Line 63-64: the description of the TMD making up the transport domain and the scaffold domain is incorrect.

Figure 1. in panel B, TFB-TBOA and UCPH-101 should be indicated clearly with labels and different colors. Line 233 states that UCHP-101 binding pocket is over 15A away from the substrate and cation bindings sites, but these are not indicated in the figure and it is not correct that the compound is 15A away from the substrate and all three of the Na+ ion binding sites.

What is the compound bound in Figure 2A? it would be useful to indicate the membrane in all structure figures as well as 'outside' and 'inside' the cell to orient the reader.

Figure 3, panel B – it is difficult to see the data in this panel, a logarithmic scale would be better.

Line 358: the word significantly is used but I can see no statistical analysis and the effect does not seem overly large.

The section (lines 362-379) is confusing, and I am not sure what these experiments are trying to show, the data in Figure S4 does not look different at all with error bars overlapping.

Table 1 shows the Km for various substrates for the ASCT2 mutants. There is no discussion or explanation offered as to why residues distant from the substrate binding site are impacting affinity and selectivity.

Figure 7D. Lines 460-465 state that the Ki for the single mutant does change as a function of serine concentration, and a mixed mode of inhibition is suggested. Why would the mode of inhibition change if UCPH-101 is binding in the same site? In addition, from the data in Figure 7D it appears to this reviewer that the Ki for UCPH-101 is also changing for the double mutant. This needs to be clarified.

Did the authors test if UCPH-101 inhibits the more closely related ASCT1? What is the conservation like in the UCPH-101 binding site?

Reviewer #3 (Recommendations for the authors):

(1) I strongly recommend to include experimental evidence that (i) compound #302 also mediates allosteric inhibition (i.e., that the inhibition constant is independent of substrate concentration) and (ii) that it binds to the same binding pocket in ASCT-2 as UCPH-101 (perhaps using the same point mutations that you have used for the UCPH-101 experiments).

(2) The MD simulations should include detailed convergence analyses to support their conclusions. Since the UCPH-101 binding pocket is presumably (according the X-ray crystal structure) only accessible via the lipid membrane, I doubt that the 100-ns timescales of your simulations are sufficiently long to permit reasonable conclusions. In any case, I would recommend that the minimum length of your MD replicas should be chosen such that you observe complete dissociation of UCPH-101 in all the ASCT2 replicas.

Furthermore, Figure 5 suggests you conducted four simulation replicas for each condition, whereas the main text says you have six replicas (line 388), what is correct?

Finally, how did you ensure independence of your simulation replicas?

(3) The conclusions of your MD simulations will also crucially depend on the chemical accuracy of your UCPH-101 model. Unfortunately, I could not find how you parameterized this compound consistent with the CHARMM force field. Please provide this information.
