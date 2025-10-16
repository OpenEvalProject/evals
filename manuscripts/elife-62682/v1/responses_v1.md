# Author response - Round 1

Authors:
- Alessandro Stirpe ([ORCID: 0000-0002-2006-4066](https://orcid.org/0000-0002-2006-4066))
- Nora Guidotti
- Sarah J Northall
- Sinan Kilic
- Alexandre Hainard
- Oscar Vadas ([ORCID: 0000-0003-3511-6479](https://orcid.org/0000-0003-3511-6479))
- Beat Fierz
- Thomas Schalch ([ORCID: 0000-0002-0758-3013](https://orcid.org/0000-0002-0758-3013))

## Response text

DOI: [10.7554/eLife.62682.sa2](https://doi.org/10.7554/eLife.62682.sa2)

Essential revisions

The following must be addressed in your revision:

1) Additional support for the claim that the mutants are only (or mostly) impaired in the ubiquitin binding activity.

We have performed thorough enzyme kinetics for wild type vs mutants, which are shown in Figure 3G and fitted parameters are tabulated in Table 1. These experiments establish that the mutants are severely affected in substrate binding specifically for the H3K14ub substrate.

Unfortunately, we ran into quality issues with the Cisbio kit, and we had to switch to Promega's MTase-glow Methyltransferase kit. While there are quantitative differences between the results obtained with the two kits they agree very well qualitatively.

2) Clarification of allostery vs. changes in binding affinities (Rev 1, point 4) ideally including measurements for the binding affinity of WT and mutants to the H3 peptide with and without ubiquitin.

We have clarified our interpretation of H3K14ub's effect on Clr4 with the following changes to the text on p. 5. This interpretation is well supported by the comprehensive kinetic analysis discussed in (1). Measuring affinities of the unmodified peptide directly by ITC failed because the Kds are very high and require concentrations that we could not reach. Change to manuscript:

"Comparison of the kinetic parameters between H3K14ub and H3 substrate indicates that the presence of ubiquitin on lysine 14 leads to a tighter enzyme-substrate complex and to conformational changes in the active site that increase the rate of the methyltransferase reaction.

To determine whether H3K14ub uses an allosteric site for ubiquitin on Clr4, we challenged the methyltransferase reaction with increasing amounts of free ubiquitin. While we observed no significant increase in activity for unmodified H3, we observed a drop in the activity for H3K14ub at high concentrations of free ubiquitin (Figure 1E). This experiment failed to produce evidence of an allosteric site for free ubiquitin on Clr4 and we conclude that the stimulation of kcat is likely to depend on an induced-fit mechanism triggered by binding of H3K14ub to the Clr4 HMT domain."

3) Better characterization of silencing defects: ChIP-qPCR data should be included for both the dg and dh regions across mutants (Rev 3, point 4).

We have further characterized the UBR mutants with ChIP-qPCR data for dg, dh and tlh1, and have added them to Figure 4E. These results do not show a differential effect in dg vs. dh for the Clr4FA mutant.

4) Analysis of the conservation of structural features in SUV34H2 (Rev 3 point 5)

We have added a comprehensive sequence and motif analysis in Figure S5D and E with the following text added to the end of the discussion:

"Bioinformatic analysis of the UBR sequence using Hidden Markov Models suggests that the UBR sequence is well conserved in the Ascomycetes clade of fungi, which includes the N. crassa Dim-5 protein for example (Figure S5D, E). Comparing the Clr4 motif with motifs obtained using homologous sequences from human SUV39H2, human G9a and Arabidopsis SUVH4 shows that SUV39H2's motif is very similar to Clr4, while G9a and SUVH4 diverge significantly. This is consistent with our observation that H3K14ub can stimulateSUV39H2, but not G9A or SUVH4."

Reviewer #1:

1. Similarity and difference with the previous study. As the authors acknowledge, this manuscript builds on a previous study by Oya et al., however I think the similarities and the differences need to be made even more explicit and better addressed.

1.1. The authors should clearly state that Figure 1B and 1C are basically a confirmation of Oya et al., 2019.

We have added: "These experiments confirm the observation by Oya et al., 2 that the H3K14ub substrate triggers a dramatic and specific increase in the methyltransferase activity of Clr4. However, in contrast to the previous study, we observe that the KMT domain is sufficient to mediate this regulatory mechanism."

1.2. I am more puzzled by the difference in the mapping of the region required for H3K14ub stimulation. The authors suggest that a difference in the preparation of the recombinant proteins might be responsible. This can and should be tested as it would seemingly be a simple experiment (compare with and without GST tag).

We agree that we cannot explain the discrepancy satisfactorily. However, Shan et al. 1 have completely independently confirmed our result and we therefore chose to focus our resources on characterizing the mutants.

1.3. Possibly to reconcile their findings with the previous report the authors state in the description of Figure 1 that "the N-terminus plays a regulatory role in the sensing of H3K14ub by the catalytic domain" but I don't see this reflected in the data show in Figure 1C, given that the degree of stimulation is very similar for KMT and FL.

We agree that our data do not establish the statistical significance to make this claim firmly and have therefore withdrawn the sentence.

2. Stimulation-defective mutants. The authors should carefully discuss the stimulation-defective mutants, which should be premised on the retention of their methyltransferase activity on unmodified H3.

We have addressed this by the kinetic analysis of the mutants in Figure 3G.

3. Heterochromatin localization of Clr4 mutants. The FLAG ChIP results in Figure 4E is not very informative, as with the loss of heterochromatin a loss of Clr4 is predicted. If the authors want to test whether the localization activity of Clr4 mutants is intact, (1) FLAG ChIP in the clr4+, Flag-Clr4GS253/F3A background (i.e., two clr4 alleles exist) or (2) in vitro H3K9me2/3 binding assay should be performed. Since Clr4 N-terminus might regulates MTase activity as discussed in Pg 18 line 19, it is also possible that amino acid substitutions in the KMT region affect the function of N-terminus, including CD. The co-IP in Figure 4C is not sufficient to clarify this point as Clr4 directly binds heterochromatin via its CD, in addition to the CLRC-mediated mechanism, and it is unclear if this is affected in the mutants.

We agree that the FLAG ChIP exclusively reports on the presence of Clr4 in heterochromatic regions and that the data confirm what is expected when heterochromatin is lost. We also agree that the proposed experiments would be very interesting and could potentially provide revealing insight into the recruitment of Clr4. However, we are of the opinion that dissecting the contribution of CD, H3K14ub and potentially other mechanisms to Clr4 recruitment goes beyond the scope of this manuscript, which is focused on the enzymatic stimulation of Clr4 through H3K14ub.

4. Allosteric vs. binding regulation. On Pg. 11, the authors suggest that an allosteric mechanism is at play, but this is not supported by the data. In fact the observation that providing ubiquitin in trans does not stimulate and rather inhibits the activity on H3K14ub would suggest that the ubiquitin just increases binding affinity. To clarify this the authors should measure binding affinity of WT and mutants to the H3 peptide with and without ubiquitin.

This point has been addressed in Essential Points 2.

Reviewer #2:

Is the H3K14ub-mediated stimulation a shared property of SUV39 class methyltransferases? This is a quite important question considering the mechanisms underlying heterochromatin assembly in eukaryotic cells. While the authors demonstrate that SUV39H2's enzymatic activity is stimulated by H3K14u (Figure 5A), it would be interesting to test whether the activity of SUV39H1, the other mammalian Su(var)3-9 homologue, is also stimulated by the presence of H3K14ub.

We agree that it would be very interesting to screen the SUV39 enzyme family to determine which members share the H3K14ub-mediated stimulation. However, we feel that addressing this question is beyond the scope of this manuscript.

Reviewer #3:

1. The relevance of the proposed mechanism in a cellular chromatin context is unclear. A significant fraction of H3K9me2/3 nucleosomes isolated from cells should also carry H3K14ub in cis. How frequently do K9Me2/3 and K14ub co-occur on nucleosomes in heterochromatin regions? This could explored by westerns with anti-H3K9me2 and or me3 – a mobility shift equivalent to monoubiquitylation should be visible.

Oya et al., have addressed this question by showing that H3K14ub can be detected in pulldown of H3K9me2. Doing this quantitatively is extremely difficult since H3K14ub is very likely removed efficiently by deubiquitinases during isolation procedures. We would like to point to Shan et al., 1 who provide further genetic evidence that the H3K14ub modification is critical for H3K9me2/3 in a physiological context.

2. The authors should consider including mutant peptide controls such as H3K9RK14ub to make sure what is detected here is indeed H3K9 methylation. Additionally, a completely unrelated substrate such as a ubiquitylated H4 N-terminal peptide could be used in the methyltransferase assays to strengthen the authors claims of specificity.

We agree that our manuscript does not fully address the question of specificity and have adjusted the wording accordingly. (see response to Rev 1, point 3.)

3. The IP-western (Figure 4C) shows association of Clr4 proteins with the Rik1 and suggesting that they are incorporated into the CLRC complex. However, a more rigorous test would be analysis these IPs by mass spectrometry to determine if the Clr4 GS253 and F3A mutant proteins are indeed assembled into a CLRC complex containing the other components.

The IP-Westerns clearly show that Clr4 remains associated with CLRC even though heterochromatin is lost. We believe that hunting after potential secondary consequences for the CLRC complex is beyond the scope of this manuscript.

4. The Clr4-F3A mutant appears to have a differential effect on the level of transcript generation from the dg and dh regions of centromeric repeats. For completeness ChIP-qPCR data should be included for both the dg and dh regions (currently only dh is assayed Figure 4 E) to determine if a difference is also detected.

We have included the requested ChIP-qPCR data in Figure 4E.

5. Are similar structural features found in the SUV39H2 KMT domain to those shown for Clr4 (Figure 5C) that would also allow ubiquitin to dock? Does computational comparison between Suv39H2, Clr4, G9a and SUVH4 provide insight into similarities/differences?

We have included a corresponding sequence analysis in Figure S5D, E.
