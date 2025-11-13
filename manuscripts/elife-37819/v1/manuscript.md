# An assay for de novo kinetochore assembly reveals a key role for the CENP-T pathway in budding yeast

## Authors

- Jackie Lang<sup>1</sup>
- Adrienne Barber<sup>1</sup>
- Sue Biggins<sup>1</sup> ([ORCID: 0000-0002-4499-6319](https://orcid.org/0000-0002-4499-6319)) †

### Affiliations

1. Division of Basic Sciences Howard Hughes Medical Institute, Fred Hutchinson Cancer Research Center Seattle United States
2. Molecular and Cellular Biology Program University of Washington Seattle United States

† Corresponding author

## Abstract

Chromosome segregation depends on the kinetochore, the machine that establishes force-bearing attachments between DNA and spindle microtubules. Kinetochores are formed every cell cycle via a highly regulated process that requires coordinated assembly of multiple subcomplexes on specialized chromatin. To elucidate the underlying mechanisms, we developed an assay to assemble kinetochores de novo using centromeric DNA and budding yeast extracts. Assembly is enhanced by mitotic phosphorylation of the Dsn1 kinetochore protein and generates kinetochores capable of binding microtubules. We used this assay to investigate why kinetochores recruit the microtubule-binding Ndc80 complex via two receptors: the Mis12 complex and CENP-T. Although the CENP-T pathway is non-essential in yeast, we demonstrate that it becomes essential for viability and Ndc80c recruitment when the Mis12 pathway is crippled by defects in Dsn1 phosphorylation. Assembling kinetochores de novo in yeast extracts provides a powerful and genetically tractable method to elucidate critical regulatory events in the future.

## Introduction

Chromosomes must be accurately segregated to daughter cells during cell division to avoid aneuploidy, a hallmark of birth defects and cancers (Pfau and Amon, 2012). Faithful segregation relies on the attachment of chromosomes to spindle microtubules via the kinetochore, a conserved protein complex that assembles at centromeres (Yamagishi et al., 2014; Musacchio and Desai, 2017). Kinetochores must track dynamically growing and shrinking microtubule tips, monitor for erroneous kinetochore-microtubule attachments, and serve as the platform for the spindle assembly checkpoint (Biggins, 2013; Joglekar and Kukreja, 2017). To carry out these many functions, the kinetochore is a highly regulated, megadalton protein structure composed of many subcomplexes (Figure 1A). Although these subcomplexes must faithfully assemble onto the centromere every cell cycle, the underlying mechanisms that regulate kinetochore assembly are not well understood.

![Figure 1.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig1-v1.jpg)

**Figure 1.:** (A) A schematic of the budding yeast kinetochore. Inner kinetochore subcomplexes assemble onto centromeres, serving as the platform for outer kinetochore recruitment. The listed subcomplexes are ordered based on physical interactions, and the yeast proteins in each kinetochore subcomplex are shown on the right. (B) DNA templates for the assembly assay. The templates include 500 bp from the E. coli ampC gene that encodes for β-lactamase (green) as a negative control, the 117 bp chromosome III centromere (CEN3), or a mutant CEN3 (CEN3mut) containing three point mutations in the CBF3 binding site (red ‘X’). The three Centromere-Determining Elements (CDEs) are indicated and ~70 bp of flanking pericentromeric DNA on either side is shown (grey). The DNA templates also contain linker DNA (purple) before the biotinylation (red star) at the 3’ end of the centromere. (C) Kinetochores assembled in vitro are centromere-specific and span the entire kinetochore. The indicated DNA templates were incubated in WT whole cell extracts prepared from a CNN1-3V5 DSN1-3Flag DAM1-9myc strain (SBY17228) for the indicated time (min). DNA-bound proteins were analyzed by immunoblotting with the indicated antibodies. Extracts are shown in Figure 1—figure supplement 1. (D) Kinetochore assembly is inhibited in an ndc10-1 temperature sensitive mutant. Extracts from a DSN1-6His-3Flag strain (SBY8253) or a DSN1-6His-3Flag ndc10-1 strain (SBY8361) shifted to the non-permissive temperature were used for assembly assays. DNA-bound proteins were analyzed by immunoblotting with the indicated antibodies. Extracts in Figure 1—figure supplement 2.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig1-figsupp1-v1.jpg)

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig1-figsupp2-v1.jpg)

Kinetochores are built on a specialized centromeric chromatin structure, in which canonical histone H3 is replaced with a centromere-specific variant, CENP-A (Earnshaw and Rothfield, 1985; Salmon and Bloom, 2017). Most eukaryotes have complex ‘regional’ centromeres composed of repetitive DNA stretches with interspersed CENP-A- and H3-containing nucleosomes (Blower et al., 2002). The constitutive centromere-associated network (CCAN) binds to centromeric chromatin to form the inner kinetochore and serve as the scaffold for outer kinetochore assembly, which mediates microtubule attachment (Foltz et al., 2006). The Ndc80 complex (‘Ndc80c’) is a key microtubule-binding site within the kinetochore, because it directly mediates attachment and recruits additional attachment factors, such as the Ska complex in vertebrates and its functional ortholog Dam1 in fungi (Cheeseman et al., 2006; DeLuca et al., 2005; Maure et al., 2011; Zhang et al., 2017; Lampert et al., 2013). Interestingly, there are two parallel kinetochore receptors for Ndc80c: the Mis12 complex (‘Mis12c’) and CENP-T (Maskell et al., 2010; Malvezzi et al., 2013; Schleiffer et al., 2012; Gascoigne et al., 2011; Nishino et al., 2013; Nishino et al., 2012). Mis12c interacts with the KNL1 and Ndc80 complexes to create a larger network called KMN (KNL1-Mis12-Ndc80) (Cheeseman et al., 2006). CENP-T, a histone-fold domain containing protein, recruits Ndc80c via the same interaction surface on the Ndc80 complex that binds Mis12c (Nishino et al., 2013; Schleiffer et al., 2012; Malvezzi et al., 2013; Hori et al., 2008; Dimitrova et al., 2016). Although Mis12c and CENP-T each contribute to Ndc80c recruitment in vivo (Malvezzi et al., 2013; Gascoigne et al., 2011), it has been unclear why cells employ two competing receptors for Ndc80c and whether the CENP-T protein functions as a histone at centromeres.

Substantial progress in understanding kinetochore assembly has been made using reconstitution systems in vitro. For example, pre-formed nucleosomal arrays incubated in Xenopus egg extracts assemble microtubule-binding elements that allowed the identification of events required to initiate kinetochore assembly (Guse et al., 2011). Furthermore, the binding selectivity of some kinetochore proteins for CENP-A nucleosomes (over H3 nucleosomes) was recently determined by reconstituting the entire linkage between the CENP-A nucleosome and KMN (Weir et al., 2016). To identify additional events that regulate kinetochore assembly, we set out to develop a reconstitution system that combines the strengths of these previously developed methods with the added ability to genetically manipulate the system and maintain post-translational modifications. To do this, we used budding yeast because they have a simple ‘point’ centromere that is defined by a ~ 125 bp specific DNA sequence and a single microtubule attachment site per chromosome (Winey et al., 1995; Biggins, 2013). The kinetochore subcomplexes and functions are largely conserved, including the specialized chromatin structure containing CENP-ACse4 that serves as the platform for kinetochore assembly. Additionally, dual pathways for Ndc80 recruitment are used in yeast, although the CENP-T ortholog, Cnn1, is not essential for viability (Schleiffer et al., 2012; Bock et al., 2012). However, CENP-TCnn1 contributes to kinetochore function because mutants display increased chromosome loss, and the tethering of CENP-TCnn1 imparts partial stability to acentric minichromosomes via Ndc80 recruitment (Malvezzi et al., 2013; Bock et al., 2012). In yeast, CENP-TCnn1 localization to kinetochores peaks in mitosis as a result of phosphoregulation (Schleiffer et al., 2012; Bock et al., 2012), but it is unclear why its recruitment is cell cycle regulated and whether this affects the Mis12 pathway of Ndc80 recruitment.

Here, we develop a cell-free method to assemble complete kinetochores de novo using centromeric DNA and yeast extracts. We demonstrate that this assay has the same basic requirements as kinetochore assembly in vivo, including the need for the CENP-ACse4 chaperone HJURPScm3, suggesting the formation of a centromeric nucleosome. Conserved mitotic phosphorylation events of the Mis12 complex enhance kinetochore assembly, revealing that the assay is sensitive to key post-translational modifications. Furthermore, this method generates kinetochores that exhibit microtubule-binding activity and employ both Ndc80 recruitment pathways. We applied this assay to identify the requirements for CENP-TCnn1 assembly and find that it requires all other inner kinetochore subcomplexes, suggesting it does not have independent DNA-binding activity. Furthermore, we discovered that the CENP-TCnn1 pathway is required for Ndc80 recruitment and cell viability when the Mis12 pathway is impaired by defects in conserved mitotic phosphoregulation (Akiyoshi et al., 2013a; Kim and Yu, 2015; Yang et al., 2008). Taken together, we have established a kinetochore assembly assay that identifies a critical function for the yeast CENP-TCnn1 pathway and that provides a powerful method to identify other key regulatory events required for kinetochore assembly and function in the future.

## Results

### Development of a method to assemble kinetochores de novo

Because we had previously identified conditions to purify functional kinetochores from yeast cells (Akiyoshi et al., 2010), we reasoned that these extracts might be permissive for de novo kinetochore assembly. To test this, we linked the chromosome III centromere (117 bp) and ~70 bp of pericentromeric DNA on each side (referred to as ‘CEN3’; Figure 1B) to beads via a biotin tag and incubated it in whole cell yeast extracts in the presence of excess non-specific competitive DNA. As negative controls, we used a template (CEN3mut) with mutations in the centromere determining element III (CDEIII) region of DNA that abolishes kinetochore assembly in vivo (Sorger et al., 1995; Lechner and Carbon, 1991) as well as a 500 bp DNA template from within the E. coli ampC gene. We optimized the extract conditions for assembly in vitro by altering the lysis buffer and method, most notably switching from potassium chloride to potassium glutamate, a salt utilized in other reconstitution assays (Seki and Diffley, 2000; Heller et al., 2011). The assembly reaction was initially performed using an extract prepared from asynchronously growing wildtype (WT) cells and analyzed by immunoblotting against representative components of most kinetochore subcomplexes. Within 30 min of assembly, every protein assayed bound specifically to centromeric DNA (Figure 1C). Inner kinetochore components are generally saturated within 30 min, while outer kinetochore proteins require longer to reach saturation. To compare the efficiency of assembly in various mutants and conditions, we analyzed assembly on CEN3 DNA at two time points hereafter.

To further analyze the composition of the assembled particles, we performed mass spectrometry. We detected 39 out of 49 core kinetochore proteins at higher coverage levels on CEN3 DNA relative to either ampC DNA or CEN3mut DNA (Table 1). In support of centromeric nucleosome assembly, CENP-ACse4 was specifically enriched on CEN3 DNA. Importantly, we detected components from all known kinetochore subcomplexes on CEN3 DNA, including the CENP-TCnn1 protein. The only proteins that were not detected are small proteins that are components of subcomplexes that were otherwise detected in the MS (for example, Dad2 in the Dam1 complex). Together, these data suggest that all kinetochore complexes assemble on centromeric DNA under the conditions we developed.

**Table 1.**
 Components from each of the core subcomplexes are detected on assembled kinetochores.Kinetochores were assembled on ampC, CEN3mut, or CEN3 DNA from an asynchronous WT DSN1-3Flag (SBY14441) extract and analyzed by LC/MS/MS mass spectrometry. The table indicates the human ortholog (if applicable) of each yeast protein, the percent coverage, and the number of unique and total peptides detected from each assembly. We included the only detected microtubule-associated protein.


<table>
  <thead>
    <tr>
      <th colspan="4">Table 1. WT assembled kinetochores</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>ampC</th>
      <th>ampC</th>
      <th>ampC</th>
      <th>CEN3mut</th>
      <th>CEN3mut</th>
      <th>CEN3mut</th>
      <th>CEN3</th>
      <th>CEN3</th>
      <th>CEN3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Subcomplex</td>
      <td>Yeast Protein</td>
      <td>Human Protein</td>
      <td>% Coverage</td>
      <td>Unique Peptides</td>
      <td>Total Peptides</td>
      <td>% Coverage</td>
      <td>Unique Peptides</td>
      <td>Total Peptides</td>
      <td>% Coverage</td>
      <td>Unique Peptides</td>
      <td>Total Peptides</td>
    </tr>
    <tr>
      <td></td>
      <td>CPC</td>
      <td>Ipl1</td>
      <td>Aurora B</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>23.7</td>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Sli15</td>
      <td>INCENP</td>
      <td>7</td>
      <td>2</td>
      <td>2</td>
      <td>14.8</td>
      <td>6</td>
      <td>7</td>
      <td>64.3</td>
      <td>54</td>
      <td>113</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Bir1</td>
      <td>Survivin</td>
      <td>15.1</td>
      <td>10</td>
      <td>11</td>
      <td>22.6</td>
      <td>14</td>
      <td>17</td>
      <td>59.2</td>
      <td>70</td>
      <td>177</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Nbl1</td>
      <td>Borealin</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>76.7</td>
      <td>6</td>
      <td>11</td>
    </tr>
    <tr>
      <td>CCAN</td>
      <td>Cbf1</td>
      <td>Cbf1</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>62.7</td>
      <td>30</td>
      <td>77</td>
      <td>59.3</td>
      <td>29</td>
      <td>60</td>
    </tr>
    <tr>
      <td></td>
      <td>Cbf3</td>
      <td>Ndc10</td>
      <td></td>
      <td>11.4</td>
      <td>7</td>
      <td>8</td>
      <td>32.9</td>
      <td>23</td>
      <td>26</td>
      <td>63.2</td>
      <td>78</td>
      <td>194</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cep3</td>
      <td></td>
      <td>3.5</td>
      <td>1</td>
      <td>2</td>
      <td>15.3</td>
      <td>8</td>
      <td>9</td>
      <td>34.2</td>
      <td>25</td>
      <td>76</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Ctf13</td>
      <td></td>
      <td>2.7</td>
      <td>1</td>
      <td>1</td>
      <td>18.4</td>
      <td>5</td>
      <td>5</td>
      <td>46</td>
      <td>22</td>
      <td>38</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Skp1</td>
      <td></td>
      <td>28.4</td>
      <td>3</td>
      <td>3</td>
      <td>19.6</td>
      <td>2</td>
      <td>2</td>
      <td>41.8</td>
      <td>12</td>
      <td>24</td>
    </tr>
    <tr>
      <td></td>
      <td>Nucleosome</td>
      <td>Cse4</td>
      <td>CENP-A</td>
      <td>13.1</td>
      <td>3</td>
      <td>3</td>
      <td>24.5</td>
      <td>6</td>
      <td>8</td>
      <td>49.8</td>
      <td>10</td>
      <td>31</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Hta2</td>
      <td>H2A</td>
      <td>35.6</td>
      <td>7</td>
      <td>20</td>
      <td>35.6</td>
      <td>5</td>
      <td>13</td>
      <td>35.6</td>
      <td>6</td>
      <td>19</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Htb2</td>
      <td>H2B</td>
      <td>45</td>
      <td>8</td>
      <td>18</td>
      <td>39.7</td>
      <td>7</td>
      <td>29</td>
      <td>39.7</td>
      <td>7</td>
      <td>29</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Hht1</td>
      <td>H3</td>
      <td>5.1</td>
      <td>1</td>
      <td>1</td>
      <td>5.1</td>
      <td>1</td>
      <td>1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Hhf1</td>
      <td>H4</td>
      <td>45.6</td>
      <td>7</td>
      <td>11</td>
      <td>56.3</td>
      <td>8</td>
      <td>19</td>
      <td>46.6</td>
      <td>8</td>
      <td>13</td>
    </tr>
    <tr>
      <td></td>
      <td>Nucleosome</td>
      <td>Psh1</td>
      <td></td>
      <td>3.9</td>
      <td>1</td>
      <td>1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Associated</td>
      <td>Scm3</td>
      <td>HJURP</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>6.3</td>
      <td>1</td>
      <td>1</td>
      <td>28.3</td>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <td></td>
      <td>Mif2</td>
      <td>Mif2</td>
      <td>CENP-C</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>9.7</td>
      <td>4</td>
      <td>4</td>
      <td>58.7</td>
      <td>29</td>
      <td>39</td>
    </tr>
    <tr>
      <td></td>
      <td>OA</td>
      <td>Okp1</td>
      <td>CENP-Q</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>20.9</td>
      <td>7</td>
      <td>9</td>
      <td>42.6</td>
      <td>21</td>
      <td>34</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Ame1</td>
      <td>CENP-U</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>20.4</td>
      <td>5</td>
      <td>6</td>
      <td>61.4</td>
      <td>22</td>
      <td>41</td>
    </tr>
    <tr>
      <td></td>
      <td>CM</td>
      <td>Ctf19</td>
      <td>CENP-P</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>6.8</td>
      <td>2</td>
      <td>2</td>
      <td>44.7</td>
      <td>21</td>
      <td>31</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Mcm21</td>
      <td>CENP-O</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>10.3</td>
      <td>3</td>
      <td>4</td>
      <td>65.8</td>
      <td>26</td>
      <td>39</td>
    </tr>
    <tr>
      <td></td>
      <td>Iml3</td>
      <td>Iml3</td>
      <td>CENP-L</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>60.8</td>
      <td>13</td>
      <td>19</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Chl4</td>
      <td>CENP-N</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>7.9</td>
      <td>3</td>
      <td>3</td>
      <td>37.1</td>
      <td>16</td>
      <td>19</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Nkp1</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>26.9</td>
      <td>4</td>
      <td>6</td>
      <td>57.6</td>
      <td>17</td>
      <td>28</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Nkp2</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>15</td>
      <td>2</td>
      <td>4</td>
      <td>55.6</td>
      <td>7</td>
      <td>10</td>
    </tr>
    <tr>
      <td></td>
      <td>Ctf3</td>
      <td>Mcm16</td>
      <td>CENP-H</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>22.7</td>
      <td>2</td>
      <td>3</td>
      <td>48.6</td>
      <td>7</td>
      <td>11</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Ctf3</td>
      <td>CENP-I</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>5.3</td>
      <td>3</td>
      <td>3</td>
      <td>23.7</td>
      <td>17</td>
      <td>27</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Mcm22</td>
      <td>CENP-K</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>25.5</td>
      <td>3</td>
      <td>4</td>
      <td>81.6</td>
      <td>18</td>
      <td>27</td>
    </tr>
    <tr>
      <td></td>
      <td>Cnn1</td>
      <td>Cnn1</td>
      <td>CENP-T</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>45.7</td>
      <td>13</td>
      <td>18</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Wip1</td>
      <td>CENP-W</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>39.3</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Mhf1</td>
      <td>CENP-S</td>
      <td>48.9</td>
      <td>4</td>
      <td>4</td>
      <td>48.9</td>
      <td>3</td>
      <td>7</td>
      <td>40</td>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Mhf2</td>
      <td>CENP-X</td>
      <td>43.8</td>
      <td>4</td>
      <td>8</td>
      <td>47.5</td>
      <td>4</td>
      <td>6</td>
      <td>28.8</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Outer Kt</td>
      <td>Mtw1</td>
      <td>Mtw1</td>
      <td>Mis12</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>22.8</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Nnf1</td>
      <td>PMF1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>13.9</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Nsl1</td>
      <td>Nsl1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>24.1</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Dsn1</td>
      <td>Dsn1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>7.3</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>Ndc80</td>
      <td>Ndc80</td>
      <td>HEC1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>28.4</td>
      <td>15</td>
      <td>16</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Nuf2</td>
      <td>NUF2</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>32.8</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Spc24</td>
      <td>SPC24</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>57.3</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Spc25</td>
      <td>SPC25</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>27.1</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <td></td>
      <td>Spc105</td>
      <td>Spc105</td>
      <td>KNL1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Kre28</td>
      <td>Zwint1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Dam1</td>
      <td>Dam1</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>10.8</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Dad1</td>
      <td></td>
      <td>26.6</td>
      <td>1</td>
      <td>1</td>
      <td>26.6</td>
      <td>1</td>
      <td>2</td>
      <td>26.6</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Dad3</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Ask1</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>8.2</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Duo1</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>7.3</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Hsk3</td>
      <td></td>
      <td>15.9</td>
      <td>1</td>
      <td>1</td>
      <td>15.9</td>
      <td>1</td>
      <td>1</td>
      <td>15.9</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Spc19</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>8.5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Spc34</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>4.7</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Dad2</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Dad4</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>MAPs</td>
      <td>Stu2</td>
      <td>CHTOG</td>
      <td>3.5</td>
      <td>2</td>
      <td>2</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

We next asked whether the assembly assay reflected requirements in vivo. Kinetochore assembly is initiated by the binding of the CBF3 complex to CDEIII, which facilitates the deposition of CENP-ACse4 (Poddar et al., 2004; Camahort et al., 2007). All kinetochore proteins except Cbf1, which binds directly to CDEI, require the Ndc10 component of the CBF3 complex for their localization in vivo (He et al., 2000). We therefore tested the requirement for CBF3 by performing the assembly assay with extracts prepared from WT cells and an ndc10-1 temperature sensitive mutant. Similar to the negative controls, the assembly reaction was completely inhibited on the CEN3 DNA in the ndc10-1 extracts (Figure 1D). Together, these data indicate that the assembly reaction is initiated by CBF3, consistent with the requirements for assembly in vivo.

### Kinetochores assemble on a single CENP-A nucleosome

Kinetochore assembly in vivo requires a CENP-A nucleosome, so we tested whether CENP-ACse4 requires its chaperone HJURPScm3 for deposition (Camahort et al., 2007; Shivaraju et al., 2011; Stoler et al., 2007). To do this, we generated cells containing an auxin-inducible degron (AID) allele of SCM3, scm3-AID, which targets the protein for proteasomal degradation when the TIR1 F-box protein and the hormone auxin are present (Nishimura et al., 2009). Although we could not detect HJURPScm3 protein in extracts due to low intracellular levels, we concluded that the protein was degraded because the cells were inviable when plated on auxin (Figure 2—figure supplement 1). We prepared extracts from scm3-AID strains (with or without TIR1) treated with auxin and performed the assembly assay (Figure 2A). As expected for the most upstream protein in the assembly pathway, Ndc10 associated with CEN3 DNA in the presence or absence of HJURPScm3. However, CENP-ACse4 and all other CCAN components assayed no longer associated with CEN3 when HJURPScm3 was depleted (Figure 2A). This strict requirement for CENP-ACse4 recruitment by its chaperone suggests that CENP-ACse4 is forming a functional nucleosome in vitro.

![Figure 2.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig2-v1.jpg)

**Figure 2.:** (A) Degradation of HJURPScm3 blocks assembly of the kinetochore beginning with CENP-ACse4. A DSN1-3Flag scm3-EGFP-AID strain (SBY16440) and a DSN1-3Flag scm3-EGFP-AID OsTIR1-myc strain (SBY16438) were treated with auxin and the extracts were used for assembly assays. DNA-bound proteins were analyzed by immunoblotting for the indicated proteins. Extracts in Figure 2—figure supplement 2. (B) Assembly on a centromeric DNA template of only 180 bp is similar to a 250 bp template. Extract from a DSN1-3Flag CNN1-3V5 DAM1-9myc (SBY17228) strain was used for assembly assays with the indicated DNA templates. DNA-bound proteins were analyzed by immunoblotting with the indicated antibodies. Extracts in Figure 2—figure supplement 3.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** The Scm3-AID protein is degraded in the presence of both auxin and OsTIR1, resulting in lethality. Saturated cultures were serial diluted and plated on the indicated media. The strains used are WT (SBY4), DSN1-3Flag (SBY14441), DSN1-3Flag scm3-EGFP-AID (SBY16440), and DSN1-3Flag scm3-EGFP-AID OsTIR1-myc (SBY16438).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig2-figsupp2-v1.jpg)

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig2-figsupp3-v1.jpg)

Centromeric nucleosomes can be detected in the surrounding pericentromeric region in vivo (Coffman et al., 2011; Lawrimore et al., 2011; Wisniewski et al., 2014), leading to debate about whether a single CENP-ACse4 nucleosome is sufficient for kinetochore assembly (Aravamudhan et al., 2013; Furuyama and Biggins, 2007; Wisniewski et al., 2014). We therefore performed the assembly assay using a shorter 180 bp template that cannot form more than one octameric nucleosome. CENP-ACse4 levels were similar on both templates, and the entire kinetochore formed in both cases (Figure 2B). Together, these data suggest that a single, well-positioned centromeric nucleosome is sufficient for kinetochore assembly in the absence of surrounding pericentromeric DNA.

### Assembly in vitro is regulated by the cell cycle and phosphorylation

Kinetochore assembly is regulated during the cell cycle and occurs during S phase in budding yeast (Kitamura et al., 2007; Pearson et al., 2004), although it isn’t clear whether this reflects a requirement for active DNA replication or another S phase event. During mitosis, there are dynamic changes in kinetochore composition and CENP-TCnn1 levels at kinetochores peak due to phosphoregulation (Schleiffer et al., 2012; Bock et al., 2012; Dhatchinamoorthy et al., 2017). To test whether the assembly assay is subject to cell cycle regulation, WT cells were grown asynchronously or arrested in G1, S phase, or mitosis, and the extracts were used for in vitro assembly assays. Assembly is least efficient in extracts from cells arrested in G1 and most efficient in S phase and mitosis (Figure 3A), consistent with cell cycle regulation that occurs in vivo. As expected, the CENP-TCnn1 pathway is noticeably enhanced in kinetochores assembled from mitotic extracts. The cellular levels of some proteins, particularly CENP-TCnn1 and CENP-CMif2, are different in the various arrests and it is not clear whether this is due to changes in expression level or solubility. We also note that there appears to be a preference for the assembly of slower-migrating forms of CENP-CMif2 during S phase and mitosis, which may reflect post-translational modifications.

![Figure 3.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig3-v1.jpg)

**Figure 3.:** (A) Assembly in vitro is most efficient in extracts made from mitotically arrested cells. Kinetochores were assembled using extract from WT cells (DSN1-3Flag CNN1-3V5 DAM1-9myc (SBY17227)) that were either asynchronously growing or arrested in G1 (with alpha factor), S phase (with hydroxyurea), or early mitosis (with benomyl). Diluted whole cell extracts (left) and DNA-bound proteins (right) were analyzed by immunoblotting with the indicated antibodies. (B) Outer kinetochore assembly is enhanced in dsn1-2D extracts. Assembly assays were performed using extracts prepared from benomyl-arrested DSN1-3Flag CNN1-3V5 DAM1-9myc (SBY17228) and dsn1-2D-3Flag CNN1-3V5 DAM1-9myc (SBY17234) strains on the indicated DNA templates. DNA-bound proteins were analyzed by immunoblotting with the indicated antibodies. Extracts in Figure 3—figure supplement 1. (C) dsn1-2D enhances the assembly of most outer kinetochore proteins by at least 5-fold. Assembly assays were performed using extracts from DSN1-3Flag (SBY14441) and dsn1-2D-3Flag (SBY14151) on CEN3 DNA. Assembled proteins were labeled with tandem mass tags and analyzed by quantitative mass spectrometry. For each protein, the relative abundance in dsn1-2D assembled kinetochores was divided by the relative abundance in WT to calculate the fold enrichment in the dsn1-2D assembled kinetochores.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig3-figsupp1-v1.jpg)

A conserved mitotic phosphorylation event that promotes kinetochore assembly is Aurora B-mediated phosphorylation of Dsn1, which promotes the interaction between Mis12c and the inner kinetochore protein CENP-CMif2 (Akiyoshi et al., 2013a; Kim and Yu, 2015; Yang et al., 2008; Dimitrova et al., 2016; Petrovic et al., 2016). To test the effects of this phosphorylation on kinetochore assembly in vitro, we made extracts made from a dsn1-S240D, S250D (dsn1-2D) phosphomimetic mutant (Akiyoshi et al., 2013a). While the innermost CCAN proteins were present at equivalent levels, the dsn1-2D assembled kinetochores showed a strong enrichment for outer kinetochore proteins beginning with the Mis12 complex itself when assayed by immunoblotting and mass spectrometry (Figure 3B and Table 2). To directly quantify the difference between WT and dsn1-2D assembly reactions, we performed quantitative mass spectrometry (qMS) using tandem mass tag labeling (McAlister et al., 2014). Although the qMS data does not allow us to analyze the stoichiometry of components within one sample, we were able to compare relative protein levels between WT and dsn1-2D assembled kinetochores. Similar to the immunoblot analysis, there was a strong enrichment of outer kinetochore proteins (3- to 7-fold enrichment) in the dsn1-2D assembled kinetochores while the CCAN levels were similar to WT assembled kinetochores (Figure 3C). Together, these data indicate that our assembly assay in vitro reflects requirements known for assembly in vivo and is sensitive to critical post-translational modifications.

**Table 2.**
 Outer kinetochore assembly is enhanced by Dsn1 phosphorylation.Kinetochores were assembled on the indicated DNA templates from an asynchronous dsn1-2D-3Flag (SBY14151) extract and analyzed by mass spectrometry as in Table 1. We included the detected microtubule-associated proteins.


<table>
  <thead>
    <tr>
      <th colspan="4">Table 2. dsn1-2D assembled kinetochores</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>ampC</th>
      <th>ampC</th>
      <th>ampC</th>
      <th>CEN3mut</th>
      <th>CEN3mut</th>
      <th>CEN3mut</th>
      <th>CEN3</th>
      <th>CEN3</th>
      <th>CEN3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Subcomplex</td>
      <td>Yeast Protein</td>
      <td>Human Protein</td>
      <td>% Coverage</td>
      <td>Unique Peptides</td>
      <td>Total Peptides</td>
      <td>% Coverage</td>
      <td>Unique Peptides</td>
      <td>Total Peptides</td>
      <td>% Coverage</td>
      <td>Unique Peptides</td>
      <td>Total Peptides</td>
    </tr>
    <tr>
      <td></td>
      <td>CPC</td>
      <td>Ipl1</td>
      <td>Aurora B</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>24.5</td>
      <td>9</td>
      <td>15</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Sli15</td>
      <td>INCENP</td>
      <td>11</td>
      <td>4</td>
      <td>5</td>
      <td>21.9</td>
      <td>10</td>
      <td>11</td>
      <td>62.6</td>
      <td>61</td>
      <td>221</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Bir1</td>
      <td>Survivin</td>
      <td>20.2</td>
      <td>13</td>
      <td>15</td>
      <td>25.5</td>
      <td>17</td>
      <td>20</td>
      <td>64.3</td>
      <td>71</td>
      <td>257</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Nbl1</td>
      <td>Borealin</td>
      <td>23.3</td>
      <td>1</td>
      <td>1</td>
      <td>21.9</td>
      <td>1</td>
      <td>1</td>
      <td>61.6</td>
      <td>7</td>
      <td>19</td>
    </tr>
    <tr>
      <td>CCAN</td>
      <td>Cbf1</td>
      <td>Cbf1</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>65</td>
      <td>27</td>
      <td>53</td>
      <td>59.3</td>
      <td>30</td>
      <td>92</td>
    </tr>
    <tr>
      <td></td>
      <td>Cbf3</td>
      <td>Ndc10</td>
      <td></td>
      <td>21.2</td>
      <td>2</td>
      <td>14</td>
      <td>24.5</td>
      <td>19</td>
      <td>22</td>
      <td>58.9</td>
      <td>68</td>
      <td>563</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Cep3</td>
      <td></td>
      <td>20.6</td>
      <td>8</td>
      <td>9</td>
      <td>15.3</td>
      <td>8</td>
      <td>10</td>
      <td>34.5</td>
      <td>21</td>
      <td>111</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Ctf13</td>
      <td></td>
      <td>2.7</td>
      <td>1</td>
      <td>1</td>
      <td>12.3</td>
      <td>5</td>
      <td>5</td>
      <td>40.6</td>
      <td>21</td>
      <td>71</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Skp1</td>
      <td></td>
      <td>8.8</td>
      <td>1</td>
      <td>2</td>
      <td>22.2</td>
      <td>3</td>
      <td>3</td>
      <td>44.3</td>
      <td>11</td>
      <td>32</td>
    </tr>
    <tr>
      <td></td>
      <td>Nucleosome</td>
      <td>Cse4</td>
      <td>CENP-A</td>
      <td>20.5</td>
      <td>5</td>
      <td>5</td>
      <td>14</td>
      <td>4</td>
      <td>6</td>
      <td>49.3</td>
      <td>10</td>
      <td>34</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Hta2</td>
      <td>H2A</td>
      <td>35.6</td>
      <td>5</td>
      <td>13</td>
      <td>35.6</td>
      <td>7</td>
      <td>20</td>
      <td>35.6</td>
      <td>5</td>
      <td>34</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Htb2</td>
      <td>H2B</td>
      <td>39.7</td>
      <td>7</td>
      <td>18</td>
      <td>39.7</td>
      <td>7</td>
      <td>31</td>
      <td>31.3</td>
      <td>6</td>
      <td>29</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Hht1</td>
      <td>H3</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>5.1</td>
      <td>1</td>
      <td>1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Hhf1</td>
      <td>H4</td>
      <td>56.3</td>
      <td>9</td>
      <td>11</td>
      <td>56.3</td>
      <td>8</td>
      <td>16</td>
      <td>55.3</td>
      <td>8</td>
      <td>22</td>
    </tr>
    <tr>
      <td></td>
      <td>Nucleosome Associated</td>
      <td>Psh1</td>
      <td></td>
      <td>7.4</td>
      <td>2</td>
      <td>2</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Scm3</td>
      <td>HJURP</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>30.5</td>
      <td>8</td>
      <td>17</td>
    </tr>
    <tr>
      <td></td>
      <td>Mif2</td>
      <td>Mif2</td>
      <td>CENP-C</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>13.7</td>
      <td>5</td>
      <td>5</td>
      <td>55.7</td>
      <td>27</td>
      <td>54</td>
    </tr>
    <tr>
      <td></td>
      <td>OA</td>
      <td>Okp1</td>
      <td>CENP-Q</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>22.7</td>
      <td>8</td>
      <td>9</td>
      <td>43.6</td>
      <td>21</td>
      <td>50</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Ame1</td>
      <td>CENP-U</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>28.7</td>
      <td>5</td>
      <td>5</td>
      <td>54.9</td>
      <td>19</td>
      <td>43</td>
    </tr>
    <tr>
      <td></td>
      <td>CM</td>
      <td>Ctf19</td>
      <td>CENP-P</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>9.8</td>
      <td>3</td>
      <td>3</td>
      <td>42.3</td>
      <td>17</td>
      <td>41</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Mcm21</td>
      <td>CENP-O</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>25.8</td>
      <td>7</td>
      <td>8</td>
      <td>48.6</td>
      <td>23</td>
      <td>42</td>
    </tr>
    <tr>
      <td></td>
      <td>Iml3</td>
      <td>Iml3</td>
      <td>CENP-L</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>15.5</td>
      <td>3</td>
      <td>3</td>
      <td>60.8</td>
      <td>13</td>
      <td>28</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Chl4</td>
      <td>CENP-N</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>7.2</td>
      <td>3</td>
      <td>3</td>
      <td>29</td>
      <td>12</td>
      <td>21</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Nkp1</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>26.5</td>
      <td>4</td>
      <td>6</td>
      <td>58</td>
      <td>18</td>
      <td>35</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Nkp2</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>15</td>
      <td>2</td>
      <td>3</td>
      <td>35.9</td>
      <td>5</td>
      <td>14</td>
    </tr>
    <tr>
      <td></td>
      <td>Ctf3</td>
      <td>Mcm16</td>
      <td>CENP-H</td>
      <td>14.9</td>
      <td>1</td>
      <td>1</td>
      <td>19.9</td>
      <td>2</td>
      <td>2</td>
      <td>44.8</td>
      <td>6</td>
      <td>12</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Ctf3</td>
      <td>CENP-I</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>13.9</td>
      <td>12</td>
      <td>19</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Mcm22</td>
      <td>CENP-K</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>14.6</td>
      <td>2</td>
      <td>2</td>
      <td>74.9</td>
      <td>17</td>
      <td>34</td>
    </tr>
    <tr>
      <td></td>
      <td>Cnn1</td>
      <td>Cnn1</td>
      <td>CENP-T</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>27.1</td>
      <td>8</td>
      <td>11</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Wip1</td>
      <td>CENP-W</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>21.1</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Mhf1</td>
      <td>CENP-S</td>
      <td>48.9</td>
      <td>3</td>
      <td>4</td>
      <td>48.9</td>
      <td>4</td>
      <td>9</td>
      <td>21.1</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Mhf2</td>
      <td>CENP-X</td>
      <td>62.5</td>
      <td>7</td>
      <td>8</td>
      <td>47.5</td>
      <td>4</td>
      <td>4</td>
      <td>28.8</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Outer KT</td>
      <td>Mtw1</td>
      <td>Mtw1</td>
      <td>Mis12</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>18.7</td>
      <td>4</td>
      <td>4</td>
      <td>48.1</td>
      <td>13</td>
      <td>21</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Nnf1</td>
      <td>PMF1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>16.9</td>
      <td>2</td>
      <td>2</td>
      <td>30.3</td>
      <td>10</td>
      <td>13</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Nsl1</td>
      <td>Nsl1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>15.3</td>
      <td>2</td>
      <td>2</td>
      <td>69</td>
      <td>15</td>
      <td>21</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Dsn1</td>
      <td>Dsn1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>13.4</td>
      <td>4</td>
      <td>4</td>
      <td>39.2</td>
      <td>21</td>
      <td>31</td>
    </tr>
    <tr>
      <td></td>
      <td>Ndc80</td>
      <td>Ndc80</td>
      <td>HEC1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>18.5</td>
      <td>8</td>
      <td>9</td>
      <td>56.4</td>
      <td>37</td>
      <td>63</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Nuf2</td>
      <td>NUF2</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>15.7</td>
      <td>6</td>
      <td>6</td>
      <td>51</td>
      <td>27</td>
      <td>42</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Spc24</td>
      <td>SPC24</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>38.5</td>
      <td>4</td>
      <td>5</td>
      <td>63.4</td>
      <td>12</td>
      <td>26</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Spc25</td>
      <td>SPC25</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>8.1</td>
      <td>1</td>
      <td>1</td>
      <td>37.6</td>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <td></td>
      <td>Spc105</td>
      <td>Spc105</td>
      <td>KNL1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>3.1</td>
      <td>2</td>
      <td>2</td>
      <td>45.9</td>
      <td>41</td>
      <td>60</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Kre28</td>
      <td>Zwint1</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>3.6</td>
      <td>1</td>
      <td>1</td>
      <td>7</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <td></td>
      <td>Dam1</td>
      <td>Dam1</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>21.6</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Dad1</td>
      <td></td>
      <td>26.6</td>
      <td>1</td>
      <td>1</td>
      <td>26.6</td>
      <td>1</td>
      <td>1</td>
      <td>37.2</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Dad3</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>29.8</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Ask1</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>21.2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Duo1</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>18.2</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Hsk3</td>
      <td></td>
      <td>15.9</td>
      <td>1</td>
      <td>1</td>
      <td>15.9</td>
      <td>1</td>
      <td>1</td>
      <td>15.9</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Spc19</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>30.3</td>
      <td>4</td>
      <td>6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Spc34</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>31.5</td>
      <td>6</td>
      <td>11</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Dad2</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Dad4</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>MAPs</td>
      <td>Stu2</td>
      <td>CHTOG</td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>33.6</td>
      <td>23</td>
      <td>31</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Bim1</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>17.7</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Slk19</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>1.6</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Bik1</td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>Not present</td>
      <td></td>
      <td></td>
      <td>10</td>
      <td>3</td>
      <td>4</td>
    </tr>
  </tbody>
</table>

### Assembled kinetochores are capable of binding microtubules

One of the most fundamental activities of the kinetochore is microtubule binding, so we next tested whether the assembled kinetochores are competent to attach to microtubules. We assembled kinetochores in extracts made from dsn1-2D cells, as well as extracts depleted of the major microtubule-binding component Ndc80 as a control (Cheeseman et al., 2006; DeLuca et al., 2005). Because the Chromosomal Passenger Complex (CPC) can mediate microtubule binding when bound to centromeric DNA in vitro (Sandall et al., 2006), we also performed the experiment in extracts depleted of INCENPSli15, the CPC scaffold protein (Jeyaprakash et al., 2007; Carmena et al., 2012). Although the AID-tagged proteins were significantly depleted from cells after auxin addition (Figure 4A), low levels of Ndc80 remained that were capable of assembling in vitro (Figure 4B). However, the residual levels were not sufficient for the proteins to perform their recruitment functions since Dam1 was absent in the ndc80-AID assembled kinetochores and Aurora BIpl1 was absent from the sli15-AID assembled kinetochores (Jeyaprakash et al., 2007; Klein et al., 2006; Lampert et al., 2013). We incubated the bead-bound assembled kinetochores with either taxol-stabilized microtubules or free tubulin as a negative control. The bound proteins were eluted from the beads and copurifying tubulin was analyzed by fluorescence. Microtubules bound much more robustly than free tubulin to the assembled dsn1-2D kinetochores (Figure 4B). Although the single mutants did not significantly alter microtubule binding, the double ndc80-AID sli15-AID mutant kinetochores were not able to bind microtubules. Thus, kinetochores assembled in vitro are capable of binding to microtubules through the established microtubule-binding interfaces.

![Figure 4.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig4-v1.jpg)

**Figure 4.:** (A) The Ndc80-3V5-AID and Sli15-3HA-AID proteins are degraded after one hour of auxin treatment as determined by immunoblotting of whole cell extracts. (B) Assembled kinetochores bind microtubules but not free tubulin. Assembly assays were performed using extracts from the following strains: dsn1-2D-3Flag DAM1-9myc OsTIR1 (SBY14343), dsn1-2D-3Flag DAM1-9myc OsTIR1 ndc80-3V5-AID (SBY14336), dsn1-2D-3Flag DAM1-9myc OsTIR1 sli15-3HA-AID (SBY14890), and dsn1-2D-3Flag DAM1-9myc OsTIR1 ndc80-3V5-AID sli15-3HA-AID (SBY17238). All strains were arrested in benomyl and treated with auxin before harvesting. The assembled kinetochores were then incubated with buffer, free tubulin, or taxol-stabilized microtubules. The free tubulin and the microtubules contained alexa-647-labeled tubulin. DNA-bound proteins were analyzed by immunoblotting with the indicated antibodies, and the tubulin and microtubules were analyzed by fluorescence imaging. The Ndc80-3V5-AID protein migrates slower than untagged Ndc80. Extracts and tubulin input in Figure 4—figure supplement 1.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Free tubulin and microtubule inputs are loaded at 1:5 and 1:20 of the amount introduced to assembled kinetochores.

### CENP-TCnn1 requires all CCAN proteins for kinetochore localization

A conserved feature of kinetochore assembly is the recruitment of Ndc80 via two complexes: Mis12c and CENP-TCnn1. The mechanism of CENP-TCnn1 recruitment to the kinetochore has been controversial. CENP-TCnn1 and its partner CENP-W have histone fold domains (HFD) and can tetramerize with two additional HFD proteins, CENP-S/X, to form a nucleosome-like structure in vitro (Nishino et al., 2012; Takeuchi et al., 2014; Schleiffer et al., 2012). The human proteins require their heterotetramerization and DNA-binding capabilities to assemble a functional kinetochore in vivo (Nishino et al., 2012), leading to the model that CENP-TCnn1 forms a unique centromeric chromatin structure. However, CENP-TCnn1 localization to kinetochores requires other CCAN proteins, suggesting it may not directly bind to centromeric DNA (Carroll et al., 2010; Basilico et al., 2014; Samejima et al., 2015; Suzuki et al., 2015; Pekgöz Altunkaya et al., 2016; Logsdon et al., 2015).

To address these issues, we used our DNA-based method to analyze the requirements for CENP-TCnn1 recruitment. The CCAN is composed of distinct subcomplexes and the physical interactions between them have been mapped using co-immunoprecipitation experiments (Schleiffer et al., 2012; Pekgöz Altunkaya et al., 2016) (Figure 1A). To map the CENP-TCnn1 assembly pathway on centromeric DNA, we performed the assembly assay from cells containing a representative mutant of each conserved CCAN subcomplex that had been arrested in mitosis. CENP-TCnn1 is absent or severely reduced in all inner kinetochore mutants tested (Figure 5A–C), indicating that CENP-TCnn1 does not have independent DNA-binding properties in our assay conditions. In addition, CENP-TCnn1 appears to be the most distal component of the CCAN because every other subcomplex is required for its kinetochore localization (Figure 5D) (Pekgöz Altunkaya et al., 2016).

![Figure 5.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig5-v1.jpg)

**Figure 5.:** (A–C) CENP-TCnn1 assembly occurs downstream of all other inner kinetochore components. Assembly assays were performed on the indicated DNA templates using extracts prepared from cells arrested in benomyl. The strains used in (A) were also shifted to the non-permissive temperature for three hours before harvesting: DSN1-3Flag CNN1-3V5 (SBY17230), DSN1-3Flag CNN1-3V5 cse4-323 (SBY17770), and DSN1-3Flag CNN1-3V5 mif2-3 (SBY17603). The strains used in (B) were treated with auxin for three hours before harvesting: DSN1-3Flag CNN1-3V5 (SBY17230), DSN1-3Flag CNN1-3V5 okp1-3V5-AID OsTIR1 (SBY17764), DSN1-3Flag CNN1-3V5 mcm22Δ (SBY17460), and DSN1-3Flag CNN1-3V5 chl4Δ (SBY17607). The strains used in (C) were benomyl treated only: DSN1-3Flag CNN1-3V5 (SBY17230) and DSN1-3Flag CNN1-3V5 mcm21Δ (SBY18304). (D) A schematic distinguishing the proteins involved in the CENP-TCnn1 and Mis12 recruitment pathways.

### Kinetochore assembly in vitro utilizes both pathways to Ndc80 recruitment

It has been unclear how CENP-TCnn1 facilitates kinetochore assembly in yeast, because Ndc80 levels are not noticeably reduced by the loss of CENP-TCnn1in vivo (Bock et al., 2012; Schleiffer et al., 2012). We therefore performed the assembly assay in a cnn1Δ extract and found that Ndc80 and KNL1Spc105 levels are slightly reduced, suggesting that CENP-TCnn1 contributes to Ndc80 recruitment (Figure 6). We next compared this to the role of Mis12c in Ndc80 recruitment by performing the assay in an extract from which dsn1-AID had been degraded. Here, Ndc80 assembly is considerably reduced but not absent. To test whether the residual Ndc80 is due to CENP-TCnn1, we analyzed assembly from a cnn1Δ dsn1-AID double mutant and found that Ndc80 recruitment is abolished. Together, these data show that the de novo assay uses both pathways of assembly and that CENP-TCnn1 contributes to Ndc80 recruitment independently of the Mis12 complex.

![Figure 6.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig6-v1.jpg)

**Figure 6.:** Dsn1 and CENP-TCnn1 both contribute to Ndc80 recruitment. Kinetochores were assembled using extract from WT, dsn1-AID, cnn1Δ, or dsn1-AID cnn1Δ double mutant cells that were arrested in benomyl and treated with auxin: DSN1-3Flag Cnn1-3V5 OsTIR1 (SBY17548), DSN1-3Flag cnn1Δ OsTIR1 (SBY17546), dsn1-3HA-AID Cnn1-3V5 OsTIR1 (SBY17544), and dsn1-3HA-AID cnn1Δ OsTIR1 (SBY17380). Extracts in Figure 6—figure supplement 1.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig6-figsupp1-v1.jpg)

### CENP-TCnn1 is essential for Ndc80 recruitment when Mis12c lacks mitotic phosphorylation

Although CENP-TCnn1 contributes to Ndc80 recruitment, Mis12c is clearly the major Ndc80 receptor in budding yeast (Schleiffer et al., 2012; Bock et al., 2012). Consistent with this, Mis12c is essential for viability while CENP-TCnn1 is non-essential, leading to the question of why yeast have retained the CENP-TCnn1 pathway. We hypothesized that CENP-TCnn1 may compensate for downregulation of the Mis12c pathway when the conserved Aurora B sites on Dsn1 are dephosphorylated. Although yeast cells lacking the Aurora B phosphorylation sites (dsn1-2A) are inviable due to low Dsn1 protein expression, mutating an additional Cdk1 site (serine 264) restores protein levels and viability (dsn1-3A) (Akiyoshi et al., 2013a; Akiyoshi et al., 2013b). Because dsn1-3A weakens the interaction between Mis12c and CENP-CMif2, we postulated that this linkage is not essential due to compensation by the CENP-TCnn1 pathway. Consistent with this, there was synthetic lethality between dsn1-3A and cnn1Δ (Figure 7A), indicating that CENP-TCnn1 becomes essential when the Mis12 pathway is misregulated. This result is similar to previous reports indicating that mutants in CENP-T/W exacerbate mutations in CENP-CMif2 (Schleiffer et al., 2012; Hornung et al., 2014). To further test this, we crossed dsn1-3A to additional mutants in the CENP-TCnn1 pathway (deletions of CENP-KMcm22 and CENP-NChl4). These deletions are also synthetically lethal with dsn1-3A (Figure 7A), indicating that the entire CENP-TCnn1 pathway is essential for viability when the interaction between Dsn1 and CENP-CMif2 is crippled by a lack of Aurora B phosphorylation. These data are consistent with previous observations that a CENP-TCnn1 deletion has synthetic phenotypes with a CENP-CMif2 mutant that cannot bind to Mis12c and with a temperature sensitive allele of the Mis12 complex component NNF1 (Bock et al., 2012; Hornung et al., 2014).

![Figure 7.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig7-v1.jpg)

**Figure 7.:** (A) The CENP-TCnn1 pathway is required for viability when the Mis12c assembly pathway is compromised. Dsn1-3A is synthetic lethal with cnn1Δ and deletions of other genes (MCM22 and CHL4) in the CENP-TCnn1 recruitment pathway. A dsn1-3A strain (SBY14170) was crossed to cnn1Δ (SBY13386), mcm22Δ (SBY6997), and chl4Δ (SBY8788). The meiotic products (tetrads) of the resulting diploids are oriented left to right, haploid spores were genotyped, and double mutants are indicated with circles. (B) A dsn1-3A mcm22-AID double mutant is lethal when treated with auxin. Serial dilutions of the following yeast strains were plated on the indicated media: WT (SBY3), dsn1-3A-3Flag (SBY14170), mcm22-3HA-AID OsTIR1 (SBY17982), and dsn1-3A-3Flag mcm22-3HA-AID OsTIR1 (SBY18171). (C) The CENP-TCnn1 pathway recruits Ndc80 when Mis12 complex assembly is compromised. Assembly was performed with extracts from HU-arrested strains that were treated with auxin: DSN1-3Flag OsTIR1 (SBY14131), DSN1-3Flag mcm22-3HA-AID OsTIR1 (SBY18044), dsn1-3A-3Flag OsTIR1 (SBY14169), and dsn1-3A-3Flag mcm22-3HA-AID OsTIR1 (SBY18034). Extracts in Figure 7—figure supplement 2. (D) WT (SBY18498) and dsn1-3A mcm22-3HA osTIR1 (SBY18324) cells containing MTW1-3GFP were released from G1 and kinetochores were analyzed by fluorescence microscopy during metaphase. The percentage of cells containing mono-lobed, bi-lobed or scattered kinetochores was quantified and a representative picture of the bi-lobed and scattered categories is shown above the graph. The p value for the difference between WT and the double mutant for bi-lobed kinetochores is 0.04 and for scattered kinetochores is 0.036. (E) The sequential order of kinetochore subcomplex recruitment to the DNA, as determined from our data and from (Pekgöz Altunkaya et al., 2016). Dotted lines indicate physical interactions.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** The strains are DSN1-3Flag CNN1-3V5 OsTIR1 (SBY18040), DSN1-3Flag CNN1-3V5 mcm22-3HA-AID OsTIR1 (SBY18042), and dsn1-3A-3Flag CNN1-3V5 OsTIR1 (SBY18028).

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig7-figsupp2-v1.jpg)

**Figure 7—figure supplement 2.:** Whole cell extracts and assembly assays for strains DSN1-3Flag CNN1-3V5 OsTIR1 (SBY18040), DSN1-3Flag CNN1-3V5 mcm22-3HA-AID OsTIR1 (SBY18042), and dsn1-3A-3Flag CNN1-3V5 OsTIR1 (SBY18028). (C) Mcm22-3HA-AID degradation for the experiment in Figure 7C.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/37819/elife-37819-fig7-figsupp3-v1.jpg)

**Figure 7—figure supplement 3.:** The levels of Ndc10 and Ndc80 were quantified and the relative ratio was graphed. The standard deviation is indicated.

We hypothesized that the synthetic lethality exhibited in the double mutant strain is due to a defect in Ndc80 recruitment. To test this, we attempted to generate a conditional double mutant strain to analyze Ndc80 assembly. However, a cnn1-AID allele was hypomorphic and exhibited synthetic lethality with dsn1-3A even in the absence of auxin (data not shown). We therefore generated an mcm22-AID allele that blocks the centromere recruitment of CENP-TCnn1 (Figure 7—figure supplements 1 and 2). The mcm22-AID dsn1-3A double mutant was inviable when auxin was added (Figure 7B). To analyze Ndc80 recruitment, we performed the assembly assay from extracts made from the single and the double mutant cells treated with auxin. Because we expected the double mutant to be deficient for Ndc80 recruitment, we reasoned that the mitotic checkpoint might be compromised and therefore arrested cells in S phase rather than mitosis. As expected, the dsn1-3A extracts showed a considerable decrease in Ndc80 assembly as well as the other KMN components, Dsn1 and KNL1Spc105, and that Ndc80 recruitment was further reduced in the dsn1-3A mcm22-AID double mutant (Figure 7C and Figure 7—figure supplement 3). Despite this reduction in Ndc80, KNL1Spc105 assembly appears unaffected by CENP-KMcm22 degradation, suggesting that the CENP-TCnn1 pathway may specifically recruit Ndc80 and not the full KMN network. To determine how the defect in Ndc80 recruitment we detected in vitro affects kinetochore function in vivo, we analyzed the distribution of kinetochores in the dsn1-3A mcm22-AID mutant. WT and dsn1-3A mcm22-AID cells containing Mtw1-3GFP were released from G1 and analyzed for kinetochore distribution when they were in metaphase. While the majority of WT cells exhibited a normal bi-lobed distribution of kinetochores, the kinetochores were scattered in the double mutant cells indicating a defect in establishing normal kinetochore-microtubule attachments (Figure 7D). Together, our data suggest that the CENP-TCnn1 pathway is required to recruit critical levels of Ndc80 complex to kinetochores to mediate proper kinetochore-microtubule attachments when the centromere recruitment of the Mis12c is compromised by a defect in Aurora B phosphorylation.

## Discussion

### Kinetochores can be assembled de novo

We developed an assay using centromeric DNA and whole cell yeast extracts to assemble kinetochores de novo. Although similar assays incubating yeast centromeric DNA in extracts were previously developed, none achieved assembly of the outer kinetochore (Ohkuni and Kitagawa, 2011; Sandall et al., 2006; Sorger et al., 1994). By altering the extract conditions, we were able to assemble all known kinetochore subcomplexes on a centromeric DNA template. Outer kinetochore assembly was dramatically enhanced when the extracts were made from cells expressing a conserved phospho-mimetic mutant that promotes kinetochore assembly in vivo (Akiyoshi et al., 2013a; Kim and Yu, 2015; Yang et al., 2008; Dimitrova et al., 2016; Petrovic et al., 2016). In addition, the assembly assay utilizes both conserved pathways for Ndc80 recruitment, and the assembled kinetochores are competent to attach to microtubules in vitro. In the future, it will be important to fully characterize the microtubule binding mode of the assembled kinetochores using biophysical assays.

A number of criteria indicate that the assay we developed reflects kinetochore assembly de novo. First, the assembly of all kinetochore proteins depends on the CBF3 complex, which is required to initiate assembly in vivo (Poddar et al., 2004). Second, CENP-A association with the template requires its chaperone (Camahort et al., 2007; Shivaraju et al., 2011; Stoler et al., 2007). Histone H2A, H2B, and H4 are also present, suggesting that a centromeric nucleosome forms on the DNA. We found that DNA templates capable of wrapping a single centromeric nucleosome efficiently assemble kinetochores, consistent with recent work showing that KMN can link to a single centromeric nucleosome (Weir et al., 2016). In addition, these data demonstrate that pericentromeric chromatin is not required for kinetochore assembly in vitro, although it contributes to kinetochore function in vivo (Bloom, 2014). Third, outer kinetochore protein recruitment depends on the inner kinetochore proteins (Gascoigne and Cheeseman, 2011; Hara and Fukagawa, 2018). Fourth, kinetochore assembly is more efficient in extracts made from cells arrested in S phase or mitosis. Although it was previously shown that yeast kinetochores assemble during S phase, it was not clear if assembly required DNA replication (Kitamura et al., 2007; Pearson et al., 2004). Because replication cannot occur in extracts without sequential kinase treatment (Heller et al., 2011), our assay also shows that active DNA replication is not a strict requirement for kinetochore assembly.

### CENP-TCnn1 localization to kinetochores requires the CCAN

Kinetochores recruit the microtubule-binding complex Ndc80 through both the Mis12 complex and CENP-TCnn1 (Nishino et al., 2013; Schleiffer et al., 2012; Malvezzi et al., 2013; Hori et al., 2008). The position of CENP-TCnn1 within the kinetochore has been unclear because it can form a nucleosome-like structure with CENP-W/S/X in vitro (Nishino et al., 2012). However, the CENP-TCnn1 and CENP-ACse4 DNA-binding sites overlap in yeast (Pekgöz Altunkaya et al., 2016), suggesting that CENP-TCnn1 may not directly contact the centromere. We found that all CCAN subcomplexes analyzed are required for CENP-TCnn1 kinetochore localization in vitro, which is generally consistent with work analyzing its localization in human cells (Carroll et al., 2010; Basilico et al., 2014; Samejima et al., 2015; Suzuki et al., 2015; Pekgöz Altunkaya et al., 2016; Logsdon et al., 2015). However, an OA mutant that is defective in the recruitment of other CCAN components does retain some CENP-TCnn1in vivo, suggesting that CENP-TCnn1 localization requirements in vivo may be more complex than revealed by our assay (Thapa et al., 2015; Schmitzberger et al., 2017). Regardless, these data are consistent with the conclusion that CENP-TCnn1 does not have intrinsic DNA binding activity under our assay conditions. In addition, we did not detect CENP-S/XMhf1/2 specifically binding to centromeric DNA, suggesting they are not yeast kinetochore components.

It was previously known that CENP-ACse4 recruits CENP-CMif2 and OA, but the relative order of CCAN components downstream of these complexes was unclear. We therefore combined our data with known physical interactions of each subcomplex to map the order of the pathway from CENP-ACse4 to CENP-TCnn1 (Figure 7D) (Pekgöz Altunkaya et al., 2016). We propose that the OA complex is the bifurcation point of the Mis12c and CENP-TCnn1 assembly pathways, because the CENP-QOkp1 mutant perturbed the assembly of both KMN and CENP-POCtf19-Mcm21, while the CCAN subcomplexes downstream of CENP-CMif2 and OA specifically altered only the CENP-TCnn1 pathway. The CENP-TCnn1 recruitment pathway is therefore comprised of the CENP-PO (CM complex), CENP-HIK, and CENP-LN complexes. We note that all of the non-essential, conserved yeast kinetochore proteins are specific to the CENP-T pathway, providing an explanation for why the yeast kinetochore contains both essential and non-essential proteins.

### Functions of the CENP-TCnn1 pathway in budding yeast

In human cells, the CENP-T pathway recruits Ndc80 both directly and indirectly. The CENP-T protein directly binds to two Ndc80 complexes and recruits a third via a phospho-regulated interaction with a Mis12 complex that is also bound to an Ndc80 complex (Huis In 't Veld et al., 2016; Rago et al., 2015). CENP-T knockdown in human cells results in severely decreased Mis12 and KNL1 complexes at kinetochores (Gascoigne et al., 2011; Kim and Yu, 2015). In contrast, we did not find evidence for the recruitment of KMN by CENP-TCnn1 in budding yeast, consistent with data showing that recombinant CENP-TCnn1 does not interact with recombinant Mis12 complex in vitro (Schleiffer et al., 2012). The CCAN mutants we assayed that specifically inhibit the CENP-TCnn1 pathway did not alter Mis12 or KNL1Spc105 assembly. A lack of linkage between CENP-TCnn1 and the Mis12 complex in yeast may also explain why CENP-TCnn1 is non-essential and does not contribute to spindle checkpoint signaling (Schleiffer et al., 2012; Bock et al., 2012). It will be important to further analyze the relationship between the yeast Mis12 complex and CENP-TCnn1 in the future.

The Mis12 pathway is responsible for the majority of Ndc80 recruitment in yeast, so it is surprising that yeast cells are viable when the conserved phosphorylation sites that promote Mis12c localization are mutated (Akiyoshi et al., 2013a; Kim and Yu, 2015; Yang et al., 2008; Dimitrova et al., 2016; Petrovic et al., 2016). Here, we discovered these cells are viable because they use the CENP-TCnn1 pathway to assemble a functional kinetochore. When the CENP-TCnn1 pathway is eliminated in cells lacking Dsn1 phosphorylation, Ndc80 levels are significantly reduced and kinetochores are defective in making normal attachments to microtubules in vivo. A deletion of CENP-TCnn1 has synthetic phenotypes with two other mutants that cripple Mis12c assembly: a CENP-CMif2 truncation lacking its Mis12c binding site and a temperature sensitive allele of NNF1 in the Mis12 complex (Bock et al., 2012; Hornung et al., 2014). Taken together, these data suggest that the CENP-TCnn1 assembly pathway is required to recruit critical levels of Ndc80 when the function of the Mis12c pathway is reduced. CENP-TCnn1 kinetochore levels peak at anaphase (Bock et al., 2012; Dhatchinamoorthy et al., 2017), which is the time when Aurora B-mediated phosphorylation of kinetochore proteins is reversed by phosphatase activity. Therefore, the anaphase enrichment of CENP-TCnn1 might not only increase the load-bearing potential of kinetochore-microtubule attachments by recruiting more Ndc80, but also reinforce kinetochore stability when Aurora B-mediated phosphorylation of Dsn1 is removed. In addition, switching to an Ndc80-recruiting pathway that does not recruit KMN may also help silence the spindle assembly checkpoint, as KNL1 is the critical scaffold for the SAC.

The development of a kinetochore assembly assay de novo has helped to define the two pathways that assemble Ndc80 at kinetochores. Our assay is complementary to a previously developed assembly method using preassembled chromatin templates and frog egg extracts (Guse et al., 2011), but provides the advantage of being genetically tractable. In the future, our assembly assay will be useful for directly examining the role of other post-translational modifications in kinetochore assembly. In addition, it will provide a method to assess the biophysical and structural properties of each Ndc80 recruitment pathway to better understand how cells maintain kinetochore-microtubule attachments to ultimately ensure accurate chromosome segregation.

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
      <td>Gene (S. cerevisiae)</td>
      <td>See supplementary file 1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Saccharomyces cerevisiae)</td>
      <td>W303</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (S. cerevisiae)</td>
      <td>See supplementary file 1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Ndc10 (rabbit polyclonal)</td>
      <td>Desai lab</td>
      <td>OD1</td>
      <td>(1:5,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Cse4 (rabbit polyclonal)</td>
      <td>Biggins lab</td>
      <td>9536</td>
      <td>(1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Mif2 (rabbit polyclonal)</td>
      <td>Desai lab</td>
      <td>OD2</td>
      <td>(1:6,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Ctf19 (rabbit polyclonal)</td>
      <td>Desai lab</td>
      <td>OD10</td>
      <td>(1:15,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Ndc80 (rabbit polyclonal)</td>
      <td>Desai lab</td>
      <td>OD4</td>
      <td>(1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Spc105 (rabbit polyclonal)</td>
      <td>Biggins lab</td>
      <td>PAC4065</td>
      <td>(1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Ipl1 (rabbit polyclonal)</td>
      <td>Desai lab</td>
      <td>OD121</td>
      <td>(1:300)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-HA (mouse monoclonal)</td>
      <td>Roche</td>
      <td>12AC5, Catalog #1-583-816</td>
      <td>(1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-V5 (mouse monoclonal)</td>
      <td>Invitrogen</td>
      <td>Catalog #R960-25</td>
      <td>(1:5,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Flag (mouse monoclonal)</td>
      <td>Sigma-Aldrich</td>
      <td>Catalog #F3165</td>
      <td>(1:3,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Myc (mouse monoclonal)</td>
      <td>Covance</td>
      <td>9E10, Catalog #MMS-150R</td>
      <td>(1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-mouse secondary (goat monoclonal)</td>
      <td>GE Healthcare BioSciences</td>
      <td>NA931</td>
      <td>(1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-rabbit secondary (goat monoclonal)</td>
      <td>GE Healthcare BioSciences</td>
      <td>NA934</td>
      <td>(1:10,000)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>See supplementary file 2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>See supplementary file 3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>α-factor</td>
      <td>United Biochemical Research Inc.</td>
      <td></td>
      <td>10 mg/mL</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>hydroxyurea</td>
      <td>Sigma</td>
      <td>H8627</td>
      <td>0.2M</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>benomyl</td>
      <td>Sigma</td>
      <td>381586–25G</td>
      <td>60 mg/mL</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>indole-3-acetic acid (IAA)</td>
      <td>Sigma</td>
      <td>I3750-5G-A</td>
      <td>500 mM</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Dynabeads M-280 Streptadivin</td>
      <td>Invitrogen</td>
      <td>112-05D</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Yeast strain construction

The Saccharomyces cerevisiae strains used in this study are listed in Supplementary file 1. Standard genetic crosses and media were used to generate and grow yeast (Sherman et al., 1974). Gene deletions, AID alleles, and epitope tagged alleles (3Flag, 9myc, 3 HA, and 3V5) were constructed at the endogenous loci by standard PCR-based integration as described in (Longtine et al., 1998) and confirmed by PCR. DSN1-3Flag, dsn1-2D-3Flag, and dsn1-3A-3Flag were generated by PCR amplification of part of the DSN1 gene, the Flag tags, and URA3 using primers SB4570 and SB4571 on plasmids pSB1113, pSB1115, and pSB1142, respectively. The PCR products were transformed into yeast, and the transformants were confirmed by sequencing. The plasmids and primers used to generate strains are listed in Supplementary file 2 and 3.

### Yeast methods

All liquid cultures were grown in yeast peptone dextrose rich (YPD) media. Cells were arrested in G1 or S phase by adding either 10 μg/mL α-factor in DMSO or 0.2M hydroxyurea, respectively, to log phase cells in liquid culture for three hours until at least 90% of the cells were shmoos (α-factor) or large-budded (hydroxyurea). To arrest cells in mitosis, log phase cultures were diluted 1:1 with liquid media containing 60 μg/mL benomyl and grown for another three hours until at least 90% of cells were large-budded.

Temperature sensitive alleles were inactivated by diluting log phase cultures 1:1 with 37°C liquid media and shifting the cultures to 37°C for 2 hr (ndc10-1) or 3 hr (cse4-323 and mif2-3) before harvesting. For cse4-323 and mif2-3, the added 37°C media included 60 μg/mL benomyl.

For strains with auxin inducible degron (AID) alleles, all cultures used in the experiment were treated with 500 μM indole-3-acetic acid (IAA, dissolved in DMSO) for the final 60 min of growth (scm3-AID, ndc80-AID, sli15-AID, and dsn1-AID) as described in (Nishimura et al., 2009; Miller et al., 2016). For the experiment that included okp1-AID (Figure 5C), all log phase cultures were diluted 1:1 with media containing benomyl and IAA such that the final concentrations were 30 μg/mL benomyl and 500 μM IAA. After two hours, another 150 μM IAA was added, and cultures were harvested after one more hour. For the experiment in Figure 7B, 0.2M hydroxyurea and 500 μM IAA was added to log phase liquid cultures. After two hours, another 150 μM IAA was added, and cultures were harvested after one more hour. For the analysis of kinetochore distribution (Figure 7D), cells were arrested in G1 with alpha factor for three hours and IAA was added during the final hour. The cells were washed and released into media with IAA and harvested after 100 min (when cells were in metaphase) for microscopy analysis. At least 200 cells were analyzed in duplicate biological replicates.

Growth assays were performed by diluting log phase cultures to OD600 ~ 1.0 from which a 1:5 serial dilution series was made. This series was plated on YPD plates that were top-plated with either DMSO or 500 μM IAA plates and incubated at 23°C.

### Preparation of DNA templates, Dynabeads, and competitive DNA

Plasmid pSB963 was used to generate the ampC and CEN3 DNA templates and pSB972 was used to generate the CEN3mut template used in this study. DNA templates were generated by PCR using a 5’ primer with pericentromeric homology upstream of the centromere and a biotinylated 3’ primer with linker DNA, an EcoRI restriction site, and pericentromeric homology downstream of the centromere. The latter primer was ordered from Invitrogen with a 5’ biotinylation. Sequences of the primers used to PCR amplify the DNA templates are listed in Supplementary file 3.

The PCR product was purified using the Qiagen PCR Purification Kit and conjugated to Streptadivin-coated Dynabeads (M-280 Streptavidin, Invitrogen) for 2.5 hr at room temperature, using 1 M NaCl, 5 mM Tris-HCl (pH7.5), and 0.5 mM EDTA as the binding and washing buffer. Per 1 mg (100 μL) of beads, we conjugated 1.98 μg/mg of the 180 bp templates, 2.75 μg/mg of the 250 bp centromeric templates, or 5.5 μg/mg of the 500 bp ampC template to have equivalent numbers of templates on beads. After washing three times, the beads were stored in 10 mM HEPES-KOH and 1 mM EDTA at 4°C until use. Competitive DNA was made by sonicating 5 μg/mL salmon sperm DNA in dH2O. The sonicated salmon sperm DNA was stored at −20°C in between uses.

### Kinetochore assembly assay

For a standard kinetochore assembly in vitro, cells were grown in 600 mL of liquid YPD media to log phase and harvested by centrifugation. All subsequent steps were performed on ice with 4°C buffers. Cells were washed once with dH2O with 0.2 mM PMSF, then once with Buffer L (25 mM HEPES pH 7.6, 2 mM MgCl2, 0.1 mM EDTA pH 7.6, 0.5 mM EGTA pH 7.6, 0.1 % NP-40, 175 mM K-Glutamate, and 15% Glycerol) supplemented with protease inhibitors (10 μg/ml leupeptin, 10 μg/ml pepstatin, 10 μg/ml chymostatin, 0.2 mM PMSF), and 2 mM DTT. Cells were resuspended in Buffer L according to the following calculation: (OD of culture) x (number of mL of culture harvested)=number of μL of Buffer L. This suspension was then snap frozen in liquid nitrogen by pipetting drops directly into liquid nitrogen. These dots were then lysed using a Freezer/Mill (SPEX SamplePrep), using 10 rounds that consisted of 2 min of bombarding the dots at 10 cycles per second, then cooling for 2 min. The subsequent powder was thawed on ice and clarified by centrifugation at 16,100 g for 30 min at 4°C. The resulting soluble whole cell extracts (WCE) generally have a concentration of 50–70 mg/mL. The dots, powder, and WCE were stored at −80°C if needed. 5 μL of WCE were saved in a sodium dodecyl sulfate (SDS) buffer for immunoblot analysis.

Typically, 750 μL of whole cell extract was incubated on ice for 15 min with 24.75 μg sonicated salmon sperm DNA (30-fold excess competitive DNA relative to the DNA template on beads). Then, 30 μL of beads pre-conjugated with DNA were added, and the reaction was rotated constantly at room temperature for 30–90 min. The reaction was stopped on ice by addition of 3–5 times the reaction volume of Buffer L. The beads were then washed once with 1 mL Buffer L supplemented with 33 μg/mL of competitive DNA, then three more times with 1 mL Buffer L. Bound proteins were eluted by resuspending the beads in 75 μL of SDS buffer, boiling the beads at 100°C for 3 min, and collecting the supernatant. Samples were stored at −20°C. Bound proteins were examined by immunoblotting, described below. All experiments were repeated two or more times as biological replicates to verify reproducibility and a representative result is reported.

### Mass spectrometry

Following the standard assembly protocol and washes, assembled kinetochores were washed twice with 1 mL of 50 mM HEPES pH 8, then resuspended in ~60 μL of 0.2% RapiGest SF Surfactant (Waters) in 50 mM HEPES pH 8. Proteins were eluted by gentle agitation at room temperature for 30 min. A small portion of the eluate was added to SDS buffer and analyzed by SDS-PAGE and immunoblotting and/or silver staining. The remaining sample was snap frozen in liquid nitrogen and sent to the Taplin Mass Spectrometry Facility for LC/MS/MS analysis, or to Thermo Fisher Scientific Center for Multiplexed Proteomics at Harvard Medical School (TCMP@HMS) for TMT labeling and MS3 analysis.

### Bulk microtubule-binding assay

Microtubules were polymerized at 37°C for 15 min using a 1:50 mixture of Alexa-647-labeled and unlabeled bovine tubulin in polymerization buffer [BRB80 (80 mM PIPES, 1 mM MgCl2, 1 mM EGTA, pH 6.8), 1 mM GTP, 5.7% (v/v) DMSO, and an additional 4 mM MgCl2]. The polymerization was stopped with the addition of BRB80 and 10 μM taxol. Microtubules were sheared by pulling them through a 27 1/2G needle 10 times, and then pelleted by room temperature centrifugation for 10 min at 170,000 g. Polymerized microtubules were resuspended in BRB80 with 10 μM taxol to approximately 14.4 μM, based on the initial amount of tubulin. Serial dilutions of both the polymerized microtubules and the equivalent amount of initial tubulin mixture were run on an SDS-PAGE gel and analyzed by fluorescence imaging with a Typhoon Trio (GE Healthcare). The amount of tubulin that successfully polymerized was estimated to ensure that comparable amounts of free tubulin and microtubules were introduced to the assembled kinetochores. Assembled and washed kinetochores on beads were resuspended in room temperature Buffer L with 0.9 mg/mL κ-casein, 20 uM taxol, and either ~5 nM tubulin or polymerized microtubules. This reaction was incubated at room temperature with constant rotation for 45 min, then washed twice with room temperature Buffer L, resuspended in SDS buffer, and eluted by boiling. Bound tubulin or microtubules were detected by fluorescence imaging.

### Whole cell extracts for AID degradation

Whole cell extracts for immunoblotting were made by freezing cells in liquid nitrogen and resuspending in SDS buffer. Cells were lysed using glass beads and a beadbeater (Biospec Products), then clarified by centrifugation at 16,100 g for 5 min at 4°C.

### Immunological methods

Whole cell extract or samples were prepared as described above and separated by SDS-PAGE. Proteins were transferred to a nitrocellulose membrane (BioRad) and standard immunoblotting was performed. Primary and secondary antibodies were used as described in (Miller et al., 2016). Additionally, α-Ndc10, α-Mif2, and α-Ipl1 were generous gifts from Arshad Desai and were used as follows: α-Ndc10 (OD1) 1:5,000; α-Mif2 (OD2) 1:6,000; and α-Ipl1 (OD121) 1:300. We also used α-Cse4 (9536) 1:500 (Pinsky et al., 2003). HRP conjugated secondary antibodies were detected with Pierce enhanced chemiluminescent (ECL) substrate and SuperSignal West Dura and Femto ECL (ThermoFisher Scientific). Note that the immunoblot exposures vary to best represent differences across extracts or assembly samples. The levels of proteins in input extracts and assembly samples can therefore not be directly compared.
