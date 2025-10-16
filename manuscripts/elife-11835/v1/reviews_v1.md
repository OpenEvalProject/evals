# Peer review - Round 1

Editors:
- Jonathan A Cooper, Fred Hutchinson Cancer Research Center , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.11835.027](https://doi.org/10.7554/eLife.11835.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Time-resolved multimodal analysis of SH2 domain binding in EGF-stimulated cells" for consideration by eLife. Your article has been favorably evaluated by Tony Hunter as Senior Editor and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper is a very interesting and comprehensive study of the interaction of different phosphotyrosine-binding SH2 domains to proteins that are phosphorylated in response to EGF in A431 cells. The combination of in vitro and in vivo approaches for following binding kinetics is a particular strength. The results show that different assays provide different and complementary results, and provide both a resource and a caution for other investigators. In this regard the paper makes an important and scholarly contribution. However, all reviewers were concerned that there was significant speculation and few answers as to why the different approaches yield different kinetics, and furthermore that some of the discrepancies may result from your use of cells that have extremely high receptor levels. It will be important to provide some data from more normal cells, that have a physiological response to EGF, or with a lower concentration of EGF in A431 cells, before the paper can be accepted.

Required revisions:

1) EGF binding and receptor occupancy should be measured over the time course and EGF concentration used in the paper. The results should be integrated into explanation of the kinetics of phosphorylation site kinetics and SH2 binding in vitro and in vivo. Appropriate discussion of the effects of receptor number and occupancy on the assays should be added.

2) Key experiments should be repeated in a cell line where EGF is mitogenic, or in A431 cells at a lower EGF concentration. The EGF concentration used in your experiments is reportedly growth inhibitory for A431 cells (Lifshitz et al. J Cell Physiol 115:235, 1983). It is important to test whether the discrepancies between different assays are also observed under mitogenic conditions.

3) Far Westerns should be probed with univalent SH2 domains, to test whether the different kinetics obtained with this method are due to avidity effects of the multivalent SH2 probes used.

4) The discussion of the effects of receptor clustering needs to incorporate the extensive literature on diffusion limited ligand binding, particularly with regard to the effects on on-rate of SH2 binding.

The full reviews now follow, and are included to help you understand the reasoning behind the required revisions.

Reviewer #1:

The authors have used iTRAQ MS, far Western blotting with purified SH2 domains, and single molecule imaging of SH2 domain-tdEOS fusion protein recruitment to the membrane, to monitor the kinetics of tyrosine phosphorylation events in A431 cells following EGF treatment. Each approach gives complementary results, with surprisingly different response kinetics. The authors discuss the limitations of each method and how together they help build a picture of the cellular response. The new findings include a transient dip in most MS detected sites 2-10 min after EGF. This may be due to recruitment of SH2-containing phosphatases. They also found discrepancies between the phosphorylation of individual sites detected by MS versus phospho antibodies. Perhaps most notably, SH2 binding sites, detected by Far Western, are apparently created more rapidly than SH2-tdEos fusions are recruited to the membrane. The latter may be limited by the time taken to form receptor clusters in the membrane.

The results are interesting in light of the many previous studies of EGF-stimulated tyrosine phosphorylation events. The paper may be a valuable resource for other investigators using this system. However, there are some major issues that weaken the results and lower the significance.

1) The authors used A431 cells, which have a hyper-abundance of EGFRs and are growth inhibited (not stimulated) at the EGF concentration used. This allowed them to follow more phosphorylation events but is of doubtful significance for cells that respond positively to EGF.

2) The responses detected by Far Western blotting were more rapid and had higher dynamic range than those detected by MS, and are faster than SH2-tdEos recruitment in vivo. This may in part be due to the use of clustered SH2 domains to probe the blots (GST-SH2, anti-GST-HRP and GSH-HRP), which will increase avidity and likely cause marked non-linearity in binding, amplifying the signal. Controls with monovalent SH2 domains should be done. The phosphoprotein targets are of course also denatured. It might be more informative to follow association of the endogenous full length proteins by conventional co-IP.

3) The membrane recruitment of fluorescent SH2 domains in vivo was analyzed both by conventional TIRF, providing on- and off-kinetics for net membrane association, and by single molecule PALM, allowing measurement of the number of molecules binding and releasing per unit time, cluster size and diffusion in the plane of the membrane (related to clustering). Based on this they conclude that SH2 domains only bind stably to clustered receptors (due to rebinding and hence low off rate), and that the slow formation of clusters slows down membrane association. This principle was already investigated in the authors' nice PNAS paper (Oh et al. 2012). However, the results don't exclude the possibility that the on-rate to EGFR clusters may also be low. Since EGFR clustering leaves more EGFR-free membrane area, a decrease in on-rate is not unreasonable. It may be possible to measure on-rate to a cluster by photo-converting a cluster and looking at new molecule binding.

Reviewer #2:

This is a very interesting and comprehensive study of the interaction of different phosphotyrosine-binding SH2 domains to proteins phosphorylated in response to EGF addition to A431 cells. The paper is technically excellent and is very well written. I had no trouble following the logic of both the experiments and the interpretations. The strengths of the paper include its use of multiple technical approaches to follow both protein phosphorylation and the dynamic interaction of different SH2 domains to their targets, its comprehensive nature and the excellent data sets included with this study (Table 1 makes the entire study worthwhile, in my opinion). The combination of in vitro and in vivo approaches for following binding kinetics is a particular strength.

Where this paper falls short is in placing their results into the context of what is already known and in understanding the consequences of using A431 cells, which have enormous numbers of EGFR.

Their basic conclusion is that clustering of the EGFR affects the ability of SH2-domain proteins to bind and dissociate from the membrane. If the receptors are diffusely distributed, binding is fast. If they are clustered, it is delayed. The reverse rate is also slower if the receptors are clustered. Both of these effects of high receptor density or clustering can be due to diffusion-limited binding, which has been well studied since the seminal work of Berg and Purcell over 35 years ago (Biophy J., 20:193-219, 1977). Although previous studies on the effect of high receptor density and clustering have focused on ligands, binding of SH2-domains should be similar. Indeed, those studies have described the same sort of effects that are described here (e.g., Potanin et al., [1994] Eur Biophys J 23, 197; Lagerholm and Thompson [1998] Biophys J 74, 1215; Gopalakrishnan et al., [2005] Biophys J 89, 3686). For example, although the "apparent binding rates" of SH2-domain proteins to clustered receptors are reduced relative to unclustered receptors, this is because clustered sites compete with each other for binding to diffusing ligands. Dissociation rates look slower because of rebinding effects, and so forth. Diffusion-limited binding of EGF has even been explored in A431 cells because of their extraordinary number of EGFR (see Wiley [1988] J Cell Biol 107, 801). I am not suggesting that these previous studies make the findings presented here superfluous, but they have direct relevance for interpreting their results, especially the effect of clustered density versus total receptor density and the effect of time-dependent receptor occupancy versus time-dependent SH2-domain protein binding. For example, because of diffusion-limited binding of EGF to A431 cells, total receptor occupancy will climb continuously over time rather than rapidly reaching equilibrium (see Figure 2 of Wiley [1988]). This looks very similar to the continuous increase in specific EGFR phosphorylation over time in Figure 3. The "oscillation" they report in the tyrosine phosphorylation levels after stimulation with EGF is thus likely due to a rapid desensitization of the initially activated receptors followed by a slow accumulation of additionally occupied receptors.

Because of diffusion-limited binding, there are three processes they must untangle: 1) the effect of a continuously increasing number of occupied EGFR over time, 2) the time-dependent change in the overall density of activated receptors at the cell surface and its effect on receptor clustering, and 3) the density of receptors in the clusters. All three of these processes will be dependent on the levels of occupied receptors, which unfortunately, were not examined in this paper. Without knowing this information, it is difficult to know whether the types of effects seen here (e.g. Figure 5) are also present in cells lacking EGFR amplification. It’s not necessarily a bad thing if these effects are only seen in EGFR-amplified cells, but this knowledge would certainly help the reader know how widely their results can be extrapolated to other systems. I would suggest that they quantify the time-dependent change in EGFR occupancy in their cells using fluorescently-labeled EGF (available commercially) and show that the range of receptor occupancy they are observing is within the range of other cells. Alternately, they could show that doses of EGF that result in lower levels of net occupancy produce similar results. At the very least, they need to incorporate the previous literature on diffusion-limited binding processes in their Discussion.

Reviewer #3:

Jadwin et al. present a comprehensive analysis of EGF-stimulated phosphorylation and associated SH2/PTB interaction datasets, and was a pleasure to read. The model cell system is the cancer-derived cell line A431, which is known to express high level wild type EGFR (>1-million per cell). The authors are experienced and credible in the field, and in this instance sought to address outstanding questions related to SH2/PTB-mediated signaling downstream of activated EGFR, but generally relevant to tyrosine kinase signaling. Far western analysis showed positively correlated kinetics of binding of a set of domains to proteins known to be tyrosine phosphorylated in response to EGFR activation. These data are complemented by MS-based analysis of individual phospho-peptides, and by measurement of membrane recruitment of ectopically expressed domains. Overall, the authors present interesting data, and Table 1 stands out as an engaging, interactive tool. A main conclusion drawn is that the integration of orthogonal datasets is an effective approach to reveal discrepancies that may relate to technical limitations or possibly biological mechanisms.

In some instances the presentation and discussion of data lack clarity, and there is considerable speculation based on technical phenomenology.

1) The coverage of EGFR phosphorylation sites, central to the study, was not as exhaustive as many published reports, and was not clearly acknowledged/presented or discussed. For example, they describe five different EGFR phosphopeptides, but three are phospho-isomers that contain pY1045. A peptide singularly phosphorylated at the primary GRB2 SH2 site pY1068 was not part of the data, which compromises the interpretation of results and discussions about GRB2.

2) Obviously FW and MS analyses, by technical design, measure different features, but the assumptions associated with these methods should be more thoroughly addressed.

3) Some conclusion statements reiterate consensus views, and hence would be appropriate for the Introduction. Examples include:

"…suggests that the concentration of SH2 domain binding sites can be as important as SH2 domain binding specificity…"

"…suggest that the stoichiometry of SH2 and PTB domain-containing effectors bound to EGFR is temporally regulated by differential phosphorylation/dephosphorylation of their specific binding sites…"

"…these data suggest that EGFR overexpression is associated with a significant expansion of its classical downstream signal transduction pathways"

4) What are the estimated concentrations of ectopic domains versus endogenous? For example, is competition between ectopic GRB2 SH2 with endogenous GRB2, which is reportedly highly expressed (approx. 500K/Hela cell), factored into the calculations and data interpretation?

5) The interpretation that the pervanadate effect is due to a lack of clustering is speculative. What is the (enhanced) stoichiometry/level of phosphorylation in response to pervanadate compared with EGF?
