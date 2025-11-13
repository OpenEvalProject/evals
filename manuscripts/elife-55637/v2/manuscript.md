# Start codon disruption with CRISPR/Cas9 prevents murine Fuchs’ endothelial corneal dystrophy

## Authors

- Hironori Uehara<sup>1</sup> ([ORCID: 0000-0001-6133-4918](https://orcid.org/0000-0001-6133-4918)) †
- Xiaohui Zhang<sup>1</sup>
- Felipe Pereira<sup>2</sup>
- Siddharth Narendran<sup>2</sup>
- Susie Choi<sup>3</sup>
- Sai Bhuvanagiri<sup>3</sup>
- Jinlu Liu<sup>3</sup>
- Sangeetha Ravi Kumar<sup>1</sup>
- Austin Bohner<sup>3</sup>
- Lara Carroll<sup>3</sup>
- Bonnie Archer<sup>1</sup>
- Yue Zhang<sup>4</sup>
- Wei Liu<sup>4</sup>
- Guangping Gao<sup>5</sup>
- Jayakrishna Ambati<sup>2</sup>
- Albert S Jun<sup>6</sup>
- Balamurali K Ambati<sup>1</sup> †

### Affiliations

1. Phil and Penny Knight Campus for Accelerating Scientific Impact, University of Oregon Eugene, OR United States
2. Department of Ophthalmology, University of Virginia Charlottesville United States
3. Moran Eye Center, Department of Ophthalmology and Visual Sciences, University of Utah Salt Lake City United States
4. Division of Epidemiology, Department of Internal Medicine, University of Utah Salt Lake City United States
5. Gene Therapy Center, Department of Microbiology and Physiological Science Systems, University of Massachusetts Medical School Worcester United States
6. Wilmer Eye Institute, Johns Hopkins University Baltimore United States

† Corresponding author

## Abstract

A missense mutation of collagen type VIII alpha 2 chain (COL8A2) gene leads to early-onset Fuchs’ endothelial corneal dystrophy (FECD), which progressively impairs vision through the loss of corneal endothelial cells. We demonstrate that CRISPR/Cas9-based postnatal gene editing achieves structural and functional rescue in a mouse model of FECD. A single intraocular injection of an adenovirus encoding both the Cas9 gene and guide RNA (Ad-Cas9-Col8a2gRNA) efficiently knocked down mutant COL8A2 expression in corneal endothelial cells, prevented endothelial cell loss, and rescued corneal endothelium pumping function in adult Col8a2 mutant mice. There were no adverse sequelae on histology or electroretinography. Col8a2 start codon disruption represents a non-surgical strategy to prevent vision loss in early-onset FECD. As this demonstrates the ability of Ad-Cas9-gRNA to restore the phenotype in adult post-mitotic cells, this method may be widely applicable to adult-onset diseases, even in tissues affected with disorders of non-reproducing cells.

## Introduction

Fuchs’ endothelial corneal dystrophy (FECD), which is characterized by progressive loss of corneal endothelial cells, is the leading cause of corneal transplantation in industrialized societies (EBAA, 2016). Currently, the only available treatment for advanced FECD is corneal transplantation, which entails significant risks (e.g., infection, hemorrhage, rejection, glaucoma) both during surgery and during the lifetime of the patient (Mitry et al., 2014; Sugar et al., 2015). A missense mutation of the collagen 8A2 (COL8A2) gene in humans causes early-onset Fuchs’ dystrophy (Gottsch et al., 2005; Biswas et al., 2001; Vedana et al., 2016). Although other mutations within the ZEB1/TCF8 locus and TCF4 trinucleotide repeats are associated with Fuchs’ dystrophy (Riazuddin et al., 2010; Igo et al., 2012; Aldave et al., 2013; Stamler et al., 2013; Nanda et al., 2014; Mootha et al., 2015; Nakano et al., 2015; Afshari et al., 2017; Kuot et al., 2017), only the Col8a2 missense mutant mouse has successfully recapitulated its key features. Two distinct transgenic approaches in mice have helped illuminate the role of Col8a2 in the onset of FECD. Knockout mice lacking Col8a2 alone or combined with a homozygous Col8a1 knockout mutation do not develop FECD (Hopfer et al., 2005). Although the double knockouts exhibited corneal biomechanical weakening (without endothelial loss), Col8a2 knockouts showed no apparent phenotype. In contrast, Col8a2 mutant knock-in mice carrying the Q455K and L450W mutations associated with early-onset FECD in human patients displayed corneal endothelial excrescences known as guttae, as well as the endothelial cell loss, which are hallmarks of human FECD (Meng et al., 2013; Jun et al., 2012). Taken together, these studies suggest that COL8A2 protein is not essential to corneal function, yet is causally responsible for FECD via mutant dominant gain-of-function activity. We, therefore, sought to test whether knockdown of mutant COL8A2 could offer a new therapeutic strategy for early-onset FECD, establishing a precedent for treating gain-of-function genetic disorders in post-mitotic cells by tissue-specific ablation of the missense gene, targeting the start codon with CRISPR/Cas9.

## Results

### Strategy of mouse Col8a2 gene knockdown by CRISPR/Cas9

To disrupt Col8a2 gene expression, we designed a guide RNA (gRNA) targeting the start codon of the Col8a2 gene (MsCol8a2gRNA) by non-homologous end-joint repair through CRISPR/Cas9 (Mali et al., 2013; Cong et al., 2013; Figure 1a). The strategy of targeting the start codon is sufficient for blocking gene expression at the translational level. The appeal of this strategy, as opposed to correcting the mutation through homologous recombination (HR), is that poor efficiency of CRISPR-based HR would result in a majority of sequence changes comprising insertions/deletions (indels). Consequently, the farther one targets downstream from the start codon, the greater the risk of missense mutations that result in viable mutant proteins with unknown activity. By targeting inside or near the start codon, this risk is minimized. As a backbone plasmid, we used pX330-U6-Chimeric_BB-CBh-hSpCas9 (Cong et al., 2013), which encodes spCas9 and gRNA downstream of the U6 promoter (px330-MsCol8a2gRNA1). To detect the indel, we used CviAII or Hin1II digestion of PCR products (Figure 1b). CviAII/Hin1II cuts 5’-CATG-3’, which digests at the Col8a2 start codon, whereas an undigested band indicates the presence of an indel at the start codon. As expected, px330-MsCol8a2gRNA1 creates an indel in mouse NIH3T3 cells (Figure 1b). Furthermore, we designed MsCol8a2gRNA2 and MsCol8a2gRNA3 downstream of MsCol8a2gRNA1 (Figure 1a). Co-transfection of px330-MsCol8a2gRNA1 with px330-MsCol8a2gRNA2 or px330-MsCol8a2gRNA3 resulted in an extra PCR band (Figure 1c). The indels by px330-MsCol8A2gRNA1 were confirmed by sequencing (Figure 1d). Although two gRNAs could potentially attenuate target gene expression more efficiently than a single gRNA, we proceeded with in vivo experiments using only MsCol8a2gRNA1.

![Figure 1.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig1-v2.jpg)

**Figure 1.:** (a) Design of guide RNAs (gRNAs) for mouse Col8a2 gene and the schematic diagram of indel detection by restriction enzyme digestion of the PCR product. gRNA1, which is used for Ad-Cas9-Col8a2gRNA, was designed to disrupt the Col8a2 start codon. PCR primers were designed to flank the start codon and gRNA-targeting sites. PCR product from the intact DNA sequence was of 560 bp, which was digested to 303 bp, 131 bp, and 126 bp by CviAII/Hin1II restriction enzymes. (b) In px330-gRNA1-transfected NIH3T3 cells, the PCR product showed an extra band (~430 bp, arrow) after CviAII digestion. pMax-GFP was used as a control. (c) A combination of two plasmids (px330-gRNA1 + px330-gRNA2 and px330-gRNA1 + px330-gRNA2) yields lower bands (arrow), reflecting the deletion between the targeted sites. (d) Deletion of the start codon by px330-gRNA1 was confirmed by Sanger sequencing after cloning.

### In vivo Col8a2 gene knockdown in mouse corneal endothelium by adenovirus-mediated CRISPR/Cas9

To introduce the genes (SpCas9 and gRNA) into corneal endothelium in vivo, we produced recombinant adenovirus Cas9-Col8a2gRNA (Ad-Cas9-Col8a2gRNA). There are several common viruses such as adeno-associated virus and lentivirus, but previous studies have indicated that only adenovirus demonstrates efficient gene transfer to corneal endothelium, in vivo. In fact, we found adenovirus-GFP showed efficient green fluorescent protein (GFP) expression in corneal endothelium (Figure 2a). First, we determined the effective adenovirus dose in vitro, for indel production at the Col8a2 start codon (Figure 2—figure supplement 1a–c). To confirm effective indel production in vivo, we tested various titers of Ad-Cas9-Col8a2gRNA injected into the aqueous humor of adult C57BL/6J mice. After 1 month, the corneal endothelium/stroma and epithelium/stroma were separated mechanically (Figure 2—figure supplement 2a–h), followed by genomic DNA (gDNA) purification. Digestion of PCR products by CviAII/Hin1II revealed an undigested band from amplified corneal endothelium DNA (arrow in Figure 2b), indicating disruption of the Col8a2 start codon, which was confirmed by Sanger sequence analysis (Figure 2c). In contrast, corneal epithelium and stroma revealed an intact start codon after CviAII/Hin1II digestion of PCR-amplified DNA. Further, the genome of Ad-Cas9-Col8a2gRNA was detected from corneal endothelium but not corneal epithelium/stroma (Figure 2—figure supplement 3). This strongly suggests that the anterior chamber injection of Ad-Cas9-Col8a2gRNA induces indels in the corneal endothelium but not in the epithelium or stroma.

![Figure 2.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig2-v2.jpg)

**Figure 2.:** (a) Adenovirus infection to corneal endothelium via intracameral injection was confirmed by adenovirus GFP. Top: whole mouse cornea flatmount. Bottom: the magnified section of the image. (b) Ad-Cas9-Col8a2gRNA1 induced an insertion/deletion (indel) at the Col8a2 start codon in the corneal endothelium but not in the corneal epithelium/stroma. Genomic DNA of corneal endothelium/stroma and corneal epithelium/stroma was PCR amplified with primers flanking the Col8a2 start site and digested with CviAII, which recognizes the intact Col8a2 start codon (5’-CATG-3’). The CviAII undigested band (arrow) demonstrates the indel at the Col8a2 start codon. (c) Sanger sequencing of the cloned PCR product from genomic DNA purified from corneal endothelium/stroma confirming indels at the Col8a2 start codon.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (a) Cloning of Ad-Cas9-Col8a2gRNA by its indel activity in AD293 cells. The method was the same as described for Figure 1. The extra band (arrow) demonstrates the indel at the start codon. We examined 30 different clones and found only one clone with indel activity. (b) As Ad-Cas9-Col8a2gRNA titer increased, indel activity also increased. (c) Results from Sanger sequencing of cloned PCR products.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Mouse corneal endothelium was peeled off mechanically. (a) Mouse cornea after excision from the rest of the eye. (b) Mouse cornea was stained with 0.4% trypan blue for visualization, and the limbus/sclera was removed. (c–e) Mechanical peeling of corneal endothelium. (f) Epithelium/stroma and stroma/endothelium after complete separation. (g, h) Cryosection image of the cornea with endothelium peeled. 4′,6-diamidino-2-phenylindole (DAPI) staining showed incomplete separation of corneal endothelium and stroma.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** 1 week following adenovirus injection, we purified DNA from corneal endothelium and epithelium/stroma, respectively. Then, PCR was conducted using primers to detect Cas9.

Next, to examine whether start codon disruption reduces COL8A2 protein expression in the corneal endothelium, we measured the localized protein in sectioned corneas with an anti-COL8A2 antibody (Figure 3 and Figure 3—figure supplement 1a). The non-injected cornea showed COL8A2 protein expression in corneal epithelium and endothelium. As predicted, Ad-Cas9-Col8a2gRNA-injected corneas exhibited reduced COL8A2 protein expression in corneal endothelium but not corneal epithelium. Furthermore, we measured the intensity of COL8A2 staining in corneal endothelium and epithelium (Figure 3—figure supplement 1b–c). The intensity of isotype control was subtracted as a background. While the epithelium layer did not show any significant difference, the intensity of COL8A2 staining in corneal endothelium layer significantly decreased at 0.63 × 107 vg and 0.25 × 108 vg of Ad-Cas9-Col8a2gRNA compared to the no-injection control. Thus, we successfully knocked down in vivo COL8A2 protein expression in adult corneal endothelium by Ad-Cas9-Col8a2gRNA.

![Figure 3.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig3-v2.jpg)

**Figure 3.:** COL8A2 protein immunostaining from the cornea 2 months after injection with Dulbecco’s phosphate-buffered saline (DPBS) (4 µl, upper figures) or Ad-Cas9-Col8a2gRNA (0.63 × 107 vg in 4 µl, lower figures). In Ad-Cas9-Col8a2gRNA-injected corneas, lower COL8A2 protein expression was seen in corneal endothelium, but not in epithelium. Epi: epithelium, Str: stroma, En (arrow): endothelium. Scale bar = 100 µm.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (a) COL8A2 immunostaining in each amount of Ad-Cas9-Col8a2gRNA injection. (b) COL8A2 expression in corneal endothelium and corneal epithelium was quantified from the images. The staining intensity in isotype control was subtracted as a background. (c) The ratio of COL8A2 staining between corneal endothelium and epithelium. *p<0.01 by Student’s t-test. The source data is Figure3-figure supplement1_source data.xlsx.

### Determination of the safety dose of Ad-Cas9-Col8a2gRNA

As adenoviruses are known to induce inflammation and cell toxicity, we tested a range of Ad-Cas9-Col8a2gRNA titers for safety. Corneal transparency, corneal thickness, and histopathology appeared normal at low titers (Figure 4a–d), and ZO-1 immunolabeling detected reduced endothelial density in corneal flat mounts after injecting 1.0 × 108 vg (Figure 4e–f). A higher titer (4.0 × 108 vg) devastated the mouse corneal endothelium, inducing corneal opacity and edema in C57BL/6J mice (Figure 4—figure supplement 1). At 0.25 × 108 vg, neither tumor necrosis factor alpha (TNFα) nor interferon gamma (IFNγ) was upregulated 4 weeks after Ad-Cas9-Col8a2gRNA injection (Figure 4—figure supplement 2). Moreover, we confirmed that Ad-Cas9-Col8a2gRNA did not suppress retinal function, as monitored by electroretinography (ERG), or damage the retinal structure, as visualized by hematoxylin-eosin (HE) staining (Figure 4—figure supplements 3 and 4a). Finally, anterior chamber injection of Ad-Cas9-Col8a2gRNA did not induce liver or kidney damage or inflammation, as visualized by HE staining of hepatic and renal tissues (Figure 4—figure supplement 4b). Hence, subsequent experiments were performed with 0.25 × 108 vg of Ad-Cas9-Col8a2gRNA, which did not induce detectable toxicity.

![Figure 4.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig4-v2.jpg)

**Figure 4.:** (a) Injection of Ad-Cas9-Col8a2gRNA at 0.63 × 107, 0.25 × 108, and 1.0 × 108 vg did not result in corneal edema or opacity. (b) Representative corneal optical coherence tomography (OCT) images captured by Heidelberg Spectralis microscope with/without Ad-Cas9-Col8a2gRNA injection. (c) The average of central corneal thickness in each condition. Significant differences among groups were not observed (analysis of variance (ANOVA), p = 0.78). n = 8–12. Error bars show standard deviation. (d) Hematoxylin-eosin (HE), Periodic Acid-Schiff (PAS), and trichrome Masson staining showed no apparent phenotypes in Ad-Cas9-Col8A2gRNA-injected corneas compared to non-injected corneas. Scale bar = 50 µm. (e) Representative images of corneal flat mounts immunolabeled with ZO-1 antibody for each condition. Scale bar = 100 µm. (f) Average corneal endothelium densities. 1.0 × 108 vg Ad-Cas9-Col8A2gRNA reduced corneal endothelium density significantly; n = 6–9. *p<0.001 by Student’s t-test. Error bars show standard deviation. The source data is (c) Figure4-source data 1.xlsx and (f) Figure4-source data 2.xlsx.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** 2 weeks following intracameral injection of Dulbecco’s phosphate-buffered saline (DPBS) or Ad-Cas9-Col8a2gRNA (4 × 108 vg), corneas were harvested to examine endothelial integrity with anti-ZO-1 antibody. This high titer of Ad-Cas9-Col8a2gRNA led to widespread devastation of the corneal endothelium. Scale bar = 200 µm.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Tumor necrosis factor alpha (TNFα) and interferon gamma (IFNγ) were stained 4 weeks post Ad-GFP, Ad-Cas9-Col8a2gRNA, or concanavalin A (1 μg) intravitreal injection. Scale bar is 100 μm.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Dark-adapted electroretinography (ERG) was used for evaluation of retinal function. (a) Representative ERG of no treatment (prior to injection), Ad-GFP (anterior chamber injection), Ad-Cas9-Col8a2gRNA (anterior chamber injection), and concanavalin A (intravitreal injection). Intravitreal injection of concanavalin A was used as a positive control by inducing retinal inflammation. (b, c) a-wave of no treatment and each treatment 2 and 4 weeks post injection. We used three different stimulus light intensities (−1.7,–0.8, and 1 log cd.s/m2). (d, e) b-wave of no treatment and each treatment 2 and 4 weeks post injection. n = 14 (no treatment), 6 (Ad-GFP), 6 (Ad-Cas9-Col8a2gRNA), and 2 (concanavalin A, 1 μg). *p<0.05 and **p<0.01 by Student’s t-test compared to no-treatment control. The source data is Figure4-figure supplement3_source data.xlsx.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** 4 weeks post injection, we observed each tissue by hematoxylin-eosin (HE) staining. (a) Retina. Scale bar is 100 μm. (b) Liver and kidney. Scale bar is 400 μm.

### Efficiency of indel induction by Ad-Cas9-Col8a2gRNA in vivo

To determine the indel rate in mouse corneal endothelium, we performed deep sequencing of PCR products (including the target site) amplified from gDNA of corneal endothelium. We found that the indel rate was 23.7 ± 4.5% in mouse corneal endothelium (Table 1). Most insertions were 1 bp insertions (19.8 ± 4.0% in total reads, Figure 5a), while 2 bp deletions were the most frequent (1.0 ± 0.3% in total reads, Figure 5b). We, moreover, found that A or T insertion was predominant, with the proportion of A:T:G:C being 48.7:44.6:1.8:4.9 (Table 2). Adenine insertion (9.4 ± 1.9% in total reads) produced a cryptic ATG start codon (Figure 5—figure supplement 1). This insertion changes G to C at the −3 position (A in ATG as +1). Since previous studies have indicated that G or A at the −3 position is important for translational commencement, which is known as a Kozak sequence (Kozak, 1984; Rual et al., 2004), a consequent reduction in protein expression by the disruption of Kozak/ATG sequence would be predicted.

![Figure 5.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig5-v2.jpg)

**Figure 5.:** (a) Frequency of insertion. 1 bp insertion was most frequent. (b) Frequency of deletion. 2 bp deletion was most frequent. n = 4. Error bar represents standard deviation. The source data is Figure5-source data.xlsx.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** An adenine insertion produced a cryptic ATG codon that resulted in disruption of Kozak sequence (G to C at −3 position).

**Table 1.**
 Indel rate at mouse Col8a2 target site by Ad-Cas9-Col8a2gRNA from corneal endothelium.Table 1—source data 1.Indel rate in Col8a2 gene.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Total read</th>
      <th>No change</th>
      <th>Insertion</th>
      <th>Deletion</th>
      <th>Indel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Cornea1</td>
      <td rowspan="2">87,554</td>
      <td>68,228</td>
      <td>16,378</td>
      <td>2948</td>
      <td>19,326</td>
    </tr>
    <tr>
      <td>(77.9%)</td>
      <td>(18.7%)</td>
      <td>(3.4%)</td>
      <td>(22.1%)</td>
    </tr>
    <tr>
      <td rowspan="2">Cornea2</td>
      <td rowspan="2">97,749</td>
      <td>69,455</td>
      <td>24,202</td>
      <td>4092</td>
      <td>28,294</td>
    </tr>
    <tr>
      <td>(77.1%)</td>
      <td>(24.8%)</td>
      <td>(4.2%)</td>
      <td>(28.9%)</td>
    </tr>
    <tr>
      <td rowspan="2">Cornea3</td>
      <td rowspan="2">87,908</td>
      <td>71,664</td>
      <td>13,508</td>
      <td>2736</td>
      <td>16,244</td>
    </tr>
    <tr>
      <td>(81.5%)</td>
      <td>(24.8%)</td>
      <td>(3.1%)</td>
      <td>(18.5%)</td>
    </tr>
    <tr>
      <td rowspan="2">Cornea4</td>
      <td rowspan="2">93,234</td>
      <td>69,747</td>
      <td>19,831</td>
      <td>3656</td>
      <td>23,487</td>
    </tr>
    <tr>
      <td>(74.8%)</td>
      <td>(21.3%)</td>
      <td>(3.9%)</td>
      <td>(25.2%)</td>
    </tr>
    <tr>
      <td colspan="2">Average of ratio</td>
      <td>76.3 ± 4.5%</td>
      <td>20.0 ± 4.0%</td>
      <td>3.6 ± 0.5%</td>
      <td>23.7 ± 4.5%</td>
    </tr>
  </tbody>
</table>

_The source data is Table1-source data.xlsx._

**Table 2.**
 Ratio of A:T:G:C in 1 bp insertions.Table 2—source data 1.Number of inserted DNA residues.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Total read number of single insertions in the start codon (between A and T)</th>
      <th>A</th>
      <th>T</th>
      <th>G</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cornea1</td>
      <td>15,655</td>
      <td>7925 (50.6%)</td>
      <td>6703 (42.8%)</td>
      <td>230 (1.5%)</td>
      <td>797 (5.1%)</td>
    </tr>
    <tr>
      <td>Cornea2</td>
      <td>23,315</td>
      <td>10,877 (46.7%)</td>
      <td>10,890 (46.7%)</td>
      <td>294 (1.3%)</td>
      <td>1254 (5.4%)</td>
    </tr>
    <tr>
      <td>Cornea3</td>
      <td>13,083</td>
      <td>6035 (46.1%)</td>
      <td>6013 (46.0%)</td>
      <td>320 (2.4%)</td>
      <td>715 (5.5%)</td>
    </tr>
    <tr>
      <td>Cornea4</td>
      <td>18,829</td>
      <td>9706 (51.5%)</td>
      <td>8088 (43.0%)</td>
      <td>356 (1.9%)</td>
      <td>679 (3.6%)</td>
    </tr>
    <tr>
      <td colspan="2">Average of ratio</td>
      <td>48.7 ± 2.7%</td>
      <td>44.6 ± 2.0%</td>
      <td>1.8 ± 0.5%</td>
      <td>4.9 ± 0.9%</td>
    </tr>
  </tbody>
</table>

_The source data is Table2-source data.xlsx._

The indel rate in corneal endothelium was 23.7 ± 4.5%, which was much lower than anticipated since COL8A2 protein expression in mouse corneal endothelium was markedly decreased by the anterior chamber injection of Ad-Cas9-Col8a2gRNA (Figure 3 and Figure 3—figure supplement 1) and because of the high rate of adenovirus infection of the corneal endothelium (Figure 2a). We speculate this is due to gDNA from corneal stroma cells based on the following. The number of corneal endothelial cells is approximately 7200 cells (2300 cells/mm2 x 1 mm x 1 mm x π), with an expected purified gDNA amount of 43 ng as the genome mass from mouse cell is 6 pg ((5.46 x 109 as 2n) x 660 (average molecular weight of DNA base pair)/(6.02 x 10−23, Avogadro’s number)). The purified gDNA from the peeled endothelium was higher than predicted (Table 3). We, therefore, hypothesized that stromal cells were contained in our samples. To confirm this, we conducted experiments as described in Figure 2—figure supplement 2. We peeled half of corneal endothelium, placed back in situ, and then proceeded to cryosection with 4′,6-diamidino-2-phenylindole (DAPI) staining. As expected, we found stroma cells along with corneal endothelial cells. Hence, we deduced that the extra gDNA is stromal-derived. Therefore, we can normalize indel rate by the proportion of endothelial cell gDNA to total isolated gDNA (Table 3). From this calculation, the normalized indel rate (proportion of endothelial cells with indels) is 102.5 ± 16.3%. This corroborates with the observed immunostaining pattern in Figure 3 and Figure 3—figure supplement 1.

**Table 3.**
 Normalized indel rate by the purified genomic DNA amount.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Concentration (ng/ul)</th>
      <th>gDNA amount (ng, 16 ul elution)</th>
      <th>Cell number from gDNA amount</th>
      <th>Intact indel rate (%)</th>
      <th>Normalized indel rate (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cornea1</td>
      <td>14.5</td>
      <td>232</td>
      <td>38,744</td>
      <td>22.1</td>
      <td>118.6</td>
    </tr>
    <tr>
      <td>Cornea2</td>
      <td>10.5</td>
      <td>168</td>
      <td>28,056</td>
      <td>28.9</td>
      <td>112.3</td>
    </tr>
    <tr>
      <td>Cornea3</td>
      <td>12</td>
      <td>192</td>
      <td>32,064</td>
      <td>18.5</td>
      <td>82.1</td>
    </tr>
    <tr>
      <td>Cornea4</td>
      <td>10.4</td>
      <td>166.4</td>
      <td>27,789</td>
      <td>25.2</td>
      <td>97.0</td>
    </tr>
  </tbody>
</table>

To understand the relationship between Cas9/gRNA expression and Col8a2 expression, we measured Cas9 and gRNA expression 1 week following injection of Ad-Cas9-Col8a2gRNA by real-time reverse transcription-PCR (RT-PCR). We found that Cas9 and gRNA expressions were high at 0.63 × 107 and 2.5 × 107 vg (Figure 6a–b) and that these doses of Ad-Cas9-Col8a2gRNA demonstrated a significant decrease of COL8A2 in corneal endothelium as shown in Figure 3—figure supplement 1. Furthermore, to determine the indel rate, we designed two sets of primers for the Col8a2 mRNA. One set was designed at the unrelated position of gRNA target. This set of primers detects total Col8a2 mRNA with and without indels. The other primer set was designed at the indel site, which does not detect Col8a2 mRNA with indel but does detect normal Col8a2 mRNA without indels. In C57BL/6J mice, the normal Col8a2 mRNA (no indel) rates were 58.7 ± 11.4% (6.3 × 106 vg) and 56.1 ± 42.9% (25 × 106 vg), while in Col8a2Q455K mice, the normal Col8a2 mRNA (no indel) rates were 67.5 ± 19.0% (6.3 × 106 vg) and 35.4 ± 33.3% (25 × 106 vg) (Figure 6c). Furthermore, Cas9 mRNA and gRNA were positively correlated (Figure 6d). On the other hand, Cas9/gRNA and normal Col8a2 mRNA rate were inversely correlated (Figure 6e and d). Thus, the anterior chamber injection of Ad-Cas9-Col8a2gRNA induces indels, directly correlated to the Cas9/gRNA expression in C57BL/6J and Col8a2Q455K mice.

![Figure 6.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig6-v2.jpg)

**Figure 6.:** (a and b) Cas9 mRNA and gRNA expression in corneal endothelium 1 week following anterior chamber injection of Ad-Cas9-Col8a2gRNA. (c) The expression ratio of mouse Col8a2 mRNA without indels and total Col8a2 mRNA with/without indels were determined by real-time reverse transcription-PCR (RT-PCR). *p<0.05 and **p<0.01 by Student’s t-test. (d) gRNA and Cas9 mRNA expression are positively correlated. (e) Normal Col8a2 mRNA (no indel) rate and Cas9 mRNA are negatively correlated. (f) Normal Col8a2 mRNA (no indel) rate and gRNA expression are negatively correlated. The source data is Figure6_source data.xlsx.

### Ad-Cas9-Col8a2gRNA rescues corneal endothelium architecture in Col8a2Q455K/Q455K FECD mice

Next, we examined whether Ad-Cas9-Col8a2gRNA rescued corneal endothelium in the early-onset Col8a2Q455K/Q455K FECD mouse model (Jun et al., 2012). At 2 months of age, we performed a single intraocular injection of Ad-Cas9-Col8a2gRNA into one eye of each mouse. Non-injected contralateral eyes were used as controls. After the injection, the corneal endothelium was examined by in vivo corneal confocal microscopy (Figure 7a). Ad-Cas9-Col8a2gRNA-injected eyes showed slower reduction of corneal endothelium than the non-injected eyes (Figure 7b). After 10 months (12-month-old), apparent differences between corneal endothelium of Ad-Cas9-Col8a2gRNA-injected and non-injected eyes were obvious (Figure 7c). We found that intraocular injection of Ad-Cas9-Col8a2gRNA significantly rescued corneal endothelium in Col8a2Q455K/Q455K mice (Figure 7d). This was confirmed by Alizarin red staining (Figure 7e), which demonstrated a significantly higher corneal endothelium density in Ad-Cas9-Col8a2gRNA-injected corneas than in non-injected FECD eyes (Figure 7f).

![Figure 7.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig7-v2.jpg)

**Figure 7.:** (a) Representative in vivo corneal endothelium images using the Heidelberg Rostock microscope at 3 and 6 months post injection. Ad-Cas9-Col8a2gRNA was injected intracamerally into Col8a2Q455K/Q455K mice at 2 months of age. Scale bar = 100 μm. (b) Time course change in corneal endothelial cell density of Col8a2Q455K/Q455K mice, n = 5. Ad-Cas9-Col8a2gRNA slows loss of corneal endothelial cells compared to no-injection group. (c) Representative in vivo corneal endothelium image at 12 months of age. Age-matched C57BL/6J and non-injected Col8a2Q455K/Q455K mice were used for comparison. Ad-Cas9-Col8a2gRNA qualitatively improved endothelial cell density. Scale bar = 100 μm. (d) Average corneal endothelium densities: C57BL/6J: 2134 ± 45 cells/mm2, non-injected Col8a2Q455K/Q455K: 677 ± 110 cells/mm2, and Ad-Cas9-Col8a2gRNA-injected Col8a2Q455K/Q455K: 1141 ± 102 cells/mm2, n = 4. Error bars show standard deviation. (e) Representative corneal endothelium from each group stained with Alizarin red. Scale bar = 200 μm. (f) Average corneal endothelium densities calculated from Alizarin red-stained corneas: C57BL/6J: 2108 ± 134 cells/mm2, non-injected Col8a2Q455K/Q455K: 696 ± 70 cells/mm2, and Ad-Cas9-Col8a2gRNA-injected Col8a2Q455K/Q455K: 1256 ± 135 cells/mm2, n = 4. Error bars show standard deviation. The source data is Figure7_source data.xlsx.

Further detailed analysis of corneal endothelium indicated changes in cell density and morphology (Figure 8). Analysis of paired corneas (injected and non-injected in the same mouse) showed significant improvements in corneal endothelial cell density by Ad-Cas9-Col8a2gRNA treatment in all four individual mice (Figure 8a). Figure 8b shows the distribution of corneal endothelial cell area. The morphology of the corneal endothelium, as monitored by hexagonality, and coefficient of variation (COV) of its density were improved considerably (Figure 8c–d). In vivo corneal optical coherence tomography (OCT) demonstrated that Ad-Cas9-Col8a2gRNA decreased the formation of guttae-like structures compared to control (Figure 9a–b), which was confirmed by histology (Figure 9c–d). Thus, Ad-Cas9-Col8a2gRNA successfully ameliorated the loss of corneal endothelium and the morphologic phenotype in the early-onset FECD mouse model.

![Figure 8.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig8-v2.jpg)

**Figure 8.:** (a) Corneal endothelium density in each cornea was calculated using Alizarin red staining. A total of 50 different cell areas were measured in each cornea. Injected (Ad-Cas9-Col8a2gRNA) and non-injected corneas in the same mouse were compared by Student’s paired t-test. (b) Histogram of corneal endothelial cell area in Ad-Cas9-Col8A2gRNA-injected cornea and non-injected cornea quantitatively demonstrates left-shifting in cell size, that is, enhanced density, in the former. N = 200 in each group from four different corneas. (c) Hexagonality and (d) coefficient of variation (COV) of corneal endothelium were significantly improved by Ad-Cas9-Col8A2gRNA intracameral injection in Col8a2Q455K/Q455K mice. N = 200 from four different corneas in each group. The source data is Figure8_source data.xlsx.

![Figure 9.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig9-v2.jpg)

**Figure 9.:** (a) Corneal optical coherence tomography (OCT) revealed numerous guttae-like excrescences (arrows) in 1-year-old Col8a2Q455K/Q455K mice, but far fewer in Ad-Cas9-Col8a2gRNA-injected Col8a2Q455K/Q455K mice. (b) Histogram showing the number of guttae-like structures in each group. Non-injected Col8a2Q455K/Q455K: 5.2 ± 3.4 excrescences/image and Ad-Cas9-Col8a2gRNA-injected Col8a2Q455K/Q455K: 0.5 ± 0.73 excrescences/image. n = 16. P-value by Mann-Whitney U-test is <0.001. (c, d) Periodic Acid-Schiff (PAS)-stained corneas from non-injected and Ad-Cas9-Col8a2gRNA-injected Col8A2Q455K/Q455K mice. The arrows indicate guttae-like structures (excrescences). The source data is Figure9_source data.xlsx.

### Ad-Cas9-Col8a2gRNA rescues corneal endothelium function in Col8a2Q455K/Q455K FECD mice

Next, we examined whether Ad-Cas9-Col8a2gRNA could rescue corneal endothelial pump function of the Col8a2Q455K/Q455K FECD mouse, which is essential for corneal clarity and optimal vision (Bonanno, 2012). Surprisingly, Col8a2Q455K/Q455K corneas did not develop edema or opacity even at 1 year of age despite reduced endothelial density (Figure 10—figure supplement 1). We, therefore, developed a functional assay to deliberately induce corneal swelling and assess pump function by measuring the de-swelling rate. As direct application of a 0 mOsm/l solution was found to induce epithelial rather than stromal swelling (Figure 10—figure supplement 2), we performed epithelial debridement to eliminate any confounding epithelial effects (Figure 10a). Application of an osmolar range of phosphate-buffered saline (PBS) solutions (Figure 10b) produced a range of swelling volumes, with 600–700 mOsm/l solution producing the maximal effect, with quadrupling of the stromal thickness (Figure 10b–c). Thus, the epithelial layer functions as a barrier to maintain stromal thickness, whereas hypertonic solutions seem to induce aqueous humor ingression into the cornea. Having optimized our model, we measured de-swelling rates following a 10-min application of 650 mOsm/l PBS. Successive corneal OCT images showed that the rate of de-swelling in non-injected Col8a2Q455K/Q455K corneas was significantly delayed compared to C57BL/6J control corneas. In contrast, Ad-Cas9-Col8a2gRNA-injected Col8a2Q455K/Q455K corneas demonstrated de-swelling rates similar to C57BL/6J corneas (Figure 10d–e). Thus, Ad-Cas9-Col8a2gRNA rescued corneal endothelial function in FECD mice.

![Figure 10.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig10-v2.jpg)

**Figure 10.:** (a) Stereomicroscopic images of scraped mouse cornea. (b) Corneal optical coherence tomography (OCT) images of pre-treatment, after scrape, and after treatment with 0 mOsm/l (water), 300, 600, 700, and 900 mOsm/l Dulbecco’s phosphate-buffered saline (DPBS) application followed by water again. (c) Changes in corneal thickness in response to variance in DPBS osmolality demonstrate that maximal swelling occurred at 600–700 mOsm/l DPBS. (d) Repeated measurements of central corneal thickness were taken using corneal OCT after application of 650 mOsm/l PBS. To prevent evaporation, 4 µl of silicone oil was applied at t = 0 (n = 6). #p<0.001 by regression analysis. NS: not significant. (e) De-swelling of central corneal thickness was measured from 0 min to 5, 10, 20, 30, 40, and 50 min. Non-injected Col8a2Q455K/Q455K corneas showed significantly delayed de-swelling compared to C57BL/6J corneas. In contrast, Ad-Cas9-Col8a2gRNA injection significantly improved corneal de-swelling rate similar to that of C57BL/6J controls (n = 6). *p<0.05 by Student’s t-test. The source data is Figure10_source data.xlsx.

![Figure 10—figure supplement 1.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig10-figsupp1-v2.jpg)

**Figure 10—figure supplement 1.:** Central corneal thickness was measured by corneal optical coherence tomography (OCT); p-value was calculated by analysis of variance (ANOVA). The source data is Figure10-figure supplement1_source data.xlsx.

![Figure 10—figure supplement 2.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig10-figsupp2-v2.jpg)

**Figure 10—figure supplement 2.:** (a) Representative corneal optical coherence tomography (OCT) images before and after water was applied for 10 min. (b) The average thickness of total, upper (epithelium), and lower (stroma) corneal surface before and after water application for 10 min. n = 5. Error bars show standard deviation; p-value was calculated by Student’s t-test. The source data is Figure10-figure supplement2_source data.xlsx.

### Potential off-target effects of gRNA targeting the human COL8A2 start codon

For potential therapeutic application of CRISPR/Cas9, we evaluated the off-target activity of humanized gRNA by a modified digenome analysis (Kim et al., 2015). Briefly, digenome analysis consists of (1) in vitro digestion of purified gDNA with SpCas9 and gRNA; (2) deep sequencing of the digested gDNA; and (3) alignment of sequence reads at the digested sites. Consequently, digested sites other than the target site are considered potential off-target sites. In fact, we found that the readings at the target site (human COL8A2 start codon) were aligned but not without gRNA (Figure 11a–b). After careful observation, a gap was often found at the target site (Figure 11c). Since off-target analysis without considering such a gap would underestimate off-target events, we included a ± 1 gap in our modified digenome analysis. Figure 11d shows the digenome score alignments of control gDNA (no gRNA) and treated gDNA (HuCol8a2gRNA). From this, candidate sites were selected, for which the score was >60. We identified eight different sequences in 13 different locations that had homology to HuCol8a2gRNA and were associated with a PAM sequence (Table 4). The majority of these sequences were non-coding sites, and the remaining sites (two of which were anti-sense sites and two of which were intronic sites) (SRGAP2-AS1, SV2C, KAT6B, LMO7-AS1, ACAN) have no known corneal function. Table 5 shows 8 of 21 candidates that had neither homology to HuCol8a2gRNA nor PAM sequence. Table 6 shows four sequences in control gDNA.

![Figure 11.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig11-v2.jpg)

**Figure 11.:** (a, b) Mapping of reads to human COL8A2 target site from HuCol8a2gRNA-treated genomic DNA (gDNA) and control gDNA. (c) A gap was observed in in vitro digestion of genomic DNA. (d) Modified digenome score alignment (0–1.0) of control gDNA (no gRNA) and HuGol8a2gRNA-treated gDNA.

![Figure 11—figure supplement 1.](https://cdn.elifesciences.org/articles/55637/elife-55637-fig11-figsupp1-v2.jpg)

**Figure 11—figure supplement 1.:** (a) Plasmid-based Cas9/HuCol8a2gRNA induced (insertions/deletions) indels in AD293 cells. Arrow indicates an indel band. (b) Gel electrophoresis image of in vitro transcription of HuCol8a2gRNA. (c) PCR confirmed in vitro digestion of purified AD293 genomic DNA by Cas9/HuCol8a2gRNA. PCR primers were designed to target the digestion site.

**Table 4.**
 HuCol8a2gRNA off-target sites with homology.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Chr</th>
      <th>Gap</th>
      <th>Start</th>
      <th>Gene</th>
      <th>Plus</th>
      <th>Depth</th>
      <th>Perc</th>
      <th>Minus</th>
      <th>Depth</th>
      <th>Perc</th>
      <th>Total</th>
      <th>Sequence with PAM*</th>
      <th>Identity (% including PAM)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>36100241</td>
      <td rowspan="3">COL8A2, coding (target site)</td>
      <td>13</td>
      <td>13</td>
      <td>100</td>
      <td>5</td>
      <td>6</td>
      <td>83.33</td>
      <td>94.74</td>
      <td>CGTCCACGGACGCCATGCTGGG</td>
      <td>100</td>
    </tr>
    <tr>
      <td></td>
      <td>1</td>
      <td>1</td>
      <td>36100241</td>
      <td>13</td>
      <td>13</td>
      <td>100</td>
      <td>9</td>
      <td>15</td>
      <td>60</td>
      <td>78.57</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>1</td>
      <td>1</td>
      <td>36100241</td>
      <td>11</td>
      <td>11</td>
      <td>100</td>
      <td>7</td>
      <td>11</td>
      <td>63.64</td>
      <td>81.82</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>1</td>
      <td>-1</td>
      <td>143388988</td>
      <td rowspan="2">Intergenic</td>
      <td>21</td>
      <td>30</td>
      <td>70</td>
      <td>26</td>
      <td>29</td>
      <td>89.66</td>
      <td>79.66</td>
      <td>CGTCCATGGACCCCAAGCTAGG</td>
      <td>81.8</td>
    </tr>
    <tr>
      <td></td>
      <td>1</td>
      <td>0</td>
      <td>143388989</td>
      <td>29</td>
      <td>59</td>
      <td>49.15</td>
      <td>26</td>
      <td>29</td>
      <td>89.66</td>
      <td>62.5</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3</td>
      <td>1</td>
      <td>-1</td>
      <td>144214582</td>
      <td rowspan="2">Intergenic</td>
      <td>21</td>
      <td>30</td>
      <td>70</td>
      <td>26</td>
      <td>31</td>
      <td>83.87</td>
      <td>77.05</td>
      <td>CGTCCATGGACCCCAAGCTAGG</td>
      <td>81.8</td>
    </tr>
    <tr>
      <td></td>
      <td>1</td>
      <td>0</td>
      <td>144214583</td>
      <td>29</td>
      <td>59</td>
      <td>49.15</td>
      <td>26</td>
      <td>31</td>
      <td>83.87</td>
      <td>61.11</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>4</td>
      <td>1</td>
      <td>-1</td>
      <td>144751794</td>
      <td rowspan="2">SRGAP2-AS1</td>
      <td>26</td>
      <td>31</td>
      <td>83.87</td>
      <td>20</td>
      <td>29</td>
      <td>68.97</td>
      <td>76.67</td>
      <td>CGTCCATGGACCCCAAGCTAGG</td>
      <td>81.8</td>
    </tr>
    <tr>
      <td></td>
      <td>1</td>
      <td>0</td>
      <td>144751794</td>
      <td>26</td>
      <td>31</td>
      <td>83.87</td>
      <td>29</td>
      <td>58</td>
      <td>50</td>
      <td>61.8</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>5</td>
      <td>2</td>
      <td>-1</td>
      <td>89549893</td>
      <td rowspan="2">Intergenic</td>
      <td>21</td>
      <td>30</td>
      <td>70</td>
      <td>17</td>
      <td>20</td>
      <td>85</td>
      <td>76</td>
      <td>CGTCCATGGACCCCAAGCTAGG</td>
      <td>81.8</td>
    </tr>
    <tr>
      <td></td>
      <td>2</td>
      <td>0</td>
      <td>89549894</td>
      <td>29</td>
      <td>59</td>
      <td>49.15</td>
      <td>17</td>
      <td>20</td>
      <td>85</td>
      <td>58.23</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>6</td>
      <td>2</td>
      <td>-1</td>
      <td>91624245</td>
      <td rowspan="2">Intergenic</td>
      <td>21</td>
      <td>30</td>
      <td>70</td>
      <td>26</td>
      <td>29</td>
      <td>89.66</td>
      <td>79.66</td>
      <td>CGTCCATGGACCCCAAGCTAGG</td>
      <td>81.8</td>
    </tr>
    <tr>
      <td></td>
      <td>2</td>
      <td>0</td>
      <td>91624246</td>
      <td>29</td>
      <td>59</td>
      <td>49.15</td>
      <td>26</td>
      <td>29</td>
      <td>89.66</td>
      <td>62.5</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>7</td>
      <td>4</td>
      <td>-1</td>
      <td>3707175</td>
      <td rowspan="2">Intergenic</td>
      <td>7</td>
      <td>8</td>
      <td>87.5</td>
      <td>10</td>
      <td>10</td>
      <td>100</td>
      <td>94.44</td>
      <td>TGCCCACGGGCACCATGTTGGG</td>
      <td>77.3</td>
    </tr>
    <tr>
      <td></td>
      <td>4</td>
      <td>-1</td>
      <td>3707175</td>
      <td>7</td>
      <td>8</td>
      <td>87.5</td>
      <td>9</td>
      <td>9</td>
      <td>100</td>
      <td>94.12</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>8</td>
      <td>4</td>
      <td>-1</td>
      <td>4185990</td>
      <td rowspan="2">Intergenic</td>
      <td>15</td>
      <td>21</td>
      <td>71.43</td>
      <td>19</td>
      <td>28</td>
      <td>67.86</td>
      <td>69.39</td>
      <td>AGTCCATGGACCACAAGCTAGG</td>
      <td>72.7</td>
    </tr>
    <tr>
      <td></td>
      <td>4</td>
      <td>0</td>
      <td>4185990</td>
      <td>15</td>
      <td>21</td>
      <td>71.43</td>
      <td>26</td>
      <td>54</td>
      <td>48.15</td>
      <td>54.67</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>9</td>
      <td>5</td>
      <td>-1</td>
      <td>76221510</td>
      <td rowspan="2">SV2C, intron</td>
      <td>9</td>
      <td>11</td>
      <td>81.82</td>
      <td>10</td>
      <td>17</td>
      <td>58.82</td>
      <td>67.86</td>
      <td>TGTCCAC-AACGTCATGCTTGG</td>
      <td>72.7</td>
    </tr>
    <tr>
      <td></td>
      <td>5</td>
      <td>-1</td>
      <td>76221510</td>
      <td>9</td>
      <td>11</td>
      <td>81.82</td>
      <td>7</td>
      <td>14</td>
      <td>50</td>
      <td>64</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10</td>
      <td>10</td>
      <td>-1</td>
      <td>74854844</td>
      <td rowspan="2">KAT6B, intron</td>
      <td>12</td>
      <td>20</td>
      <td>60</td>
      <td>21</td>
      <td>21</td>
      <td>100</td>
      <td>80.49</td>
      <td>CGTACACAGAAACCATGCTGGG</td>
      <td>81.8</td>
    </tr>
    <tr>
      <td></td>
      <td>10</td>
      <td>-1</td>
      <td>74854844</td>
      <td>12</td>
      <td>20</td>
      <td>60</td>
      <td>19</td>
      <td>19</td>
      <td>100</td>
      <td>79.49</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>11</td>
      <td>10</td>
      <td>-1</td>
      <td>130741051</td>
      <td rowspan="2">Intergenic</td>
      <td>7</td>
      <td>10</td>
      <td>70</td>
      <td>10</td>
      <td>16</td>
      <td>62.5</td>
      <td>65.38</td>
      <td>AGTCCA-GGAGGCCATGCTTGG</td>
      <td>81.8</td>
    </tr>
    <tr>
      <td></td>
      <td>10</td>
      <td>-1</td>
      <td>130741051</td>
      <td>7</td>
      <td>10</td>
      <td>70</td>
      <td>10</td>
      <td>16</td>
      <td>62.5</td>
      <td>65.38</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>12</td>
      <td>13</td>
      <td>-1</td>
      <td>75612825</td>
      <td rowspan="2">LMO7-AS1</td>
      <td>8</td>
      <td>14</td>
      <td>57.14</td>
      <td>13</td>
      <td>17</td>
      <td>76.47</td>
      <td>67.74</td>
      <td>GGTCCAC-GCCGCCATGCCCGG</td>
      <td>77.3</td>
    </tr>
    <tr>
      <td></td>
      <td>13</td>
      <td>-1</td>
      <td>75612825</td>
      <td>8</td>
      <td>14</td>
      <td>57.14</td>
      <td>13</td>
      <td>16</td>
      <td>81.25</td>
      <td>70</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>13</td>
      <td>15</td>
      <td>1</td>
      <td>88847941</td>
      <td rowspan="2">ACAN, coding</td>
      <td>16</td>
      <td>16</td>
      <td>100</td>
      <td>18</td>
      <td>21</td>
      <td>85.71</td>
      <td>91.89</td>
      <td>AGCCCCCGGACCCCATGCGTGG</td>
      <td>77.3</td>
    </tr>
    <tr>
      <td></td>
      <td>15</td>
      <td>1</td>
      <td>88847941</td>
      <td>16</td>
      <td>16</td>
      <td>100</td>
      <td>17</td>
      <td>20</td>
      <td>85</td>
      <td>91.67</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_*Red characters indicate mismatched DNA residues._

**Table 5.**
 HuCol8a2gRNA off-target sites without homology.


<table>
  <thead>
    <tr>
      <th>Location</th>
      <th>Chr</th>
      <th>Gap</th>
      <th>Start</th>
      <th>Plus</th>
      <th>Depth</th>
      <th>Perc</th>
      <th>Minus</th>
      <th>Depth2</th>
      <th>Perc2</th>
      <th>Total</th>
      <th>Sequence (50 bp around the detection site)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>189206630</td>
      <td>5</td>
      <td>10</td>
      <td>50</td>
      <td>6</td>
      <td>9</td>
      <td>66.67</td>
      <td>57.89</td>
      <td rowspan="2">gaacctcccacctcagcctaccgagtagctgagactatgggcacattccg</td>
    </tr>
    <tr>
      <td></td>
      <td>3</td>
      <td>1</td>
      <td>189206630</td>
      <td>5</td>
      <td>9</td>
      <td>55.56</td>
      <td>5</td>
      <td>7</td>
      <td>71.43</td>
      <td>62.5</td>
    </tr>
    <tr>
      <td>2</td>
      <td>4</td>
      <td>0</td>
      <td>83023938</td>
      <td>5</td>
      <td>7</td>
      <td>71.43</td>
      <td>6</td>
      <td>11</td>
      <td>54.55</td>
      <td>61.11</td>
      <td>acacatggacacagggagggggacatcactgtgtgatgtggggggcaagg</td>
    </tr>
    <tr>
      <td>3</td>
      <td>8</td>
      <td>1</td>
      <td>1351347</td>
      <td>6</td>
      <td>11</td>
      <td>54.55</td>
      <td>12</td>
      <td>16</td>
      <td>75</td>
      <td>66.67</td>
      <td>ggccgtgcgggtcctgagtgtggaacggccgtgcgggtcctgactgtgtg</td>
    </tr>
    <tr>
      <td>4</td>
      <td>8</td>
      <td>0</td>
      <td>143167239</td>
      <td>15</td>
      <td>26</td>
      <td>57.69</td>
      <td>11</td>
      <td>13</td>
      <td>84.62</td>
      <td>66.67</td>
      <td>ggaagtggagaaggggaaggaaggtcgtctagggaggaagtggagagggg</td>
    </tr>
    <tr>
      <td>5</td>
      <td>9</td>
      <td>1</td>
      <td>64082996</td>
      <td>6</td>
      <td>11</td>
      <td>54.55</td>
      <td>5</td>
      <td>7</td>
      <td>71.43</td>
      <td>61.11</td>
      <td>tatatatatatatatatatatatatatatatatatatatatatatatata</td>
    </tr>
    <tr>
      <td>6</td>
      <td>10</td>
      <td>1</td>
      <td>3085303</td>
      <td>15</td>
      <td>17</td>
      <td>88.24</td>
      <td>7</td>
      <td>13</td>
      <td>53.85</td>
      <td>73.33</td>
      <td>cccccactccactctccagcacagtcccccactccactctccagcacagt</td>
    </tr>
    <tr>
      <td>7</td>
      <td>16</td>
      <td>-1</td>
      <td>19382526</td>
      <td>5</td>
      <td>8</td>
      <td>62.5</td>
      <td>5</td>
      <td>8</td>
      <td>62.5</td>
      <td>62.5</td>
      <td>agttctcatctggaatttctataatagacccagagtcaacagccaggttc</td>
    </tr>
    <tr>
      <td>8</td>
      <td>16</td>
      <td>-1</td>
      <td>34625947</td>
      <td>46</td>
      <td>57</td>
      <td>80.7</td>
      <td>8</td>
      <td>26</td>
      <td>30.77</td>
      <td>65.06</td>
      <td>caaagctatccaaatatccacttgtagattatattcgagtgcattcgatg</td>
    </tr>
  </tbody>
</table>

**Table 6.**
 Detected sites with digenome scores >60 in the control genomic DNA.


<table>
  <thead>
    <tr>
      <th>Location</th>
      <th>Chr</th>
      <th>Gap</th>
      <th>Start</th>
      <th>Plus</th>
      <th>Depth</th>
      <th>Perc</th>
      <th>Minus</th>
      <th>Depth2</th>
      <th>Perc2</th>
      <th>Total</th>
      <th>Sequence (50 bp around the detection site)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>112180048</td>
      <td>5</td>
      <td>10</td>
      <td>50</td>
      <td>5</td>
      <td>6</td>
      <td>83.33</td>
      <td>62.5</td>
      <td>aaaagaaagtatcaaaggagtaaacagacaacctacagaatgggagaaaa</td>
    </tr>
    <tr>
      <td>2</td>
      <td>8</td>
      <td>0</td>
      <td>58814608</td>
      <td>6</td>
      <td>9</td>
      <td>66.67</td>
      <td>5</td>
      <td>9</td>
      <td>55.56</td>
      <td>61.11</td>
      <td>atagttttaggatttcaggatgccttctgttcagtttagtttatattgtt</td>
    </tr>
    <tr>
      <td>3</td>
      <td>12</td>
      <td>1</td>
      <td>74918031</td>
      <td>5</td>
      <td>7</td>
      <td>71.43</td>
      <td>5</td>
      <td>8</td>
      <td>62.5</td>
      <td>66.67</td>
      <td>tacctagaaagcaagcagaatactcttagccaagaaaacaatatgtactc</td>
    </tr>
    <tr>
      <td>4</td>
      <td>18</td>
      <td>-1</td>
      <td>49878347</td>
      <td>5</td>
      <td>10</td>
      <td>50</td>
      <td>6</td>
      <td>8</td>
      <td>75</td>
      <td>61.11</td>
      <td>ttaaaaatacttttttttttcctgcatctgatttggctgtcagtgtgaaa</td>
    </tr>
  </tbody>
</table>

## Discussion

In this study, we demonstrated that intraocular injection of a single adenoviral vector achieved efficient and restricted delivery of CRISPR/Cas9 to adult post-mitotic corneal endothelium, leading to in vivo knockdown of mutant Col8a2 with long-term preservation of corneal endothelial density, structure, and function in the early-onset Fuchs’ dystrophy mouse model.

We found that most of the insertions were single insertions of adenine, creating a cryptic start codon without frame shift (Figure 5—figure supplement 1). As mentioned above, this would disrupt the Kozak sequence. Taken together, our results indicate that disruption of the Kozak sequence effectively reduces protein expression without complications such as non-functional or frame-shifted protein production. Hence, Kozak sequence disruption by CRISPR/Cas9 targeting may provide a viable option for gene knockdown.

In this study, we performed the modified digenome method to determine potential off-target regions. Interestingly, we found a gap at the target site (Figure 11c). This gap may have been generated during sample preparation, due to causes such as Covaris shearing, polishing of overhanging DNA, and adenylation at 3’-end for ligation or fluctuation of Cas9/gRNA recognition to gDNA. We identified 13 potential off-target sites with homology, the majority of which were in non-coding sequences and other regions in genes of uncertain function. We found one potential coding exonic off-target sequence in the ACAN gene. ACAN (also referred to as aggrecan core protein) is a major component of extracellular matrix of cartilaginous tissues. Although several cartilage-bone-related diseases are caused by mutations of ACAN coding region, its expression was not observed in previously published RNAseq data of human corneal endothelium (Wieben et al., 2018; Wieben et al., 2019). Therefore, it is unlikely that this off-target indel would affect corneal function. We found off-target sequences in the intron of two genes, SV2C (Synaptic vesicle glycoprotein 2C) and KAT6B. SV2C is involved in synaptic function throughout the brain (Dunn et al., 2017), but it is rarely expressed in human corneal endothelium (Wieben et al., 2018; Wieben et al., 2019). KAT6B is a histone acetyltransferase that may be involved in both positive and negative regulation of transcription. Several developmental disorders are caused by distinct mutations of KAT6B (Campeau et al., 2012), and acute myeloid leukemia may be caused by a chromosomal aberration involving KAT6B gene (Panagopoulos et al., 2001). Therefore, KAT6B gene should be considered a gene at risk with our Crispr/Cas9 treatment. In most cases, intronic mutations causing human diseases are located within 100 bp from intron–exon boundary, as most diseases associated with intronic mutation create a pseudo-exon that disrupts splicing. The observed KAT6B off-target site is located over 11,000 bp from the exon–intron boundary. Hence, the off-target mutation in KAT6B is unlikely to cause corneal dysfunction. Two additional off-target candidates were found in the intron of non-coding RNAs, SRGAP2-AS1 and LMO7-AS1. Non-coding RNAs are sometimes known to have various functions in gene regulation, but the functions of SRGAP2-AS1 and LMO7-AS1 are unknown. All other off-target candidates are located in intergenic regions. Since some intergenic regions contain gene enhancer elements, mutations could theoretically contribute to disease risk (Bartonicek et al., 2017). Compared with exonic or intronic mutations, the risk of intergenic mutations inducing deleterious effects would be low. Thus, we identified off-target candidates of our CRISPR/Cas9 treatment that are expected to not cause corneal dysfunction. However, testing in large animals such as non-human primates should be performed prior to any clinical testing of in vivo CRISPR/cas9 treatment for humans.

Eight potential off-target sites without homology or PAM sequence were found, but we speculate these are likely random errors since the non-gRNA control also showed four potential off-target sites.

Previous papers have achieved in vivo editing in post-mitotic neurons using dual adeno-associated virus (AAV) to co-infect cells with Cas9 machinery (Nishiyama et al., 2017; Yu et al., 2017; Zhu et al., 2017). Although AAV has the advantages of low immunogenicity and toxicity, the low efficiency of HR by dual AAV delivery (10–12%) (Nishiyama et al., 2017) is unrealistic as a treatment approach, and the complexity of two vectors makes targeting efficacy assessment and clinical development challenging. Moreover, the long-term expression of AAV-based CRISPR/Cas9 may ultimately prove undesirable for a post-mitotic cell, since the potential for off-target gene editing will continue for the life of the AAV. In contrast, the high infectivity and short duration of adenoviral expression would enable structural and functional rescue by Ad-Cas9-Col8a2gRNA at a titer below adenoviral cytotoxicity, without risk of further (mis) editing events.

In conclusion, we succeeded in Col8a2 gene knockdown in corneal endothelium in vivo using an adenovirus-mediated SpCas9 and gRNA delivery, resulting in a functionally relevant rescue of corneal endothelium in the early-onset FECD mouse model. Our strategy can be applicable to other genes and useful in experiments. While a previous study (Yu et al., 2017) has shown prevention of neurodegeneration with a similar strategy, this is the first demonstration of functional rescue with Cas9-mediated gene knockdown using start codon disruption. Future studies will explore the impact of this approach on endothelial and inflammatory gene expression using RNA-Seq and whether we can suppress activation of the unfolded protein response in endothelial cells. In addition, prior to clinical development, gene therapy approaches will require optimization of gRNA and Cas9, understanding long-term effects, and refinement of the delivery strategy. Still, these results strongly suggest that our strategy can treat or at least prolong corneal endothelial life in early-onset Fuchs’ dystrophy, potentially eliminating the need for transplantation.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Strain, strain background (Mus musculus, C57BL/6J)</td>
      <td>C57BL/6J</td>
      <td>Jackson laboratories</td>
      <td>Stock # 000664 RRID:IMSR_JAX:000664</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus, 129S6/SvEvTac and C57BL/6J)</td>
      <td>Col8a2Q455K</td>
      <td>Johns Hopkins Medical Institutions</td>
      <td>PMID:22002996 RRID:MGI:5305276</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>a-COL8A2, rabbit polyclonal,</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# PA5-35077 RRID:AB_2552387</td>
      <td>(5 μg/ml)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Isotype, rabbit polyclonal</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 02–6102 RRID:AB_2532938</td>
      <td>(5 μg/ml)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>a-ZO1, mouse monoclonal</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 339188 RRID:AB_2532187</td>
      <td>(2.5 μg/ml)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>a-TNFa, rat monoclonal</td>
      <td>BioLegend</td>
      <td>Cat# 506301, clone: MP6-XT22 RRID:AB_315422</td>
      <td>(5 μg/ml)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>a-IFNg, rat monoclonal</td>
      <td>BioLegend</td>
      <td>Cat# 505801, clone: XMG1.2 RRID:AB_315395</td>
      <td>(5 μg/ml)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Isotype, rat monoclonal</td>
      <td>BioLegend</td>
      <td>Cat# 400401, clone RTK2071 RRID:AB_326507</td>
      <td>(5 μg/ml)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Secondary to rat IgG, conjugated with AlexaFluor647, goat polyclonal</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# A-21247 RRID:AB_141778</td>
      <td>(2 μg/ml)</td>
    </tr>
    <tr>
      <td>Cell line (human)</td>
      <td>AD-293</td>
      <td>Agilent Technologies</td>
      <td>Cat# 240085</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (mouse)</td>
      <td>NIH3T3</td>
      <td>ATCC</td>
      <td>Cat# CRL-1658 RRID:CVCL_0594</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>px330</td>
      <td>Addgene</td>
      <td>Cat# 42230 RRID:Addgene_42230</td>
      <td>Plasmid</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pShuttle</td>
      <td>Addgene</td>
      <td>Cat# 16402 RRID:Addgene_16402</td>
      <td>Plasmid</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BJ5183-AD-1</td>
      <td>Agilent Technologies</td>
      <td>Cat# 200157</td>
      <td>Competent cells</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>XL10-Gold</td>
      <td>Agilent Technologies</td>
      <td>Cat# 200314</td>
      <td>Competent cells</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>DH5a</td>
      <td>NEB</td>
      <td>Cat# C2987H</td>
      <td>Competent cells</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>MsCol8a2_intron2F</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>cggtggtaggtggtaattgg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>MsCol8a2_intron3R</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>tgtggtctggagtgtctgga</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>gRNAcloneF_EcoRV</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>TAGATATCgagggcctatttcccatgattc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>gRNAcloneR_XbaI</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>TATCTAGAagccatttgtctgcagaattggc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Forward PCR primer for DNAseq</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>TTCTTCTTCTCCCTGCAGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Reverse PCR primer for DNAseq</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>GCACATACTTTACCGGGGCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>HuCol8a2_F</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>tgatcttttggtgaccccgg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>HuCol8a2_R</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>GGATGTACTTCACTGGGGCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Forward PCR primer for gRNA template of in vitro transcription</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>TAATACGACTCACTATAGCGTCCACGGACGCCATG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Reverse PCR primer for gRNA template of in vitro transcription</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>AAAAGCACCGACTCGGTGCCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Cas9_Forward</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>CCGAAGAGGTCGTGAAGAAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Cas9_Reverse</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>GCCTTATCCAGTTCGCTCAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>gRNA_Forward</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>AGACGCCATGCGTTTTAGAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>gRNA_Reverse</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>CGGTGCCACTTTTTCAAGTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mouse GAPDH_Forward</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>AACTTTGGCATTGTGGAAGGGCTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mouse GAPDH_Reverse</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>ACCAGTGGATGCAGGGATGATGTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mouse Col8a2_Forward1 at Indel site</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>CCACCTACACGTACGACGAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mouse Col8a2_Reverse1</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>ACTCGGTGGAGTAGAGACCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mouse Col8a2_Forward2</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>CCATCCACAGACGCCATG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Mouse Col8a2_Reverse2</td>
      <td>This paper</td>
      <td>PCR primer</td>
      <td>GGGCTGCACATACTTTACCG</td>
    </tr>
  </tbody>
</table>

### Mice

C57BL/6J mice, 8–12 weeks old, were purchased from The Jackson Laboratory (Bar Harbor, ME) and used in this study. The Col8a2Q455K/Q455K mouse has been previously described (Meng et al., 2013; Jun et al., 2012; Matthaei et al., 2012). All animals were treated according to the Association for Research in Vision and Ophthalmology(ARVO) Statement for the Use of Animals in Ophthalmic and Vision Research.

### Plasmid construction

px330 plasmid encoding humanized Streptococcus pyogenes Cas9 was obtained from Addgene (Cambridge, MA). The design of gRNA and cloning were performed following published methods (Cong et al., 2013). Three separate gRNAs were designed to target sequences containing a trinucleotide PAM sequence (in italics):

Col8a2-gRNA1: CCCATCCACAGACGCCATGCAGG;

Col8a2-gRNA2: GGGTGCAGCGGGCTATGCCCCGG;

Col8a2-gRNA3: CCGCCTTTCCGAGAGGGCAAAGG.

### Cell lines

AD-293 cells were obtained from Agilent technology (Santa Clara, CA) in 2014. AD-293 cells are HEK-293-derived cells for adenovirus production. We provided genome sequences of our AD-293 cells in digenome experiments and were able to obtain adequate titers of adenovirus, substantiating the HEK-293 origin of this cell line. NIH3T3 cells were obtained from ATCC (Manassas, VA), which conducted the cell authentication. Both Agilent and ATCC tested for mycoplasma with negative tests. We did not use any of these cells after passage 10.

### Cell culture, plasmid transfection, and indel detection

Mouse NIH3T3 cells were maintained in 10% bovine calf serum/Dulbecco’s Modified Eagle’s medium (DMEM) following manufacturer’s instructions. 2 μg of plasmid was transfected by nucleofection (Lonza, Allendale, NJ). After 2 days, gDNA was purified using QIAamp DNA Mini Kit (Qiagen, Valencia, CA). 10 ng of gDNA was PCR amplified with the following primer set: MsCol8a2_intron2F: cggtggtaggtggtaattgg and MsCol8a2_intron3R: tgtggtctggagtgtctgga. The PCR product (560 bp) was purified with a Qiagen PCR purification kit and subsequently digested by CviAII restriction enzyme (NEB, Ipswich, MA) or Hin1II (Thermo Fisher Scientific, Waltham, MA) following the manufacturer’s protocols. We initially used CviAII before switching to Hin1ll due to low stability of CviAII (both enzymes cut CATG). Digested products were run on a 1% agarose electrophoresis gel. Uncut bands (~420 bp) were purified and cloned with CloneJET PCR Cloning kit (Thermo Fisher Scientific). After transformation to DH5α (NEB), individual colonies were cultured in lysogeny broth (LB) medium with ampicillin, purified via miniprep, and sent to the University of Utah DNA core facility for Sanger sequencing.

### Adenovirus production

Adenovirus production was carried out following previously published methods (Luo et al., 2007). All restriction enzymes described here were purchased from NEB. Empty Shuttle vector (pShuttle, #16402) was obtained from Addgene. Col8a2-gRNA1 with U6 promoter and terminator was amplified from pCas9-Col8A2gRNA by PCR using the following primers: gRNAcloneF_EcoRV: TAGATATCgagggcctatttcccatgattc and gRNAcloneR_XbaI: TATCTAGAagccatttgtctgcagaattggc. PCR product was cloned into pShuttle using EcoRV/XbaI (pShuttle-Col8A2gRNA). Next, Cas9 DNA (including the promoter and polyadenylation signal) was excised from px330 with NotI/XbaI and cloned into pShuttle-Col8A2gRNA1 (pShuttle-Cas9-Col8A2gRNA1). After linearization with PmeI, pShuttle-Col8A2gRNA was electroporated into BJ5183-AD-1 cells (Agilent Technologies, Santa Clara, CA) and grown on kanamycin LB plates. Small colonies were individually picked and cultured in 5 ml LB medium with kanamycin. After confirming size by digestion with PacI and other restriction enzymes, XL10-Gold Ultracompetent Cells (Agilent Technologies) were transformed with an amplified plasmid of the correct size. The Maxiprep (Qiagen) purified plasmids were linearized by PacI digestion and transfected to AD-293 cells (Agilent Technologies) using Lipofectamine 2000 (Thermo Fisher Scientific). After 14–20 days’ culture, adenovirus generating AD293 cells were harvested. HeLa cells were used to confirm the replication deficiency. The titer of recombinant adenovirus was determined by Adenovirus Functional Titer Immunoassay Kit (Cell Biolabs, Inc, San Diego, CA). The function of Ad-Cas9-Col8a2gRNA was examined using NIH3T3 as described above. For in vivo experiments, further production and purification were performed in a viral core facility at the University of Massachusetts.

### Anterior chamber injection

8-week-old male C57BL/6J mice received a single unilateral injection of Ad-Cas9-Col8a2gRNA into the anterior chamber, while the contralateral eye served as a non-injected control. All injections were performed in Animal Biosafety Level 2 Comparative Medicine Core Facility at the University of Utah. Mice were first anesthetized with ketamine (90 mg/kg) and xylazine (10 mg/kg) before topical application of tropicamide and proparacaine. Corneas were punctured 1.5 mm above the limbus with a 31 G needle and the needle gently withdrawn. Using a blunt 33 G Hamilton syringe, Ad-Cas9-Col8a2gRNA (4 μl) was injected through the puncture. To ensure injection delivery, the cannula remained in the anterior chamber for ~5 s after injection before applying erythromycin ophthalmic ointment to the cornea.

### Measurement of indel rate by deep sequencing

1-month post Ad-Cas9-Col8a2gRNA injection to C57BL/6J mice, the corneal endothelium was separated mechanically (Figure 2—figure supplement 2). gDNA from the corneal endothelium/stroma was purified by Quick-DNA Microprep Plus Kit (Zymo research). PCRs were performed on the locus using TTCTTCTTCTCCCTGCAGCC and GCACATACTTTACCGGGGCA (30 cycles, the product size: 155 bp). The deep sequencing was performed by the HSC core at University of Utah. The library was prepared using the Swift Biosciences Accel-NGS 1S Plus DNA Library Kit. The sequence protocol used MiSeq Nano 150 Cycle Paired End Sequencing v2. The total number of reads per file was counted. The reads with median quality scores ≤ 5 were removed from the data set. The reads were aligned to the expected genomic sequence: gi|372099106|ref|NC_000070.6|:126309560–126309770 Mus musculus strain C57BL/6J chromosome 4, GRCm38.p4 C57BL/6J.

### Digenome sequencing

#### Human COL8A2 gRNA design

We designed two different human Col8a2 gRNAs at the start codon of human COL8A2 similar to mouse Col8a2 gRNA.

HuCol8a2gRNA1 ACGTCCACGGACGCCATGC.

HuCol8a2gRNA2 CGTCCACGGACGCCATGCT.

Underlines indicate the start codon of human COL8A2. As explained in the main text, these sequences were cloned into px330 plasmid.

#### AD-293 cell culture and plasmid transfection

To confirm the activity of human gRNAs, we used human AD-293 cells (Agilent), which were maintained following the manufacturer’s instructions. Ca-phosphate method was used for plasmid transfection. Briefly, 0.25 × 106 cells were plated in a six-well plate with 2 ml of 10% fetal bovine serum/DMEM. The next day, 6 µg plasmid was transfected. 2 days post transfection, gDNAs were purified with Quick-DNA Plus Kit (Zymo Research, Irvine, CA).

#### PCR and restriction enzyme digestion for indel examination

To examine the indel at the target site, we used PCR and restriction enzyme digestion. PCR primers used were HuCol8a2_F: tgatcttttggtgaccccgg and HuCol8a2_R: GGATGTACTTCACTGGGGCA. The PCR product (226 bp) was digested with Hin1II, which recognizes CATG. Without indels, the COL8A2 PCR products were digested to 94 bp and 132 bp. As shown in Figure 11—figure supplement 1a, both px330 plasmid transfections showed the indel. Since we found that HuCol8a2gRNA2 showed slightly higher activity, we proceeded with HuCol8a2gRNA2 for further experiments (mentioned as HuCol8a2gRNA hereafter).

#### gRNA production by in vitro transcription

To produce gRNA, in vitro transcription was performed with MEGAshortscript T7 Transcription Kit (Thermo Fisher). The template DNA was obtained by PCR (Phusion High-Fidelity DNA Polymerase; NEB) with primers forward: TAATACGACTCACTATAGCGTCCACGGACGCCATG and reverse: AAAAGCACCGACTCGGTGCCA (the underline indicates T7 promoter) using px330-huCol8a2gRNA plasmid as a template. The integrity of gRNA was confirmed by 2% agarose DNA electrophoresis (Figure 11—figure supplement 1b).

#### In vitro genome digestion with Cas9

SpCas9 protein was obtained from NEB (M0386M). The reaction was performed in 8 µg gDNA (AD-293), 120 pmol (300 nM) SpCas9, 120 pmol (300 nM), or 360 pmol (900 nM) gRNA with 1X NEBuffer 3.1 (a total volume of 400 µl) at 37°C for 8 hr. After gDNA purification, the digestion at the target site was examined by PCR with HuCol8a2_F and HuCol8a2_R primers (Figure 11—figure supplement 1c). We found that 360 pmol gRNA (Cas9: gRNA = 1:3) showed efficient digestion. Therefore, we proceeded with 360 pmol gRNA-treated gDNA for deep sequencing.

#### Deep sequencing

Deep sequencing was performed at the HSC core at the University of Utah. The library was prepared with Illumina TruSeq Nano DNA Sample Prep kit (Illumina, San Diego, CA). The sequence protocol is NovaSeq 2 × 150 bp Sequencing 30X Human Whole Genome.

#### Data analysis

The sequencing data was analyzed at the Bioinformatics core of the University of Utah. As shown in Figure 11a–b, Cas9-digested gDNA with HuCol8a2 gRNA showed aligned sequencing at the Col8a2 gene target site. On the other hand, control gDNA (Cas9-digested without gRNA) showed random sequencing. Since we found a gap at the target site (Figure 11c), our analysis accepts the gap, which is explained below.

The human GRCh38 FASTA file was downloaded from Ensembl and a reference database was created using bowtie2 version 2.3.4. Adapters were trimmed out of reads using Cutadapt 1.16 and then aligned using Bowtie 2 in end-to-end mode (full options --end-to-end --sensitive --no-unal -k 20). The aligned reads were loaded into R using the GenomicAlignments package, and total coverage and read start coverage were calculated for the plus and minus strands. Positions with five or more read starts were compared to the total coverage and read starts with less than 25% of total coverage were removed. The filtered read starts on the positive and negative strands were joined to find predicted cut sites with either no overlap (blunt end), 1 bp gap, or 1 bp overhang.

### Real-time PCR

After purification of total RNA from the corneal endothelium and DNase I treatment, cDNA was synthesized with iScript cDNA Synthesis Kit (Biorad). Real-time PCR was conducted using SsoAdvanced Universal SYBR Green Supermix (Biorad) with BioRad CFX96 Real-Time PCR following the manufacture’s protocol (two-step PCR). The following primers were used in this study. Cas9 mRNA and DNA detection, Cas9_forward: CCGAAGAGGTCGTGAAGAAG and Cas9_reverse: GCCTTATCCAGTTCGCTCAG; gRNA detection, gRNA_forward: AGACGCCATGCGTTTTAGAG and gRNA_reverse: CGGTGCCACTTTTTCAAGTT; mouse GADPH, mouse GAPDH_forward: AACTTTGGCATTGTGGAAGGGCTC and mouse GAPDH_reverse: ACCAGTGGATGCAGGGATGATGTT; total mouse Col8a2, mouse Col8a2_forward1: CCACCTACACGTACGACGAA and mouse Col8a2_reverse1: ACTCGGTGGAGTAGAGACCA; and normal mouse Col8a2, not detection of Col8a2 mRNA with indel, mouse Col8a2_forward2: CCATCCACAGACGCCATG and mouse Col8a2_reverse2: GGGCTGCACATACTTTACCG.

### In vivo optical coherence tomography and corneal confocal microscopy

2 months after anterior chamber injection, corneal thickness was quantified by Spectralis OCT with the anterior-segment OCT module (Heidelberg Engineering, Franklin, MA). An HRT3 Rostock microscope (Heidelberg Engineering) was used to produce serial images of central corneal endothelial density, and endothelial cell counts were performed using ImageJ.

### Immunohistochemistry and histology

Immediately following mouse euthanasia, eyes were enucleated and the sclera/retina was punctured to facilitate fixation by immersion in 4% paraformaldehyde/PBS at 4°C. After 2 hr of fixation, the cornea was excised at the limbal boundary, paraffin embedded using standard protocols, and sectioned at 10 μm. For COL8A2 immunostaining, we used avidin-biotin-based detection (Vector Lab Elite ABC kit, Burlingame, CA) with 5 µg/ml rabbit anti-COL8A2 polyclonal antibody (PA5-35077; Thermo Fisher Scientific). 5 µg/ml rabbit IgG was used as an isotype control (02–6102; Thermo Fisher Scientific). After developing with DAB (Vector Lab) and counter-staining with Nuclear Fast Red (Vector Lab), x20 magnified images were obtained with a light microscope (EVOS FL Auto Cell Imaging System; Thermo Fisher Scientific). The intensity of staining was measured by Image J. Briefly, after the color images were converted to the gray scale images, the mean of intensity in corneal epithelium and corneal endothelium was quantified. To compensate for background, the staining intensity in the isotype control was subtracted from each result.

Masson’s trichrome and Periodic Acid-Schiff (PAS) stainings were performed using Trichrome Stain Kit (Masson, HT15; Sigma-Aldrich, St Louis, MO) and PAS Kit (395B; Sigma-Aldrich), respectively. For corneal endothelial cell density, the whole cornea was fixed with acetone for 1 hr. This and all subsequent washes and incubations were performed at room temperature. After four washes with PBS, the cornea was blocked for 1 hr (3% bovine serum albumin/PBS) and incubated for a further hour with 2.5 µg/ml Alexa Fluor 488 conjugated to anti-ZO1 antibody (339188; Thermo Fisher Scientific). After four final PBS washes, corneas were mounted on glass slides, endothelial side up, and imaged by confocal microscopy (Olympus FluoView FV1000). Corneal endothelial density was calculated manually by counting the number of corneal endothelial cells in three different areas of each cornea.

For immunostaining on corneal cryosections, we used rat anti-TNFα antibody (clone MP6-XT22; BioLegend, San Diego, CA) and rat anti-IFNγ (clone XMG1.2; BioLegend). As a control, we used isotype antibody (RTK2071; BioLegend). Briefly, the sections were blocked with 5% goat serum, 0.02% triton X-100/PBS for 30 min at room temperature. Then, the sections were stained with antibodies at 5 μg/ml for 1 hr at room temperature. After washing with PBS, the sections were stained with Alexa Fluor 647-conjugated goat anti-rat IgG (H + L) antibody (A-21247; Thermo Fisher Scientific). After DAPI staining, the fluorescence was observed with EVOS microscope.

### Electroretinography

C57BL6J mice were injected with Ad-GFP (anterior chamber injection), Ad-Cas9-Col8a2gRNA (anterior chamber injection), or 1 μg concanavalin A (intravitreal injection) (Sigma-Aldrich). The mice were examined with ERG for retinal function safety at 0 (prior to injection), 2, and 4 weeks. Mice were dark-adapted overnight before the experiments and anesthetized with an intraperitoneal injection of tribromoethanol and 2-methyl-2-butanol diluted in physiological saline at 14.5 ml/kg dose. The pupils were dilated with tropicamide (0.5%) and phenylephrine (2.5%) eye drops. ERG experiments were performed with a Ganzfeld ERG (Phoenix Laboratories, Pleasanton, CA). Scotopic combined response was obtained under dark-adapted conditions (no background illumination, 0 cd/m2) using white-flash stimuli ranging from −1.7 to 1.0 log cd s/m2 with 20 responses averaged for each stimulus.

### Alizarin red staining

Alizarin red staining for corneal endothelium was performed according to previously published methods (Taylor and Hunt, 1981). After euthanizing mice, corneas were harvested and washed twice with saline (0.9% NaCl) prior to a 2 min immersion in 0.2% Alizarin red solution (pH 4.2 adjusted by 0.1% NH4OH, in saline). After washing twice again with saline, corneas were fixed with acetone for 10 min and again washed in saline three times (10 min each). Corneas were mounted on glass slides and imaged with a bright-field microscope.

### Corneal swelling/de-swelling experiment

Mice were anesthetized with ketamine/xylazine. Imaged corneas were kept moist with Dulbecco’s phosphate-buffered saline (DPBS), excess DPBS was removed with absorbent tissue, while the contralateral eye was covered with an ointment to prevent dehydration. Corneal OCT images were taken before scraping and before treatment. The corneal epithelium was removed mechanically using a Tooke corneal knife (Novo Surgical Inc, Oak Brook, IL) and jeweler’s forceps (Figure 10a). This process takes about 5 min. For testing the corneal swelling response to different osmolalities of DPBS solution, we sequentially applied solutions at 5 min intervals, beginning with 0 mOsm/l (deionized water) to 900 mOsm/l DPBS, completely covering the eye throughout the course of each application. Each application required 1–2 min for image acquisition with OCT, which was performed immediately after removing the residual solution with a clean absorbent paper. To analyze corneal de-swelling, the cornea was fully covered with 650 mOsm/l DPBS for 10 min. After removing excess solution with a clean filter paper, 4 µl of silicone oil was applied to avoid evaporation from the corneal surface. Corneal and OCT images commenced at 5, 10, 20, 30, 40, and 50 min after the application of DPBS.

### Statistical analysis

Student’s t-test was used for comparison of averages accompanied with analysis of variance (ANOVA) for multiple group comparisons. To compare the slopes of central corneal thickness trajectory, we employed linear mixed-effects regression approach among groups of C57BL/6J, non-injected Col8a2Q455K/Q455K, and Ad-Cas9-Col8a2gRNA-injected Col8a2Q455K/Q455K mice. Random-effect component in the regression approach was used to account for the correlation among repeated measurements within each mouse. The regression analyses were performed using statistical software R at a significance level of 0.05.
