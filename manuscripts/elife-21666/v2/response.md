# Author response - Round 1

Authors:
- Alicia N McMurchy ([ORCID: 0000-0002-7033-8790](https://orcid.org/0000-0002-7033-8790))
- Przemyslaw Stempor ([ORCID: 0000-0002-9464-7475](https://orcid.org/0000-0002-9464-7475))
- Tessa Gaarenstroom
- Brian Wysolmerski
- Yan Dong
- Darya Aussianikava
- Alex Appert
- Ni Huang ([ORCID: 0000-0001-8849-038X](https://orcid.org/0000-0001-8849-038X))
- Paulina Kolasinska-Zwierz
- Alexandra Sapetschnig
- Eric A Miska ([ORCID: 0000-0002-4450-576X](https://orcid.org/0000-0002-4450-576X))
- Julie Ahringer ([ORCID: 0000-0002-7074-4051](https://orcid.org/0000-0002-7074-4051))

## Response text

DOI: [10.7554/eLife.21666.040](https://doi.org/10.7554/eLife.21666.040)

Essential points:

1) Does upregulation of repetitive elements through loss of heterochromatin disable or overload the piRNA pathway? The authors could address this by small RNA-seq in the different heterochromatin mutant backgrounds, and would expect to see a change in the 21U/22G population if the piRNA pathway is overloaded (i.e. upregulation of a repetitive element leads to a bias in the 22G population in the mutant and a decrease in other 22Gs), or a loss of 21Us if piRNAs are completely eliminated. A simpler experiment might be to see whether any of the RNAi treatments in Figure 4 restore piRNA sensor silencing in the heterochromatin factor mutant backgrounds to link repetitive element expression and/or DNA repair to piRNA pathway function.

Small RNA sequencing was previously done for hpl-2 mutants in Ashe et al., 2012, where they found normal levels of piRNAs targeted to the piRNA sensor and to a few endogenous target genes. We have extended this analysis to the whole genome and find that piRNA levels are normal in hpl-2 mutants. We also tested whether piRNA dependent 22G RNAs were produced in hpl-2 mutants using the method in Lee et al. 2012 to define piRNA targets. We found that piRNA dependent 22G RNA levels were reduced in prg-1 mutants, as expected, but levels were normal in hpl-2 mutants. These results suggest that hpl-2 acts downstream of piRNA biogenesis and subsequent 22G production. We have added these data to the paper in Figure 6—figure supplement 1.

As suggested, we also tested whether RNAi of cep-1, spo-11, or MIRAGE1 elements restored piRNA sensor silencing in heterochromatin mutants and found that none did, arguing that the role of heterochromatin factors in the piRNA pathway is independent of these genes (see Author response image 1). Because this experiment does not conclusively show that the affected pathways are not involved, we have decided not to include this figure in the paper.10.7554/eLife.21666.036Author response image 1.Quantification of piRNA sensor expression in wild type and heterochromatin mutants hpl-2, let-418 and lin-61.Animals were fed on indicated RNAi bacteria from L1 at 20°C and scored as 1 day old adults, similar to Figure 6D. A minimum of 15 worms were scored over 2 independent experiments. None of the RNAi treatments resilenced the sensor.DOI: http://dx.doi.org/10.7554/eLife.21666.036

Animals were fed on indicated RNAi bacteria from L1 at 20°C and scored as 1 day old adults, similar to Figure 6D. A minimum of 15 worms were scored over 2 independent experiments. None of the RNAi treatments resilenced the sensor.

DOI: http://dx.doi.org/10.7554/eLife.21666.036

2) The authors could use ChIP-seq or immunofluorescence for histone modifications in heterochromatin factor mutant backgrounds in order to demonstrate the loss of heterochromatin marks at repetitive elements. Without such experiments, the connection between heterochromatin proteins and small RNA pathways remains tenuous. If the authors cannot add such experiments they must at least explain and discuss this.

We agree that better understanding the connection between heterochromatin proteins and small RNA pathways is important. The suggested experiments would address the role of heterochromatin proteins in regulating histone modifications but not the link to small RNA pathways. However, were able to make use of published H3K9me3 ChIP seq data in four nuclear RNAi mutant backgrounds to explore this connection. Analysing these datasets, we found that germ line nrde pathway mutants (hrde-1, nrde-2, nrde-4) had decreased H3K9me3 marking at heterochromatin regulated loci, but there was no change in nrde-3 mutants, which are defective in nuclear RNAi in the soma (Figure 7—figure supplements 2 and 3). The decrease in H3K9me3 levels on heterochromatin targets that are not upregulated in nrde-2 mutants, supports redundancy in target regulation.

3) In Figure 4: Is the increase in fertility in response to mirage, cep-1, and spo-11 knockdown (KD) a general phenomenon or specific to heterochromatin mutants? The authors could compare the brood size of wt cells with and without KD of the above genes. Measure fold change in wt plus or minus KD and compare to the fold change seen in mutants.

Because mutation of cep-1 or spo-11 does not cause an increased brood size (Rinaldo et al. 2002 and Figure 4B), the effect of RNAi knockdown on heterochromatin mutants is not due to a general increase in fertility. We have strengthened the fertility suppression results by testing whether mutation of cep-1, like RNAi, suppressed the decreased fertility of heterochromatin mutants. We found that hpl-2; cep-1, lin-13; cep-1, and let-418; cep-1 double mutants all had larger brood sizes than the corresponding heterochromatin single mutants, confirming the RNAi results. In addition, we observed that mutation of cep-1 also partially rescued the somatic growth defect of the mutants, suggesting that the interaction is not limited to prevention of cell death. Because p53 is important for mediating DNA damage signaling, the results suggest that such signaling may underlie heterochromatin factor defects. We include the new cep-1 double mutant results in Figure 4.

4) Figure 5: how specific is the cep-1-mediated promotion of apoptosis in response to DNA damage? Do cells with no DDR also show an increase in survival if cep-1 is knocked down? The authors could compare the survival of wt cells with and without cep-1 knockdown and compare this to the fold change observed in mutants.

See response to point 3 above. In addition to promoting apoptosis in the germ line in response to DNA damage, cep-1/p53 is also responsible for the slow growth caused by loss of DNA damage checkpoint protein CLK-2/TEL2 (Derry et al., 2007). Similarly, we observed that mutation of cep-1 suppressed the slow growth phenotypes of hpl-2, lin-13, and let-418 (Figure 4C). We do not know if fertility suppression by loss of cep-1 is due to prevention of apoptosis or another stress response. To reflect this, we now write: “The increase in fertility upon cep-1/p53 inhibition may be a direct consequence of reduced germ line apoptosis, or alternatively the effect may be indirect, by preventing DNA damage signalling or improving growth rate.”

5) The authors should highlight the novelty of their own findings in this manuscript by discussing their contributions in the context of what has been previously published in nuclear RNAi, piRNA and heterochromatin in C. elegans and other organisms e.g. Ashe et al. 2012; Gu et al. 2012; Burton et al. 2011; Buckley et al. 2012; Ni et al. 2014).

We have rewritten and expanded the Introduction and Discussion to better explain previous studies and the advances made by our study.
