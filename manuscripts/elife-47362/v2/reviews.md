# Peer review - Round 1

Editors:
- Stipan Jonjic, University Rijeka Croatia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.47362.035](https://doi.org/10.7554/eLife.47362.035)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Systematic identification of cancer cell vulnerabilities to natural killer cell-mediated immune surveillance" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tadatsugu Taniguchi as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors employed a genome-wide CRISPR-Cas9 pooled sgRNA screen to identify genes that impact the susceptibility of the K562 cell line to NK-cells in a co-culture assay. Following infection with a genome-scale single guide RNA (sgRNA) library, Cas9-expressing K562 cells were challenged with NK-cell line in vitro or left to grow without challenge. A population of leukemic cancer cells that survived the NK-cell challenge, as well as control cells, were assessed for sgRNA abundance. This analysis revealed two sets of genes, inactivation of which either significantly enhanced or diminished the sensitivity of K562 cell line to NK-cell challenge. These two gene sets were comprised of genes involved in (1) formation of tumor immune synapses or (2) IFNγ signaling pathway. The most significantly enriched target in K562 population following NK-cell challenge was ICAM1, whereas the most significantly depleted target in K562 population following NK-cell challenge was the cullin4-RING E3 ubiquitin ligase (CRL4) substrate adaptor DCAF15. Further experiments confirmed that the disruption of this protein led to an increase in activating molecules such as CD80, but also inhibitory molecules such as MHC I. Since the effector cells were NK-92, the investigators saw an overall increase in NK-92 activity against the target cells, dependent on DCAF15 activity. Furthermore, the investigators presented data on novel substrates of DCAF15. They also provide first evidence between a link of DCAF15 and the cohesion complex. Ultimately, the study presented how the use of an unbiased CRISPR-Cas9 screen can lead to potential new therapies based on the discovery of unique proteins involved in immune surveillance.

Essential revisions:

1) All experiments including the CRISPR screen have been performed with NK92 cells, which do not recapitulate all features of primary NK cells. The authors should at least include primary NK cells to investigate the functional relevance of the proposed mechanism as validation (experiments shown in Figure 3B-C, Figure 4C, 4E). NK-92 cells are very different from primary fresh or activated NK cells, and therefore modulating the expression of DCAF15 may not even be relevant in clinical settings. This would increase the validity of the suggestion that DCAF inhibition may have immunomodulatory properties. The authors claim that the DCAF15 KO phenotype is dependent on CD80 upregulation and a more APC like state of K562s, which promotes NK92 activation. This mechanism should be validated for primary NK cells. Is CD28 really expressed on human NK cells and is this mechanism then relevant? Can the authors speculate if DCAF15 may play a role in bona fide APCs for regulating NK cell activation during immune responses?

2) Authors validate that indisulam-induced CD80 upregulation can also be achieved in other cell lines in addition to K562s. It should be tested if CD80 upregulation by indisulam treatment and/or by DCAF15 KO also makes these additional cell lines (Daudi and Ku812 cells) more sensitive to NK92 killing. What about CD33? This is also a top hit and antibodies are available – can that be used as control?

3) The authors identify ICAM1 and components of the IFNγ pathway as top hits as genes whose loss promote resistance of K562s towards NK92-mediated attack. These findings contrast recent data available on bioRxiv from a similar K562 CRISPR screen performed with primary NK cells (Klein et al., 2019), where B7H6 (NCR3LG1) was found as a single dominant hit in a comparable setting. B7H6 however only scored as #26 in their screen. This may indicate differences in K562-related resistance mechanisms against the functionally restricted NK cell line NK92 in contrast to primary NK cells. This must be at least discussed and further emphasizes the necessity to validate the outcome of the study with NK92 in a primary NK cell setting.

4) PTPN2 and DCAF15 knockout results in upregulation of MHC-I (Figure 4A), but still enhances NK cell killing, which is counterintuitive and against the dogma that low MHCI promotes NK cell cytotoxicity (missing self). This discrepancy should at least be discussed in more detail. Please also include a discussion on Dufva et al., 2018, where the expected effect that loss of IFN signaling enhanced tumor cell lysis is described. NK92 cells have restricted KIR expression, this may explain the reduced sensitivity towards MHC-I-mediated inhibition. Under this NK92 specific conditions further NK-cell activating effects of IFNγ may dominate in contrast to the situation in primary NK cells. These potential differences between NK92 and primary NK cells must be validated in more depth.

5) The authors do not provide/discuss a potential mechanism of how loss of IFNγ responsiveness in their screen promotes NK cell resistance. They exclude a direct cytostatic/cytotoxic effect of IFNγ. May that be related to a suppression of the proposed APC-like state of K562, associated with lower CD80 etc. levels? CD80 and other APC activation markers should be investigated e.g. on STAT1-KO (or IFNGR KO) K562 cells.

6) Can the RNA-seq data be exploited to speculate about the underlying mechanism of the growth inhibitory effect of PTPN2 knockout cells in contrast to WT K562 and DCAF15 KO cells in presence of IFNγ (Figure 4C)? Is there a threshold of hyperactivity of IFNγ signaling or may other PTPN2-controlled mechanisms play a role? Do the growth inhibitory effects of PTPN2-KO in presence of IFNγ produced by NK92 account for depletion of PTPN2-KO cells in the screen? Or does PTPN2 KO similar to DCAF15 KO also contribute to an APC-like inflamed state of K562s (e.g. CD80 upregulation)?

7) Figure 4B: The pSTAT1 levels are over-exposed in a manner that would prevent detection of any differences. I do see a reduced pSTAT1 phosphorylation of dCAF15 lanes versus control. Please repeat and show lower exposures – there may be something hidden.

8) Figure 7 is of great interest regarding the cohesion complex association. Can the authors explore that in more depth? What is the relation between cohesion mutations and DCAF165 expression? Can that at least be explored in silico in the AML samples? As it is the biochemical data appear a bit "lost".

9) Since the authors have identified many other intermediate molecules involved, it remains unclear what is the role of other receptors which are differentially regulated after inactivation of DCAF15. Some of these molecules may also be important in co-stimulation. Is there any specific reason why the authors focus on CD80 except that indisulam, an inhibitor of DCAF15, has a substantial impact on this receptor? Also, the ultimate mechanism by which DCAF15 disruption led to increased expression of CD80 is not clear.

10) As suggested by authors, upregulation of CD80 in DCAF15 KO cells may result in their differentiation towards APC-like properties. Indeed, they have shown that DCAF15 KO cells revealed higher levels of APC markers CD80, CD40, as well as MHC-I molecules which could give them the capacity to prime and present antigens to T-cells. Do T-lymphocytes have any role in better control of cancer cells lacking DCAF15? The authors have shown that the level of DCAF15 correlates with survival rate in patients, but this is by no means a proof of survival association with NK-cells.
