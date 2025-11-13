# SARS-CoV-2 strategically mimics proteolytic activation of human ENaC

## Authors

- Praveen Anand<sup>1</sup> ([ORCID: 0000-0002-2478-7042](https://orcid.org/0000-0002-2478-7042))
- Arjun Puranik<sup>2</sup>
- Murali Aravamudan<sup>2</sup>
- AJ Venkatakrishnan<sup>2</sup> ([ORCID: 0000-0003-2819-3214](https://orcid.org/0000-0003-2819-3214)) †
- Venky Soundararajan<sup>2</sup> ([ORCID: 0000-0001-7434-9211](https://orcid.org/0000-0001-7434-9211)) †

### Affiliations

1. nference Labs Bengaluru India
2. nference, Inc Cambridge United States

† Corresponding author

## Abstract

Molecular mimicry is an evolutionary strategy adopted by viruses to exploit the host cellular machinery. We report that SARS-CoV-2 has evolved a unique S1/S2 cleavage site, absent in any previous coronavirus sequenced, resulting in the striking mimicry of an identical FURIN-cleavable peptide on the human epithelial sodium channel α-subunit (ENaC-α). Genetic alteration of ENaC-α causes aldosterone dysregulation in patients, highlighting that the FURIN site is critical for activation of ENaC. Single cell RNA-seq from 66 studies shows significant overlap between expression of ENaC-α and the viral receptor ACE2 in cell types linked to the cardiovascular-renal-pulmonary pathophysiology of COVID-19. Triangulating this cellular characterization with cleavage signatures of 178 proteases highlights proteolytic degeneracy wired into the SARS-CoV-2 lifecycle. Evolution of SARS-CoV-2 into a global pandemic may be driven in part by its targeted mimicry of ENaC-α, a protein critical for the homeostasis of airway surface liquid, whose misregulation is associated with respiratory conditions.

## Introduction

The surface of SARS-CoV-2 virions is coated with the spike (S) glycoprotein, whose proteolysis is key to the infection lifecycle. After the initial interaction of the S-protein with the ACE2 receptor (Walls et al., 2020), host cell entry is mediated by two key proteolytic steps. The S1 subunit of the S-protein engages ACE2, and viral entry into the host cell is facilitated by proteases that catalyze S1/S2 cleavage (Belouzard et al., 2012; Belouzard et al., 2009) at Arginine-667/Serine-668 (Figure 1a). This is followed by S2’ site cleavage that is required for fusion of viral-host cell membranes (Hoffmann et al., 2020; Walls et al., 2020).

![Figure 1.](https://cdn.elifesciences.org/articles/58603/elife-58603-fig1-v2.jpg)

**Figure 1.:** (a) The cartoon representation of the S-protein homotrimer from SARS-CoV-2 is shown (PDB ID: 6VSB). One of the monomers is highlighted in red. The alignment of the S1/S2 cleavage site required for the activation of SARS-CoV-2, SARS-CoV, Pangolin-CoV, and Bat-CoV RaTG13 are shown. The four amino acid insertion evolved by SARS-CoV-2, along with the abutting cleavage site is shown in a box. (b) The cartoon representation of human ENaC protein is depicted (PDB ID: 6BQN; chain in green), highlighting the ENaC-ɑ chain in green. The alignment on the right captures FURIN cleavage at the S1/S2 site of SARS-CoV-2, along with its striking molecular mimicry of the identical peptide from human ENaC-ɑ protein (dotted loop in the cartoon rendering of human ENaC). The alignment further shows the equivalent 8-mer peptide of mouse ENaC-ɑ that is also known to be cleaved by FURIN. One of the known genetic alterations on human ENaC-ɑ is highlighted as well (Welzel et al., 2013). (c) The single cell transcriptomic co-expression of ACE2, ENaC-ɑ, and FURIN is summarized. The heatmap depicts the mean relative expression of each gene across the identified cell populations. The human and mouse single cell RNA-seq are visualized independently. The cell types are ranked based on decreasing expression of ACE2. The box highlights the ACE2 positive cell types in human and mouse samples.

## Results

We hypothesized that the virus may mimic host substrates to achieve proteolysis. Comparing human-infecting SARS-CoV-2 with SARS-CoV strains, as well as with candidates of zoonotic origin (Pangolin-CoV and Bat-CoV RaTG13), shows that SARS-CoV-2 has evolved a unique sequence insertion at the S1/S2 site (Zhang et al., 2020; Figure 1a). Although the S protein of SARS-CoV-2 shares high sequence identity with the S proteins of Pangolin-CoV (92%) and Bat-CoV RaTG13 (97%), the furin insertion site seems to be uniquely acquired by SARS-CoV-2. The resulting tribasic 8-mer peptide (RRARSVAS) on the SARS-CoV-2 S1/S2 site is conserved among 10,956 of 10,967 circulating strains deposited at GISAID (https://www.gisaid.org/) (Elbe and Buckland-Merrett, 2017), as of April 28, 2020 (Supplementary file 1a). This peptide is also absent in over 13,000 non-COVID-19 coronavirus S-proteins from the VIPR database (Carrillo-Tripp et al., 2009). Strikingly, examining over 10 million peptides (8-mers) of 20,350 canonical human proteins from UniProtKB shows that the peptide of interest (RRARSVAS) is present exclusively in human ENaC-ɑ, also known as SCNN1A (p-value=4E-4) (see Materials and methods). The location of this SARS-CoV-2 mimicked peptide in the ENaC-ɑ structure is in the extracellular domain (Noreng et al., 2018; Figure 1b). This suggests that the SARS-CoV-2 may have specifically evolved to mimic a human protease substrate.

ENaC regulates sodium ion (Na+) and water homeostasis, and ENaC’s expression levels are controlled by aldosterone and the associated Renin-Angiotensin-Aldosterone System (RAAS)6. In distal lung airways, ENaC is known to play a key role in controlling fluid reabsorption at the air–liquid interface (Rossier and Stutts, 2009), and similar to SARS-CoV2, ENaC-ɑ also needs to be proteolytically activated for its function (Vallet et al., 1997). FURIN cleaves the equivalent peptide on mouse ENaC-ɑ between the Arginine and Serine residues in the 4th and 5th positions respectively (RSAR|SASS) (Hughey et al., 2004a; Hughey et al., 2004b), akin to the recent report establishing FURIN cleavage at the S1/S2 site of SARS-CoV-2 (Walls et al., 2020; Figure 1b). It is conceivable that human ENaC activation may be compromised in SARS-CoV-2 infected cells, for instance by SARS-CoV-2 exploiting host FURIN for its own activation. The likely consequence would be low ENaC activity on the surface of the airways leading to compromised fluid reabsorption (Planès et al., 2010; Yurdakök, 2010), an important lung pathology in COVID-19 patients with acute respiratory distress syndrome (ARDS). Indeed, the exact mechanism of SARS-CoV-2’s potential impact of ENaC activation needs to be investigated.

Although the furin-like cleavage motifs can be found in other viruses (Coutard et al., 2020), the exact mimicry of human ENaC-ɑ cleavage site raises the specter that SARS-CoV-2 may be hijacking the protease network of ENaC-ɑ for viral activation. We asked whether there is an overlap between putative SARS-CoV-2 infecting cells and ENaC-ɑ expressing cells. Systematic single cell expression profiling of the ACE2 receptor and ENaC-ɑ was performed across human and mouse samples comprising ~1.3 million cells (Venkatakrishnan et al., 2020; Figure 1c). Interestingly, ENaC-ɑ is expressed in the nasal epithelial cells, type II alveolar cells of the lungs, tongue keratinocytes, and colon enterocytes (Figure 1c and Figure 2—figure supplements 1–6), which are all implicated in COVID-19 pathophysiology (Shweta et al., 2020; Venkatakrishnan et al., 2020). Further, ACE2 and ENaC-ɑ are known to be expressed generally in the apical membranes of polarized epithelial cells (Butterworth, 2010; Musante et al., 2019). The overlap of the cell-types expressing ACE2 and ENaC-ɑ, and similar spatial distributions at the apical surfaces, suggest that SARS-CoV-2 may be leveraging the protease network responsible for ENaC cleavage.

Beyond FURIN, which cleaves the S1/S2 site (Walls et al., 2020), we were intrigued by the possibility of other host proteases also being exploited by SARS-CoV-2. We created a 160-dimensional vector space (20 amino acids x eight positions on the peptide) for assessment of cleavage similarities between the 178 human proteases with biochemical validation from the MEROPS database (see Materials and methods; 0 < protease similarity metric <1) (Rawlings et al., 2018). This shows that FURIN (PCSK3) has overall proteolytic similarity to select PCSK family members, specifically PCSK5 (0.99), PCSK7 (0.99), PCSK6 (0.99), PCSK4 (0.98), and PCSK2 (0.94) (Supplementary file 1b). It is also known that the protease PLG cleaves the ɣ-subunit of ENaC (ENaC-ɣ)(Passero et al., 2008).

In order to extrapolate the tissue tropism of SARS-CoV-2 from the lens of the host proteolytic network, we assessed the co-expression of these proteases concomitant with the viral receptor ACE2 and ENaC-ɑ (Figure 2). This analysis shows that FURIN is expressed with ACE2 and ENaC-ɑ in the colon (immature enterocytes, transit amplifying cells) and pancreas (ductal cells, acinar cells) of human tissues, as well as tongue (keratinocytes) of mouse tissues. PCSK5 and PCSK7 are broadly expressed across multiple cell types with ACE2 and ENaC-ɑ, making it a plausible broad-spectrum protease that may cleave the S1/S2 site. In humans, concomitant with ACE2 and ENaC-ɑ, PCSK6 appears to be expressed in cells from the intestines, pancreas, and lungs, whereas PCSK2 is noted to be co-expressed in the pancreas (Figure 2). It is worth noting that the extracellular proteases need not necessarily be expressed in the same cells as ACE2 and ENaC-ɑ. Among the PCSK family members with the potential to cleave the mimicked 8-mer peptide, it is intriguing that the same tissue can house multiple proteases and also that multiple tissues do share the same set of proteases.

![Figure 2.](https://cdn.elifesciences.org/articles/58603/elife-58603-fig2-v2.jpg)

**Figure 2.:** The heatmap depicts the relative expression of ACE2 and ENaC-ɑ along with a list of proteases that can potentially cleave the S1/S2 site. The relative expression levels are denoted on a scale of blue (low) to red (high). The rows denote proteases and columns denote cell-types.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/58603/elife-58603-fig2-figsupp1-v2.jpg)

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/58603/elife-58603-fig2-figsupp2-v2.jpg)

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/58603/elife-58603-fig2-figsupp3-v2.jpg)

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/58603/elife-58603-fig2-figsupp4-v2.jpg)

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/58603/elife-58603-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** Although only 2.77% of the proximal tubule cells had detectable expression of SCNN1A, a higher percentage (8.46%) of these cells were also observed to express ACE2 (Primary data processed from Pubmed ID: 31604275 and hosted on https://academia.nferx.com/).

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/58603/elife-58603-fig2-figsupp6-v2.jpg)

## Discussion

Our findings emphasize that redundancy may be wired into the mechanisms of host proteolytic activation of SARS-CoV-2. This study should stimulate the design of experiments that confirm the working hypothesis generated by our unbiased and systematic computational analysis. The mimicry of a cleavable host peptide central to pulmonary, renal, and cardiovascular function provides a new perspective to the evolution of SARS-CoV-2 in causing a global coronavirus pandemic.

## Materials and methods

### Alignment of coronavirus spike proteins

The complete S-protein sequence for SARS-CoV (Uniprot ID: P59594) and SARS-CoV-2 was obtained from uniprot (ftp://ftp.uniprot.org/pub/databases/uniprot/pre_release/). The sequences of Pangolin-CoV and Bat-CoV RaTG13 were obtained from the VIPR database (https://www.viprbrc.org/). Sequence alignments using Clustal-W, and comparison of SARS-CoV-2 versus other coronavirus strains were performed using JalView17.

### Analysis of 8-mers of the human proteome

We enumerated 10,257,893 (10.26M) 8-mers from 20,350 reviewed uniprot reference sequences from human proteome (Proteome ID: UP000005640, as accessed on May 4th 2020). The previously identified SARS-CoV-2 8-mer ‘RRARSVAS’ was in fact found in ENaC-ɑ protein (Uniprot ID: P37088; p-value ≈ 10.26M/208 = 4E-4; chance of finding that particular 8-mer anywhere in the reference sequences).

### Calculating the cosine similarity metric for protease cleavage site

The position frequency matrix (PFM) of the individual proteases obtained from the MEROPS database (Rawlings et al., 2018) was converted to a probability weight matrix (PWM) (normalized and scaled) (Supplementary file 1b). Out of 178 proteases, there were 146 proteases that had specificity information available on the eight mer peptide spanning the cleavage site (±4). The 20 (amino acids) x 8 (position) matrix defined for each of the proteases were flattened into a single vector with 160 elements. We performed a cosine similarity calculation between all pairs (X,Y) of protease specificity vector. The similarity was derived as the normalized dot product of X and Y: K(X, Y) = <X, Y> / (||X||*||Y||)).

### Overlap of cell types expressing ENaC-ɑ, ACE2, and proteases from scRNA-seq datasets

We performed a systematic expression profiling of the ACE2 and ENaC-ɑ across 65 published human and mouse single-cell studies comprising ~1.3 million cells using nferX Single Cell platform (Supplementary file 1c, https://academia.nferx.com/) (Venkatakrishnan et al., 2020). The ACE2 expression could be detected in 66 studies (59 studies of human samples and 7 studies of mouse samples) spanning across ~50 tissues, over 450 cell-types and ~1.05 million cells. In order to call a given cell-type to be positive for both ACE2 and a protease we applied a cutoff of 1% of the cells in the total cell-type cluster population to have a non-zero count associated with both ACE2 and the respective protease. The mean expression of the proteases, ENaC-ɑ and ACE2 was derived for individual cell population within each of the studies. The cell-type information was obtained from the author annotations provided for each of the studies. The analysis was performed separately on the mouse and human datasets. For each protease, the mean expression of given cell-population (mean log[cp10k +1] counts) was Z-score normalized (to ensure the sd = 1 and mean ~0 for all the genes) to obtain relative expression profiles across all the samples. The same normalization was applied to ACE2 and ENaC-ɑ and both human and mouse datasets were analyzed independently by generating heatmaps. The cell types having zero-expression values of ACE2 were also included as negative control to probe the expression of various proteases.

We performed an analysis to identify the cell types with significant overlap of ACE2 and ENaC-ɑ expression. To this end, we shortlisted cell types in which ENaC-ɑ is expressed in a significantly higher proportion of ACE2-expressing cells than in the overall population of cells of that sub-type. We computed the ratios of these proportions, and used a corresponding Fisher exact test to compute significance.
