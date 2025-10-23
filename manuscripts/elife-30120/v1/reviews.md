# Peer review - Round 1

Editors:
- Andreas Martin, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.30120.035](https://doi.org/10.7554/eLife.30120.035)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Regulatory coiled-coil domains promote head-to-head assemblies of AAA+ chaperones essential for tunable activity control" for consideration by eLife. Your article has been favorably evaluated by Ivak Dikic (Senior Editor) and three reviewers, one of whom, Andreas Martin (Reviewer #1), is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Eilika Weber-Ban (Reviewer #2); Gabriel C Lander (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Carroni and Franke et al. identify and characterize the resting state of Staphylococcus areus ClpC, in which the coiled coil middle domains (MDs) mediate a head-to-head interaction of two pentameric ClpC lockwashers. Comparison of cryo-EM reconstructions for ClpC in the absence and presence of the adaptor MecA gives intriguing structural insights into potential mechanisms for ClpC activation, where the disruption of the MD coiled-coil interactions by MecA splits the ClpC lockwashers apart and induces their reconfiguration into hexamers with robust ATPase and protein unfoldase activity.

The combination of these structural data with mutagenesis, biochemical analyses, and in vivo studies allows the proposal of a compelling model about the role of MDs in regulating the ClpC oligomeric state, MecA adaptor interactions, and the proteolytic activity of the ClpCP protease. So far, only structures of the active, MecA-bound ClpC hexamer had been available, whereas the mechanisms underlying ClpC's inactivation in the absence of MecA remained elusive. The present study thus significantly advances our understanding of ClpC regulation and unravels a new concept of AAA motor regulation by coiled coil middle domains.

Essential revisions:

1) A major concern regarding the biochemical experiments is that none of the presented degradation assays were performed under true steady state or multiple turnover conditions. The authors used either 0.3 μm FITC casein or 0.2 μm GFP-SsrA substrate with 1 μm ClpC and 2 μm ClpP. Neither in the figure legends nor the Materials and methods it is specified whether the ClpC and ClpP concentrations refer to monomers or hexamers/tetradecamers, but assuming monomers, those concentrations would be equivalent to 166 nM ClpC6 and 142 nM ClpP14. There is not even enough ClpP to saturate all ClpC, and the substrate concentration is barely above the enzyme concentration. Consequently, degradation kinetics (e.g. in Figure 1) strongly resemble exponential behavior, as expected for single-turnover reactions. Measuring the initial slopes of these curves, as done by the authors, may give a qualitative impression of enzyme activity, but is certainly not suited to determine quantitative degradation rates.

In addition, the substrate affinities of WT ClpC and its various MD and N-domain mutants remain completely elusive, and it is unclear whether the used concentrations reflect saturating conditions. This is particularly important when comparing ClpC mutations that differentially affect the ATPase activity or substrate affinity. For instance, it is proposed that the ClpC N-domain interferes with GFP-SsrA binding and therefore degradation. However, N-terminal deletion also leads to an almost 20-fold stimulation of WT ATPase activity and a > 2-fold stimulation for the F436A and R443A mutants. It therefore remains unclear whether the N-terminal domain indeed inhibits GFP-SsrA binding or makes GFP unfolding less efficient due to lower ATPase activity.

In general, performing these measurements at just a single substrate concentration is certainly not sufficient to quantitatively compare the degradation activities of ClpC variants with mutations that differentially affect Km and Vmax.

To draw reliable conclusions about substrate binding and ClpC motor activity, the authors should perform Michaelis-Menten analyses for at least a couple of key mutants presented, and otherwise should perform multiple-turnover measurements with saturating concentrations of substrate to derive more reliable degradation rates. The reviewers agreed that this should be easy to accomplish with the FITC-casein and especially the GFP-SsrA model substrates that can be produced in high amounts.

2) Similarly, the concentrations used for measuring the stimulatory effects of casein substrate on the ATPase activity of WT ClpC/P are not ideal for quantitative analyses (Figure 2B). Even though the authors confirmed a 1:1 complex of ClpC and MecA, they used only 0.2 μm MecA with 1 μm ClpC and 10 μm casein. Under these conditions, 80% of ClpC subunits would not be bound to MecA. In addition, the authors again used only 2 μm ClpP monomers, equivalent to 142 nM ClpP14 (while there is 166 nM ClpC6 present). Having not all ClpC saturated with ClpP and MecA thus leads to strongly convoluted ATPase rates, with contributions from free ClpC, ClpC/P, MecA-ClpC/P, and substrate bound MecA-ClpC/P, which doesn't allow accurate quantitative conclusions about the stimulatory effects of substrate. The authors should therefore repeat those experiments under saturating conditions, both for substrate and MecA.

3) The fact that the lockwasher is pentameric and not hexameric is intriguing – there does appear to be disordered density that might correspond to a sixth subunit in Figure 3—figure supplement 1E. No mention is made of this density, and the reviewers wondered if the authors tried low-pass filtering the density or viewing the density at low iso-surface thresholds to assess the possibility that this is a transiently or flexibly associated sixth subunit. The SLS data suggest that the complex is decameric, but this region should nonetheless be investigated through further cryoEM analysis, such as by focused classification using a 3D mask in this area. There may be a subset of particles that more clearly resolved density. Or does the conformation sterically prevent the association of an additional subunit? This should be explored in more detail.

4) Based on their finding that the F436A-DWB mutant stayed monomeric in the absence of nucleotide, the authors propose that the ClpC decameric structure relies entirely on MD contacts. This is surprising, and given the presented structural data (Figure 4C and D) it is hard to imagine how the MDs could provide sufficient lateral interactions to hold neighboring ClpC subunits together. Is there indeed no contribution of the AAA1 and AAA2 domains, which seem to have much more extensive interactions than the MD and neighboring N-domains?

Do the authors have information about whether or not deltaN ClpC can form an inactive higher order resting state like wt ClpC? Based on the structures, this seems unlikely, as the N-domains feature prominently in achieving the resting state.

In general, the authors should attempt to clarify the role of a potential interplay between N-domains and M-domains, and how much the effects observed for MD deletion or mutation might in fact stem from a MecA-mediated association of MD with the N-domain. Could the viability defects observed in vivo not also be explained by the fact that without MD, MecA cannot keep the N-domains away to the side?

5) Based on the observed effects of ClpC MD mutants on cellular viability, the authors propose that the M-domains are essential to control ClpC/P degradation activity by inactivating ClpC in the absence of MecA. The authors should test and confirm this model by co-expression of WT ClpC and MecA, which is expected to have the same phenotype/toxicity as delta-N ClpC F436A (unless MecA-bound WT ClpC has a much more restricted substrate specificity).

Major points:

1) Flexible fitting was stated as being used to generate the atomic model of the ClpC-MecA structure, but very few details are given regarding its generation, aside from the fact that iModFit was used. Why was flexible fitting not used to generate a model of the ClpC double lockwasher, which is at higher resolution? The fitting shown in Figure 3C has much of the atomic model out of density, and should not be used for detailed structural interpretation. For example, in the second paragraph of the subsection “Head-to-head interactions of M-domains mediate formation of an inactive ClpC resting state”, the authors state that the trans-acting arginine fingers are displaced away from the nucleotide binding pockets (Figure 3—figure supplement 1F), but given the limited resolution of the map and poor fitting of the atomic model, this cannot be claimed. The reviewers agreed that it is fine to include side chains in the models depicted in Figure 3D and 4, as these data are supported by biochemistry. However, when depositing atomic models based on the presented intermediate resolution EM, the models should only include the C-alpha's of amino acids.

2) The ClpC-MecA structure is described as "asymmetric", but is the structure organized as a spiral, as has been shown in numerous other AAA ATPases? If not, this is novel and should be described in more detail.

Also, the structures of Hsp104 and VAT in a steep lockwasher-like conformation were recently solved – are there any structural similarities with the resting state of ClpC?

3) It's puzzling that 3D classification was not performed at any point – this is regularly used before 3D refinement of a structure to identify a set of conformationally and compositionally homogeneous particles for processing, and then a classification without further alignment is performed after refinement to identify the subset of particles containing the highest resolution information. If these steps were performed and all 3D classes looked identical, this should be stated. Furthermore, it isn't clear which final density from Figure 3—figure supplement 1G was used for the structural analyses. The final structure from cryoSparc appears to be at higher resolution than the RELION structures – what was the reported resolution of this structure? Was C2 symmetry applied?

4) The authors use glutaraldehyde crosslinking to analyze how MecA and the F436A mutation affect the formation of the decameric resting state of ClpC (Figure 5A). Surprisingly, lane 9 shows that most of the double-Walker B mutant still forms the decamer (or even larger structure) in the presence of MecA. Was this trend also observed in the MecA-bound EM sample? In the Discussion, the authors state that "once formed, the ClpC6/MecA6 complex is stable and does not dissociate spontaneously". Why then does MecA-bound ClpC-DWB show any crosslinking larger than hexamers?

5) It is surprising that, based on gel filtration results (Figure 5B), the formation of ClpC decamers is ATP-dependent, whereas hexamer formation is not, and the authors should try to discuss this. Furthermore, how does the limited interaction surface of MDs (~ 50 A2) compare to the AAA interfaces? Is this interaction indeed substantial and strong enough to disrupt the interactions in a planar, ATP-bound AAA ring when MecA is absent?

6) MecA has been shown in B. subtilis to promote assembly from a lower assembly state (monomeric/dimeric) to the active hexamer. Although the authors convincingly show the existence of an inactive higher order assembly of S. aureus ClpC, it remains unclear why such a complex is beneficial. This should be discussed.

The authors suggest that activation upon MecA association occurs via monomeric ClpC. Can they provide evidence for that? Can it be excluded that the double-spiral dissociates into two single spirals that then transition more directly into the hexameric state?

7) It is proposed that the MecA adaptor is degraded and ClpC consequently inactivated when substrates are no longer available. However, the strong cytotoxicity of MD mutants in E. coli would suggest that the substrate specificity of ClpC/P is rather broad. The authors also speculate that deregulated ClpC/P may go after newly synthesized proteins, which raises the question whether ClpC/P would indeed ever run out of substrates to then be inactivated. Is the assumption that MecA makes ClpC/P more specific and less promiscuous than MD mutants like F436A? The authors should try to address this in their Discussion.
