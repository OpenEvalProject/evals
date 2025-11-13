# NaLi-H1: A universal synthetic library of humanized nanobodies providing highly functional antibodies and intrabodies

## Authors

- Sandrine Moutel<sup>1</sup>
- Nicolas Bery<sup>4</sup> ([ORCID: 0000-0002-2643-3897](https://orcid.org/0000-0002-2643-3897))
- Virginie Bernard<sup>1</sup>
- Laura Keller<sup>4</sup> ([ORCID: 0000-0002-1786-9760](https://orcid.org/0000-0002-1786-9760))
- Emilie Lemesre<sup>1</sup>
- Ario de Marco<sup>1</sup> ([ORCID: 0000-0001-7729-819X](https://orcid.org/0000-0001-7729-819X))
- Laetitia Ligat<sup>7</sup>
- Jean-Christophe Rain<sup>8</sup>
- Gilles Favre<sup>4</sup> ([ORCID: 0000-0002-2344-1883](https://orcid.org/0000-0002-2344-1883))
- Aurélien Olichon<sup>4</sup> †
- Franck Perez<sup>1</sup> ([ORCID: 0000-0002-9129-9401](https://orcid.org/0000-0002-9129-9401)) †

### Affiliations

1. Institut Curie, PSL Research University Paris France
2. CNRS UMR144 Paris France
3. Translational Research Department Institut Curie Paris France
4. Inserm, UMR 1037-CRCT Toulouse France
5. Faculté des Sciences Pharmaceutiques, Université Toulouse III-Paul Sabatier Toulouse France
6. Institut Claudius Regaud Toulouse France
7. Le Pôle Technologique du Centre de Recherches en Cancérologie de Toulouse, plateau de protéomique Toulouse France
8. Hybrigenics Service Paris France

† Corresponding author

## Abstract

In vitro selection of antibodies allows to obtain highly functional binders, rapidly and at lower cost. Here, we describe the first fully synthetic phage display library of humanized llama single domain antibody (NaLi-H1: Nanobody Library Humanized 1). Based on a humanized synthetic single domain antibody (hs2dAb) scaffold optimized for intracellular stability, the highly diverse library provides high affinity binders without animal immunization. NaLi-H1 was screened following several selection schemes against various targets (Fluorescent proteins, actin, tubulin, p53, HP1). Conformation antibodies against active RHO GTPase were also obtained. Selected hs2dAb were used in various immunoassays and were often found to be functional intrabodies, enabling tracking or inhibition of endogenous targets. Functionalization of intrabodies allowed specific protein knockdown in living cells. Finally, direct selection against the surface of tumor cells produced hs2dAb directed against tumor-specific antigens further highlighting the potential use of this library for therapeutic applications.

## Introduction

Antibodies expended as the biochemical tools of choice to label antigens in cells or tissues. Over the past 20 years, recombinant methods have been developed to quickly select and improve monoclonal antibodies from highly diverse libraries. Recombinant antibodies can be selected from immune or naïve libraries. Immune libraries provide in general high affinity binders but, depending on the antigen, diversity is sometimes limited. Because natural antibody selection requires animal immunization, very conserved or toxic antigens should be avoided and, in general, only limited control of the immune response is possible. On the contrary, non-immune (naïve) libraries provide a higher diversity of binders even for antigens highly conserved in mammals, but high specificity and affinity can be reached only when selecting from very large functional libraries. Immune and naïve libraries are based on the manipulation of antibody fragment that retain binding capacity and specificity of the entire immunoglobulin G (IgG).

The smallest IgG portion capable of binding with high specificity an antigen is the Fv fragment consisting of the variable heavy (VH) and the variable light (VL) domains. In the case of single domain antibodies (sdAb), a VH or a VL alone, is able to bind its target antigen. Each variable domain contains four conserved framework regions (FRW or framework) and three regions called CDR (Complementarity Determining Regions) corresponding to hypervariable sequences which determine the specificity for the antigen. VH and VL can be fused together using a synthetic linker and produced as a single protein in the form of a single chain Fv (scFv). Easier to manipulate, they can be produced in several bacteria or eukaryote cell types, fused to various tags or functional domains. Interestingly, antibodies called HCAb in Camelidae (Hamers-Casterman et al., 1993) or IgNAR in sharks (Greenberg et al., 1995) have an antigen recognition part composed of only a VH domain. Camelid natural single domain VH, referred to as VHH or nanobodies, can be expressed as recombinant fragments and represent attractive alternatives over classical antibody fragments like scFvs because they are easy to manipulate and they are not limited by potential misfolding of the two domains (Wörn and Plückthun, 1999). It is noteworthy that VHH FRWs show a high sequence and structural homology with human VH domains of family III (Muyldermans, 2013) and VHH have comparable immunogenicity as human VH (Bartunek et al., 2013; Holz et al., 2013). Thus, they further constitute very interesting agents for therapeutic applications, some of them are currently in phase II and Phase III clinical trials (Ablynx Nanobodies; http://clinicaltrials.gov/ct2/results?term=ablynx).

Recombinant antibody fragments allowed not only to accelerate the identification of unique binders, but also the development of a novel type of tool: in this case, the antibodies are directly expressed in living cells as intracellular antibodies (intrabodies), to trace or perturb endogenous target at the protein level. Some scFv or sdAb have indeed been directly expressed in eukaryotic cell as intrabodies to target with high specificity intracellular antigens. Several intrabodies have been used as fluorescent protein fusion to highlight endogenous antigen in cells in a spatio-temporal manner (Nizak et al., 2003a; Rothbauer et al., 2006). Intrabodies with intrinsic blocking activity have been reported (Haque et al., 2011; Shin et al., 2005), and several other approaches have been developed to allow a larger fraction of intrabodies to be used as inhibitory factors: forced co-localization (Tanaka et al., 2007), suicide through proteasome targeting (Joshi et al., 2012; Melchionna and Cattaneo, 2007), rerouting or sequestration to cell compartment (Böldicke et al., 2005), degradation (Caussinus et al., 2011). Depending on the target, such inhibitors may have potential in human therapy. Production of functional intrabodies depends on the stability of the antibody fragments in the reducing environment of the cytosol that does not allow disulfide bond formation between conserved cysteine. In this context, many advantages of the nanobody scaffold have been reported and, in particular, higher solubility, improved stability in a reducing environment (Wesolowski et al., 2009), as well as higher expression yield and thermostability (Jobling et al., 2003). For all these reasons, the nanobody scaffold represents an attractive option to generate functional intrabodies.

Thus, we decided to create a non-immune recombinant antibody library of high diversity, based on a nanobody scaffold that would enable efficient in vitro antibody selection against virtually any antigen. Such a library should provide antibodies usable in conventional immune assays and be enriched in antibodies active in the intracellular environment. First, using a fusion assay in E. coli, a family of highly functional VHH scaffolds was isolated, optimized for intracellular expression and high stability. One particularly stable VHH scaffold consensus sequence was chosen from these selected antibodies. Additional changes were then introduced to reduce the distance between the Camelidae and human VH3 sequences. We confirmed by CDR grafting that this humanized synthetic scaffold (hs2dAb) was robust and functional. Statistics of amino-acid diversity in the CDRs were computed and these information were used to construct a high diversity phage display library of 3.109 independent hs2dAb. The library was then screened against diverse targets of various structures and origin. Highly specific antibodies were selected against EGFP, mCherry, β-tubulin, β-actin, heterochromatin protein HP1α, GTP-bound RHO, p53 and HER2. Affinity measurement indicated that affinities in the nM range can be obtained using this library. As expected from our design, we further showed that hs2dAb are frequently usable as fluorescent intrabodies to track antigens in cells. We also showed that they can be functionalized to induce antigen knockdown. This thus represents the first report of a large and diverse synthetic single domain antibody library enabling fully in vitro selection of highly functional antibodies and intrabodies.

## Results

### Library design

We reasoned that the usual lower quality of these non-immune libraries may come from (1) an antibody scaffold that may not allow robust folding and presentation of CDR region, (2) a lack of control of diversity in the CDR regions and (3) a frequent occurrence of incorrect clones due to the presence of unexpected mutation or empty clones. We designed a pipeline for the development of functional synthetic libraries that aims at overcoming these limitations (Figure 1A). As a first step to construct a single domain antibody library enriched in highly stable and functional antibody fragments, we screened for a robust sdAb scaffold (Figure 1—figure supplement 1). Previously, we selected from immune or naïve llama VHH libraries several hundreds of clones (Monegal et al., 2012; Olichon and Surrey, 2007). From this population, we identified a set of robust scaffolds using an assay that discriminates highly stable clones from clones prone to aggregation, or unfolding, in the bacterial cytoplasm (Olichon and Surrey, 2007). This assay is based on the fusion of HA-tagged chloramphenicol acetyl transferase (CAT) to the carboxy-terminus of VHH sequences (Figure 1—figure supplement 1A). In these conditions, only bacteria expressing a functional VHH fusion in the reducing cytosol (non aggregating, non degraded) can grow in the presence of high antibiotic concentration, thus filtrating a sub-library of potential intrabodies. Expression yield in E.coli and apparent solubility as EGFP fusion in the mammalian cell cytoplasm were further assessed to select a set of robust antibody scaffolds. Strikingly, the consensus scaffold was matching the sequence of the most robust VHH framework, represented by a single domain antibody D10 (hereafter named sdAbD10). When compared to previously reported thermostable nanobodies (Olichon et al., 2007a) or intrabodies (Rothbauer et al., 2006) obtained from immune libraries, sdAbD10 was found to provide higher antibiotic resistance in the chloramphenicol filter assay (Figure 1—figure supplement 1A). Its expression yield in E.coli periplasm was in the higher range of soluble llama VHH fragments, allowing efficient and quantitative purification (Figure 1—figure supplement 1B). Purified sdAbD10 showed excellent solubility, stability after treatment at 70°C and we did not observe aggregation when expressed as an intrabody fused to the EGFP in mammalian cells (Figure 1—figure supplement 1C).

![Figure 1.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig1-v2.jpg)

**Figure 1.:** The development of the NaLi-H1 library followed three lines of optimization. (i) A novel scaffold was defined by selecting a set of robust nanobodies using a CAT fusion assay (1). A consensus was derived and mutations were introduced to humanize the scaffold (2). Usability and efficacy of the novel scaffolds (VHH and humanized) were then confirmed evaluating their display on phage, expression in CHO cells and use as intrabodies (3).In silico design was completed analyzing natural CDR diversity (4) and using this information to design synthetic CDRs. A fixed size of 7 aa was chosen for the CDR1 and CDR2. 4 sizes (9, 12, 15 and 18 amino acids) were chosen for CDR3. Finally, the pHEN2 vector was improved by implementing a triple myc tag and inserting a toxic gene (ccdb) to ensure low frequency of empty clones during library construction (6). Gene synthesis (using a tri-nucleotide approach) was ordered, synthetic sequences cloned into the novel pHEN2+ vector, transformed into bacteria and plated on 430 15 cm plates. 3 × 109 clones were obtained. Quality control was carried out using Sanger sequencing of 315 randomly picked clones and large scale sequencing of 56 000 clones. No redundant clone was found. The NaLi-H1 was then screened in various conditions and diversity, efficacy, versatility and affinity evaluated.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Chloramphenicol acetyl transferase carboxy terminal fusion is a folding reporter allowing for the selection of soluble amino terminal VHH. Top: scheme of the construct expressed from pAO-VHH-CAT-HA vector. Bottom: Relative colony growth of selected VHH (GFP4 and Lam1 chromobodies, or thermostable Re3) on chloramphenicol selection medium (Cam). Serial dilution of E.coli culture expressing VHH. (B) Analysis of heat purified sdAbD10 by SDS-PAGE. Clone D10 was expressed in E.coli and protein secreted in the periplasm were extracted (lane 1). Periplasmic extract was subjected to heat treatment at 70°C and insoluble proteins were pelleted by centrifugation (lane 2). The soluble supernatant containing the VHH was then concentrated using Amicon filters (lane 3). (C) HeLa cells expressing a GFP fusion of sdAbD10 showing homo-dispersed fluorescence (right) compared to typical randomly chosen aggregating llama VHH considered as non intrabody (left).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Phages presenting each scaffolds (sdAbD10 and hs2dAb) bearing anti-lamin CDRs were produced in E.coli and supernatant were detected in Western Blot with an anti-pIII antibody (NEB). Two bands are visible, one for wild-type pIII and one for the pIII fusion with single domain antibodies. (B) Dot blot analysis of the production of both scaffolds either as single domain antibodies in E. coli supernatant or as fusions with a human Fc domain and secreted by CHO cells (Moutel et al., 2009). Serial dilutions of supernatant were revealed with an anti-His tag antibody or an anti-human Fc antibody. (C) Immunofluorescence of HeLa cells with recombinant antibody in both scaffolds labeling the nuclear rim structure characteristic of the nuclear lamina. (D) The anti-lamin based on the two scaffolds were transiently expressed in HeLa cells as GFP fusion. Living cells were imaged after 24 hr and showed that the hs2dAb recognized its intracellular target lamin. Bar = 10 µm.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Comparison between relative amino acid frequencies in CRD1 and CDR2 observed from 250 llama VHH isolated from a naïve library (llama), the rationally designed (Designed) and the effective diversity in the synthetic library (Nali-H1) as computed after sequencing of 2500 clones using NGS. The position of each amino acid is indicated (CDR1 1; CDR1 2; etc). Amino Acid are indicated in single letter code. (B) Comparison between the designed diversity set for every amino acid position in the CDR3 region with the effective diversity observed after sequencing 2500 clones using NGS. Note that various CDR3 amino acid lengths are present in the library. They were almost evenly distributed with a little bias for shorter CDR3s (9 aa: 26%; 12 aa: 27.2%; 15 aa: 23.7%; 18 aa: 23.1%). For simplicity, we report in the figure the diversity observed for up to 18 aa. Note also that although cysteine occurs in natural llama CDRs, they were avoided by design and, accordingly, not found in Nali-H1 CDRs.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** (A) Sequential centrifugation carried out using clones selected from the NaLi-H1 library (anti-GFP, anti-mCherry) or obtained after CDR grafting into the hs2dAb scaffold (anti-lamin). As a reference, the behaviour of a widely used natural anti-GFP antibody (GFP4 or Chromobody) was analysed. I: Input; P1: pellet after the 20 000 g centrifugation, P2: pellet obtained after the 250 000 g centrifugation, SN: supernatant of the 250 000 g centrifugation. Samples were analysed after western blotting using an anti-HIS antibody. Note that the apparent size of the lamin antibody and the Chromobody is lower because these antibodies are fused to only one myc tag (expressed from the parental pHEN2-His-Myc plasmid). (B), (C): a set of clones randomly chosen in the NaLi-H1 library was expressed in a multiwell format and analysed as in A. Only-the pellet (P) and the supernatant (SN) of the 250 000 g centrifugation are shown. Two samples (an anti-GFP hs2dAb and a randomly picked clone #1) were heated at 90°C for 10 min before being analysed by sequential centrifugation (anti-GFP* and #1*). Note that in these conditions, a fraction of the hs2dAb is unfolded and found in the pellet. A significant resistance to temperature is however observed. Note that high molecular weight bands were systematically seen which may suggest that a fraction of the hs2dAb is in a multimeric form. The same behaviour was observed for the natural Chromobody.

To test whether the sdAbD10 scaffold composed of the FRW 1 to 4 was robust independently on the CDR sequences, we grafted the CDR loops of the lam1 VHH (Rothbauer et al., 2006) directed against laminB into the framework of the sdAbD10 (sdAbD10-anti lamin). In parallel, partial humanization of the scaffold was also tested to figure out whether it affected dramatically its intrinsic properties. Seven residues of the synthetic scaffold sdAbD10 were altered towards the most represented in human VH3 while five other divergent residues were kept unchanged. The four llama VHH-specific amino acids hallmarks in the framework-2 region (positions 42, 49, 50, and 52), which are essential to increase intrinsic solubility properties, as well as the Glutamine in position 103, were maintained. We named the resulting hybrid single domain VH hs2dAb (humanized synthetic single domain antibody) (Figure 1B). After grafting the CDR of the anti-lamin into these two scaffolds, we analyzed their display on the M13 surface (Figure 1—figure supplement 2A) and their production by E. coli and by CHO cells (Figure 1—figure supplement 2B). Both scaffold showed similarly good efficacy. Importantly, both the sdAbD10 and hs2dAb scaffolds enabled functional display of the grafted CDRs and robust detection of endogenous lamin was observed by immunofluorescence staining of Hela cells (Figure 1—figure supplement 2C). Last, Rothbauer et al. (Rothbauer et al., 2006) showed that the original anti-lamin VHH recognized its target antigen upon intracellular expression. Similarly, we observed that both the hs2dAb and the sdAbD10 scaffolds allowed the efficient intrabody use of the synthetic anti-lamin antibodies (Figure 1—figure supplement 2D). This further indicated that the synthetic scaffolds were robust, non-aggregating and resisted to the reducing conditions found in the cytosol, while allowing the proper display of CDR loops. As partial humanization did not affect the properties of the sdAbD10 scaffold, we chose the hs2dAb scaffold as a unique framework to construct a diverse library of synthetic nanobodies endowed with the characteristic stability of these single domain antibodies while displaying an amino acid sequence closer to human VH3.

### Library construction

A synthetic diversity was introduced in the three CDRs by rationally controlling each position of the CDR1 and CDR2 using a set of amino acids that recapitulates partially natural diversity (see the Appendix for more details) while reducing the presence of the most hydrophobic residues in order to avoid the aggregation propensity (see Material and methods). A constant length of 7 amino acids was selected for CDR1 and CDR2. A large spectrum of Camelidae VHH CDR3 length is naturally observed and this loop is known to contribute strongly to antigen binding selectivity. Thus, we chose to use four different lengths of CDR3 to cover this spectrum (9, 12, 15 or and 18 amino acids) and introduce random amino acid (except cysteine) at each position.

Synthetic DNA was produced by the trinucleotide DNA assembly and amplification was carried out starting from 2.1011 different molecules, using only a few cycles of PCR (PCR linearity validated by Q-PCR) to prevent drift during amplification. The synthetic library was inserted into a modified pHEN2 phagemid vector containing a triple myc-tag and suicide gene (ccdB) that allowed positive selection of insert-bearing clones (Bernard et al., 1994). Massive electroporation was carried out using E. coli TG1 cells and 430 large agar dishes (140 mm) were used to ensure proper plating of the library. About 3.109 individual recombinant hs2dAb clones were obtained. We named this library NaLi-H1 (for Nanobody Library-Humanized 1). We first evaluated the quality of the NaLi-H1 library by sequencing 315 random clones. Only 13 sequences were found to be incorrect (bearing an in-frame stop codon, missing one base, missing a large region [the CDR1 or CDR1-FWR1- CDR2], or being empty). Thus, a total of about 4% of potential default was observed, which is rather low and only marginal in comparison to the 3.109 clones obtained. The diversity was then evaluated by sequencing 5.6 105 inserts using ion Torrent chips (Life Technologies). This confirmed the quality of the library and showed that the four CDR3 lengths (9, 12, 15 or and 18 amino acids) were present in similar proportions. The diversity and statistical distribution of amino acids in the CDRs were found to be as expected (Figure 1—figure supplement 3). To estimate the overall folding of the hs2dAb present in the library, we picked randomly 24 clones and tested their solubility in bacteria medium after secretion. Medium were centrifuged at 250 000 g and the supernatant and pellet were analyzed. All tested clones showed essentially complete solubility, at least as good as a natural Lama antibody (GFP4). Even after warming at 90°C for 10 min, the hs2dAb showed good solubility (over 70%) (Figure 1—figure supplement 4).

### Library screening and validation

The NaLi-H1 library was screened against a set of various antigens. Several standard phage display methods (Hoogenboom, 2005) were used (see Materials and methods for details): antigen adsorption on immunotube, native antigen captured on beads, direct selection at the cell surface. All conditions allowed the efficient recovery of diverse and functional antibodies.

As a first screen to evaluate the quality of the library, we chose to select specific binders for the EGFP and mCherry fluorescent proteins. NaLi-H1 phages were panned against biotinylated EGFP or mCherry and 3 rounds of selection were carried out. Eighty clones were analyzed for each screening campaign. From the panning against EGFP, 37 non redundant nanobodies were shown to detect EGFP by phage ELISA. These antibodies were then used for immunofluorescence and 10 of them were found to efficiently stain EGFP in fixed HeLa cells (Figure 2A). Similarly, selection against mCherry led to 6 positive binders (Figure 2B). As shown in Figure 2A and B, no staining was obtained in untransfected cells.

![Figure 2.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig2-v2.jpg)

**Figure 2.:** (A) HeLa cells were transfected with GFP-Rab6, fixed using paraformaldehyde, permeabilized using saponin and stained with non-purified myc-tagged hs2dAb (R3TF3) directed against EGFP and revealed with anti-Myc-Tag (9E10) and Cy3-labeled secondary antibodies. (B) HeLa cells transfected with mCherry-Rab6, fixed and permeabilized as in A and stained using a myc-tagged non purified hs2dAb against mCherry (C11). The hs2dAb was then revealed using 9E10 and A488-labeled secondary antibodies. (C) Cells were fixed in methanol and co-stained with a non-purified anti-tubulin hs2dAb (D5) fused to a human Fc domain and a mouse monoclonal anti-tubulin antibody (DM1A), and revealed using an anti-Human Fc-A488 and an anti-Mouse-Cy3 secondary antibody, respectively. (D) hs2dAb F4 anti-beta-actin was used to stain MRC5 cells fixed with paraformaldehyde and post fixed with methanol. The hs2dAb was then revealed using 9E10 and A488-labeled secondary antibodies. Cells were co-stained by red fluorescent phalloidin to detect actin stress fibers. (E) A431 cells were fixed with 3% paraformaldehyde, permeabilized with 0.1% Triton and stained with the anti-p53 hs2dAb (B7) fused to a human Fc domain together with a rabbit polyclonal antibody directed against p53. Immuno-labeling was revealed using anti-Human Fc-Cy3 and anti-Rabbit-A488 secondary antibodies. (F) The hs2dAb antibody directed against HP1α (A5) fused to a human Fc domain was used to stain HeLa cells fixed with paraformaldehyde and permeabilized with 0.1% TritonX100. Cells were co-stained using a polyclonal rabbit antibody directed against HP1α and immuno-labeling was revealed using anti-Human Fc-Cy3 and anti-Rabbit-A488 secondary antibodies. (scale bar = 10 µm).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) HeLa cells were left untreated (top) or incubated with 10 µM nocodazole for 90 min at 37°C (bottom). Cells were then permeabilized using 0.2% tritonX100, fixed using methanol (−20°C, 4 min) and immunolabelled using an anti-tubulin hs2dAb (green) and a polyclonal anti-tubulin antibody (Red). Staining was essentially lost upon nocodazole treatment with only few nocodazole-stable microtubules being labelled. Bar = 10 µm (B) HeLa cells were left untreated (top) or incubated with 5 µM cytochalasin D for 60 min at 37°C (bottom). Cells were then fixed using paraformaldehyde, permeabilized with saponin and immunolabelled using the anti-actin hs2dAb H2 (green) and a polyclonal anti-actin antibody (Red). Staining was strongly reorganized upon cytochalasin D treatment. Bar = 10 µm (C) SDS-PAGE of 40 µg sample per well of WI38 whole cell extract was blotted and separated in stripes for each lane. Stripes were then incubated for immuno-detection with various hs2dAb (lane 1–3: anti-actin hs2dAb; lane 4: non relevant [NR] control; lane 6: anti-tubulin hs2dAb) directly used from E.coli culture supernatant and further revealed using myc-HRP antibodies. Control monoclonal anti-actin or anti-tubulin were used on stripes 5 and 7, respectively.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) RPE-1 were left untreated or irradiated with UV light (100 J/m2). Cells were then fixed and stained using an anti-p53 hs2dAb together with an anti-p53 rabbit polyclonal antibody. Both the polyclonal and the hs2dAb antibodies detected the strong increase of p53 localization in the nuclei. (B) RPE-1 cells stably expressing an shRNA directed against p53 together with GFP were irradiated as in A and stained using the hs2dAb. No labeling was obtained in p53 KD cells. Bar = 10 µm.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (B). (A) GFP tagged HP1α, HP1b and HP1γ were expressed in Hela cells. Cells were then lysed and extract separated by SDS-PAGE, transferred on nitrocellulose filters. Immunodetection was carried out using an anti-GFP antibody (left) or an anti-HP1 hs2dAb. Although the selection was carried out against was HP1α, the hs2dAb efficiently detected GFP tagged HP1α, HP1β and HP1γ. The band indicated by a star likely represent the endogenous HP1 proteins. (B) Cells were transfected as in (A), fixed and analyzed by immunofluorescence using the anti-HP1 hs2dAb. Nuclei were stained using DAPI. GFP tagged HP1α, HP1b and HP1γ were all efficiently detected by the recombinant antibody. Bar = 10 µm.

In the next screen, two highly and constitutively expressed components of cell cytoskeleton, tubulin and β-actin, were targeted. Antibodies against tubulin were selected in native conditions (Nizak et al., 2003a) using commercial biotinylated tubulin (Cytoskeleton). After two rounds of selection, 3 out of 40 clones analyzed were shown to detect endogenous tubulin by immunofluorescence (Figure 2C). As expected, staining was lost in cells treated with the microtubule destabilizing drug nocodazole, with only a few stable microtubules being labelled in these conditions (Figure 2—figure supplement 1A). This antibody was recently used to stain microtubules by super-resolution imaging (Mikhaylova et al., 2015). Among phage display methods, selection on antigens directly adsorbed on the surface of immunotube is often used as a cheap and straightforward method, despite the low capacity and the strong denaturation imposed by non-specific adsorption. A screen against coated β-actin led to the identification of 16 unique binders positive in phage ELISA. Seven of these antibodies decorated endogenous actin stress fibers by immunofluorescence in MRC5 cells (Figure 2D) as well as in other cell lines. Treatment of cells with cytochalasin D disorganizes actin fibers. Accordingly, staining with the hs2dAb was strongly altered (Figure 2—figure supplement 1B). Three of the hs2dAb detected a single band at the molecular weight of β-actin in western blot from HeLa cell extract while one of the anti-tubulin detected a band at the correct molecular weight of tubulin (Figure 2—figure supplement 1C).

Actin and tubulin are strongly expressed cellular proteins. Another screen was thus performed to select binders directed against proteins expressed at a lower level. A first screen was carried out against the tumor suppressor p53 protein. The 83 first amino acids of the NP_000537.3 isoform were produced in bacteria fused to a SNAP tag, biotinylated in vitro and used as a target in the phage display selection. Among 12 clones positive in phage ELISA, 6 selected hs2dAb were shown to label endogenous p53 in immunofluorescence on A431 cells (Figure 2E). The specificity of the staining was confirmed using RPE-1 cells (Figure 2—figure supplement 2). A low nuclear staining was observed in normal conditions, with some variability between cells. As expected, the intensity was enhanced upon UV-induced DNA damage. Such an increase was not observed in a RPE-1 cell line stably expressing an shRNA against p53. A second screen was carried out against the heterochromatin protein HP1α. HP1α was produced in bacteria fused to an avitag to obtain a biotinylated recombinant protein. Biot-HP1α was then immobilized on streptavidin beads and used as a target for 3 rounds of selection. 5 individual hs2dAb were directly identified by immunofluorescence staining of HeLa cells. Figure 2F shows that selected antibodies were efficiently staining endogenous HP1 in the nucleus. Overexpression of the different HP1 variant followed by western blot and immunofluorescence analysis actually suggested that HP1β/γ were also detected by the antibody (Figure 2—figure supplement 3). Together these results showed that the NaLi-H1 synthetic library can be screened in various conditions against very different purified targets while leading to the rapid identification of diverse and specific binders that can be used in classical antibody-based staining methods.

### Selection of conformation-sensitive antibodies

One of the main advantages of full in vitro immunization using display technologies is the control of antigen conformation and concentration. It allows to drive selection towards the desired outcome. For example, selection schemes can be devised to improve the recovery of high affinity binders endowed with low off-rate kinetics (Lee et al., 2007), to target specific epitopes (Even-Desrumeaux et al., 2014; Vielemeyer et al., 2009), or to identify conformation sensitive-binders (Haque et al., 2011). Recombinant antibody fragment library screening have, for example, provided several binders targeting selectively the active conformation of GTP binding proteins (Dimitrov et al., 2008; Nizak et al., 2003a; Tanaka et al., 2007). We hypothesized that the NaLi-H1 synthetic library had enough diversity and functionality to enable the identification of selective conformational binders. A subtractive panning was performed to select conformation-specific antibodies directed against small GTPases from the RHO subfamily (Chinestra et al., 2012). Small GTPases are molecular switch that cycle between an inactive and an active state when bound to GDP or GTP nucleotides, respectively. Mutant of small GTPases can be designed that adopt stably an active or inactive conformation. A constitutively active (CA) mutant RHOA L63 was expressed in HEK293 as a bait then freshly pulled down for panning to preserve its native conformation. To enrich in phage specific for GTP-bound RHOA, a depletion step was introduced from the second round of panning using GDP-bound RHO proteins. After four rounds of selection, clones were analyzed using phage ELISA against either wild type RHOA loaded with GTPγS (a non-hydrolysable analogue of GTP) or GDP-loaded RHOA. Forty clones presenting a differential ELISA signal in favor of the GTP loaded RHOA were sequenced. One antibody, represented by clone H12, represented more than 50% of the population. We analyzed H12 binding specificity by ELISA on several purified RHO proteins expressed as GST fusion in E.coli. H12 recognized the constitutively active mutant RHOA L63 (RHOA-CA) which is bound to GTP due to impaired hydrolysis activity. A similar signal was obtained with wild type RHOA loaded with the non-hydrolysable GTP analogue GTPγS. In contrast, no binding was observed to the dominant negative RHOA N19 mutant RHOA-DN nor to GDP-loaded wild type RHOA (Figure 3A). The capacity of H12 to specifically immunoprecipitate GTP-loaded RHOA from mammalian cell extracts was then evaluated in comparison to the standard method to assay RHO activity (Ren et al., 1999). This pull down method is based on the RHO binding domain of Rhotekin fused to GST (GST-RBD) which is known to bind to the active conformation of RHO GTPase. The hs2dAb H12 bearing a carboxy-terminal CBD (Chitin-Binding Domain) was expressed in E. coli and immobilized on chitin beads. These beads were then incubated with HeLa cell extracts pre-treated with either GTPγS or GDP to load small GTPases with the respective nucleotide. The H12 hs2dAb was found to be highly selective of RHO loaded with GTPγS as it was unable to precipitate RHO from GDP loaded extract (Figure 3B). A similarly strong conformation-specificity was found when using H12 for immunofluorescence staining (Figure 3C). HeLa cells expressing the GFP-RHOA constitutively active mutant carrying the mutation Q63L (GFP-RHOA CA) or the dominant negative mutated T19N (GFP-RHOA DN), were fixed and stained with H12 hs2dAb. Expression of the dominant negative mutant GFP-RHOA DN, did not lead to an increased signal over the background of un-transfected cells. In contrast, a staining with H12 was correlated with the level of GFP-RHOA CA mutant expression. Note that the signal does not fully overlap GFP fluorescence and appeared stronger at the cell border and in large zone where cell shape is strongly retracted by large bundled actin stress fibers induced by a sustained activation of the RHOA/ROCK pathway (Mayer et al., 1999). This CA mutant, like active mutant of many small GTPases related to RAS still need to be activated by guanine nucleotide exchange factors to be loaded with GTP and display the active conformation. Thus, we believe that the H12 staining revealed the active form of this mutant in cells (Figure 3C). All together, these results demonstrated that the H12 hs2dAb is selective for RHO GTPases in their active conformation, highlighting the performance and diversity of the NaLi-H1 library.

![Figure 3.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig3-v2.jpg)

**Figure 3.:** (A–C) H12 is a conformational hs2dAb binding only to the GTP bound, activated state, of the RHOA GTPase: (A) ELISA using the H12 or anti-GST antibodies to reveal recombinant GST-RHOA wild type proteins loaded with either 100 µM GTP gamma S (Black) or 1 mM GDP (White), or constitutively active mutant proteins GST-RHOA Q63L (Grey). Means ± SEM. (B) A CBD tagged H12 pull down from HeLa cell extract loaded with100 µM GTP gamma S (GTP) or with 1 mM GDP as inputs. Western blot reveals RHOA at a similar level in 5% of both input but only on the GTP loaded extract in the CBD-H12 pull down. D5 anti tubulin was used as a negative control and the standard GST-RBD (RHO binding domain of Rhotekin) as a positive control of active RHO pull down. (C) Immunofluorescence on HeLa cells overexpressing GFP-RHOA CA (constitutively active) mutant or GFP-RHOA DN dominant negative mutant. H12 staining detected using a myc tag antibody revealed only cells overexpressing the constitutively active mutant with a pattern stronger at the cell periphery were RHOA activation is high. (D) Tumor cell surface subtractive selection scheme. (E) ELISA of hs2dAb F7 anti-HER2 on HER2 fused with a rabbit Fc versus binding on rabbit Fc at equimolar concentration. (F) hs2dAb F7 anti-HER2 decorated the SKBR3 membrane in immunofluorescence. SKBR3 cells were fixed with 3% paraformaldehyde and stained with F7 revealed by an anti-HisTag (Sigma) and an anti-MouseCy3 secondary antibody (Jackson). (G) FACS analysis of F7 anti-HER2 on SKBR3 HER2 positive cells versus MCF10A HER2 negative cells. (Scale bar = 10 µm).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig3-figsupp1-v2.jpg)

### Direct selection against cell surface antigens

The use of antibodies to target cells involved in pathologies like cancers or viral infection is one of the most promising therapeutic approach. Antibodies also represent a unique tool to identify novel targets at the cell surface. Using synthetic libraries like the NaLi-H1 library to carry out direct selection against the cell surface of tumor cells would strongly accelerate the identification of specific antigens while allowing extended control over the conditions of selection. A subtractive selection scheme was set up to identify antibodies selectively detecting the surface of breast tumor cells: phages displaying hs2dAbs were first depleted against a reference cell line before being selected against the target one (Figure 3D). As a target cell line, we used the SKBR3 line, which is known to overexpress the HER2 cell surface protein, while the MCF7 cell line, negative for HER2, was used to pre-adsorb the library. After the third round of bio-panning, 88 clones were analyzed by FACS and 58 were found to be positive when tested on SKBR3 cells and negative on MCF7 cells. Sequencing the 58 positive clones revealed that 15 independent binders had been selected. Although the subtractive selection was not performed on identical cell lines expressing or not HER2, we observed strikingly that 12 clones out of 15 recognized HER2 exoplasmic domain by ELISA using HER2-Fc as a target antigen (Figure 3E), suggesting that it behaves as a dominant differential epitope. As shown in Figure 4, these antibodies efficiently detected HER2 at the cell surface by immunofluorescence (Figure 3F) or by FACS (Figure 3G). These experiments demonstrated that the NaLi-H1 library will represent a unique tool to discover, in a rapid and cost effective manner, specific antibodies detecting antigens present at the surface of pathological cells. These antibodies may then be used to identify the corresponding target.

![Figure 4.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig4-v2.jpg)

**Figure 4.:** Intracellular expression of hs2dAb. (A) (top panel) HeLa cells were co-transfected with GFP-Rab6 and a hs2dAb-mCherry anti-EGFP plasmids. The hs2dAb mCherry anti-EGFP colocalized perfectly with the Rab6 Golgi staining. (bottom panel) HeLa cells were co-transfected with Myr-palm-mCherry and a VHH-EGFP anti-mCherry plasmids. The VHH-EGFP anti-mCherry interacted with its target in vivo and colocalized perfectly with the mCherry staining at the plasma membrane. (B) SKBR3 cells were transfected with an anti-p53 hs2dAb-mCherry alone (top panel), or together with full length p53-EGFP which concentrated the hs2dAb into the nucleus (bottom panel). (C) GFP, used as a control (top panel) or a GFP-tagged anti-HP1 hs2dAb (bottom panel) were transiently expressed in HeLa cells (green). In contrast to the GFP control, the GFP-tagged anti-HP1 strongly accumulated in the nucleus where it labeled nuclear condensations. (Scale bar = 10 µm)

### hs2dAbs as intracellular antibodies

Various antibody fragments have long been proposed to represent powerful tools when expressed in cells as intrabodies. Although several studies indeed report efficient use of intrabodies (reviewed in [Kaiser et al., 2014; Lobato and Rabbitts, 2003; Stocks, 2005]), this is limited to antibody scaffolds that resist to the reducing environment of the cytosol. We evaluated the use of the hs2dAb scaffold to develop intrabodies. Randomly chosen hs2dAbs were fused to a fluorescent protein and observed in living cells. In comparison to our previous experience with scFv or nanobody libraries in which a majority of tested antibodies showed aggregation when expressed in the cytosol as an EGFP-fusion, most of the hs2dAbs tested here gave a monodispersed fluorescence, and very few were showing aggregates. Monodispersed fluorescence of the EGFP has been proposed to be a convenient indicator of stability and potential use as intrabody (Guglielmi et al., 2011). Several hs2dAb directed against actin, tubulin, EGFP or p53 were tested for their ability to trace intracellular antigens in living cells. None of the anti-tubulin or anti-actin antibodies tested were found localized on microtubule or microfilament, respectively, in living cells. We reasoned that this poor efficiency may be linked to the antigen denaturating conditions used during the selection of antibodies directed against actin. The existence of a large pool of unpolymerized actin and tubulin may also prevent efficient recruitment on the polymers. In contrast, several anti-GFP and anti-mCherry hs2dAbs were found to efficiently label their targets, like for example GFP-Rab6 or Myr-Palm-mCherry fusion proteins, in living cells (Figure 4A). Similarly, the anti-p53 hs2dAb fused to mCherry were clearly accumulated in the nucleus of SKBR3 cells where endogenous p53 is also localized. This signal was enhanced in cells overexpressing p53-EGFP (Figure 4B). This further confirmed the binding specificity of the hs2dAb anti-p53 while expressed in the reducing cytosol. Effective intrabodies were also obtained against HP1. Figure 4C (lower panel) shows that anti-HP1 expressed as an EGFP tagged protein in HeLa cells localized in the nucleus where it labels condensed structures similar to HP1 usual staining. In contrast, a diffuse cytoplasmic and nuclear staining was obtained using non relevant hs2dAbs fused to EGFP (Figure 4C, upper panel).

These results indicate that functional intrabodies can be obtained at high frequency using the NaLi-H1 library. Intrabodies can be used, upon fusion with a fluorescent protein, to track the dynamics of their target in living cells (see for example Nizak et al., 2003a). Such an application is illustrated in the Video 1 where an hs2dAb directed against mCherry is used to track mCherry-fused Rab6 in living cells. Intrabodies may allow not only to track the dynamics of their cellular target, but also to perturb, or block, their activity. Our results indeed indicate that the H12 antibody was able to perturb endogenous RHO activity when expressed in the cytosol. We could not directly image enrichment of the H12 antibodies in cellular sub-domains in living cells but we observed that H12 may behave as an efficient intrabody carrying out co-immunoprecipitation experiments. H12 carrying a carboxy-terminal myc tag was expressed in HeLa cells together with either the CBD-fused RHOA DN or with the CBD-RHOA CA mutants. H12 was pulled-down by RHOA CA but not by inactive RHOA DN (Figure 5—figure supplement 1). H12 thus worked as an intrabody and kept its conformation sensitivity in the cytosol. Because RHO GTPases are involved in signaling pathways that promotes the actin cytoskeleton polymerization, we looked at functional effects induced by H12 overexpression. In contrast to un-transfected cells or cells transfected with various non-relevant EGFP fused hs2dAb (Figure 5A, upper panel), we observed that cells expressing H12-EGFP were totally devoid of actin stress fibers (Figure 5A, lower panel). This alteration in actin filament organization was associated with marked changed in cell shape characteristic of loss of intracellular mechanical forces and tension. As RHOA plays a major role in activating myosin II and actin cytoskeleton reorganization, our results suggested that H12 efficiently perturbed RHO-dependent signaling, mimicking the phenotype induced by the C3 exoenzyme RHO inhibitor (Ridley and Hall, 1992).

![Video 1.](https://cdn.elifesciences.org/articles/16228/elife-16228-media1.mp4.jpg)

![Figure 5.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig5-v2.jpg)

**Figure 5.:** (A) HeLa cells expressing transiently a EGFP-tagged non relevant hs2dAB (top panel) or EGFP-H12 anti RHO-GTP (bottom panel) were fixed 20 hr post transfection and stained using DAPI and Alexa 594 phalloidin to detect actin stress fibers. The H12 hs2dAb induced actin stress fibers disappearance and major cell shape change (see cells outlined with a dotted line) (B) Protein knockdown of H2B-EGFP mediated by functionalized inhibitory antibodies. HeLa S3 cell stably expressing histone H2B-EGFP were transfected with vectors expressing antibodies fused to an F-box (F-Ib) to induce degradation of the targeted cellular antigen. The F-GFP4 VHH (DegradFP) was used as a positive control (top panel) and a non-relevant hs2dAb as a negative control (bottom panel). F-Ib were expressed using a bi-cistronic vector driving the co-expression of mitochondrial targeted mCherry. Protein interference is analyzed in cells displaying mCherry positive mitochondria (mitoCherry channel). Efficient protein knockdown is obtained using the R3TF3 anti-EGFP intrabody. Note that not all nanobodies can be used as F-Ib because R3TG4 does not induce protein degradation. (Scale bars = 20 µm) (C) Fluorescence decay measurement of the protein interference assay was quantified by flow cytometry (10000 cells analyzed, from 3 independent replicates). GFP fluorescence intensity was quantified in the transfected and the untransfected subpopulations for each F-Ib. The ratio of each median of fluorescence (transfected versus untransfected population) was calculated as a percentage of GFP fluorescence intensity for one F-Ib. A strong decrease in fluorescence corresponding to protein knockdown was observed with F-GFP4 VHH and F-R3TF3 hs2dAb intrabodies while the non-relevant negative control and R3TG4 did not induce a decrease of fluorescence. (D) Cells were analyzed as in C but the cells were incubated in 1 µM MG132 or DMSO for 44 hr after transfection by the different F-Ib and fluorescence intensity was normalized using the non-relevant control. Protein knockdown was inhibited by MG132.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** HeLa cells were co-transfected for 24 hr with the anti RHO hs2dAb H12 fused to carboxy-terminal myc tag (H12-myc) or a non relevant control (NR-myc) that was a negative clone in a panning against FITC together with chitin binding domain (CBD) fusion of either the dominant negative mutant RHOA-N19 (DN) or the constitutively active mutant RHOA-L63 locked in the GTP bound state (CA). Chitin beads pull down of CBD-RHOA-DN or CBD-RHOA-CA revealed the selective co-precipitation of H12-myc together with the RHO active mutant. The total level of CBD-RHOA or hs2dAb-myc proteins was revealed by loading 5% of the respective input. CBD-RHOA proteins were detected with anti CBD tag and the hs2dAb antibodies with an anti-myc tag antibody.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Model for F-Ib degradation by fusing Fbox domain to the VHH GFP4 inducing GFP target protein ubiquitiation followed by proteasome-dependent degradation of the target protein. (B) Schematic illustration of the bicistronic vectors: an Fbox or NoFbox domain, respectively, is fused to the N terminal part of hs2dAb and a transfection marker MTS-mCherry, labeling mitochondria in red, is co-expressed using an Internal Ribosome Entry Site (IRES). (C) Fluorescence visualization HeLa S3 cells stably expressing H2B-GFP and transfected with NoF-VHH GFP4 or F-VHH GFP4. Degradation by the degradFP was observed in cells expressing F-VHH GFP4. Scale bar = 10 µm (D) Western blot quantification of protein knockdown mediated by F-GFP4. (E) Quantification of GFP fluorescence by flow cytometry in MTS Cherry positive cells.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig5-figsupp3-v2.jpg)

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig5-figsupp4-v2.jpg)

Identification of blocking antibodies is a challenging task and not all functional intrabodies are inhibitory. However, it is possible to functionalize non-blocking intrabodies to inhibit their target function. One approach relies on the ubiquitinylation and degradation of the recognized target as described by Caussinus et al. (2011). This approach is based on the fusion of intrabodies to an F-box domain which allows interaction with Skip1, a member of the SCF complex, an E3 ubiquitin ligase of the complex E1/E2/E3 ubiquitinylation machinery, that targets proteins to proteasome-dependent cellular degradation (Caussinus et al., 2011) (Figure 5—figure supplement 2). This approach was efficiently developed to target several EGFP fusion proteins in Drosophila using a single anti EGFP intrabody, named GFP4, which is a robust and high affinity EGFP llama intrabody originally isolated from an immune library (Rothbauer et al., 2006). To get insight into the relative functionality of hs2dAb for such a protein interference approach, several of the anti EGFP hs2dAb selected from the NaLi-H1 library were fused at their amino terminus to the Fbox domain and their efficacy was compared to the efficacy of the Fbox-GFP4 nanobody. To detect cells expressing Fbox-intrabody fusion proteins (F-Ib), we constructed a bicistronic vector driving the co-expression of F-Ib together with a mitochondria-targeted mCherry (Mito-mCherry) (Figure 5B). We expressed the F-Ib antibodies in a HeLa clone stably expressing EGFP fused to histone H2B (Silljé et al., 2006) and looked for EGFP-H2B depletion. As expected, F-GFP4, also known as degradFP, induced a strong reduction of H2B-EGFP expression as analyzed by western blot (Figure 5—figure supplement 2). Accordingly, a strong reduction in nuclear fluorescence intensity was observed in cells expressing F-GFP4 (see mito-mCherry positive cells, Figure 5B; Figure 5—figure supplement 2). No effect was observed when expressing either GFP4 alone or a GFP4 fused to a truncated, nonfunctional, Fbox domain (Figure 5—figure supplement 2). When anti-EGFP clones selected from the NaLi-H1 library were tested, we observed that some of the hs2dAb that were found to active as fluorescent intrabodies failed to degrade H2B-EGFP when expressed as F-Ib. This highlights the fact that not all intrabodies can efficiently be functionalized with the F-box and that in vivo binding to a target is not the only parameter to consider. However, several hs2dAb anti-EGFP induced a complete disappearance of nuclear H2B-EGFP signal when expressed as F-Ib (F-R3TF3, Figure 5B) while no reduction was observed when using an anti-EGFP that cannot be used as an intrabody (F-R3TG4, Figure 5B). FACS analysis showed a decreased of fluorescence intensity by as much as 70% (Figure 5C). As expected, this effect was reversed in the presence of a proteasome inhibitor (Figure 5D). Altogether, these experiments show that the hs2dAb scaffold enables the frequent selection of antibodies that can be expressed in the mammalian cell cytoplasm to be used as functional fluorescent or inhibitory intrabodies.

## Discussion

Here, we report the construction of the first large fully synthetic single domain antibody library based on a humanized scaffold derived from llama VHH. A set of robust nanobody scaffolds was first identified using a positive expression screening in E. coli cytosol. One very robust scaffold (sdAbD10) was identified and was used as a base. After introduction of several modifications that aimed at humanizing its primary sequence, we designed the hs2dAb scaffold which is as stable as sdAbD10 while being closer to human VH3. Our data indicate that the hs2dAb displays partial resistance and/or refolding after treatment for 10 min at 90°C. Using CDR grafting experiments we confirmed the efficacy and the stability of the synthetic scaffold to display CDR regions. Based on our prior experience on phage display libraries, immune or naïve llama VHH libraries (Monegal et al., 2012; Olichon and Surrey, 2007) or from scFv libraries (Dimitrov et al., 2008; Goffinet et al., 2008; Nizak et al., 2003a) we then rationally designed CDR diversity with fixed CDR1 and CDR2 size and four CDR3 sizes (9, 12, 15 or and 18 amino acids). The power of modern gene synthesis approach permits to reach very high genetic diversity while controlling codon bias and cloning features. Fully random codon combination using NNN or NNK trinucleotide cannot prevent stop codon, undesired cysteine or hydrophobic residues to be incorporated, and it does not lead to the controlled probability of amino acid occurrence at a given position. Therefore a more rational design was implemented with defined set of codons for each CDR amino acid position so that it does not mimic natural diversity, in contrast to recently developed Fab synthetic libraries (Prassler et al., 2011; Zhai et al., 2011), but is rather optimized for intrinsic hydrophilicity or solubility. After a large-scale cloning of synthetic fragments, 3 billion independent clones were transformed in the bacteria. Library quality was confirmed by Sanger and next generation sequencing.

The library was validated by screening against various targets and in each case specific and highly functional antibodies were obtained (Table 1). Various selection schemes yielded a large diversity of high affinity and high selectivity binders. Selections were carried out using purified antigen coated on polystyrene, on magnetic beads or directly on the cell surface. In many cases, two rounds of selection were sufficient to obtain selective binders. We usually analyzed only 80 randomly picked clones because the diversity of specific binders was systemically high. Only a few selections led to antibodies usable in western blotting (anti-actin, ant-tubulin) probably because most screenings were done using natively folded targets. Accordingly, selected hs2dAb performed very well in other conventional immunoassays like ELISA, FACS, immunoprecipitation or immunofluorescence. Affinity measurements done by surface plasmon resonance revealed KD values in the order of 10 nanomolar and up to 50 picomolar. Such high affinities are rather good and usually rarely observed for monovalent binders obtained without in vivo immunization or in vitro affinity maturation steps (Figure 6; Table 2).

**Table 1.**
 Summary of screenings showing the number of unique clones giving positive signal. (ND means non determined)


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="3">Positive clones</th>
      <th></th>
    </tr>
    <tr>
      <th>Antigen</th>
      <th>Phage ELISA</th>
      <th>IF/FACS</th>
      <th>Intrabody</th>
      <th>Rounds of panning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GFP</td>
      <td>37</td>
      <td>10/ND</td>
      <td>4/10</td>
      <td>2</td>
    </tr>
    <tr>
      <td>mCherry</td>
      <td>ND</td>
      <td>6/ND</td>
      <td>2/6</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Tubulin</td>
      <td>ND</td>
      <td>3/ND</td>
      <td>0/3</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Actin</td>
      <td>16</td>
      <td>7/ND</td>
      <td>1/7</td>
      <td>3</td>
    </tr>
    <tr>
      <td>p53</td>
      <td>12</td>
      <td>6/ND</td>
      <td>2/6</td>
      <td>2</td>
    </tr>
    <tr>
      <td>RHOA-GTP</td>
      <td>24</td>
      <td>8/ND</td>
      <td>3/8</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Her2</td>
      <td>6</td>
      <td>5/10</td>
      <td>ND</td>
      <td>3</td>
    </tr>
  </tbody>
</table>

![Figure 6.](https://cdn.elifesciences.org/articles/16228/elife-16228-fig6-v2.jpg)

**Figure 6.:** Single cycle kinetics analysis was simultaneously performed on immobilized His fusion VHH antibodies (250–300 RU), with five injections of analytes (EGFP, HER2, RHOAQ63L and mCherry) at 3.125 nM, 6.25 nM, 12.5 nM, 25 nM, and 50 nM. Analytes injections lasted for 120 s each and were separated by 10 s dissociation phases. At this time of buffer exchange, a slight refraction index discrepancy between the sample and the flow buffer can induce a drop in resonance unit. This common bulk effect, which is clearly visible on sensorgrams with a smaller scale range on the RU axis (ie: R3SE4, R2TB5), does not affect the measurement of off-rate constant. Off-rate constant was calculated from an extended dissociation period of 10 min following the last injection according to the single cycle kinetics method. Each sensorgram (expressed in RUs as a function of time in seconds) represents a differential response where the response on an empty reference channel (Fc1) was subtracted. The red curves correspond to the data and the black curves represent the fit done by the BIAevaluation software. Note that the fitted curve is almost identical to the data curve in some cases like for example the RHOA Q63L or the HER2 binding measurement.

**Table 2.**
 Binding affinities of 9 selected hs2dAb fused to a 6HIS tag measured by surface plasmon resonance single cycle kinetics method. Dissociation equilibrium constant KD corresponds to the ratio between off-rate and on-rate kinetic constant Koff/Kon. Non relevant hs2dAb were used as negative controls and gave no detectable binding signal. A positive control endowed with subnanomolar affinity, the GFP binder VHH-GFP4, was analyzed in parallel to the GFP hs2dAbs. A KD of 1.55–10 M was measured for VHH-GFP4 which is similar to published values. The binding properties of the conformational H12 hs2dAb to the GTP loaded RHOA subfamily were measured using the L63 or L61 constitutively active mutants of RHO, RHOB, RHOC, RAC1 and CDC42 related small GTPases, as well as the negative mutant T19N of RHOA. ('no' means no detectable binding).


<table>
  <thead>
    <tr>
      <th>hs2dAb-6xHis</th>
      <th>Antigen</th>
      <th>kon (M−1 s−1)</th>
      <th>koff (s−1)</th>
      <th>KD(M)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>R2TB5 anti-GFP</td>
      <td>GFP</td>
      <td>1.24 10+6</td>
      <td>3.05 10−4</td>
      <td>2.45 10−10</td>
    </tr>
    <tr>
      <td>R3SD1 anti-GFP</td>
      <td>GFP</td>
      <td>7.07 10+5</td>
      <td>6.68 10−4</td>
      <td>9.44 10−10</td>
    </tr>
    <tr>
      <td>R3SE4 anti-GFP</td>
      <td>GFP</td>
      <td>1.45 10+5</td>
      <td>5.83 10−4</td>
      <td>4.01 10−9</td>
    </tr>
    <tr>
      <td>Llama VHH GFP4</td>
      <td>GFP</td>
      <td>2.99 10+5</td>
      <td>4.65 10−5</td>
      <td>1.55 10−10</td>
    </tr>
    <tr>
      <td>D4 anti-Her2</td>
      <td>Her2</td>
      <td>1.79 10+5</td>
      <td>1.63 10−4</td>
      <td>9.11 10−10</td>
    </tr>
    <tr>
      <td>A10 anti-Her2</td>
      <td>Her2</td>
      <td>1.66 10+4</td>
      <td>4.88 10−5</td>
      <td>2.94 10−9</td>
    </tr>
    <tr>
      <td>B9 anti-Cherry</td>
      <td>mCherry</td>
      <td>6.14 10+4</td>
      <td>1.68 10−4</td>
      <td>2.74 10−9</td>
    </tr>
    <tr>
      <td>E4 anti-Cherry</td>
      <td>mCherry</td>
      <td>6.57 10+4</td>
      <td>2.03 10−4</td>
      <td>3.10 10−9</td>
    </tr>
    <tr>
      <td>B3 anti-Cherry</td>
      <td>mCherry</td>
      <td>6.19 10+4</td>
      <td>2.71 10−4</td>
      <td>4.38 10−9</td>
    </tr>
    <tr>
      <td>H12 anti-RHO.GTP</td>
      <td>RHOA Q63L</td>
      <td>4.81 10+5</td>
      <td>1.28−4</td>
      <td>2.65 10−10</td>
    </tr>
    <tr>
      <td>H12 anti-RHO.GTP</td>
      <td>RHOB Q63L</td>
      <td>2.24 10+5</td>
      <td>3.59−4</td>
      <td>1.57 10−9</td>
    </tr>
    <tr>
      <td>H12 anti-RHO.GTP</td>
      <td>RHOC Q63L</td>
      <td>1.12 10+6</td>
      <td>5.41−5</td>
      <td>4.79 10−11</td>
    </tr>
    <tr>
      <td>H12 anti-RHO.GTP</td>
      <td>RHOA T19N</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
    <tr>
      <td>H12 anti-RHO.GTP</td>
      <td>RAC1 Q61L</td>
      <td>7.53 10+5</td>
      <td>2.55−4</td>
      <td>3.3 10−10</td>
    </tr>
    <tr>
      <td>H12 anti-RHO.GTP</td>
      <td>CDC42 Q61L</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
    </tr>
  </tbody>
</table>

The NaLi-H1 library thus enables the rapid selection of diverse and highly functional binders. Because it is a fully synthetic, non immune, library, it does not depend on animal experimentation, it is not limited by natural immunogenicity or toxicity of antigens and allows to develop and adjust the selection without ethic consideration. In addition, because all steps are carried out in vitro, conditions can be tightly controlled. This allowed to develop powerful differential selection and to identify conformation-specific antibodies. This also allowed to directly screen for antibodies directed against antigens specifically present at the surface of a particular cell type. Such a differential selection will be a powerful approach to identify novel antigen at the surface of tumor or infected cells. Such antibodies may also represent powerful tools for diagnostic and therapeutic applications to target cells in human pathologies. For example, after dimerization using Fc domains, hs2dAb antibodies may be used to target tumor cells and benefit from antibody-dependent cell-mediated cytotoxicity (ADCC) for example. They may also be used directly as the smallest antibody-derived domain naked as an agonist or antagonist or armed for enhanced toxicity. Similarly, it may be labeled using radioactive compounds (e.g. 99mTc, 111In, 64Cu) and used to image tumors in patient using positron emission tomography. Altogether, he NaLi-H1 library may accelerate the identification of novel potent tools to be used in human clinical applications.

The synthetic scaffold we defined was based on the selection of a set of VHH able to fold properly in the bacteria cytosol. The goal was not only to define a robust scaffold that would be efficiently produced without aggregation but also to allow frequent selection of functional intrabodies. Intrabodies have been isolated from various antibody libraries (Nizak et al., 2003a; Rothbauer et al., 2006; Tanaka and Rabbitts, 2010; Vercruysse et al., 2010) as well as other protein scaffold like Darpin (Tamaskovic et al., 2012) or FN3 (Koide et al., 2012) which are devoid of cysteine. A peculiar feature of the NaLi-H1 library is that it is based on a humanized nanobody-like robust scaffold, stable in a reducing environment, while it still contains the two canonical cysteine residues. Stabilized nanobodies, human single domain scaffolds (Christ et al., 2007; Saerens et al., 2005) and libraries (Goldman et al., 2006; Mandrup et al., 2013) were reported before. However, to our knowledge, no synthetic library producing at high frequency functional intrabodies was developed before based on such stabilized scaffolds. Almost every hs2dAb antibodies we expressed in mammalian cytosol showed no sign of aggregation, which further supported the idea that the synthetic scaffold we designed is robust and highly resistant to reduction. Previous studies showed that functional intrabody identification often relied on additional steps of selection in a protein–protein interaction reporter system such as PCA (Koch et al., 2006) or bacterial 2 hybrid (Pellis et al., 2012), yeast IACT (Tanaka and Rabbitts, 2010) or F2H assays (Zolghadr et al., 2008). Using the NaLi-H1 library, we observed that without using particular selection schemes, functional intrabodies were frequently obtained. Although we did not formally compare the NaLi-H1 library to previous llama naïve or semi synthetic libraries, the functionality of selected hs2dAb was compared to a sub-nanomolar affinity intrabody, the GFP4 nanobody, which has been extensively used (Caussinus et al., 2011; Kirchhofer et al., 2010). We observed by monitoring its signal-to-noise ratio and by using it in a protein knockdown assay that NaLi-H1 can provide highly functional hs2dAb which appeared as good as intrabodies from immune libraries.

Intrabodies can be used in several applications like tracking of intracellular dynamics of endogenous proteins (Nizak et al., 2003a, 2003b; Rothbauer et al., 2006) but the most appealing application is to use them for rapid protein inactivation in living cells. Intrabodies may be used to directly block their target proteins in cells. One of the conformation-sensitive antibody that was selected can be used to inhibit active RHO GTPase signaling in living cells and is as potent as the C3 exoenzyme toxin. Only few intrabodies have been described to be intrinsically inhibitors of protein activity (Haque et al., 2011; Vercruysse et al., 2010), and our results suggest that the NaLi-H1 library may enable rapid selection of inhibitory antibodies. The next challenge will be to select conformational sensors specifically directed against a particular member of closely related RHO subtypes (RHOA/B/C) which share more than 90% similarity in primary sequence. But in any case, our results show that the NaLi-H1 library allows the selection of efficient, conformation-specific, inhibitory intrabodies.

Another way intrabodies may be used to inactivate their targets in living cells is to fuse the intrabody to a dominant inhibitory domain. Following an idea pioneered by Affolter and colleagues (Caussinus et al., 2011), we showed here that intrabodies selected from the NaLi-H1 library can be fused to a proteasome-targeting domain to impose the specific degradation of their respective targets. This protein interference approach was validated using anti-EGFP hs2dAb and we believe that this approach will bring disruptive tools to generate rapid protein knockdown both in cell culture and in the animal.

In summary, we have designed a novel nanobody scaffold endowed with improved stability and created a highly diverse library, the NaLi-H1 library, that was successfully screened to identify highly functional binders directed against very diverse targets. We believe that this library will allow the fast, and fully in vitro, identification of immunological tools usable both for fundamental and medical applications.

## Materials and methods

### Plasmids and cloning

Artificial gene synthesis (Mr Gene, GmbH, Germany) composed of a 6His-Tag and a triple c-myc Tag was inserted into the pHEN2 phagemid vector (Griffin 1. library) between NotI and BamHI sites. CcdB gene from pENTR4 vector (Invitrogen - ThermoFisher Scientific, France) was inserted into the pHEN2 vector between NcoI and NotI sites. This vector allows to express antibody fragments in fusion, upstream, with the pelB leader to drive secretion in the periplasm and downstream with the PIII protein of M13 phages. An amber stop codon is present between the antibody and the pIII. This stop codon is partially suppressed in SupE E. coli. For expression and purification of dimeric antibodies, hs2dAb were inserted in vectors derived from pFuse (Invivogen, France) as described in Moutel et al. (2009). For intrabody expression in mammalian cells, hs2dAb were digested by NcoI and NotI and ligated into the pIb-mEGFP, pEGFP or the pmCherry vectors (Clontech - Takara, USA). (See the Appendix for more details).

### CAT filter assay

Previously selected VHHs from naïve or immune libraries were subcloned into pAOCAT (Monegal et al., 2012) using the NcoI and NotI restriction sites. Chloramphenicol resistance assay was performed using BL21 (DE3) cells transformed with the pAOCAT-VHH fusion constructs. (See the Appendix for more details).

### Library construction

Details about the construction of the library can be found in the Appendix. In short, a synthetic design was ordered based on a statistic analysis of the diversity found in natural VHH and aiming at reducing hydrophobicity at some position. The size of the CDR1 and CR2 was fixed at 7 amino acids while 4 sizes of CDR3 were chosen (9, 12, 15 and 18 amino acids). Large -scale PCR was then carried out ensuring that at least 1010 DNA molecules were used as a matrix. Fragments were then cut and inserted into the pHEN2-3myc plasmid. The ligated DNA material was used to transform electrocompetent E. coli TG1 cells (Lucigen Corp., Middleton, United States). Serial dilution was used to count the total number of bacteria transformed. A potential diversity of 3 × 109 was calculated. Transformed bacteria plated on 430 2xYT-ampicillin agar dishes (140 mm), grown overnight at 37°C, scrapped and stored in 30% of glycerol at −80°C.

### Ion torrent sequencing

IonTorrent sequencing library was prepared with the Ion Plus Fragment Library kit for AB Library Builder System (Life Technologies - TermoFisher Scientific, France) following manufacturer's instructions and was controlled on the Agilent 2100 Bioanalyzer (Agilent Technologies, France) with the High Sensitivity DNA Kit (Agilent Technologies). The sequencing template was prepared by emulsion PCR with the Ion OneTouch 2 system and the Ion PGM Template OT2 400 Kit (Life Technologies). Sequencing was performed on a IonTorrent Personal Genome Machine using the Ion PGM Sequencing 400 Kit and a 314v2 Ion chip (Life Technologies).

### Antigens

Human βActin was purchased from Sigma-Aldrich (France). RHOA GTPase fused to either an amino terminal Chitin Binding Domain or a streptactin binding peptide were produced in HEK293 cells. EGFP (as mCherry) in fusion with a streptavidine binding peptide (SBP) were produced through in vitro translation system (Roche Life Science, France) and used directly for screening without the need for purification.

Biotinylated Tubulin was purchased from Cytoskeleton, Inc. (Denver, United States). For p53, the 83 first amino acids of the NP_000537.3 isoform were produced in bacteria with a SNAP and His Tag, purified using Talon resin (Takara - Clontech) and biotinylated in vitro. HP1α was produced in bacteria with an avitag and a His Tag, and purified using Talon resin.

For HER2, the natural receptor was used as membrane protein target on SKBR3 cells.

For more details see the Appendix for more details.

### Phage display selections

Screening for ßactin was performed by panning in immunotubes as described (Marks et al., 1991).Screening for EGFP, Tubulin and p53 were performed in native condition as described (Nizak et al., 2005). Screening for HER2 was performed on surface cells as described (Even-Desrumeaux and Chames, 2012). Screening on RHO was performed in native condition. (See the Appendix for more details).

### Enzyme-linked immunosorbent assay (ELISA)

Individual clones were screened by monoclonal phage ELISA as described. (See the Appendix for more details).

### Western-blot

After boiling in SDS-PAGE loading buffer, the samples were separated on a 12% SDS-PAGE and transferred to nitrocellulose membranes (Whatman GmbH, Germany). Membranes were blocked in 3% non-fat milk-PBS with 0.2% Tween 20 for 1 hr at room temperature or overnight at 4°C. unpurified hs2dAb were used at 1/100 from culture supernatant and added to the membranes with an anti-hisTag antibody at 1/3000 (Sigma-Aldrich) for 90 min. Blots were then washed and incubated 1 hr with secondary anti-Mouse HRP labeled antibodies (diluted at 1/10000 in PBS 0.1% Tween 20) (Jakson ImmunoResearch Laboratories). After 5 washes with PBS 0.1% Tween 20, secondary antibodies were then revealed using the SuperSignal chemoluminescent reagent (Pierce) and Hyperfilm ECL (GE HealthCare). For RHO-GTP pull down, the primary anti RHOA mAb was used (Cell Signaling Technology; 1/1000). For protein knockdown experiments, 500 000 of transfected cells (mCherry positive cells) were sorted with a MoFlo Astrios flow cytometer (Beckman Coulter). Cells were lysed with SDS-Tris lysis buffer (Tris pH7.4 10 mM, SDS 1% supplemented with phosphatase and protease inhibitors). 20 µg of cell extracts were separated on 12.5% SDS-PAGE and electro transferred onto PVDF membranes. Blots were probed with a rabbit polyclonal anti-EGFP full length (Santa Cruz, sc-8334, 1:500), a mouse monoclonal anti-α-tubulin (Sigma, T5168, 1:25000) and an anti-myc HRP antibody (Novus Biologicals, NB600-341, 1:40000). Detection was performed using peroxydase conjugated secondary antibodies and Pierce ECL Western Blotting Substrate (Thermo Scientific Pierce).

### Immunofluorescence

Immunofluorescence screenings were performed on HeLa cells as described before (Nizak et al., 2005). (See the Appendix for more details).

### Transient transfection

Hela or HeLa S3 H2B-EGFP Cells cultured on coverslips were transfected according to the CaPO4 or jet prime procedure with 1 µg DNA per well (24 wells plate) or 10 µg DNA (10 cm2 diameter dish). Cells can be observed from 12 hr post-transfection on.

### Flow cytometry

For HER2 immunoassay, cell surface staining were performed in phosphate-buffered saline (PBS) supplemented with 1% SFV. 100 µL of supernatant (80 µL phages + 20 µL PBS/milk1%) were incubated on 1.105 cells for 1 hr on ice. Phage binding was detected by a 1:300 dilution of anti-M13 antibody (GE healthcare, France) for 1 hr on ice followed by a 1:1000 dilution of PE-conjugated anti-Mouse antibody (BD Bioscience, France) for 45 min. Samples were analyzed by flow cytometry on a FACSCalibur using CellQuest Pro software (BD Biosciences,France).

In the protein knockdown experiments, 48 hr after transfection, at least 10000 HeLa S3 H2B-GFP cells were analyzed on a MoFlo Astrios flow cytometer (Beckman Coulter France S.A.S) for their GFP fluorescence intensity. This fluorescence was analyzed in mCherry transfected cells and non transfected cells. Flow cytometry data were analyzed with Kaluza software (Beckman Coulter). 1 µM of proteasome inhibitor MG132 (Sigma-Aldrich) was used in the cell growth medium for 48 hr. Values reported represent median ± standard deviation (SD) of at least three independent experiments. p values were calculated with GraphPad Prism 6 (RRID:SCR_002798) using a Student’s t test. **p<0.01; ***p<0.001; ****p<0.0001.

### Affinity measurement

All binding studies based on SPR technology were performed on BIAcore T200 optical biosensor instrument (RRID:SCR_008424, GE Healthcare). Capture of single domain Hs2dAb-6xHis was performed on a nitrilotriacetic acid (NTA) sensorchip in HBS-P+ buffer (10 mM Hepes pH 7.4, 150 mM NaCl, and 0.05% surfactant P20) (GE Healthcare). The four flow cells (FC) of the sensorchip were used: one (FC 1) to monitor nonspecific binding and to provide background corrections for analyses and the other three flow cells (FC 2, 3, and 4) containing immobilized Hs2dAb-6xHis for measurement.

For immobilization strategies, the four flow cells were loaded with nickel solution (10 μL/min for 60 s) in order to saturate the NTA surface with Ni2+ and an extra wash using running buffer containing 3 mM EDTA after the nickel injection. Each His-tagged hs2dAb in running buffer was injected in flow cells at a flow-rate of 10 μL/min. The total amount of immobilized hs2dAb-6xHis was 250–300 resonance units. (RUs; 1 RU corresponds approximately to 1 pg/mm2 of protein on the sensor chip). A Single-Cycle Kinetics (SCK) analysis to determine association (on-rates), dissociation (off-rates) and affinity constants (kon, koff and KD respectively) was carried out. SCK method prevents potential inaccuracy due to sensorchip regeneration between cycles which are necessary in the conventional multiple cycle kinetics (MCK) (Trutnau, 2006). SCK binding parameters are evaluated for each injection according to the tools and fit models of the BIAevaluation software, giving similar values than MCK. As hs2dAb were smaller proteins than their respective antigens, hs2dAbs were captured on the sensorchip while the recombinant antigens were used as analytes. Analytes were injected sequentially with increased concentrations ranging between 3.125 nM to 50 nM in a single cycle without regeneration of the sensorship between injections. Binding parameters were obtained by fitting the overlaid sensorgrams with the 1:1. Langmuir binding model of the BIAevaluation software version 1.0.
