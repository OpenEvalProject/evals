# Author response - Round 1

Authors:
- Jeroen Overman
- Frank Fontaine
- Mehdi Moustaqil
- Deepak Mittal
- Emma Sierecki
- Natalia Sacilotto
- Johannes Zuegg
- Avril AB Robertson
- Kelly Holmes
- Angela A Salim
- Sreeman Mamidyala
- Mark S Butler
- Ashley S Robinson
- Emmanuelle Lesieur
- Wayne Johnston
- Kirill Alexandrov
- Brian L Black ([ORCID: 0000-0002-6664-8913](https://orcid.org/0000-0002-6664-8913))
- Benjamin M Hogan
- Sarah De Val
- Robert J Capon
- Jason S Carroll ([ORCID: 0000-0003-3643-0080](https://orcid.org/0000-0003-3643-0080))
- Timothy L Bailey
- Peter Koopman
- Ralf Jauch
- Mark J Smyth
- Matthew A Cooper
- Yann Gambin ([ORCID: 0000-0001-7378-8976](https://orcid.org/0000-0001-7378-8976))
- Mathias Francois ([ORCID: 0000-0002-9846-6882](https://orcid.org/0000-0002-9846-6882))

## Response text

DOI: [10.7554/eLife.21221.028](https://doi.org/10.7554/eLife.21221.028)

[…] Whilst the reviewers find your results supports these major conclusions, they find that the following points should be adequately addressed before publication:

1) The claim of selectivity of SM4 against Sox18 deserves further investigation, in particular, to clarify if the potentially redundant activity of Sox17 in vascular development is also affected. Also, potential activity against Sox7 should be clarified. You may already have the required data on activity of SM4 against Sox17 and Sox7, in which case adding these to the figure and text, as well as commenting on their implications for the claimed selectivity of SM4 will be sufficient. In case this means you need to repeat experiments, we suggest to limit yourself to any that can be achieved reasonably within 2 months.

We acknowledge that selectivity is a crucial consideration for an inhibitor to be of use as a chemical probe or therapeutic. Therefore, we have broken down the matter regarding selectivity into three key aspects: PPI disruption, inhibition of transcriptional actvity, and SOXF loss of function phenocopy in vascular development.

PPI disruption selectivity

To further investigate the selectivity of Sm4 between all three SOXF family members (SOX7, -17 and -18) we have performed additional PPI analyses by ALPHAScreen, focusing on the recruitment of RBPJ (relevant in a vascular context as demonstrated by Sacilotto et al. 2013), MEF2C (only known SOX18 interactor, Hosking et al. 2001) and the SOX17 protein partner OCT4 (key determinant in endoderm specification, Jauch et al. 2011 and Aksoy et al. 2013).

Figure 1—figure supplement 1 (new): This in vitro protein-protein interaction analysis revealed that SOX18 has the capacity to selectively form a hetero-dimer with SOX7 and RBPJ whereas SOX17 does not interact with other SOXF proteins, nor does it interact with RBPJ or MEF2C. The interaction with RBPJ is conserved between SOX18 and SOX7 (left panel). Sm4 has the ability to interfere with SOX7-SOX18 heterodimer formation (IC50 19.6 μM, Figure 1—figure supplement 1F) and partially disrupts SOX7-RBPJ interaction. In addition, as suggested by reviewer #1, we have investigated the effects of Sm4 on SOXF-OCT4 protein-protein interaction. Results show that Sm4 has the potential to disrupt SOX17-OCT4 interaction but not SOX18-OCT4 or SOX7-OCT4.

Data shown in Figure 1 of the manuscript combined with new supplemental results (new Figure 1—figure supplement 2) suggest that Sm4 selectivity is mostly towards SOX18 but has some potential to interfere with SOX7- or SOX17-dependent PPI (in the high micro-molar range [Sm4] 50-100 μM). Our observations indicate that this inhibitory effect predominantly occurs in the scenario where SOX18 and the other SOXF protein share a particular interactor.

Of note the interaction between SOX17 and OCT4 (POU5F1) is not relevant to endothelial cell biology since this transcription factor is not expressed by endothelial cells as shown by transcripts analysis from FANTOM5 database (Author response image 1), and from the RNA-seq data in HUVECs generated in-house (Figure 2). Correspondingly, OCT4 was not identified in SOX18 ChIP-MS experiments performed in endothelial cells. We can therefore exclude that the SOXF-OCT4 interaction – and disruption thereof – contributes to the observed effects of Sm4-treatment in endothelial cells.10.7554/eLife.21221.018Author response image 1.Snapshot of FANTOM5 database, showing (absence of) OCT4 transcript levels in arterial, venous and lymphatic endothelial cell types.DOI: http://dx.doi.org/10.7554/eLife.21221.018

DOI: http://dx.doi.org/10.7554/eLife.21221.018

It is often challenging for small molecules to achieve selective targeting between closely related proteins, such as those within the SOXF group of transcription factors (SOX7,-17 and 18). The small molecule that we describe acts in such a way that SOX18-dependent protein complexes are disrupted. Each SOXF protein has its distinct ‘primary’ function mediated by specific sets of PPIs, which bestows opportunities for selective inhibition. However, these 3 TFs also do have certain PPIs in common, which could explain their overlaping function in the context of rescue mechanism. Redundancy has been shown for SOX7, 17 and 18 protein that can act interchangeably to rescue the loss of function of one another within the F-group (Hosking et al. 2009). The fact that Sm4 has the potential to inhibit a subset of SOX7, SOX17 or SOX18–dependent PPIs is an advantage to prevent any potential redundancy mechanism.

The claims regarding the specific targeting of SOX18 by Sm4 has been reworded more carefully in light of these new data (fifth paragraph of the main text). The additional PPI analysis has been added as new Figure 1—figure supplement 2.

Off-target profiling

To include a wider analysis of Sm4 specificity towards SOX18, we have performed an unbiased off target investigation using a CEREP/Eurofins/ Panlabs profiling panel. This is shown by a new data set we have now included in the revised version of our companion manuscript (standard profiling panel, new Table S3 Fontaine et al. Cell Chemical Biology). Proteins tested on this panel are representative of various biological processes, such as: GPCRs, kinases, nuclear receptors, HDACs, sirtuins and membrane receptors. CEREP uses as a cut off 50% inhibition to flag any potential off target effect. This panel analysis with Sm4at 10 μM did not flag any non-specific binding out of 36 protein tested.

Selectivity on transcriptional interference

To assess other SOX proteins’ activity that could be potentially affected by Sm4 we have included SOX9 and SOX17 as negative controls throughout the study. We show that Sm4 does not perturb:

SOX9 homodimer formation (Figure 1)

SOX9 transcriptional activity in cell-based assay in vitro (Figure 2—figure supplement 3)

SOX9-induced Col2a1 transactivation in zebrafish larvae (Figure 3—figure supplement 1)

SOX17-induced ECE1 transactivation (Figure 2—figure supplement 3).

The analysis of ChiPseq/RNAseq data sets (Figure 2) further demonstrates that Sm4 is specific to SOX18 interference amongst endothelial TFs, including SOX7.

Selectivity on vascular development- phenotypic output

The current data set based on two SoxF reporter assays in zebrafish (Figure 3), combined with the partial phenocopy of sox7/18 double morphants/knockout (Figure 3—figure supplement 2) and the ALPHAScreen data, demonstrates the ability of Sm4 to block Sox18 activity in vivo. Since Sm4 has the ability to interfere partially with Sox7/RBPJ interaction, we further investigated whether Sm4 could directly interfere with Sox7 function in zebrafish. For this approach, we used as a readout the phenotypic outcome of the sox7 KO zebrafish line (Hermkens et al. Development 2015) and compared it to Sm4-induced phenotype.

The hallmark of sox7 genetic disruption in zebrafish is a short circulatory loop in the head with no circulation in the trunk and tortuous lateral dorsal artery (LDA). In presence of Sm4, we observe a partial phenocopy of Sox7 loss of function characterized by a mild vascular defect in the LDA (Author response image 2). The observed Sm4-induced phenotype supports the conclusion that Sox7 activity is partially affected in presence of the small compound. However, the treated larvae fully establish blood circulation in the head (in contrast to the trunk), and do not form a short circulatory loop typical of Sox7 loss of function. This is now included in the text of the revised manuscript (eleventh paragraph of the main text). Of note, it is possible that the minor LDA phenotype is be secondary to the arteriovenous fusion phenotype.10.7554/eLife.21221.019Author response image 2.Sm4-treatment causes mild malformations to the lateral dorsal aorta (LDA), reminiscent of partial interference with Sox7 function.Head circulation is unaffected by Sm4.DOI: http://dx.doi.org/10.7554/eLife.21221.019

Head circulation is unaffected by Sm4.

DOI: http://dx.doi.org/10.7554/eLife.21221.019

Lastly, the use of various zebrafish model system to assess the effects of Sm4 in vivo during development (Figure 3 and Figure 3—figure supplement 1 and Figure 3—figure supplement 2) strongly suggest that Sm4 has no conspicuous effect on other SOX TFs. Interference (chemical or genetic) with developmental transcription factors at the stages we investigated would results in severe defects, while we observe that Sm4-treated zebrafish larvae develop normally, with the exception of the phenotype associated with perturbed SOXF function (malformation of axial blood vessels).

2) The discrepancy between the effects on the Dll4int3 reporter and endogenous Dll4 gene expression effects of SM4 need to be clarified. Given that the Dll4int3 reporter does not contain all regulatory elements of the endogenous Dll4 gene, it could be that SM4 is more effective against the reporter and other elements still drive endogenous Dll4. As you currently don't comment on the discrepancy in the text, it is difficult for us to recommend precisely how you should address this issue. We suggest to carefully compare the response of endogenous Dll4 expression similarly to the dose response you find for the Dll4 reporter. Given the dynamic nature of Dll4 expression, it could also be a timing issue, and thus related to the half-life of the drug? A possible experiment in vivo could be to show in situ hybridisation for Dll4 in WT fish treated with SM4. As Dll4 levels have a major impact on blood vessel formation also in tumour angiogenesis, and your in vivo mouse experiments show effects on tumour angiogenesis, we feel this needs to be clear in order to understand the action of SM4. This should be possible to address in two months. In case experimental data do not provide a clear answer, please address this issue carefully in text and Discussion.

We agree with the interpretation regarding the discrepancy in terms of activity comparing Dll4int3 synthetic reporter line versus endogenous dll4 expression. It is often the case that synthetic enhancers – containing only a discrete number of regulatory elements – are more responsive to a subset of regulators. For example, the synthetic -6.5kdrl promoter that we use the assess SoxF activity is highly responsive to Sox7 and Sox18 activity, while the endogenous gene kdrl (flk1) is not (Duong et al. 2014). We also observe this for this synthetic promoter fragment using both Morpholino approaches and Sm4-treatment (Figure 3).

Work by Sacilotto et al. demonstrated that deletion of the Sox binding motif in this Dll4int3 enhancer fragment leads to a loss of transcriptional activation, which demonstrates that this transgene is dependent on SoxF activity (Sacilotto et al. 2013). This does not mean that the endogenous regulation of dll4 solely relies on SoxF activity. It has been shown that another dll4 enhancer Dll4int12 is also required to drive proper expression of this gene in endothelial cells (Wyth et al. 2013). This enhancer relies on Ets and Rbpj combinatorial mode of action and it is unknown whether SoxF are at play to modulate this particular regulatory element.

In the context of vascular development in the zebrafish and mouse, Sacilotto et al. showed that individual loss of SoxF proteins or Rbpj has little effect on Dll4in3 activation, and correspondingly, we show in our study that Sm4 treatment slightly affects this transgene in zebrafish (Figure 3). A more profound effect was observed when Sm4-treatment was combined with rbpj morpholino injections. Overall, we do not claim that Sox18 is a master regulator of dll4 expression, nor do we suggest that Sm4 is a chemical regulator of dll4 transcription. Instead, we utilize Dll4int3 synthetic enhancer activity as a readout for on-target Sox18 inhibition. To make this clear to the reader, we have adjusted the text accordingly (tenth paragraph of the main text).

In order to explore the effect of Sm4 on dll4 endogenous transcriptional activation we have performed in situ hybridization on DMSO ctrl and Sm4 treated zebrafish larvae, as suggested (Author response image 3).

This analysis shows that the effect of Sm4 on the endogenous dll4 transcript is not as profound as the effects observed on Dll3int3 enhancer activity. This result is consistent with the qRT-PCR data analysis of dll4 in Sm4-treated zebrafish larvae (Figure 4G), which also show a very mild reduction in the overall dll4 transcript levels.10.7554/eLife.21221.020Author response image 3.Effect of Sm4 on endogenous dll4 transcript in 27 hpf zebrafish larvae.Both the dorsal aorta and intersomitic vessels (ISV) were labeled by dll4 ish probe. In presence of Sm4(1 μM) ISV show a mild decrease of signal intensity.DOI: http://dx.doi.org/10.7554/eLife.21221.020

Both the dorsal aorta and intersomitic vessels (ISV) were labeled by dll4 ish probe. In presence of Sm4(1 μM) ISV show a mild decrease of signal intensity.

DOI: http://dx.doi.org/10.7554/eLife.21221.020

3) The mechanism of reduced tumour angiogenesis and metastasis should be adequately discussed and ideally experimentally clarified. Given that the route of metastasis is likely through lymphatics and that Sox18 also regulates lymphangiogenesis, we feel you should consider this as potential mechanism. As you have the expertise in mouse lymphatic analysis from previous studies, we hope you will be able to provide experiments that show whether or not SM4 interferes with tumour lymphangiogenesis through blocking Sox18 function. It will not be necessary to show that this is the definitive cause for changes in metastasis, but we feel that without analysing lymphatics, this work is incomplete. Given that you use a xenograft model, it should be feasible to perform these experiments within the 2 months of revision period.

We greatly appreciate this suggestion, given the reported role of Sox18 in lymphangiogenesis and the contribution of lymphatic vasculature to the malignancy of many types of solid tumour. To address this request, we have quantified the tumour-induced lymphangiogenic response in absence or presence of Sm4. Immunofluorescence staining of 4T1.2 tumour sections was performed for lymphatic specific markers PROX1 and Podoplanin along with the blood vascular marker endomucin. Results show that both lymphatic vessel density and number of lymphatic endothelial cells is reduced in presence of Sm4 treatment. This lack of lymphatic outgrowth in presence of the small molecule is likely to contribute to the decrease in lung metastasis and improved disease latency. This result is now included in the manuscript as new Figure 4—figure supplement 4 and in the main text (fifteenth paragraph).
