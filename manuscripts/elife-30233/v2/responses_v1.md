# Author response - Round 1

Authors:
- Min Woo Kim ([ORCID: 0000-0003-1327-3617](https://orcid.org/0000-0003-1327-3617))
- Wenjing Wang ([ORCID: 0000-0001-6025-9848](https://orcid.org/0000-0001-6025-9848))
- Mateo I Sanchez ([ORCID: 0000-0003-1359-6969](https://orcid.org/0000-0003-1359-6969))
- Robert Coukos ([ORCID: 0000-0002-7307-8293](https://orcid.org/0000-0002-7307-8293))
- Mark von Zastrow ([ORCID: 0000-0003-1375-6926](https://orcid.org/0000-0003-1375-6926))
- Alice Y Ting ([ORCID: 0000-0002-8277-5226](https://orcid.org/0000-0002-8277-5226))

## Response text

DOI: [10.7554/eLife.30233.015](https://doi.org/10.7554/eLife.30233.015)

Essential revisions:

1) Unfortunately, there is no quantification of experiments describing non membrane protein interactions, only low-resolution images of cell culture. Figure 2 shows that the efficacy of the approach varies widely depending on the specific protein-protein interaction being studied. A quantification of results from these protein-protein interactions (non-GPCR-arrestin) is required.

We now have quantification of all PPIs shown in Figure 2:

· DRD1-Arrestin PPI quantification (luciferase readout) shown in Figure 2D;

· NMDR-Arrestin PPI quantification (luciferase readout) shown in Figure 2D;

· EGFR-Grb2 PPI quantification (Citrine readout) given in the legend of Figure 2B;

· FRB-FKBP PPI quantification (luciferase readout) shown in Figure 2—figure supplement 1;

· Mito-FRB/FKBP PPI quantification (luciferase readout) shown in Figure 2—figure supplement 1;

· CIBN-CRY2PHR PPI quantification (luciferase readout) shown in Figure 2—figure supplement 1.

2) The method proposed is conceptually very similar to three systems published earlier this year:

Cal-Light:https://www.ncbi.nlm.nih.gov/pubmed/28650460

FLARE:https://www.ncbi.nlm.nih.gov/pubmed/28650461iTango:https://www.ncbi.nlm.nih.gov/pubmed/28369042

Despite the similarities with previously reported systems, there is no mention of these in the Introduction of this manuscript, where comparisons are drawn between TIGER and other molecular approaches for monitoring protein-protein interactions. These other techniques should be mentioned in the Introduction and similarities and differences to these systems should be discussed.

Our Introduction and Abstract both mention Tango, which is highly relevant to SPARK (the new name for our tool, changed from TIGER) as it is also a transcriptional PPI tool. We now explicitly mention FLARE and what it is for, as soon as we begin to discuss the design of our SPARK tool, because that is the way that FLARE is relevant – in its design, but not in its purpose (its purpose is to sense calcium, not PPIs). iTango was published as a dopamine sensing tool, not a PPI detection methodology, and therefore we do not believe it is appropriate to mention it in our Introduction of PPI methods. Later in the manuscript, we have an entire section on iTango and a side by side comparison to SPARK (because we extrapolate that iTango could be used for PPI detection, even though the previous study did not demonstrate it). Cal-Light is even less relevant, as it is not for PPIs, and its design is different from that of SPARK and FLARE; nevertheless we do cite Cal-Light when we discuss LOV domain optimization.
