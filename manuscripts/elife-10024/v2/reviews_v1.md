# Peer review - Round 1

Editors:
- Richard Aldrich, The University of Texas , , Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10024.022](https://doi.org/10.7554/eLife.10024.022)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Near-infrared photoactivatable control of Ca2+ signaling" for peer review at eLife. Your submission has been evaluated by John Kuriyan (Senior editor) and three reviewers, one of whom, Richard Aldrich, is a member of our Board of Reviewing Editors, and another is Murali Prakriya.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

He et al. integrated several techniques to a create photoactivatable system called "Opto-CRAC" that controls Ca2+ influx into cells through CRAC channels. The high Ca2+ selectivity of CRAC channels is a clear advantage over the current non-selective channelrodopsin-based optogenetic systems and the authors use this as a central justification for developing methods that would directly elicit Ca2+ influx instead of relying on membrane depolarization (in the channelrodopsin-based optogenetic systems) to activate endogenous Ca2+ channels. The study develops a protein construct with LOV2 (a photoswitch that responds to blue-light) fused to a STIM1 C-terminal fragment. Using a HEK293 cell line that stably expresses Orai1 transfected with their chimeric construct, they demonstrate tight control of Ca2+ influx using blue light. They also showed that NFAT-translocation, which is a downstream effect of CRAC channel activation, correlates with the frequency of the blue light-mediated Ca2+ pulses. In addition, the study pairs the opto construct with lanthanide-doped up conversion nanoparticles (UCNP) that absorb in the near-infrared wavelengths and emit blue light. This allowed control Ca2+ influx and NFAT-translocation in cells using near-infrared light, which is necessary in developing a system that can penetrate tissues in an in vivo system. Finally, as a proof-of-concept experiment, HeLa cells expressing the Opto-CRAC system are grafted subcutaneously into the flanks of mice and the manuscript demonstrates changes in NFAT-luciferase expression using near-infrared light in these cells under the skin. A light activated Ca2+ channel could be tremendously useful for applications ranging from studies of basic biology of CRAC channels, local activation of CRAC channels in microdomains within cells, and in vivo interrogation of immune and other cells.

Essential revisions:

While there is considerable enthusiasm for the successful development of Opto-CRAC as a tool, particularly for use in non-excitable cells, the reviewers feel that there remains much to be done to eliminate current problems that make it unfeasible. While we recognize that this is essentially a proof of concept paper for a new technique, we feel that the following issues must be adequately addressed if the paper is to be accepted for publication.

1) In the current form, the system's limitations are substantial, even at this proof-of-concept stage. Optogenetic stimulation offers two key advantages: the requirement for a single protein and rapid kinetics. On the other hand, channelrhodopsin use is somewhat constrained by the need for blue light, which necessitates optical fiber implantation and hinders concurrent functional imaging, by its rapid inactivation, and by its limited single channel conductance. While Opto-CRAC offers significant advantages in being more calcium selective than channelrhodopsin based methods, It functions on the order of seconds to minutes, far slower than channelrhodopsin, limiting its usefulness to slower signaling processes, like many of those occurring in non-excitable cells. Although only a single protein is required for visible light stimulation, the resulting conductances are low, as judged by dynamic ranges of the employed genetically-encoded calcium indicators. In fact, it seems that the conductances are smaller than those produced by channelrhodopsin despite much longer stimulus duration. This may be due to the reliance on native ORAI channels – unlike many existing stimulation methods, where the heterologous activator is in excess, endogenous channels limit maximal conductance and make that conductance highly cell type-dependent. Moreover, induction of gene expression is predicated on concurrent treatment of cells with phorbol ester, a potent carcinogen. For these reasons, Opto-CRAC is far from being useful in animal studies.

2) However, the authors promote Opto-CRAC as a non-invasive NIR deep tissue cellular stimulator of non-excitable cells. Their assertion that no tools exist for this purpose is inaccurate, since multiple visible light-independent methods, including DREADDs, have proven quite effective outside the brain. For NIR use in culture, the authors assemble a far more elaborate system than described for visible light, consisting of engineered STIM and ORAI proteins, streptavidin-coated UCNP beads and PMA (for gene induction). For in vivo use, they implant cells expressing the encoded components that have been pre-treated with beads subcutaneously, hardly a non-invasive procedure.

3) Critically, the properties of this four-part (and not genetic) NIR system are inadequately described: NIR-dependent calcium entry is shown (as a function of GCaMP fluorescence), but not measured; NFAT translocation to the nucleus is demonstrated, but no gene expression data is provided.

4) How does one reconcile the complexity and limited sensitivity of Opto-CRAC, including the requirement for UNCP beads, with its intended application to modulate calcium in cells of the immune and hematopoietic systems? Are stem cells propagated and pre-treated ex vivo to be injected into the bone marrow or thymus? Will NIR, which elevated reporter expression in subcutaneous cells, have any impact on those tissues? No feasibility testing is described.

5) The one area where UNCPs might have a real impact as NIR light transducers is for activating channelrhodopsin (in fact, the inability of ChR to be gated by long-wave light is given as an explicit motivation for UNCP development). Injected locally and recruited to genetically targeted cells that express channelrhodopsin, UNCP could enable NIR ChR gating. Surprisingly, this potentially exciting application is not explored.

6) Is the relatively slow time scale due to properties of ORAI channels, rather than a limitation of the light induction by STIM1-LOV? If so, the comparison to channelrhodopsin should probably be tempered. At least some discussion, and perhaps some experiments should be included as to which protein is limiting (both in terms of maximal conductance and kinetics).

7) STIM1 has other targets besides Orai1 channels including other Orai isoforms, voltage-activated Ca2+ channels (which it inhibits), and even TRP channels. How the optically responsive STIM1 (LOVSoc) fits into this larger framework of potential targets is unclear. Since other channels may be engaged by STIMs, the authors should examine calcium selectivity by testing for other ions in cells that have additional endogenous channels, as opposed to using fibroblasts stably expressing ORAIs.

8) The vector size appears small enough for viral gene delivery, but it is unclear how UCNPs can be delivered. In addition, if the UCNPs binds to off-targets, that could wreak havoc with the high-energy blue light in the body.

9) Regarding the UNCPs: the conversion here is from low energy to high, which could be highly inefficient. Energies of excitation and emission at different wavelengths should be included.
