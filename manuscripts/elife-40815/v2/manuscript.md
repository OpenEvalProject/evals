# Individual long non-coding RNAs have no overt functions in zebrafish embryogenesis, viability and fertility

## Authors

- Mehdi Goudarzi<sup>1</sup> ([ORCID: 0000-0001-6669-5800](https://orcid.org/0000-0001-6669-5800)) †
- Kathryn Berg<sup>1</sup>
- Lindsey M Pieper<sup>1</sup>
- Alexander F Schier<sup>1</sup> ([ORCID: 0000-0001-7645-5325](https://orcid.org/0000-0001-7645-5325)) †

### Affiliations

1. Department of Molecular and Cellular Biology Harvard University Cambridge United States
2. Center for Brain Science Harvard University Cambridge United States
3. FAS Center for Systems Biology Harvard University Cambridge United States
4. Allen Discovery Center for Cell Lineage Tracing University of Washington Seattle United States
5. Biozentrum University of Basel Basel Switzerland

† Corresponding author

## Abstract

Hundreds of long non-coding RNAs (lncRNAs) have been identified as potential regulators of gene expression, but their functions remain largely unknown. To study the role of lncRNAs during vertebrate development, we selected 25 zebrafish lncRNAs based on their conservation, expression profile or proximity to developmental regulators, and used CRISPR-Cas9 to generate 32 deletion alleles. We observed altered transcription of neighboring genes in some mutants, but none of the lncRNAs were required for embryogenesis, viability or fertility. Even RNAs with previously proposed non-coding functions (cyrano and squint) and other conserved lncRNAs (gas5 and lnc-setd1ba) were dispensable. In one case (lnc-phox2bb), absence of putative DNA regulatory-elements, but not of the lncRNA transcript itself, resulted in abnormal development. LncRNAs might have redundant, subtle, or context-dependent roles, but extrapolation from our results suggests that the majority of individual zebrafish lncRNAs have no overt roles in embryogenesis, viability and fertility.

## Introduction

Long non-coding RNAs (lncRNAs) comprise a heterogeneous group of transcripts longer than 200 nucleotides that do not encode proteins. LncRNAs have been proposed to affect the expression of neighboring or distant genes by acting as signaling, guiding, sequestering or scaffolding molecules (St Laurent et al., 2015; Rinn and Chang, 2012; Nagalakshmi et al., 2008; Carninci et al., 2005; Kapranov et al., 2007). The functions of specific lcnRNAs in dosage compensation (xist (Brockdorff et al., 1991; Marahrens et al., 1997), tsix (Lee et al., 1999), jpx (Johnston et al., 2002)) and imprinting (Airn (Wutz et al., 1997; Latos et al., 2012), MEG3 (Miyoshi et al., 2000; Kobayashi et al., 2000), H19 (Bartolomei et al., 1991; Feil et al., 1994)) are well established, and mutant studies in mouse have suggested that fendrr, peril, mdget, linc-brn1b, linc-pint (Sauvageau et al., 2013), and upperhand (Anderson et al., 2016) are essential for normal development. However, other studies have questioned the developmental relevance of several mouse lncRNAs, including Hotair (Amândio et al., 2016), MIAT/Gumafu (Ip et al., 2016), Evx1-as (Bell et al., 2016), upperhand, braveheart and haunt (Han et al., 2018). In zebrafish, morpholinos targeting the evolutionarily conserved lncRNAs megamind (TUNA (Lin et al., 2014)) and cyrano resulted in embryonic defects (Ulitsky et al., 2011). However, a mutant study found no function for megamind and revealed that a megamind morpholino induced non-specific defects (Kok et al., 2015). These conflicting results have led to a controversy about the importance of lncRNAs for vertebrate development (Sauvageau et al., 2013), (Han et al., 2018). We therefore decided to mutate a group of selected zebrafish lncRNAs using CRISPR-Cas9, and assay their roles in embryogenesis, viability and fertility.

Transcriptomic studies of early embryonic development (Ulitsky et al., 2011; Pauli et al., 2012) and five adult tissues (Kaushik et al., 2013) have identified over 2000 lncRNAs in zebrafish (Dhiman et al., 2015), of which 727 have been confirmed as non-coding based on ribosome occupancy patterns (Chew et al., 2013). For our mutant analysis we selected 24 bona fide lncRNAs based on synteny (conserved relative position on at least one other vertebrate genome), sequence conservation, expression dynamics (expression levels, onset and pattern) and proximity to developmental regulatory genes (see Table 1). These criteria were chosen to increase the likelihood of potential functional requirements of the selected lncRNAs. In addition, we selected a protein-coding RNA with a proposed non-coding function (squint).

**Table 1.**
 Summary of lncRNA features and mutant phenotypes lncRNA names are shown in the first column.lncRNAs were named using the last four digits of their corresponding ENSEMBL Transcript ID or their chromosome number if no transcript ID was available (e.g. lnc-1200 is located on chromosome 12). The second column represents ribosomal occupancy pattern along the length of lncRNAs in comparison to the 5’UTR, coding and 3’UTR of typical protein-coding transcripts (Chew et al., 2013). The third column shows the transcript ID for the investigated lncRNA or its genomic coordinate in GRCz10. Column Four shows the deletion size. Fifth column represent the percentage decrease in the level of lncRNA in comparison to wild type from three biological replicates (qRT-PCR). The six and seven columns show the presence of embryonic phenotypes, viability and fertility (at least 15 adult pairs per allele) of homozygous mutant fish. Eighth and ninth column show the upstream and downstream neighboring genes in a 200 kb window centered around the lncRNA’s TSS. The last column provides the selection criteria for each lncRNA.


<table>
  <thead>
    <tr>
      <th rowspan="2">lncRNA mutant, deletion type</th>
      <th rowspan="2">Ribosome Profiling, class</th>
      <th rowspan="2">lncRNA transcript ID</th>
      <th rowspan="2">Deletion size</th>
      <th rowspan="2">Percent reduction</th>
      <th rowspan="2">Embryonic phenotype</th>
      <th rowspan="2">Viability and fertility</th>
      <th colspan="2">Neighboring genes</th>
      <th rowspan="2">Selection criteria</th>
    </tr>
    <tr>
      <th>Up 100 Kb</th>
      <th>Down 100 Kb</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>cyranoa171, TSS-del.</td>
      <td>Trailerlike</td>
      <td>ENSDART00000139872</td>
      <td>326 bp</td>
      <td>98%</td>
      <td>No</td>
      <td>Yes</td>
      <td>tmem39b</td>
      <td>oip5</td>
      <td>Syntenic and sequence conservation, Reported phenotype</td>
    </tr>
    <tr>
      <td>cyranoa172, gene del.</td>
      <td>Trailerlike</td>
      <td>ENSDART00000139872</td>
      <td>4374 bp</td>
      <td>94%</td>
      <td>No</td>
      <td>Yes</td>
      <td>tmem39b</td>
      <td>oip5</td>
      <td>Syntenic and sequence conservation, Reported phenotype</td>
    </tr>
    <tr>
      <td>gas5a173, TSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000156268</td>
      <td>296 bp</td>
      <td>100%</td>
      <td>No</td>
      <td>Yes</td>
      <td>osbpl9</td>
      <td>tor3a</td>
      <td>Syntenic conservation, well studied lncRNA, host of several snoRNA</td>
    </tr>
    <tr>
      <td>lnc-setd1baa174, gene del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000141500</td>
      <td>3137 bp</td>
      <td>100%</td>
      <td>No</td>
      <td>Yes</td>
      <td>setd1ba</td>
      <td>rhoF</td>
      <td>Syntenic and sequence conservation, Proximity to developmental regulatory genes</td>
    </tr>
    <tr>
      <td>squinta175, gene del.</td>
      <td>Coding</td>
      <td>ENSDART0 0000079692</td>
      <td>1032 bp</td>
      <td>95%</td>
      <td>No</td>
      <td>Yes</td>
      <td>htr1ab</td>
      <td>eif4ebp1</td>
      <td>Evolutionary conservation, Reported phenotype, putative cncRNA</td>
    </tr>
    <tr>
      <td>lnc-phox2bba176, TSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000158002</td>
      <td>652 bp</td>
      <td>99%</td>
      <td>No</td>
      <td>Yes</td>
      <td>smntl1</td>
      <td>phox2bb</td>
      <td>Syntenic conservation</td>
    </tr>
    <tr>
      <td>lnc-phox2bba177, gene del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000158002</td>
      <td>9361 bp</td>
      <td>87%</td>
      <td>Yes</td>
      <td>No</td>
      <td>smntl1</td>
      <td>phox2bb</td>
      <td>Syntenic conservation</td>
    </tr>
    <tr>
      <td>lnc-3852a178, TSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000153852</td>
      <td>447 bp</td>
      <td>100%</td>
      <td>No</td>
      <td>Yes</td>
      <td>lima1a</td>
      <td>hoxc1a</td>
      <td>Maternal expression, Proximity to developmental regulatory genes</td>
    </tr>
    <tr>
      <td>lnc-1562a179, TSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000131562</td>
      <td>409 bp</td>
      <td>90%</td>
      <td>No</td>
      <td>Yes</td>
      <td>*</td>
      <td>fgf10a</td>
      <td>Maternal expression, Proximity to developmental regulatory genes</td>
    </tr>
    <tr>
      <td>lnc-3982a180, TSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000153982</td>
      <td>352 bp</td>
      <td>97%</td>
      <td>No</td>
      <td>Yes</td>
      <td>*</td>
      <td>bmp2b</td>
      <td>Maternal expression, Proximity to developmental regulatory genes</td>
    </tr>
    <tr>
      <td>lnc-6269a181, TSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000156269</td>
      <td>535 bp</td>
      <td>99%</td>
      <td>No</td>
      <td>Yes</td>
      <td>tbx1</td>
      <td>*</td>
      <td>Maternal expression, Proximity to developmental regulatory genes</td>
    </tr>
    <tr>
      <td>lnc-2154a182, TSS-del.</td>
      <td>Trailerlike</td>
      <td>ENSDART00000132154</td>
      <td>546 bp</td>
      <td>100%</td>
      <td>No</td>
      <td>Yes</td>
      <td>rpz</td>
      <td>nr2f5</td>
      <td>Maternal expression, Proximity to developmental regulatory genes</td>
    </tr>
    <tr>
      <td>lnc-1200a183, TSS-del.</td>
      <td>Leaderlike</td>
      <td>Chr12:1708389-1925779:1</td>
      <td>590 bp</td>
      <td>95%</td>
      <td>No</td>
      <td>Yes</td>
      <td>*</td>
      <td>zip11</td>
      <td>Maternal expression, Longest selected lncRNA</td>
    </tr>
    <tr>
      <td>lnc-1200a184, gene del.</td>
      <td>Leaderlike</td>
      <td>Chr12:1708389-1925779:1</td>
      <td>203.8 kb</td>
      <td>84%</td>
      <td>No</td>
      <td>Yes</td>
      <td>*</td>
      <td>zip11</td>
      <td>Maternal expression, Longest selected lncRNA</td>
    </tr>
    <tr>
      <td>lnc-2646a185, TSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00 000152646</td>
      <td>240 bp</td>
      <td>97%</td>
      <td>No</td>
      <td>Yes</td>
      <td>*</td>
      <td>dkk1b</td>
      <td>Proximity to developmental regulatory genes</td>
    </tr>
    <tr>
      <td>lnc-4468a186, TSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000154468</td>
      <td>306 bp</td>
      <td>100%</td>
      <td>No</td>
      <td>Yes</td>
      <td>fam169ab</td>
      <td>lhx5</td>
      <td>Proximity to developmental regulatory genes, Low expression level</td>
    </tr>
    <tr>
      <td>lnc-0600a187, TSS-del.</td>
      <td>Trailerlike</td>
      <td>Chr6:59414652-59443141:1</td>
      <td>244 bp</td>
      <td>95%</td>
      <td>No</td>
      <td>Yes</td>
      <td>*</td>
      <td>gli1</td>
      <td>Proximity to developmental regulatory genes, Low expression level</td>
    </tr>
    <tr>
      <td>lnc-0900a188, TSS-del.</td>
      <td>Leaderlike</td>
      <td>Chr9:6684669-6691350:1</td>
      <td>377 bp</td>
      <td>83%</td>
      <td>No</td>
      <td>Yes</td>
      <td>pou3f3a</td>
      <td>*</td>
      <td>Syntenic conservation, Low expression level</td>
    </tr>
    <tr>
      <td>lnc-8507a189, mTSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000158507</td>
      <td>323 bp</td>
      <td>81%</td>
      <td>No</td>
      <td>Yes</td>
      <td>npvf</td>
      <td>hoxa1a</td>
      <td>Proximity to Hox genes, Maternal and Zygotic promoters</td>
    </tr>
    <tr>
      <td>lnc-8507a190, mzTSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000158507</td>
      <td>9773 bp</td>
      <td>95%</td>
      <td>No</td>
      <td>Yes</td>
      <td>npvf</td>
      <td>hoxa1a</td>
      <td>Proximity to Hox genes, Maternal and Zygotic promoters</td>
    </tr>
    <tr>
      <td>lnc-7620a191, TSS-del.</td>
      <td>Trailerlike</td>
      <td>ENSDART00000137620</td>
      <td>668 bp</td>
      <td>99%</td>
      <td>No</td>
      <td>Yes</td>
      <td>gal3st1b</td>
      <td>srsf9</td>
      <td>Syntenic and sequence conservation, Implicated in adult fish and mouse behavior. Bitetti, A., et al. (2018)</td>
    </tr>
    <tr>
      <td>lnc-1300a192, TSS-del.</td>
      <td>Leaderlike</td>
      <td>Chr13:4535992-4538275:1</td>
      <td>367 bp</td>
      <td>92%</td>
      <td>No</td>
      <td>Yes</td>
      <td>c1d</td>
      <td>pla2g12b</td>
      <td>Syntenic and sequence conservation, High expression level</td>
    </tr>
    <tr>
      <td>lnc-7118a193, TSS-del.</td>
      <td>Trailerlike</td>
      <td>ENSDART00000157118</td>
      <td>438 bp</td>
      <td>82%</td>
      <td>No</td>
      <td>Yes</td>
      <td>mrps9</td>
      <td>pou3f3b</td>
      <td>Syntenic conservation</td>
    </tr>
    <tr>
      <td>lnc-5888a194, TSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000155888</td>
      <td>606 bp</td>
      <td>96%</td>
      <td>No</td>
      <td>Yes</td>
      <td>glrx5</td>
      <td>zgc:100997</td>
      <td>Syntenic conservation, scaRNA13 host gene, shortest selected lncRNA</td>
    </tr>
    <tr>
      <td>lnc-6913a195, TSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000156913</td>
      <td>333 bp</td>
      <td>72%</td>
      <td>No</td>
      <td>Yes</td>
      <td>usp20</td>
      <td>ptges</td>
      <td>Proximity to developmental regulatory genes</td>
    </tr>
    <tr>
      <td>lnc-6913a196, gene del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000156913</td>
      <td>5568 bp</td>
      <td>93%</td>
      <td>No</td>
      <td>Yes</td>
      <td>usp20</td>
      <td>ptges</td>
      <td>Proximity to developmental regulatory genes</td>
    </tr>
    <tr>
      <td>lnc-1666a197, TSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000141666</td>
      <td>544 bp</td>
      <td>96%</td>
      <td>No</td>
      <td>Yes</td>
      <td>ptf1a</td>
      <td>*</td>
      <td>Proximity to developmental regulatory genes, Restricted late expression</td>
    </tr>
    <tr>
      <td>lnc-6490a198, TSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000146490</td>
      <td>607 bp</td>
      <td>99%</td>
      <td>No</td>
      <td>Yes</td>
      <td>nr2f2</td>
      <td>*</td>
      <td>Syntenic conservation, Restricted late expression</td>
    </tr>
    <tr>
      <td>lnc-6490a199, gene del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000146490</td>
      <td>8378 bp</td>
      <td>100%</td>
      <td>No</td>
      <td>Yes</td>
      <td>nr2f2</td>
      <td>*</td>
      <td>Syntenic conservation, Restricted late expression</td>
    </tr>
    <tr>
      <td>lnc-0464a200, TSS-del.</td>
      <td>Trailerlike</td>
      <td>ENSDART00000140464</td>
      <td>597 bp</td>
      <td>96%</td>
      <td>No</td>
      <td>Yes</td>
      <td>nr2f1a</td>
      <td>*</td>
      <td>Restricted late expression pattern</td>
    </tr>
    <tr>
      <td>lnc-4149a201, TSS-del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000154149</td>
      <td>491 bp</td>
      <td>98%</td>
      <td>No</td>
      <td>Yes</td>
      <td>bhlhe22</td>
      <td>*</td>
      <td>Proximity to developmental regulatory genes</td>
    </tr>
    <tr>
      <td>lnc-4149a202, gene del.</td>
      <td>Leaderlike</td>
      <td>ENSDART00000154149</td>
      <td>35.11 kb</td>
      <td>100%</td>
      <td>No</td>
      <td>Yes</td>
      <td>bhlhe22</td>
      <td>*</td>
      <td>Proximity to developmental regulatory genes</td>
    </tr>
  </tbody>
</table>

## Results and discussion

The genomic location of selected lncRNAs are depicted in Figure 1. The neighbor-relationship, and expression levels of the selected lncRNAs and their neighboring genes are shown in Figure 1—figure supplement 1–1, Figure 1—figure supplement 1–2, respectively.

![Figure 1.](https://cdn.elifesciences.org/articles/40815/elife-40815-fig1-v2.jpg)

**Figure 1.:** The chromosomal positions of selected lncRNAs are depicted. lncRNAs discussed in the text are underlined. The corresponding genomic coordinates for all lncRNAs are provided in the supplementary file 2.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/40815/elife-40815-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) lncRNA names and sizes are shown in the middle section (blue columns). The distance, size and transcriptional orientation of the neighboring genes, in a 200 kb window centered on lncRNA’s TSS are shown on the left (upstream neighbor) and on the right (downstream neighbor). The transcription orientation is represented by green (in the same direction as lncRNA) and magenta (in the opposite direction of lncRNA). (B) Visual representation of data in A. All sizes and distances are in Kb.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/40815/elife-40815-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** LncRNAs are color coded as blue (Intergenic), brown (Overlapping) and green (Divergent/Promoter associated) (see Figure 1—figure supplement 1B). For each lncRNA and its upstream (top) and downstream (bottom) neighbor, the expression levels at 10 early-developmental stages are shown (Pauli et al., 2012). The scale is log2 (FPKM +1) value, represented as gradient between 0 (white) and 8 (magenta).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/40815/elife-40815-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** Nine guide RNAs (the first six plus three additional gRNAs around the Transcriptional Termination Site, TTS) were used to generate the gene deletions. Relative positions of genotyping primers are indicated by numbered circles.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/40815/elife-40815-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** Visual representation of the expression level changes for each lncRNA and its neighboring genes in homozygous deletion mutants. Three biological replicates for homozygous mutant and wild-type samples. Log2 of fold change between −4 (magenta) and 4 (green) is shown.

Using CRISPR-Cas9 (Figure 1—figure supplement 1–3) we generated 32 knockout-alleles. 24 alleles removed regions containing transcription start sites (TSS-deletion; 244 bp to 736 bp), and eight alleles fully or partially removed the gene (1 kb to 203 kb) (Table 1). qRT-PCR analysis demonstrated effective reduction in the levels of the targeted lncRNA transcripts (average reduction of 94 ± 6%; Table 1), which was further tested and confirmed for a subset of lncRNAs by in situ RNA hybridization (Figures 2B, 3B, C, 4D, 5B and 6D).

![Figure 2.](https://cdn.elifesciences.org/articles/40815/elife-40815-fig2-v2.jpg)

**Figure 2.:** (A) The positions of TSS-deletion allele and gene deletion allele are marked by dashed red lines. Green box represents the conserved element in cyrano which is complementary to miR-7. Solid red lines indicate the position of the first exon-intron boundary (e1i1) morpholino and conserved microRNA binding site (CMiBS) morpholinos. Arrows flanking black dotted line mark the primer binding sites for qRT-PCR product. (B) Representative images of in situ hybridization for cyrano in wild type (15/15) and both homozygous TSS-deletion (21/22) and gene deletion (18/18) 1-dpf. (C) At 2-dpf gene deletion mutants (lower-left), (and TSS-deletion mutants, not shown) were not different from the wild-type embryos (upper-left). Morpholino injected wild-type embryos (upper-middle and upper-left) reproduced observed phenotype in Ulitsky et. al (Kok et al., 2015). Morpholino injected deletion-mutants, lacking the corresponding binding sites for morpholinos, (lower-middle and lower-left) were comparable to morpholino injected wild types.

![Figure 3.](https://cdn.elifesciences.org/articles/40815/elife-40815-fig3-v2.jpg)

**Figure 3.:** (A) Position of the TSS-deletion allele in gas5 is marked by dashed red line. Arrows flanking black dotted lines mark the primer binding sites for 5’-qPCR and 3’-qPCR products. (B) Representative in situ hybridization images for gas5 in wild type (11/11) and homozygous TSS-deletion mutants (11/11). (C) Maternal and Zygotic gas5 (MZgas5) mutant embryos at 1-dpf were indistinguishable from the wild-type embryos at the same developmental stage (not shown). (D) Expression level of gas5 and osbpl9 measured by qRT-PCR. Tor3A, the other neighboring gene, was not expressed at the investigated time-point. (E) Expression level of gas5, its trans targets ptena, ptenb and nr3c1 measured by qRT-PCR. The statistical significance of the observed changes was determined using t-test analysis and represented by star marks (*, **, ***, and **** respectively mark p-values<0.05,<0.01,<0.001 and<0.0001).

![Figure 4.](https://cdn.elifesciences.org/articles/40815/elife-40815-fig4-v2.jpg)

**Figure 4.:** (A) The relative position of lnc-setd1ba and the protein-coding gene setd1ba. The gene deletion region is marked by dashed red line. Arrows flanking black dotted line mark the primer-binding sites for qRT-PCR product. (B) Maternal and zygotic lnc-setd1ba mutants were not different from wild-type embryos at 1-dpf. (C) Representative images of in situ hybridization for lnc-setd1ba at four- to eight-cell stage mutant (18/18) and wild-type (25/25) embryos. (D) In situ hybridization for the protein-coding mRNA, setd1ba (9/11) in lnc-setd1ba mutants compared to the wild-type embryos (15/15). (E) qRT-PCR at 1 cell stage and 1-dpf for the lncRNA and its neighboring genes rhoF and setd1ba. The statistical significance of the observed changes was determined using t-test analysis and represented by star marks (ns, *, **, ***, and **** respectively mark p-values≥0.05,<0.05,<0.01,<0.001 and<0.0001).

![Figure 5.](https://cdn.elifesciences.org/articles/40815/elife-40815-fig5-v2.jpg)

**Figure 5.:** (A) The position of untranslated regions (brown), coding region (green), putative Dorsal Localization Element- DLE (blue) and the gene deletion (red dashed line) in the squint genomic locus. Arrows flanking black dotted line mark the primer binding sites for qRT-PCR product. (B) In situ hybridization for squint at 8-cell stage on wild-type (18/20) and MZsquinta175(17/17) embryos. (C) qRT-PCR for squint and eif4ebp1 on wild-type and MZsquinta175 embryos at 1-cell stage. (D) Two representative MZsquinta175 embryos. (E) MZsquinta175 embryonic phenotype (N = 4 independent crosses, n = 360 embryos). The statistical significance of the observed changes was determined using t-test analysis and represented by star marks (ns, *, **, ***, and **** respectively mark p-values≥0.05,<0.05,<0.01,<0.001 and<0.0001).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/40815/elife-40815-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Schematic representation of injected mRNAs. Cap-analog is indicated by in blue circles at the beginning of each mRNA. squint non-protein coding mRNA was generated by adding 8 Adenine-nucleotides (red circles) after in-frame ATG codons. (B) Table shows scoring outcome of observed phenotypes in embryos injected with 30 pg of each indicated mRNA. (C) Representative embryos showing typical wild-type, squint mutant or dorsalized morphology. Ambiguous phenotypes were scored as ‘Affected’.

![Figure 6.](https://cdn.elifesciences.org/articles/40815/elife-40815-fig6-v2.jpg)

**Figure 6.:** (A) The red dashed lines depict the respective positions of the lnc-phox2bb TSS and gene deletion. Arrows flanking black dotted line mark the primer binding sites for qRT-PCR product. (B) Homozygous gene deletion mutants but not the TSS-deletion mutants show embryonic defects in jaw formation (arrow head) and swim bladder inflation (asterisk) by 4-dpf. (C) Histone marks (H3K4me1 and H3K27ac) associated with enhancer activity (Bogdanovic et al., 2012) and conserved noncoding elements (CNEs) (Hiller et al., 2013) overlap with gene deletion. (D) phox2bb expression pattern in the TSS and gene deletions. (E) qRT-PCR analysis on MZ TSS-deletion and gene deletion mutants. The statistical significance of the observed changes was determined using t-test analysis and represented by star marks (*, **, ***, and **** respectively mark p-values<0.05,<0.01,<0.001 and<0.0001).

Previous observations in mammalian cell culture systems suggested that lncRNA promoters can affect the expression of nearby genes (Engreitz et al., 2016). To test if these results hold true in vivo, we measured the changes in the expression of neighboring genes (a 200 kb window centered on each lncRNA) in lncRNA mutants. Several mutants displayed changes in the expression of neighboring genes (Figure 1—figure supplement 1–4). In particular, 10 out of 40 neighboring genes showed more than two-fold changes in expression, lending in vivo support to observations in cell culture systems (Engreitz et al., 2016).

To determine the developmental roles of our selected lncRNAs, we generated maternal-zygotic mutant embryos (lacking both maternal and zygotic lncRNA activity) and analyzed morphology from gastrulation to larval stages, when all major organs have formed. Previous large-scale screens (Driever et al., 1996; Haffter et al., 1996) have shown that the visual assessment of live embryos and larvae is a powerful and efficient approach to identify mutant phenotypes, ranging from gastrulation movements and axis formation to the formation of brain, spinal cord, floor plate, notochord, somites, eyes, ears, heart, blood, pigmentation, vessels, kidney, pharyngeal arches, head skeleton, liver, and gut. No notable abnormalities were detected in 31/32 mutants. Moreover, these 31 mutants survived to adulthood, indicating functional organ physiology, and were fertile (Table 1). In the following section, we describe the results for five specific lncRNAs and put them in the context of previous studies.

### Cyrano

cyrano is evolutionarily conserved lncRNA and based on morpholino studies, has been suggested to have essential functions during zebrafish embryogenesis (Ulitsky et al., 2011) and brain morphogenesis (Sarangdhar et al., 2018). cyrano has also been suggested to act as a sponge (decoy-factor) for HuR during neuronal proliferation (Kim et al., 2016a), regulate miR-7 mediated embryonic stem cell differentiation (Smith et al., 2017), and control the level of miR-7 in the adult mouse brain (Kleaveland et al., 2018). We generated two mutant alleles that removed the TSS (cyranoa171) or the gene (cyranoa172), including the highly conserved miR-7 binding-site (Figure 2A,B). The expression level of the nearby gene (oip5) was not affected in either of these mutants (Figure 1—figure supplement 1–4). In contrast to previous morpholino studies in zebrafish (Ulitsky et al., 2011) but in support of recent findings in mouse (Kleaveland et al., 2018), cyrano mutants developed normally and were viable and fertile.

The difference between morphant (Ulitsky et al., 2011) and mutant phenotypes might be caused by compensation in the mutants (Rossi et al., 2015; El-Brolosy and Stainier, 2017). To test this possibility, we injected the previously used morpholinos targeting the first exon-intron boundary (e1i1) or the conserved miR-7 binding site (CMiBS) into wild type and homozygous deletion mutants. The TSS-mutant allele lacked the e1i1 morpholino-binding site and the gene deletion allele lacked the CMiBS morpholino-binding site (Figure 2A). The previously reported phenotypes, including small heads and eyes, heart edema, and kinked tails were found in both wild type and mutants (Figure 2C), demonstrating that the morpholino-induced phenotypes were non-specific. These results reveal that cyrano transcripts or their evolutionarily conserved miR-7-binding site, are not required for embryogenesis, viability or fertility.

### gas5

gas5 is an evolutionarily conserved lncRNA (growth-arrest specific 5) (Coccia et al., 1992) that is highly expressed in early development (Figure 3B) and hosts several snoRNAs implicated in zebrafish development (Higa-Nakamine et al., 2012). Knockdown and knockout studies in cell culture (Ma et al., 2016) have indicated that gas5 might act as a tumor suppressor (Pickard and Williams, 2015) and exert effects at distant genomic sites (Schneider et al., 1988). However, the role of this lncRNA in development has not been studied in any vertebrate. Our gas5a173 mutant allele removed the sequences containing the TSS (−169 to +127) (Figure 3A) and resulted in complete elimination of its expression (Figure 3B and D). Expression of the neighboring gene osbpl9, encoding a lipid-binding protein, was increased by 50% (Figure 3D). Previous studies have shown that gas5 lncRNA can act in trans to affect pten expression (ptena and ptenb in zebrafish) by sequestering specific microRNAs (Li et al., 2017; Zhang et al., 2018; Liu et al., 2018). Additionally, gas5 transcript can mimic Glucocorticoid Response Element and act as a decoy factor (riborepressor) for the Glucocorticoid Receptor (nr3c1)-mediated transcription (Kino et al., 2010). We analyzed the expression level changes of these genes in MZgas5a173 embryos (at 1-dpf) and found significant upregulation for ptena in MZgas5a173 mutants (Figure 3E). Despite these changes in gene expression, gas5a173 mutants were indistinguishable from wild type (Figure 3C), reached adulthood and were fertile.

### Lnc-setd1ba

Lnc-setd1ba is the zebrafish orthologue of human LIMT (Sas-Chen et al., 2016) (LncRNA Inhibiting Metastasis), which has been implicated in basal-like breast cancers. It is expressed from a shared promoter region that also drives the expression of the histone methyltransferase setd1ba in opposite direction (Figure 4A). Evolutionary conservation in vertebrates and proximity to setd1ba, whose mouse homolog is essential for embryonic development (Eymery et al., 2016; Kim et al., 2016b) prompted us to investigate the function of this lncRNA in zebrafish. We removed the gene of lnc-setd1ba downstream of its TSS (3137 bp deletion) (lnc-setd1baa174). In situ hybridization and qRT-PCR revealed absence of lncRNA expression (Figure 4C and E) and strong upregulation of setd1ba (Figure 4D and E) during cleavage stages and slight upregulation of setd1ba and the other neighboring gene rhoF at one-day post fertilization (1-dpf) (Figure 4E). Despite these changes, maternal-zygotic lnc-setd1baa174 mutants were indistinguishable from wild type (Figure 4B), reached adulthood and produced normal progeny.

### Squint

Squint encodes a Nodal ligand involved in mesendoderm specification (Pei et al., 2007; Heisenberg and Nüsslein-Volhard, 1997). The previously studied squint insertion mutant alleles (squintHi975Tg 50 and squintcz35 51) lead to delayed mesendoderm specification and partially penetrant cyclopia (Dougan et al., 2003). Morpholino and misexpression studies have suggested an additional, non-coding role for maternally provided squint, wherein the squint 3'UTR mediates dorsal localization of squint mRNA, induces the expression of dorsal mesoderm genes, and is required for the development of dorsal structures (Gore et al., 2005; Lim et al., 2012). This mode of activity assigns squint to the cncRNA family - RNAs with both protein-coding and non-coding roles (Sampath and Ephrussi, 2016). To investigate the non-coding roles of squint mRNA we generated a deletion allele (squinta175) that lacked most of the protein coding region and the 3’UTR, including the Dorsal Localization Element (DLE) implicated in maternal squint RNA localization (Gilligan et al., 2011) (Figure 5A). In this allele 525 bp (178 bp 5’UTR, 280 bp first exon and 67 bp of second exon) out of the 1592bp-long mature transcript remain in the genome (Figure 5A). In situ hybridization (Figure 5B) and qRT-PCR (Figure 5C) showed that the level of remaining squint transcript was greatly reduced (~90%). MZsquint a175 embryos displayed partially penetrant cyclopia, similar to existing protein-disrupting squint alleles (Figure 5D) (Pei et al., 2007; Heisenberg and Nüsslein-Volhard, 1997; Golling et al., 2002), but the defects proposed to be caused by interference with squint non-coding activity (Gore et al., 2005) were not detected.

To further test whether squint mRNA might have non-coding roles, we injected wild-type and MZsquint a175 embryos with either control RNA, full-length squint mRNA, a non-coding version of squint mRNA, or the putative transcript produced in squint a175 (Figure 5—figure supplement 5–S1). We found that in contrast to wild-type squint mRNA, control RNA, non-protein coding squint RNA or squint a175 RNA did not cause any phenotypes and did not rescue MZsquint a175 mutants. These results indicate that squint 3’UTR does not have the previously proposed non-coding functions and that the squint transcript may not be a member of the cncRNA family.

### Transcript-independent phenotype at lnc-phox2bb locus

Lnc-phox2bb neighbors phox2bb and smtnl1. Phox2bb is a transcription factor implicated in the development of the sympathetic nervous system (Pei et al., 2013), (Moreira et al., 2016; Tolbert et al., 2017), while smtnl1 has been implicated in smooth muscle contraction (Borman et al., 2009). Whole-gene deletion of lnc-phox2bb (lnc-phox2bba177) (Figure 6A) led to jaw deformation and failure to inflate the swim-bladder (Figure 6B), and no homozygous mutant fish survived to adulthood. Like the whole-gene deletion allele, the TSS-deletion allele (lnc-phox2bba176) lacked lnc-phox2bb RNA (Figure 6E), but in contrast to the whole-gene deletion mutants, TSS-deletion mutants developed normally and gave rise to fertile adults. To determine the cause of this difference, we analyzed the expression level and pattern of neighboring genes. We found that the anterior expression domain of phox2bb in the hindbrain was absent in the whole-gene deletion allele (Figure 6D). This finding is consistent with the observation that the deleted region contains enhancer elements for phox2bb (McGaughey et al., 2008), conserved non-coding elements (CNEs) (Hiller et al., 2013) (Figure 6C), and histone marks related to enhancer regions (H3K4me1 and H3K27Ac) (Bogdanovic et al., 2012). We also found that the expression level of smtnl1 increased in gene deletion mutants relative to the TSS-deletion mutant and wild type (Figure 6E). These results indicate that lnc-phox2bb RNA is not required for normal development but that the lnc-phox2bb overlaps with regulatory elements required for proper expression of phox2bb and smtnl1 (Figure 6E).

In summary, our systematic mutant studies indicate that none of the 25 lncRNAs analyzed here are essential for embryogenesis, viability or fertility, including the prominent lncRNAs cyrano, gas5, and lnc-setd1ba. Additionally, they refute the proposed non-coding function of squint RNA. Our phenotypic screen does not exclude more subtle phenotypes; for example in behavior or brain activity (Rihel et al., 2010; Randlett et al., 2015; Summer et al., 2018). This mutant collection can now be analyzed for subtle, context specific or redundant functions, but extrapolation suggests that most individual zebrafish lncRNAs are not required for embryogenesis, viability or fertility.

## Materials and methods

### Animal care

TL/AB zebrafish (Danio rerio) were used as wild-type fish in this study. Fish were maintained on daily 14 hr (light): 10 hr (dark) cycle at 28°C. All animal works were performed at the facilities of Harvard University, Faculty of Arts and Sciences (HU/FAS). This study was approved by the Harvard University/Faculty of Arts and Sciences Standing Committee on the Use of Animals in Research and Teaching (IACUC; Protocol #25–08)

### Cas9 mediated mutagenesis

Guide RNAs (gRNAs) were designed using CHOPCHOP (Montague et al., 2014) and synthesized in pool for each candidate as previously described (Gagnon et al., 2014). (See supplementary file 1 for the gRNA sequences). gRNAs were combined with Cas9 protein (50 μM) and co-injected (~1 nL) into the one-cell stage TL/AB wild-type embryos. Genomic DNA from 10 injected and 10 un-injected siblings was extracted (Meeker et al., 2007) and screened for the difference in amplified band pattern from the targeted region (See supplementary file 1 for the genotyping primer sequences). The rest of injected embryos were raised to adulthood, crossed to wild-type fish and screened for passing the mutant allele to the next generation. Founder fish with desirable mutations were selected and confirmed by Sanger sequencing of the amplified mutant allele. Heterozygous mutants were crossed together to generate homozygous mutants. At least 15 adult homozygous mutant pairs per allele were crossed to test fertility of mutants and to generate maternal and zygotic mutants (MZ) devoid of maternally and zygotic lncRNA activity.

### Phenotype scoring procedure

Visual assessment of live embryos and larvae performed (Driever et al., 1996; Haffter et al., 1996) to identify mutant phenotypes, ranging from gastrulation movements and axis formation to the formation of brain, spinal cord, floor plate, notochord, somites, eyes, ears, heart, blood, pigmentation, vessels, kidney, pharyngeal arches, head skeleton, liver, and gut.

At day 5, formation of swim bladder and overall appearance of the embryos were checked again (at any stage 60–100 embryos were scored). Sixty to hundred fish from heterozygous mutant crosses were grown to adulthood and genotyped to identify the viability of adult homozygous fish. Validated homozygous mutant fish were further crossed together to test for potential fertility phenotypes or putative maternal functions of candidate lncRNAs.

### Antisense RNA synthesis and in situ hybridization

Antisense probes for in situ hybridization were transcribed using the DIG RNA labeling kit (Roche). All RNAs were purified using EZNA Total RNA kits (Omega Biotek). Embryos were fixed in 4% formaldehyde overnight at 4°C (embryos younger than 50% epiboly fixed for 2 days). In situ hybridizations were performed according to standard protocols (Thisse and Thisse, 2008). NBT/BCIP/Alkaline phosphatase-stained embryos were dehydrated in methanol and imaged in benzyl benzoate:benzyl alcohol (BBBA) using a Zeiss Axio Imager.Z1 microscope.

### qRT-PCR

Total RNA was isolated from three individuals or sets of 10–20 embryos per condition using EZNA Total RNA kits (Omega Biotek). cDNA was generated using iScript cDNA Synthesis kit (Bio-Rad). qPCR was conducted using iTaq Universal SYBR Green Supermix (Bio-Rad) on a CFX96 (Bio-Rad). Gene expression levels were calculated relative to a reference gene, ef1a. Three technical replicates were used per condition. The qPCR primer sequences are listed in supplementary file 1.

### Bright-field imaging

Embryos were anesthetized in Tricaine (Sigma) and mounted in 1% low melting temperature agarose (Sigma) with Tricaine, then imaged using a Zeiss SteREO Discovery.V12 microscope or Zeiss Axio Imager.Z1 microscope. Images were processed in FIJI/ImageJ (Schindelin et al., 2012). Brightness, contrast and color balance was applied uniformly to images.

### Sense RNA synthesis and injections

The sequences for the wild-type squint mRNA, non-protein coding squint transcript (One Adenine base was added after eight in-frame ATG codons, and the 3’UTR sequence kept unchanged) and the squinta175 transcript were synthesized as gBlocks (IDT) containing 5’ XhoI cut site and 3’ NotI site. Fragments were digested and inserted the pCS2 plasmid. Positive colonies were selected, and sanger sequenced to assure the accuracy of the gene synthesis process. Sequences of the constructs are provided in supplementary file 1. mRNA was in vitro transcribed by mMessage mMachine (Ambion) and purified by EZNA Total RNA kits (Omega Biotek). h2b-gfp was used as control mRNA. Each injection mix contained 30 ng/ul of squint or control mRNA). 1 nl of mRNA mix was injected into the yolk of one-cell stage embryos.

Morpholinos were ordered from Gene Tools and injected based on Ulitsky et al. (2011).
