# Author response - Round 1

Authors:
- Neel H Shah
- Qi Wang
- Qingrong Yan
- Deepti Karandur
- Theresa A Kadlecek
- Ian R Fallahee
- William P Russ
- Rama Ranganathan
- Arthur Weiss ([ORCID: 0000-0002-2414-9024](https://orcid.org/0000-0002-2414-9024))
- John Kuriyan ([ORCID: 0000-0002-4414-5477](https://orcid.org/0000-0002-4414-5477))

## Response text

DOI: [10.7554/eLife.20105.045](https://doi.org/10.7554/eLife.20105.045)

[…] Essential revisions:

The plotting of peptide kinetics vs. bacterial display preferences in Figure 5B is odd in that the kinase kinetics is presented in a linear scale and the bacterial display data on a log scale. It is not clear what the physical basis for this is. In linear free energy correlations, it is customary to use a log-log plot. For that matter, it seems surprising that the kinetic effects with kinase assays and peptides seem much smaller than the bacterial display selectivity effects. Perhaps the authors could comment on this.

The reviewers make a good point about the kinetic data being displayed on a linear scale and the enrichment values being displayed on a logarithmic scale. We have converted our graph in Figure 5B to a log-log plot. Indeed, the correlation between in vitro phosphorylation rates and enrichment values from our screen fits better to a line when both variables are log-transformed.

The difference in the magnitudes of the kinetic effects and the bacterial display selectivity effects (the slope of the line in Figure 5B) is somewhat arbitrary, and it will be dependent on the screen. For example, the mutants shown in Figure 5B span a range of -1 to 1 in log10(enrichment), and this corresponds to a 2- to 3-fold change in phosphorylation rate. This reflects the fact that the wild-type peptide, surrounding LAT Tyr 226, is a good substrate for ZAP-70, and thus individual substitutions only have a modest, albeit measurable, effect. By contrast, for ZAP-70 phosphorylation of a poor substrate, the peptide encompassing LAT Tyr 132 (Figure 5D), substitutions at Gly 131 have a log10(enrichment) of roughly 1, but this can correspond to a 16-fold enhancement in phosphorylation rate (Figure 5—figure supplement 4). We consider the ability to accurately detect small effects from point mutants, even in the context of an optimal substrate, to be a strength of our specificity screening platform. We have modified the text, where the results of the screens are first introduced, to state this.

The authors point out that there have not been convincing structures reported that show how activation loop tyrosine kinase phosphorylations occur in trans. The reviewers are not aware of any examples either. However, in PMID: 19060208, Chen et al. make a good case that their crystal structure of the FGFR2 kinase domain captures trans-phosphorylation state of one kinase molecule phosphorylating the C-terminus of the other. The authors should probably cite this study and briefly describe the similarities/differences between their findings and that of the FGFR2 structural analysis of Chen et al.

We agree that Chen et al. make a compelling case that the structure reported in their paper captures a trans-phosphorylation complex. We have analyzed that structure, which depicts C-terminal tail phosphorylation, along with other proposed trans-autophosphorylation structures that may be relevant to activation loop phosphorylation. During our analysis, we also looked at serine/threonine kinase trans-autophosphorylation complexes, as suggested in another reviewers’ comment. To reflect these considerations, we have modified our section entitled “A model for tyrosine kinase activation loop phosphorylation” to contain a consolidated paragraph that cites all of the appropriate references, including Chen et al., and explains why we ultimately utilized PDB code 3LVP for our modeling of the Lck and c-Src autophosphorylation complexes.

Given the strong conclusion about long-range electrostatic steering as a critical aspect of the ZAP-70-LAT interaction, it would be interesting to determine the effects of varied salt concentration on the kinase reactions. Presumably, the phosphorylation rate should increase at low salt and decrease at very high salt. This type of salt dependence of the induction phase in kinetic assays was exploited to the role of an electrostatic network in a previous study (Ozkirimli et al. Protein Sci. 2008 Nov;17(11):1871-80). We recognize, however, that the authors have already included an extensive set of experiments in this manuscript. If they choose not to include additional measurements in this study, perhaps they could comment on this issue.

The reviewers make a valid point about salt-dependent phosphorylation. We have measured phosphorylation of a LAT-based sequence by ZAP-70 under varying salt concentrations, and these data are now included Figure 8—figure supplement 1. As expected, increasing the ionic strength of the reaction solution dramatically reduces the rate of LAT phosphorylation. The end of the section on Brownian dynamics and long-range electrostatics has been updated to reference these new data. The citation provided by the reviewer is interesting because it points to the importance of an electrostatic network in controlling the activity of Src kinases, such as Lck, and we now cite this work in the revised manuscript.
